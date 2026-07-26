# PHASE 10 — ENGINEERING LAWS
## How Healthcare Software Should Actually Be Built

**Phase:** 10 of 16 (+ Ω) · **Date:** 2026-07-26 · **Status:** COMPLETE — canonical
**Outputs:** `exports/phase10_engineering_laws.{json,yaml,csv}`

> **Sourcing note (DL-035).** Phase 5 established that this corpus is a go-to-market instrument: `bot_clinician_capacity` = 2 hits, `bot_integration_effort` = 14. It cannot supply engineering constraints. **These twelve laws are therefore derived from JARVIS code ground truth (🔵 Code-Backed) and prior-phase measured findings — not from the dossiers.**

Every law carries evidence, trade-offs, and failure cases as required.

### ENG01 — Protocol over platform

**Define the action contract first; let adapters satisfy it. Never let a platform-specific detail reach the planner.**

- **Evidence:** JARVIS base_adapter.py defines detect_ui/build_plan/verify_action_result as an abstract contract; the 149 fabricated adapters failed because they satisfied the SHAPE of the contract without the substance
- **Trade-off:** Contract rigidity slows one-off integrations
- **Failure case:** A contract too abstract to verify produces verify_action_result(): return True — exactly what 144/160 adapters did

### ENG02 — Verification over automation

**An action is not done until independently observed as done. No verification = no action.**

- **Evidence:** CB-06 144/160 adapters return True unconditionally; docs/adapter_audit.md: first step real, last step missing; ODAV loop already has a verify stage
- **Trade-off:** Verification can cost more than the action itself
- **Failure case:** Verifying the wrong signal (URL changed) instead of the outcome (message sent)

### ENG03 — Honest failure over silent success

**Report inability explicitly and specifically. Never no-op silently.**

- **Evidence:** resolution_gate.py: "I do not know how to control [platform] yet"; Phase8 R5 shows this is the entry condition to the only virtuous loop
- **Trade-off:** Surfaces incompleteness to users; feels worse in demos
- **Failure case:** Honest failure without a path forward becomes learned helplessness

### ENG04 — Policy over prompts

**Safety constraints belong in deterministic code, not in model instructions.**

- **Evidence:** JARVIS policy_manager.py 338 LOC + permission_engine.py 301 LOC + feature_gate modes; prompts cannot be audited or diffed
- **Trade-off:** Less flexible than natural-language policy
- **Failure case:** Policy engine that can be bypassed by the planner defeats its own purpose

### ENG05 — Adapters over replacements

**Integrate with the incumbent; never attempt to replace the system of record.**

- **Evidence:** LAW01 (incumbent lock-in GREEN 16 cos); Phase2 0/19 occupy SoR; B2 balancing loop
- **Trade-off:** Ceiling on capability set by the host system
- **Failure case:** Adapter coupling to an unstable UI creates permanent maintenance debt

### ENG06 — Graduated autonomy per action class

**Autonomy is granted per action type by reversibility and blast radius, never globally.**

- **Evidence:** feature_gate.py implements OFF/SHADOW/SUGGEST/FORCE; Phase7 F-7.5 human review is liability allocation; B1 loop
- **Trade-off:** Complex permission matrix
- **Failure case:** Uniform autonomy setting forces the whole system to the safety level of its riskiest action

### ENG07 — Local reasoning for PHI, cloud reasoning for general intelligence

**Split inference by data sensitivity, not by capability need.**

- **Evidence:** JARVIS local-first Ollama; Phase5 arch_on_device_local is the ONE non-converged architecture (7 cos); DPDP/HIPAA localisation pressure
- **Trade-off:** Local models are weaker; hybrid routing adds complexity
- **Failure case:** memory_store.py XOR encryption shows local != secure (CB-08)

### ENG08 — Depth-first over breadth-first

**One workflow completed end-to-end beats one hundred declared.**

- **Evidence:** CB-04 3 real/8 defective/149 fabricated; Phase8 R6 flywheel requires completion to generate failure signal
- **Trade-off:** Slower apparent coverage; worse for marketing
- **Failure case:** Depth in the wrong workflow wastes the entire budget

### ENG09 — State must live in the system, not in the human

**If a workflow requires a human to remember it, the software has failed.**

