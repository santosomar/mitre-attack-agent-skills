---
name: attack-mob-t1521-003-ssl-pinning
description: "Analyze MITRE ATT&CK T1521.003 SSL Pinning in the mobile matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1521.003, SSL Pinning, or mobile ATT&CK. Adversaries may use [SSL Pinning](https://attack.mitre.org/techniques/T1521/003) to protect the C2 traffic from being intercepted and analyzed."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: mobile
  attack_id: T1521.003
  attack_stix_id: attack-pattern--dfafc230-5465-4993-8dc5-f51fa9fec002
  attack_version: "1.0"
  attack_modified: "2024-04-16T20:24:13.854Z"
---

# MITRE ATT&CK T1521.003: SSL Pinning

## When to use this skill

Use this skill when the task involves T1521.003, SSL Pinning, mobile ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK sub-technique.

## Technique context

- ATT&CK domain: mobile
- ATT&CK ID: T1521.003
- Technique name: SSL Pinning
- Type: sub-technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1521/003
- Tactics: command-and-control
- Platforms: Android, iOS
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may use [SSL Pinning](https://attack.mitre.org/techniques/T1521/003)  to protect the C2 traffic from being intercepted and analyzed.

[SSL Pinning](https://attack.mitre.org/techniques/T1521/003)  is a technique commonly utilized by legitimate websites to ensure that encrypted communications are only allowed with a pre-defined certificate. If another certificate is presented, it could indicate device compromise, traffic interception, or another upstream issue. While benign usages are common, it is also possible for adversaries to abuse this technology to protect malicious C2 traffic.

In normal, not pinned SSL validation, when a client connects to a server using HTTPS, it typically checks whether the server’s SSL/TLS certificate is signed by a trusted Certificate Authority (CA) in the device’s trust store. If the certificate is valid and signed by a trusted CA, the connection is established. However, with [SSL Pinning](https://attack.mitre.org/techniques/T1521/003) , the client is configured to trust a specific SSL/TLS certificate or public key, rather than relying on the device’s trust store. This means that even if the server’s certificate is signed by a trusted CA, the client will only establish the connection of the certificate or key is pinned.

There are two types of [SSL Pinning](https://attack.mitre.org/techniques/T1521/003) :

1.	Certificate Pinning: The client stores a copy of the server’s certificate and compares it with the certificate received during the SSL handshake. If the certificates match, then the client proceeds with the connection. This approach also works with self-signed certificates.

2.	Public Key Pinning: Instead of pinning the entire certificate, the client pins just the public key extracted from the certificate. This is often more flexible, as it allows the server to renew its certificate without having to update the pinned certificate or breaking the SSL connection.

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
- User Guidance

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- eSurv (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.

## ATT&CK contributors

- Takahashi Wataru, NEC Corporation
- Manikantan Srinivasan, NEC Corporation India
- Pooja Natarajan, NEC Corporation India
