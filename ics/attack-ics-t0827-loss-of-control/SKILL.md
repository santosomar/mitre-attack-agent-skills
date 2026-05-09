---
name: attack-ics-t0827-loss-of-control
description: "Analyze MITRE ATT&CK T0827 Loss of Control in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0827, Loss of Control, or ics ATT&CK. Adversaries may seek to achieve a sustained loss of control or a runaway condition in which operators cannot issue any commands even if the malicious interference has subsided."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0827
  attack_stix_id: attack-pattern--a81696ef-c106-482c-8f80-59c30f2569fb
  attack_version: "1.0"
  attack_modified: "2025-04-15T19:58:56.356Z"
---

# MITRE ATT&CK T0827: Loss of Control

## When to use this skill

Use this skill when the task involves T0827, Loss of Control, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0827
- Technique name: Loss of Control
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0827
- Tactics: impact
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may seek to achieve a sustained loss of control or a runaway condition in which operators cannot issue any commands even if the malicious interference has subsided. (Citation: Corero) (Citation: Michael J. Assante and Robert M. Lee) (Citation: Tyson Macaulay)

The German Federal Office for Information Security (BSI) reported a targeted attack on a steel mill in its 2014 IT Security Report.(Citation: BSI State of IT Security 2014) These targeted attacks affected industrial operations and resulted in breakdowns of control system components and even entire installations. As a result of these breakdowns, massive impact resulted in damage and unsafe conditions from the uncontrolled shutdown of a blast furnace.

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

- Data Backup
- Out-of-Band Communications Channel
- Redundancy of Service

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- 2015 Ukraine Electric Power Attack (campaign)
- 2025 Poland Wiper Attacks (campaign)
- Industroyer (malware)
- LockerGoga (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.

## ATT&CK contributors

- Dragos Threat Intelligence
