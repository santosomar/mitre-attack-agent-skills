---
name: attack-ics-t0862-supply-chain-compromise
description: "Analyze MITRE ATT&CK T0862 Supply Chain Compromise in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0862, Supply Chain Compromise, or ics ATT&CK. Adversaries may perform supply chain compromise to gain control systems environment access by means of infected products, software, and workflows."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0862
  attack_stix_id: attack-pattern--5e0f75da-e108-4688-a6de-a4f07cc2cbe3
  attack_version: "1.1"
  attack_modified: "2025-04-16T21:26:14.822Z"
---

# MITRE ATT&CK T0862: Supply Chain Compromise

## When to use this skill

Use this skill when the task involves T0862, Supply Chain Compromise, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0862
- Technique name: Supply Chain Compromise
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0862
- Tactics: initial-access
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may perform supply chain compromise to gain control systems environment access by means of infected products, software, and workflows. Supply chain compromise is the manipulation of products, such as devices or software, or their delivery mechanisms before receipt by the end consumer. Adversary compromise of these products and mechanisms is done for the goal of data or system compromise, once infected products are introduced to the target environment. 

Supply chain compromise can occur at all stages of the supply chain, from manipulation of development tools and environments to manipulation of developed products and tools distribution mechanisms. This may involve the compromise and replacement of legitimate software and patches, such as on third party or vendor websites. Targeting of supply chain compromise can be done in attempts to infiltrate the environments of a specific audience. In control systems environments with assets in both the IT and OT networks, it is possible a supply chain compromise affecting the IT environment could enable further access to the OT environment.   

Counterfeit devices may be introduced to the global supply chain posing safety and cyber risks to asset owners and operators. These devices may not meet the safety, engineering and manufacturing requirements of regulatory bodies but may feature tagging indicating conformance with industry standards. Due to the lack of adherence to standards and overall lesser quality, the counterfeit products may pose a serious safety and operational risk. (Citation: Control Global May 2019) 

Yokogawa identified instances in which their customers received counterfeit differential pressure transmitters using the Yokogawa logo. The counterfeit transmitters were nearly indistinguishable with a semblance of functionality and interface that mimics the genuine product. (Citation: Control Global May 2019) 

F-Secure Labs analyzed the approach the adversary used to compromise victim systems with Havex. (Citation: Daavid Hentunen, Antti Tikkanen June 2014) The adversary planted trojanized software installers available on legitimate ICS/SCADA vendor websites. After being downloaded, this software infected the host computer with a Remote Access Trojan (RAT).

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

- Audit
- Code Signing
- Supply Chain Management
- Update Software
- Vulnerability Scanning

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- Backdoor.Oldrea (malware)
- Dragonfly (intrusion-set)
- TEMP.Veles (intrusion-set)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
