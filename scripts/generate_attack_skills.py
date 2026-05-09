#!/usr/bin/env python3
"""Generate Agent Skills for MITRE ATT&CK techniques from STIX bundles."""

from __future__ import annotations

import csv
import datetime as dt
import hashlib
import json
import re
import shutil
import subprocess
import textwrap
from pathlib import Path


WORKSPACE = Path("/home/user/workspace")
SOURCE_ROOT = WORKSPACE / "attack-stix-data"
OUT_ROOT = WORKSPACE / "mitre-attack-agent-skills"

DOMAINS = [
    ("enterprise", "ent", SOURCE_ROOT / "enterprise-attack" / "enterprise-attack.json", "mitre-attack"),
    ("mobile", "mob", SOURCE_ROOT / "mobile-attack" / "mobile-attack.json", "mitre-mobile-attack"),
    ("ics", "ics", SOURCE_ROOT / "ics-attack" / "ics-attack.json", "mitre-ics-attack"),
]


def slugify(value: str, max_len: int = 36) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    if len(value) <= max_len:
        return value or "technique"
    cut = value[:max_len].rstrip("-")
    return cut or "technique"


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'


def md_escape(value: str) -> str:
    return value.replace("|", "\\|")


def as_list(value) -> list[str]:
    if not value:
        return []
    if isinstance(value, list):
        return [str(v) for v in value if v]
    return [str(value)]


def get_external_ref(obj: dict, preferred_source: str) -> dict:
    refs = obj.get("external_references", [])
    for ref in refs:
        if ref.get("source_name") == preferred_source and ref.get("external_id"):
            return ref
    for ref in refs:
        if ref.get("external_id", "").startswith("T"):
            return ref
    return {}


def first_sentence(text: str, fallback: str, max_chars: int = 220) -> str:
    clean = re.sub(r"\s+", " ", text or "").strip()
    if not clean:
        clean = fallback
    match = re.search(r"(?<=[.!?])\s+", clean)
    sent = clean[: match.start()].strip() if match else clean
    if len(sent) > max_chars:
        sent = sent[: max_chars - 1].rstrip() + "…"
    return sent


def bullet_list(items: list[str], empty: str = "Not specified in the STIX object.") -> str:
    if not items:
        return f"- {empty}"
    return "\n".join(f"- {item}" for item in items)


