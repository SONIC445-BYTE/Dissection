#!/usr/bin/env python3
"""Progress + depth-variance dashboard across all dossiers.

Depth variance is the metric that detects the failure the pipeline exists to
prevent: later companies getting shallower analysis than earlier ones.
"""
from __future__ import annotations

import csv
import statistics
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPANIES = ROOT / "phase-2-dossiers" / "Companies"

sys.path.insert(0, str(Path(__file__).parent))
from registry import load  # noqa: E402


def dossier_stats(folder: Path) -> dict:
    d = folder / "dossier.md"
    e = folder / "evidence-register.csv"
    words = len(d.read_text(encoding="utf-8").split()) if d.exists() else 0
    claims = 0
    if e.exists():
        rows = list(csv.DictReader(e.open(encoding="utf-8")))
        claims = len([r for r in rows
                      if not (r.get("claim_id") or "").startswith("EXAMPLE")])
    ratified = False
    if d.exists():
        res = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "validate.py"), folder.name],
            capture_output=True,
        )
        ratified = res.returncode == 0
    return {"name": folder.name, "words": words, "claims": claims, "ratified": ratified}


def main() -> int:
    entities = [e for e in load() if not e.get("self") and e.get("layer") != "L15"]
    folders = sorted(p for p in COMPANIES.iterdir() if p.is_dir()) if COMPANIES.exists() else []

    print("\n\033[1mJARVIS CI - Phase 2 Status\033[0m")
    print(f"  registry: {len(entities)} scoreable entities")
    print(f"  scaffolded: {len(folders)}")

    if not folders:
        print("\n  No dossiers yet.")
        print("  Start: python3 tools/new_company.py Mem0\n")
        return 0

    stats = [dossier_stats(f) for f in folders]
    ratified = [s for s in stats if s["ratified"]]
    pct = 100 * len(ratified) / len(entities) if entities else 0
    print(f"  ratified: {len(ratified)} / {len(entities)}  ({pct:.1f}%)\n")

    print(f"  {'company':<24} {'words':>7} {'claims':>7}  status")
    print(f"  {'-' * 24} {'-' * 7} {'-' * 7}  {'-' * 12}")
    for s in stats:
        badge = "\033[32mratified\033[0m" if s["ratified"] else "\033[33mdraft\033[0m"
        print(f"  {s['name']:<24} {s['words']:>7} {s['claims']:>7}  {badge}")

    done = [s for s in stats if s["ratified"]]
    if len(done) >= 2:
        words = [s["words"] for s in done]
        claims = [s["claims"] for s in done]
        wmean = statistics.mean(words)
        cmean = statistics.mean(claims)
        wcv = statistics.stdev(words) / wmean if wmean else 0
        ccv = statistics.stdev(claims) / cmean if cmean else 0

        print("\n  \033[1mDepth variance\033[0m  (ratified only)")
        print(f"    words   mean {wmean:>7.0f}  CV {wcv:.2f}")
        print(f"    claims  mean {cmean:>7.1f}  CV {ccv:.2f}")

        if max(wcv, ccv) > 0.40:
            print("\n    \033[31mCV > 0.40 - uneven depth.\033[0m")
            print("    This is the exact failure the pipeline exists to prevent.")
            print("    Re-run the thin dossiers before Phase 2.5.")
        else:
            print("\n    \033[32mdepth is even (CV <= 0.40)\033[0m")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
