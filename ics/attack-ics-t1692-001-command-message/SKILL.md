---
name: attack-ics-t1692-001-command-message
description: "Analyze MITRE ATT&CK T1692.001 Command Message in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1692.001, Command Message, or ics ATT&CK. Adversaries may send unauthorized command messages to instruct control system assets to perform actions outside of their intended functionality, or without the logical preconditions to trigger their expected function."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T1692.001
  attack_stix_id: attack-pattern--4344d1b8-968b-4697-9ab9-f9abe5f52265
  attack_version: "1.0"
  attack_modified: "2026-04-23T18:59:19.225Z"
---

# MITRE ATT&CK T1692.001: Command Message

## When to use this skill

Use this skill when the task involves T1692.001, Command Message, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK sub-technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T1692.001
- Technique name: Command Message
- Type: sub-technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1692/001
- Tactics: evasion, impair-process-control
- Platforms: Not specified
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may send unauthorized command messages to instruct control system assets to perform actions outside of their intended functionality, or without the logical preconditions to trigger their expected function. Command messages are used in ICS networks to give direct instructions to control systems devices. If an adversary can send an unauthorized command message to a control system, then it can instruct the control systems device to perform an action outside the normal bounds of the device's actions. An adversary could potentially instruct a control systems device to perform an action that will cause an [Impact](https://attack.mitre.org/tactics/TA0105).(Citation: Bonnie Zhu, Anthony Joseph, Shankar Sastry 2011)

In the Dallas Siren incident, adversaries were able to send command messages to activate tornado alarm systems across the city without an impending tornado or other disaster.(Citation: Zack Whittaker April 2017)(Citation: Benjamin Freed March 2019)

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

- Communication Authenticity
- Filter Network Traffic
- Network Allowlists
- Network Segmentation
- Software Process and Device Authentication
- Validate Program Inputs

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- 2015 Ukraine Electric Power Attack (campaign)
- 2022 Ukraine Electric Power Attack (campaign)
- INCONTROLLER (malware)
- Industroyer (malware)
- Industroyer2 (malware)
- Maroochy Water Breach (campaign)
- Triton Safety Instrumented System Attack (campaign)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
