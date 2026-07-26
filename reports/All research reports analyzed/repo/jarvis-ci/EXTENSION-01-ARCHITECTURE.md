# Extension Architecture — Strategic Intelligence Platform
`v1.0.0` · 2026-07-26 · Extends `jarvis-ci` without modifying it

> **Contract:** every existing phase, document, ontology, evidence rule and tool is preserved. This adds a **substrate layer** beneath them and a **query layer** above them.

---

## 1. The transform chain, made mechanical

The requested chain, with the component that owns each arrow:

```
   EVIDENCE          evidence-register.csv        [EXISTS]
      │ harvest ─────────────────────────────────  tools/harvest.py         NEW
      ▼
   KNOWLEDGE         9 registries                                           NEW
      │ abstract ────────────────────────────────  patterns + failures      NEW
      ▼
   PATTERNS          pattern-library.yaml                                   NEW
      │ generalise ──────────────────────────────  principle extraction     NEW
      ▼
   PRINCIPLES        principle-library.yaml                                 NEW
      │ apply ───────────────────────────────────  capability coverage map  NEW
      ▼
   ARCHITECTURE      decision-register.yaml                                 NEW
      │ position ────────────────────────────────  value-chain + radar      NEW
      ▼
   STRATEGY          Phases 6/7/8/Ω               [EXISTS]
      │ sequence ────────────────────────────────  priority engine          NEW
      ▼
   ROADMAP           Phase Ω                      [EXISTS]
      │ commit ──────────────────────────────────  decision register        NEW
      ▼
   ADVANTAGE         moat-register.yaml                                     NEW
      │
      └── feedback ──────────────────────────────  tools/evolve.py          NEW
                                                    ↑ closes the loop
```

**The feedback arrow is the whole point.** Without it, this is still a pipeline.

---

## 2. Layered model

```
┌─────────────────────────────────────────────────────────────┐
│  L4  VIEWS      rendered docs · radar · coverage map        │  NEW
│                 (generated, never hand-edited)              │
├─────────────────────────────────────────────────────────────┤
│  L3  QUERY      tools/ask.py — structured interrogation     │  NEW
├─────────────────────────────────────────────────────────────┤
│  L2  SUBSTRATE  9 registries (YAML, versioned, append-only) │  NEW
├─────────────────────────────────────────────────────────────┤
│  L1  RESEARCH   Phases 0/R/1/2/2.5/3/4/5/6/7/8/Ω            │  EXISTS
│                 unchanged — now also emits harvest records  │
├─────────────────────────────────────────────────────────────┤
│  L0  LAW        Phase 0 constitution — 10 documents         │  EXISTS
│                 governs every layer above                   │
└─────────────────────────────────────────────────────────────┘
```

Data flows **up** (research → substrate → query → views). Governance flows **down** (constitution binds all).

---

## 3. The nine registries

All live in `registries/`. All YAML. All versioned. All emit provenance to dossier claim IDs.

### 3.1 `capability-registry.yaml` — Module 1
The capability-centric index. Answers *"who does X, how, and how well?"*

```yaml
- id: memory-consolidation
  name: Memory consolidation & forgetting
  parent: remember               # capability tree from 06-technology-ontology
  layer: L3
  discovered_via: M7-negative-space
  discovered_in: [MEM0]          # dossier that surfaced it
  maturity: S1
  engineering_complexity: high
  maintenance_burden: high
  implementations:
    - company: Mem0
      approach: "claims outdated-fact forgetting; no mechanism described"
      evidence: [MEM0-C-033]
      quality: unverified
  architectural_patterns: []      # → pattern-library
  common_failures: [unbounded-memory-growth]   # → failure-library
  ecosystem_trend: unclaimed
  jarvis_state: absent           # absent|designed|built|wired|verified
  jarvis_opportunity: high
  opportunity_class: contested-hard   # commodity|contested-neglected|contested-hard|moat|structural
  review_interval_days: 90
  last_verified: 2026-07-26
```

