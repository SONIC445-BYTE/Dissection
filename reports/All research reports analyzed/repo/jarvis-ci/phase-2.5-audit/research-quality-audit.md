# Phase 2.5 — Research Quality Audit
`v1.0.0` · **THE HARD GATE** · Article VI

> No cross-company synthesis, pattern claim, ranking, or ecosystem conclusion may be produced until this audit passes.

---

## 1. Why this gate exists

Synthesis is **lossy compression of its inputs**. Compressing uneven inputs produces confident conclusions with invisible error bars — and those conclusions become load-bearing in architecture commitments and funding decisions long after anyone remembers which dossier was thin.

The failure is silent by construction. A synthesis built on 90 strong dossiers and 18 weak ones reads exactly like one built on 108 strong dossiers. There is no way to detect it downstream. It must be caught here.

**Article VI.3: if the audit fails, the remedy is re-running deficient dossiers, never softening the audit.**

---

## 2. The seven checks

### C1 — Coverage
Every registry entity except `self:true` has a ratified dossier.

| Metric | Threshold |
|---|---|
| Ratified / scoreable | 100% |
| Tier-1 entities ratified | 100% (no exceptions) |
| Registry entities added mid-phase and still unresearched | 0 |

*Tier-3 entities may be thin in depth but must exist with all 16 sections and explicit gap notes.*

### C2 — Depth variance ⭐ the critical check
Detects the exact failure the pipeline exists to prevent.

| Metric | Threshold | Action if breached |
|---|---|---|
| Word-count CV (ratified) | ≤ 0.40 | Re-run thin dossiers |
| Claim-count CV (ratified) | ≤ 0.40 | Re-run thin dossiers |
| Any tier-1 dossier < 50% of tier-1 mean | 0 allowed | Mandatory re-run |
| Any dossier with < 15 registered claims | 0 allowed | Mandatory re-run |

**Analyse by position, not just spread.** If dossiers 80–108 are systematically thinner than 1–20, that is context degradation across runs, and it invalidates the isolation principle's whole purpose. Compute the correlation between run order and depth; a negative correlation is a structural failure, not noise.

### C3 — Evidence integrity

| Check | Threshold |
|---|---|
| Claims with a tier marker | 100% |
| E1 claims sourced only to Tier C/D | 0 |
| E4 claims without falsifier | 0 |
| Source IDs referenced but absent from source table | 0 |
| Dossiers with zero E3/E4 claims | 0 — implausible certainty |
| Numeric claims without date | 0 |
| Sources > 12 months old | flagged `STALE`, must be justified |
| **Promotion violations** (same claim, different tiers) | **0 — hard fail** |

### C4 — Role classification consistency

| Check | Threshold |
|---|---|
| Direct Competitor share of scoreable entities | **≤ 15%** |
| Direct Competitor entries with complete three-part proof | 100% |
| Entities with `Threat_Index ≥ 3.5` **not** classified Direct Competitor | must carry written justification |
| Entities with `Dependency_Risk ≥ 3.5` without mitigation plan | 0 |
| Same-layer entities with wildly divergent roles | flag for review |

> If Direct Competitor exceeds 15%, the corpus has produced a **threat list**, not an intelligence base. Threat lists make teams defensive, imitative and slow.

### C5 — Contradiction handling

| Check | Threshold |
|---|---|
| Contradictions recorded with `CONTESTED` flag | 100% of known conflicts |
| Contradictions silently resolved by preference | 0 |
| Cross-dossier factual conflicts | **enumerated, not resolved** |

**Cross-dossier conflicts are expected and are not errors.** Two dossiers may report different figures for the same third-party fact because they used different sources. The audit's job is to *find and list* them so Phase 6 resolves them deliberately, with full visibility, rather than inheriting whichever number happened to appear first.

### C6 — Isolation integrity

| Check | Threshold |
|---|---|
| Cross-company comparative claims in Phase 2 dossiers | **0** |
| Repo/blueprint contamination (Phase R terms) | **0** |
| Dossiers citing other dossiers | 0 |

Machine-enforced by `validate.py`. A breach means the isolation principle failed and the affected dossier's independence is compromised.

### C7 — Analytical rigour

| Check | Threshold |
|---|---|
| Dossiers with ≥1 uncomfortable finding | 100% |
| Direct JARVIS analogues with ≥3 | 100% |
| Dossiers testing ≥1 thesis (T1–T4) | 100% |
| Dossiers with complete 8-question Final Reflection | 100% |
| Scores without justification | 0 |
| Open questions logged to `OPEN-QUESTIONS.md` | ≥1 per dossier |
| **Unanswered high-priority open questions** | enumerated for Phase 3–5 |

---

## 3. Audit outputs

The audit produces four artefacts, all consumed downstream:

| Artefact | Content | Consumed by |
|---|---|---|
| `audit-report.md` | Pass/fail per check with evidence | gate decision |
| `contradiction-ledger.md` | Every cross-dossier conflict, unresolved | **Phase 6** |
| `remediation-list.md` | Dossiers requiring re-run, with reason | Phase 2 re-runs |
| `AUDIT-PASSED` | Marker file — **only created on full pass** | `tools/gate.py` |

`gate.py` checks for the marker file. It cannot be created by passing "most" checks.

---

## 4. Failure protocol

1. **Do not proceed.** Do not begin Phase 3, 4, 5 or 6.
2. **Do not soften thresholds.** They were set before the data existed, deliberately.
3. Produce `remediation-list.md` naming each deficient dossier and the specific check failed.
4. Re-run those dossiers as **full fresh-context runs** — not patches. A dossier that failed depth cannot be topped up; the thinness reflects the original run's budget.
5. Re-run the audit from scratch.

> Patching a thin dossier produces a dossier that *passes the metric* without gaining the *rigour the metric proxies for*. This is Goodhart's law applied to your own strategy, and it is worse than failing the audit — because it passes.

---

## 5. Anti-gaming

The audit measures proxies. Proxies can be gamed, including unintentionally. Guard against:

| Gaming pattern | Detection |
|---|---|
| Padding word count with restated content | Claim density (claims per 1000 words) must stay in band |
| Inflating claim count with trivial claims | Sample review of 10% of claims for substance |
| Manufacturing uncomfortable findings that aren't | Uncomfortable findings must cite evidence, not opinion |
| Labelling everything E2 to avoid E1 scrutiny | Tier distribution per dossier must be plausible |
| Marking contradictions `CONTESTED` to avoid resolving | Contradiction ledger reviewed for genuine irresolvability |

**Claim density band:** 8–15 claims per 1,000 words. The exemplar sits at 10.6 (44 claims / 4,136 words). Outside this band in either direction warrants review — too low suggests padding, too high suggests trivial claims.

---

## 6. Current status

```
Dossiers ratified:        1 / 108   (0.9%)
Tier-1 ratified:          1 / 31
Depth variance:           n/a (needs ≥2)
Direct Competitor share:  0% of ratified (1 demoted from hypothesis)
Contradictions logged:    3 (all within Mem0, correctly flagged)
Isolation breaches:       0
AUDIT-PASSED marker:      ABSENT

STATUS: 🔒 GATE LOCKED
```

Phases 3, 4, 5 and 6 are correctly blocked.
