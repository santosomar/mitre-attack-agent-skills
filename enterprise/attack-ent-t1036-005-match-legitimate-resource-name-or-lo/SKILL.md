---
name: attack-ent-t1036-005-match-legitimate-resource-name-or-lo
description: "Analyze MITRE ATT&CK T1036.005 Match Legitimate Resource Name or Location in the enterprise matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1036.005, Match Legitimate Resource Name or Location, or enterprise ATT&CK. Adversaries may match or approximate the name or location of legitimate files, Registry keys, or other resources when naming/placing them."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: enterprise
  attack_id: T1036.005
  attack_stix_id: attack-pattern--1c4e5d32-1fe9-4116-9d9d-59e3925bd6a2
  attack_version: "3.0"
  attack_modified: "2026-04-15T20:39:41.881Z"
---

# MITRE ATT&CK T1036.005: Match Legitimate Resource Name or Location

## When to use this skill

Use this skill when the task involves T1036.005, Match Legitimate Resource Name or Location, enterprise ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK sub-technique.

## Technique context

- ATT&CK domain: enterprise
- ATT&CK ID: T1036.005
- Technique name: Match Legitimate Resource Name or Location
- Type: sub-technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1036/005
- Tactics: stealth
- Platforms: Containers, ESXi, Linux, macOS, Windows
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may match or approximate the name or location of legitimate files, Registry keys, or other resources when naming/placing them. This is done for the sake of evading defenses and observation. 

This may be done by placing an executable in a commonly trusted directory (ex: under System32) or giving it the name of a legitimate, trusted program (ex: `svchost.exe`). Alternatively, a Windows Registry key may be given a close approximation to a key used by a legitimate program. In containerized environments, a threat actor may create a resource in a trusted namespace or one that matches the naming convention of a container pod or cluster.(Citation: Aquasec Kubernetes Backdoor 2023)

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

- Code Signing
- Execution Prevention
- Restrict File and Directory Permissions

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- 2016 Ukraine Electric Power Attack (campaign)
- 2025 Poland Wiper Attacks (campaign)
- ANDROMEDA (malware)
- APT-C-36 (intrusion-set)
- APT1 (intrusion-set)
- APT28 (intrusion-set)
- APT29 (intrusion-set)
- APT32 (intrusion-set)
- APT39 (intrusion-set)
- APT41 (intrusion-set)
- APT42 (intrusion-set)
- APT5 (intrusion-set)
- Akira (intrusion-set)
- AppleSeed (malware)
- Aquatic Panda (intrusion-set)
- AshTag (malware)
- BADNEWS (malware)
- BLINDINGCAN (malware)
- BRICKSTORM (malware)
- BRONZE BUTLER (intrusion-set)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.

## ATT&CK contributors

- Vishwas Manral, McAfee
- Yossi Weizman, Azure Defender Research Team
