# Extension 03 — Design Intelligence Operating System
`v1.0.0` · 2026-07-26 · Extends the CI-OS without modifying it

> **The gap closed:** the repository stopped at knowledge. Registries accumulated
> insight; nothing converted insight into engineering decisions. This layer does
> that conversion — mechanically, with stage discipline enforced in code.
>
> **Primary output is no longer reports. It is a prioritised, evidence-based roadmap.**

---

## 1. What was missing

The CI-OS answered *"what is true about the ecosystem?"* extremely well. It never
answered *"so what should we build?"*

An insight like *"the category leader has zero compliance posture and lost regulated
markets"* sat in `failure-library.yaml` as a well-evidenced record. Nothing turned it
into an ADR, assigned it a stage, costed it, or told anyone it was P0.

The chain terminated one step early:

```
EVIDENCE → KNOWLEDGE → PATTERNS → PRINCIPLES → ... → ADVANTAGE
                                                          ✗ stopped here
                                                          ↓
                                          ENGINEERING DECISIONS   ← now added
```

---

## 2. Architecture

```
┌──────────────────────────────────────────────────────────────┐
│  L5  DECISIONS   ADR · RFC · Research · Issue · Milestone     │  NEW
│                  Parked · Ignored — all with 11 fields        │
├──────────────────────────────────────────────────────────────┤
│  L4½ ROUTER      tools/route.py                               │  NEW
│                  15 questions · stage gate · priority scoring │
├──────────────────────────────────────────────────────────────┤
│  L4½ JARVIS      jarvis-model/                                │  NEW
│      MODEL       stage-model · subsystem-map · routing-rules  │
├──────────────────────────────────────────────────────────────┤
│  L2  SUBSTRATE   12 registries                                │  EXISTS
├──────────────────────────────────────────────────────────────┤
│  L1  RESEARCH    Phases 0/R/1/2/2.5/3–Ω                       │  EXISTS
├──────────────────────────────────────────────────────────────┤
│  L0  LAW         Phase 0 constitution                         │  EXISTS
└──────────────────────────────────────────────────────────────┘
```

The **JARVIS model** layer is the new critical piece. Stage discipline cannot be
enforced mechanically without a machine-readable blueprint, and none existed —
the staged plan lived in prose. `stage-model.yaml` makes it executable.

---

## 3. The 15 questions

Every insight is evaluated against all 15, in order. Early exits are cheap.

| # | Question | Field / destination |
|---|---|---|
| 1 | Does this affect JARVIS? | exit → `ignore` if no |
| 2 | Which JARVIS stage? | `affected_stage` |
| 3 | Which subsystem? | `affected_subsystem` |
| 4 | Introduces a new module? | `introduces_module` |
| 5 | Invalidates an architectural decision? | `invalidates_decision` |
| 6 | Strengthens or weakens a design? | `design_effect` |
| 7 | Creates technical debt? | `debt_created` |
| 8 | Reduces technical debt? | `debt_reduced` |
| 9–15 | ADR · RFC · Research · Issue · Milestone · Parked · Ignore | destination |

`route.py --explain <ID>` prints all 15 answers for any recommendation. Every
routing decision is inspectable; none is a black box.

---

## 4. Stage discipline — enforced, not advised

The requirement: *never recommend Stage 3 work when Stage 0 prerequisites remain
incomplete.*

```python
if affected_stage <= current_stage:          admissible
elif blocking_prerequisites_open:            PARK  ← automatic
else:                                        admissible
```

**Verified live.** With 7 Stage-0 blocking criteria open, three Stage-1/2
recommendations were auto-parked. The RFC for MCP conformance was *withheld* despite
HIGH confidence and sound reasoning, purely because its stage was inadmissible.

### Parked ≠ rejected

Parked items keep their evidence, reasoning, date and an **unpark trigger** naming
the exact prerequisite that releases them. Unparking is mechanical, not a judgement
call. This is what makes the discipline survivable — nothing is lost by deferring,
so deferring is cheap.

### No override, deliberately

There is no `--force`. An override flag would be used, and the discipline would
erode exactly under delivery pressure — which is precisely when it matters. The
corpus contains three post-mortems that died from stage expansion; the mechanism
that prevents it should not have an off switch.

---

## 5. Priority scoring

