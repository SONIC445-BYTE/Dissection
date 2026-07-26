# Repository Gap Analysis
**Chief Research Architect assessment** · 2026-07-26 · Against `jarvis-ci` @ 44 files

> **Verdict:** the foundation is sound and stays. What is missing is not documents — it is **substrate**. The repository is a *pipeline*; the requirement is an *operating system*. Those differ in one structural way, and everything else follows from it.

---

## 1. The structural diagnosis

### 1.1 What exists

A rigorous, gated, evidence-disciplined **batch DAG**:

```
Phase 0 → R → 1 → 2 → 2.5 ⛔ → 3/4/5 → 6 → 7 → 8 → Ω
```

It runs once. It terminates. It produces documents.

### 1.2 The two defects

**Defect A — the pipeline terminates.** Phase Ω is a leaf node. Nothing reads it; nothing writes back. When dossier #109 arrives six months later, there is no mechanism by which it updates any conclusion reached in Phase 6, 7, 8 or Ω. The knowledge base would be *correct as of the day it was finished* and silently decaying thereafter.

**Defect B — knowledge is indexed by company only.** Today there is exactly **one** accumulating data structure (`company-registry.yaml`) plus per-dossier artefacts. Everything else is prose inside documents.

To answer *"which companies attempt memory consolidation, using what approaches, with what failure modes?"* you must **read all 108 dossiers**. The knowledge exists but is not addressable. That is a filing cabinet, not a knowledge base.

### 1.3 Why this matters more than it sounds

The user's acceptance test is precise: **"every new competitor report should strengthen the system."**

Under the current design a new report strengthens *the reader*, temporarily. It does not strengthen *the system*, because there is nowhere for its generalisable content to land. Lessons, patterns, failure modes and principles are extracted into prose in §15 of each dossier and then trapped there.

---

## 2. The fix, stated once

**Invert the data model.**

| | Current | Extended |
|---|---|---|
| Unit of knowledge | the dossier | **the registry record** |
| Unit of research | the dossier | the dossier *(unchanged)* |
| Documents are | the product | **views over registries** |
| New dossier effect | adds a document | **updates 9 registries** |
| Query surface | full-text read | **structured query** |
| Lifecycle | terminates at Ω | **cycles continuously** |

The existing phases become **producers** that emit structured records into a shared substrate. Nothing about how research is *conducted* changes. What changes is that each run now **harvests** its generalisable findings into addressable form.

This is why no rewrite is needed: the dossier template already requires every field the registries need — §5.1 capability map, §12 moats, §13 failure analysis, §15.1 principles, §15.4/15.5 commodity-vs-moat. **The data is already being produced and then discarded.** The extension captures it.

---

## 3. Gap register

Each mapped to the requested item, with the specific defect and where the data already exists.

