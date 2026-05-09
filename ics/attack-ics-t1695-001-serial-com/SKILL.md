---
name: attack-ics-t1695-001-serial-com
description: "Analyze MITRE ATT&CK T1695.001 Serial COM in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1695.001, Serial COM, or ics ATT&CK. Adversaries may block access to serial COM to prevent instructions or configurations from reaching target devices."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T1695.001
  attack_stix_id: attack-pattern--55e7e5c1-3760-4451-bae0-e79b29f452c5
  attack_version: "1.0"
  attack_modified: "2026-04-23T19:59:10.079Z"
---

# MITRE ATT&CK T1695.001: Serial COM

## When to use this skill

Use this skill when the task involves T1695.001, Serial COM, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK sub-technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T1695.001
- Technique name: Serial COM
- Type: sub-technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1695/001
- Tactics: inhibit-response-function
- Platforms: Not specified
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may block access to serial COM to prevent instructions or configurations from reaching target devices. Serial Communication ports (COM) allow communication with control system devices. Devices can receive command and configuration messages over such serial COM. Devices also use serial COM to send command and reporting messages. Blocking device serial COM may also block command messages and block reporting messages.

A serial to Ethernet converter is often connected to a serial COM to facilitate communication between serial and Ethernet devices. One approach to blocking a serial COM would be to create and hold open a TCP session with the Ethernet side of the converter. A serial to Ethernet converter may have a few ports open to facilitate multiple communications. For example, if there are three serial COM available -- 1, 2 and 3 --, the converter might be listening on the corresponding ports 20001, 20002, and 20003. If a TCP/IP connection is opened with one of these ports and held open, then the port will be unavailable for use by another party. One way the adversary could achieve this would be to initiate a TCP session with the serial to Ethernet converter at 10.0.0.1 via Telnet on serial port 1 with the following command: telnet 10.0.0.1 20001.

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

- Network Allowlists
- Network Segmentation
- Out-of-Band Communications Channel

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- 2015 Ukraine Electric Power Attack (campaign)
- Industroyer (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
