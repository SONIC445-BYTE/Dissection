# PHASE 11 — JARVIS IMPLICATIONS
## Translating Everything Into Engineering

**Phase:** 11 of 16 (+ Ω) · **Date:** 2026-07-26 · **Status:** COMPLETE — canonical
**Outputs:** `exports/phase11_jarvis_architecture.{json,yaml,csv}`, `registry/phase11_reachability.json`

> This is the phase the engagement objective (Q2) exists for. Every recommendation below is bound by the twelve engineering laws (DL-054) and the solo-builder constraint (DL-007).

---

## 11.0 THE REACHABILITY AUDIT — ENG11 APPLIED

Before designing anything, ENG11/DL-055 required proving what actually runs. I built the import graph from real entrypoints (`jarvis`, `jarvis_launcher`, `co_brain`, `onboarding`, `daemon.*`) on the canonical branch:

| Metric | Value |
|---|---|
| Production modules | 602 |
| **Reachable from entrypoints** | **147 (24%)** |
| **Orphaned** | **455 (76%)** |
| Reachable LOC | 20,171 |
| **Orphaned LOC** | **18,558** |

### F-11.1 — The entire safety stack is orphaned

Verified twice — once by graph traversal, once by direct import grep:

| Module | LOC | Non-test importers | Status |
|---|---|---|---|
| `policy_manager` | 338 | **0** | 🔴 ORPHANED |
| `session_memory` | 113 | **0** | 🔴 ORPHANED |
| `permission_engine` | 301 | 1 (only `policy_manager`, itself orphaned) | 🔴 ORPHANED |
| `audit_log` | 307 | 3 (all themselves orphaned) | 🔴 ORPHANED |
| `memory_store` | 315 | 3 (orphaned chain, CB-09) | 🔴 ORPHANED |
| `task_graph` | 338 | 2 (orphaned) | 🔴 ORPHANED |

**JARVIS has a policy engine, a permission engine, an audit log and a memory store — and none of them execute.** They form a mutually-importing island disconnected from the running system.

This is the most consequential engineering finding in the engagement, and it inverts a Phase-3 conclusion. Phase 3 counted 10,515 LOC across 13 genome concepts and called it an accidental strategic asset. **Reachability analysis shows the safety-relevant portion of that asset does not run.** Preserved and corrected per protocol, not silently amended.

It also indicts both G01 due-diligence panels and my own earlier phases: everyone counted lines. Nobody measured reachability. *Safety code that never executes is worse than absent code, because it creates false confidence.*

---

## 11.1 THE TWENTY-LAYER ARCHITECTURE

Status: **6 reachable · 7 partial · 4 orphaned · 3 absent.**

