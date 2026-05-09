---
name: attack-ics-t0853-scripting
description: "Analyze MITRE ATT&CK T0853 Scripting in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0853, Scripting, or ics ATT&CK. Adversaries may use scripting languages to execute arbitrary code in the form of a pre-written script or in the form of user-supplied code to an interpreter."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0853
  attack_stix_id: attack-pattern--2dc2b567-8821-49f9-9045-8740f3d0b958
  attack_version: "1.0"
  attack_modified: "2025-04-16T21:26:12.511Z"
---

# MITRE ATT&CK T0853: Scripting

## When to use this skill

Use this skill when the task involves T0853, Scripting, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0853
- Technique name: Scripting
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0853
- Tactics: execution
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may use scripting languages to execute arbitrary code in the form of a pre-written script or in the form of user-supplied code to an interpreter. Scripting languages are programming languages that differ from compiled languages, in that scripting languages use an interpreter, instead of a compiler. These interpreters read and compile part of the source code just before it is executed, as opposed to compilers, which compile each and every line of code to an executable file. Scripting allows software developers to run their code on any system where the interpreter exists. This way, they can distribute one package, instead of precompiling executables for many different systems. Scripting languages, such as Python, have their interpreters shipped as a default with many Linux distributions. 

In addition to being a useful tool for developers and administrators, scripting language interpreters may be abused by the adversary to execute code in the target environment. Due to the nature of scripting languages, this allows for weaponized code to be deployed to a target easily, and leaves open the possibility of on-the-fly scripting to perform a task.

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

- Application Isolation and Sandboxing
- Disable or Remove Feature or Program
- Execution Prevention

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- 2016 Ukraine Electric Power Attack (campaign)
- 2022 Ukraine Electric Power Attack (campaign)
- APT33 (intrusion-set)
- OilRig (intrusion-set)
- REvil (malware)
- Triton (malware)
- Triton Safety Instrumented System Attack (campaign)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
