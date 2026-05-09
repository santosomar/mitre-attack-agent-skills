---
name: attack-mob-t1417-001-keylogging
description: "Analyze MITRE ATT&CK T1417.001 Keylogging in the mobile matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1417.001, Keylogging, or mobile ATT&CK. Adversaries may log user keystrokes to intercept credentials or other information from the user as the user types them."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: mobile
  attack_id: T1417.001
  attack_stix_id: attack-pattern--b1c95426-2550-4621-8028-ceebf28b3a47
  attack_version: "1.1"
  attack_modified: "2025-10-24T17:49:14.276Z"
---

# MITRE ATT&CK T1417.001: Keylogging

## When to use this skill

Use this skill when the task involves T1417.001, Keylogging, mobile ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK sub-technique.

## Technique context

- ATT&CK domain: mobile
- ATT&CK ID: T1417.001
- Technique name: Keylogging
- Type: sub-technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1417/001
- Tactics: collection, credential-access
- Platforms: Android, iOS
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may log user keystrokes to intercept credentials or other information from the user as the user types them.

Some methods of keylogging include:

* Masquerading as a legitimate third-party keyboard to record user keystrokes.(Citation: Zeltser-Keyboard) On both Android and iOS, users must explicitly authorize the use of third-party keyboard apps. Users should be advised to use extreme caution before granting this authorization when it is requested.
* Abusing accessibility features. On Android, adversaries may abuse accessibility features to record keystrokes by registering an `AccessibilityService` class, overriding the `onAccessibilityEvent` method, and listening for the `AccessibilityEvent.TYPE_VIEW_TEXT_CHANGED` event type. The event object passed into the function will contain the data that the user typed. 
*Additional methods of keylogging may be possible if root access is available.

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
- User Guidance

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- Anubis (malware)
- BOULDSPY (malware)
- BRATA (malware)
- BusyGasper (malware)
- Cerberus (malware)
- Chameleon (malware)
- Crocodilus (malware)
- DocSwap (malware)
- Drinik (malware)
- Escobar (malware)
- EventBot (malware)
- Exobot (malware)
- FlexiSpy (tool)
- GodFather (malware)
- Gustuff (malware)
- Monokle (malware)
- S.O.V.A. (malware)
- SharkBot (malware)
- VajraSpy (malware)
- Windshift (intrusion-set)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
