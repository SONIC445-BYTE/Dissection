# HPID — Healthcare Platform Intelligence Database
Living intelligence asset. Extends the Phase-0 449-platform registry (DL-002 — extend, never rebuild).

## Query
    sqlite3 hpid.sqlite "SELECT * FROM v_buildable;"
    sqlite3 hpid.sqlite "SELECT * FROM v_gaps WHERE domain='clinical';"

## Tables
| Table | Rows | Content |
|---|---|---|
| feature | 55 | canonical feature ontology, deduplicated from 1,277 rows |
| workflow | 84 | workflow ontology: patient/clinical/financial/administrative |
| integration | 562 | platform ↔ category ↔ protocol ↔ automation method |
| concept | 26 | FHIR resources, ABDM entities, departments, modules |
| backlog | 15 | prioritised JARVIS adapter backlog |
| platform | 449 | government-sourced platform registry |
| market_law | 12 | Phase-9 laws with evidence |
| engineering_law | 12 | Phase-10 laws with tradeoffs and failure cases |

## Views
- `v_buildable` — READY backlog items joined to feature scores
- `v_gaps` — TRUE_GAP and UNOWNED workflow stages by domain

## Refresh (weekly)
    python3 refresh.py
Re-pulls the live ABDM Strapi API, snapshots to `sources/abdm_<date>.json`, and diffs
against the previous pull to surface newly certified and delisted platforms.

## Absorbing a new competitor dossier
1. Extract feature rows → map to `feature.concept` (add a concept only if no existing one fits)
2. Add participation to `workflow` stages
3. Re-run Phase-5 corroboration (DL-012: cross-geography or cross-class required)
4. Re-score `backlog`; append to the Decision Ledger if a conclusion changes

## Provenance rules
- Evidence requires BOTH a resolvable URL and a verbatim quote (DL-013)
- HPID platform scores are IMPUTED, not measured (DL-017) — use for targeting, never ranking
- Preserve superseded conclusions; never silently amend (engagement protocol)
