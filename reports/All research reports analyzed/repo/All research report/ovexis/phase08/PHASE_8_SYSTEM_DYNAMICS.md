# PHASE 8 — SYSTEM DYNAMICS
## Causal Loops, Leverage Points, and Why the Market Stays Stuck

**Phase:** 8 of 16 (+ Ω) · **Date:** 2026-07-26 · **Status:** COMPLETE — canonical
**Outputs:** `exports/phase8_system_dynamics.{json,yaml}`, `exports/phase8_leverage_points.csv`

**9 loops: 6 reinforcing (4 vicious, 2 virtuous), 3 balancing.**

---

## 8.1 THE VICIOUS REINFORCING LOOPS

### R1 — The Commit Gap Loop *(the deepest structure in the market)*

```
AI produces recommendation → human must execute it → execution slow or skipped
   → outcome data never captured → AI cannot learn from outcomes
      → recommendation quality plateaus → trust falls → less execution ──┐
   └──────────────────────────────────────────────────────────────────────┘
```

**Evidence:** Phase 2 F-2.12, Phase 3 F-3.1, Phase 5 F-5.1 — four independent confirmations.

This explains *why* the commit gap persists rather than closing. It is self-sealing: because software stops at the recommendation, **no outcome data is ever generated**, so the recommendation engine cannot improve, so trust never rises to the level required for execution.

> The market is not failing to close the gap through inattention. It has built a structure that **prevents** the gap from closing.

**Leverage:** execute *and* capture in one loop. This is the only intervention that creates outcome data where none exists. JARVIS's ODAV loop (observe → decide → act → **verify**) is already this shape.

### R2 — The Documentation Burden Loop

```
billing requires a written artifact → clinician documents for billing not care
   → note quality degrades → data quality degrades → AI trained on poor data
      → AI output distrusted → more manual documentation ──┐
   └────────────────────────────────────────────────────────┘
```

This is the loop the brief itself proposed as an example — and the corpus confirms it (pajama time, click fatigue, EHR burden). Phase 7 F-7.2 adds the root: the note exists for **payment**, not care.

**Leverage:** decouple capture from the billing artifact — capture once, render many. Not available to a solo builder, which is precisely why ambient scribing (19 competitors) attacks the symptom.

### R3 — The Integration Avoidance Loop

```
integration is expensive → vendors avoid deep integration → workflows stay fragmented
   → staff re-key between systems → manual work becomes normalised
      → nobody demands integration → integration stays expensive ──┐
   └──────────────────────────────────────────────────────────────────┘
```

**Evidence:** 253 fragmented HMIS vendors (Phase 2); `bot_integration_effort` only 14 corpus hits (Phase 5) — *the market has stopped even discussing the problem*, which is the loop's signature.

**Leverage:** drive integration marginal cost toward zero via computer-use adapters (DL-046).

### R4 — The Consumer Subscription Trap

```
payer revenue blocked by clinical validation cost → company sells to consumer
   → CAC rises → retention pressure → feature breadth over depth
      → clinical validation deferred → payer revenue stays blocked ──┐
   └──────────────────────────────────────────────────────────────────┘
```

**Evidence:** Phase 2 F-2.7 (19/21 discuss payer revenue, nearly all bill consumers); Phase 5 F-5.4 (churn 11 companies, CAC 11 companies — both GREEN).

This is the structural explanation for Phase 2's AI-11. Consumer subscription is not a choice; it is a **trap with a self-reinforcing wall**.

**Leverage:** enter on the *operational budget*, which requires no clinical validation — bypassing the loop entirely.

---

## 8.2 THE VIRTUOUS LOOPS

### R5 — The Trust Compounding Loop ⭐ *the core Ovexis loop*

```
honest failure reported → user calibrates expectations → user delegates more
   → more actions executed → more provenance accumulated
      → audit confidence rises → more delegation authorised ──┐
   └────────────────────────────────────────────────────────────┘
```

**Evidence:** Phase 2 F-2.11 (trust flows through traceability), Phase 7 F-7.4 (trust primitives strengthen under autonomy), JARVIS `resolution_gate.py` CB-05.

**F-8.1 — Honest failure is not a safety feature; it is the entry condition for a compounding loop.** A system that silently no-ops cannot enter R5 at all, because the user never learns where the boundary is and therefore never delegates further. JARVIS's *"I don't know how to control [platform] yet"* is the cheapest possible entry into the only virtuous loop available.

This retrospectively justifies DL-011 at the systems level rather than the ethical level.

### R6 — The Adapter Coverage Flywheel

```
adapter built → workflow automated end-to-end → usage generates failure cases
   → adapter hardens → more platforms viable → coverage attracts users → more adapters ──┐
```

**F-8.2 — JARVIS's 160 adapters produced zero flywheel because 149 are fabricated (CB-04).** The flywheel requires *end-to-end completion* to generate failure cases. An adapter that navigates but never clicks Send produces no learning signal. **Three real adapters would spin the flywheel; 160 fake ones do not.**

This is the systems-level argument for depth-first over breadth-first, and it directly contradicts the repository's existing strategy.

---

## 8.3 THE BALANCING LOOPS

