---
name: attack-mob-t1641-001-transmitted-data-manipulation
description: "Analyze MITRE ATT&CK T1641.001 Transmitted Data Manipulation in the mobile matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1641.001, Transmitted Data Manipulation, or mobile ATT&CK. Adversaries may alter data en route to storage or other systems in order to manipulate external outcomes or hide activity."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: mobile
  attack_id: T1641.001
  attack_stix_id: attack-pattern--74e6003f-c7f4-4047-983b-708cc19b96b6
  attack_version: "1.1"
  attack_modified: "2025-10-24T17:48:57.794Z"
---

# MITRE ATT&CK T1641.001: Transmitted Data Manipulation

## When to use this skill

Use this skill when the task involves T1641.001, Transmitted Data Manipulation, mobile ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK sub-technique.

## Technique context

- ATT&CK domain: mobile
- ATT&CK ID: T1641.001
- Technique name: Transmitted Data Manipulation
- Type: sub-technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1641/001
- Tactics: impact
- Platforms: Android
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may alter data en route to storage or other systems in order to manipulate external outcomes or hide activity. By manipulating transmitted data, adversaries may attempt to affect a business process, organizational understanding, or decision making.

Manipulation may be possible over a network connection or between system processes where there is an opportunity to deploy a tool that will intercept and change information. The type of modification and the impact it will have depends on the target transmission mechanism as well as the goals and objectives of the adversary. For complex systems, an adversary would likely need special expertise and possibly access to specialized software related to the system, typically gained through a prolonged information gathering campaign, in order to have the desired impact.

One method to achieve [Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1641/001) is by modifying the contents of the device clipboard. Malicious applications may monitor clipboard activity through the `ClipboardManager.OnPrimaryClipChangedListener` interface on Android to determine when clipboard contents have changed. Listening to clipboard activity, reading clipboard contents, and modifying clipboard contents requires no explicit application permissions and can be performed by applications running in the background. However, this behavior has changed with the release of Android 10.

Adversaries may use [Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1641/001) to replace text prior to being pasted. For example, replacing a copied Bitcoin wallet address with a wallet address that is under adversarial control.

[Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1641/001) was seen within the Android/Clipper.C trojan. This sample was detected by ESET in an application distributed through the Google Play Store targeting cryptocurrency wallet numbers.(Citation: ESET Clipboard Modification February 2019)

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

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- BRATA (malware)
- S.O.V.A. (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
