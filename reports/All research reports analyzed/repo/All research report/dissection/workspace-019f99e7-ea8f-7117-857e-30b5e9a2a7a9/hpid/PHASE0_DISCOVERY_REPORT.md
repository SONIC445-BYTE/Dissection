# JARVIS / Ovexis — Healthcare Platform Intelligence Database
## Phase 0: Ecosystem Discovery + Phase 1: Prioritisation — India

**Agent:** HPDA (Healthcare Platform Discovery Agent)
**Run date:** 2026-07-25
**Platforms discovered this pass:** **449**
**Target:** 500+ platforms (India), later global
**Status:** Phase 0 complete (first pass) · Phase 1 complete · Phase 2 dossiers PENDING

---

## 0. What was actually built

This is not a market-research document. It is a **populated, queryable registry** plus the
scoring model that decides what JARVIS integrates and in what order.

| Artefact | Path | Rows / Size |
|---|---|---|
| Master registry (JSON) | `registry/platform_registry.json` | 449 platforms, 551 KB |
| Master registry (YAML) | `registry/platform_registry.yaml` | 449 platforms, 451 KB |
| Master registry (CSV) | `registry/platform_registry.csv` | 449 rows, 153 KB |
| **Queryable DB (SQLite)** | `registry/platform_registry.sqlite` | 9 tables + 1 view |
| Raw govt API capture | `sources/abdm_partners_raw.json` | 445 records, unmodified |
| Normalised govt capture | `sources/abdm_norm.json` | 445 records |
| Govt product ratings | `sources/abdm_integrators_clean.json` | 23 records, 16 rated criteria |
| Curated non-ABDM set | `scripts/augment.py` | 40 entries, each source-cited |
| Rebuild pipeline | `scripts/build_registry.py` | idempotent, re-runnable |

Everything is reproducible: re-run `python3 scripts/build_registry.py` to rebuild all four
formats from source captures.

---

## 1. Method — and the single most important finding

### 1.1 The breakthrough: ABDM's partner registry is a live, machine-readable API

`abdm.gov.in/our-partners` renders as a React SPA (no server-side HTML — scraping the page
yields nothing). Reverse-engineering `main.3ae3bb20.js` exposed the Strapi CMS backing it:

```
https://abdm.gov.in/strapicms/api/our-partners?locale=en&populate=*&pagination[pageSize]=100&pagination[page]=N
https://abdm.gov.in/strapicms/api/our-partners-integrators?locale=en&populate=*
```

Unauthenticated, paginated, JSON. **445 government-certified platforms** in five pages.

This matters far beyond convenience. It is the *authoritative* Government of India list of
software that has passed ABDM sandbox certification — meaning every one of these vendors has
**already implemented FHIR R4 and consent-based exchange**. For an integration engine, this is
the highest-signal target list that exists in Indian healthcare, and it can be **re-pulled on a
schedule to keep the registry fresh automatically**. I recommend wiring this into CI as a weekly job.

Per-platform the API also yields:
- **405 signed certification PDFs** (proof of ABDM milestone compliance)
- **19 "Safe-to-Host" / WASA security-audit certificates** — a genuine, hard-to-find security signal
- **82 vendor demo videos** — direct input to Phase 2 UI reverse engineering
- Integration date, expiry date, category, sector, contact person, NHCX sub-type

### 1.2 The second find: the government publishes its own product quality ratings

The `our-partners-integrators` endpoint returns **NHA-assessed product ratings** — 13 platforms
scored 2.5–4.5 against 16 published criteria including *"Ease of data capture by doctor"*,
*"Patient registration"*, *"OP Consultation"*, *"Lab Report"*, *"Billing Module"*, *"Radiology"*,
*"Inventory"*, *"Technical Attributes"*.

These are effectively **free, government-run usability audits of the exact workflows JARVIS must
automate**. Highest rated: Eka Care / Orbi Health (4.5), Drucare (4.5), MocDoc / Yro Systems (4.4),
Plus91 (4.3), HODO (4.1), C-DAC (4.0). These per-criterion scores are captured in
`sources/abdm_integrators_clean.json` and should feed directly into Phase 2 workflow difficulty ratings.

### 1.3 Coverage gap analysis (why the count is 449, not 445)

I programmatically diffed the ABDM registry against a checklist of platforms known from market
sources. ABDM **does not** cover: open-source stacks, global enterprise EHRs, imaging/PACS vendors,
and several large legacy Indian HIS players. Those 40 were added as a cited, curated set with
explicit `VERIFIED` / `INFERRED` confidence flags — never silently merged.

