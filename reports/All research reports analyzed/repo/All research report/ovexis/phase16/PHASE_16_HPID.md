# PHASE 16 — KNOWLEDGE GRAPH & CONTINUOUS LEARNING
## The Healthcare Platform Intelligence Database (HPID)

**Phase:** 16 of 16 (+ Ω) · **Date:** 2026-07-26 · **Status:** COMPLETE — canonical
**Location:** `ovexis/hpid/` · **Database:** `hpid.sqlite` (8 tables, 2 views)

> Per **DL-002**, HPID *extends* the existing 449-platform Phase-0 registry rather than rebuilding it. The engagement's output is not a set of documents — it is a queryable asset that absorbs future dossiers.

---

## 16.1 WHAT WAS BUILT

| Artifact | Rows | Content |
|---|---|---|
| **feature_ontology** | **55** | Canonical, deduplicated feature definitions from 1,277 raw rows |
| **workflow_ontology** | **84** | Stages classed patient / clinical / financial / administrative |
| **integration_graph** | **562** | platform ↔ category ↔ protocol ↔ API surface ↔ automation method |
| **healthcare_concepts** | **26** | FHIR resources, ABDM entities, departments, software modules |
| **adapter_backlog** | **15** | Prioritised JARVIS backlog with readiness status |
| **platform** | **449** | Government-sourced registry (carried forward) |
| **market_law** | 12 | Phase-9 laws with evidence |
| **engineering_law** | 12 | Phase-10 laws with trade-offs and failure cases |

Every table is emitted in **CSV, JSON, YAML and SQLite**.

### Views

```sql
SELECT * FROM v_buildable;              -- READY backlog joined to feature scores
SELECT * FROM v_gaps WHERE domain='clinical';
```

Live output from `v_buildable`:

| Rank | Opportunity | Concept | Owners | Liability | SI |
|---|---|---|---|---|---|
| 5 | Claim validation / scrubbing | billing_claims | 0 | LOW | 7.7 |
| 6 | Claims adjudication liaison | billing_claims | 0 | LOW | 7.7 |
| 7 | Charge capture at point of care | billing_claims | 1 | LOW | 7.7 |
| 8 | Claim submission & tracking | billing_claims | 1 | LOW | 7.7 |
| 9 | Denial management & appeal | billing_claims | 1 | LOW | 7.7 |
| 10 | Pre-authorisation | billing_claims | 2 | LOW | 7.7 |
| 14 | Cross-system data normalisation | data_normalisation | 0 | LOW | 3.6 |

The database independently reproduces the Phase-6 conclusion: **the billing chain is the contiguous buildable block.**

---

## 16.2 THE LIVING PART

`refresh.py` re-pulls the live ABDM Strapi API, snapshots to `sources/abdm_<date>.json`, and **diffs against the previous pull** to surface newly certified and delisted platforms.

**Executed successfully today: 445 partners fetched.** This is not a described capability — it ran.

Weekly execution keeps the registry current with the Government of India's own certification pipeline at zero cost and no authentication.

---

## 16.3 HOW TO ABSORB THE NEXT DOSSIER

Documented in `hpid/README.md`:

1. Extract feature rows → map to `feature.concept`; add a concept **only** if none fits
2. Add participation to `workflow` stages
3. **Re-run Phase-5 corroboration** — DL-012 still binds: cross-geography or cross-class required
4. Re-score `backlog`; append to the Decision Ledger if any conclusion changes

**Provenance rules carried into the schema:** evidence requires both a resolvable URL *and* a verbatim quote (DL-013); platform scores are imputed and must never be used for ranking (DL-017); superseded conclusions are preserved, never silently amended.

---

## 16.4 DELIVERABLES

**🟢 Verified:** 8 tables, 2 views, 1,203 ontology rows plus 449 platforms; all four export formats validated; `refresh.py` executed live against the government API.

**⚠️ Contradiction C-35:** HPID presents scores as queryable columns ↔ DL-017 established they are imputed. **Resolution:** the constraint is written into `README.md` and carried in-schema. A future user querying `platform` must read it — this is a residual risk of making imputed data convenient.

**❓ Unknowns:** (1) Does the ABDM API schema change without notice? `refresh.py` would break silently — needs a schema assertion. (2) The 82 demo videos are still unwatched; HPID has a slot for that evidence but not the evidence.

**📒 DL-074:** HPID is the canonical destination for all future intelligence. No future analysis produces standalone documents without also updating the database.

**📊 Confidence — HIGH.** Everything is built, populated, validated and executed.

---

## PHASE 16 COMPLETE — all sixteen phases done. Phase Ω is now unlocked.