def write_resource_files(
    skill_dir: Path,
    *,
    domain: str,
    external_id: str,
    name: str,
    url: str,
    obj: dict,
    tactics: list[str],
    platforms: list[str],
    permissions: list[str],
    data_sources: list[str],
    mitigations: list[str],
    used_by: list[str],
    detection: str,
) -> None:
    """Write per-skill scripts, references, templates, and assets/resources."""
    references_dir = skill_dir / "references"
    templates_dir = skill_dir / "templates"
    scripts_dir = skill_dir / "scripts"
    assets_dir = skill_dir / "assets"
    for d in (references_dir, templates_dir, scripts_dir, assets_dir):
        d.mkdir(parents=True, exist_ok=True)

    profile = {
        "domain": domain,
        "attack_id": external_id,
        "name": name,
        "type": "sub-technique" if obj.get("x_mitre_is_subtechnique") else "technique",
        "attack_url": url,
        "stix_id": obj.get("id", ""),
        "attack_version": obj.get("x_mitre_version", ""),
        "created": obj.get("created", ""),
        "modified": obj.get("modified", ""),
        "tactics": tactics,
        "platforms": platforms,
        "permissions_required": permissions,
        "effective_permissions": as_list(obj.get("x_mitre_effective_permissions")),
        "defenses_bypassed": as_list(obj.get("x_mitre_defense_bypassed")),
        "data_sources": data_sources,
        "mitigations": mitigations,
        "known_context": used_by,
        "detection": detection,
        "description": obj.get("description", "").strip(),
    }
    (references_dir / "technique-profile.json").write_text(json.dumps(profile, indent=2), encoding="utf-8")

    detection_ref = f"""# Detection and Mitigation Notes

## Technique

- ATT&CK ID: {external_id}
- Name: {name}
- Domain: {domain}
- Tactics: {", ".join(tactics) if tactics else "Not specified"}
- Platforms: {", ".join(platforms) if platforms else "Not specified"}

## ATT&CK detection guidance

{detection}

## Telemetry checklist

{bullet_list(data_sources)}

## Mitigation candidates

{bullet_list(mitigations, "No ATT&CK mitigation relationships were present in the source STIX bundle.")}

## Triage questions

- What asset, identity, workload, application, or control-plane component is in scope?
- Which observed events directly align with the ATT&CK behavior, and which are only circumstantial?
- What telemetry is missing, delayed, filtered, or known to be unreliable?
- Is this a single event, repeated pattern, campaign-level behavior, or expected administrative activity?
- What compensating controls should have prevented, detected, or limited the behavior?

## False-positive considerations

- Authorized administration, software deployment, security tooling, backup activity, and automated platform maintenance can resemble ATT&CK behavior.
- Before escalating, compare command lineage, account ownership, change tickets, destination reputation, asset criticality, and historical baselines.
"""
    (references_dir / "detection-and-mitigation.md").write_text(detection_ref, encoding="utf-8")

    procedures_ref = f"""# Known Threat Context

Use this file as a contextual lead list, not attribution evidence. ATT&CK relationships indicate that groups, campaigns, or software have been associated with this technique in ATT&CK data, but an observed event still requires independent evidence.

## Associated context from STIX relationships

{bullet_list(used_by, "No group, campaign, or software uses relationships were included for this technique in the source STIX bundle.")}

## Attribution caution

- Do not infer a threat actor from a technique match alone.
- Combine multiple independent signals, such as infrastructure, tooling, targeting, language artifacts, timing, malware families, and victimology.
- Prefer phrasing such as "consistent with" or "overlaps with" unless attribution is independently confirmed.
"""
    (references_dir / "known-threat-context.md").write_text(procedures_ref, encoding="utf-8")

    readme = f"""# Resources for {external_id}: {name}

This directory is a self-contained resource bundle for the `{external_id}` ATT&CK skill.

## Files

- `references/technique-profile.json`: structured ATT&CK metadata extracted from STIX.
- `references/detection-and-mitigation.md`: detection notes, telemetry checklist, triage questions, and mitigations.
- `references/known-threat-context.md`: ATT&CK relationship context and attribution cautions.
- `templates/detection-brief.md`: reusable detection engineering brief template.
- `templates/hunt-plan.md`: reusable threat hunt plan template.
- `templates/incident-response-note.md`: reusable IR note template.
- `templates/coverage-assessment.md`: reusable ATT&CK coverage assessment template.
- `scripts/render_brief.py`: renders a Markdown brief from the structured profile.
- `assets/output-schema.json`: JSON schema for structured outputs related to this technique.
"""
    (skill_dir / "resources.md").write_text(readme, encoding="utf-8")

    templates = {
        "detection-brief.md": f"""# Detection Brief: {external_id} {name}

## Objective

Create, review, or tune a defensive analytic for {external_id} {name}.

## ATT&CK mapping

- Domain: {domain}
- Tactics: {", ".join(tactics) if tactics else "[fill in]"}
- Platforms: {", ".join(platforms) if platforms else "[fill in]"}
- ATT&CK URL: {url or "[fill in]"}

## Data requirements

- Required data sources: {", ".join(data_sources) if data_sources else "[fill in]"}
- Required fields:
  - timestamp
  - asset or device identifier
  - user or principal
  - process, command, API, or event action
  - source and destination context

## Detection logic

Describe the behavior to detect in plain language, then provide SIEM, EDR, cloud logging, or data-lake query logic as appropriate.

## Tuning and exclusions

Document expected administrative activity, approved tooling, service accounts, maintenance windows, and environment-specific suppressions.

## Validation

Describe safe authorized validation steps, expected log artifacts, and pass/fail criteria. Avoid operational abuse instructions.

## Response guidance

Summarize containment, investigation, eradication, and recovery actions.
""",
        "hunt-plan.md": f"""# Hunt Plan: {external_id} {name}

## Hypothesis

Adversary behavior consistent with {external_id} {name} may be present in the environment.

## Scope

- Time range:
- Assets:
- Identities:
- Platforms:
- Exclusions:

## Required telemetry

{bullet_list(data_sources)}

## Hunt steps

1. Establish baseline activity for relevant assets and identities.
2. Search for behavior matching the ATT&CK description and detection notes.
3. Pivot across related entities, parent/child activity, network destinations, and persistence points.
4. Separate confirmed evidence from weak correlations and false positives.
5. Record coverage gaps and recommendations.

## Findings table

| Finding | Evidence | Confidence | Impact | Recommended action |
|---|---|---:|---|---|
|  |  | Low/Medium/High |  |  |
""",
        "incident-response-note.md": f"""# Incident Response Note: {external_id} {name}

## Executive summary

Summarize what happened, affected scope, confidence, current risk, and immediate actions.

## ATT&CK assessment

- Technique: {external_id} {name}
- Domain: {domain}
- Confidence:
- Rationale:

## Evidence

| Time | Asset | Identity | Event | Evidence source |
|---|---|---|---|---|
|  |  |  |  |  |

## Containment

- Immediate containment:
- Longer-term containment:
- Business impact:

## Eradication and recovery

- Root cause:
- Remediation actions:
- Validation steps:

## Lessons learned

- Detection gaps:
- Control gaps:
- Process gaps:
""",
        "coverage-assessment.md": f"""# ATT&CK Coverage Assessment: {external_id} {name}

## Control coverage

| Control | Status | Evidence | Gap | Owner |
|---|---|---|---|---|
| Preventive | Unknown |  |  |  |
| Detective | Unknown |  |  |  |
| Response | Unknown |  |  |  |

## Telemetry coverage

{bullet_list(data_sources)}

## Detection maturity

- None: no known telemetry or analytic.
- Basic: logs exist but analytic is manual or low fidelity.
- Intermediate: analytic exists with documented tuning.
- Advanced: analytic is validated, monitored, and mapped to response automation.

## Improvement backlog

| Priority | Improvement | Dependency | Owner | Target date |
|---:|---|---|---|---|
| 1 |  |  |  |  |
""",
    }
    for filename, content in templates.items():
        (templates_dir / filename).write_text(content, encoding="utf-8")

    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": f"Structured output for {external_id} {name}",
        "type": "object",
        "properties": {
            "attack_id": {"type": "string", "const": external_id},
            "technique_name": {"type": "string", "const": name},
            "domain": {"type": "string", "const": domain},
            "assessment": {"type": "string"},
            "confidence": {"type": "string", "enum": ["low", "medium", "high"]},
            "evidence": {"type": "array", "items": {"type": "string"}},
            "data_sources": {"type": "array", "items": {"type": "string"}},
            "detections": {"type": "array", "items": {"type": "string"}},
            "mitigations": {"type": "array", "items": {"type": "string"}},
            "response_actions": {"type": "array", "items": {"type": "string"}},
            "coverage_gaps": {"type": "array", "items": {"type": "string"}},
            "references": {"type": "array", "items": {"type": "string", "format": "uri"}},
        },
        "required": ["attack_id", "technique_name", "domain", "assessment", "confidence"],
        "additionalProperties": False,
    }
    (assets_dir / "output-schema.json").write_text(json.dumps(schema, indent=2), encoding="utf-8")

    script = """#!/usr/bin/env python3
\"\"\"Render a defensive ATT&CK brief from this skill's bundled profile.\"\"\"

from __future__ import annotations

import argparse
import json
from pathlib import Path


def bullets(items, empty=\"Not specified\"):
    return \"\\n\".join(f\"- {item}\" for item in items) if items else f\"- {empty}\"


def main():
    parser = argparse.ArgumentParser(description=\"Render a Markdown brief for this ATT&CK skill.\")
    parser.add_argument(\"--profile\", default=\"../references/technique-profile.json\", help=\"Path to technique-profile.json relative to this script\")
    parser.add_argument(\"--output\", default=\"-\", help=\"Output Markdown path, or '-' for stdout\")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    profile_path = (script_dir / args.profile).resolve()
    profile = json.loads(profile_path.read_text())

    md = f'''# ATT&CK Defensive Brief: {profile[\"attack_id\"]} {profile[\"name\"]}

## Context

- Domain: {profile[\"domain\"]}
- Type: {profile[\"type\"]}
- Tactics: {\", \".join(profile.get(\"tactics\", [])) or \"Not specified\"}
- Platforms: {\", \".join(profile.get(\"platforms\", [])) or \"Not specified\"}
- ATT&CK URL: {profile.get(\"attack_url\", \"\")}

## Description

{profile.get(\"description\", \"No description available.\")}

## Detection guidance

{profile.get(\"detection\", \"No detection guidance available.\")}

## Data sources

{bullets(profile.get(\"data_sources\", []))}

## Mitigations

{bullets(profile.get(\"mitigations\", []), \"No mapped mitigations in the bundled profile.\")}

## Known context

{bullets(profile.get(\"known_context\", []), \"No known context in the bundled profile.\")}
'''

    if args.output == \"-\":
        print(md)
    else:
        Path(args.output).write_text(md)


if __name__ == \"__main__\":
    main()
"""
    script_path = scripts_dir / "render_brief.py"
    script_path.write_text(script, encoding="utf-8")
    script_path.chmod(0o755)


