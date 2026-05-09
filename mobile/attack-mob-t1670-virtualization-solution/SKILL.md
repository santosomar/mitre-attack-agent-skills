---
name: attack-mob-t1670-virtualization-solution
description: "Analyze MITRE ATT&CK T1670 Virtualization Solution in the mobile matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1670, Virtualization Solution, or mobile ATT&CK. Adversaries may carry out malicious operations using virtualization solutions to escape from Android sandboxes and to avoid detection."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: mobile
  attack_id: T1670
  attack_stix_id: attack-pattern--8e097ec5-1755-41d6-807c-3882442b818a
  attack_version: "1.0"
  attack_modified: "2025-03-14T17:56:26.095Z"
---

# MITRE ATT&CK T1670: Virtualization Solution

## When to use this skill

Use this skill when the task involves T1670, Virtualization Solution, mobile ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: mobile
- ATT&CK ID: T1670
- Technique name: Virtualization Solution
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1670
- Tactics: defense-evasion
- Platforms: Android
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may carry out malicious operations using virtualization solutions to escape from Android sandboxes and to avoid detection. Android uses sandboxes to separate resources and code execution between applications and the operating system.(Citation: Android Application Sandbox) There are a few virtualization solutions available on Android, such as the Android Virtualization Framework (AVF).(Citation: Android AVF Overview)  

 

Through virtualization solutions, adversaries may execute malicious operations without user knowledge. For example, adversaries may mimic a legitimate banking application’s functionalities in a virtual environment, thanks to the virtualization solution, while malicious code captures credentials.

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

- User Guidance

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- FjordPhantom (malware)
- GodFather (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.

## ATT&CK contributors

- Liran Ravich, CardinalOps
