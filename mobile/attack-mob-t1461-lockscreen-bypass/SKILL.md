---
name: attack-mob-t1461-lockscreen-bypass
description: "Analyze MITRE ATT&CK T1461 Lockscreen Bypass in the mobile matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1461, Lockscreen Bypass, or mobile ATT&CK. An adversary with physical access to a mobile device may seek to bypass the device’s lockscreen."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: mobile
  attack_id: T1461
  attack_stix_id: attack-pattern--dfe29258-ce59-421c-9dee-e85cb9fa90cd
  attack_version: "1.3"
  attack_modified: "2025-10-24T17:49:29.764Z"
---

# MITRE ATT&CK T1461: Lockscreen Bypass

## When to use this skill

Use this skill when the task involves T1461, Lockscreen Bypass, mobile ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: mobile
- ATT&CK ID: T1461
- Technique name: Lockscreen Bypass
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1461
- Tactics: initial-access
- Platforms: Android, iOS
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

An adversary with physical access to a mobile device may seek to bypass the device’s lockscreen. Several methods exist to accomplish this, including:

* Biometric spoofing: If biometric authentication is used, an adversary could attempt to spoof a mobile device’s biometric authentication mechanism. Both iOS and Android partly mitigate this attack by requiring the device’s passcode rather than biometrics to unlock the device after every device restart, and after a set or random amount of time.(Citation: SRLabs-Fingerprint)(Citation: TheSun-FaceID)
* Unlock code bypass: An adversary could attempt to brute-force or otherwise guess the lockscreen passcode (typically a PIN or password), including physically observing (“shoulder surfing”) the device owner’s use of the lockscreen passcode. Mobile OS vendors partly mitigate this by implementing incremental backoff timers after a set number of failed unlock attempts, as well as a configurable full device wipe after several failed unlock attempts.
* Vulnerability exploit: Techniques have been periodically demonstrated that exploit mobile devices to bypass the lockscreen. The vulnerabilities are generally patched by the device or OS vendor once disclosed.(Citation: Wired-AndroidBypass)(Citation: Kaspersky-iOSBypass)

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

- Enterprise Policy
- Security Updates

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- BRATA (malware)
- Chameleon (malware)
- Escobar (malware)
- VajraSpy (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.
