---
name: attack-ics-t0843-002-online-edit
description: "Analyze MITRE ATT&CK T0843.002 Online Edit in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0843.002, Online Edit, or ics ATT&CK. Adversaries may execute an online edit of a PLC to update parts of an existing program."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0843.002
  attack_stix_id: attack-pattern--d85a6ee9-820c-4adf-8a64-2392ee70c83c
  attack_version: "1.0"
  attack_modified: "2026-04-23T17:40:18.368Z"
---

# MITRE ATT&CK T0843.002: Online Edit

## When to use this skill

Use this skill when the task involves T0843.002, Online Edit, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK sub-technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0843.002
- Technique name: Online Edit
- Type: sub-technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0843/002
- Tactics: lateral-movement
- Platforms: Not specified
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may execute an online edit of a PLC to update parts of an existing program. It does not require stopping the PLC which allows it to continue running during transfer and reconfiguration without interruption to process control. Adversaries may leverage this approach to minimize downtime and evade detection. 

The ability to perform an online edit to the PLC typically relies on access to a workstation with the vendor-specific PLC programming software installed.

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

- Access Management
- Audit
- Authorization Enforcement
- Code Signing
- Communication Authenticity
- Filter Network Traffic
- Human User Authentication
- Network Allowlists
- Network Segmentation
- Software Process and Device Authentication

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