**Source types searched this pass:** ABDM/NHA official APIs and guidance docs, PIB press releases,
C-DAC official pages, Delhi High Court proceedings (NIC e-HMIS), vendor directories
(SoftwareSuggest, TechnologyCounter, Inven, LinkCentre, TradeIndia), Tracxn/YourStory funding data,
Black Book global EHR research, PACS/RIS vendor comparisons, Bahmni/OpenMRS technical docs.

---

## 2. Ecosystem shape (n=449)

**By category** (platforms are multi-category; ABDM's own taxonomy retained):

| Category | Count | JARVIS relevance |
|---|---:|---|
| HMIS | 253 | **Core target.** The main battlefield. |
| Health Tech | 81 | Mixed; mostly point solutions |
| LMIS (lab) | 43 | High value — structured data, high volume |
| Insurance | 37 | Claims automation opportunity |
| NHCX | 29 | Claims exchange, FHIR-native |
| PHR App | 27 | Patient-side, low adapter priority |
| Government Programs | 22 | High strategic weight |
| Health Locker | 20 | Storage layer |
| **Connectors** | 14 | **Disproportionately important — see §5** |
| Pharmacy | 10 | |
| RIS/PACS | 6 | DICOM-automatable |
| EMR | 4 | |
| Imaging AI | 3 | |
| Others / infra | 8 | |

**By sector:** 397 private · 43 government · 4 microsites · 3 open-source · 2 unknown
**By confidence:** 431 VERIFIED · 18 INFERRED
**By tier:** P0 = 15 · P1 = 35 · P2 = 100 · P3 = 299

### The structural insight for JARVIS

The Indian HMIS market is a **massive long tail**: 253 HMIS vendors, of which maybe 15 have
meaningful multi-hospital scale. **A per-vendor adapter strategy does not scale to this market.**

But every one of those 253 is ABDM-certified — which means they all speak the *same* FHIR R4
resources, the same ABHA identity, the same consent flow, the same M1/M2/M3 milestones.

> **Strategic recommendation: JARVIS's primary adapter should target the ABDM protocol layer, not
> individual vendors.** One well-built ABDM/FHIR adapter reaches a certified surface across
> ~250 HMIS platforms. Vendor-specific adapters should then be built only where (a) scale is
> national, or (b) the vendor's proprietary surface unlocks workflows ABDM doesn't model —
> billing, inventory, OT scheduling, nursing notes, queue management.

This inverts the naive "build 500 adapters" plan into "build 1 protocol adapter + ~15 deep
vendor adapters + a long-tail UI-automation fallback."

---

## 3. Scoring model

Ten 0–10 dimensions per platform, all stored in the `score` table:

| Dimension | Derivation |
|---|---|
| `market_importance` | deployment footprint tier × category weight, +1 if ABDM-certified |
| `api_quality` | known programmatic surface; ABDM cert implies ≥5 (FHIR M1–M3 floor) |
| `fhir_readiness` | 8 baseline if ABDM-certified; 10 for national FHIR infra |
| `ui_automation` | web/cloud delivery = more tractable than thick-client/Win32 |
| `security` | +2 if a WASA / Safe-to-Host audit certificate is published |
| `automation_potential` | 0.45·API + 0.35·UI + 0.20·FHIR |
| `integration_difficulty` | inverse of weighted API+FHIR (1 = easy) |
| `maintenance_burden` | rises with footprint (more versions/tenants in the wild) |
| `strategic_importance` | 0.55·market + 0.30·automation + 0.25·govt rating |
| `recommended_priority` | 0.60·strategic + 0.30·market + 0.10·(10 − difficulty) |

Footprint tiers (`NATIONAL/LARGE/MID/SMB/NICHE`) are evidence-backed where cited, `UNKNOWN`
(conservative default 3) otherwise. **This is the model's main weakness and the top fix for
Phase 0b** — 380+ platforms sit at `UNKNOWN` because per-vendor installation counts aren't public.

---

## 4. Phase 1 — Recommended integration order

### Tier P0 — build these first (15)

| # | Platform | Category | Footprint | Pri | Why |
|---|---|---|---|---|---|
| 1 | **ABHA / ABDM core** (HFR, HPR, HIE-CM) | National Infra | NATIONAL | 8.8 | Not a competitor — the *substrate*. FHIR R4, national identity + consent. Reaches ~250 certified HMIS at once. Mandatory for AB-PMJAY hospitals. |
| 2 | **C-DAC** | Connectors/HMIS | NATIONAL | 8.5 | Govt-rated 4.0. Publisher of e-Sushrut, eAushadhi, e-Raktkosh. |
| 3 | **Practo** (healthrx) | HMIS | LARGE | 8.1 | Govt-rated 3.5. Huge clinic + Insta HMS hospital base. |
| 4 | **NIC** | HMIS | NATIONAL | 7.9 | e-Hospital operator across govt hospitals nationally. |
| 5 | **KareXpert** | HMIS | LARGE | 7.5 | Jio/Reliance-funded ($6.99M, Nidhi Jain). Adopted by 13 Indian states. Cloud-native = automation-friendly. |
| 6 | **e-Hospital / NextGen e-HMIS** | HMIS | NATIONAL | 7.4 | 38 Delhi govt hospitals; under Delhi HC supervision. |
| 7 | **e-Sushrut** | HMIS | NATIONAL | 7.4 | **17 AIIMS + 4,000+ facilities.** Maharashtra 847→2,667 facilities. |
| 8 | **HealthPlix** | HMIS | LARGE | 7.4 | Large doctor-side EMR footprint. |
| 9 | **Bahmni** | HMIS | LARGE | 7.4 | **Open source — full source access.** Ideal first adapter to *learn* on. |
| 10 | **OpenMRS** | EMR | LARGE | 7.2 | Bahmni's backend; REST + FHIR modules. |
| 11 | **Medixcel / Plus91** | HMIS | LARGE | 6.7 | Govt-rated 4.3; ABDM *technical integrator*. |
| 12 | **NHCX** | Insurance Exchange | NATIONAL | 6.7 | National claims exchange, FHIR-based. 29 partners live. |
| 13 | **dcm4chee** | RIS/PACS | LARGE | 6.4 | Open-source DICOM archive; scriptable C-FIND/C-MOVE/STOW-RS. |
| 14 | **Attune HIS/LIS** | HMIS | LARGE | 5.9 | Enterprise + diagnostic chains. *(INFERRED footprint)* |
| 15 | **Insta HMS** (Practo) | HMIS | LARGE | 5.9 | Widely deployed private hospital HIS. |

### Suggested build sequence (dependency-aware, not just score order)

1. **Bahmni / OpenMRS first.** Open source means you can read the schema, run it locally, and
   build a full-fidelity test harness with zero vendor cooperation. Every automation primitive
   JARVIS needs — REST, DB, FHIR, DICOM, Atom feeds — can be developed and regression-tested here
   before touching a customer system. *This is the cheapest possible place to make your mistakes.*
2. **ABDM/ABHA core second.** The protocol adapter. Highest leverage per hour in the entire plan.
3. **e-Sushrut + NIC e-Hospital third.** Unlocks the government segment — 17 AIIMS, thousands of
   facilities, and procurement-driven scale.
4. **KareXpert, Practo/Insta, Medixcel fourth.** Cloud-native private sector; good API surface.
5. **dcm4chee / imaging fifth.** Separate protocol domain (DICOM), separate skill set.
6. **Long tail (P2/P3)** via generic ABDM adapter + UI-automation fallback — never bespoke.

### Tier P1 (35) — notable entries
Eka Care/Orbi (4.5★), Drucare (4.5★), MocDoc/Yro (4.4★), Bajaj Finserv Health (4.0★),
Dhanush (4.0★), HODO (4.1★), Healthray (3.6★), NICE-HMS (3.5★), CrelioHealth,
e-Sushrut@Clinic, eAushadhi, Akhil Systems, Amrita Technologies, Aosta, ArguSoft (ABDM connector),
Caresoft, Napier, SoftClinic, Halemind, Ezovion, Drlogy, A-HMIS (AYUSH).

Full ranked list of all 449: `registry/platform_registry.csv`.

---

## 5. Non-obvious findings worth acting on

**a) The "Connectors" category is a shortcut.** 14 platforms exist purely to bolt ABDM compliance
onto HMIS systems that lack it (e.g. ArguSoft's `abdmconnector.argusservices.in`). These are
pre-built bridges into otherwise-closed legacy systems. Partnering with or emulating a connector
may reach more hospitals than a dozen direct adapters.

**b) Every ABDM certification in the registry shows an expiry date, and none extend past
2026-07-25.** Certifications appear to run ~12 months and the published dataset is lagging.
Do **not** treat `abdm_certified` as proof of a currently-live integration — treat it as proof the
vendor *has* built FHIR capability. Re-verify before committing engineering time.

