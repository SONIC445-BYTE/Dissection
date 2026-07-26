# Healthcare Platform Intelligence Database — JARVIS / Ovexis

Pipeline: **HPDA (discovery) → HPIA (dossiers) → Adapter Architect**

| Phase | Status | Output |
|---|---|---|
| 0 — Ecosystem discovery | ✅ pass 1 (449 platforms) | `registry/*` |
| 1 — Prioritisation | ✅ complete | `PHASE0_DISCOVERY_REPORT.md` §4 |
| 2 — Per-platform dossiers | ⏳ 0/449 (`dossier.status='PENDING'`) | `dossiers/` |
| 3 — Adapter architecture | ⏳ pending | `dossiers/*/adapter/` |
| 4 — Machine-readable registry | ✅ JSON+YAML+CSV+SQLite | `registry/` |

## Read this first
`PHASE0_DISCOVERY_REPORT.md`

## Rebuild
    python3 scripts/build_registry.py     # idempotent

## Query
    sqlite3 registry/platform_registry.sqlite "SELECT * FROM v_priority LIMIT 15;"

## Layout
    registry/    platform_registry.{json,yaml,csv,sqlite}
    sources/     raw + normalised API captures (provenance)
    scripts/     augment.py (curated non-ABDM set), build_registry.py
    dossiers/    Phase 2 output (empty)
    screenshots/ Phase 2 UI captures (empty)

## Key data source (reusable, unauthenticated, weekly-refreshable)
    https://abdm.gov.in/strapicms/api/our-partners?locale=en&populate=*&pagination[pageSize]=100&pagination[page]=N
    https://abdm.gov.in/strapicms/api/our-partners-integrators?locale=en&populate=*