**Auto-discovery:** capabilities are not hardcoded. `harvest.py` extracts them from dossier §5.1 and §3.1, matches against the existing tree in `06-technology-ontology.md`, and **creates new entries for unmatched capabilities** — flagged `discovered_via` for human confirmation.

### 3.2 `technology-radar.yaml` — Module 2

```yaml
- id: vector-retrieval
  ring: commodity                # emerging|growing|mature|commodity|declining
  ring_history:
    - {ring: growing, date: 2024-06}
    - {ring: mature, date: 2025-06}
    - {ring: commodity, date: 2026-04}   # ← movement is the signal
  movement: inward
  adoption_trend: universal
  strategic_importance: low
  risk: low
  expected_lifespan_years: 10
  replacement_candidates: [hybrid-graph-vector]
  jarvis_recommendation: integrate
  recommendation_rationale: "Commodity. Building is value-destroying."
  review_interval_days: 180
  evidence: [MEM0-C-027]
```

`ring_history` addresses **G17**: a radar without movement is astrology. Velocity between rings is the forecast.

### 3.3 `decision-register.yaml` — Module 3 ⭐

Irreversible-decision tracking, **available from Phase 2 onward** rather than only at Phase Ω.

```yaml
- id: DEC-001
  title: Memory architecture — vector-first vs temporal-graph-native
  category: architecture
  reversibility: one-way         # one-way|costly|reversible
  cost_of_change_later: "Rewriting storage + migrating all accumulated
    user memories. 6-12 months at S2; effectively impossible at S3."
  cost_curve: exponential
  recommended_timing: before-stage-1
  status: open                   # open|decided|deferred|superseded
  alternatives:
    - option: vector-first
      pros: [simpler, commodity-components, cheap]
      cons: [temporal-reasoning-ceiling, stale-fact-retrieval]
      evidence: [MEM0-C-032]
    - option: temporal-graph-native
      pros: [temporal-validity, invalidation]
      cons: [operational-complexity, fewer-off-the-shelf-parts]
  dependencies: [DEC-004]
  confidence: MEDIUM
  decided: null
  reversal_trigger: null         # mandatory once decided
```

**Why this is critical:** the existing repo records decisions only in Phase Ω §12 — the *last* document. Every architecture decision made during Phases 2–8 is currently unrecorded at the moment it is made, which is exactly when its alternatives are still visible.

### 3.4 `evidence-aging.yaml` — Module 4

Extends the existing register rather than replacing it.

```yaml
decay_model:
  E1: {half_life_days: 540, floor: MEDIUM}
  E2: {half_life_days: 365, floor: LOW}
  E3: {half_life_days: 270, floor: LOW}
  E4: {half_life_days: 120, floor: UNKNOWN}

volatility_multipliers:          # domain decays at different speeds
  pricing: 0.4                   # pricing rots fast
  funding: 0.6
  benchmarks: 0.5
  architecture: 1.5              # architecture is durable
  standards: 2.0
  licence: 1.8

revalidation_triggers:
  - {event: funding_round, invalidates: [funding, valuation, headcount]}
  - {event: major_release, invalidates: [features, architecture, benchmarks]}
  - {event: acquisition, invalidates: [ALL]}
  - {event: pricing_change, invalidates: [pricing, business_model]}
  - {event: licence_change, invalidates: [licence, deployment, moat]}
```

`age.py` computes **effective confidence** = declared confidence decayed by tier half-life × domain multiplier, and emits a re-verification queue. This makes staleness a *managed* property instead of a warning nobody reads.

### 3.5 `pattern-library.yaml` — Module 5

```yaml
- id: PAT-011
  name: Pluggable backends behind a stable interface
  category: extensibility
  purpose: "Let users choose infrastructure without forking"
  strengths: [adoption-breadth, avoids-lock-in-objection, community-contribution]
  tradeoffs: [lowest-common-denominator-API, N-backend test matrix]
  complexity: medium
  observed_in:
    - {company: Mem0, evidence: [MEM0-C-027], note: "19 vector backends"}
  jarvis_recommendation: adopt
  applies_to: [adapter-framework, storage, inference]
  antipattern_of: null
  first_observed: 2026-07-26
  instances: 1                   # promotes to CONFIRMED at >= 3
```

