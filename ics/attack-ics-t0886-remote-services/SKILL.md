---
name: attack-ics-t0886-remote-services
description: "Analyze MITRE ATT&CK T0886 Remote Services in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0886, Remote Services, or ics ATT&CK. Adversaries may leverage remote services to move between assets and network segments."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0886
  attack_stix_id: attack-pattern--e1f9cdd2-9511-4fca-90d7-f3e92cfdd0bf
  attack_version: "1.1"
  attack_modified: "2025-04-16T21:26:19.525Z"
---

# MITRE ATT&CK T0886: Remote Services

## When to use this skill

Use this skill when the task involves T0886, Remote Services, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0886
- Technique name: Remote Services
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0886
- Tactics: initial-access, lateral-movement
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may leverage remote services to move between assets and network segments. These services are often used to allow operators to interact with systems remotely within the network, some examples are RDP, SMB, SSH, and other similar mechanisms. (Citation: Blake Johnson, Dan Caban, Marina Krotofil, Dan Scali, Nathan Brubaker, Christopher Glyer December 2017) (Citation: Dragos December 2017) (Citation: Joe Slowik April 2019) 

Remote services could be used to support remote access, data transmission, authentication, name resolution, and other remote functions. Further, remote services may be necessary to allow operators and administrators to configure systems within the network from their engineering or management workstations. An adversary may use this technique to access devices which may be dual-homed (Citation: Blake Johnson, Dan Caban, Marina Krotofil, Dan Scali, Nathan Brubaker, Christopher Glyer December 2017) to multiple network segments, and can be used for [Program Download](https://attack.mitre.org/techniques/T0843) or to execute attacks on control devices directly through [Valid Accounts](https://attack.mitre.org/techniques/T0859).

Specific remote services (RDP & VNC) may be a precursor to enable [Graphical User Interface](https://attack.mitre.org/techniques/T0823) execution on devices such as HMIs or engineering workstation software.

Based on incident data, CISA and FBI assessed that Chinese state-sponsored actors also compromised various authorized remote access channels, including systems designed to transfer data and/or allow access between corporate and ICS networks.  (Citation: CISA AA21-201A Pipeline Intrusion July 2021)

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
- Authorization Enforcement
- Filter Network Traffic
- Human User Authentication
- Network Allowlists
- Network Segmentation
- Password Policies
- Software Process and Device Authentication
- User Account Management

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- 2015 Ukraine Electric Power Attack (campaign)
- 2016 Ukraine Electric Power Attack (campaign)
- 2025 Poland Wiper Attacks (campaign)
- INCONTROLLER (malware)
- REvil (malware)
- Stuxnet (malware)
- Triton Safety Instrumented System Attack (campaign)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.

## ATT&CK contributors

- Daisuke Suzuki
