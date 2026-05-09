---
name: attack-ics-t0835-manipulate-i-o-image
description: "Analyze MITRE ATT&CK T0835 Manipulate I/O Image in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0835, Manipulate I/O Image, or ics ATT&CK. Adversaries may manipulate the I/O image of PLCs through various means to prevent them from functioning as expected."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0835
  attack_stix_id: attack-pattern--36e9f5bc-ac13-4da4-a2f4-01f4877d9004
  attack_version: "1.1"
  attack_modified: "2025-04-15T19:58:22.225Z"
---

# MITRE ATT&CK T0835: Manipulate I/O Image

## When to use this skill

Use this skill when the task involves T0835, Manipulate I/O Image, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0835
- Technique name: Manipulate I/O Image
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0835
- Tactics: inhibit-response-function
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may manipulate the I/O image of PLCs through various means to prevent them from functioning as expected. Methods of I/O image manipulation may include overriding the I/O table via direct memory manipulation or using the override function used for testing PLC programs. (Citation: Dr. Kelvin T. Erickson December 2010) During the scan cycle, a PLC reads the status of all inputs and stores them in an image table. (Citation: Nanjundaiah, Vaidyanath) The image table is the PLCs internal storage location where values of inputs/outputs for one scan are stored while it executes the user program. After the PLC has solved the entire logic program, it updates the output image table. The contents of this output image table are written to the corresponding output points in I/O Modules. 

One of the unique characteristics of PLCs is their ability to override the status of a physical discrete input or to override the logic driving a physical output coil and force the output to a desired status.

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

- Mitigation Limited or Not Effective

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
