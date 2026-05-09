---
name: attack-ent-t1685-disable-or-modify-tools
description: "Analyze MITRE ATT&CK T1685 Disable or Modify Tools in the enterprise matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1685, Disable or Modify Tools, or enterprise ATT&CK. Adversaries may disable, degrade, or tamper with security tools or applications (e.g., endpoint detection and response (EDR) tools, intrusion detection systems (IDS), antivirus, logging agents, sensors, etc.) to impair…"
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: enterprise
  attack_id: T1685
  attack_stix_id: attack-pattern--bbde9781-60aa-4b8a-a911-895b0c1b3872
  attack_version: "1.0"
  attack_modified: "2026-04-22T15:39:46.202Z"
---

# MITRE ATT&CK T1685: Disable or Modify Tools

## When to use this skill

Use this skill when the task involves T1685, Disable or Modify Tools, enterprise ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: enterprise
- ATT&CK ID: T1685
- Technique name: Disable or Modify Tools
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1685
- Tactics: defense-impairment
- Platforms: Containers, ESXi, IaaS, Linux, macOS, Network Devices, Windows
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may disable, degrade, or tamper with security tools or applications (e.g., endpoint detection and response (EDR) tools, intrusion detection systems (IDS), antivirus, logging agents, sensors, etc.) to impair or reduce visibility of defensive capabilities. This may include stopping specific services, killing processes, modifying or deleting tool configuration files and Registry keys, or preventing tools from updating. This may also include impairing defenses more broadly by disrupting preventative, detection, and response mechanisms across host, network, and cloud environments.(Citation: SCADAfence_ransomware) 

In addition to directly targeting tools, adversaries may block or manipulate indicators and telemetry used for detection. This includes maliciously disabling or redirecting sensors such as Event Tracing for Windows (ETW), modifying event log configurations (e.g., redirecting Security logs), or interfering with logging pipelines and forwarding mechanisms (e.g., SIEM ingestion).(Citation: Microsoft Lamin Sept 2017)(Citation: ETW Palantir)

More advanced techniques include leveraging legitimate drivers or debugging mechanisms to render tools non-functional, bypassing anti-tampering protections, and targeting specific defenses such as Sysmon or cloud monitoring agents. Adversaries may also disrupt broader defensive operations, including update mechanisms, logging infrastructure (e.g., syslog), or event aggregation, further degrading an organization’s ability to detect and respond to malicious activity.(Citation: Cocomazzi FIN7 Reboot)

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
- Disable or Remove Feature or Program
- Execution Prevention
- Restrict File and Directory Permissions
- Restrict Registry Permissions
- Software Configuration
- User Account Management

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- 2015 Ukraine Electric Power Attack (campaign)
- APT38 (intrusion-set)
- APT41 (intrusion-set)
- APT5 (intrusion-set)
- Agent Tesla (malware)
- Agrius (intrusion-set)
- Akira (intrusion-set)
- Aquatic Panda (intrusion-set)
- ArcaneDoor (campaign)
- Avaddon (malware)
- BOLDMOVE (malware)
- BRONZE BUTLER (intrusion-set)
- Babuk (malware)
- Bazar (malware)
- BlackByte (intrusion-set)
- BlackByte Ransomware (malware)
- Brave Prince (malware)
- Brute Ratel C4 (tool)
- Bundlore (malware)
- Carberp (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.

## ATT&CK contributors

- Alex Soler, AttackIQ
- Cian Heasley
- Daniel Feichter, @VirtualAllocEx, Infosec Tirol
- Gal Singer, @galsinger29, Team Nautilus Aqua Security
- Gordon Long, LegioX/Zoom, asaurusrex
- Lucas Heiligenstein
- Menachem Goldstein
- Nathaniel Quist, Palo Alto Networks
- Nay Myo Hlaing (Ethan), DBS Bank
- Rob Smith
- Sarathkumar Rajendran, Microsoft Defender365
- Ziv Karliner, @ziv_kr, Team Nautilus Aqua Security
