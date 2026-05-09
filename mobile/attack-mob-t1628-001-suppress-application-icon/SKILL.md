---
name: attack-mob-t1628-001-suppress-application-icon
description: "Analyze MITRE ATT&CK T1628.001 Suppress Application Icon in the mobile matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1628.001, Suppress Application Icon, or mobile ATT&CK. A malicious application could suppress its icon from being displayed to the user in the application launcher."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: mobile
  attack_id: T1628.001
  attack_stix_id: attack-pattern--f05fc151-aa62-47e3-ae57-2d1b23d64bf6
  attack_version: "1.1"
  attack_modified: "2025-10-24T17:49:35.410Z"
---

# MITRE ATT&CK T1628.001: Suppress Application Icon

## When to use this skill

Use this skill when the task involves T1628.001, Suppress Application Icon, mobile ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK sub-technique.

## Technique context

- ATT&CK domain: mobile
- ATT&CK ID: T1628.001
- Technique name: Suppress Application Icon
- Type: sub-technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1628/001
- Tactics: defense-evasion
- Platforms: Android
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

A malicious application could suppress its icon from being displayed to the user in the application launcher. This hides the fact that it is installed, and can make it more difficult for the user to uninstall the application. Hiding the application's icon programmatically does not require any special permissions. 

This behavior has been seen in the BankBot/Spy Banker family of malware.(Citation: android-trojan-steals-paypal-2fa)(Citation: sunny-stolen-credentials)(Citation: bankbot-spybanker) 

Beginning in Android 10, changes were introduced to inhibit malicious applications’ ability to hide their icon. If an app is a system app, requests no permissions, or does not have a launcher activity, the application’s icon will be fully hidden. Further, if the device is fully managed or the application is in a work profile, the icon will be fully hidden. Otherwise, a synthesized activity is shown, which is a launcher icon that represents the app’s details page in the system settings. If the user clicks the synthesized activity in the launcher, they are taken to the application’s details page in the system settings.(Citation: Android 10 Limitations to Hiding App Icons)(Citation: LauncherApps getActivityList)

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

- Use Recent OS Version
- User Guidance

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- Agent Smith (malware)
- Android/AdDisplay.Ashas (malware)
- BusyGasper (malware)
- Cerberus (malware)
- Desert Scorpion (malware)
- DoubleAgent (malware)
- Drinik (malware)
- FakeSpy (malware)
- FlexiSpy (tool)
- FlixOnline (malware)
- Ginp (malware)
- Gustuff (malware)
- Mandrake (malware)
- Rotexy (malware)
- S.O.V.A. (malware)
- SimBad (malware)
- SpyC23 (malware)
- Tiktok Pro (malware)
- Twitoor (malware)
- ViceLeaker (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.

## ATT&CK contributors

- Emily Ratliff, IBM
