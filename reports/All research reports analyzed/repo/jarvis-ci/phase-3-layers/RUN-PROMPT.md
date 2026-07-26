# Phase 3 — Layer Intelligence Run Prompt
`v1.0.0` · 🔒 **Requires AUDIT-PASSED** · One layer per run

---

## Shift of unit

Phase 2 asked *"what is this company?"* Phase 3 asks **"how does this layer work?"**

Companies come and go. Layers persist. A layer report should stay useful after half its named players are acquired or dead.

## Context

✅ All Phase 0 constitution documents
✅ **All Phase 2 dossiers for companies in this layer** — cross-company comparison is now *permitted and required*
✅ `phase-2.5-audit/contradiction-ledger.md` — resolve conflicts deliberately here
✅ `08-jarvis-architecture-baseline.md` §2 layer posture table only
❌ JARVIS repo / dissection / blueprint (`09-repo-context-isolation.md`)

> Phase 3 may compare companies. That prohibition applied to Phase 2 only, and it was lifted by the audit passing.

---

## Deliverable: `LAYER-{{N}}-{{NAME}}.md`

### 1. Layer definition
What value is captured here? Where does this layer begin and end? What is *not* in it?

### 2. Player map
Every registered company in this layer, with dossier cross-references.

| Company | Stage | D1 | Threat | Partnership | Role | One-line position |
|---|---|---|---|---|---|---|

### 3. Architectural divergence ⭐ the core of the report
**How do implementations actually differ?** Not feature tables — *architectural bets*.

For each distinct approach: the bet being made, what it optimises, what it sacrifices, and which workloads expose the sacrifice.

> Feature comparison is what everyone does and it ages in weeks. Architectural divergence explains *why* the features differ and stays true for years.

### 4. Convergence and divergence
- What has the layer **converged** on? (Convergence = commoditisation. Anything converged is no longer differentiating.)
- Where does it still **diverge**? (Divergence = the contested ground.)
- What was tried and **abandoned**? Deprecations are the honest signal.

### 5. Benchmark landscape
Which benchmarks exist · what they actually measure · saturation status · contested figures with claimants · **what is NOT benchmarked**.

> The unbenchmarked capabilities are often the ones that decide production outcomes. Absence of a benchmark is not absence of importance — frequently it is the opposite.

### 6. Layer economics
Capital intensity · commoditisation velocity · switching costs · standardisation exposure · distribution dependence · data compounding. Verdict: **is this a good layer to own?**

### 7. Negative space ⭐
What does **no one** in this layer do? Is it (a) not real, (b) not yet valuable, or (c) the opportunity?

Answer with evidence from the dossiers, not speculation.

### 8. Standards exposure
Which L11 standards constrain this layer? Has a standards wave already erased differentiators here?

### 9. JARVIS posture
Confirm or revise the baseline posture. If revising, state the trigger and log a Decision Ledger entry.

Then: what must JARVIS build, integrate, abstract, or refuse **in this layer specifically**?

### 10. Contradiction resolution
Every conflict from the ledger touching this layer — resolved with reasoning, or marked genuinely irresolvable.

---

## Layers to run

| Layer | Priority | Why |
|---|---|---|
| **L3 Memory** | 1 | Contested core; OQ-01 lives here |
| **L4 Planning** | 1 | Contested core |
| L10 Healthcare Platforms | 1 | Differentiated market |
| L11 Healthcare Standards | 1 | Constrains all adapters |
| L5 Perception | 2 | OCR gap; Indic scripts |
| L6 Execution | 2 | Confirm commodity thesis |
| L7 Voice | 2 | Confirm commoditisation velocity |
| L8 OS AI | 2 | Existential distribution risk |
| L1, L2 | 2 | Dependency risk assessment |
| L0, L9, L12, L13, L14 | 3 | Context |
| **L15 Frontier** | 1 | The three unclaimed slots |

---

## Exit criteria
- [ ] Every layer with ≥2 registered companies has a report
- [ ] Architectural divergence documented, not feature-compared
- [ ] Negative space answered with evidence
- [ ] Every baseline posture confirmed or revised with a trigger
- [ ] All layer-relevant contradictions resolved
