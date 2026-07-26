# PHASE 12 — OVEXIS PRODUCT STRATEGY

**Phase:** 12 of 16 (+ Ω) · **Date:** 2026-07-26 · **Status:** COMPLETE — canonical
**Outputs:** `exports/phase12_strategy.{json,yaml,csv}`

**Binding constraints:** DL-007 (solo builder, no team) · DL-034 (pricing not inheritable) · LAW01–12 (DL-053) · ENG01–12 (DL-054)

---

## THE FIFTEEN RECOMMENDATIONS


### 10-Year Vision

**The execution layer for healthcare operations: the system that completes work other systems only recommend**

- *Basis:* LAW02 + commit gap (4 independent confirmations)
- *Risk:* Category may be absorbed by HMIS vendors if they wake up

### Beachhead Market

**Indian private multi-specialty hospitals, 100-500 beds, ABDM-certified HMIS installed. Entry workflow: OT turnover/scheduling OR claim validation**

- *Basis:* Phase6 T1 robust across all 5 weightings; LAW11 fragmentation; LAW12 NHCX rail live
- *Risk:* Unknown whether HMIS already covers these internally (G-4.2)

### Category Positioning

**NOT an EHR, NOT a copilot, NOT a scribe. "Operational execution agent" - sits beside the HMIS and completes multi-step internal work**

- *Basis:* LAW01 never replace SoR; DL-049 scribe excluded (19 competitors); Phase7 dashboards are legacy
- *Risk:* Category has no existing budget line

### Distribution

**Direct founder-led to 1-3 hospitals; then ABDM-certified HMIS vendors as channel (253 fragmented vendors need differentiation)**

- *Basis:* DL-007 solo; LAW11; HPID gives named targets with contacts
- *Risk:* Long enterprise cycles vs solo runway

### Pricing

**DERIVE FROM FIRST PRINCIPLES - do not inherit. Start: per-completed-workflow outcome pricing (e.g. per validated claim, per theatre turnover saved)**

- *Basis:* DL-034 all 7 pricing patterns failed corroboration; LAW02 value is in completion
- *Risk:* Outcome pricing requires measurement infrastructure Ovexis must build

### Moat

**Adapter coverage x completed-workflow outcome data (R6 flywheel). Neither is buyable; both compound**

- *Basis:* Phase8 R6; LAW02 only completion generates data
- *Risk:* Thin until first workflows complete; no moat at all for 12+ months

### AI Strategy

**Model-agnostic. Local for PHI, cloud for general reasoning. Never train foundation models**

- *Basis:* ENG07; Phase5 arch_llm_wrapper GREEN 18 cos = commodity
- *Risk:* Local model quality ceiling

### Healthcare Strategy

**Stay out of clinical decisions entirely for 24 months. Operational and financial workflows only**

- *Basis:* LAW04 liability bounds automation; Phase6 all clinical opportunities T4-blocked
- *Risk:* Ceiling on TAM; perceived as unambitious

### Technical Strategy

**Stage 0 wiring before features (DL-057). Depth-first adapters. Workflow engine as the core build**

- *Basis:* Phase11 F-11.1 76% unreachable; ENG08, ENG12, DL-059
- *Risk:* Months of invisible work with nothing to demo

### Regulatory Strategy

**Deliberately stay below SaMD threshold. ABDM M1-M3 certification as the credential. DPDP compliance by design**

- *Basis:* LAW04; Phase6 liability tiers; ABDM cert is the recognised trust signal in India
- *Risk:* Regulatory definitions may shift

### Hiring Strategy

**NO HIRES until one workflow completes end-to-end in one hospital. First hire: a hospital operations person, not an engineer**

- *Basis:* DL-007 no team; G-4.2 the pivotal unknown is domain not technical
- *Risk:* Solo capacity limits parallelism

### Capital Allocation

**Zero-capital Stage 0. Any capital raised goes to: (1) one design-partner hospital, (2) ABDM sandbox integration, (3) NOT marketing**

- *Basis:* DL-052 leverage is sequencing not build volume
- *Risk:* No funding data exists for Ovexis (Phase0 unknown)

### Partnership Strategy

**Target the 13 NHA-rated HMIS vendors (govt-published quality scores) as integration partners, not competitors**

- *Basis:* LAW01; HPID govt ratings are a free qualified target list; LAW11
- *Risk:* Vendors may see an agent as a threat to their roadmap

### Platform Strategy

**Adapter SDK only after 10 workflows complete. Platform before product is the 149-adapter mistake repeated**