| ID | Loop | Structure | Leverage |
|---|---|---|---|
| **B1** | Liability | automation ↑ → liability exposure ↑ → human review reinstated → automation benefit capped | **Graduated autonomy per action class** (DL-048) raises the cap without raising exposure |
| **B2** | Incumbent lock-in | new tool → requires HMIS change → switching cost blocks → tool adapts around HMIS → capability ceiling | **Operate where the HMIS doesn't** (Phase-6 Tier 1) — the ceiling doesn't bind |
| **B3** | Clinical safety | error → scrutiny ↑ → guardrails tighten → autonomy ↓ → error rate ↓ | **Pre-build the guardrail** — cheaper than recovering lost trust |

**F-8.3 — B1 and B2 are why every company in the corpus stalled at the same place.** They are not competitive failures; they are structural ceilings. Any strategy that does not explicitly defeat B1 (liability) and B2 (lock-in) will hit the identical ceiling regardless of execution quality.

Phase 6's Tier-1 selection defeats both **by construction**: operational workflows carry no clinical liability (B1 doesn't bind) and are not owned by the HMIS (B2 doesn't bind). That was not the reason they were selected — it is independent confirmation that the selection is structurally sound.

---

## 8.4 RANKED LEVERAGE POINTS

| # | Leverage point | Loop | Cost | JARVIS status |
|---|---|---|---|---|
| 1 | **Execute and capture in one loop** | R1 | MED | ODAV loop already observe-act-**verify** |
| 2 | **Honest failure as trust entry point** | R5 | **LOW** | `resolution_gate.py` exists (174 LOC) |
| 3 | **Enter on operational budget** | R4 + B2 | **LOW** | go-to-market, no build |
| 4 | **Depth-first adapters** | R6 | MED | ⚠️ contradicts existing 160-adapter strategy |
| 5 | Graduated autonomy per action class | B1 | MED | `feature_gate` has OFF/SHADOW/SUGGEST/FORCE |
| 6 | Zero-marginal-cost integration | R3 | HIGH | `ui_automation_execution` 1,747 LOC |

**F-8.4 — The three highest-leverage interventions are all LOW or MEDIUM cost, and two require no new code.** Honest failure exists. Operational-budget entry is a positioning decision. Graduated autonomy is already scaffolded in `feature_gate`'s four modes.

For a solo builder (DL-007), this is the most important finding in Phase 8: **the leverage is in sequencing and positioning, not in building more.**

---

## 8.5 DELIVERABLES

### 🟢 Verified Facts
| # | Fact | Evidence |
|---|---|---|
| VF-67 | 9 loops identified: 4 vicious reinforcing, 2 virtuous reinforcing, 3 balancing | Loop construction |
| VF-68 | R1 (commit gap) is confirmed by 4 independent phase methods | Phases 2, 3, 4, 5 |
| VF-69 | `feature_gate` already implements OFF/SHADOW/SUGGEST/FORCE — graduated autonomy scaffolding exists | Phase-1 CB, code |
| VF-70 | 149 of 160 adapters fabricated → R6 flywheel never started | CB-04 |

### 🧠 Architectural Inferences
- **AI-40:** The commit gap is self-sealing — it prevents the outcome data that would close it.
- **AI-41:** Honest failure is the entry condition for the only virtuous loop available (R5).
- **AI-42:** B1 and B2 are structural ceilings, not competitive failures — they explain why all 19 companies stalled similarly.
- **AI-43:** Phase-6 Tier-1 opportunities defeat B1 and B2 by construction — independent confirmation of that selection.
- **AI-44:** Breadth-first adapters cannot start a flywheel; only end-to-end completion generates the failure signal that hardens them.

### ⚠️ Contradictions
| # | Contradiction | Resolution |
|---|---|---|
| C-28 | JARVIS's 160-adapter strategy ↔ R6 requires depth-first | 🔵 Code wins: the repo's own audit says 149 are fabricated. **Strategy should change, and the repo already knows it** (resolution gate is the admission) |

### ❓ Unknowns
1. How many completed actions are needed before R5 delegation measurably increases? No data.
2. Does R4 (subscription trap) also apply to B2B operational software? Untested — the corpus is consumer-weighted.
3. What is the actual liability exposure of an operational error (wrong bed assignment)? Unquantified (G-6.2).

### 📒 Decision Ledger
| ID | Decision | Rationale | Reversible? |
|---|---|---|---|
| DL-050 | **R5 (trust compounding) is designated the core Ovexis loop.** All product decisions evaluated against whether they feed it | Only virtuous loop reachable at low cost; JARVIS already has the entry point | No |
| DL-051 | **Depth-first adapters mandated.** No new adapter unless it completes a workflow end-to-end | R6/AI-44; 149 fabricated adapters produced zero flywheel | No |
| DL-052 | **Leverage is in sequencing and positioning, not volume of build** — top 3 leverage points need almost no new code | F-8.4 + DL-007 solo constraint | No |

### 📊 Confidence
| Dimension | Score |
|---|---|
| Loop identification | **MEDIUM-HIGH** — grounded in prior phases' measured findings |
| R1 commit-gap loop | **HIGH** — 4 independent confirmations |
| Leverage ranking | **MEDIUM** — reasoned, not measured |
| **Overall Phase 8** | **MEDIUM-HIGH** |

---

## PHASE 8 COMPLETE

**The three things that change:** (1) The commit gap is self-sealing — it structurally prevents the data that would close it. (2) Honest failure is the entry condition to the only virtuous loop available, and JARVIS already has it. (3) The top three leverage points cost almost nothing to pull — the constraint is sequencing, not engineering.

Proceeding to Phase 9.
