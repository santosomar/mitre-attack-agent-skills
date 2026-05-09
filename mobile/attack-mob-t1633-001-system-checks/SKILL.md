---
name: attack-mob-t1633-001-system-checks
description: "Analyze MITRE ATT&CK T1633.001 System Checks in the mobile matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1633.001, System Checks, or mobile ATT&CK. Adversaries may employ various system checks to detect and avoid virtualization and analysis environments."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: mobile
  attack_id: T1633.001
  attack_stix_id: attack-pattern--6ffad4be-bfe0-424f-abde-4d9a84a800ad
  attack_version: "1.1"
  attack_modified: "2025-10-24T17:48:56.336Z"
---

# MITRE ATT&CK T1633.001: System Checks

## When to use this skill

Use this skill when the task involves T1633.001, System Checks, mobile ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK sub-technique.

## Technique context

- ATT&CK domain: mobile
- ATT&CK ID: T1633.001
- Technique name: System Checks
- Type: sub-technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1633/001
- Tactics: defense-evasion
- Platforms: Android, iOS
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may employ various system checks to detect and avoid virtualization and analysis environments. This may include changing behavior after checking for the presence of artifacts indicative of a virtual environment or sandbox. If the adversary detects a virtual environment, they may alter their malware’s behavior to disengage from the victim or conceal the core functions of the implant. They may also search for virtualization artifacts before dropping secondary or additional payloads. 

Checks could include generic system properties such as host/domain name and samples of network traffic. Adversaries may also check the network adapters addresses, CPU core count, and available memory/drive size. 

Hardware checks, such as the presence of motion sensors, could also be used to gather evidence that can be indicative a virtual environment. Adversaries may also query for specific readings from these devices.

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

- No ATT&CK mitigation relationships were present in the source STIX bundle.

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- AbstractEmu (malware)
- Android/AdDisplay.Ashas (malware)
- Anubis (malware)
- BRATA (malware)
- Cerberus (malware)
- Chameleon (malware)
- Dendroid (malware)
- FakeSpy (malware)
- Ginp (malware)
- HenBox (malware)
- Mandrake (malware)
- Rotexy (malware)
- TERRACOTTA (malware)
- TrickMo (malware)
- Windshift (intrusion-set)
- WolfRAT (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