**c) Government deployment ≠ working deployment.** The Delhi High Court ordered NIC to conduct
surprise audits of NextGen e-HMIS across 38 Delhi hospitals in July 2026 after ICU-bed
availability shown on the portal didn't match reality. Real-world data quality in govt HMIS is
uneven — **JARVIS adapters for government systems must assume stale/inconsistent data and
validate defensively.** This is a design requirement, not a footnote.

**d) e-Sushrut@Clinic at ₹299/month is about to create a large, uniform, ABDM-native long tail.**
Government-subsidised, HPR/HFR-gated, targeting PHCs and small clinics. 800+ facilities already.
A single adapter here could eventually reach tens of thousands of small facilities running
*identical* software — a rare thing in this market. Watch this closely.

**e) Only 19 of 449 publish a security audit certificate.** Security posture is largely unverifiable
from public sources. Assume weak transport/credential hygiene in on-prem long-tail deployments.

---

## 6. SQLite schema (built and populated)

```
platform(platform_id PK, rank, tier, name, company, website, sector, country,
         deployment_footprint, source_type, abdm_certified, abdm_id,
         abdm_integrated_date, abdm_expiry, abdm_listings, abdm_mvp_compliant,
         nhcx_type, cert_pdf, security_audit_cert, demo_video,
         govt_product_rating, notes, evidence, confidence, last_verified)
category(platform_id, category)                       -- multi-category
score(platform_id PK, market_importance, automation_potential, api_quality,
      ui_automation, fhir_readiness, security, integration_difficulty,
      maintenance_burden, strategic_importance, recommended_priority)
dossier(platform_id PK, status, path, completed_date, author, revision)   -- Phase 2 tracker
automation_method(platform_id, method, feasible, difficulty, notes)       -- Phase 3
adapter(platform_id PK, priority, est_hours, primary_strategy,
        fallback_strategy, repo_path, feature_flag)                       -- Phase 3
module(platform_id, module, present)                                      -- Phase 2
source(platform_id, url, kind, retrieved)                                 -- provenance
VIEW v_priority                                                           -- ranked worklist
```

