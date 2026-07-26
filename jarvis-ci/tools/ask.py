#!/usr/bin/env python3
"""Query layer over the registry substrate (G13).

Nine registries without interrogation are nine filing cabinets.
Dependency-free: parses the block-style YAML subset used by registries/.

  ask.py coverage                    # THE query: JARVIS capability map
  ask.py capability --gap
  ask.py radar --ring commodity
  ask.py decision --open --one-way
  ask.py pattern --confirmed
  ask.py failure --exposure high
  ask.py principle --durability MEDIUM
  ask.py unknown --priority critical
  ask.py priority
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REG = Path(__file__).resolve().parent.parent / "registries"

C = {"b": "\033[1m", "d": "\033[2m", "r": "\033[31m", "g": "\033[32m",
     "y": "\033[33m", "c": "\033[36m", "m": "\033[35m", "x": "\033[0m"}


def load_items(fname: str, key: str) -> list[dict]:
    """Parse top-level list items under `key:` from a registry file."""
    path = REG / fname
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8").splitlines()

    start, base_indent = None, None
    for i, line in enumerate(lines):
        if re.match(rf"^{key}:\s*$", line):
            start = i + 1
            break
    if start is None:
        return []

    items: list[dict] = []
    cur: dict | None = None
    for line in lines[start:]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        if re.match(r"^\w[\w-]*:\s*$", line) and indent == 0:
            break  # next top-level key
        if stripped.startswith("- "):
            if base_indent is None:
                base_indent = indent
            if indent == base_indent:
                if cur:
                    items.append(cur)
                cur = {}
                stripped = stripped[2:]
                indent += 2
                # inline flow mapping: - {rank: 1, company: "X", ...}
                if stripped.startswith("{") and stripped.rstrip().endswith("}"):
                    body = stripped.strip()[1:-1]
                    parts, depth, quote, buf = [], 0, None, []
                    for ch in body:
                        if quote:
                            if ch == quote:
                                quote = None
                            buf.append(ch)
                        elif ch in "\"'":
                            quote = ch
                            buf.append(ch)
                        elif ch == "[":
                            depth += 1
                            buf.append(ch)
                        elif ch == "]":
                            depth -= 1
                            buf.append(ch)
                        elif ch == "," and depth == 0:
                            parts.append("".join(buf))
                            buf = []
                        else:
                            buf.append(ch)
                    if buf:
                        parts.append("".join(buf))
                    for p in parts:
                        if ":" in p:
                            k, v = p.split(":", 1)
                            cur[k.strip()] = v.strip().strip('"').strip("'")
                    items.append(cur)
                    cur = None
                    continue
            else:
                continue
        if cur is None:
            continue
        m = re.match(r"^([\w_]+):\s*(.*)$", stripped)
        if m and indent <= (base_indent or 0) + 2:
            k, v = m.group(1), m.group(2).strip()
            if v.startswith("[") and v.endswith("]"):
                inner = v[1:-1].strip()
                cur[k] = [x.strip().strip("\"'") for x in inner.split(",") if x.strip()]
            elif v in ("", "|", ">"):
                cur.setdefault(k, "")
            else:
                cur[k] = v.strip('"').strip("'")
    if cur:
        items.append(cur)
    return items


def hdr(text: str) -> None:
    print(f"\n{C['b']}{text}{C['x']}")


def coverage() -> None:
    """The single most valuable query in the system (G15)."""
    caps = load_items("capability-registry.yaml", "capabilities")
    hdr("JARVIS CAPABILITY COVERAGE MAP")
    print(f"{C['d']}  ecosystem capability -> JARVIS state -> gap class{C['x']}\n")

    states = {"absent": C["r"], "designed": C["y"], "built": C["y"],
              "wired": C["c"], "verified": C["g"]}
    buckets: dict[str, list] = {}
    for c in caps:
        buckets.setdefault(c.get("opportunity_class", "?"), []).append(c)

    order = ["moat", "contested-hard", "contested-neglected", "commodity", "structural"]
    advice = {
        "moat": "BUILD — this is the roadmap",
        "contested-hard": "EVALUATE — unclaimed because hard, not neglected",
        "contested-neglected": "OPPORTUNITY — unclaimed and possibly tractable",
        "commodity": "INTEGRATE — never build",
        "structural": "DEPEND — never contest",
    }
    for cls in order:
        if cls not in buckets:
            continue
        print(f"  {C['b']}{cls.upper()}{C['x']}  {C['d']}{advice[cls]}{C['x']}")
        for c in buckets[cls]:
            st = c.get("jarvis_state", "?")
            col = states.get(st, "")
            opp = c.get("jarvis_opportunity", "?")
            flag = " <" if (st == "absent" and opp == "high") else ""
            print(f"    {col}{st:<9}{C['x']} {c.get('name', c.get('id'))[:46]:<46}"
                  f" opp:{opp}{C['r']}{flag}{C['x']}")
        print()

    gaps = [c for c in caps
            if c.get("jarvis_state") == "absent" and c.get("jarvis_opportunity") == "high"]
    print(f"  {C['r']}{len(gaps)} high-opportunity capabilities with zero JARVIS coverage{C['x']}\n")


def capability(args: list[str]) -> None:
    caps = load_items("capability-registry.yaml", "capabilities")
    if "--gap" in args:
        caps = [c for c in caps if c.get("jarvis_state") == "absent"
                and c.get("jarvis_opportunity") == "high"]
        hdr("CAPABILITY GAPS (absent + high opportunity)")
    elif "--unclaimed" in args:
        caps = [c for c in caps if c.get("ecosystem_trend") == "unclaimed"]
        hdr("UNCLAIMED CAPABILITIES (negative space)")
    else:
        hdr("ALL CAPABILITIES")
    for c in caps:
        print(f"\n  {C['b']}{c.get('name')}{C['x']}  {C['d']}{c.get('layer')} · "
              f"{c.get('maturity')} · {c.get('opportunity_class')}{C['x']}")
        print(f"    trend: {c.get('ecosystem_trend')}   jarvis: "
              f"{C['r']}{c.get('jarvis_state')}{C['x']}")
        if c.get("ecosystem_note"):
            print(f"    {C['y']}note:{C['x']} {c['ecosystem_note'][:150]}")
        if c.get("opportunity_caveat"):
            print(f"    {C['r']}caveat:{C['x']} {c['opportunity_caveat'][:150]}")
    print()


def radar(args: list[str]) -> None:
    techs = load_items("technology-radar.yaml", "technologies")
    if "--ring" in args:
        ring = args[args.index("--ring") + 1]
        techs = [t for t in techs if t.get("ring") == ring]
        hdr(f"TECHNOLOGY RADAR — ring: {ring}")
    elif "--moving-inward" in args:
        techs = [t for t in techs if t.get("movement") == "inward"]
        hdr("TECHNOLOGY RADAR — commoditising (moving inward)")
    else:
        hdr("TECHNOLOGY RADAR")
    rings = {"emerging": C["m"], "growing": C["c"], "mature": C["g"],
             "commodity": C["y"], "declining": C["r"]}
    arrows = {"inward": "-->", "outward": "<--", "static": "---"}
    for t in techs:
        col = rings.get(t.get("ring", ""), "")
        print(f"\n  {col}{t.get('ring', '?'):<10}{C['x']} {arrows.get(t.get('movement', ''), '')} "
              f"{C['b']}{t.get('name')}{C['x']}")
        print(f"    importance: {t.get('strategic_importance')}   risk: {t.get('risk')}"
              f"   lifespan: {t.get('expected_lifespan_years')}y")
        print(f"    {C['c']}-> {t.get('jarvis_recommendation', '').upper()}{C['x']}"
              f"  {C['d']}{t.get('recommendation_rationale', '')[:90]}{C['x']}")
    print()


def decision(args: list[str]) -> None:
    decs = load_items("decision-register.yaml", "decisions")
    if "--open" in args:
        decs = [d for d in decs if d.get("status") == "open"]
    if "--one-way" in args:
        decs = [d for d in decs if d.get("reversibility") == "one-way"]
    hdr("IRREVERSIBLE DECISION REGISTER")
    for d in decs:
        rev = d.get("reversibility", "?")
        col = C["r"] if rev == "one-way" else C["y"] if rev == "costly" else C["g"]
        print(f"\n  {C['b']}{d.get('id')}{C['x']} {d.get('title')}")
        print(f"    {col}{rev.upper()}{C['x']}  status: {d.get('status')}"
              f"   timing: {d.get('recommended_timing')}")
        print(f"    cost curve: {d.get('cost_curve')}   confidence: {d.get('confidence')}")
        if d.get("cost_of_change_later"):
            print(f"    {C['d']}{d['cost_of_change_later'][:160]}{C['x']}")
    n = len([d for d in decs if d.get("reversibility") == "one-way"
             and d.get("status") == "open"])
    if n:
        print(f"\n  {C['r']}{n} ONE-WAY decisions still OPEN{C['x']}")
        print(f"  {C['d']}Alternatives are visible now. They will not be later.{C['x']}")
    print()


def pattern(args: list[str]) -> None:
    pats = load_items("pattern-library.yaml", "patterns")
    if "--confirmed" in args:
        pats = [p for p in pats if p.get("status") == "CONFIRMED"]
        hdr("CONFIRMED PATTERNS (>=3 instances)")
        if not pats:
            print(f"\n  {C['y']}None yet.{C['x']} {C['d']}Patterns promote at 3 instances."
                  f" Two is a coincidence.{C['x']}\n")
            return
    else:
        hdr("PATTERN LIBRARY")
    for p in pats:
        rec = p.get("jarvis_recommendation", "?")
        col = C["g"] if rec == "adopt" else C["r"] if rec == "reject" else C["y"]
        anti = f" {C['r']}[ANTIPATTERN]{C['x']}" if p.get("is_antipattern") else ""
        print(f"\n  {C['b']}{p.get('id')}{C['x']} {p.get('name')}{anti}")
        print(f"    status: {p.get('status')} ({p.get('instances')}x)   "
              f"{col}-> {rec.upper()}{C['x']}")
        if p.get("jarvis_rationale"):
            print(f"    {C['d']}{p['jarvis_rationale'][:150]}{C['x']}")
    print()


def failure(args: list[str]) -> None:
    fails = load_items("failure-library.yaml", "failures")
    if "--exposure" in args:
        lvl = args[args.index("--exposure") + 1]
        fails = [f for f in fails if f.get("jarvis_exposure") == lvl]
        hdr(f"FAILURE MODES — JARVIS exposure: {lvl}")
    else:
        hdr("FAILURE PATTERN LIBRARY")
    for f in fails:
        exp = f.get("jarvis_exposure", "?")
        col = C["r"] if exp == "high" else C["y"] if exp == "medium" else C["g"]
        print(f"\n  {C['b']}{f.get('id')}{C['x']} {f.get('name')}")
        print(f"    severity: {f.get('severity')}   "
              f"jarvis exposure: {col}{exp}{C['x']}")
        if f.get("mechanism"):
            print(f"    {C['d']}{f['mechanism'][:180]}{C['x']}")
        if f.get("jarvis_guard"):
            print(f"    {C['g']}guard:{C['x']} {f['jarvis_guard'][:140]}")
    print()


def principle(args: list[str]) -> None:
    prins = load_items("principle-library.yaml", "principles")
    if "--durability" in args:
        lvl = args[args.index("--durability") + 1]
        prins = [p for p in prins if p.get("durability_5yr") == lvl]
    hdr("STRATEGIC PRINCIPLES")
    for p in prins:
        d = p.get("durability_5yr", "?")
        col = C["g"] if d == "HIGH" else C["y"] if d == "MEDIUM" else C["r"]
        print(f"\n  {C['b']}{p.get('id')}{C['x']}  {col}durability {d}{C['x']}")
        print(f"    \"{p.get('statement', '')}\"")
        print(f"    {C['r']}fails when:{C['x']} {p.get('fails_when', '')[:150]}")
        print(f"    {C['c']}-> {p.get('jarvis_verdict', '').upper()}{C['x']}")
    print()


def unknown(args: list[str]) -> None:
    unks = load_items("unknown-unknowns.yaml", "probes")
    if "--priority" in args:
        lvl = args[args.index("--priority") + 1]
        unks = [u for u in unks if u.get("priority") == lvl]
    hdr("UNKNOWN UNKNOWNS")
    for u in unks:
        pr = u.get("priority", "?")
        col = C["r"] if pr == "critical" else C["y"] if pr == "high" else C["d"]
        print(f"\n  {C['b']}{u.get('id')}{C['x']} {col}[{pr}]{C['x']} "
              f"{C['d']}{u.get('probe_class')}{C['x']}")
        print(f"    {u.get('question', '')[:220]}")
        if u.get("would_invalidate"):
            print(f"    {C['r']}would invalidate:{C['x']} {u['would_invalidate']}")
    print()


def priority() -> None:
    items = load_items("research-priority.yaml", "current_ranking")
    hdr("RESEARCH PRIORITY — what to run next, and why")
    print(f"{C['d']}  Re-ranked from evidence. Phase 1's tier guess is now the "
          f"least-weighted input.{C['x']}\n")
    for i in items:
        print(f"  {C['b']}{i.get('rank'):>2}.{C['x']} {i.get('company', ''):<20} "
              f"{C['c']}{i.get('score')}{C['x']}  {C['d']}{i.get('why', '')}{C['x']}")
    print()


def dashboard() -> None:
    caps = load_items("capability-registry.yaml", "capabilities")
    decs = load_items("decision-register.yaml", "decisions")
    pats = load_items("pattern-library.yaml", "patterns")
    fails = load_items("failure-library.yaml", "failures")
    prins = load_items("principle-library.yaml", "principles")
    unks = load_items("unknown-unknowns.yaml", "probes")
    cons = load_items("contradiction-ledger.yaml", "contradictions")
    techs = load_items("technology-radar.yaml", "technologies")

    hdr("STRATEGIC INTELLIGENCE PLATFORM — substrate status")
    print(f"""
  capabilities tracked      {len(caps):>3}   ({len([c for c in caps if c.get('jarvis_state') == 'absent'])} absent in JARVIS)
  technologies on radar     {len(techs):>3}   ({len([t for t in techs if t.get('movement') == 'inward'])} commoditising)
  irreversible decisions    {len(decs):>3}   ({C['r']}{len([d for d in decs if d.get('reversibility') == 'one-way' and d.get('status') == 'open'])} one-way still OPEN{C['x']})
  patterns                  {len(pats):>3}   ({len([p for p in pats if p.get('status') == 'CONFIRMED'])} confirmed)
  failure modes             {len(fails):>3}   ({len([f for f in fails if f.get('jarvis_exposure') == 'high'])} high JARVIS exposure)
  principles                {len(prins):>3}
  unknown-unknown probes    {len(unks):>3}   ({len([u for u in unks if u.get('priority') == 'critical'])} critical)
  contradictions            {len(cons):>3}   ({len([c for c in cons if c.get('status', '').startswith('unresolved')])} unresolved)

  {C['d']}source: 1 ratified dossier. Substrate grows with every run.{C['x']}
""")


CMDS = {
    "coverage": lambda a: coverage(), "capability": capability, "radar": radar,
    "decision": decision, "pattern": pattern, "failure": failure,
    "principle": principle, "unknown": unknown,
    "priority": lambda a: priority(), "dashboard": lambda a: dashboard(),
}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in CMDS:
        print(__doc__)
        print("commands:", ", ".join(CMDS))
        sys.exit(2)
    CMDS[sys.argv[1]](sys.argv[2:])
