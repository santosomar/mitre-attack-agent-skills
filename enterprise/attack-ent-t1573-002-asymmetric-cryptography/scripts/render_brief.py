#!/usr/bin/env python3
"""Render a defensive ATT&CK brief from this skill's bundled profile."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def bullets(items, empty="Not specified"):
    return "\n".join(f"- {item}" for item in items) if items else f"- {empty}"


def main():
    parser = argparse.ArgumentParser(description="Render a Markdown brief for this ATT&CK skill.")
    parser.add_argument("--profile", default="../references/technique-profile.json", help="Path to technique-profile.json relative to this script")
    parser.add_argument("--output", default="-", help="Output Markdown path, or '-' for stdout")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    profile_path = (script_dir / args.profile).resolve()
    profile = json.loads(profile_path.read_text())

    md = f'''# ATT&CK Defensive Brief: {profile["attack_id"]} {profile["name"]}

## Context

- Domain: {profile["domain"]}
- Type: {profile["type"]}
- Tactics: {", ".join(profile.get("tactics", [])) or "Not specified"}
- Platforms: {", ".join(profile.get("platforms", [])) or "Not specified"}
- ATT&CK URL: {profile.get("attack_url", "")}

## Description

{profile.get("description", "No description available.")}

## Detection guidance

{profile.get("detection", "No detection guidance available.")}

## Data sources

{bullets(profile.get("data_sources", []))}

## Mitigations

{bullets(profile.get("mitigations", []), "No mapped mitigations in the bundled profile.")}

## Known context

{bullets(profile.get("known_context", []), "No known context in the bundled profile.")}
'''

    if args.output == "-":
        print(md)
    else:
        Path(args.output).write_text(md)


if __name__ == "__main__":
    main()