Append-only and reusable, as specified. Phase 2/3 tables are pre-created and empty — every
platform already has a `dossier` row with `status='PENDING'`, so the pipeline can be driven by:

```sql
SELECT platform_id, name FROM v_priority
WHERE platform_id IN (SELECT platform_id FROM dossier WHERE status='PENDING')
LIMIT 10;
```

---

## 7. Honest limitations

1. **380+ platforms have `UNKNOWN` footprint.** Installation counts are not public for most Indian
   vendors. Their scores are therefore conservative and their relative ranking within P2/P3 is
   low-confidence. Ranking within **P0/P1 is high-confidence**; below that, treat as a shortlist
   rather than a strict order.
2. **18 entries are `INFERRED`**, mostly legacy/mid-market vendors sourced from review directories
   (which carry SEO/pay-to-list bias). Flagged, never mixed with verified data.
3. **Scoring weights are analyst-set, not empirical.** They encode my judgement about what matters
   for an automation engine. They are one edit away in `build_registry.py` — tune them and rebuild.
4. **No dossiers yet.** Per your Phase 2 spec, each platform gets its own independent document;
   none were written this pass. Deliberate: prioritisation must be right before deep research burns time.
5. **Not yet 500.** 449 discovered. The next pass should reach and exceed 500 — see below.

---

## 8. Next actions

**Phase 0b — close the gap to 500+ (highest value first)**
- State-level HMIS tenders: Tamil Nadu, Kerala (e-Health), Karnataka, Telangana, WB Swasthya Sathi,
  Rajasthan, UP — state procurement portals and eProcure RFPs
- NABH/NABL accredited-facility lists → vendor mentions in case studies
- Blood bank, CSSD, OT, dialysis, oncology, IVF, ophthalmology **single-specialty** systems (thin so far)
- Pharmacy retail chains, ABDM microsites, insurance TPA platforms
- GitHub/StackOverflow mining for Indian HIS integration chatter
- **Wire the ABDM API pull into a weekly CI job** — registry self-refreshes

**Phase 2 — first dossier**
On your go-ahead I'll produce the full HPIA engineering dossier (every section of your original
spec, including screenshots pulled into the workspace and per-workflow automation difficulty
ratings) for the recommended first target: **Bahmni** (open source → fully verifiable, best
learning target) or **ABDM/ABHA core** (highest leverage). My recommendation is **Bahmni first,
ABDM second** — build the muscle on a system you can read the source of.

---

*Provenance: primary sources are the ABDM/NHA partner + integrator APIs (Govt of India), PIB
releases, C-DAC official pages, and court records. Secondary vendor directories are used only for
`INFERRED` entries and are labelled as such. Every record carries `evidence`, `confidence`, and
`last_verified`.*
