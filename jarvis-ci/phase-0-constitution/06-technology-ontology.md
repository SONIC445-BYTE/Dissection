# Technology Ontology
`v1.0.0` · Phase 0

Technologies are analysed separately from companies (Phase 4) because **capabilities outlive vendors**. A vendor dies; the capability re-homes.

---

## 1. Capability tree

```
AGENT CAPABILITY
├── PERCEIVE
│   ├── Screen understanding      (screenshot → semantic model)
│   ├── DOM/accessibility parsing (structured UI tree)
│   ├── OCR                       (pixels → text; incl. Indic scripts, handwriting)
│   ├── Document understanding    (layout, tables, forms, medical reports)
│   ├── Speech recognition        (STT, diarisation, code-switching)
│   └── Computer vision           (objects, medical imaging)
├── REASON
│   ├── Language understanding
│   ├── Chain/tree reasoning
│   ├── Test-time compute scaling
│   ├── Structured output
│   ├── Confidence estimation      ← chronically underserved
│   └── Domain reasoning           (clinical, legal, financial)
├── REMEMBER
│   ├── Working context            (window management, compaction)
│   ├── Episodic memory            (what happened, when)
│   ├── Semantic memory            (extracted facts)
│   ├── Procedural memory          (learned how-to)  ← chronically underserved
│   ├── Temporal validity          (what was true when; invalidation)
│   ├── Consolidation & forgetting ← THE unsolved problem
│   └── Retrieval                  (vector, graph, hybrid, agentic)
├── PLAN
│   ├── Task decomposition
│   ├── Control flow               (DAG, state machine, loop)
│   ├── Tool selection
│   ├── Error recovery & replanning ← chronically underserved
│   ├── Multi-agent coordination
│   └── Long-horizon execution
├── ACT
│   ├── API invocation
│   ├── Browser automation
│   ├── Desktop UI automation
│   ├── File/OS operations
│   ├── Code execution
│   └── Speech synthesis
└── GOVERN
    ├── Permissions & scoping
    ├── Human-in-the-loop checkpoints  ← non-negotiable in clinical contexts
    ├── Audit trail & provenance
    ├── Safety guardrails
    ├── Prompt-injection defence      ← rising fast with MCP surface area
    ├── Evaluation & regression
    └── Privacy / data residency
```

---

## 2. Commodity vs moat classification

The most consequential judgement in the entire framework. For each capability, classify:

| Class | Definition | Investment posture |
|---|---|---|
| **COMMODITY NOW** | Free/near-free, multiple good options | Integrate. Never build. |
| **COMMODITISING** | Paid today, free within ~24 months | Integrate, avoid deep coupling, do not differentiate here |
| **CONTESTED** | Genuinely unsettled; no winner | **Where differentiation is possible today** |
| **DURABLE MOAT** | Compounds with data/workflow/regulation | **Where to invest for the long term** |
| **STRUCTURAL** | Requires capital/scale JARVIS won't have | Depend on it. Never contest. |

### Working classification (to be validated in Phase 4, not assumed)

| Capability | Class | Reasoning |
|---|---|---|
| Speech recognition | COMMODITY NOW | Multiple free high-quality open models |
| Speech synthesis | COMMODITISING | Quality gap closing; price collapsing |
| Browser automation | COMMODITY NOW | Mature free drivers; rebuilding is self-harm |
| Basic OCR | COMMODITY NOW | Free engines adequate for clean text |
| **Indic/handwritten medical OCR** | **CONTESTED** | Prescriptions, regional scripts — genuinely hard, genuinely valuable in India |
| Vector retrieval | COMMODITY NOW | Many engines; embeddings near-free |
| Model inference | COMMODITISING | Runtimes converged on a shared engine lineage |
| Frontier model capability | STRUCTURAL | Requires capital JARVIS will not have |
| Task decomposition | CONTESTED | Every framework does it differently; none has won |
| **Error recovery / replanning** | **CONTESTED — underserved** | Demos skip it; production dies without it |
| **Temporal memory validity** | **CONTESTED** | Active research frontier; benchmarks disputed |
| **Memory consolidation / forgetting** | **CONTESTED — the real gap** | Universally acknowledged unsolved |
| **Procedural memory** | **CONTESTED — underserved** | Agents rarely learn *how*, only *what* |
| **Confidence estimation** | **CONTESTED — underserved** | Agents are confidently wrong by default |
| **Workflow-specific memory** | **DURABLE MOAT** | Compounds with usage in a specific domain |
| **Clinical workflow encoding** | **DURABLE MOAT** | Requires domain access competitors lack |
| **Regulatory compliance posture** | **DURABLE MOAT** | Slow, expensive, boring, defensible |
| Human-in-the-loop design | CONTESTED | Everyone claims it; few design it well |
| Prompt-injection defence | CONTESTED | Attack surface growing faster than defences |
| Audit trail / provenance | CONTESTED → moat in regulated markets | Cheap to build, hard to retrofit |

**Pattern:** the underserved capabilities cluster in **error recovery, forgetting, procedural learning, and confidence** — the unglamorous parts that determine whether an agent survives contact with production. Demos never show them, so vendors underinvest, so they stay contested longer than they should. This clustering is a strategic opportunity and should be tested hard in Phase 4.

---

## 3. Per-technology assessment template (Phase 4)

For each technology: definition & scope · maturity (S0–S4) · leading implementations · **benchmark landscape + saturation status** · open vs proprietary · cost curve & direction · integration difficulty · failure modes in production · commodity/moat class · **JARVIS posture** · what would change the assessment.

---

## 4. Benchmark discipline

**4.1** Vendor-reported = E2 about the *claim*, not E1 about *capability*.
**4.2** Record methodology, model used, date, and who ran it.
**4.3** **Note saturation.** When implementations cluster near the top, the benchmark has stopped discriminating and a high score means "competent", not "best."
**4.4** Record contests in full, with each disputed figure and its claimant.
**4.5** Prefer **task-level production metrics** over leaderboards: success rate on *your* workflows, cost per completed task, recovery rate after failure, human intervention rate.
**4.6** Benchmarks measure what is easy to measure. The capabilities that matter most in production — recovery, forgetting, calibration — are the least benchmarked. Absence of a benchmark is not absence of importance; frequently it is the opposite.
