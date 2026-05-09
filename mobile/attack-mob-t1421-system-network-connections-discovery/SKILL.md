---
name: attack-mob-t1421-system-network-connections-discovery
description: "Analyze MITRE ATT&CK T1421 System Network Connections Discovery in the mobile matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1421, System Network Connections Discovery, or mobile ATT&CK. Adversaries may attempt to get a listing of network connections to or from the compromised device they are currently accessing or from remote systems by querying for information over the network."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: mobile
  attack_id: T1421
  attack_stix_id: attack-pattern--dd818ea5-adf5-41c7-93b5-f3b839a219fb
  attack_version: "2.1"
  attack_modified: "2025-10-24T17:49:29.321Z"
---

# MITRE ATT&CK T1421: System Network Connections Discovery

## When to use this skill

Use this skill when the task involves T1421, System Network Connections Discovery, mobile ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: mobile
- ATT&CK ID: T1421
- Technique name: System Network Connections Discovery
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1421
- Tactics: discovery
- Platforms: Android
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may attempt to get a listing of network connections to or from the compromised device they are currently accessing or from remote systems by querying for information over the network. 

 

This is typically accomplished by utilizing device APIs to collect information about nearby networks, such as Wi-Fi, Bluetooth, and cellular tower connections. On Android, this can be done by querying the respective APIs: 

 

* `WifiInfo` for information about the current Wi-Fi connection, as well as nearby Wi-Fi networks. Querying the `WiFiInfo` API requires the application to hold the `ACCESS_FINE_LOCATION` permission. 

* `BluetoothAdapter` for information about Bluetooth devices, which also requires the application to hold several permissions granted by the user at runtime. 

* For Android versions prior to Q, applications can use the `TelephonyManager.getNeighboringCellInfo()` method. For Q and later, applications can use the `TelephonyManager.getAllCellInfo()` method. Both methods require the application hold the `ACCESS_FINE_LOCATION` permission.

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

- No ATT&CK mitigation relationships were present in the source STIX bundle.

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- C0033 (campaign)
- Exodus (malware)
- FakeSpy (malware)
- FlexiSpy (tool)
- LightSpy (malware)
- Monokle (malware)
- Pallas (malware)
- Pegasus for iOS (malware)
- ViperRAT (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
