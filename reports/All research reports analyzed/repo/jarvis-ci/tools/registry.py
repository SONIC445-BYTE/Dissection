#!/usr/bin/env python3
"""Registry loader + validator for the JARVIS CI knowledge base.

Deliberately dependency-free: parses the restricted YAML subset used by
company-registry.yaml (flow-style mappings, one per line) so the toolchain
runs anywhere without pip install.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "phase-1-discovery" / "company-registry.yaml"

VALID_LAYERS = {f"L{i}" for i in range(16)}
VALID_ROLES = {
    "Foundational Dependency",
    "Integration Target",
    "Direct Competitor",
    "Potential Partner",
    "Technology Supplier",
    "Market Signal",
}
VALID_TYPES = {
    "commercial", "oss-project", "oss-commercial", "standard",
    "government-infra", "research-lab", "internal",
}


def _split_top_level(body: str) -> list[str]:
    """Split a flow mapping body on commas that are not inside [] or quotes."""
    parts, depth, quote, buf = [], 0, None, []
    for ch in body:
        if quote:
            if ch == quote:
                quote = None
            buf.append(ch)
            continue
        if ch in "\"'":
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
    return parts


def _coerce(val: str):
    val = val.strip()
    if val.startswith("[") and val.endswith("]"):
        inner = val[1:-1].strip()
        return [v.strip().strip("\"'") for v in inner.split(",") if v.strip()] if inner else []
    if len(val) >= 2 and val[0] in "\"'" and val[-1] == val[0]:
        return val[1:-1]
    if val in ("true", "True"):
        return True
    if val in ("false", "False"):
        return False
    if val in ("null", "None", "~", ""):
        return None
    if re.fullmatch(r"-?\d+", val):
        return int(val)
    return val


def load() -> list[dict]:
    entities: list[dict] = []
    for raw in REGISTRY.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line.startswith("- {"):
            continue
        body = line[line.index("{") + 1: line.rindex("}")]
        entity: dict = {}
        for part in _split_top_level(body):
            if ":" not in part:
                continue
            k, v = part.split(":", 1)
            entity[k.strip()] = _coerce(v)
        entities.append(entity)
    return entities


def validate(entities: list[dict]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()

    for e in entities:
        eid = e.get("id", "<missing id>")
        if not e.get("id"):
            errors.append(f"ERROR: entity with no id: {e}")
            continue
        if eid in seen:
            errors.append(f"ERROR: duplicate id '{eid}'")
        seen.add(eid)

        if e.get("layer") not in VALID_LAYERS:
            errors.append(f"ERROR: {eid}: invalid layer {e.get('layer')!r}")
        if e.get("type") not in VALID_TYPES:
            errors.append(f"ERROR: {eid}: invalid type {e.get('type')!r}")

        role = e.get("role_hypothesis")
        is_self = bool(e.get("self"))
        if is_self:
            if role is not None:
                errors.append(f"ERROR: {eid}: self:true entity must have null role")
            if e.get("tier") != 0:
                errors.append(f"ERROR: {eid}: self:true entity must be tier 0")
        elif e.get("layer") == "L15":
            pass  # unclaimed frontier slots legitimately carry no role
        elif role not in VALID_ROLES:
            errors.append(f"ERROR: {eid}: invalid role_hypothesis {role!r}")

        if not is_self and e.get("tier") not in (1, 2, 3):
            errors.append(f"ERROR: {eid}: tier must be 1, 2 or 3")

    return errors


def _bar(n: int, total: int, width: int = 28) -> str:
    filled = round(width * n / total) if total else 0
    return "█" * filled + "·" * (width - filled)


def report(entities: list[dict]) -> None:
    scored = [e for e in entities if not e.get("self") and e.get("layer") != "L15"]
    total = len(entities)

    print(f"\n\033[1mJARVIS CI — Company Registry\033[0m")
    print(f"{total} entities · {len(scored)} scoreable · "
          f"{sum(1 for e in entities if e.get('self'))} self · "
          f"{sum(1 for e in entities if e.get('layer') == 'L15')} frontier\n")

    print("\033[1mBy layer\033[0m")
    for i in range(16):
        layer = f"L{i}"
        members = [e for e in entities if e.get("layer") == layer]
        if not members:
            continue
        t1 = sum(1 for e in members if e.get("tier") == 1)
        print(f"  {layer:<4} {len(members):>3}  {_bar(len(members), 22)}  tier-1: {t1}")

    print("\n\033[1mBy role hypothesis\033[0m  (preliminary — dossiers decide)")
    counts: dict[str, int] = {}
    for e in scored:
        counts[e.get("role_hypothesis", "?")] = counts.get(e.get("role_hypothesis", "?"), 0) + 1
    for role, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        pct = 100 * n / len(scored)
        flag = ""
        if role == "Direct Competitor":
            flag = "  ✅ healthy (<15%)" if pct <= 15 else "  ⚠ COMPETITOR INFLATION"
        print(f"  {role:<26} {n:>3}  {pct:>5.1f}%{flag}")

    print("\n\033[1mBy tier\033[0m")
    for tier in (1, 2, 3):
        n = sum(1 for e in entities if e.get("tier") == tier)
        print(f"  Tier {tier}  {n:>3}  {_bar(n, 45)}")

    dead = [e for e in entities if e.get("entity_status") == "dead"]
    if dead:
        print(f"\n\033[1mPost-mortem subjects\033[0m  ({len(dead)} — cleanest evidence in the corpus)")
        for e in dead:
            print(f"  · {e['name']}")

    frontier = [e for e in entities if e.get("layer") == "L15"]
    if frontier:
        print(f"\n\033[1mL15 frontier / negative space\033[0m  ({len(frontier)} nominations)")
        for e in frontier:
            print(f"  · {e['name']}")

    print(f"\n\033[1mNext up\033[0m  (tier-1 research order)")
    for e in [x for x in entities if x.get("tier") == 1][:8]:
        print(f"  {e['layer']:<4} {e['name']}")
    print()


if __name__ == "__main__":
    ents = load()
    errs = validate(ents)
    report(ents)
    if errs:
        print("\033[31m" + f"{len(errs)} validation error(s):" + "\033[0m")
        for err in errs:
            print("  " + err)
        sys.exit(1)
    print("\033[32m✓ registry valid\033[0m\n")
