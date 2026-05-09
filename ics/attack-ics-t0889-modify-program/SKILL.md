---
name: attack-ics-t0889-modify-program
description: "Analyze MITRE ATT&CK T0889 Modify Program in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0889, Modify Program, or ics ATT&CK. Adversaries may modify or add a program on a controller to affect how it interacts with the physical process, peripheral devices and other hosts on the network."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0889
  attack_stix_id: attack-pattern--fc5fda7e-6b2c-4457-b036-759896a2efa2
  attack_version: "1.2"
  attack_modified: "2025-04-15T19:59:24.213Z"
---

# MITRE ATT&CK T0889: Modify Program

## When to use this skill

Use this skill when the task involves T0889, Modify Program, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0889
- Technique name: Modify Program
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0889
- Tactics: persistence
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may modify or add a program on a controller to affect how it interacts with the physical process, peripheral devices and other hosts on the network. Modification to controller programs can be accomplished using a Program Download in addition to other types of program modification such as online edit and program append. 

Program modification encompasses the addition and modification of instructions and logic contained in Program Organization Units (POU)  (Citation: IEC February 2013) and similar programming elements found on controllers. This can include, for example, adding new functions to a controller, modifying the logic in existing functions and making new calls from one function to another. 

Some programs may allow an adversary to interact directly with the native API of the controller to take advantage of obscure features or vulnerabilities.

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

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
