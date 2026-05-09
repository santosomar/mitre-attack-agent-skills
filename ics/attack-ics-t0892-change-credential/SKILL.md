---
name: attack-ics-t0892-change-credential
description: "Analyze MITRE ATT&CK T0892 Change Credential in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0892, Change Credential, or ics ATT&CK. Adversaries may modify software and device credentials to prevent operator and responder access."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0892
  attack_stix_id: attack-pattern--fab8fc7d-f27f-4fbb-9de6-44740aade05f
  attack_version: "1.0"
  attack_modified: "2025-04-16T21:26:20.690Z"
---

# MITRE ATT&CK T0892: Change Credential

## When to use this skill

Use this skill when the task involves T0892, Change Credential, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0892
- Technique name: Change Credential
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0892
- Tactics: inhibit-response-function
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may modify software and device credentials to prevent operator and responder access. Depending on the device, the modification or addition of this password could prevent any device configuration actions from being accomplished and may require a factory reset or replacement of hardware. These credentials are often built-in features provided by the device vendors as a means to restrict access to management interfaces.

An adversary with access to valid or hardcoded credentials could change the credential to prevent future authorized device access. Change Credential may be especially damaging when paired with other techniques such as Modify Program, Data Destruction, or Modify Controller Tasking. In these cases, a device’s configuration may be destroyed or include malicious actions for the process environment, which cannot not be removed through normal device configuration actions. 

Additionally, recovery of the device and original configuration may be difficult depending on the features provided by the device. In some cases, these passwords cannot be removed onsite and may require that the device be sent back to the vendor for additional recovery steps.


A chain of incidents occurred in Germany, where adversaries locked operators out of their building automation system (BAS) controllers by enabling a previously unset BCU key. (Citation: German BAS Lockout Dec 2021)

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

- Data Backup
- Password Policies
- Redundancy of Service

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- 2025 Poland Wiper Attacks (campaign)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.

## ATT&CK contributors

- Felix Eberstaller