Patterns with `instances >= 3` promote from OBSERVED to CONFIRMED. Below 3 it is a coincidence — the same discipline Phase 6 already applies.

### 3.6 `failure-library.yaml` — Module 6

```yaml
- id: FAIL-003
  name: Differentiator gated above the evaluation threshold
  category: business-model
  mechanism: "The capability that proves the product's value sits behind a
    price step large enough to convert a technical evaluation into a
    procurement decision. Evaluation stalls; the deal is lost before the
    product is judged."
  observed_in:
    - {company: Mem0, evidence: [MEM0-C-025, MEM0-C-039, MEM0-C-040]}
  leading_indicators:
    - "community reports of blocked evaluation"
    - "price step > 5x between adjacent tiers"
    - "differentiating capability absent from free/entry tier"
  severity: high
  reversibility: reversible
  jarvis_exposure: low
  jarvis_guard: "Any future pricing must keep the differentiating
    capability inside the evaluation tier."
  instances: 1
```

Every dossier §13 and §14 harvests into this. Post-mortems (Olive AI, Forward, Pear) will contribute the highest-value entries.

### 3.7 `principle-library.yaml` — Module 8

The most abstract registry, and the one with the longest shelf life.

```yaml
- id: PRIN-002
  statement: "Neutrality is a wedge against incumbents who lack the
    incentive to make their layer portable."
  derived_from: [Mem0]
  evidence: [MEM0-C-008]
  underlying_assumption: "Incumbent incentives stay misaligned with
    portability."
  fails_when: "An incumbent decides portability grows their market, or a
    regulator mandates it."
  durability_5yr: MEDIUM
  durability_rationale: "Depends on a competitor's choice, not on
    anything the wedge-holder controls."
  jarvis_verdict: adopt-modified
  jarvis_application: "Applies directly in healthcare: EMR vendors have
    no incentive to make clinical workflow portable across systems.
    Same wedge, different layer."
  conflicts_with: []
```

`fails_when` and `durability_5yr` are mandatory. A principle without stated failure conditions is a slogan.

### 3.8 `value-chain-registry.yaml` — Module 9

Answers the six economic questions `01-canonical-taxonomy.md` §4 poses but never records.

```yaml
- layer: L3
  value_created_by: "persistence enabling continuity across sessions"
  value_captured_by: "whoever owns the agent loop, not the memory box"
  margin_concentration: low
  margin_evidence: [MEM0-C-043]
  lock_in_source: accumulated-user-memories
  lock_in_strength: 4
  lock_in_ceiling: "Apache-2.0 self-host escapes it"
  network_effects: none
  switching_cost: 4
  commoditising: [storage, extraction, vector-retrieval]
  contested: [consolidation, temporal-validity, procedural-memory]
  new_categories_forming: [portable-cross-app-memory]
  jarvis_position: "own the contested subset only; integrate the commodity subset"
  last_reviewed: 2026-07-26
```

### 3.9 `moat-register.yaml` — Module 12 output

```yaml
- id: MOAT-001
  name: Honest-failure discipline
  type: technology
  state: seed                    # seed|building|moat|eroding|lost
  current_strength: 2
  target_strength: 4
  compounds: true
  compounding_mechanism: "Every failure mode encoded becomes permanent
    behaviour; the library of known-honest failures grows with usage."
  copy_resistance: moderate
  time_to_copy_months: 12
  copy_rationale: "Copyable in principle; requires sustained discipline
    that demo-driven competitors have no incentive to maintain."
  rented_or_owned: owned
  evidence: [phase-R capability-ledger]
  depends_on: []
```

`rented_or_owned` operationalises the Phase 6 §9 distinction. Distribution deals read like owned moats and are rented.

---

## 4. Cross-cutting registries (my additions)

### 4.1 `decision-intelligence.yaml` — Module 7 🔴
The missing link between evidence and action.

