---
name: attack-ent-t1195-001-compromise-software-dependencies-and
description: "Analyze MITRE ATT&CK T1195.001 Compromise Software Dependencies and Development Tools in the enterprise matrix. Use for TTP triage, detection engineering, hunting, defensive emulation planning, mitigations, incident response mapping, ATT&CK coverage, or questions mentioning T1195.001, Compromise Software Dependencies and Development Tools, or enterprise ATT&CK. Adversaries may manipulate software dependencies and development tools prior to receipt by a final consumer for the purpose of data or system compromise."
license: MITRE ATT&CK Terms of Use apply to ATT&CK-derived content. See https://attack.mitre.org/resources/terms-of-use/
metadata:
  source: mitre-attack/attack-stix-data
  domain: enterprise
  attack_id: T1195.001
  attack_stix_id: attack-pattern--191cc6af-1bb2-4344-ab5f-28e496638720
  attack_version: "1.3"
  attack_modified: "2025-10-24T17:48:27.436Z"
---

# MITRE ATT&CK T1195.001: Compromise Software Dependencies and Development Tools

## When to use this skill

Use this skill when the task involves T1195.001, Compromise Software Dependencies and Development Tools, enterprise ATT&CK, TTP mapping, detection engineering, hunting, incident-response enrichment, control validation, or authorized adversary-emulation planning. Treat it as a defensive analysis aid: keep outputs focused on understanding, detecting, mitigating, and safely validating this ATT&CK sub-technique.

## Technique context

- ATT&CK domain: enterprise
- ATT&CK ID: T1195.001
- Technique name: Compromise Software Dependencies and Development Tools
- Type: sub-technique
- ATT&CK URL: https://attack.mitre.org/techniques/T1195/001
- Tactics: initial-access
- Platforms: Linux, macOS, Windows
- Required permissions: Not specified
- Effective permissions: Not specified
- Defenses bypassed: Not specified

## ATT&CK description

Adversaries may manipulate software dependencies and development tools prior to receipt by a final consumer for the purpose of data or system compromise. Applications often depend on external software to function properly. Popular open source projects that are used as dependencies in many applications, such as pip and NPM packages, may be targeted as a means to add malicious code to users of the dependency.(Citation: Trendmicro NPM Compromise)(Citation: Bitdefender NPM Repositories Compromised 2021)(Citation: MANDVI Malicious npm and PyPI Packages Disguised) This may also include abandoned packages, which in some cases could be re-registered by threat actors after being removed by adversaries.(Citation: The Hacker News PyPi Revival Hijack 2024) Adversaries may also employ "typosquatting" or name-confusion by choosing names similar to existing popular libraries or packages in order to deceive a user.(Citation: Ahmed Backdoors in Python and NPM Packages)(Citation: Meyer PyPI Supply Chain Attack Uncovered)(Citation: Checkmarx-oss-seo)

Additionally, CI/CD pipeline components, such as GitHub Actions, may be targeted in order to gain access to the building, testing, and deployment cycles of an application.(Citation: Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025) By adding malicious code into a GitHub action, a threat actor may be able to collect runtime credentials (e.g., via [Proc Filesystem](https://attack.mitre.org/techniques/T1003/007)) or insert further malicious components into the build pipelines for a second-order supply chain compromise.(Citation: OWASP CICD-SEC-4) As GitHub Actions are often dependent on other GitHub Actions, threat actors may be able to infect a large number of repositories via the compromise of a single Action.(Citation: Palo Alto Networks GitHub Actions Worm 2023)

Targeting may be specific to a desired victim set or may be distributed to a broad set of consumers but only move on to additional tactics on specific victims.

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

- Application Developer Guidance
- Limit Software Installation
- Update Software
- Vulnerability Scanning

## Known threat context

Use these examples only as contextual leads, not as proof that an observed event is this technique:

- BeaverTail (malware)
- GlassWorm (malware)
- Shai-Hulud (malware)
- Tsundere Botnet (malware)
- XCSSET (malware)

## Recommended output pattern

When responding with this skill, structure the answer as:

- Assessment: whether the evidence supports this ATT&CK mapping and why.
- Evidence: specific indicators, logs, behaviors, and assumptions.
- Detection: telemetry sources, analytic logic, and tuning considerations.
- Response: containment, eradication, recovery, and validation actions.
- Coverage gaps: missing logs, sensors, controls, or environmental details.
- References: include the ATT&CK URL and any user-provided evidence references.

## ATT&CK contributors

- Enis Aksu
- Joe Gumke, U.S. Bank
- Liran Ravich, CardinalOps
