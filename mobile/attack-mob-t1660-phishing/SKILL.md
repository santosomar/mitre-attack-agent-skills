---
name: attack-mob-t1660-phishing
description: "Analyze MITRE ATT&CK T1660 Phishing in the mobile matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1660, Phishing, or mobile ATT&CK. Adversaries may send malicious content to users in order to gain access to their mobile devices."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: mobile
  attack_id: T1660
  attack_stix_id: attack-pattern--defc1257-4db1-4fb3-8ef5-bb77f63146df
  attack_version: "1.2"
  attack_modified: "2026-04-20T17:38:10.545Z"
---

# MITRE ATT&CK T1660: Phishing

## When to use this skill

Use this skill when the task involves T1660, Phishing, mobile ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK technique.

## Technique context

- ATT&CK domain: mobile
- ATT&CK ID: T1660
- Technique name: Phishing
- Type: technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1660
- Tactics: initial-access
- Platforms: Android, iOS
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may send malicious content to users in order to gain access to their mobile devices. All forms of phishing are electronically delivered social engineering. Adversaries can conduct both non-targeted phishing, such as in mass malware spam campaigns, as well as more targeted phishing tailored for a specific individual, company, or industry, known as “spearphishing.” Phishing often involves social engineering techniques, such as posing as a trusted source, as well as evasion techniques, such as removing or manipulating emails or metadata/headers from compromised accounts being abused to send messages.

Mobile phishing may take various forms. For example, adversaries may send emails containing malicious attachments or links, typically to deliver and then execute malicious code on victim devices. Phishing may also be conducted via third-party services, like social media platforms. Adversaries may also impersonate executives of organizations to persuade victims into performing some action on their behalf. For example, adversaries will often use social engineering techniques in text messages to trick the victims into acting quickly, which leads to adversaries obtaining credentials and other information. 

Mobile devices are a particularly attractive target for adversaries executing phishing campaigns.  Due to their smaller form factor than traditional desktop endpoints, users may not be able to notice minor differences between genuine and phishing websites. Further, mobile devices have additional sensors and radios that allow adversaries to execute phishing attempts over several different vectors, such as: 

- SMS messages: Adversaries may send SMS messages (known as “smishing”) from compromised devices to potential targets to convince the target to, for example, install malware, navigate to a specific website, or enable certain insecure configurations on their device.
- Quick Response (QR) Codes: Adversaries may use QR codes (known as “quishing”) to redirect users to a phishing website. For example, an adversary could replace a legitimate public QR Code with one that leads to a different destination, such as a phishing website. A malicious QR code could also be delivered via other means, such as SMS or email. In the latter case, an adversary could utilize a malicious QR code in an email to pivot from the user’s desktop computer to their mobile device.
- Phone Calls: Adversaries may call victims (known as "vishing") to persuade them to perform an action, such as providing login credentials or navigating to malicious websites. Common vishing targets include employees, especially executives of organizations, and help desks. This may also be used as a technique to perform the initial access on a mobile device, but then pivot to a desktop computer by having the victims perform actions on a desktop computer. With the rise of artificial intelligence (AI), adversaries may also use AI to clone a person’s voice, resulting in deepfake vishing. The cloned voice provides familiarity to the victims, increasing the likelihood of successful malicious actions performed by the victims. Additionally, adversaries may leave voicemails, which may use a real person’s voice or an AI-generated voice; these scams would urgently ask victims into calling back to perform an action, e.g. sending money or providing sensitive information and credentials.

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
- User Guidance

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- APT-C-23 (intrusion-set)
- BITTER (intrusion-set)
- BRATA (malware)
- Chameleon (malware)
- CherryBlos (malware)
- DocSwap (malware)
- FjordPhantom (malware)
- FluBot (malware)
- GodFather (malware)
- Kimsuky (intrusion-set)
- LightSpy (malware)
- Pegasus for iOS (malware)
- RatMilad (malware)
- Sandworm Team (intrusion-set)
- Scattered Spider (intrusion-set)
- UNC788 (intrusion-set)
- VajraSpy (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.

## ATT&CK contributors

- Vijay Lalwani
- Will Thomas, Equinix
- Adam Mashinchi
- Sam Seabrook, Duke Energy
- Naveen Devaraja, bolttech
- Brian Donohue
- Lookout
