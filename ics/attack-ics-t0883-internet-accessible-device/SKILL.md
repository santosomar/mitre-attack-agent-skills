---
name: attack-ics-t0883-internet-accessible-device
description: "Analyze MITRE ATT&CK T0883 Internet Accessible Device in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0883, Internet Accessible Device, or ics ATT&CK. Adversaries may gain access into industrial environments through systems exposed directly to the internet for remote access rather than through [External Remote Services](https://attack.mitre.org/techniques/T0822)."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0883
  attack_stix_id: attack-pattern--f8df6b57-14bc-425f-9a91-6f59f6799307
  attack_version: "1.0"
  attack_modified: "2025-04-16T21:26:20.494Z"
---

# MITRE ATT&CK T0883: Internet Accessible Device

## When to use this skill

Use this skill when the task involves T0883, Internet Accessible Device, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0883
- Technique name: Internet Accessible Device
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0883
- Tactics: initial-access
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may gain access into industrial environments through systems exposed directly to the internet for remote access rather than through [External Remote Services](https://attack.mitre.org/techniques/T0822). Internet Accessible Devices are exposed to the internet unintentionally or intentionally without adequate protections. This may allow for adversaries to move directly into the control system network. Access onto these devices is accomplished without the use of exploits, these would be represented within the [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T0819) technique.

Adversaries may leverage built in functions for remote access which may not be protected or utilize minimal legacy protections that may be targeted. (Citation: NCCIC January 2014) These services may be discoverable through the use of online scanning tools. 

In the case of the Bowman dam incident, adversaries leveraged access to the dam control network through a cellular modem. Access to the device was protected by password authentication, although the application was vulnerable to brute forcing. (Citation: NCCIC January 2014) (Citation: Danny Yadron December 2015) (Citation: Mark Thompson March 2016)

In Trend Micros manufacturing deception operations adversaries were detected leveraging direct internet access to an ICS environment through the exposure of operational protocols such as Siemens S7, Omron FINS, and EtherNet/IP, in addition to misconfigured VNC access. (Citation: Stephen Hilt, Federico Maggi, Charles Perine, Lord Remorin, Martin Rsler, and Rainer Vosseler)

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

- Network Segmentation

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- Fuxnet (malware)
- Unitronics Defacement Campaign (campaign)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
