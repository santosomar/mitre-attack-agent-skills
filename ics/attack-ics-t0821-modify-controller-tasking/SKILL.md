---
name: attack-ics-t0821-modify-controller-tasking
description: "Analyze MITRE ATT&CK T0821 Modify Controller Tasking in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0821, Modify Controller Tasking, or ics ATT&CK. Adversaries may modify the tasking of a controller to allow for the execution of their own programs."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0821
  attack_stix_id: attack-pattern--09a61657-46e1-439e-b3ed-3e4556a78243
  attack_version: "1.2"
  attack_modified: "2025-04-16T21:26:10.230Z"
---

# MITRE ATT&CK T0821: Modify Controller Tasking

## When to use this skill

Use this skill when the task involves T0821, Modify Controller Tasking, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0821
- Technique name: Modify Controller Tasking
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0821
- Tactics: execution
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may modify the tasking of a controller to allow for the execution of their own programs. This can allow an adversary to manipulate the execution flow and behavior of a controller. 

According to 61131-3, the association of a Task with a Program Organization Unit (POU) defines a task association. (Citation: IEC February 2013) An adversary may modify these associations or create new ones to manipulate the execution flow of a controller. Modification of controller tasking can be accomplished using a Program Download in addition to other types of program modification such as online edit and program append.

Tasks have properties, such as interval, frequency and priority to meet the requirements of program execution. Some controller vendors implement tasks with implicit, pre-defined properties whereas others allow for these properties to be formulated explicitly. An adversary may associate their program with tasks that have a higher priority or execute associated programs more frequently. For instance, to ensure cyclic execution of their program on a Siemens controller, an adversary may add their program to the task, Organization Block 1 (OB1).

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

- Audit
- Authorization Enforcement
- Code Signing
- Human User Authentication

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- PLC-Blaster (malware)
- Stuxnet (malware)
- Triton (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
