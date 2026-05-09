---
name: attack-mob-t1422-001-internet-connection-discovery
description: "Analyze MITRE ATT&CK T1422.001 Internet Connection Discovery in the mobile matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1422.001, Internet Connection Discovery, or mobile ATT&CK. Adversaries may check for Internet connectivity on compromised systems."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: mobile
  attack_id: T1422.001
  attack_stix_id: attack-pattern--45a5fe76-eda3-4d40-8f22-c186efd6278d
  attack_version: "1.0"
  attack_modified: "2024-02-20T23:39:08.047Z"
---

# MITRE ATT&CK T1422.001: Internet Connection Discovery

## When to use this skill

Use this skill when the task involves T1422.001, Internet Connection Discovery, mobile ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK sub-technique.

## Technique context

- ATT&CK domain: mobile
- ATT&CK ID: T1422.001
- Technique name: Internet Connection Discovery
- Type: sub-technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1422/001
- Tactics: discovery
- Platforms: Android, iOS
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may check for Internet connectivity on compromised systems. This may be performed during automated discovery and can be accomplished in numerous ways such as using `adb shell netstat` for Android.(Citation: adb_commands)

Adversaries may use the results and responses from these requests to determine if the mobile devices are capable of communicating with adversary-owned C2 servers before attempting to connect to them. The results may also be used to identify routes, redirectors, and proxy servers.

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

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- AbstractEmu (malware)
- Asacub (malware)
- BOULDSPY (malware)
- CarbonSteal (malware)
- Corona Updates (malware)
- EventBot (malware)
- Exobot (malware)
- Exodus (malware)
- FakeSpy (malware)
- FlyTrap (malware)
- Hornbill (malware)
- INSOMNIA (malware)
- Monokle (malware)
- Pegasus for Android (malware)
- RedDrop (malware)
- TERRACOTTA (malware)
- TianySpy (malware)
- TrickMo (malware)
- ViperRAT (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
