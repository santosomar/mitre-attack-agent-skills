---
name: attack-ics-t0860-wireless-compromise
description: "Analyze MITRE ATT&CK T0860 Wireless Compromise in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0860, Wireless Compromise, or ics ATT&CK. Adversaries may perform wireless compromise as a method of gaining communications and unauthorized access to a wireless network."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0860
  attack_stix_id: attack-pattern--2877063e-1851-48d2-bcc6-bc1d2733157e
  attack_version: "1.2"
  attack_modified: "2025-04-15T19:58:15.610Z"
---

# MITRE ATT&CK T0860: Wireless Compromise

## When to use this skill

Use this skill when the task involves T0860, Wireless Compromise, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0860
- Technique name: Wireless Compromise
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0860
- Tactics: initial-access
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may perform wireless compromise as a method of gaining communications and unauthorized access to a wireless network. Access to a wireless network may be gained through the compromise of a wireless device. (Citation: Alexander Bolshev, Gleb Cherbov July 2014) (Citation: Alexander Bolshev March 2014) Adversaries may also utilize radios and other wireless communication devices on the same frequency as the wireless network. Wireless compromise can be done as an initial access vector from a remote distance. 

A Polish student used a modified TV remote controller to gain access to and control over the Lodz city tram system in Poland. (Citation: John Bill May 2017) (Citation: Shelley Smith February 2008) The remote controller device allowed the student to interface with the trams network to modify track settings and override operator control. The adversary may have accomplished this by aligning the controller to the frequency and amplitude of IR control protocol signals. (Citation: Bruce Schneier January 2008) The controller then enabled initial access to the network, allowing the capture and replay of tram signals. (Citation: John Bill May 2017)

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
- Encrypt Network Traffic
- Minimize Wireless Signal Propagation
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

## ATT&CK contributors

- Scott Dougherty
