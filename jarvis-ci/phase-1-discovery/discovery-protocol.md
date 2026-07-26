# Company Discovery Protocol
`v1.0.0` · Phase 1 · **Continuous, never "done"**

The wrong question is *"who are our competitors?"* — it produces a list of companies that look like you.

The right question is **"who owns value in each ecosystem layer?"** — it produces a map of where value actually accrues, including the players who will matter in eighteen months and the ones quietly making your differentiator free.

---

## 1. Discovery methods

Run all seven. Each surfaces entities the others miss.

### M1 — Layer sweep
For each layer L0–L15: *who captures value here?* Force at least 3 candidates per layer, including one non-obvious.

### M2 — Dependency archaeology
Read the dependency graphs of the leaders. What do they build on? Those are L0–L2 dependencies and Technology Suppliers — and they are systematically underrepresented in competitor lists because they are invisible from the outside.

### M3 — Standards tracing
Who authors, governs, and implements the standards? Standards bodies are not companies but they set the rules everyone follows. Track conformance *and* extension behaviour.

### M4 — Job-posting archaeology
Read hiring at adjacent companies. Roles reveal roadmap 6–12 months ahead of announcements. A company hiring clinical informaticists is entering healthcare regardless of what its blog says.

### M5 — Community mining
GitHub trending, HN, Reddit, Product Hunt, Discord. Rising OSS projects become tomorrow's infrastructure. This is where L15 candidates are found earliest.

### M6 — Adjacency walk
For every registered company: who do *they* consider competitors? Who do they integrate with? Who do their users mention as alternatives? Follow the graph two hops out.

### M7 — Negative space
**The highest-value method.** What layer has *no* strong player? Empty layers are either (a) not real, (b) not yet valuable, or (c) **the opportunity**. Distinguishing (c) from (a) is the most valuable analytical act in this entire pipeline — and it is the only method that finds opportunities rather than threats.

---

## 2. Inclusion criteria

Include if **any** apply:
- Owns meaningful value in any layer L0–L15
- JARVIS depends on it or plausibly will
- JARVIS's target users already run it
- Contests a layer JARVIS intends to own
- Its decisions reshape the ecosystem
- **It failed, and the failure is instructive** ← chronically undervalued
- It is healthcare infrastructure in India or a major market

Exclude if: pure consultancy with no product · no evidence of real usage · duplicate of an existing entry · a feature rather than a product.

**When uncertain, include as Priority Tier 3 Market Signal.** Registration is cheap; blind spots are not.

---

## 3. Priority tiers

| Tier | Criteria | Research depth |
|---|---|---|
| **1** | Contests L3/L4 · foundational dependency · healthcare system of record · L8 distribution owner | Full dossier, maximum depth |
| **2** | Meaningful layer owner · likely integration target · significant supplier | Full dossier, standard depth |
| **3** | Market signal · adjacent · emerging · instructive failure | Full structure, thinner sections, explicit gap notes |

Tier drives **ordering and depth budget**, never structure. Every tier gets all 16 sections.

---

## 4. Registry hygiene

- `id` is stable and never reused
- `entity_status` reviewed each cycle (`active | acquired | dormant | dead | pivoted`)
- Layer reassignment requires a Decision Ledger entry
- New entries default to Tier 3 until evidence justifies promotion
- **RHINAL/JARVIS carry `self: true`** and are excluded from all scoring

---

## 5. Discovery cadence

| Trigger | Action |
|---|---|
| Every 10 dossiers completed | Re-run M1, M6, M7 |
| Any Final Reflection Q8 naming a new entity | Register immediately |
| Major funding/acquisition/launch in a tracked layer | Register + assess tier |
| Each phase boundary | Full M1–M7 sweep |
| **Every cycle, mandatory** | Nominate ≥1 L15 candidate; promote or dismiss with reasoning |

---

## 6. Open discovery questions

Carried forward and answered as research proceeds. These are live gaps, not rhetorical prompts.

| # | Question | Method | Status |
|---|---|---|---|
| DQ-01 | Who owns **memory consolidation/forgetting**? Universally named as unsolved — is anyone actually solving it, or is it unclaimed negative space? | M7 | OPEN |
| DQ-02 | Which Indian HIS vendors dominate tier-2/3 hospitals? Largely invisible in English-language sources; likely regional and offline. | M1, M5 | OPEN |
| DQ-03 | Who owns **procedural memory** (agents learning *how*, not just *what*)? | M7 | OPEN |
| DQ-04 | Which OCR engines actually handle Indian medical documents — handwritten prescriptions, regional scripts, mixed-script forms? | M1 | OPEN |
| DQ-05 | Who is building **error recovery / replanning** as a first-class capability rather than an afterthought? | M7 | OPEN |
| DQ-06 | Which ABDM-integrated vendors have real transaction volume vs. sandbox-certified-only? Certification counts are widely cited; usage counts are not. | M3 | OPEN |
| DQ-07 | What is the MCP server landscape for healthcare specifically? | M3, M5 | OPEN |
| DQ-08 | Who owns **confidence estimation / calibration** for agents? | M7 | OPEN |
| DQ-09 | Which agent-memory or agent-framework startups have died, and why? Failure evidence is cleaner than success narrative. | M6 | OPEN |
| DQ-10 | Is anyone building an **adapter SDK** for legacy clinical systems as a product in its own right? Direct test of JARVIS thesis T4. | M7 | OPEN |
| DQ-11 | Who serves the gap between "ABDM-connected" and "digitally mature" — the tier-2/3 middle market? | M7 | OPEN |
| DQ-12 | L15 nomination for this cycle — what category doesn't have a name yet? | M7 | OPEN |

> DQ-01, DQ-03, DQ-05, DQ-08, DQ-10 and DQ-11 are all **negative-space questions**. If they stay unanswered, that is itself the finding — and probably the most commercially important output of Phase 1.