```
value  = (uv*3 + sv*2 + debt_reduction*1.5 + confidence*1.5) / 32.5 * 10
effort = 1 / (1 + 0.25*cost + 0.1*maintenance)
score  = value * effort * irreversibility * stage_multiplier
```

**A calibration bug was found and fixed during construction.** The first formula
divided by cost, which produced a score of 47 for a trivial wiring task while a
one-way memory-architecture decision sank to P3. Bang-for-buck metrics crush
expensive strategic work.

The corrected formula **dampens** by cost rather than dividing, and applies a 1.8×
multiplier to one-way decisions — because an irreversible decision left open gets
more expensive every week, regardless of its implementation cost.

| Band | Score | Meaning |
|---|---|---|
| P0 | ≥6.0 | do now — blocks stage exit |
| P1 | ≥4.0 | current stage, high value |
| P2 | ≥2.5 | current stage, scheduled |
| P3 | ≥1.0 | opportunistic |
| P4 | <1.0 | parked or informational |

---

## 6. Current output

From 45 substrate insights, 15 routed recommendations:

```
adr:2   issue:3   milestone:3   research:2   rfc:1   parked:3   ignore:1
```

**Top of the roadmap:**

| Pri | Route | Recommendation |
|---|---|---|
| P0 10.00 | ADR | Clinical audit trail — architect in, do not retrofit |
| P0 6.49 | Issue | Knowledge retrieval — replace HTML scraping with API tiers |
| P0 6.43 | Issue | Wire `generate_stream()` — dark capability, largest latency win |
| P0 6.19 | Milestone | Build OPD queue — Stage 0 centerpiece |
| P1 5.10 | Issue | Replace external-URL STT with local recognition |

Three of these come from Phase R's repo dissection; two come from the Mem0 dossier.
**Research and repo reality are now producing a single ranked list.**

---

## 7. Worked artifacts

| File | Demonstrates |
|---|---|
| `adr/ADR-001-clinical-audit-trail.md` | Full ADR with alternatives, consequences, reversal trigger |
| `research/RES-001-memory-consolidation.md` | Research project with falsifier and must-not-block constraint |
| `parked/PARKED-001-mcp-conformance.md` | Parked item with preserved reasoning and unpark trigger |
| `ROADMAP.md` | Generated, never hand-written; regenerates on every run |

---

## 8. Commands

```bash
python3 tools/route.py --all              # route every insight
python3 tools/route.py --stage-check      # verify discipline holds
python3 tools/route.py --explain R-003    # all 15 questions for one insight
python3 tools/route.py --roadmap          # regenerate ROADMAP.md
```

---

## 9. Honest limitations

**The routing table is hand-curated.** The 15 entries in `route.py` are seeded
ground truth that proves the pipeline and calibrates the scoring. Automatic
generation from registry records lands in M2, alongside the harvest markers — the
same dependency, because both need structured emission from dossiers.

This is deliberate sequencing rather than an omission. Auto-generating routes
before the scoring is calibrated would produce a confidently-wrong roadmap, which
is worse than a hand-checked one.

**Stage completion is manually maintained.** `stage-model.yaml` reflects the
blueprint as of 2026-07-23. It needs updating when exit criteria close — currently
a human step, and the most likely source of drift.

**Cost estimates are t-shirt sizes.** `xs/s/m/l/xl` are analyst judgement, not
engineering estimates. They are honest about being rough; treating them as
precise would be false precision.

---

## 10. Acceptance against the requirement

| Required | Status |
|---|---|
| Every insight answers 15 questions | ✅ `--explain` prints all 15 |
| Never recommend Stage 3 while Stage 0 incomplete | ✅ verified — 3 auto-parked |
| affected stage | ✅ mandatory field |
| affected subsystem | ✅ mandatory, from `subsystem-map.yaml` |
| implementation cost | ✅ xs–xl |
| maintenance burden | ✅ none–high |
| dependency graph | ✅ blocking ids |
| expected user value | ✅ 0–5 |
| strategic value | ✅ 0–5 |
| evidence confidence | ✅ inherited from registry tier |
| recommended priority | ✅ P0–P4 with score |
| review trigger | ✅ mandatory |
| Output is a roadmap, not reports | ✅ `ROADMAP.md`, generated |
