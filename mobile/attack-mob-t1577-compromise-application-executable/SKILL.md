---
name: attack-mob-t1577-compromise-application-executable
description: "Analyze MITRE ATT&CK T1577 Compromise Application Executable in the mobile matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1577, Compromise Application Executable, or mobile ATT&CK. Adversaries may modify applications installed on a device to establish persistent access to a victim."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: mobile
  attack_id: T1577
  attack_stix_id: attack-pattern--d3bc5020-f6a2-41c0-8ccb-5e563101b60c
  attack_version: "1.0"
  attack_modified: "2025-10-24T17:49:26.629Z"
---

# MITRE ATT&CK T1577: Compromise Application Executable

## When to use this skill

Use this skill when the task involves T1577, Compromise Application Executable, mobile ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: mobile
- ATT&CK ID: T1577
- Technique name: Compromise Application Executable
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1577
- Tactics: persistence
- Platforms: Android
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may modify applications installed on a device to establish persistent access to a victim. These malicious modifications can be used to make legitimate applications carry out adversary tasks when these applications are in use.

There are multiple ways an adversary can inject malicious code into applications. One method is by taking advantages of device vulnerabilities, the most well-known being Janus, an Android vulnerability that allows adversaries to add extra bytes to APK (application) and DEX (executable) files without affecting the file's signature. By being able to add arbitrary bytes to valid applications, attackers can seamlessly inject code into genuine executables without the user's knowledge.(Citation: Guardsquare Janus)

Adversaries may also rebuild applications to include malicious modifications. This can be achieved by decompiling the genuine application, merging it with the malicious code, and recompiling it.(Citation: CheckPoint Agent Smith)

Adversaries may also take action to conceal modifications to application executables and bypass user consent. These actions include altering modifications to appear as an update or exploiting vulnerabilities that allow activities of the malicious application to run inside a system application.(Citation: CheckPoint Agent Smith)

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

- Security Updates
- Use Recent OS Version

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- Agent Smith (malware)
- BOULDSPY (malware)
- YiSpecter (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
