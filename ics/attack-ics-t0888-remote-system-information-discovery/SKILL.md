---
name: attack-ics-t0888-remote-system-information-discovery
description: "Analyze MITRE ATT&CK T0888 Remote System Information Discovery in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0888, Remote System Information Discovery, or ics ATT&CK. An adversary may attempt to get detailed information about remote systems and their peripherals, such as make/model, role, and configuration."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0888
  attack_stix_id: attack-pattern--2fedbe69-581f-447d-8a78-32ee7db939a9
  attack_version: "1.1"
  attack_modified: "2025-04-16T21:26:12.694Z"
---

# MITRE ATT&CK T0888: Remote System Information Discovery

## When to use this skill

Use this skill when the task involves T0888, Remote System Information Discovery, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0888
- Technique name: Remote System Information Discovery
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0888
- Tactics: discovery
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

An adversary may attempt to get detailed information about remote systems and their peripherals, such as make/model, role, and configuration. Adversaries may use information from Remote System Information Discovery to aid in targeting and shaping follow-on behaviors. For example, the system's operational role and model information can dictate whether it is a relevant target for the adversary's operational objectives. In addition, the system's configuration may be used to scope subsequent technique usage. 

Requests for system information are typically implemented using automation and management protocols and are often automatically requested by vendor software during normal operation. This information may be used to tailor management actions, such as program download and system or module firmware. An adversary may leverage this same information by issuing calls directly to the system's API.

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

- Static Network Configuration

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- 2025 Poland Wiper Attacks (campaign)
- Backdoor.Oldrea (malware)
- INCONTROLLER (malware)
- Industroyer (malware)
- Industroyer2 (malware)
- Stuxnet (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
