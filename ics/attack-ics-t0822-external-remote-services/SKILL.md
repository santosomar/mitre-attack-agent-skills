---
name: attack-ics-t0822-external-remote-services
description: "Analyze MITRE ATT&CK T0822 External Remote Services in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0822, External Remote Services, or ics ATT&CK. Adversaries may leverage external remote services as a point of initial access into your network."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0822
  attack_stix_id: attack-pattern--8d2f3bab-507c-4424-b58b-edc977bd215c
  attack_version: "1.1"
  attack_modified: "2025-04-16T21:26:16.385Z"
---

# MITRE ATT&CK T0822: External Remote Services

## When to use this skill

Use this skill when the task involves T0822, External Remote Services, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0822
- Technique name: External Remote Services
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0822
- Tactics: initial-access
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may leverage external remote services as a point of initial access into your network. These services allow users to connect to internal network resources from external locations. Examples are VPNs, Citrix, and other access mechanisms. Remote service gateways often manage connections and credential authentication for these services. (Citation: Daniel Oakley, Travis Smith, Tripwire)

External remote services allow administration of a control system from outside the system. Often, vendors and internal engineering groups have access to external remote services to control system networks via the corporate network. In some cases, this access is enabled directly from the internet. While remote access enables ease of maintenance when a control system is in a remote area, compromise of remote access solutions is a liability. The adversary may use these services to gain access to and execute attacks against a control system network. Access to valid accounts is often a requirement. 

As they look for an entry point into the control system network, adversaries may begin searching for existing point-to-point VPN implementations at trusted third party networks or through remote support employee connections where split tunneling is enabled. (Citation: Electricity Information Sharing and Analysis Center; SANS Industrial Control Systems March 2016)

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

- Account Use Policies
- Disable or Remove Feature or Program
- Limit Access to Resource Over Network
- Multi-factor Authentication
- Network Segmentation
- Password Policies
- User Account Management

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- 2015 Ukraine Electric Power Attack (campaign)
- 2025 Poland Wiper Attacks (campaign)
- Fuxnet (malware)
- Maroochy Water Breach (campaign)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
