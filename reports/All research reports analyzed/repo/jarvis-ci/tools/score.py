#!/usr/bin/env python3
"""Compute competitive indices from a dossier scorecard.

Formulas are defined in phase-0-constitution/03-competitive-scoring-framework.md §2
and must not be changed here without a Decision Ledger entry.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPANIES = ROOT / "phase-2-dossiers" / "Companies"


def parse_scorecard(path: Path) -> dict:
    """Minimal parser for the restricted scorecard YAML subset."""
    text = path.read_text(encoding="utf-8")
    data: dict = {"scores": {}, "flags": [], "stage": []}

    for m in re.finditer(
        r"^\s{2}(D\d{1,2}):\s*\{value:\s*([^,]+),", text, re.MULTILINE
    ):
        dim, raw = m.group(1), m.group(2).strip()
        data["scores"][dim] = None if raw in ("null", "~", "") else float(raw)

    for key in (
        "company", "id", "layer_primary", "entity_type",
        "strategic_role_primary", "uncomfortable_findings",
    ):
        m = re.search(rf"^{key}:\s*(.+)$", text, re.MULTILINE)
        if m:
            data[key] = m.group(1).strip().strip('"').strip("'")

    m = re.search(r"^flags:\s*\[(.*?)\]", text, re.MULTILINE)
    if m and m.group(1).strip():
        data["flags"] = [f.strip().strip('"') for f in m.group(1).split(",")]

    block = re.search(
        r"^contested_layer_proof:\n((?:\s{2}\w+:.*\n?)+)", text, re.MULTILINE
    )
    if block:
        proof = {}
        for line in block.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                proof[k.strip()] = v.strip().strip('"').strip("'")
        data["contested_layer_proof"] = proof

    return data


def compute(s: dict) -> dict | None:
    if any(s.get(f"D{i}") is None for i in range(1, 11)):
        return None
    d = {f"D{i}": s[f"D{i}"] for i in range(1, 11)}

    threat = (d["D9"] * 3 + d["D1"] * 2 + d["D3"] * 2 + d["D8"] * 1.5 + d["D2"] * 1) / 9.5
    partnership = (d["D10"] * 3 + d["D5"] * 2 + d["D7"] * 1.5 + d["D2"] * 1.5) / 8
    dependency = (d["D6"] * 2 + d["D3"] * 2 + d["D1"] * 1.5 + (5 - d["D5"]) * 1) / 6.5
    priority = max(threat, partnership) * (1 + d["D7"] / 10)

    return {
        "threat": round(threat, 2),
        "partnership": round(partnership, 2),
        "dependency_risk": round(dependency, 2),
        "priority": round(priority, 2),
    }


def interpret(idx: dict, role: str) -> list[str]:
    out = []
    if idx["threat"] >= 3.5:
        out.append(
            f"⚠ Threat {idx['threat']} ≥ 3.5 — Direct Competitor must be seriously "
            f"considered. Currently '{role}'. Justify in writing if not chosen."
        )
    if idx["partnership"] >= 3.5:
        out.append(
            f"→ Partnership {idx['partnership']} ≥ 3.5 — integration/partnership path "
            "must be evaluated BEFORE any 'build our own' recommendation."
        )
    if idx["dependency_risk"] >= 3.5:
        out.append(
            f"🔴 Dependency risk {idx['dependency_risk']} ≥ 3.5 — mitigation plan is "
            "MANDATORY: abstraction layer, second source, or exit path."
        )
    if idx["threat"] >= 3.0 and idx["partnership"] >= 3.0:
        out.append(
            "🟣 COMPLEX — high threat AND high leverage. The most demanding "
            "relationship type. Flag for explicit handling in Phase 7."
        )
    if not out:
        out.append("✓ No index thresholds breached.")
    return out


def main(company: str) -> int:
    path = COMPANIES / company / "scorecard.yaml"
    if not path.exists():
        print(f"✗ no scorecard at {path}")
        return 1

    data = parse_scorecard(path)
    idx = compute(data["scores"])

    print(f"\n\033[1m{data.get('company', company)}\033[0m  "
          f"{data.get('layer_primary', '?')} · {data.get('strategic_role_primary', '?')}")

    if idx is None:
        missing = [f"D{i}" for i in range(1, 11) if data["scores"].get(f"D{i}") is None]
        print(f"\n  ⚠ incomplete scorecard — missing: {', '.join(missing)}\n")
        return 1

    print("\n  \033[1mScores\033[0m")
    names = {
        "D1": "Layer ownership", "D2": "Technical depth", "D3": "Distribution",
        "D4": "Data advantage", "D5": "Ecosystem gravity", "D6": "Switching cost",
        "D7": "Healthcare relevance", "D8": "Velocity", "D9": "Threat to JARVIS",
        "D10": "Leverage value",
    }
    for k, label in names.items():
        v = data["scores"][k]
        print(f"    {k:<4} {label:<22} {int(v)}  {'●' * int(v)}{'○' * (5 - int(v))}")

    print("\n  \033[1mIndices\033[0m")
    for k, v in idx.items():
        print(f"    {k:<16} {v:>5.2f}  {'█' * int(v * 5):<25}")

    print("\n  \033[1mInterpretation\033[0m")
    for line in interpret(idx, data.get("strategic_role_primary", "?")):
        print(f"    {line}")
    print()
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: score.py <Company>")
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
