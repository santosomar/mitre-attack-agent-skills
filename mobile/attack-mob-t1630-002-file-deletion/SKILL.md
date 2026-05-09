---
name: attack-mob-t1630-002-file-deletion
description: "Analyze MITRE ATT&CK T1630.002 File Deletion in the mobile matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1630.002, File Deletion, or mobile ATT&CK. Adversaries may wipe a device or delete individual files in order to manipulate external outcomes or hide activity."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: mobile
  attack_id: T1630.002
  attack_stix_id: attack-pattern--ab7400b7-3476-4776-9545-ef3fa373de63
  attack_version: "1.1"
  attack_modified: "2025-10-24T17:49:12.849Z"
---

# MITRE ATT&CK T1630.002: File Deletion

## When to use this skill

Use this skill when the task involves T1630.002, File Deletion, mobile ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK sub-technique.

## Technique context

- ATT&CK domain: mobile
- ATT&CK ID: T1630.002
- Technique name: File Deletion
- Type: sub-technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1630/002
- Tactics: defense-evasion
- Platforms: Android
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may wipe a device or delete individual files in order to manipulate external outcomes or hide activity. An application must have administrator access to fully wipe the device, while individual files may not require special permissions to delete depending on their storage location.(Citation: Android DevicePolicyManager 2019) 

Stored data could include a variety of file formats, such as Office files, databases, stored emails, and custom file formats. The impact file deletion will have depends on the type of data as well as the goals and objectives of the adversary, but can include deleting update files to evade detection or deleting attacker-specified files for impact.

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

- User Guidance

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- Agent Smith (malware)
- Binary Validator (malware)
- CarbonSteal (malware)
- Desert Scorpion (malware)
- DocSwap (malware)
- DoubleAgent (malware)
- Fakecalls (malware)
- FlexiSpy (tool)
- GPlayed (malware)
- GolfSpy (malware)
- Hornbill (malware)
- Mandrake (malware)
- Monokle (malware)
- Operation Triangulation (campaign)
- Pallas (malware)
- SilkBean (malware)
- Tiktok Pro (malware)
- TriangleDB (malware)
- ViceLeaker (malware)
- WolfRAT (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
