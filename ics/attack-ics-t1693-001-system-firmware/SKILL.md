---
name: attack-ics-t1693-001-system-firmware
description: "Analyze MITRE ATT&CK T1693.001 System Firmware in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1693.001, System Firmware, or ics ATT&CK. System firmware on modern assets is often designed with an update feature."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T1693.001
  attack_stix_id: attack-pattern--68a9324d-a524-4766-a899-a026f68a33df
  attack_version: "1.0"
  attack_modified: "2026-04-23T19:10:31.871Z"
---

# MITRE ATT&CK T1693.001: System Firmware

## When to use this skill

Use this skill when the task involves T1693.001, System Firmware, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK sub-technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T1693.001
- Technique name: System Firmware
- Type: sub-technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1693/001
- Tactics: impair-process-control, inhibit-response-function, persistence
- Platforms: Not specified
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

System firmware on modern assets is often designed with an update feature. Older device firmware may be factory installed and require special reprograming equipment. When available, the firmware update feature enables vendors to remotely patch bugs and perform upgrades. Device firmware updates are often delegated to the user and may be done using a software update package. It may also be possible to perform this task over the network.

An adversary may exploit the firmware update feature on accessible devices to upload malicious or out-of-date firmware. Malicious modification of device firmware may provide an adversary with root access to a device, given firmware is one of the lowest programming abstraction layers.(Citation: Basnight, Zachry, et al.)

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
- Boot Integrity
- Code Signing
- Communication Authenticity
- Encrypt Network Traffic
- Encrypt Sensitive Information
- Filter Network Traffic
- Human User Authentication
- Network Allowlists
- Network Segmentation
- Software Process and Device Authentication
- Update Software

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- 2015 Ukraine Electric Power Attack (campaign)
- 2025 Poland Wiper Attacks (campaign)
- FrostyGoop Incident (campaign)
- Triton (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