- **Evidence:** Phase6: bed state "lives in whiteboards and phone calls"; Phase4 break rate 1.00 in ICU/ED/admin
- **Trade-off:** Requires durable state model and reconciliation
- **Failure case:** System state diverging from reality is worse than no state

### ENG10 — Provenance is a first-class output

**Every action emits an auditable record of what, why, on whose authority, with what evidence.**

- **Evidence:** audit_log.py 307 LOC + execution_logger.py 225; LAW07 trust via traceability; Phase7 F-7.4 strengthens under autonomy
- **Trade-off:** Storage and performance overhead
- **Failure case:** Logs nobody can query are compliance theatre

### ENG11 — The orphaned-module rule: unreachable code is not capability

**A module nothing imports does not exist. Measure reachability, not lines.**

- **Evidence:** CB-09 MemoryStore orphaned - imported only by feedback_engine/optimizer which nothing imports; 10515 LOC across 13 concepts but reachability unverified (G-3.4)
- **Trade-off:** Reachability analysis is extra work
- **Failure case:** Counting orphaned LOC as progress - the exact error both G01 panels made

### ENG12 — Merge before you build

**Unmerged work is negative value: it decays, conflicts, and hides the true baseline.**

- **Evidence:** CB-02 9713 unmerged lines on phase-2-adapter-wiring; default branch = README cosmetics with 7 passing tests vs 325 on the branch
- **Trade-off:** Merging costs time that feels unproductive
- **Failure case:** Merging without CI reproduces the same divergence next cycle

---

## THE THREE LAWS THAT MOST INDICT THE CURRENT REPOSITORY

**ENG11 (orphaned-module rule)** is the most uncomfortable. JARVIS has ~10,515 LOC across 13 genome concepts, but `MemoryStore` — 315 of those lines — is imported only by `feedback_engine` and `optimizer`, which **nothing imports** (CB-09). Reachability across the rest is unverified (G-3.4). Both G01 due-diligence panels counted lines; neither measured reachability. *Counting orphaned LOC as progress is the exact error to avoid in Phase 11.*

**ENG12 (merge before you build)** is the cheapest high-value action available. 9,713 lines sit unmerged on `phase-2-adapter-wiring` with 325 passing tests, while the default branch is a README-cosmetics branch with 7. Every day unmerged increases divergence cost and hides the true baseline.

**ENG08 (depth-first)** directly contradicts the repository's existing strategy. 160 adapters, 149 fabricated, zero flywheel (Phase 8 R6). The repo already knows this — `docs/adapter_audit.md` and `resolution_gate.py` are the admission. The strategy has not yet caught up with the diagnosis.

---

## DELIVERABLES

**🟢/🔵 Verified:** 12 laws, 8 directly code-backed against the canonical branch, 4 derived from measured prior-phase findings.

**⚠️ Contradiction C-30:** ENG07 recommends local reasoning for PHI ↔ JARVIS's local store uses base64(XOR) with a hardcoded key (CB-08). **Resolution:** local ≠ secure. ENG07 is a *routing* principle; it does not imply the current local implementation is safe. Fixing `memory_store.py` is a precondition for any PHI handling.

**❓ Unknowns:** (1) What fraction of the 10,515 LOC is actually reachable? Unmeasured — first Phase-11 task. (2) Do the 12 wired adapters work on real Windows hardware? No test environment (G-1.1). (3) What is local-model latency/cost for clinical text? No data (G-1.5).

**📒 Decision Ledger:**

| ID | Decision | Reversible? |
|---|---|---|
| DL-054 | **ENG01–ENG12 are binding on Phase 11 architecture.** Any component violating a law must be redesigned or the exception justified | No |
| DL-055 | **Reachability analysis precedes all new development.** No LOC counts as capability until proven reachable | No |
| DL-056 | **Merge `phase-2-adapter-wiring` and add CI before any new feature work** — ENG12, zero cost, immediate compounding | No |

**📊 Confidence — Phase 10: HIGH** for code-backed laws (ENG01–04, 06, 08, 10–12); **MEDIUM-HIGH** for derived laws (ENG05, 07, 09).

---

## PHASE 10 COMPLETE — proceeding to Phase 11.