- *Basis:* Phase8 R6; CB-04
- *Risk:* Slower ecosystem formation

### Global Expansion

**India first, deeply. US entry only via a US-specific rail (clearinghouse partnership), never by porting**

- *Basis:* DL-018, DL-023 one product two substrates; LAW12 US network must be bought
- *Risk:* India-only revenue may cap valuation narrative

---

## 12.1 THE STRATEGY IN ONE PARAGRAPH

Ovexis is the **execution layer for healthcare operations** — the system that *completes* work other systems only recommend. It enters through Indian private hospitals of 100–500 beds, in the operational and financial workflows the HMIS does not own and standards do not reach (OT turnover, bed flow, claim validation). It never touches clinical decisions, never replaces the system of record, and never competes for the scribe market. Its moat is the compounding product of adapter coverage and completed-workflow outcome data — neither purchasable, both requiring completion to exist. It stays below the SaMD threshold deliberately, uses ABDM certification as its trust credential, and hires nobody until one workflow runs end-to-end in one hospital.

---

## 12.2 WHAT THIS STRATEGY REFUSES TO DO

Stated explicitly, because a strategy is defined by its exclusions:

| Refused | Why |
|---|---|
| Build an EHR or HMIS | LAW01, DL-020 — 0 of 19 companies occupy the SoR and all arranged around it |
| Build a dashboard product | LAW10, DL-045 — most crowded concept, pure legacy artifact |
| Compete in ambient scribing | DL-049 — 19 competitors, and it automates a billing artifact not care |
| Sell consumer subscriptions | LAW06, R4 trap — hard ceiling, brutal CAC, blocks institutional revenue |
| Target nursing first | DL-031/DL-042 — largest gap, no digital artifact, no budget authority, highest liability |
| Enter clinical decision support | LAW04 — all clinical opportunities liability-blocked |
| Build a platform/SDK early | Phase-8 R6, CB-04 — platform-before-product is the 149-adapter mistake |
| Inherit a pricing model | DL-034 — all 7 pricing patterns failed corroboration |
| Hire before proof | DL-007 + the pivotal unknown is domain knowledge, not engineering capacity |

---

## 12.3 DELIVERABLES

### ⚠️ Contradictions
| # | Contradiction | Resolution |
|---|---|---|
| C-33 | Q3 mandates both India and US ↔ strategy is India-first | Not a violation. DL-018/DL-023: one product, two substrates. US entry is sequenced later via a US-specific rail, not abandoned |
| C-34 | Moat requires outcome data ↔ no moat exists for 12+ months | Acknowledged and unresolved. This is the strategy's genuine weakness and the primary Phase-13 attack surface |

### ❓ Unknowns
1. **Ovexis has no known capital, runway or traction** (Phase-0 unknown, never closed). Capital allocation advice is therefore conditional.
2. Will Indian hospitals buy operational software from a solo builder with no clinical credentials? No procurement evidence (G-6.4).
3. Do HMIS vendors already cover Tier-1 workflows internally? **Still the pivotal unknown** (G-4.2) — the 82 ABDM demo videos remain unopened.
4. Outcome pricing requires measurement infrastructure that does not exist. Chicken-and-egg unresolved.

### 📒 Decision Ledger
| ID | Decision | Reversible? |
|---|---|---|
| DL-061 | **Beachhead: Indian private hospitals 100–500 beds, ABDM-certified, entry via OT turnover or claim validation** | Yes, on primary evidence |
| DL-062 | **Category: operational execution agent** — explicitly not EHR, copilot, or scribe | Yes |
| DL-063 | **No clinical decisions for 24 months** | Yes, on regulatory capability |
| DL-064 | **No hires until one workflow completes end-to-end**; first hire is hospital-operations, not engineering | Yes |
| DL-065 | **Validate G-4.2 before committing to the beachhead** — watch the 82 ABDM demo videos first | No |

### 📊 Confidence
| Dimension | Score |
|---|---|
| Category positioning | **HIGH** — follows from 12 laws and 4-method commit-gap confirmation |
| Beachhead selection | **MEDIUM-HIGH** — stress-tested (DL-044) but G-4.2 open |
| Pricing | **LOW** — deliberately; no corroborated basis exists |
| Capital allocation | **LOW** — no financial data about Ovexis exists |
| Moat thesis | **MEDIUM** — logically sound, empirically unproven |
| **Overall Phase 12** | **MEDIUM-HIGH** on direction, **LOW** on financials |

---

## PHASE 12 COMPLETE — proceeding to Phase 13 (Red Team).
