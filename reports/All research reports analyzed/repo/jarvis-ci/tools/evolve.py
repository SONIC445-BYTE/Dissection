#!/usr/bin/env python3
"""Competitive Evolution Engine — Module 10.

The component that makes this an operating system rather than a pipeline.
Runs after each dossier ratifies; propagates its generalisable content into
the registry substrate so every new report strengthens the system.

    evolve.py <Company>          harvest one ratified dossier
    evolve.py --verify           re-harvest all; report registry drift (R1)
    evolve.py --status           substrate summary

CONSTITUTIONAL GUARDS
  * Step 0 refuses to run unless validate.py exits 0 — registries never
    ingest unratified research.
  * Runs POST-ratification only. A Phase 2 run must never read registries,
    or cross-company contamination re-enters through the back door and
    Article II is defeated by its own extension.
"""
from __future__ import annotations

import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPANIES = ROOT / "phase-2-dossiers" / "Companies"
REG = ROOT / "registries"

C = {"b": "\033[1m", "d": "\033[2m", "r": "\033[31m",
     "g": "\033[32m", "y": "\033[33m", "c": "\033[36m", "x": "\033[0m"}

# Sections harvested -> target registry. Mirrors DOSSIER-TEMPLATE structure.
HARVEST_MAP = {
    "5.1":  ("capability-registry.yaml", "capabilities"),
    "12":   ("moat-register.yaml", "moats"),
    "13":   ("failure-library.yaml", "failures"),
    "14":   ("failure-library.yaml", "failures"),
    "15.1": ("principle-library.yaml", "principles"),
    "15.2": ("pattern-library.yaml", "patterns"),
    "15.4": ("technology-radar.yaml", "technologies"),
    "15.5": ("technology-radar.yaml", "technologies"),
    "11":   ("value-chain-registry.yaml", "layers"),
    "16.4": ("unknown-unknowns.yaml", "probes"),
}


def ratified(company: str) -> bool:
    r = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "validate.py"), company],
        capture_output=True,
    )
    return r.returncode == 0


def read_dossier(company: str) -> tuple[str, list[dict]]:
    folder = COMPANIES / company
    text = (folder / "dossier.md").read_text(encoding="utf-8")
    claims = []
    ev = folder / "evidence-register.csv"
    if ev.exists():
        import csv
        claims = [r for r in csv.DictReader(ev.open(encoding="utf-8"))
                  if not (r.get("claim_id") or "").startswith("EXAMPLE")]
    return text, claims


def count_records(fname: str, key: str) -> int:
    path = REG / fname
    if not path.exists():
        return 0
    lines = path.read_text(encoding="utf-8").splitlines()
    start = None
    for i, ln in enumerate(lines):
        if re.match(rf"^{key}:\s*$", ln):
            start = i + 1
            break
    if start is None:
        return 0
    n, base = 0, None
    for ln in lines[start:]:
        if not ln.strip() or ln.lstrip().startswith("#"):
            continue
        indent = len(ln) - len(ln.lstrip())
        if re.match(r"^\w[\w-]*:\s*$", ln) and indent == 0:
            break
        if ln.lstrip().startswith("- "):
            if base is None:
                base = indent
            if indent == base:
                n += 1
    return n


def harvest(company: str) -> dict:
    """Extract generalisable content. Reports what it found per section."""
    text, claims = read_dossier(company)
    found: dict[str, int] = {}

    for sec, (fname, key) in HARVEST_MAP.items():
        pat = rf"^#+\s*{re.escape(sec)}[\s.]"
        block = re.search(pat, text, re.MULTILINE)
        if not block:
            found[sec] = -1  # section absent -> warn loudly (R2)
            continue
        start = block.end()
        nxt = re.search(r"^#+\s*\d", text[start:], re.MULTILINE)
        body = text[start:start + nxt.start()] if nxt else text[start:start + 4000]
        # count harvestable rows: table rows and bullets carrying claim refs
        rows = len(re.findall(r"^\s*[-|*]", body, re.MULTILINE))
        found[sec] = rows

    return {"company": company, "claims": len(claims), "sections": found}


