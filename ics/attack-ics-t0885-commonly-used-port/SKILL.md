---
name: attack-ics-t0885-commonly-used-port
description: "Analyze MITRE ATT&CK T0885 Commonly Used Port in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0885, Commonly Used Port, or ics ATT&CK. Adversaries may communicate over a commonly used port to bypass firewalls or network detection systems and to blend in with normal network activity, to avoid more detailed inspection."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0885
  attack_stix_id: attack-pattern--e6c31185-8040-4267-83d3-b217b8a92f07
  attack_version: "1.1"
  attack_modified: "2025-04-16T21:26:19.961Z"
---

# MITRE ATT&CK T0885: Commonly Used Port

## When to use this skill

Use this skill when the task involves T0885, Commonly Used Port, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0885
- Technique name: Commonly Used Port
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0885
- Tactics: command-and-control
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may communicate over a commonly used port to bypass firewalls or network detection systems and to blend in with normal network activity, to avoid more detailed inspection. They may use the protocol associated with the port, or a completely different protocol. They may use commonly open ports, such as the examples provided below. 
 
 * TCP:80 (HTTP) 
 * TCP:443 (HTTPS) 
 * TCP/UDP:53 (DNS) 
 * TCP:1024-4999 (OPC on XP/Win2k3) 
 * TCP:49152-65535 (OPC on Vista and later) 
 * TCP:23 (TELNET) 
 * UDP:161 (SNMP) 
 * TCP:502 (MODBUS) 
 * TCP:102 (S7comm/ISO-TSAP) 
 * TCP:20000 (DNP3) 
 * TCP:44818 (Ethernet/IP)

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

- Disable or Remove Feature or Program
- Human User Authentication
- Network Intrusion Prevention
- Network Segmentation

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- 2015 Ukraine Electric Power Attack (campaign)
- 2025 Poland Wiper Attacks (campaign)
- FrostyGoop (malware)
- Stuxnet (malware)
- Triton (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.

## ATT&CK contributors

- Matan Dobrushin - Otorio
