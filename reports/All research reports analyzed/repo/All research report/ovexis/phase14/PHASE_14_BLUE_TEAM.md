# PHASE 14 — BLUE TEAM
## Defending Only What Survived

**Phase:** 14 of 16 (+ Ω) · **Date:** 2026-07-26 · **Status:** COMPLETE — canonical
**Outputs:** `exports/phase14_blueteam.{json,yaml,csv}`

**4 fully survive · 2 conditional · 2 strengthened or reframed by attack · 1 replaced · 4 abandoned.**

---

## 14.1 THE SURVIVING RECOMMENDATIONS


### BT01 — Stage 0: wire the safety stack, merge the branch, add CI

**Status: FULLY SURVIVES** · Confidence: HIGH

Not attacked by any red-team vector. Zero capital, zero market risk, pure downside removal. Value is independent of whether the beachhead thesis holds.

*Conditions:* None

### BT02 — Operational scope only, no clinical decisions for 24 months

**Status: FULLY SURVIVES** · Confidence: HIGH

RT08 attacked the commit-gap thesis and in surviving RESTRICTED it to exactly this scope. RT07 attacked it as unambitious; LAW04 shows clinical entry is unsafe for a solo builder. Two independent attacks converged on confirming it.

*Conditions:* None

### BT03 — JARVIS as technical foundation, with Stage 0 mandatory

**Status: SURVIVES CONDITIONALLY** · Confidence: MEDIUM-HIGH

RT05 correctly notes 76% unreachable and orphaned safety. But the REACHABLE execution stack (ui_executor 567, odav_loop 355, command_router 347, resolution_gate 174, validation_engine 286) is the exact capability the market lacks and is genuinely hard to rebuild.

*Conditions:* Stage 0 completed first; XOR replaced before any PHI

### BT04 — SHADOW-mode entry into every hospital

**Status: STRENGTHENED BY ATTACK** · Confidence: HIGH

Emerged as the defence to the highest-severity threat (CIO rejection). Simultaneously the R5 trust-loop entry condition and the procurement objection handler. Already implemented in feature_gate.

*Conditions:* None

### BT05 — India-first sequencing

**Status: SURVIVES ON STRUCTURE, UNVALIDATED ON ECONOMICS** · Confidence: MEDIUM

LAW11 (fragmentation favours interface layer) and LAW12 (NHCX network verified live: 38 partners, 12 insurers, 4 TPAs) are strong. It is also the structural defence against Epic (NICHE tier in India).

*Conditions:* RT06 unit economics must be validated with one real hospital before scaling

### BT06 — Depth-first adapters, freeze at 14, quarantine 149

**Status: FULLY SURVIVES** · Confidence: HIGH

Code-backed (CB-04) and loop-backed (R6). The repository already reached this conclusion independently in its own adapter_audit.md. No attack contests it.

*Conditions:* None

### BT07 — Moat = domain adapters + policy + provenance (NOT automation)

**Status: REFRAMED BY ATTACK, NOW STRONGER** · Confidence: MEDIUM

RT02 correctly showed coverage alone is not defensible and OpenAI commoditises clicking. The reframe to domain+policy+provenance is more defensible than the original and aligns with LAW07 and ENG10.

*Conditions:* Accept there is no moat for 12+ months

### BT08 — Beachhead: OT turnover / claim validation in Indian hospitals

**Status: CONDITIONALLY SURVIVES - EVIDENCE GATED** · Confidence: MEDIUM-LOW until evidence closes

Robust across all 5 weighting scenarios including one that deletes JARVIS-readiness. Break-rate evidence (1.00 in admin/ICU/ED) suggests that even where HMIS modules exist they do not connect.

*Conditions:* BLOCKED until 82 ABDM demo videos reviewed (DL-066). If modules exist and connect, pivot to the claim chain which has a verified external rail.

### BT09 — Flat pilot fee, outcome pricing later

**Status: REPLACED BY ATTACK** · Confidence: MEDIUM

RT04 correctly identified circular dependency. Flat pilot fee removes it. Weaker but executable.

