---
name: attack-ent-t1027-017-svg-smuggling
description: "Analyze MITRE ATT&CK T1027.017 SVG Smuggling in the enterprise matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1027.017, SVG Smuggling, or enterprise ATT&CK. Adversaries may smuggle data and files past content filters by hiding malicious payloads inside of seemingly benign SVG files.(Citation: Trustwave SVG Smuggling 2025) SVGs, or Scalable Vector Graphics, are vector-based…"
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: enterprise
  attack_id: T1027.017
  attack_stix_id: attack-pattern--78b9e70d-1605-459c-b23d-e3a25036968c
  attack_version: "2.0"
  attack_modified: "2026-04-15T22:22:02.298Z"
---

# MITRE ATT&CK T1027.017: SVG Smuggling

## When to use this skill

Use this skill when the task involves T1027.017, SVG Smuggling, enterprise ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK sub-technique.

## Technique context

- ATT&CK domain: enterprise
- ATT&CK ID: T1027.017
- Technique name: SVG Smuggling
- Type: sub-technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1027/017
- Tactics: stealth
- Platforms: Linux, macOS, Windows
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may smuggle data and files past content filters by hiding malicious payloads inside of seemingly benign SVG files.(Citation: Trustwave SVG Smuggling 2025) SVGs, or Scalable Vector Graphics, are vector-based image files constructed using XML. As such, they can legitimately include `<script>` tags that enable adversaries to include malicious JavaScript payloads. However, SVGs may appear less suspicious to users than other types of executable files, as they are often treated as image files. 

SVG smuggling can take a number of forms. For example, threat actors may include content that: 

* Assembles malicious payloads(Citation: Talos SVG Smuggling 2022)
* Downloads malicious payloads(Citation: Cofense SVG Smuggling 2024)
* Redirects users to malicious websites(Citation: Bleeping Computer SVG Smuggling 2024)
* Displays interactive content to users, such as fake login forms and download buttons.(Citation: Bleeping Computer SVG Smuggling 2024)

SVG Smuggling may be used in conjunction with [HTML Smuggling](https://attack.mitre.org/techniques/T1027/006) where an SVG with a malicious payload is included inside an HTML file.(Citation: Talos SVG Smuggling 2022) SVGs may also be included in other types of documents, such as PDFs.

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

No ATT&CK detection guidance was present in the source STIX object.

## Useful telemetry and data sources

- Not specified in the STIX object.

## Mitigations to consider

- Application Isolation and Sandboxing

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- No group or software uses relationships were included for this technique in the source STIX bundle.

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.

## ATT&CK contributors

- Dhiraj Mishra (@RandomDhiraj)
- Suraj Khetani (@r00treaver)
