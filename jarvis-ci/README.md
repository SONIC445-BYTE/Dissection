# JARVIS Competitive Intelligence Knowledge Base

**A research pipeline, not a report.** One complete run per company → standardized dossier → quality audit gate → only then, synthesis.

> **Status:** Phases 0, R, 1, 2, 2.5 machinery **complete and tested**. Phases 3–Ω **built and locked**.
> 112 entities registered · 1 exemplar dossier ratified · 107 dossier runs remain.
> Constitution `v1.0.0` · Baseline `v0.2.0` (repo-grounded) · 2026-07-26

---

## 0. Why this exists

Most competitive research fails in four ways. This repo is engineered against all four:

| Failure mode | Where it comes from | Structural defence |
|---|---|---|
| **Context collapse** — company #17 gets 1/10th the depth of #1 | One giant prompt for all competitors | One isolated run per company. Depth variance measured by CV, gate blocks at >0.40. |
| **Inference laundering** — a guess becomes fact by repetition | No evidence discipline | 4 tiers, machine-linted. E3→E1 requires a new primary source ID. |
| **Competitor inflation** — everything is a "competitor" | No role taxonomy | 6 roles. "Direct Competitor" requires a 3-part contested-layer proof. Audit fails above 15%. |
| **Stage mismatch** — judging S0 work by S3 standards | No maturity normalisation | S0–S4 per product line. Criticism must be stage-adjusted. |

---

## 1. Pipeline

```
PHASE 0   Research Framework .................... run ONCE     ✅ COMPLETE
   │      Constitution · Taxonomy · Evidence Rules · Scoring
   │      Company/Healthcare/Technology Ontologies · Baseline · Isolation rule
   │
PHASE R   Repository Dissection ................. run ONCE     ✅ COMPLETE
   │      Capability Ledger · Architecture Map · Gap Register
   │      Blueprint Review     → feeds Phases 7/8/Ω ONLY
   ▼
PHASE 1   Company Discovery .................... continuous    ✅ COMPLETE
   │      112 entities · Direct Competitor share 6.5% (healthy)
   ▼
PHASE 2   Company Dossiers ..................... N runs        ⚙️ 1 / 108
   │      16 deliverables each · ⛔ NO CROSS-COMPANY CLAIMS
   ▼
PHASE 2.5 ⛔ RESEARCH QUALITY AUDIT — HARD GATE ...            🔒 LOCKED
   │      7 checks · synthesis FORBIDDEN until pass
   ▼
PHASE 3   Layer Intelligence ................... 16 runs       🔒 ready
PHASE 4   Technology Intelligence .............. ~20 runs      🔒 ready
PHASE 5   Healthcare Intelligence .............. ~25 runs      🔒 ready
PHASE 6   Cross-Company Synthesis .............. 1 run         🔒 ready
PHASE 7   JARVIS Opportunity Mapping ........... 1 run         🔒 ✅ repo unlocked
PHASE 8   Moat Engineering ..................... 1 run         🔒 ✅ repo unlocked
PHASE Ω   Master Strategy Bible ................ 1 run         🔒 ✅ repo unlocked
```

`[LOCKED]` is enforced by `tools/gate.py`, not by convention.

---

## 2. Repo-context isolation ⭐

The JARVIS repository, dissection, and blueprint are **strategy-layer inputs only**.

| Phase | Repo access | Why |
|---|---|---|
| 1 Discovery | ❌ | Must ask "who owns value here?", not "who resembles us?" |
| 2 Dossiers | ❌ | Scoring against your own code invites flattery and panic |
| 2.5 Audit | ❌ | Audits check research integrity, not strategic fit |
| 3/4/5 | ⚠️ partial | Layer map / capability list / workflow list only |
| 6 Synthesis | ❌ | Patterns must be found on their own terms or they're unfalsifiable |
| **7 / 8 / Ω** | ✅ **full** | Where repo reality meets clean ecosystem findings |

Machine-enforced: `validate.py` flags repo paths, module names, and commit SHAs in Phase 2 dossiers.

---

## 3. Quick start

```bash
python3 tools/registry.py                 # 112 entities, validated
python3 tools/status.py                   # progress + depth variance
python3 tools/gate.py --check phase-6     # BLOCKED until audit passes

python3 tools/new_company.py "Zep / Graphiti"
#  → open phase-2-dossiers/_TEMPLATE/RUN-PROMPT.md
#  → paste into a FRESH context window. One company per run.
python3 tools/validate.py Zep-Graphiti    # must exit 0
python3 tools/score.py Zep-Graphiti
python3 tools/audit.py                    # the hard gate
```

