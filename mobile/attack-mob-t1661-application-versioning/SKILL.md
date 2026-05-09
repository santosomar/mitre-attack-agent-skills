---
name: attack-mob-t1661-application-versioning
description: "Analyze MITRE ATT&CK T1661 Application Versioning in the mobile matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1661, Application Versioning, or mobile ATT&CK. An adversary may push an update to a previously benign application to add malicious code."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: mobile
  attack_id: T1661
  attack_stix_id: attack-pattern--28fdd23d-aee3-4afe-bc3f-5f1f52929258
  attack_version: "1.0"
  attack_modified: "2023-09-28T15:36:11.282Z"
---

# MITRE ATT&CK T1661: Application Versioning

## When to use this skill

Use this skill when the task involves T1661, Application Versioning, mobile ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: mobile
- ATT&CK ID: T1661
- Technique name: Application Versioning
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1661
- Tactics: defense-evasion, initial-access
- Platforms: Android, iOS
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

An adversary may push an update to a previously benign application to add malicious code. This can be accomplished by pushing an initially benign, functional application to a trusted application store, such as the Google Play Store or the Apple App Store. This allows the adversary to establish a trusted userbase that may grant permissions to the application prior to the introduction of malicious code. Then, an application update could be pushed to introduce malicious code.(Citation: android_app_breaking_bad)

This technique could also be accomplished by compromising a developer’s account. This would allow an adversary to take advantage of an existing userbase without having to establish the userbase themselves.

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

- Enterprise Policy
- Use Recent OS Version

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- SharkBot (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.

## ATT&CK contributors

- Edward Stevens, BT Security
- Adam Lichters
