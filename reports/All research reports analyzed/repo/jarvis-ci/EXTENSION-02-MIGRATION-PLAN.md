# Migration, Integration & Implementation Plan
`v1.0.0` · 2026-07-26

> **Zero-disruption guarantee:** the extension is purely additive. No existing file is modified except by explicit, listed amendment. If the extension were deleted entirely today, the original repository would function exactly as before.

---

## 1. What changed, precisely

### 1.1 Added — 18 new files

```
registries/                          12 registries (the substrate)
  capability-registry.yaml              Module 1
  technology-radar.yaml                 Module 2
  decision-register.yaml                Module 3
  pattern-library.yaml                  Module 5
  failure-library.yaml                  Module 6
  decision-intelligence.yaml            Module 7
  principle-library.yaml                Module 8
  value-chain-registry.yaml             Module 9
  unknown-unknowns.yaml                 Module 11
  moat-register.yaml                    Module 12
  contradiction-ledger.yaml             G14
  research-priority.yaml                G16
tools/
  ask.py                                query layer (G13)
  evolve.py                             evolution engine (Module 10)
phase-2-dossiers/_TEMPLATE/
  HARVEST-MARKERS.md                    R2 mitigation
EXTENSION-00-GAP-ANALYSIS.md
EXTENSION-01-ARCHITECTURE.md
EXTENSION-02-MIGRATION-PLAN.md
```

### 1.2 Modified — nothing yet

**Zero existing files have been changed.** The extension runs alongside.

### 1.3 Amendments required (proposed, not yet applied)

Three small, surgical amendments to activate the loop. Each is listed with its exact scope so it can be reviewed before application.

| # | File | Change | Lines | Why |
|---|---|---|---|---|
| A1 | `00-research-constitution.md` Art. X | Add one checklist item: *"`evolve.py` harvest succeeds"* | +1 | Makes harvest part of Definition of Done |
| A2 | `phase-2.5-audit/research-quality-audit.md` | Add checks **C8** registry integrity, **C9** harvest completeness, **C10** contradiction resolution | +18 | Extends the gate; does not weaken it |
| A3 | `_TEMPLATE/DOSSIER-TEMPLATE.md` | Reference `HARVEST-MARKERS.md`; add marker slots to §5.1, 11, 12, 13, 15.1, 15.2, 15.4, 15.5, 16.4 | +10 | Makes harvest mechanical |

**A1 and A2 are the only ones that change behaviour.** A3 is additive scaffolding.

> These are deliberately left **unapplied**. Applying A1/A2 would immediately mark the Mem0 exemplar as non-compliant until its harvest markers are retrofitted — which is Milestone 2 work. Applying them now would fail a currently-passing dossier for a reason unrelated to its quality.

---

## 2. Integration with existing phases

Each phase gains a substrate interaction. **No phase changes what it does.**

| Phase | Reads registries? | Writes registries? | Note |
|---|---|---|---|
| 0 Constitution | — | — | Governs registries; unchanged |
| R Repo Dissection | — | ✍️ `jarvis_state`, `moat-register` seeds | Already produced this data as prose |
| 1 Discovery | — | ✍️ new capability candidates | Discovery already emits DQ questions |
| **2 Dossiers** | 🚫 **FORBIDDEN** | ✍️ **post-ratification only** | ⚠ **Article II critical** — see §3 |
| 2.5 Audit | ✅ | ✍️ audit results | Gains C8/C9/C10 |
| 3 Layers | ✅ | ✍️ value-chain, radar rings | Layer economics land in registry |
| 4 Technology | ✅ | ✍️ radar, capability maturity | Validates ontology §2 classifications |
| 5 Healthcare | ✅ | ✍️ capability, decision-register | Adapter costs inform DEC entries |
| 6 Synthesis | ✅ **all** | ✍️ pattern/failure promotions | Registries make patterns queryable |
| 7 Opportunity | ✅ + repo | ✍️ decision-register decisions | `ask.py coverage` is the core input |
| 8 Moat | ✅ + repo | ✍️ moat-register | Registry *is* the deliverable |
| Ω Master Strategy | ✅ everything | ✍️ decision reversal triggers | Renders from substrate |

### 2.1 The Article II safeguard — the one that matters

```
Phase 2 run  ──> dossier.md ──> validate.py ──> RATIFIED
                                                    │
                                                    ▼  (only here)
                                              evolve.py ──> registries
                                                    │
                                            ┌───────┴────────┐
                                            │ NEXT Phase 2   │
                                            │ run must NOT   │
                                            │ read these     │
                                            └────────────────┘
```

Enforced three ways:
1. `evolve.py` step 0 refuses unratified dossiers — **verified live**, exits 1
2. `validate.py` flags `registries/` references inside dossiers *(to be added in M2)*
3. `RUN-PROMPT.md` context list omits registries entirely

