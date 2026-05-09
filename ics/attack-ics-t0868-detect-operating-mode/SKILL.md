---
name: attack-ics-t0868-detect-operating-mode
description: "Analyze MITRE ATT&CK T0868 Detect Operating Mode in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0868, Detect Operating Mode, or ics ATT&CK. Adversaries may gather information about a PLCs or controllers current operating mode."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0868
  attack_stix_id: attack-pattern--2aa406ed-81c3-4c1d-ba83-cfbee5a2847a
  attack_version: "1.0"
  attack_modified: "2025-04-16T21:26:11.972Z"
---

# MITRE ATT&CK T0868: Detect Operating Mode

## When to use this skill

Use this skill when the task involves T0868, Detect Operating Mode, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0868
- Technique name: Detect Operating Mode
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0868
- Tactics: collection
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may gather information about a PLCs or controllers current operating mode. Operating modes dictate what change or maintenance functions can be manipulated and are often controlled by a key switch on the PLC (e.g.,  run, prog [program], and remote). Knowledge of these states may be valuable to an adversary to determine if they are able to reprogram the PLC. Operating modes and the mechanisms by which they are selected often vary by vendor and product line. Some commonly implemented operating modes are described below:  

* Program - This mode must be enabled before changes can be made to a devices program. This allows program uploads and downloads between the device and an engineering workstation. Often the PLCs logic Is halted, and all outputs may be forced off. (Citation: N.A. October 2017)  
* Run - Execution of the devices program occurs in this mode. Input and output (values, points, tags, elements, etc.) are monitored and used according to the programs logic.[Program Upload](https://attack.mitre.org/techniques/T0845) and [Program Download](https://attack.mitre.org/techniques/T0843) are disabled while in this mode. (Citation: Omron) (Citation: Machine Information Systems 2007)  (Citation: N.A. October 2017) (Citation: PLCgurus 2021)   
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
- Filter Network Traffic
- Human User Authentication
- Network Allowlists
- Network Segmentation
- Software Process and Device Authentication

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- Triton (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
