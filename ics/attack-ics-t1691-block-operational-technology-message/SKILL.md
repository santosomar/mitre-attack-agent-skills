---
name: attack-ics-t1691-block-operational-technology-message
description: "Analyze MITRE ATT&CK T1691 Block Operational Technology Message in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1691, Block Operational Technology Message, or ics ATT&CK. Adversaries may block messages between systems and devices in an OT/ICS environment to disrupt processes."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T1691
  attack_stix_id: attack-pattern--338f4364-2269-4f70-9079-b20384b16628
  attack_version: "1.0"
  attack_modified: "2026-04-23T18:49:15.673Z"
---

# MITRE ATT&CK T1691: Block Operational Technology Message

## When to use this skill

Use this skill when the task involves T1691, Block Operational Technology Message, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T1691
- Technique name: Block Operational Technology Message
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1691
- Tactics: inhibit-response-function
- Platforms: Not specified
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may block messages between systems and devices in an OT/ICS environment to disrupt processes. Messages typically fall into two categories: (1) reporting messages that contain telemetry data about the current state of systems, devices, and processes and (2) command messages that contain instructions to control systems, devices, and processes. Both types of messages are critical for the proper functioning of industrial control processes and failure of the messages to reach their intended destinations could inhibit response functions or create an unsafe condition that could have physical impacts.(Citation: Bonnie Zhu, Anthony Joseph, Shankar Sastry 2011)(Citation: Electricity Information Sharing and Analysis Center; SANS Industrial Control Systems March 2016)

Adversaries may block communications by either making modifications to software ([System Firmware](https://attack.mitre.org/techniques/T0857), [Module Firmware](https://attack.mitre.org/techniques/T0839), [Hooking](https://attack.mitre.org/techniques/T0874), and [Rootkit](https://attack.mitre.org/techniques/T0851)) and services ([Service Stop](https://attack.mitre.org/techniques/T0881), [Denial of Service](https://attack.mitre.org/techniques/T0814)) on systems and devices or by positioning themselves between systems and devices and intercepting and blocking the communications such as the case with an [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T0830) attack.

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
- Out-of-Band Communications Channel
- Static Network Configuration

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
