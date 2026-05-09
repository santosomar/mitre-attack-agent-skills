---
name: attack-ics-t0894-system-binary-proxy-execution
description: "Analyze MITRE ATT&CK T0894 System Binary Proxy Execution in the ics matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T0894, System Binary Proxy Execution, or ics ATT&CK. Adversaries may bypass process and/or signature-based defenses by proxying execution of malicious content with signed, or otherwise trusted, binaries."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: ics
  attack_id: T0894
  attack_stix_id: attack-pattern--1c5cf58c-a34a-40d7-82f4-f987cdfc2b91
  attack_version: "1.0"
  attack_modified: "2025-04-15T19:58:11.559Z"
---

# MITRE ATT&CK T0894: System Binary Proxy Execution

## When to use this skill

Use this skill when the task involves T0894, System Binary Proxy Execution, ics ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: ics
- ATT&CK ID: T0894
- Technique name: System Binary Proxy Execution
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T0894
- Tactics: evasion
- Platforms: None
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may bypass process and/or signature-based defenses by proxying execution of malicious content with signed, or otherwise trusted, binaries. Binaries used in this technique are often Microsoft-signed files, indicating that they have been either downloaded from Microsoft or are already native in the operating system. (Citation: LOLBAS Project) Binaries signed with trusted digital certificates can typically execute on Windows systems protected by digital signature validation. Several Microsoft signed binaries that are default on Windows installations can be used to proxy execution of other files or commands. Similarly, on Linux systems adversaries may abuse trusted binaries such as split to proxy execution of malicious commands. (Citation: split man page)(Citation: GTFO split)

Adversaries may abuse application binaries installed on a system for proxy execution of malicious code or domain-specific commands. These commands could be used to target local resources on the device or networked devices within the environment through defined APIs ([Execution through API](https://attack.mitre.org/techniques/T0871)) or application-specific programming languages (e.g., MicroSCADA SCIL). Application binaries may be signed by the developer or generally trusted by the operators, analysts, and monitoring tools accustomed to the environment. These applications may be developed and/or directly provided by the device vendor to enable configuration, management, and operation of their devices without many alternatives. 

Adversaries may seek to target these trusted application binaries to execute or send commands without the development of custom malware. For example, adversaries may target a SCADA server binary which has the existing ability to send commands to substation devices, such as through IEC 104 command messages. Proxy execution may still require the development of custom tools to hook into the application binary’s execution.

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

- Execution Prevention

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
