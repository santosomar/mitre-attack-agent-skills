---
name: attack-ics-t0865-spearphishing-attachment
description: "Analyze MITRE ATT&CK T0865 Spearphishing Attachment in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0865, Spearphishing Attachment, or ics ATT&CK. Adversaries may use a spearphishing attachment, a variant of spearphishing, as a form of a social engineering attack against specific targets."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0865
  attack_stix_id: attack-pattern--648f995e-9c3a-41e4-aeee-98bb41037426
  attack_version: "1.1"
  attack_modified: "2025-04-16T21:26:15.346Z"
---

# MITRE ATT&CK T0865: Spearphishing Attachment

## When to use this skill

Use this skill when the task involves T0865, Spearphishing Attachment, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0865
- Technique name: Spearphishing Attachment
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0865
- Tactics: initial-access
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may use a spearphishing attachment, a variant of spearphishing, as a form of a social engineering attack against specific targets. Spearphishing attachments are different from other forms of spearphishing in that they employ malware attached to an email. All forms of spearphishing are electronically delivered and target a specific individual, company, or industry. In this scenario, adversaries attach a file to the spearphishing email and usually rely upon [User Execution](https://attack.mitre.org/techniques/T0863) to gain execution and access. (Citation: Enterprise ATT&CK October 2019) 

A Chinese spearphishing campaign running from December 9, 2011 through February 29, 2012, targeted ONG organizations and their employees. The emails were constructed with a high level of sophistication to convince employees to open the malicious file attachments. (Citation: CISA AA21-201A Pipeline Intrusion July 2021)

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

- Antivirus/Antimalware
- Network Intrusion Prevention
- Restrict Web-Based Content
- User Training

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- ALLANITE (intrusion-set)
- APT33 (intrusion-set)
- Backdoor.Oldrea (malware)
- BlackEnergy (malware)
- Lazarus Group (intrusion-set)
- OilRig (intrusion-set)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
