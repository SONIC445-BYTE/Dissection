#!/usr/bin/env python3
"""Phase 2.5 Research Quality Audit — the hard gate.

Runs the seven checks in phase-2.5-audit/research-quality-audit.md.
Creates the AUDIT-PASSED marker ONLY on a full pass.

Article VI.3: if this fails, re-run deficient dossiers. Never soften the audit.
"""
from __future__ import annotations

import csv
import re
import statistics
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPANIES = ROOT / "phase-2-dossiers" / "Companies"
AUDIT_DIR = ROOT / "phase-2.5-audit"
MARKER = AUDIT_DIR / "AUDIT-PASSED"

sys.path.insert(0, str(Path(__file__).parent))
from registry import load  # noqa: E402
from score import compute, parse_scorecard  # noqa: E402


class Check:
    def __init__(self, cid: str, name: str) -> None:
        self.id, self.name = cid, name
        self.failures: list[str] = []
        self.notes: list[str] = []

    @property
    def passed(self) -> bool:
        return not self.failures


def gather() -> list[dict]:
    out = []
    if not COMPANIES.exists():
        return out
    for folder in sorted(p for p in COMPANIES.iterdir() if p.is_dir()):
        d = folder / "dossier.md"
        e = folder / "evidence-register.csv"
        if not d.exists():
            continue
        text = d.read_text(encoding="utf-8")
        claims = []
        if e.exists():
            claims = [r for r in csv.DictReader(e.open(encoding="utf-8"))
                      if not (r.get("claim_id") or "").startswith("EXAMPLE")]
        res = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "validate.py"), folder.name],
            capture_output=True,
        )
        sc = folder / "scorecard.yaml"
        card = parse_scorecard(sc) if sc.exists() else {"scores": {}}
        out.append({
            "name": folder.name, "text": text, "words": len(text.split()),
            "claims": claims, "n_claims": len(claims),
            "ratified": res.returncode == 0, "card": card,
        })
    return out