def normalize_id(external_id: str) -> str:
    return external_id.lower().replace(".", "-")


def domain_objects(path: Path) -> tuple[list[dict], dict[str, dict], list[dict]]:
    data = json.loads(path.read_text())
    objects = data.get("objects", [])
    by_id = {o.get("id"): o for o in objects if o.get("id")}
    techniques = [
        o
        for o in objects
        if o.get("type") == "attack-pattern"
        and not o.get("revoked")
        and not o.get("x_mitre_deprecated")
    ]
    return techniques, by_id, objects


def relationship_maps(objects: list[dict], by_id: dict[str, dict]) -> dict[str, dict[str, list[str]]]:
    maps: dict[str, dict[str, list[str]]] = {}
    for rel in objects:
        if rel.get("type") != "relationship" or rel.get("revoked"):
            continue
        rel_type = rel.get("relationship_type")
        source = by_id.get(rel.get("source_ref"))
        target = by_id.get(rel.get("target_ref"))
        if not source or not target:
            continue
        if rel_type == "mitigates" and target.get("type") == "attack-pattern":
            maps.setdefault(target["id"], {}).setdefault("mitigations", []).append(source.get("name", "Unnamed mitigation"))
        elif rel_type == "uses" and target.get("type") == "attack-pattern":
            source_type = source.get("type", "object")
            label = f"{source.get('name', 'Unnamed')} ({source_type})"
            maps.setdefault(target["id"], {}).setdefault("used_by", []).append(label)
    return maps


