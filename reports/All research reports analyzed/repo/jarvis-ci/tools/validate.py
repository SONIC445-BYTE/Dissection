#!/usr/bin/env python3
"""Lint a Phase 2 dossier against the Research Constitution.

Enforces the rules in:
  02-evidence-rules.md  §7 (lint rules)
  00-research-constitution.md  Article II (isolation), III (stage), X (done)
  07-strategic-role-classification.md  (contested-layer proof)
  09-repo-context-isolation.md  (no repo contamination)

Exit 0 = ratifiable.
"""
from __future__ import annotations

import csv
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPANIES = ROOT / "phase-2-dossiers" / "Companies"
REGISTRY = ROOT / "phase-1-discovery" / "company-registry.yaml"

REQUIRED_SECTIONS = [
    "Executive Intelligence", "Company Intelligence", "Product Reverse Engineering",
    "Technical Architecture", "AI Architecture", "Developer Platform",
    "Distribution", "Business Model", "User Intelligence",
    "Healthcare Relevance", "Layer Analysis", "Moat Assessment",
    "Failure Analysis", "Competitive Attack Plan", "Lessons for JARVIS",
    "Evidence & Gaps",
]

REFLECTION_CUES = [
    "teach us that we did not know",
    "assumptions did it challenge",
    "opportunities does it reveal",
    "architecture are worth emulating",
    "deliberately avoid",
    "strengthen or weaken",
    "ecosystem and value chain",
    "new research questions",
]

# Repo contamination — Phase 2 must not know JARVIS's implementation.
REPO_TERMS = [
    r"\bAgentCore\b", r"\bLevel6\b", r"\bco_brain\b", r"\bODAVLoop\b",
    r"\bjarvis\.py\b", r"\bNetHyTechSTT\b", r"\bIntentRouter\b",
    r"\bCommandRouter\b", r"phase-2-adapter-wiring", r"\bRollbackManager\b",
    r"\bjarvis_orb\b", r"\bserp_fetcher\b", r"\bStage 0\.5\b",
]

