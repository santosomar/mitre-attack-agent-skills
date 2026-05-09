---
name: attack-ics-t0879-damage-to-property
description: "Analyze MITRE ATT&CK T0879 Damage to Property in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0879, Damage to Property, or ics ATT&CK. Adversaries may cause damage and destruction of property to infrastructure, equipment, and the surrounding environment when attacking control systems."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0879
  attack_stix_id: attack-pattern--83ebd22f-b401-4d59-8219-2294172cf916
  attack_version: "1.1"
  attack_modified: "2025-04-16T21:26:15.731Z"
---

# MITRE ATT&CK T0879: Damage to Property

## When to use this skill

Use this skill when the task involves T0879, Damage to Property, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0879
- Technique name: Damage to Property
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0879
- Tactics: impact
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may cause damage and destruction of property to infrastructure, equipment, and the surrounding environment when attacking control systems. This technique may result in device and operational equipment breakdown, or represent tangential damage from other techniques used in an attack. Depending on the severity of physical damage and disruption caused to control processes and systems, this technique may result in [Loss of Safety](https://attack.mitre.org/techniques/T0880). Operations that result in [Loss of Control](https://attack.mitre.org/techniques/T0827) may also cause damage to property, which may be directly or indirectly motivated by an adversary seeking to cause impact in the form of [Loss of Productivity and Revenue](https://attack.mitre.org/techniques/T0828). 


The German Federal Office for Information Security (BSI) reported a targeted attack on a steel mill under an incidents affecting business section of its 2014 IT Security Report. (Citation: BSI State of IT Security 2014)  These targeted attacks affected industrial operations and resulted in breakdowns of control system components and even entire installations. As a result of these breakdowns, massive impact and damage resulted from the uncontrolled shutdown of a blast furnace. 

A Polish student used a remote controller device to interface with the Lodz city tram system in Poland. (Citation: John Bill May 2017) (Citation: Shelley Smith February 2008) (Citation: Bruce Schneier January 2008) Using this remote, the student was able to capture and replay legitimate tram signals. This resulted in damage to impacted trams, people, and the surrounding property. Reportedly, four trams were derailed and were forced to make emergency stops. (Citation: Shelley Smith February 2008) Commands issued by the student may have also resulted in tram collisions, causing harm to those on board and the environment outside. (Citation: Bruce Schneier January 2008)

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

- Mechanical Protection Layers
- Network Allowlists
- Safety Instrumented Systems

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
