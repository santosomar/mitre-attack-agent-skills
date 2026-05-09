---
name: attack-ics-t0887-wireless-sniffing
description: "Analyze MITRE ATT&CK T0887 Wireless Sniffing in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0887, Wireless Sniffing, or ics ATT&CK. Adversaries may seek to capture radio frequency (RF) communication used for remote control and reporting in distributed environments."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0887
  attack_stix_id: attack-pattern--0fe075d5-beac-4d02-b93e-0f874997db72
  attack_version: "1.1"
  attack_modified: "2025-04-16T21:26:10.392Z"
---

# MITRE ATT&CK T0887: Wireless Sniffing

## When to use this skill

Use this skill when the task involves T0887, Wireless Sniffing, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0887
- Technique name: Wireless Sniffing
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0887
- Tactics: collection, discovery
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may seek to capture radio frequency (RF) communication used for remote control and reporting in distributed environments. RF communication frequencies vary between 3 kHz to 300 GHz, although are commonly between 300 MHz to 6 GHz. (Citation: Candell, R., Hany, M., Lee, K. B., Liu,Y., Quimby, J., Remley, K. April 2018)  The wavelength and frequency of the signal affect how the signal propagates through open air, obstacles (e.g. walls and trees) and the type of radio required to capture them. These characteristics are often standardized in the protocol and hardware and may have an effect on how the signal is captured. Some examples of wireless protocols that may be found in cyber-physical environments are: WirelessHART, Zigbee, WIA-FA, and 700 MHz Public Safety Spectrum. 

Adversaries may capture RF communications by using specialized hardware, such as software defined radio (SDR), handheld radio, or a computer with radio demodulator tuned to the communication frequency. (Citation: Bastille April 2017) Information transmitted over a wireless medium may be captured in-transit whether the sniffing device is the intended destination or not. This technique may be particularly useful to an adversary when the communications are not encrypted. (Citation: Gallagher, S. April 2017) 

In the 2017 Dallas Siren incident, it is suspected that adversaries likely captured wireless command message broadcasts on a 700 MHz frequency during a regular test of the system. These messages were later replayed to trigger the alarm systems. (Citation: Gallagher, S. April 2017)

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

- Encrypt Network Traffic
- Minimize Wireless Signal Propagation

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- No group or software uses relationships were included for this technique in the source STIX bundle.

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.

## ATT&CK contributors

- ICSCoE Japan
