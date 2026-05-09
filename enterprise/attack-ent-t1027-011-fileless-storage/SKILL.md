---
name: attack-ent-t1027-011-fileless-storage
description: "Analyze MITRE ATT&CK T1027.011 Fileless Storage in the enterprise matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1027.011, Fileless Storage, or enterprise ATT&CK. Adversaries may store data in \"fileless\" formats to conceal malicious activity from defenses."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: enterprise
  attack_id: T1027.011
  attack_stix_id: attack-pattern--02c5abff-30bf-4703-ab92-1f6072fae939
  attack_version: "3.0"
  attack_modified: "2026-04-15T22:18:39.119Z"
---

# MITRE ATT&CK T1027.011: Fileless Storage

## When to use this skill

Use this skill when the task involves T1027.011, Fileless Storage, enterprise ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK sub-technique.

## Technique context

- ATT&CK domain: enterprise
- ATT&CK ID: T1027.011
- Technique name: Fileless Storage
- Type: sub-technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1027/011
- Tactics: stealth
- Platforms: Linux, Windows
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may store data in "fileless" formats to conceal malicious activity from defenses. Fileless storage can be broadly defined as any format other than a file. Common examples of non-volatile fileless storage in Windows systems include the Windows Registry, event logs, or WMI repository.(Citation: Microsoft Fileless)(Citation: SecureList Fileless) Shared memory directories on Linux systems (`/dev/shm`, `/run/shm`, `/var/run`, and `/var/lock`) and volatile directories on Network Devices (`/tmp` and `/volatile`) may also be considered fileless storage, as files written to these directories are mapped directly to RAM and not stored on the disk.(Citation: Elastic Binary Executed from Shared Memory Directory)(Citation: Akami Frog4Shell 2024)(Citation: Aquasec Muhstik Malware 2024)(Citation: Bitsight 7777 Botnet)(Citation: CISCO Nexus 900 Config).

Similar to fileless in-memory behaviors such as [Reflective Code Loading](https://attack.mitre.org/techniques/T1620) and [Process Injection](https://attack.mitre.org/techniques/T1055), fileless data storage may remain undetected by antivirus and other endpoint security tools that can only access specific file formats from disk storage. Leveraging fileless storage may also allow adversaries to bypass the protections offered by read-only file systems in Linux.(Citation: Sysdig Fileless Malware 23022)

Adversaries may use fileless storage to conceal various types of stored data, including payloads/shellcode (potentially being used as part of [Persistence](https://attack.mitre.org/tactics/TA0003)) and collected data not yet exfiltrated from the victim (e.g., [Local Data Staging](https://attack.mitre.org/techniques/T1074/001)). Adversaries also often encrypt, encode, splice, or otherwise obfuscate this fileless data when stored. 

Some forms of fileless storage activity may indirectly create artifacts in the file system, but in central and otherwise difficult to inspect formats such as the WMI (e.g., `%SystemRoot%\System32\Wbem\Repository`) or Registry (e.g., `%SystemRoot%\System32\Config`) physical files.(Citation: Microsoft Fileless)

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

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- APT32 (intrusion-set)
- CHOPSTICK (malware)
- Chaes (malware)
- ComRAT (malware)
- DarkWatchman (malware)
- Exaramel for Windows (malware)
- Gelsemium (malware)
- Grandoreiro (malware)
- Mosquito (malware)
- NETWIRE (malware)
- Operation CuckooBees (campaign)
- Pikabot (malware)
- Pillowmint (malware)
- PipeMon (malware)
- PolyglotDuke (malware)
- QUADAGENT (malware)
- QakBot (malware)
- Quad7 Activity (campaign)
- RCSession (malware)
- REvil (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.

## ATT&CK contributors

- Christopher Peacock
- Denise Tan
- Mark Wee
- Simona David
- Vito Alfano, Group-IB
- Xavier Rousseau