```yaml
decision_domains: [architecture, business, distribution, healthcare,
                   security, platform, developer-ecosystem, roadmap,
                   hiring, funding]

- finding_id: MEM0-C-032
  finding: "Vector-first architecture caps temporal reasoning"
  influences:
    - {domain: architecture, decision: DEC-001, direction: "favours temporal-graph-native"}
    - {domain: roadmap, decision: null, direction: "L3 work must target the contested subset"}
  strength: strong               # strong|moderate|weak
  actioned: false
```

Every dossier finding must map to ≥1 decision domain or be explicitly marked `informational`. This is what converts research into decisions rather than reading material.

### 4.2 `contradiction-ledger.yaml` — G14
Cross-dossier conflicts as persistent first-class objects.

```yaml
- id: CON-001
  subject: "Mem0 total funding"
  claims:
    - {claim_id: MEM0-C-012, value: "$24M", tier: E1, source: company-release}
    - {claim_id: MEM0-C-017, value: "$24.5M", tier: E2, source: aggregator}
    - {claim_id: MEM0-C-018, value: "$20.5M", tier: E2, source: aggregator}
  scope: intra-dossier           # intra-dossier|cross-dossier
  status: unresolved
  resolution: null
  resolution_rationale: null
  blocks_synthesis: false
```

### 4.3 `unknown-unknowns.yaml` — Module 11
Systematic blind-spot discovery, as a permanent phase rather than a Phase Ω afterthought.

```yaml
probe_classes:
  - hidden-assumptions
  - architectural-blind-spots
  - distribution-blind-spots
  - regulatory-blind-spots
  - organisational-bottlenecks
  - missing-integrations
  - emerging-competitors
  - adjacent-markets
  - new-ecosystem-layers
  - future-technologies

- id: UNK-001
  probe_class: hidden-assumptions
  question: "Every registered company assumes memory is worth persisting.
    What if the correct architecture is aggressive forgetting with cheap
    re-derivation from source systems?"
  surfaced_by: pattern-absence
  surfaced_in: [Mem0]
  status: open
  priority: high
  would_invalidate: [PRIN-002, DEC-001]
```

**Auto-generation triggers:** capability with zero implementations · pattern with exactly one instance · layer with no Direct Competitor · three dossiers sharing an unexamined assumption · registry field empty across >80% of entries.

### 4.4 `research-priority.yaml` — G16
Closes the loop Phase 1 opened. Re-ranks the remaining 107 dossiers using what the first *N* taught.

```yaml
recompute_every_n_dossiers: 10
factors:
  - {name: capability_gap_severity, weight: 3}
  - {name: unresolved_open_questions_touching, weight: 3}
  - {name: decision_blocking, weight: 4}        # highest — blocks a decision
  - {name: layer_coverage_deficit, weight: 2}
  - {name: contradiction_resolution, weight: 2}
  - {name: original_tier, weight: 1}            # Phase 1's guess, now least important
```

`decision_blocking` carries the highest weight deliberately: research that unblocks a pending irreversible decision is worth more than research that merely fills a map.

---

## 5. `tools/evolve.py` — Module 10, the engine ⭐

The component that makes this an OS. Runs automatically after each dossier ratifies.

```
evolve.py <Company>
  │
  ├─ 0. GUARD    refuse unless validate.py exits 0
  │              (registries never ingest unratified research)
  │
  ├─ 1. HARVEST  parse dossier + evidence register + scorecard
  │              §5.1 → capabilities      §12   → moats
  │              §13  → failure modes     §15.1 → principles
  │              §15.2→ patterns          §15.4/5 → radar rings
  │              §11  → value chain       §16.4 → open questions
  │
  ├─ 2. MERGE    upsert into 9 registries
  │              new capability?  → create, flag for confirmation
  │              pattern seen 3x? → promote OBSERVED → CONFIRMED
  │              radar ring moved?→ append ring_history entry
  │
  ├─ 3. DETECT   cross-dossier contradictions → contradiction-ledger
  │
  ├─ 4. PROBE    unknown-unknown triggers → unknown-unknowns.yaml
  │
  ├─ 5. LINK     findings → decision domains (decision-intelligence)
  │
  ├─ 6. AGE      recompute effective confidence; emit re-verify queue
  │
  ├─ 7. REPRIO   every 10th dossier, recompute research-priority
  │
  └─ 8. RENDER   regenerate views/ (radar, coverage map, dashboards)
```

