---
name: attack-ics-t0830-adversary-in-the-middle
description: "Analyze MITRE ATT&CK T0830 Adversary-in-the-Middle in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0830, Adversary-in-the-Middle, or ics ATT&CK. Adversaries with privileged network access may seek to modify network traffic in real time using adversary-in-the-middle (AiTM) attacks."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0830
  attack_stix_id: attack-pattern--9a505987-ab05-4f46-a9a6-6441442eec3b
  attack_version: "2.0"
  attack_modified: "2025-04-16T21:26:16.777Z"
---

# MITRE ATT&CK T0830: Adversary-in-the-Middle

## When to use this skill

Use this skill when the task involves T0830, Adversary-in-the-Middle, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0830
- Technique name: Adversary-in-the-Middle
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0830
- Tactics: collection
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries with privileged network access may seek to modify network traffic in real time using adversary-in-the-middle (AiTM) attacks. (Citation: Gabriel Sanchez October 2017) This type of attack allows the adversary to intercept traffic to and/or from a particular device on the network. If a AiTM attack is established, then the adversary has the ability to block, log, modify, or inject traffic into the communication stream. There are several ways to accomplish this attack, but some of the most-common are Address Resolution Protocol (ARP) poisoning and the use of a proxy. (Citation: Bonnie Zhu, Anthony Joseph, Shankar Sastry 2011)  

An AiTM attack may allow an adversary to perform the following attacks:  
[Block Reporting Message](https://attack.mitre.org/techniques/T0804), [Spoof Reporting Message](https://attack.mitre.org/techniques/T0856), [Modify Parameter](https://attack.mitre.org/techniques/T0836), [Unauthorized Command Message](https://attack.mitre.org/techniques/T0855)

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
- Communication Authenticity
- Disable or Remove Feature or Program
- Network Intrusion Prevention
- Network Segmentation
- Out-of-Band Communications Channel
- Software Process and Device Authentication
- Static Network Configuration

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- Triton Safety Instrumented System Attack (campaign)
- VPNFilter (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.

## ATT&CK contributors

- Conrad Layne - GE Digital