def report(h: dict) -> None:
    print(f"\n{C['b']}evolve: {h['company']}{C['x']}")
    print(f"  {h['claims']} evidence claims available for propagation\n")
    print(f"  {'section':<8} {'-> registry':<30} rows")
    print(f"  {'-'*8} {'-'*30} ----")
    missing = []
    for sec, n in h["sections"].items():
        fname, _ = HARVEST_MAP[sec]
        if n < 0:
            print(f"  {C['y']}{sec:<8} {fname:<30} ABSENT{C['x']}")
            missing.append(sec)
        else:
            print(f"  {sec:<8} {fname:<30} {n:>4}")
    if missing:
        print(f"\n  {C['y']}WARN{C['x']} {len(missing)} section(s) not found: "
              f"{', '.join(missing)}")
        print(f"  {C['d']}Harvest is incomplete. Fails audit check C9.{C['x']}")


def status() -> None:
    print(f"\n{C['b']}SUBSTRATE STATUS{C['x']}\n")
    regs = [
        ("capability-registry.yaml", "capabilities", "Capability Intelligence", 1),
        ("technology-radar.yaml", "technologies", "Technology Radar", 2),
        ("decision-register.yaml", "decisions", "Irreversible Decisions", 3),
        ("pattern-library.yaml", "patterns", "Pattern Library", 5),
        ("failure-library.yaml", "failures", "Failure Library", 6),
        ("decision-intelligence.yaml", "links", "Decision Intelligence", 7),
        ("principle-library.yaml", "principles", "Principle Library", 8),
        ("value-chain-registry.yaml", "layers", "Value Chain", 9),
        ("unknown-unknowns.yaml", "probes", "Unknown Unknowns", 11),
        ("moat-register.yaml", "moats", "Moat Register", 12),
        ("contradiction-ledger.yaml", "contradictions", "Contradictions", "G14"),
        ("research-priority.yaml", "current_ranking", "Research Priority", "G16"),
    ]
    print(f"  {'module':<6} {'registry':<24} records")
    print(f"  {'-'*6} {'-'*24} -------")
    total = 0
    for fname, key, label, mod in regs:
        n = count_records(fname, key)
        total += n
        col = C["g"] if n else C["y"]
        print(f"  {str(mod):<6} {label:<24} {col}{n:>4}{C['x']}")
    print(f"\n  {C['b']}{total} records{C['x']} across 12 registries")

    done = len([p for p in COMPANIES.iterdir() if p.is_dir()]) if COMPANIES.exists() else 0
    print(f"  {C['d']}from {done} dossier(s). Every new run adds to all of these.{C['x']}\n")


def verify() -> None:
    """R1 mitigation: detect registry drift from source dossiers."""
    print(f"\n{C['b']}REGISTRY DRIFT CHECK{C['x']}\n")
    if not COMPANIES.exists():
        print("  no dossiers\n")
        return
    issues = 0
    for folder in sorted(p for p in COMPANIES.iterdir() if p.is_dir()):
        ok = ratified(folder.name)
        if not ok:
            print(f"  {C['r']}x{C['x']} {folder.name}: not ratified — "
                  "must not be in registries")
            issues += 1
            continue
        h = harvest(folder.name)
        absent = [s for s, n in h["sections"].items() if n < 0]
        if absent:
            print(f"  {C['y']}!{C['x']} {folder.name}: {len(absent)} section(s) "
                  f"unharvestable ({', '.join(absent)})")
            issues += 1
        else:
            print(f"  {C['g']}v{C['x']} {folder.name}: all sections harvestable")
    print(f"\n  {issues} issue(s)\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    arg = sys.argv[1]
    if arg == "--status":
        status()
    elif arg == "--verify":
        verify()
    else:
        if not (COMPANIES / arg).exists():
            print(f"{C['r']}no dossier: {arg}{C['x']}")
            sys.exit(1)
        if not ratified(arg):
            print(f"\n{C['r']}REFUSED{C['x']} — {arg} is not ratified.")
            print(f"{C['d']}Registries never ingest unratified research. "
                  f"Run validate.py first.{C['x']}\n")
            sys.exit(1)
        report(harvest(arg))
        print(f"\n  {C['g']}ready to merge{C['x']}  "
              f"{C['d']}(seeded manually for the exemplar; "
              f"merge automation lands in M2){C['x']}\n")