def technique_skill(domain: str, domain_code: str, obj: dict, ref: dict, rels: dict[str, list[str]]) -> tuple[str, str]:
    external_id = ref.get("external_id", "unknown")
    url = ref.get("url", "")
    name = obj.get("name", "Unnamed Technique")
    skill_name = f"attack-{domain_code}-{normalize_id(external_id)}-{slugify(name)}"
    if len(skill_name) > 64:
        digest = hashlib.sha1(f"{domain}:{external_id}:{name}".encode()).hexdigest()[:6]
        base = f"attack-{domain_code}-{normalize_id(external_id)}"
        remaining = 63 - len(base) - len(digest) - 2
        skill_name = f"{base}-{slugify(name, max(8, remaining))}-{digest}"
    description_seed = first_sentence(obj.get("description", ""), f"Analyze MITRE ATT&CK {external_id} {name}.")
    description = (
        f"Analyze MITRE ATT&CK {external_id} {name} in the {domain} matrix. "
        f"Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, "
        f"incident response mapping, ATT&CK coverage, or questions mentioning {external_id}, {name}, or {domain} ATT&CK. "
        f"{description_seed}"
    )
    if len(description) > 1000:
        description = description[:999].rstrip() + "…"

    tactics = sorted({p.get("phase_name", "") for p in obj.get("kill_chain_phases", []) if p.get("phase_name")})
    platforms = as_list(obj.get("x_mitre_platforms"))
    permissions = as_list(obj.get("x_mitre_permissions_required"))
    data_sources = as_list(obj.get("x_mitre_data_sources"))
    effective_permissions = as_list(obj.get("x_mitre_effective_permissions"))
    defenses_bypassed = as_list(obj.get("x_mitre_defense_bypassed"))
    contributors = as_list(obj.get("x_mitre_contributors"))
    mitigations = sorted(set(rels.get("mitigations", [])))
    used_by = sorted(set(rels.get("used_by", [])))[:20]
    detection = obj.get("x_mitre_detection", "").strip() or "No ATT&CK detection guidance was present in the source STIX object."
    technique_type = "sub-technique" if obj.get("x_mitre_is_subtechnique") else "technique"

    body = f"""---
name: {skill_name}
description: {yaml_quote(description)}
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: {domain}
  attack_id: {external_id}
  attack_stix_id: {obj.get("id", "")}
  attack_version: "{obj.get("x_mitre_version", "")}"
  attack_modified: "{obj.get("modified", "")}"
---

# MITRE ATT&CK {external_id}: {name}

## When to use this skill

Use this skill when the task involves {external_id}, {name}, {domain} ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK {technique_type}.

## Technique context

- ATT&CK domain: {domain}
- ATT&CK ID: {external_id}
- Technique name: {name}
- Type: {technique_type}
- ATT&CK URL: {url or "Not specified"}
- Tactics: {", ".join(tactics) if tactics else "Not specified"}
- Platforms: {", ".join(platforms) if platforms else "Not specified"}
- Required permissions: {", ".join(permissions) if permissions else "Not specified"}
- Effective permissions: {", ".join(effective_permissions) if effective_permissions else "Not specified"}
- Defenses bypassed: {", ".join(defenses_bypassed) if defenses_bypassed else "Not specified"}

## ATT&CK description

{obj.get("description", "No description was present in the source STIX object.").strip()}

## Agent workflow

1. Clarify scope: identify the system, asset class, log sources, cloud or endpoint platform, and whether the user wants triage, detection, coverage assessment, or safe emulation planning.
2. Load bundled resources as needed: use `references/technique-profile.json` for structured metadata, `references/detection-and-mitigation.md` for triage and telemetry guidance, `references/known-threat-context.md` for ATT&CK relationship context, and `templates/` for repeatable outputs.
3. Map observations to ATT&CK: compare the user's evidence to the ATT&CK description, tactics, platforms, and known procedure patterns before asserting a match.
4. Produce defensive outputs: prioritize hypotheses, telemetry requirements, detection logic ideas, validation steps, containment guidance, and mitigations.
5. Preserve uncertainty: distinguish confirmed evidence, plausible indicators, assumptions, and gaps. Recommend what to collect next.
6. Stay safe: do not provide malware, credential theft, persistence, evasion, destructive automation, or unauthorized exploitation instructions. For adversary emulation, keep steps bounded to approved lab or control-validation contexts and omit operational abuse details.

## Bundled resources

- `references/technique-profile.json`: machine-readable ATT&CK metadata for this technique.
- `references/detection-and-mitigation.md`: detection notes, telemetry checklist, triage questions, mitigation candidates, and false-positive considerations.
- `references/known-threat-context.md`: ATT&CK relationship context with attribution cautions.
- `templates/detection-brief.md`: detection engineering brief template.
- `templates/hunt-plan.md`: threat hunt plan template.
- `templates/incident-response-note.md`: incident response note template.
- `templates/coverage-assessment.md`: ATT&CK coverage assessment template.
- `scripts/render_brief.py`: local helper that renders a Markdown defensive brief from `technique-profile.json`.
- `assets/output-schema.json`: JSON schema for structured technique analysis outputs.

To generate a quick brief, run `python scripts/render_brief.py --output brief.md` from inside this skill directory, or adapt the templates directly.

## Detection guidance

{detection}

## Useful telemetry and data sources

{bullet_list(data_sources)}

## Mitigations to consider

{bullet_list(mitigations, "No ATT&CK mitigation relationships were present in the source STIX bundle.")}

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

{bullet_list(used_by, "No group or software uses relationships were included for this technique in the source STIX bundle.")}

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
"""
    if contributors:
        body += "\n## ATT&CK contributors\n\n" + bullet_list(contributors) + "\n"
    return skill_name, body


