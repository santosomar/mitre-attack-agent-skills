---
name: attack-ics-t0828-loss-of-productivity-and-revenue
description: "Analyze MITRE ATT&CK T0828 Loss of Productivity and Revenue in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0828, Loss of Productivity and Revenue, or ics ATT&CK. Adversaries may cause loss of productivity and revenue through disruption and even damage to the availability and integrity of control system operations, devices, and related processes."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0828
  attack_stix_id: attack-pattern--63b6942d-8359-4506-bfb3-cf87aa8120ee
  attack_version: "1.0"
  attack_modified: "2025-04-16T21:26:15.157Z"
---

# MITRE ATT&CK T0828: Loss of Productivity and Revenue

## When to use this skill

Use this skill when the task involves T0828, Loss of Productivity and Revenue, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0828
- Technique name: Loss of Productivity and Revenue
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0828
- Tactics: impact
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may cause loss of productivity and revenue through disruption and even damage to the availability and integrity of control system operations, devices, and related processes. This technique may manifest as a direct effect of an ICS-targeting attack or tangentially, due to an IT-targeting attack against non-segregated environments. 

In cases where these operations or services are brought to a halt, the loss of productivity may eventually present an impact for the end-users or consumers of products and services. The disrupted supply-chain may result in supply shortages and increased prices, among other consequences. 

A ransomware attack on an Australian beverage company resulted in the shutdown of some manufacturing sites, including precautionary halts to protect key systems. (Citation: Paganini, Pierluigi June 2020) The company announced the potential for temporary shortages of their products following the attack. (Citation: Paganini, Pierluigi June 2020) (Citation: Lion Corporation June 2020) 

In the 2021 Colonial Pipeline ransomware incident, the pipeline was unable to transport approximately 2.5 million barrels of fuel per day to the East Coast.  (Citation: Colonial Pipeline Company May 2021)

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

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- 2015 Ukraine Electric Power Attack (campaign)
- Bad Rabbit (malware)
- Conficker (malware)
- EKANS (malware)
- LockerGoga (malware)
- NotPetya (malware)
- REvil (malware)
- Ryuk (malware)
- Triton Safety Instrumented System Attack (campaign)
- Unitronics Defacement Campaign (campaign)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