---

## 4. Map

```
jarvis-ci/
├── phase-0-constitution/          ← the law; everything inherits
│   ├── 00-research-constitution.md      11 articles, 12 prohibitions
│   ├── 01-canonical-taxonomy.md         L0–L15, value chain, Agent Core
│   ├── 02-evidence-rules.md             E1–E4, source hierarchy, lint rules
│   ├── 03-competitive-scoring-framework.md  10 dims → 4 indices
│   ├── 04-company-ontology.md           what a company record contains
│   ├── 05-healthcare-ontology.md        ABDM/FHIR + Indian clinical reality
│   ├── 06-technology-ontology.md        capability tree, commodity/moat
│   ├── 07-strategic-role-classification.md  6 roles + decision tree
│   ├── 08-jarvis-architecture-baseline.md   postures + theses T1–T4
│   └── 09-repo-context-isolation.md     ⭐ the isolation rule
├── phase-R-repo-dissection/       ← capability ledger, gaps, blueprint review
├── phase-1-discovery/             ← protocol + 112-entity registry + report
├── phase-2-dossiers/
│   ├── _TEMPLATE/                 ← RUN-PROMPT (the engine) + schemas
│   ├── Companies/Mem0/            ← ⭐ ratified exemplar
│   └── OPEN-QUESTIONS.md          ← the only cross-run channel
├── phase-2.5-audit/               ← 7 checks, anti-gaming, failure protocol
├── phase-3-layers/ … phase-omega/ ← run prompts + exit criteria, locked
└── tools/                         ← registry, new_company, validate, score,
                                      status, audit, gate
```

---

## 5. Non-negotiable rules

1. **One company per run.** No batching.
2. **No cross-company claims in Phase 2.** Comparison is Phase 3/6 work.
3. **Every claim carries an evidence tier.**
4. **README ≠ implementation.** E2 ceiling.
5. **Roadmap ≠ product.** State the shipping rung.
6. **Stage-adjusted criticism only.**
7. **RHINAL is never self-scored.** `self: true`, comparison only.
8. **Exactly one primary Strategic Role.**
9. **Inference never promotes to fact.**
10. **Every dossier ends with the 8 Final Reflection questions.**
11. **≥1 uncomfortable finding per dossier.** Intelligence that only reassures isn't intelligence.
12. **Never soften the audit.** Re-run deficient dossiers instead.

---

## 6. What the exemplar proved

`Companies/Mem0/` — 4,136 words, 44 claims, 10 sources, ratified.

Its most important output: the registry hypothesised Mem0 as a **Direct Competitor**; the three-part test **failed on buyer substitution** (Mem0 sells to developers; JARVIS serves clinicians — no buyer chooses between them), and it was demoted to **Technology Supplier**.

That demotion is the framework working. Overlap of *capability* is not overlap of *buyer*.

It also produced a split thesis verdict — **T1 weakened, T2 strengthened** — leading to a strategically consequential conclusion from a single dossier: *JARVIS's differentiation must come from the vertical, not the layer.*

---

## 7. Honest status

**1 of 108 dossiers ratified.** The engine is built, tested, and proven; the corpus is not. The remaining 107 are genuine research runs, each needing a fresh context window and real primary-source work.

The gate will correctly refuse synthesis until they exist. That is the design.

**Next action:** run tier-1 dossiers in registry order, starting with **Zep/Graphiti** — the most likely place to answer OQ-01, now the highest-priority open question in the knowledge base.

---

## 8. Extension: Strategic Intelligence Platform ⭐

The pipeline above is preserved intact. Layered beneath it is a **registry substrate**
that turns the repository from a batch pipeline into a continuously improving system.

**The structural change:** knowledge was indexed by *company* only, so answering
"who does memory consolidation, how, and how well?" meant reading 108 dossiers.
Now every ratified dossier harvests its generalisable content into 12 registries.

```
EVIDENCE -> KNOWLEDGE -> PATTERNS -> PRINCIPLES -> ARCHITECTURE
   -> STRATEGY -> ROADMAP -> DECISIONS -> ADVANTAGE
        |                                      |
        +------------- evolve.py --------------+   <- the loop closes
```

