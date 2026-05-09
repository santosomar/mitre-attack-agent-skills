---
name: attack-ics-t1694-002-hardcoded-credentials
description: "Analyze MITRE ATT&CK T1694.002 Hardcoded Credentials in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1694.002, Hardcoded Credentials, or ics ATT&CK. Adversaries may leverage credentials that are hardcoded in software or firmware to gain an unauthorized interactive user session to an asset."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T1694.002
  attack_stix_id: attack-pattern--6b335943-c3af-430e-a135-ab09623bdc20
  attack_version: "1.0"
  attack_modified: "2026-04-23T19:32:38.851Z"
---

# MITRE ATT&CK T1694.002: Hardcoded Credentials

## When to use this skill

Use this skill when the task involves T1694.002, Hardcoded Credentials, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK sub-technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T1694.002
- Technique name: Hardcoded Credentials
- Type: sub-technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1694/002
- Tactics: lateral-movement, persistence
- Platforms: Not specified
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may leverage credentials that are hardcoded in software or firmware to gain an unauthorized interactive user session to an asset. Examples credentials that may be hardcoded in an asset include:

* Username/Passwords
* Cryptographic keys/Certificates
* API tokens

Unlike [Default Credentials](https://attack.mitre.org/techniques/T0812), these credentials are built into the system in a way that they either cannot be changed by the asset owner, or may be infeasible to change because of the impact it would cause to the control system operation. These credentials may be reused across whole product lines or device models and are often not published or known to the owner and operators of the asset.(Citation: ICS-ALERT-13-164-01)(Citation: OT IceFall)

Adversaries may utilize these hardcoded credentials to move throughout the control system environment or provide reliable access for their tools to interact with industrial assets.

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

- Access Management

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- INCONTROLLER (malware)
- Stuxnet (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
