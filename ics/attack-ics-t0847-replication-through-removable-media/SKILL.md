---
name: attack-ics-t0847-replication-through-removable-media
description: "Analyze MITRE ATT&CK T0847 Replication Through Removable Media in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0847, Replication Through Removable Media, or ics ATT&CK. Adversaries may move onto systems, such as those separated from the enterprise network, by copying malware to removable media which is inserted into the control systems environment."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0847
  attack_stix_id: attack-pattern--c267bbee-bb59-47fe-85e0-3ed210337c21
  attack_version: "1.0"
  attack_modified: "2025-04-15T19:59:04.946Z"
---

# MITRE ATT&CK T0847: Replication Through Removable Media

## When to use this skill

Use this skill when the task involves T0847, Replication Through Removable Media, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0847
- Technique name: Replication Through Removable Media
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0847
- Tactics: initial-access
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may move onto systems, such as those separated from the enterprise network, by copying malware to removable media which is inserted into the control systems environment. The adversary may rely on unknowing trusted third parties, such as suppliers or contractors with access privileges, to introduce the removable media. This technique enables initial access to target devices that never connect to untrusted networks, but are physically accessible.     

Operators of the German nuclear power plant, Gundremmingen, discovered malware on a facility computer not connected to the internet. (Citation: Kernkraftwerk Gundremmingen April 2016) (Citation: Trend Micro April 2016) The malware included Conficker and W32.Ramnit, which were also found on eighteen removable disk drives in the facility. (Citation: Christoph Steitz, Eric Auchard April 2016) (Citation: Catalin Cimpanu April 2016) (Citation: Peter Dockrill April 2016) (Citation: Lee Mathews April 2016) (Citation: Sean Gallagher April 2016) (Citation: Dark Reading Staff April 2016) The plant has since checked for infection and cleaned up more than 1,000 computers. (Citation: BBC April 2016) An ESET researcher commented that internet disconnection does not guarantee system safety from infection or payload execution. (Citation: ESET April 2016)

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

- Disable or Remove Feature or Program
- Limit Hardware Installation
- Operating System Configuration

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- Conficker (malware)
- Stuxnet (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
