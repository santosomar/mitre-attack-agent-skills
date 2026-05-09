---
name: attack-ics-t0895-autorun-image
description: "Analyze MITRE ATT&CK T0895 Autorun Image in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0895, Autorun Image, or ics ATT&CK. Adversaries may leverage AutoRun functionality or scripts to execute malicious code."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0895
  attack_stix_id: attack-pattern--77d9c726-b53e-481d-8bcc-1068aebfbb9d
  attack_version: "1.0"
  attack_modified: "2025-04-15T19:58:42.824Z"
---

# MITRE ATT&CK T0895: Autorun Image

## When to use this skill

Use this skill when the task involves T0895, Autorun Image, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0895
- Technique name: Autorun Image
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0895
- Tactics: execution
- Platforms: Not specified
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may leverage AutoRun functionality or scripts to execute malicious code. Devices configured to enable AutoRun functionality or legacy operating systems may be susceptible to abuse of these features to run malicious code stored on various forms of removeable media (i.e., USB, Disk Images [.ISO]). Commonly, AutoRun or AutoPlay are disabled in many operating systems configurations to mitigate against this technique. If a device is configured to enable AutoRun or AutoPlay, adversaries may execute code on the device by mounting the removable media to the device, either through physical or virtual means. This may be especially relevant for virtual machine environments where disk images may be dynamically mapped to a guest system on a hypervisor.  

An example could include an adversary gaining access to a hypervisor through the management interface to modify a virtual machine’s hardware configuration. They could then deploy an iso image with a malicious AutoRun script to cause the virtual machine to automatically execute the code contained on the disk image. This would enable the execution of malicious code within a virtual machine without needing any prior remote access to that system.

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

- Operating System Configuration

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- 2022 Ukraine Electric Power Attack (campaign)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