*Conditions:* Outcome pricing only after measurement infrastructure exists

### BT10 — No hires until one workflow completes end-to-end

**Status: FULLY SURVIVES** · Confidence: HIGH

Unattacked. Consistent with DL-007 and with the pivotal unknown being domain knowledge rather than engineering capacity.

*Conditions:* None

---

## 14.2 WHAT WAS ABANDONED

A blue team that defends everything is worthless. These are dropped:

| Abandoned | Why |
|---|---|
| Per-completed-workflow pricing as the entry model | RT04 circular dependency: cannot measure before deploying, cannot deploy without price |
| "Unowned workflow" as the marketing claim | RT01: not evidenced. Claim must become "disconnected workflow" which IS evidenced by break rate 1.00 |
| Adapter coverage as the stated moat | RT02 + OpenAI commoditisation. Replaced by domain+policy+provenance |
| Inventing a new budget category | RT03: no CFO can code an invoice for a category that does not exist |

### The most important abandonment

**'Unowned workflow' must be replaced by 'disconnected workflow'.**

RT01 showed the unowned claim rests on marketing copy from two datasets. But Phase-4's break-rate measurement is a *different and stronger* finding: ICU, emergency, administration and management all score **1.00** — every adjacent handoff is a break.

That claim survives RT01 completely, because break rate measures *connection between stages*, not *existence of modules*. A hospital can own a bed-management module and a theatre module and still have no connection between them.

> The defensible claim is not 'nobody built this.' It is **'nothing connects these.'** That is what Ovexis sells against, and it is evidenced.

---

## 14.3 THE STRATEGY AFTER ADVERSARIAL REVIEW

Ovexis is an **operational execution agent** that enters Indian private hospitals in **SHADOW mode**, observing and recommending across the **disconnected** operational and financial workflows — theatre turnover, bed flow, claim validation — where break rate is 1.00 and no clinical judgement is required.

It charges a **flat pilot fee**. It attaches to an **existing budget line** (HMIS AMC uplift or claims-recovery percentage). It completes **one workflow end-to-end in one hospital** before anything else. Its moat is **domain adapters, healthcare policy and audit provenance** — never the automation itself, which OpenAI will commoditise.

Before any of this, it spends its first weeks on **Stage 0**: merging 9,713 unmerged lines, adding CI, and wiring a safety stack that currently does not execute.

**And it does not commit to the beachhead until the 82 ABDM demo videos are reviewed.**

---

## 14.4 DELIVERABLES

### 📒 Decision Ledger
| ID | Decision | Reversible? |
|---|---|---|
| DL-071 | **Claim changes from 'unowned' to 'disconnected'** — survives RT01, evidenced by break rate 1.00 | No |
| DL-072 | **BT01 (Stage 0) is unconditional and starts immediately** — no attack touched it, no evidence gate applies | No |
| DL-073 | **BT08 (beachhead) remains evidence-gated** — the only surviving recommendation that cannot begin | No |

### 📊 Confidence — Phase 14
| Recommendation class | Confidence |
|---|---|
| Stage 0 / engineering hygiene | **HIGH** — unattackable, zero-cost, independent of market thesis |
| Operational scope restriction | **HIGH** — confirmed by two independent attacks |
| Shadow-mode entry | **HIGH** — strengthened by attack |
| Depth-first adapters | **HIGH** — code-backed and self-confirmed by the repo |
| India-first structure | **MEDIUM** — structurally sound, economically unvalidated |
| Beachhead workflow choice | **MEDIUM-LOW** — evidence-gated |
| **Overall Phase 14** | **MEDIUM-HIGH**, with the highest-confidence items being the ones executable today |

---

## PHASE 14 COMPLETE

**The strategy that survived is smaller, more specific, and more defensible than the one that entered.** The highest-confidence recommendations are also the cheapest and most immediate: merge the branch, wire the safety stack, enter in shadow mode, complete one workflow. The most ambitious claim — an unowned beachhead — is the one blocked pending evidence.

Proceeding to Phase 15 (Board Memo).
