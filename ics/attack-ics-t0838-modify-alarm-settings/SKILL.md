---
name: attack-ics-t0838-modify-alarm-settings
description: "Analyze MITRE ATT&CK T0838 Modify Alarm Settings in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0838, Modify Alarm Settings, or ics ATT&CK. Adversaries may modify alarm settings to prevent alerts that may inform operators of their presence or to prevent responses to dangerous and unintended scenarios."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0838
  attack_stix_id: attack-pattern--e5de767e-f513-41cd-aa15-33f6ce5fbf92
  attack_version: "1.2"
  attack_modified: "2025-04-16T21:26:19.764Z"
---

# MITRE ATT&CK T0838: Modify Alarm Settings

## When to use this skill

Use this skill when the task involves T0838, Modify Alarm Settings, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0838
- Technique name: Modify Alarm Settings
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0838
- Tactics: inhibit-response-function
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may modify alarm settings to prevent alerts that may inform operators of their presence or to prevent responses to dangerous and unintended scenarios. Reporting messages are a standard part of data acquisition in control systems. Reporting messages are used as a way to transmit system state information and acknowledgements that specific actions have occurred. These messages provide vital information for the management of a physical process, and keep operators, engineers, and administrators aware of the state of system devices and physical processes. 

If an adversary is able to change the reporting settings, certain events could be prevented from being reported. This type of modification can also prevent operators or devices from performing actions to keep the system in a safe state. If critical reporting messages cannot trigger these actions then a [Impact](https://attack.mitre.org/tactics/TA0105) could occur. 

In ICS environments, the adversary may have to use [Alarm Suppression](https://attack.mitre.org/techniques/T0878) or contend with multiple alarms and/or alarm propagation to achieve a specific goal to evade detection or prevent intended responses from occurring. (Citation: Jos Wetzels, Marina Krotofil 2019)  Methods of suppression often rely on modification of alarm settings, such as modifying in memory code to fixed values or tampering with assembly level instruction code.

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
- Authorization Enforcement
- Human User Authentication
- Network Allowlists
- Network Segmentation
- Software Process and Device Authentication
- User Account Management

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- Maroochy Water Breach (campaign)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
