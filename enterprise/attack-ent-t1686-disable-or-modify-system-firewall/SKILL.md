---
name: attack-ent-t1686-disable-or-modify-system-firewall
description: "Analyze MITRE ATT&CK T1686 Disable or Modify System Firewall in the enterprise matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1686, Disable or Modify System Firewall, or enterprise ATT&CK. Adversaries may disable or modify host-based or network firewalls to impair defensive mechanisms and enable further action."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: enterprise
  attack_id: T1686
  attack_stix_id: attack-pattern--eec096b8-c207-43df-b6c1-11523861e452
  attack_version: "1.0"
  attack_modified: "2026-04-22T15:36:31.474Z"
---

# MITRE ATT&CK T1686: Disable or Modify System Firewall

## When to use this skill

Use this skill when the task involves T1686, Disable or Modify System Firewall, enterprise ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: enterprise
- ATT&CK ID: T1686
- Technique name: Disable or Modify System Firewall
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1686
- Tactics: defense-impairment
- Platforms: ESXi, Linux, macOS, Network Devices, Windows
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may disable or modify host-based or network firewalls to impair defensive mechanisms and enable further action. Once an adversary has gathered sufficient privileges, they can tamper with firewall services, policies, or rule sets to remove restrictions on inbound or outbound traffic. For example, this may include turning off firewall profiles, altering existing rules to permit previously blocked ports or protocols, or adding new rules that create covert communication paths (e.g., adding a new firewall rule for a well-known protocol (such as RDP) using a non-traditional and potentially less securitized port.(Citation: change_rdp_port_conti)

Adversaries may disable or modify firewalls using different behaviors, depending on the platform. For example, in ESXi, firewall rules may be modified directly via the esxcli (e.g., via esxcli network firewall set) or via the vCenter user interface.(Citation: Broadcom ESXi Firewall)(Citation: Trellix Rnasomhouse 2024)

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
- Restrict File and Directory Permissions
- Restrict Registry Permissions
- User Account Management

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- APT38 (intrusion-set)
- BACKSPACE (malware)
- BPFDoor (malware)
- BlackByte (intrusion-set)
- Carbanak (intrusion-set)
- CookieMiner (malware)
- Dragonfly (intrusion-set)
- FIN7 (intrusion-set)
- Grandoreiro (malware)
- HOPLIGHT (malware)
- Hannotog (malware)
- InvisiMole (malware)
- Kasidet (malware)
- Kimsuky (intrusion-set)
- Leviathan Australian Intrusions (campaign)
- Medusa Group (intrusion-set)
- NanoCore (malware)
- PlugX (malware)
- PyDCrypt (malware)
- Rocke (intrusion-set)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