| Module | Registry | Answers |
|---|---|---|
| 1 Capability Intelligence | `capability-registry.yaml` | who implements what, how well |
| 2 Technology Radar | `technology-radar.yaml` | what is commoditising, with ring history |
| 3 Irreversible Decisions | `decision-register.yaml` | what gets expensive to change |
| 5 Pattern Library | `pattern-library.yaml` | reusable architecture, 3-instance promotion |
| 6 Failure Library | `failure-library.yaml` | recurring failure modes + JARVIS guards |
| 7 Decision Intelligence | `decision-intelligence.yaml` | which decision does this evidence influence |
| 8 Principles | `principle-library.yaml` | principles with `fails_when` + 5yr durability |
| 9 Value Chain | `value-chain-registry.yaml` | where value is created vs captured |
| 11 Unknown Unknowns | `unknown-unknowns.yaml` | questions nobody asked |
| 12 Moat Register | `moat-register.yaml` | owned vs **rented** moats |
| G14 | `contradiction-ledger.yaml` | cross-dossier conflicts, persistent |
| G16 | `research-priority.yaml` | what to research next, re-ranked by evidence |

### Query it

```bash
python3 tools/ask.py coverage              # THE query: JARVIS capability map
python3 tools/ask.py decision --open --one-way   # 4 open. Alternatives visible now.
python3 tools/ask.py capability --unclaimed      # negative space
python3 tools/ask.py radar --moving-inward       # commoditising
python3 tools/ask.py failure --exposure high     # what could kill us
python3 tools/ask.py priority                    # what to run next, and why
python3 tools/evolve.py --status                 # substrate summary
python3 tools/evolve.py --verify                 # drift check
```

### Constitutional compliance

`evolve.py` runs **post-ratification only** and refuses unratified dossiers
(verified: exits 1). Phase 2 runs never read registries — otherwise the isolation
principle would be defeated by its own extension.

**Docs:** `EXTENSION-00-GAP-ANALYSIS.md` · `EXTENSION-01-ARCHITECTURE.md` ·
`EXTENSION-02-MIGRATION-PLAN.md`

---

## 9. Design Intelligence OS ⭐ — research becomes engineering decisions

The CI-OS answered *"what is true about the ecosystem?"* It stopped there. This
layer converts every verified insight into an engineering decision, with **stage
discipline enforced in code**.

```
EVIDENCE → KNOWLEDGE → PATTERNS → PRINCIPLES → ARCHITECTURE
    → STRATEGY → ROADMAP → DECISIONS → ADVANTAGE
                      |
              tools/route.py          ← 15 questions, stage gate, priority
                      ↓
   ADR · RFC · Research · Issue · Milestone · Parked · Ignored
```

### The 15 questions, per insight

Affects JARVIS? · which stage? · which subsystem? · new module? · invalidates a
decision? · strengthens or weakens? · creates debt? · reduces debt? · ADR? · RFC? ·
research? · issue? · milestone? · future-stage? · ignore?

`route.py --explain R-003` prints all 15 answers. No routing decision is a black box.

### Stage discipline is mechanical

```
python3 tools/route.py --stage-check
#   current stage 0 · 7 blocking exit criteria open
#   1 recommendation auto-parked by the stage gate
#   R-009 stage 1 → parked (rfc withheld)
```

**Parked ≠ rejected.** Parked items keep evidence, reasoning and an *unpark trigger*
naming the exact prerequisite that releases them.

**There is no override flag.** An override would be used, and the discipline would
erode exactly under delivery pressure.

### Every recommendation carries 11 mandatory fields

affected stage · subsystem · implementation cost · maintenance burden · dependency
graph · expected user value · strategic value · evidence confidence · recommended
priority · review trigger · source insight

### Current roadmap top

| Pri | Route | Recommendation |
|---|---|---|
| P0 10.00 | ADR | Clinical audit trail — architect in, do not retrofit |
| P0 6.49 | Issue | Knowledge retrieval — replace HTML scraping |
| P0 6.43 | Issue | Wire `generate_stream()` — dark capability |
| P0 6.19 | Milestone | Build OPD queue — Stage 0 centerpiece |
| P1 5.10 | Issue | Replace external-URL STT with local recognition |

### Commands

```bash
python3 tools/route.py --all           # route every insight
python3 tools/route.py --stage-check   # verify discipline holds
python3 tools/route.py --explain R-001 # 15 questions for one insight
python3 tools/route.py --roadmap       # regenerate ROADMAP.md
```

**Docs:** `EXTENSION-03-DESIGN-INTELLIGENCE.md`
**Model:** `jarvis-model/` — stage-model · subsystem-map · routing-rules
**Output:** `design-intelligence/` — ROADMAP.md · adr/ · rfc/ · research/ · issues/ · parked/
