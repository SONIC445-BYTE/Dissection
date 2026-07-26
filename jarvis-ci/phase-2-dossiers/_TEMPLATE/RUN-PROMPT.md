# Phase 2 — Company Intelligence Run Prompt
`v1.0.0` · **Paste into a FRESH context window. One company per run. Never two.**

---

## Substitutions

- `{{COMPANY}}` — name from the registry
- `{{ID}}` — registry slug
- `{{LAYER}}` — primary layer L0–L15
- `{{TIER}}` — 1, 2 or 3 (depth budget only, never structure)

---

## Context you MAY read

✅ `phase-0-constitution/` — all nine documents
✅ `phase-1-discovery/company-registry.yaml` — this entity's row only
✅ Open Research Questions emitted by prior runs (`phase-2-dossiers/OPEN-QUESTIONS.md`)

## Context you may NOT read

❌ **Any other company's dossier** — Isolation Principle, Article II
❌ **The JARVIS repository, dissection, or blueprint** — `09-repo-context-isolation.md`

> You know JARVIS only through `08-jarvis-architecture-baseline.md` §2 (layer postures) and §3 (theses T1–T4, stated as *hypotheses to attack*). That is deliberate. If you knew the implementation, you would score this company against it and produce a mirror instead of a description.

---

## Your task

Produce a complete standalone intelligence dossier on **{{COMPANY}}**.

Not a summary. **Reverse-engineer the company.**

Write to `phase-2-dossiers/Companies/{{COMPANY}}/`:
- `dossier.md` — 16 sections, following `DOSSIER-TEMPLATE.md` exactly
- `evidence-register.csv` — every claim, tiered and sourced
- `scorecard.yaml` — 10 dimensions with justifications

---

## The 16 deliverables

1. Executive Intelligence · 2. Company Intelligence · 3. Product Reverse Engineering
4. Technical Architecture · 5. AI Architecture · 6. Developer Platform
7. Distribution · 8. Business Model · 9. User Intelligence
10. Healthcare Relevance · 11. Layer Analysis & Strategic Role · 12. Moat Assessment
13. Failure Analysis · 14. Competitive Attack Plan · 15. Lessons for JARVIS
16. Evidence Register · Confidence Matrix · Open Questions · Research Gaps

Plus the **Final Reflection** — 8 questions, mandatory, no exceptions.

---

## Hard rules

### Evidence
Every substantive claim carries exactly one tier: 🟢 **E1** verified primary · 🟡 **E2** corroborated · 🟠 **E3** inferred · 🔴 **E4** speculation (with falsifier).

- README ≠ implementation. E2 ceiling.
- Roadmap ≠ product. State the shipping rung: *rumoured → announced → preview → GA → adopted at scale*.
- Every number carries a date and a source ID.
- Absence of evidence → Research Gaps, never "they don't have it."
- Three articles citing one blog post = **one** source.
- **Inference never promotes to fact.** E3→E1 requires a new primary source ID.

### Stage discipline
Declare **stage per product line**, not per company. Criticism must be stage-adjusted. Do not credit an S0 project with S3 capabilities because its README describes them.

### No cross-company comparison
Any construction like *"unlike X"*, *"better than X"*, *"X does this too"* is a **lint error**. Comparison is Phase 3 and 6 work.

> ⚠ **Benchmark exception, handled precisely:** if a benchmark inherently involves another system, record it in the Evidence Register as a **contest** — every disputed figure with its claimant and a `CONTESTED` flag. In prose, describe the subject's own number and note that a competing figure exists, *without drawing a strategic conclusion*. "System A scores higher than {{COMPANY}}, therefore A is better positioned" is Phase 3's job, not yours.

### Strategic Role
Exactly **one primary role**. If you choose 🔴 Direct Competitor you must name all three:
1. contested layer · 2. contested JARVIS capability · 3. the buyer who picks one *instead of* the other.

Missing any one → the classification is wrong → default to 📡 Market Signal.

### Mandatory discomfort
Produce **≥1 uncomfortable finding for JARVIS** — a capability gap, an obsoleted assumption, a commoditised differentiator, or a reason a customer would rationally choose {{COMPANY}} instead. Direct JARVIS analogues require **≥3**.

A dossier with zero uncomfortable findings fails audit. Intelligence that only reassures is not intelligence.

### Thesis testing
Test **≥1 of T1–T4** (`08-jarvis-architecture-baseline.md` §3) against your evidence. Report whether it is strengthened or weakened. Their current status is already recorded in §7 of that file — use those statuses, not the original aspirational framing.

---

## Research method

Work through these in order. Do not skip to conclusions.

| Step | Focus |
|---|---|
| 1 | **Primary sources first** — repo, official docs, API responses, filings, pricing page |
| 2 | **Architecture** — infer stack from error messages, headers, job posts, SDK shape. Show the reasoning; mark E3. |
| 3 | **Product surface** — every feature, workflow, permission, retention loop, growth loop, monetisation trigger |
| 4 | **AI architecture** — model providers, memory, planning, context, guardrails, evaluation |
| 5 | **Business** — pricing with date, revenue model, segments, switching costs, **the open/closed boundary** |
| 6 | **User intelligence** — GitHub issues, Reddit, HN, G2, Discord. Rank complaints by frequency. Find churn reasons and unexpected use cases. |
| 7 | **Moats and failure modes** — both, for every company, including dominant ones |
| 8 | **Attack plan** — write it even for dependencies and integration targets; it finds *their* weaknesses |
| 9 | **Score** — 10 dimensions, each with 1–3 sentences of justification citing claim IDs |
| 10 | **Reflect** — the 8 questions |

### Where the real signal hides

- **Non-customers.** Who they refuse to serve reveals strategy better than any mission statement.
- **Hiring.** Roles reveal roadmap 6–12 months before announcements. E3, but high-confidence direction.
- **Churn reasons.** This is where attack plans come from.
- **Unexpected use cases.** This is where new categories hide.
- **The paywall line** in open-core. Where the boundary sits *is* the strategy. A paywall blocking production evaluation is a growth decision with competitive consequences.
- **What they stopped doing.** Deprecations and quiet removals are honest signals.

---

## Scoring reminders

- **Most companies score 0–2 on D9 (threat).** If you're reaching for 4, re-read the contested-layer test.
- **D10 (leverage) is usually higher than instinct suggests.** Most of the ecosystem is leverage, not enemies.
- **D9 is scored only against layers where JARVIS's posture is OWN or COMPETE.** A company dominating a layer JARVIS depends on is context, not threat.
- High threat *and* high leverage is legitimate → flag `COMPLEX`.

---

## Final Reflection (mandatory)

1. What did this company teach us that we did not know before?
2. Which assumptions did it challenge?
3. Which opportunities does it reveal for JARVIS?
4. Which parts of its architecture are worth emulating?
5. Which parts should JARVIS deliberately avoid?
6. Does this company strengthen or weaken the strategic case for JARVIS?
7. Where does it sit in the AI ecosystem and value chain?
8. **What new research questions emerged that should be investigated before analysing the next company?**

> Q8 is the only permitted cross-run channel. Questions flow forward; findings do not. Append them to `phase-2-dossiers/OPEN-QUESTIONS.md`.

---

## Done when

`python3 tools/validate.py {{COMPANY}}` exits 0.