def main() -> None:
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True)
    generated_at = dt.datetime.now(dt.UTC).isoformat()
    manifest_rows = []

    for domain, code, path, source_name in DOMAINS:
        techniques, by_id, objects = domain_objects(path)
        rel_maps = relationship_maps(objects, by_id)
        for obj in techniques:
            ref = get_external_ref(obj, source_name)
            if not ref.get("external_id"):
                continue
            skill_name, content = technique_skill(domain, code, obj, ref, rel_maps.get(obj["id"], {}))
            skill_dir = OUT_ROOT / domain / skill_name
            skill_dir.mkdir(parents=True, exist_ok=False)
            (skill_dir / "SKILL.md").write_text(content, encoding="utf-8")
            tactics = sorted({p.get("phase_name", "") for p in obj.get("kill_chain_phases", []) if p.get("phase_name")})
            platforms = as_list(obj.get("x_mitre_platforms"))
            permissions = as_list(obj.get("x_mitre_permissions_required"))
            data_sources = as_list(obj.get("x_mitre_data_sources"))
            mitigations = sorted(set(rel_maps.get(obj["id"], {}).get("mitigations", [])))
            used_by = sorted(set(rel_maps.get(obj["id"], {}).get("used_by", [])))[:20]
            detection = obj.get("x_mitre_detection", "").strip() or "No ATT&CK detection guidance was present in the source STIX object."
            write_resource_files(
                skill_dir,
                domain=domain,
                external_id=ref.get("external_id", ""),
                name=obj.get("name", ""),
                url=ref.get("url", ""),
                obj=obj,
                tactics=tactics,
                platforms=platforms,
                permissions=permissions,
                data_sources=data_sources,
                mitigations=mitigations,
                used_by=used_by,
                detection=detection,
            )
            manifest_rows.append(
                {
                    "skill_name": skill_name,
                    "domain": domain,
                    "attack_id": ref.get("external_id", ""),
                    "technique_name": obj.get("name", ""),
                    "is_subtechnique": str(bool(obj.get("x_mitre_is_subtechnique"))).lower(),
                    "attack_url": ref.get("url", ""),
                    "stix_id": obj.get("id", ""),
                    "attack_version": obj.get("x_mitre_version", ""),
                    "modified": obj.get("modified", ""),
                }
            )

    manifest_rows.sort(key=lambda r: (r["domain"], r["attack_id"], r["skill_name"]))
    with (OUT_ROOT / "manifest.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(manifest_rows[0].keys()))
        writer.writeheader()
        writer.writerows(manifest_rows)
    (OUT_ROOT / "manifest.json").write_text(json.dumps(manifest_rows, indent=2), encoding="utf-8")
    counts = {}
    for row in manifest_rows:
        counts[row["domain"]] = counts.get(row["domain"], 0) + 1
    readme = f"""# MITRE ATT&CK Agent Skills

Generated at: {generated_at}

This package contains one Agent Skill per non-revoked, non-deprecated ATT&CK `attack-pattern` object from the latest MITRE ATT&CK STIX bundles in `mitre-attack/attack-stix-data`.

## Counts

{chr(10).join(f"- {domain}: {count}" for domain, count in sorted(counts.items()))}
- Total: {len(manifest_rows)}

## Layout

```text
mitre-attack-agent-skills/
├── enterprise/
├── mobile/
├── ics/
├── manifest.csv
├── manifest.json
├── validation-summary.txt
└── README.md
```

Each skill directory contains a `SKILL.md` file whose frontmatter name matches the directory name and whose description includes ATT&CK ID, technique name, domain, and defensive use cases. Each skill also bundles technique-specific resources under `references/`, `templates/`, `scripts/`, and `assets/`.

## Notes

- Skill names use the pattern `attack-<domain-code>-<technique-id>-<technique-slug>`.
- Domain codes are `ent`, `mob`, and `ics`.
- Every skill includes:
  - `references/technique-profile.json`
  - `references/detection-and-mitigation.md`
  - `references/known-threat-context.md`
  - `templates/detection-brief.md`
  - `templates/hunt-plan.md`
  - `templates/incident-response-note.md`
  - `templates/coverage-assessment.md`
  - `scripts/render_brief.py`
  - `assets/output-schema.json`
- ATT&CK-derived content is subject to MITRE ATT&CK Terms of Use: https://attack.mitre.org/resources/terms-of-use/
- These skills are intentionally defensive. They guide triage, detection engineering, hunting, mitigation, coverage assessment, incident response, and safe authorized validation without providing malware or unauthorized exploitation instructions.
"""
    (OUT_ROOT / "README.md").write_text(readme, encoding="utf-8")
    print(json.dumps({"generated": len(manifest_rows), "counts": counts, "output": str(OUT_ROOT)}, indent=2))


if __name__ == "__main__":
    main()
