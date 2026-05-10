# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A generated catalog of **918 Agent Skills** (one per non-revoked, non-deprecated MITRE ATT&CK `attack-pattern`) across three domains:

- `enterprise/` — 697 skills (domain code `ent`)
- `mobile/` — 124 skills (domain code `mob`)
- `ics/` — 97 skills (domain code `ics`)

Plus top-level artifacts: `manifest.csv`, `manifest.json`, `validation-summary.txt`, `README.md`.

The skills are **intentionally defensive**: triage, detection engineering, hunting, mitigation, coverage assessment, incident response, and authorized validation. Do not add offensive content (malware, credential theft recipes, evasion guidance, unauthorized exploitation steps) to any skill.

## The generator is the source of truth

Every file under `enterprise/`, `mobile/`, `ics/`, plus `manifest.csv`, `manifest.json`, and the generated `README.md`, is produced by `scripts/generate_attack_skills.py` from upstream STIX bundles in [`mitre-attack/attack-stix-data`](https://github.com/mitre-attack/attack-stix-data).

Implications:

- **Do not hand-edit individual skill files.** Changes to one skill's `SKILL.md`, `references/`, `templates/`, `scripts/render_brief.py`, or `assets/output-schema.json` will be wiped on the next regeneration. Edit the generator instead and regenerate.
- Cross-cutting changes (new template, new reference file, schema tweak, frontmatter field, slug rule) belong in `scripts/generate_attack_skills.py` — search for the relevant template literal or `write_resource_files` block.
- `main()` does `shutil.rmtree(OUT_ROOT)` before regenerating, so the output tree is recreated from scratch each run.
- The script has **hardcoded absolute paths** (`WORKSPACE = Path("/home/user/workspace")`, `SOURCE_ROOT`, `OUT_ROOT`) reflecting the sandbox where it was originally run. To regenerate locally you'll need to either edit those constants or run it in an equivalent layout with `attack-stix-data` checked out alongside the output root.

## Skill anatomy

Each skill directory follows this exact layout (11 files; enforced by `validation-summary.txt`):

```
attack-<domain-code>-<technique-id>-<technique-slug>/
├── SKILL.md                              # frontmatter + body; name matches dir name
├── resources.md                          # index of bundled resources
├── references/
│   ├── technique-profile.json            # structured ATT&CK metadata (consumed by render_brief.py)
│   ├── detection-and-mitigation.md
│   └── known-threat-context.md
├── templates/
│   ├── detection-brief.md
│   ├── hunt-plan.md
│   ├── incident-response-note.md
│   └── coverage-assessment.md
├── scripts/
│   └── render_brief.py                   # reads ../references/technique-profile.json
└── assets/
    └── output-schema.json                # JSON schema for structured analysis output
```

Skill naming: `attack-<ent|mob|ics>-<lowercased-dotted-id-with-dashes>-<slugified-name>`, capped at 64 chars (a 6-char sha1 suffix is appended when the slug would overflow — see `technique_skill()`).

## Regenerating

```bash
# After updating attack-stix-data or editing the generator
python3 scripts/generate_attack_skills.py
```

The script prints a JSON summary (`{"generated": N, "counts": {...}, "output": ...}`) and rewrites `manifest.csv` / `manifest.json` / `README.md` at the output root.

External validation (referenced in `validation-summary.txt`) is run via `agentskills validate` — this tool is not bundled in the repo.

## When making changes

- Updating ATT&CK content → update the upstream STIX bundle reference and regenerate; don't patch individual SKILL.md files.
- Adding a new bundled resource type (e.g., a new template) → add it to `write_resource_files()` and update the "Bundled resources" list in `technique_skill()`'s body template, the `resources.md` listing, and the README's "Every skill includes" list so all three stay in sync.
- Changing the SKILL.md frontmatter schema → edit the f-string in `technique_skill()`; check `yaml_quote()` handling for any new free-text fields.
- Changes to skill content should preserve the defensive framing already baked into the workflow section ("do not provide malware, credential theft, persistence, evasion...").
