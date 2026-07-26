#!/usr/bin/env python3
"""Enforce phase locks.

Article VI: no cross-company synthesis until the Phase 2.5 audit passes.
This is not decorative. Synthesis is lossy compression of its inputs;
compressing uneven inputs produces confident conclusions with invisible
error bars that later become load-bearing in funding decisions.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPANIES = ROOT / "phase-2-dossiers" / "Companies"
AUDIT_PASS = ROOT / "phase-2.5-audit" / "AUDIT-PASSED"

sys.path.insert(0, str(Path(__file__).parent))
from registry import load  # noqa: E402

PHASES = {
    "phase-2":   {"requires": "phase-1",   "desc": "Company Dossiers"},
    "phase-2.5": {"requires": "phase-2",   "desc": "Research Quality Audit"},
    "phase-3":   {"requires": "phase-2.5", "desc": "Layer Intelligence"},
    "phase-4":   {"requires": "phase-2.5", "desc": "Technology Intelligence"},
    "phase-5":   {"requires": "phase-2.5", "desc": "Healthcare Intelligence"},
    "phase-6":   {"requires": "phase-2.5", "desc": "Cross-Company Synthesis"},
    "phase-7":   {"requires": "phase-6",   "desc": "JARVIS Opportunity Mapping"},
    "phase-8":   {"requires": "phase-7",   "desc": "Moat Engineering"},
    "phase-omega": {"requires": "phase-8", "desc": "Master Strategy Bible"},
}


def ratified_count() -> tuple[int, int]:
    entities = [e for e in load() if not e.get("self") and e.get("layer") != "L15"]
    if not COMPANIES.exists():
        return 0, len(entities)
    n = 0
    for folder in COMPANIES.iterdir():
        if not folder.is_dir():
            continue
        res = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "validate.py"), folder.name],
            capture_output=True,
        )
        if res.returncode == 0:
            n += 1
    return n, len(entities)


def check(phase: str) -> int:
    if phase not in PHASES:
        print(f"unknown phase '{phase}'. known: {', '.join(PHASES)}")
        return 2

    info = PHASES[phase]
    done, total = ratified_count()
    audit_passed = AUDIT_PASS.exists()

    print(f"\n\033[1mgate: {phase}\033[0m  ({info['desc']})")
    print(f"  requires: {info['requires']}")
    print(f"  dossiers ratified: {done} / {total}")
    print(f"  audit passed: {'yes' if audit_passed else 'no'}")

    blocked: list[str] = []

    if phase == "phase-2.5" and done < total:
        blocked.append(f"{total - done} dossiers not ratified")

    if info["requires"] == "phase-2.5" and not audit_passed:
        blocked.append(
            "Phase 2.5 audit has not passed (Article VI.1 - synthesis prohibited)"
        )

    if phase in ("phase-7", "phase-8", "phase-omega") and not audit_passed:
        blocked.append("upstream audit gate not cleared")

    if blocked:
        print(f"\n  \033[31mBLOCKED\033[0m")
        for b in blocked:
            print(f"    - {b}")
        print("\n  Remedy is to re-run deficient dossiers, never to soften the")
        print("  audit (Article VI.3).\n")
        return 1

    print(f"\n  \033[32mUNLOCKED\033[0m\n")
    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "--check":
        sys.exit(check(sys.argv[2]))
    print("usage: gate.py --check <phase>")
    print("phases:", ", ".join(PHASES))
    sys.exit(2)