| # | Requested | Gap | Data already produced in | Severity |
|---|---|---|---|---|
| 1 | Capability Intelligence | No capability-indexed structure. Phase 4 analyses technologies *one at a time* into documents; nothing aggregates. | Dossier §5.1, §3.1 | 🔴 CRITICAL |
| 2 | Technology Radar | Ontology §2 has a static commodity/moat table written from priors. No rings, no trend, no lifespan, no review cadence. | Ontology §2, dossier §15.4/15.5 | 🔴 CRITICAL |
| 3 | Irreversible Decisions | Decision Ledger exists **only inside Phase Ω §12** — the last document. Decisions are made in Phases 2–8 and recorded nowhere until the end. | Phase Ω §12 (too late) | 🔴 CRITICAL |
| 4 | Evidence Aging | `accessed` date + 365-day STALE warning only. No confidence decay, no per-claim review interval, no revalidation trigger, no re-verification workflow. | evidence-register.csv | 🟠 HIGH |
| 5 | Pattern Library | Patterns observed per-dossier in prose; never abstracted or accumulated. | Dossier §15.2 | 🟠 HIGH |
| 6 | Failure Library | Every dossier has §13 Failure Analysis. Phase 6 §8 aggregates **once**. No persistent library. | Dossier §13, §14 | 🟠 HIGH |
| 7 | Decision Intelligence | No link from evidence → decision. Research and decisions are separate universes. | — (absent entirely) | 🔴 CRITICAL |
| 8 | Principle Extraction | §15.1 mandates principles-not-features — good — but they evaporate into prose. | Dossier §15.1 | 🟠 HIGH |
| 9 | Value Chain Intelligence | Taxonomy §4 lists six economic properties as *questions to ask*. Never answered, stored or tracked. | Taxonomy §4, Phase 3 §6 | 🟠 HIGH |
| 10 | Evolution Engine | **The core gap.** No mechanism propagates a new dossier into any downstream artefact. | — (absent entirely) | 🔴 CRITICAL |
| 11 | Unknown Unknowns | `OPEN-QUESTIONS.md` is a flat list of *known* unknowns. Phase Ω §13 addresses unknown-unknowns once, at the end. No systematic discovery. | OPEN-QUESTIONS.md (partial) | 🟠 HIGH |
| 12 | Research OS | Consequence of 1–11. The transform chain Evidence→…→Advantage has no machinery. | — | 🔴 CRITICAL |

---

## 4. Gaps I found that were not requested

Acting as architect rather than order-taker, five additional gaps surfaced. Each is load-bearing for the OS framing.

### G13 — No query layer 🔴
Nine registries with no way to interrogate them is nine more filing cabinets. *"Show every capability where JARVIS has no coverage and the pattern is CONTESTED"* must be one command, or the substrate will not be used.

### G14 — No contradiction persistence 🟠
`contested` is a per-claim CSV flag. When dossier #7 and dossier #52 disagree about a third party, nothing detects it. Phase 2.5 C5 enumerates conflicts **once**. Cross-dossier contradiction needs to be a first-class, persistent, resolvable object.

### G15 — No capability-coverage map for JARVIS 🔴
The single most valuable query in the entire system: *for every capability the ecosystem has, what is JARVIS's state?* Phase R produced this **once**, for one point in time, in prose. It must be live, because it is the actual roadmap input.

### G16 — No research-priority feedback loop 🟠
Phase 1 sets research order by tier, decided **before any research existed**. After 30 dossiers the system knows far more about what matters — but has no mechanism to re-prioritise the remaining 78. The most informed prioritisation decision is the one never made.

### G17 — No temporal / trend layer 🟠
Every registry as designed is a snapshot. *"Vector retrieval commoditised over 18 months"* is a strategically vital observation that requires **versioned history**, not current state. Radar rings without movement are astrology.

---

## 5. What must NOT change

Explicitly preserved, per instruction and on merit:

- ✅ All 10 Phase 0 constitution documents — the extension **inherits** them
- ✅ Evidence tiers E1–E4, source hierarchy, promotion prohibition
- ✅ Isolation Principle (Article II) — registries are written **after** a dossier ratifies, never read during a Phase 2 run
- ✅ Repo-context isolation (`09`) — registries carry the same phase-access rules
- ✅ Strategic Role taxonomy and the three-part competitor test
- ✅ Stage discipline S0–S4
- ✅ Phase 2.5 hard gate — **extended, not weakened**: new checks added for registry integrity
- ✅ All existing phase run-prompts, templates, tooling
- ✅ The Mem0 exemplar

**One deliberate constraint:** the harvest step runs *post-ratification*. A Phase 2 run must never read the registries, or cross-company contamination re-enters through the back door and Article II is defeated by its own extension.

---

## 6. Design principle for the extension

> **Registries accumulate. Documents render. Research produces. Queries consume.**

Four roles, cleanly separated. The existing repository already does *research* and *documents* well. The extension adds *accumulation* and *consumption*, and closes the loop between them.

The full design follows in `EXTENSION-01-ARCHITECTURE.md`.
