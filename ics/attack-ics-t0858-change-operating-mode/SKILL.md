---
name: attack-ics-t0858-change-operating-mode
description: "Analyze MITRE ATT&CK T0858 Change Operating Mode in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0858, Change Operating Mode, or ics ATT&CK. Adversaries may change the operating mode of a controller to gain additional access to engineering functions such as Program Download."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0858
  attack_stix_id: attack-pattern--2883c520-7957-46ca-89bd-dab1ad53b601
  attack_version: "1.0"
  attack_modified: "2025-04-16T21:26:11.583Z"
---

# MITRE ATT&CK T0858: Change Operating Mode

## When to use this skill

Use this skill when the task involves T0858, Change Operating Mode, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0858
- Technique name: Change Operating Mode
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0858
- Tactics: evasion, execution
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may change the operating mode of a controller to gain additional access to engineering functions such as Program Download.   Programmable controllers typically have several modes of operation that control the state of the user program and control access to the controllers API. Operating modes can be physically selected using a key switch on the face of the controller but may also be selected with calls to the controllers API. Operating modes and the mechanisms by which they are selected often vary by vendor and product line. Some commonly implemented operating modes are described below:  

* Program - This mode must be enabled before changes can be made to a devices program. This allows program uploads and downloads between the device and an engineering workstation. Often the PLCs logic Is halted, and all outputs may be forced off. (Citation: N.A. October 2017)  
* Run - Execution of the devices program occurs in this mode. Input and output (values, points, tags, elements, etc.) are monitored and used according to the programs logic. [Program Upload](https://attack.mitre.org/techniques/T0845) and [Program Download](https://attack.mitre.org/techniques/T0843) are disabled while in this mode. (Citation: Omron) (Citation: Machine Information Systems 2007)  (Citation: N.A. October 2017) (Citation: PLCgurus 2021)   
* Remote - Allows for remote changes to a PLCs operation mode. (Citation: PLCgurus 2021)    
* Stop - The PLC and program is stopped, while in this mode, outputs are forced off. (Citation: Machine Information Systems 2007)   
* Reset - Conditions on the PLC are reset to their original states. Warm resets may retain some memory while cold resets will reset all I/O and data registers. (Citation: Machine Information Systems 2007)   
* Test / Monitor mode - Similar to run mode, I/O is processed, although this mode allows for monitoring, force set, resets, and more generally tuning or debugging of the system. Often monitor mode may be used as a trial for initialization. (Citation: Omron)

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
- Communication Authenticity
- Human User Authentication
- Network Allowlists
- Network Segmentation
- Software Process and Device Authentication

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- INCONTROLLER (malware)
- PLC-Blaster (malware)
- Triton (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