TIER_MARKERS = ["🟢", "🟡", "🟠", "🔴", "E1", "E2", "E3", "E4"]


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warns: list[str] = []

    def err(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warns.append(msg)


def registry_names() -> set[str]:
    names = set()
    for line in REGISTRY.read_text(encoding="utf-8").splitlines():
        m = re.search(r"name:\s*([^,}]+)", line)
        if m:
            names.add(m.group(1).strip().strip('"').strip("'"))
    return names


def check_dossier(company: str, r: Report) -> None:
    path = COMPANIES / company / "dossier.md"
    if not path.exists():
        r.err(f"missing dossier.md at {path}")
        return
    text = path.read_text(encoding="utf-8")

    for sec in REQUIRED_SECTIONS:
        if sec.lower() not in text.lower():
            r.err(f"missing required section: {sec}")

    for cue in REFLECTION_CUES:
        if cue.lower() not in text.lower():
            r.err(f"Final Reflection incomplete — missing: '{cue}'")

    # Article II.5 — no cross-company comparison
    others = registry_names() - {company}
    for name in others:
        if len(name) < 4 or name.startswith("["):
            continue
        for pat in (
            rf"unlike {re.escape(name)}",
            rf"better than {re.escape(name)}",
            rf"worse than {re.escape(name)}",
            rf"compared to {re.escape(name)}",
            rf"{re.escape(name)} does this too",
        ):
            if re.search(pat, text, re.IGNORECASE):
                r.err(f"cross-company comparison (Article II.5): '{pat}'")

    # 09-repo-context-isolation
    for pat in REPO_TERMS:
        if re.search(pat, text):
            r.err(f"repo contamination (09-repo-context-isolation): {pat}")

    # Article VII.3 — mandatory discomfort
    if "uncomfortable" not in text.lower():
        r.err("no uncomfortable findings section (Article VII.3)")

    # Stage discipline
    if not re.search(r"\bS[0-4]\b", text):
        r.err("no stage declared (Article III)")

    # Evidence tiers present in prose
    if not any(m in text for m in TIER_MARKERS):
        r.err("no evidence tier markers found (Article IV.1)")

    # Thesis testing
    if not re.search(r"\bT[1-4]\b", text):
        r.warn("no thesis test found — ≥1 of T1–T4 expected")

    # Undated numerics in prose (crude heuristic, warn only)
    body = re.sub(r"\|.*\|", "", text)
    for m in re.finditer(r"\$[\d,.]+[MBK]?|\b\d[\d,]{3,}\b", body):
        window = body[max(0, m.start() - 160): m.end() + 160]
        if not re.search(r"20\d\d|S-\d{3}", window):
            r.warn(f"possibly undated number: '{m.group(0)}'")
            break


def check_evidence(company: str, r: Report) -> None:
    path = COMPANIES / company / "evidence-register.csv"
    if not path.exists():
        r.err("missing evidence-register.csv")
        return

    rows = [row for row in csv.DictReader(path.open(encoding="utf-8"))
            if not (row.get("claim_id") or "").startswith("EXAMPLE")]
    if not rows:
        r.err("evidence register contains only template EXAMPLE rows")
        return

    tiers: dict[str, int] = {}
    claims: dict[str, str] = {}
    today = dt.date.today()

    for i, row in enumerate(rows, start=2):
        cid = (row.get("claim_id") or "").strip()
        tier = (row.get("tier") or "").strip()
        claim = (row.get("claim") or "").strip()

        if not cid:
            r.err(f"row {i}: missing claim_id")
            continue
        if tier not in ("E1", "E2", "E3", "E4"):
            r.err(f"{cid}: invalid tier '{tier}'")
        tiers[tier] = tiers.get(tier, 0) + 1

        if not (row.get("source_ids") or "").strip():
            r.err(f"{cid}: no source_ids")

        if tier == "E4" and not (row.get("falsifier") or "").strip():
            r.err(f"{cid}: E4 speculation requires a falsifier (rule 2.7)")

        # Promotion violation — same claim, different tiers
        key = claim.lower()[:70]
        if key and key in claims and claims[key] != tier:
            r.err(f"{cid}: same claim appears at tier {claims[key]} and {tier} "
                  "(inference promotion, Article IV.2)")
        claims[key] = tier

        acc = (row.get("accessed") or "").strip()
        if acc:
            try:
                age = (today - dt.date.fromisoformat(acc)).days
                if age > 365:
                    r.warn(f"{cid}: source {age}d old — STALE")
            except ValueError:
                r.err(f"{cid}: bad date '{acc}'")

    if tiers.get("E3", 0) == 0 and tiers.get("E4", 0) == 0:
        r.warn("zero E3/E4 claims — implausible certainty, likely unlabelled inference")

    total = sum(tiers.values())
    if total < 15:
        r.warn(f"only {total} registered claims — thin for a full dossier")


def check_scorecard(company: str, r: Report) -> None:
    path = COMPANIES / company / "scorecard.yaml"
    if not path.exists():
        r.err("missing scorecard.yaml")
        return

    sys.path.insert(0, str(Path(__file__).parent))
    from score import compute, parse_scorecard  # noqa: E402

    data = parse_scorecard(path)

    for i in range(1, 11):
        if data["scores"].get(f"D{i}") is None:
            r.err(f"D{i} not scored")

    text = path.read_text(encoding="utf-8")
    for m in re.finditer(r"(D\d{1,2}):\s*\{value:\s*([^,]+),\s*justification:\s*\"(.*?)\"",
                         text, re.DOTALL):
        if not m.group(3).strip():
            r.err(f"{m.group(1)}: score without justification")

    role = data.get("strategic_role_primary", "")
    if role == "Direct Competitor":
        proof = data.get("contested_layer_proof", {})
        for field in ("layer", "jarvis_capability", "buyer_substitution"):
            if not proof.get(field):
                r.err(f"Direct Competitor requires contested_layer_proof.{field} "
                      "(07-strategic-role-classification §V.3)")

    try:
        if int(data.get("uncomfortable_findings", 0)) < 1:
            r.err("uncomfortable_findings must be ≥ 1 (Article VII.3)")
    except (TypeError, ValueError):
        r.err("uncomfortable_findings not set")

    idx = compute(data["scores"])
    if idx and idx["dependency_risk"] >= 3.5:
        dossier = COMPANIES / company / "dossier.md"
        if dossier.exists() and "mitigation" not in dossier.read_text(
            encoding="utf-8"
        ).lower():
            r.err(f"dependency_risk {idx['dependency_risk']} ≥ 3.5 but no "
                  "mitigation plan in dossier")


def main(company: str) -> int:
    r = Report()
    folder = COMPANIES / company
    if not folder.exists():
        print(f"✗ no dossier folder: {folder}")
        return 1

    check_dossier(company, r)
    check_evidence(company, r)
    check_scorecard(company, r)

    print(f"\n\033[1mvalidate: {company}\033[0m")
    if r.errors:
        print(f"\n  \033[31m{len(r.errors)} ERROR(S)\033[0m")
        for e in r.errors:
            print(f"    ✗ {e}")
    if r.warns:
        print(f"\n  \033[33m{len(r.warns)} warning(s)\033[0m")
        for w in r.warns:
            print(f"    ⚠ {w}")

    if not r.errors:
        print("\n  \033[32m✓ RATIFIABLE\033[0m — meets Article X definition of done\n")
        return 0
    print("\n  \033[31m✗ NOT RATIFIABLE\033[0m\n")
    return 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: validate.py <Company>")
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
