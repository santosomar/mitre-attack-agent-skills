---
name: attack-ics-t0851-rootkit
description: "Analyze MITRE ATT&CK T0851 Rootkit in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0851, Rootkit, or ics ATT&CK. Adversaries may deploy rootkits to hide the presence of programs, files, network connections, services, drivers, and other system components."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0851
  attack_stix_id: attack-pattern--3b6b9246-43f8-4c69-ad7a-2b11cfe0a0d9
  attack_version: "1.1"
  attack_modified: "2025-04-16T21:26:13.542Z"
---

# MITRE ATT&CK T0851: Rootkit

## When to use this skill

Use this skill when the task involves T0851, Rootkit, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0851
- Technique name: Rootkit
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0851
- Tactics: evasion, inhibit-response-function
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may deploy rootkits to hide the presence of programs, files, network connections, services, drivers, and other system components. Rootkits are programs that hide the existence of malware by intercepting and modifying operating-system API calls that supply system information. Rootkits or rootkit-enabling functionality may reside at the user or kernel level in the operating system, or lower. (Citation: Enterprise ATT&CK January 2018)   

Firmware rootkits that affect the operating system yield nearly full control of the system. While firmware rootkits are normally developed for the main processing board, they can also be developed for the I/O that is attached to an asset. Compromise of this firmware allows the modification of all of the process variables and functions the module engages in. This may result in commands being disregarded and false information being fed to the main device. By tampering with device processes, an adversary may inhibit its expected response functions and possibly enable [Impact](https://attack.mitre.org/tactics/TA0105).

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
- Code Signing

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- Stuxnet (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