> If a Phase 2 run could read the capability registry, it would see what previous dossiers concluded — and the isolation principle would be defeated by its own extension. This is the single highest-severity risk in the design (R4), and it is why harvest is strictly post-ratification.

---

## 3. Prioritised implementation roadmap

Sequenced so **each milestone delivers standalone value**. If work stops after any milestone, the repository is still better than before — mitigating R7 (over-engineering).

### ✅ M0 — Foundation *(COMPLETE)*
Gap analysis · architecture · 12 registries seeded from Mem0 · `ask.py` · `evolve.py` · harvest-marker spec.
**Value now:** `ask.py coverage` answers *"where is JARVIS absent and the opportunity high?"* in one command. **4 open one-way decisions** are visible that were previously invisible until Phase Ω.

### M1 — Activate the loop *(next, ~1 session)*
1. Apply amendments A1, A2, A3
2. Retrofit harvest markers into the Mem0 exemplar
3. Implement `evolve.py` merge logic (upsert, 3-instance promotion, ring-history append)
4. Add `validate.py` registry-reference check
**Exit:** running `evolve.py Mem0` reproduces the seeded registries mechanically. Drift check passes.

### M2 — Prove at scale *(~3 sessions)*
Run dossiers 2–5 in `research-priority.yaml` order: **Zep/Graphiti → Letta → Epic → ABDM**. Each with harvest markers, each fully evolved.
**Exit:** ≥1 pattern promotes OBSERVED→CONFIRMED at 3 instances. Cross-dossier contradiction auto-detected. `ask.py` answers questions no single dossier could.
**This is the acceptance test for "every new report strengthens the system."**

### M3 — Aging & automation *(~2 sessions)*
`tools/age.py` — confidence decay, volatility multipliers, re-verification queue. `ask.py evidence --stale`. Auto-triggered unknown-unknown probes.
**Exit:** the system tells you what to re-verify without being asked.

### M4 — Views layer *(~2 sessions)*
`tools/render.py` generating `views/` — radar chart, coverage map, decision dashboard. Regenerated on every evolve.
**Exit:** human-readable strategic dashboards, always current, never hand-edited.

### M5 — Continuous operation *(ongoing)*
Priority recompute every 10 dossiers. Quarterly radar review. Decision-register review at each phase boundary.

---

## 4. Risks — status after M0

| # | Risk | Status | Evidence |
|---|---|---|---|
| R1 | Registry rot | 🟢 mitigated | `evolve.py --verify` built, passing |
| **R2** | **Harvest brittleness** | 🟡 **materialised, spec'd** | **4 sections returned 0 rows on live test.** `HARVEST-MARKERS.md` written; implementation in M1 |
| R3 | Premature abstraction | 🟢 mitigated | 3-instance rule enforced; 0 CONFIRMED patterns from 1 dossier — correct |
| R4 | Isolation leak | 🟢 mitigated | Guard verified live (exit 1 on unratified) |
| R5 | Maintenance burden | 🟡 partial | `evolve.py` automates; merge logic pending M1 |
| R6 | False precision | 🟢 mitigated | Every record carries evidence + last_verified |
| R7 | Over-engineering | 🟢 mitigated | M0 delivers standalone value; milestones independently useful |
| R8 | Auto-discovery noise | 🟢 mitigated | `pending_confirmation` field; excluded from queries |

> **R2 materialising during M0 is a good outcome.** It was found by testing rather than by discovering broken registries after 40 dossiers. The fix is specified and cheap.

---

## 5. Rollback

The extension is a strict superset. To remove entirely:

```bash
rm -rf registries/ views/ tools/ask.py tools/evolve.py EXTENSION-*.md
rm phase-2-dossiers/_TEMPLATE/HARVEST-MARKERS.md
# revert A1/A2/A3 if applied
```

The original 44-file repository is untouched and fully functional.

---

## 6. Acceptance test

The user's requirement: **"every new competitor report should strengthen the system."**

| Before | After |
|---|---|
| New dossier → 1 document added | New dossier → 12 registries updated |
| "Who does memory consolidation?" → read 108 dossiers | → `ask.py capability --unclaimed` |
| Decisions recorded at Phase Ω | → visible from dossier #1 |
| Patterns trapped in prose | → promote at 3 instances, queryable |
| Research order fixed at Phase 1 | → re-ranked by what's been learned |
| Pipeline terminates at Ω | → loop closes; Ω feeds priority |

**Verified at M0 with a single dossier:** 64 records across 12 registries, 6 high-opportunity capability gaps identified, 4 open one-way decisions surfaced, 2 high-exposure failure modes flagged with guards, and a research priority ranking that reorders Phase 1's tier-based guess using evidence.