def run_checks(dossiers: list[dict], entities: list[dict]) -> list[Check]:
    scoreable = [e for e in entities if not e.get("self") and e.get("layer") != "L15"]
    ratified = [d for d in dossiers if d["ratified"]]
    checks: list[Check] = []

    # C1 coverage
    c = Check("C1", "Coverage")
    if len(ratified) < len(scoreable):
        c.failures.append(f"{len(scoreable) - len(ratified)} of {len(scoreable)} "
                          "scoreable entities lack a ratified dossier")
    tier1 = [e for e in scoreable if e.get("tier") == 1]
    names = {d["name"].lower().replace("-", "") for d in ratified}
    missing_t1 = [e["name"] for e in tier1
                  if e["name"].lower().replace(" ", "").replace("/", "").replace("-", "")
                  not in {n.replace(" ", "") for n in names}]
    if missing_t1:
        c.notes.append(f"tier-1 outstanding: {len(missing_t1)}")
    checks.append(c)

    # C2 depth variance
    c = Check("C2", "Depth variance")
    if len(ratified) < 2:
        c.notes.append("needs >= 2 ratified dossiers")
    else:
        words = [d["words"] for d in ratified]
        nclaims = [d["n_claims"] for d in ratified]
        wcv = statistics.stdev(words) / statistics.mean(words)
        ccv = statistics.stdev(nclaims) / statistics.mean(nclaims)
        c.notes.append(f"word CV {wcv:.2f}, claim CV {ccv:.2f}")
        if wcv > 0.40:
            c.failures.append(f"word-count CV {wcv:.2f} > 0.40")
        if ccv > 0.40:
            c.failures.append(f"claim-count CV {ccv:.2f} > 0.40")
        wmean = statistics.mean(words)
        for d in ratified:
            if d["words"] < 0.5 * wmean:
                c.failures.append(f"{d['name']}: {d['words']}w < 50% of mean")
        # order correlation
        if len(ratified) >= 5:
            idx = list(range(len(ratified)))
            try:
                r = statistics.correlation(idx, words)
                c.notes.append(f"order/depth correlation {r:+.2f}")
                if r < -0.5:
                    c.failures.append(f"depth degrades with run order (r={r:+.2f}) "
                                      "- context degradation across runs")
            except Exception:
                pass
    for d in ratified:
        if d["n_claims"] < 15:
            c.failures.append(f"{d['name']}: only {d['n_claims']} claims (<15)")
    checks.append(c)

    # C3 evidence integrity
    c = Check("C3", "Evidence integrity")
    for d in ratified:
        seen: dict[str, str] = {}
        for row in d["claims"]:
            tier = (row.get("tier") or "").strip()
            if tier not in ("E1", "E2", "E3", "E4"):
                c.failures.append(f"{d['name']}/{row.get('claim_id')}: bad tier")
            if tier == "E4" and not (row.get("falsifier") or "").strip():
                c.failures.append(f"{d['name']}/{row.get('claim_id')}: E4 no falsifier")
            key = (row.get("claim") or "").lower()[:70]
            if key and key in seen and seen[key] != tier:
                c.failures.append(f"{d['name']}/{row.get('claim_id')}: "
                                  "PROMOTION VIOLATION")
            seen[key] = tier
        tiers = {t: sum(1 for r in d["claims"] if r.get("tier") == t)
                 for t in ("E1", "E2", "E3", "E4")}
        if tiers["E3"] + tiers["E4"] == 0:
            c.failures.append(f"{d['name']}: zero E3/E4 - implausible certainty")
    checks.append(c)

    # C4 role consistency
    c = Check("C4", "Role classification")
    roles: dict[str, int] = {}
    for d in ratified:
        role = d["card"].get("strategic_role_primary", "?")
        roles[role] = roles.get(role, 0) + 1
        idx = compute(d["card"].get("scores", {}))
        if idx:
            if idx["threat"] >= 3.5 and role != "Direct Competitor":
                if "justif" not in d["text"].lower():
                    c.failures.append(f"{d['name']}: threat {idx['threat']} >= 3.5 "
                                      f"but role '{role}' with no written justification")
            if idx["dependency_risk"] >= 3.5 and "mitigation" not in d["text"].lower():
                c.failures.append(f"{d['name']}: dependency {idx['dependency_risk']} "
                                  ">= 3.5 without mitigation plan")
    if ratified:
        dc = roles.get("Direct Competitor", 0)
        pct = 100 * dc / len(ratified)
        c.notes.append(f"Direct Competitor {dc}/{len(ratified)} ({pct:.1f}%)")
        if pct > 15:
            c.failures.append(f"Direct Competitor {pct:.1f}% > 15% - "
                              "corpus is a threat list, not intelligence")
    checks.append(c)

    # C5 contradictions
    c = Check("C5", "Contradiction handling")
    total = sum(1 for d in ratified for r in d["claims"]
                if (r.get("contested") or "").strip().lower() == "yes")
    c.notes.append(f"{total} contested claims flagged across corpus")
    checks.append(c)

    # C6 isolation
    c = Check("C6", "Isolation integrity")
    repo_terms = [r"\bAgentCore\b", r"\bLevel6\b", r"\bco_brain\b", r"\bODAVLoop\b",
                  r"\bNetHyTechSTT\b", r"phase-2-adapter-wiring"]
    for d in ratified:
        for pat in repo_terms:
            if re.search(pat, d["text"]):
                c.failures.append(f"{d['name']}: repo contamination {pat}")
    checks.append(c)

    # C7 analytical rigour
    c = Check("C7", "Analytical rigour")
    for d in ratified:
        try:
            if int(d["card"].get("uncomfortable_findings", 0)) < 1:
                c.failures.append(f"{d['name']}: no uncomfortable findings")
        except (TypeError, ValueError):
            c.failures.append(f"{d['name']}: uncomfortable_findings unset")
        if not re.search(r"\bT[1-4]\b", d["text"]):
            c.failures.append(f"{d['name']}: no thesis test")
        if d["words"]:
            density = 1000 * d["n_claims"] / d["words"]
            if not (8 <= density <= 15):
                c.notes.append(f"{d['name']}: claim density {density:.1f} "
                               "outside 8-15 band")
    checks.append(c)

    return checks


def main() -> int:
    entities = load()
    dossiers = gather()
    checks = run_checks(dossiers, entities)

    scoreable = [e for e in entities if not e.get("self") and e.get("layer") != "L15"]
    ratified = [d for d in dossiers if d["ratified"]]

    print("\n\033[1mPHASE 2.5 - RESEARCH QUALITY AUDIT\033[0m")
    print(f"  {len(ratified)} / {len(scoreable)} dossiers ratified\n")

    for c in checks:
        badge = "\033[32mPASS\033[0m" if c.passed else "\033[31mFAIL\033[0m"
        print(f"  [{badge}] {c.id} {c.name}")
        for n in c.notes:
            print(f"          . {n}")
        for f in c.failures[:6]:
            print(f"          \033[31mx {f}\033[0m")
        if len(c.failures) > 6:
            print(f"          \033[31mx ... +{len(c.failures) - 6} more\033[0m")

    all_pass = all(c.passed for c in checks)
    print()
    if all_pass:
        MARKER.write_text(
            f"AUDIT PASSED\ndossiers: {len(ratified)}/{len(scoreable)}\n",
            encoding="utf-8",
        )
        print("  \033[32mAUDIT PASSED\033[0m - marker created, Phases 3-6 unlocked\n")
        return 0

    if MARKER.exists():
        MARKER.unlink()
    failed = [c.id for c in checks if not c.passed]
    print(f"  \033[31mAUDIT FAILED\033[0m - {', '.join(failed)}")
    print("  Remedy: re-run deficient dossiers as FULL fresh-context runs.")
    print("  Never patch to pass the metric (Article VI.3).\n")
    return 1


if __name__ == "__main__":
    sys.exit(main())
