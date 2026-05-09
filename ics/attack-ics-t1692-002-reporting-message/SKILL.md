---
name: attack-ics-t1692-002-reporting-message
description: "Analyze MITRE ATT&CK T1692.002 Reporting Message in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1692.002, Reporting Message, or ics ATT&CK. Adversaries may spoof reporting messages in control system environments for evasion and to impair process control."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T1692.002
  attack_stix_id: attack-pattern--527106b3-95a2-4ed2-bf89-db7f0e4d0da0
  attack_version: "1.0"
  attack_modified: "2026-04-23T19:01:42.644Z"
---

# MITRE ATT&CK T1692.002: Reporting Message

## When to use this skill

Use this skill when the task involves T1692.002, Reporting Message, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK sub-technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T1692.002
- Technique name: Reporting Message
- Type: sub-technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1692/002
- Tactics: evasion, impair-process-control
- Platforms: Not specified
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may spoof reporting messages in control system environments for evasion and to impair process control. In control systems, reporting messages contain telemetry data (e.g., I/O values) pertaining to the current state of equipment and the industrial process. Reporting messages are important for monitoring the normal operation of a system or identifying important events such as deviations from expected values.

If an adversary has the ability to Spoof Reporting Messages, they can impact the control system in many ways. The adversary can Spoof Reporting Messages that state that the process is operating normally, as a form of evasion. The adversary could also Spoof Reporting Messages to make the defenders and operators think that other errors are occurring in order to distract them from the actual source of a problem.(Citation: Bonnie Zhu, Anthony Joseph, Shankar Sastry 2011)

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

- Communication Authenticity
- Filter Network Traffic
- Network Allowlists
- Network Segmentation
- Software Process and Device Authentication

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- Maroochy Water Breach (campaign)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
