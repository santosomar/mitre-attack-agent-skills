---
name: attack-mob-t1521-001-symmetric-cryptography
description: "Analyze MITRE ATT&CK T1521.001 Symmetric Cryptography in the mobile matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1521.001, Symmetric Cryptography, or mobile ATT&CK. Adversaries may employ a known symmetric encryption algorithm to conceal command and control traffic, rather than relying on any inherent protections provided by a communication protocol."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: mobile
  attack_id: T1521.001
  attack_stix_id: attack-pattern--bb4387ab-7a51-468b-bf5f-a9a8612f0303
  attack_version: "1.0"
  attack_modified: "2025-10-24T17:49:17.802Z"
---

# MITRE ATT&CK T1521.001: Symmetric Cryptography

## When to use this skill

Use this skill when the task involves T1521.001, Symmetric Cryptography, mobile ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK sub-technique.

## Technique context

- ATT&CK domain: mobile
- ATT&CK ID: T1521.001
- Technique name: Symmetric Cryptography
- Type: sub-technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1521/001
- Tactics: command-and-control
- Platforms: Android, iOS
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may employ a known symmetric encryption algorithm to conceal command and control traffic, rather than relying on any inherent protections provided by a communication protocol. Symmetric encryption algorithms use the same key for plaintext encryption and ciphertext decryption. Common symmetric encryption algorithms include AES, Blowfish, and RC4.

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

- No ATT&CK mitigation relationships were present in the source STIX bundle.

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- C0033 (campaign)
- EventBot (malware)
- Operation Triangulation (campaign)
- Rotexy (malware)
- SharkBot (malware)
- TriangleDB (malware)
- Windshift (intrusion-set)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
