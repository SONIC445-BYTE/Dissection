#!/usr/bin/env python3
"""Scaffold a dossier folder from the template, pre-filled from the registry."""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "phase-2-dossiers" / "_TEMPLATE"
COMPANIES = ROOT / "phase-2-dossiers" / "Companies"

sys.path.insert(0, str(Path(__file__).parent))
from registry import load  # noqa: E402


def main(name: str) -> int:
    entities = load()
    match = next(
        (e for e in entities
         if e.get("name", "").lower() == name.lower()
         or e.get("id", "").lower() == name.lower()),
        None,
    )
    if match is None:
        print(f"✗ '{name}' is not in the registry.")
        print("  Register it in phase-1-discovery/company-registry.yaml first —")
        print("  ad-hoc dossiers break the discovery discipline.")
        return 1

    if match.get("self"):
        print(f"✗ '{name}' is flagged self:true. Article VII.2 — never scored.")
        return 1

    folder = COMPANIES / match["name"].replace("/", "-").replace(" ", "-")
    if folder.exists():
        print(f"✗ already exists: {folder}")
        return 1
    folder.mkdir(parents=True)

    subs = {
        "{{COMPANY}}": match["name"],
        "{{ID}}": match["id"],
        "{{LAYER}}": match["layer"],
        "{{TIER}}": str(match.get("tier", 3)),
    }

    for src, dst in (
        (TEMPLATE / "DOSSIER-TEMPLATE.md", folder / "dossier.md"),
        (TEMPLATE / "scorecard.yaml", folder / "scorecard.yaml"),
    ):
        text = src.read_text(encoding="utf-8")
        for k, v in subs.items():
            text = text.replace(k, v)
        dst.write_text(text, encoding="utf-8")

    shutil.copy(TEMPLATE / "evidence-register.csv", folder / "evidence-register.csv")

    print(f"\n\033[1m✓ scaffolded {match['name']}\033[0m")
    print(f"  {folder.relative_to(ROOT)}/")
    print(f"    dossier.md · scorecard.yaml · evidence-register.csv")
    print(f"\n  layer {match['layer']} · tier {match.get('tier')} · "
          f"hypothesis: {match.get('role_hypothesis')}")
    if match.get("note"):
        print(f"  note: {match['note']}")
    print("\n  Next: open _TEMPLATE/RUN-PROMPT.md, paste into a FRESH context window.")
    print("  One company per run. Never two.\n")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: new_company.py <Company name or id>")
        sys.exit(2)
    sys.exit(main(" ".join(sys.argv[1:])))