**Idempotent.** Re-running for the same dossier produces no duplicates — merge keys on `(registry, id, source_dossier)`.

---

## 6. `tools/ask.py` — the query layer (G13)

Nine registries without interrogation are nine filing cabinets.

```bash
ask.py capability --gap                 # where JARVIS is absent + opportunity high
ask.py capability --unclaimed           # zero implementations = negative space
ask.py radar --ring commodity           # what must never be built
ask.py radar --moving-inward            # commoditising now
ask.py decision --open --one-way        # irreversible decisions still open ⚠
ask.py decision --blocking              # decisions blocked on research
ask.py pattern --confirmed              # >= 3 instances
ask.py failure --exposure high          # failure modes JARVIS is exposed to
ask.py principle --durability LOW       # principles that may not survive
ask.py evidence --stale                 # re-verification queue
ask.py contradiction --unresolved
ask.py coverage                         # ⭐ full JARVIS capability map (G15)
ask.py priority                         # what to research next, and why
```

`ask.py coverage` is the single most valuable command in the system: for every capability the ecosystem has, JARVIS's state, the gap class, and the opportunity — live, not a Phase R snapshot.

---

## 7. Constitutional compliance

| Rule | How the extension honours it |
|---|---|
| **Article II — Isolation** | `evolve.py` runs **post-ratification only**. Phase 2 runs never read registries. Enforced by the step-0 guard. |
| **Article IV — Evidence** | Every registry field carries `evidence: [claim_ids]`. No unsourced records. Tiers propagate. |
| **Article IV.2 — No promotion** | Registries store tier alongside value; merge never upgrades a tier. |
| **09 — Repo isolation** | Registries inherit phase-access rules. `jarvis_state` fields populate **only** from Phase R, and are readable only in Phases 7/8/Ω. |
| **Article VI — Synthesis gate** | Registries accumulate during Phase 2 but **synthesis views stay locked** until AUDIT-PASSED. `evolve.py` writes; it does not conclude. |
| **Article X — Done** | Extended: a dossier is ratified only when `validate.py` **and** `evolve.py` both succeed. |
| **Phase 2.5 audit** | Gains 3 checks: C8 registry integrity · C9 harvest completeness · C10 contradiction resolution. |

---

## 8. Risks

| # | Risk | Severity | Mitigation |
|---|---|---|---|
| R1 | **Registry rot** — substrate drifts from dossiers | 🔴 | `evolve.py --verify` re-harvests and diffs; audit check C8 |
| R2 | **Harvest brittleness** — parsing prose is fragile | 🟠 | Template gains explicit `<!-- harvest:capability -->` markers; unparsed sections warn loudly rather than fail silently |
| R3 | **Premature abstraction** — patterns from 1 instance | 🟠 | 3-instance promotion rule; OBSERVED never used in synthesis |
| R4 | **Isolation leak** — registries read during Phase 2 | 🔴 | Step-0 guard + `validate.py` flags registry references in dossiers |
| R5 | **Maintenance burden** — 9 registries to keep current | 🟠 | Fully automated via `evolve.py`; humans only confirm auto-discovered capabilities |
| R6 | **False precision** — YAML looks authoritative | 🟠 | Every record carries tier + confidence + last_verified; `ask.py` prints them always |
| R7 | **Over-engineering** — building an OS nobody runs | 🟠 | Phased migration; M1 (capability + evolve + ask) delivers standalone value before anything else is built |
| R8 | **Auto-discovery noise** — junk capabilities | 🟡 | New entries land in `pending_confirmation`; excluded from queries until confirmed |

**R7 is the honest one.** The mitigation is real: Milestone 1 is independently useful. If the extension stalls after M1, the repository is still strictly better than it is today.
