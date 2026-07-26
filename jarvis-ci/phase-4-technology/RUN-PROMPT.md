# Phase 4 — Technology Intelligence Run Prompt
`v1.0.0` · 🔒 **Requires AUDIT-PASSED** · One technology per run

---

## Shift of unit

Phase 3 asked *"how does this layer work?"* Phase 4 asks **"how good is this capability, really?"**

**Capabilities outlive vendors.** A vendor dies; the capability re-homes. Analysing technologies separately from companies is what makes the knowledge base durable.

## Context

✅ Phase 0 constitution · Phase 2 dossiers · Phase 3 layer reports
✅ `06-technology-ontology.md` — the capability tree and commodity/moat table
⚠ `08-jarvis-architecture-baseline.md` capability list only — **may check "do we have this?", may not shape the benchmark**
❌ JARVIS repo / dissection / blueprint

> The isolation caveat matters here specifically. If you benchmark a capability while looking at your own implementation, you will unconsciously choose criteria your implementation satisfies.

---

## Deliverable: `TECH-{{NAME}}.md`

### 1. Definition and scope
What exactly is this capability? What is adjacent but excluded?

### 2. Maturity (S0–S4) with justification

### 3. Implementation landscape
| Implementation | Type | Maturity | Approach | Cost | Notes |
|---|---|---|---|---|---|

### 4. Benchmark landscape
What exists · what it measures · **saturation status** · contested figures with claimants · methodology critiques.

**And critically: what is not benchmarked, and why.**

### 5. Production reality ⭐
Where benchmarks and production diverge. Failure modes under real load. What breaks that demos never show.

Prefer task-level production metrics over leaderboards: success rate on real workflows · cost per completed task · **recovery rate after failure** · human intervention rate.

### 6. Cost curve
Current cost, direction of travel, and what drives it. Is this heading toward free?

### 7. Commodity / moat classification
Assign one: `COMMODITY NOW` · `COMMODITISING` · `CONTESTED` · `DURABLE MOAT` · `STRUCTURAL`.

**Validate or overturn the working classification in `06-technology-ontology.md` §2.** That table was written from priors. This is where it gets tested against evidence. Overturning it is a valuable result, not a failure.

### 8. Integration difficulty
Effort to adopt · abstraction cost · lock-in risk · replaceability.

### 9. JARVIS posture
Build · integrate · abstract · ignore — with reasoning tied to the classification.

### 10. What would change this assessment
Name the specific developments that would move the classification.

---

## Technologies to run

**Priority 1 — the contested-underserved cluster**
`Memory consolidation & forgetting` · `Temporal validity` · `Procedural memory` · `Error recovery & replanning` · `Confidence estimation & calibration`

> These five clustered as CONTESTED-underserved in the ontology because demos skip them and vendors underinvest. If that clustering survives evidence, it is the strategic core of Phase 7. If it doesn't, the whole differentiation thesis needs rework. **Run these first.**

**Priority 1 — healthcare-specific**
`Indic/handwritten medical OCR` · `Clinical document understanding`

**Priority 2**
`Local inference` · `RAG` · `Knowledge graphs` · `Vector retrieval` · `Speech recognition` · `Speech synthesis` · `Browser automation` · `Desktop UI automation` · `Prompt-injection defence` · `Audit trail & provenance`

**Priority 3**
`Computer vision` · `Structured output` · `Multi-agent coordination` · `Test-time compute scaling`

---

## Exit criteria
- [ ] All priority-1 technologies assessed
- [ ] Every ontology §2 classification validated or overturned with evidence
- [ ] Benchmark saturation documented per technology
- [ ] Production-reality section grounded in real failure evidence, not vendor claims
- [ ] JARVIS posture stated for each
