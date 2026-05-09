---
name: attack-ent-t1027-016-junk-code-insertion
description: "Analyze MITRE ATT&CK T1027.016 Junk Code Insertion in the enterprise matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1027.016, Junk Code Insertion, or enterprise ATT&CK. Adversaries may use junk code / dead code to obfuscate a malware’s functionality."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: enterprise
  attack_id: T1027.016
  attack_stix_id: attack-pattern--671cd17f-a765-48fd-adc4-dad1941b1ae3
  attack_version: "2.0"
  attack_modified: "2026-04-15T22:19:48.489Z"
---

# MITRE ATT&CK T1027.016: Junk Code Insertion

## When to use this skill

Use this skill when the task involves T1027.016, Junk Code Insertion, enterprise ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK sub-technique.

## Technique context

- ATT&CK domain: enterprise
- ATT&CK ID: T1027.016
- Technique name: Junk Code Insertion
- Type: sub-technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1027/016
- Tactics: stealth
- Platforms: Linux, macOS, Windows
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may use junk code / dead code to obfuscate a malware’s functionality. Junk code is code that either does not execute, or if it does execute, does not change the functionality of the code. Junk code makes analysis more difficult and time-consuming, as the analyst steps through non-functional code instead of analyzing the main code. It also may hinder detections that rely on static code analysis due to the use of benign functionality, especially when combined with [Compression](https://attack.mitre.org/techniques/T1027/015) or [Software Packing](https://attack.mitre.org/techniques/T1027/002).(Citation: ReasonLabs)(Citation: ReasonLabs Cyberpedia Junk Code)

No-Operation (NOP) instructions are an example of dead code commonly used in x86 assembly language. They are commonly used as the 0x90 opcode. When NOPs are added to malware, the disassembler may show the NOP instructions, leading to the analyst needing to step through them.(Citation: ReasonLabs)

The use of junk / dead code insertion is distinct from [Binary Padding](https://attack.mitre.org/techniques/T1027/001) because the purpose is to obfuscate the functionality of the code, rather than simply to change the malware’s signature.

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

- Antivirus/Antimalware

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- ANELLDR (malware)
- APT-C-36 (intrusion-set)
- APT32 (intrusion-set)
- CORESHELL (malware)
- FIN7 (intrusion-set)
- FatDuke (malware)
- FinFisher (malware)
- Gamaredon Group (intrusion-set)
- Gelsemium (malware)
- Goopy (malware)
- Kimsuky (intrusion-set)
- LODEINFO (malware)
- Maze (malware)
- Mustang Panda (intrusion-set)
- NOOPLDR (malware)
- POWERSTATS (malware)
- Pony (malware)
- PureCrypter (malware)
- SamSam (malware)
- StrelaStealer (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.

## ATT&CK contributors

- Joas Antonio dos Santos, @C0d3Cr4zy