| # | Layer | Status | Action | Why |
|---|---|---|---|---|
| 01 | Core Architecture | PARTIAL (agent_brain 487 + odav_loop 355 REACHABLE) | **Keep. This is the asset.** | ODAV is already the R1-breaking shape: it verifies, which is what generates ou |
| 02 | Agent Architecture | PARTIAL (task_planner 352 REACH, task_graph 338 ORPH | **Wire task_graph or delete it** | Multi-agent adds coordination failure modes a solo builder cannot debug |
| 03 | Policy Engine | ORPHANED (policy_manager 338 + permission_engine 301 | **WIRE IMMEDIATELY - highest priority** | Safety code that never executes is worse than none: it creates false confidenc |
| 04 | Adapter Framework | REACHABLE (command_router 347, resolution_gate 174,  | **Freeze at 14 wired; delete or quarantine the** | 149 fabricated adapters produce no flywheel and poison the catalog |
| 05 | Workflow Engine | ABSENT (task_graph orphaned; no persistence) | **BUILD - this is protocol_commitment (Phase3 ** | State must live in the system; every Tier-1 opportunity is a state problem |
| 06 | Knowledge Graph | ABSENT | **BUILD after workflow engine** | Phase7 AN05; cross-departmental state nobody aggregates |
| 07 | Memory System | ORPHANED + INSECURE (memory_store 315, XOR hardcoded | **Wire session_memory; replace XOR with AES-GC** | CB-08: local != secure |
| 08 | Conversation Engine | REACHABLE (conversation_loop, turn_manager, command_ | **Keep** | Already handles pending/resume - the substrate for human confirmation |
| 09 | Verification Engine | REACHABLE (validation_engine 286) but 144/160 adapte | **Make verify_action_result non-optional; fail** | Unverified action = no action (LAW02) |
| 10 | Safety Layer | PARTIAL (feature_gate 39 REACH; modes exist but glob | **Extend to per-action-class** | B1 loop: uniform autonomy forces system to riskiest action safety level |
| 11 | Observability | ORPHANED (audit_log 307, 3 importers all themselves  | **WIRE - second priority after policy** | Provenance is product (LAW07); required for R5 trust loop |
| 12 | Integration Layer | ABSENT (zero healthcare code, all branches CB-07) | **BUILD - ABDM sandbox first** | LAW12: counterparty network already exists (38 NHCX partners) |
| 13 | Vision Layer | PARTIAL (ui_perception 342, element_selector 259 REA | **Keep; retarget from consumer apps to HMIS sc** | LAW05/DL-046: internal ops are permanently API-poor |
| 14 | Voice Layer | PARTIAL (local_stt 213, listen 76, TTS 73) | **Defer** | Phase7 AN04 nursing capture is Tier-3; not the beachhead |
| 15 | Reasoning Layer | PARTIAL (llm_engine 309 via subprocess curl to Ollam | **Replace subprocess curl with a proper client** | Fragile transport for the systems core dependency |
| 16 | Planner | REACHABLE (task_planner 352, intent_router) | **Keep** | Works; contract is sound |
| 17 | Execution Layer | REACHABLE (ui_executor 567, action_executor) | **Keep; enforce dry-run default in clinical co** | Largest single asset; 1747 LOC of the markets thinnest layer |
| 18 | Validation Layer | REACHABLE (validation_engine 286) | **Keep; extend to workflow-level invariants** | Step validation exists; workflow validation does not |
| 19 | Audit Layer | ORPHANED (audit_log 307) | **Wire + make append-only** | Mutable audit is not audit |
| 20 | Deployment | PARTIAL (daemon, installers, pyproject on branch) | **Merge branch; add CI** | ENG12: 9713 lines unmerged, 325 vs 7 passing tests |

---

## 11.2 WHY, NOT ONLY WHAT

**Why keep the ODAV loop (L01).** It is the only structure in the codebase that breaks Phase-8's R1 self-sealing loop. ODAV *verifies*, and verification is what produces the outcome data the entire market fails to generate (LAW02). This is JARVIS's single most valuable inheritance.

**Why wire policy first (L03).** Not for compliance — for R5. The trust-compounding loop cannot start while the constraint system is decorative. Every action executed without a policy check is an action that cannot later be defended, which caps delegation permanently (B1).

**Why freeze adapters at 14 (L04).** ENG08 + Phase-8 R6: the flywheel needs end-to-end completion to generate failure signal. 149 fabricated adapters generate none and actively poison the catalog by making `resolution_gate` reason about platforms that will never work.

**Why build the workflow engine (L05).** It *is* `protocol_commitment` — Phase 3's highest-value concept (SI 9.6, highest user value in the genome, built by only 6 of 17). And every Phase-6 Tier-1 opportunity — OT turnover, bed flow, rostering, claim chains — is fundamentally a durable-state problem (ENG09).

**Why ABDM/NHAX before anything US (L12).** LAW12: the counterparty network already exists — 38 NHCX partners including 12 insurers and 4 TPAs, verified live. In the US that network must be bought.

**Why retarget vision at HMIS screens (L13).** LAW05/DL-046: 409 of 449 platforms are FHIR-certified, yet FHIR covers zero internal operations. The screen is the only universal interface to intra-institutional work, permanently.

---

## 11.3 THE SEQUENCED PLAN FOR ONE PERSON

Ordered by leverage-per-effort under DL-007, DL-052 and the engineering laws.

**Stage 0 — Recover the baseline (days, near-zero cost)**

1. Merge `phase-2-adapter-wiring` → `main`; make `main` default *(ENG12, DL-056)*
2. Add CI running the 325-test suite on every push
3. Wire `policy_manager` + `permission_engine` into the execution path, or delete them *(ENG04, F-11.1)*
4. Wire `audit_log` as append-only *(ENG10)*
5. Replace `memory_store` XOR with AES-GCM *(ENG07, CB-08)*
6. Quarantine the 149 fabricated adapters *(ENG08)*

> Nothing here is new capability. All of it is converting existing code from decorative to load-bearing. This is the highest-return work available and it is invisible on a demo.

**Stage 1 — One workflow, end to end (the flywheel start)**

7. Build the durable workflow engine (`protocol_commitment`) *(ENG09)*
8. Extend `feature_gate` to per-action-class autonomy *(ENG06)*
9. Make `verify_action_result` mandatory and fail-closed *(ENG02)*
10. Pick **one** Phase-6 Tier-1 workflow — OT turnover or claim validation — and complete it end-to-end for **one** hospital *(ENG08, R6)*

**Stage 2 — Attach to the rail**

11. ABDM sandbox client (M1/M2/M3)
12. NHCX claims client
13. Institutional knowledge graph *(AN05)*

---

## 11.4 DELIVERABLES

### 🔵 Code-Backed Facts
| # | Fact |
|---|---|
| CB-15 | 602 production modules; **147 reachable (24%)**, 455 orphaned (76%) |
| CB-16 | Reachable 20,171 LOC vs orphaned **18,558 LOC** |
| CB-17 | `policy_manager` (338 LOC) and `session_memory` (113 LOC) have **zero non-test importers** |
| CB-18 | `permission_engine`, `audit_log`, `memory_store`, `task_graph` form an orphaned mutually-importing island |
| CB-19 | Reachable and load-bearing: `agent_brain` 487, `odav_loop` 355, `ui_executor` 567, `command_router` 347, `resolution_gate` 174, `validation_engine` 286, `task_planner` 352 |

### ⚠️ Contradictions
| # | Contradiction | Resolution |
|---|---|---|
| C-31 | Phase 3 called 10,515 LOC an accidental strategic asset ↔ 76% of production code is unreachable | **Both true, precisely.** The *execution* stack (ui_executor, command_router, odav_loop, validation_engine) is reachable and genuinely valuable. The *safety* stack is orphaned. Phase 3's conclusion holds for the asset; F-11.1 corrects its scope |
| C-32 | Repo markets itself as privacy-first with policy and audit ↔ both are orphaned | 🔵 Code wins. Marketing describes unwired subsystems (extends C-09) |

### ❓ Unknowns
1. Do the 12 wired adapters work on real Windows hardware? Still no test environment (G-1.1).
2. Local-model latency and cost for clinical text — still unmeasured (G-1.5).
3. Is the orphaned code *abandoned* or *staged for wiring*? Determines delete-vs-wire for ~18,558 LOC.
4. Solo-builder velocity: Stage 0 has no credible time estimate (G-3.3).

### 📒 Decision Ledger
| ID | Decision | Reversible? |
|---|---|---|
| DL-057 | **Stage 0 (wire the safety stack) precedes all feature work.** Orphaned policy/audit/permission is a false-confidence hazard | No |
| DL-058 | **Freeze adapters at 14 wired; quarantine 149 fabricated** | Yes |
| DL-059 | **Workflow engine (`protocol_commitment`) is the single most valuable thing to build** — Phase-3 top concept and the substrate for every Tier-1 opportunity | No |
| DL-060 | **One workflow, one hospital, end-to-end before any second workflow** (ENG08, R6 flywheel) | No |

### 📊 Confidence
| Dimension | Score |
|---|---|
| Reachability audit | **HIGH** — graph traversal + direct grep, two methods agree |
| Layer status assessment | **HIGH** — code-backed |
| Sequencing | **MEDIUM-HIGH** — reasoned from laws + loops; no velocity data |
| Effort estimates | **NOT PROVIDED** — no solo-builder model exists (G-3.3); ordinal sequence only |
| **Overall Phase 11** | **HIGH** for diagnosis, **MEDIUM-HIGH** for plan |

---

## PHASE 11 COMPLETE

**The three things that change:** (1) 76% of production code is unreachable and *the entire safety stack is orphaned* — policy, permissions, audit and memory are real code that never runs. (2) The valuable inheritance is narrower than Phase 3 suggested but real: the execution stack is reachable and it is the market's thinnest layer. (3) The highest-return work is invisible — wiring, merging, CI — not new features.

Proceeding to Phase 12.
