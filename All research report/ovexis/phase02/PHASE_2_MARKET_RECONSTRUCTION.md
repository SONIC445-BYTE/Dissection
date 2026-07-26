# PHASE 2 — MARKET RECONSTRUCTION
## The Market as a Structure, Not a List of Companies

**Engagement:** Ovexis / JARVIS Strategic Intelligence Synthesis (OISE)
**Phase:** 2 of 16 (+ Phase Ω)
**Date:** 2026-07-26 (Asia/Calcutta)
**Status:** COMPLETE — canonical
**Inputs:** Phase 0 (canonical), Phase 1 (canonical), live ABDM API probe, HPID registry
**Machine-readable outputs:** `exports/phase2_market_model.{json,yaml}`, `exports/phase2_layers.csv`, `exports/phase2_departments.csv`, `registry/phase2_*.json`

> **Method note.** Company names are deliberately suppressed below. Each of the 21 artifacts is treated as *one observation of a single ecosystem*. Structure was measured — term-density per layer, per department, per interoperability mechanism, per monetisation model, normalised per 1,000 words — not read off from narrative. Where the corpus and primary government data disagree, primary data wins.

---

## 2.0 A CORRECTION AND A CONFIRMATION BEFORE THE ANALYSIS

**Two Phase-1 gaps were closed by direct probe, and one measurement error was caught and fixed.**

### 2.0.1 G-1.4 CLOSED — the ABDM rail is live today 🟢

I called the ABDM Strapi endpoints directly (2026-07-26):

| Endpoint | Result |
|---|---|
| `/strapicms/api/our-partners` | **HTTP 200**, `total: 445`, `pageCount: 89`, unauthenticated |
| `/strapicms/api/our-partners-integrators` | **HTTP 200**, 63,617 bytes, **23 integrator records** with `productRating` |

The live API returns **exactly** the counts I01 recorded a day earlier — 445 partners, 23 rated integrators. Per-record fields confirmed live: `certificate`, `demoVideoUrl`, `NHCXSubCategoryType`, `integrationPublishedDate`, `expiryDate`, `mvpCompliance`, `partner_categories`.

**F-2.1 🟢 Confirmed by primary probe.** The Government of India operates a free, unauthenticated, paginated, machine-readable registry of every FHIR-certified health platform in the country, including signed compliance certificates and demo videos. This is not a research finding; it is **live infrastructure Ovexis can build on this week**.

### 2.0.2 A measurement error, caught and corrected ⚠️

My first interoperability pass reported "HL7v2: 791 hits" — implying HL7v2 dominated the market conversation. I distrusted the magnitude and drilled in. The regex `\borm\b` was matching **"platform", "inform", "transform"**.

Corrected, de-duplicated counts: **HL7v2 = 80**, not 791. A **10× error** that would have inverted a core conclusion about integration mechanics.

Recorded as **DL-016**: *every term-density measurement in this engagement must be spot-checked against verbatim context before it becomes a finding.* Reported here rather than silently fixed, per the engagement's evidence rules.

### 2.0.3 A material caveat on HPID's scores 🔴

Reading `scripts/build_registry.py:112-140`, HPID's per-platform scores are **derived by formula from ABDM certification status**, not measured per platform:

```python
api  = OPEN_API.get(platform_id, 5 if abdm_certified else 2)
fhir = 8 if abdm_certified else OPEN_API.get(platform_id, 2)
web  = 8 if (sector in ("private","open-source") or abdm_certified) else 6
```

Evidence: `score_ui_automation` has **2 distinct values across 449 rows** (442 are `8`); `score_api_quality` has 8 distinct values with 405 rows at exactly `5`; **386 of 449 rows share one identical 5-score signature**.

**F-2.2.** HPID's *inventory* is 🟢 primary-sourced and excellent. HPID's *scores* are 🟡 **imputed priors with a hand-curated override list of ~17 platforms** — genuine analytical judgement, but not per-platform measurement. Any Phase-16 backlog ranking built naively on these columns would be ranking a formula, not the market. Recorded as **DL-017**.

---

## 2.1 THE TWELVE-LAYER MARKET MODEL

Corpus attention measured by term density across all 21 artifacts (de-duplicated):

| Rank | Layer | Attention (hits) | Artifacts engaging | Reading |
|---|---|---|---|---|
| 1 | **AI** | 2,762 | 21/21 | Universal. Every player claims it. |
| 2 | **Hospital** | 1,170 | 19/21 | Discussed constantly — *from outside*. |
| 3 | **Patient** | 1,081 | 19/21 | Crowded consumer surface. |
| 4 | **Workflow** | 1,017 | 20/21 | Named often, owned rarely (§2.4). |
| 5 | **Data** | 704 | 18/21 | FHIR-centric, thin on terminology. |
| 6 | Infrastructure | 593 | 17/21 | Commodity. |
| 7 | Insurance | 590 | 18/21 | Discussed; almost never *built into*. |
| 8 | Identity | 536 | 18/21 | India-led (ABHA), US-fragmented. |
| 9 | Clinical | 491 | 16/21 | Concentrated in 4 knowledge players. |
| 10 | Government | 475 | 16/21 | Structurally decisive, under-weighted. |
| 11 | Decision | 473 | 15/21 | Recommending is common. |
| 12 | **Automation** | **208** | **12/21** | **⬅ The floor of the market.** |

### F-2.3 — The Automation Inversion (the central finding of Phase 2)

**AI attention exceeds automation attention by 13.3×** (2,762 vs 208). Two-thirds of the corpus discusses *models*; barely half meaningfully discusses *doing the work*.

This is not a vocabulary artifact. It is the market's actual shape:

> **The industry has built an enormous capacity to produce recommendations and an almost negligible capacity to execute them.**

Every layer above `automation` generates *outputs a human must then act on*. The corpus's own words confirm the pattern — a clinical-AI player is described as producing *"a clinician-editable draft, not automated order execution"*; another's workflow *"requires clinician review, correction, attribution and EHR sign-off."*

**Strategic consequence for the engagement objective (JARVIS = an execution engine):** JARVIS is not entering a crowded market. It is entering the market's **thinnest layer**, from a repository whose entire existing competence is execution mechanics (ODAV loop, action executor, verification, resolution gate). This is the first strong evidence that the JARVIS-to-healthcare thesis is structurally sound rather than merely ambitious. 🟡 **Strong Inference**, corroborated across artifact classes (dossier corpus + G01 code ground truth), satisfying **DL-012**.

---

## 2.2 MARKET OCCUPANCY — WHO STANDS WHERE

Each artifact's dominant structural position, by normalised density (per 1,000 words):

| Position | Count | Artifacts |
|---|---|---|
| **Sensor** (device/biometric capture) | 6 | D04, D05, D12, D14, D16, D19 |
| **Marketplace** (discovery/transaction) | 6 | D02, D03, D09, D10, D17, I01 |
| **Knowledge corpus** (clinical reference) | 4 | D06, D07, D08, D18 |
| **System of engagement** (front door) | 2 | D01, D15 |
| **Service delivery** (humans in loop) | 2 | D11, D13 |
| **System of intelligence** | 1 | G01 (JARVIS itself) |
| **System of record** | **0** | **— nobody** |

### F-2.4 — Nobody in this corpus owns the system of record

Across 19 competitor dossiers, the maximum `system_of_record` density is **0.14 per 1,000 words** (D12, D19) — statistical noise. The EHR/HMIS is discussed constantly (hospital layer = 1,170 hits, 2nd highest) but **always as a foreign object**: something to integrate with, extract from, or sit beside.

Two readings, and the distinction matters enormously:

- 🟡 **Reading A (structural truth).** The record layer is owned by incumbents outside this corpus (Epic, Cerner/Oracle, Meditech, and in India the 253 HMIS vendors in HPID). Everyone studied here has *organised themselves around* an unmovable centre.
- ⚪ **Reading B (corpus artifact).** Phase 1 F-1.2 established that no EHR incumbent was ever dossiered. Absence of evidence.

**Both are true, and they compound.** The corpus systematically studied the *periphery* of healthcare software while the *centre* went unexamined — and every peripheral player independently organised itself around that unexamined centre. That convergence is itself evidence for Reading A.

**This is the single most important structural fact for Ovexis positioning**, and it directly supports the engagement's own protocol instruction — *"Hospitals rarely replace their core HMIS"* — with measured data rather than assertion.

---

## 2.3 SUPPLY DENSITY — WHAT THE INDIAN MARKET ACTUALLY CONTAINS

From HPID's 449 platforms (inventory 🟢 primary; scores 🟡 imputed per DL-017):

| Category | Platforms | Share |
|---|---|---|
| **HMIS** | **253** | **56%** |
| Health Tech | 81 | 18% |
| LMIS (lab) | 43 | 10% |
| Insurance | 37 | 8% |
| NHCX (claims exchange) | 29 | 6% |
| PHR App | 27 | 6% |
| Government Programs | 22 | 5% |
| Health Locker | 20 | 4% |
| Connectors | 14 | 3% |
| Pharmacy | 10 | 2% |
| **RIS/PACS** | **6** | **1.3%** |
| **EMR** | **4** | **0.9%** |
| **Imaging AI** | **3** | **0.7%** |
| Blood Bank / Pharmacy-SCM / Teleradiology | 1 each | — |

Sector split: **397 private / 43 government / 3 open-source**. Certification: **409 of 449 ABDM-certified**. Tiering: 15 P0 · 35 P1 · 100 P2 · 299 P3.

### F-2.5 — Extreme fragmentation at the record layer

**253 HMIS vendors** hold the position that in the US market is held by roughly five. No single Indian vendor is an Epic-scale monopolist; HPID's own P0 tier mixes government rails (ABDM core, CDAC, NIC, e-Hospital, e-Sushrut) with private platforms (Practo, KareXpert, HealthPlix).

The strategic asymmetry between the two beachheads (both mandated per Q3) is now precise:

| | India | US |
|---|---|---|
| Record layer | **253 HMIS vendors, no monopolist** | ~5 vendors, Epic dominant |
| Integration substrate | **One national rail (ABDM), govt-operated, free API** | TEFCA/QHIN, commercial, fragmented |
| Identity | **ABHA — one national patient ID** | No national ID; MRN reconciliation is a business |
| Barrier to an adapter strategy | **Breadth** (many small targets) | **Depth** (few, fortified targets) |

🟡 **Strong Inference:** an adapter-based execution engine is *structurally favoured in India and structurally disfavoured in the US*. In India, ABDM certification means 409 platforms already speak FHIR R4 — the adapter problem is *many shallow integrations over a common substrate*. In the US, the same strategy requires penetrating a handful of deeply defended systems whose vendors control app-store gatekeeping.

**This does not contradict Q3 (both markets).** It sequences them. Recorded as **DL-018**.

### F-2.6 — The government publishes free usability audits of the exact workflows JARVIS must automate

13 platforms carry NHA `productRating` scores (2.5–4.5) across 16 published criteria including *"Ease of data capture by doctor"*, *"Patient registration"*, *"OP Consultation"*, *"Lab Report"*, *"Billing Module"*, *"Radiology"*, *"Inventory"*. Verified live in the integrator endpoint today.

No competitor in this corpus is using this. 🟡 **Strong Inference** — it is an unexploited public asset for target prioritisation.

---

## 2.4 THE FLOWS

### 2.4.1 How money flows

| Model | Signal | Carried by | Structural reading |
|---|---|---|---|
| **Diagnostics/testing** | 547 | 13 | The revenue engine behind "prevention" |
| **Hardware** | 460 | 8 | Sensor layer's entry toll |
| **B2C subscription** | 453 | **19/21 — universal** | Default monetisation |
| **B2B enterprise** | 253 | 9 | Where contract value concentrates |
| **Payer/reimbursement** | 251 | **19/21 — universal** | Discussed everywhere, *earned* almost nowhere |
| B2B2C (employer) | 179 | 14 | The escape hatch from consumer CAC |
| Data monetisation (RWD/RWE) | 86 | 7 | Quiet, high-margin |
| Transaction/marketplace | 64 | 3 | India-concentrated |
| Ads/lead-gen | 17 | 2 | Marginal |

**F-2.7 — The reimbursement paradox.** Payer/reimbursement appears in **19 of 21 artifacts** yet ranks 5th by intensity, while B2C subscription (also 19/21) ranks 3rd with 1.8× the density. Nearly every player *discusses* getting paid by the health system; nearly every player *actually* gets paid by the consumer's credit card.

🟡 **Strong Inference:** consumer subscription is not these companies' chosen destination — it is the **fallback taken because payer/provider revenue is unreachable without clinical validation, procurement cycles, and reimbursement codes**. The corpus corroborates: *"Zero switching cost at signup, annual renewal decision points, price transparency across competitors, and a category conditioned to discount"*, and one dossier's blunt prediction that *"the US never exceeds $10–20M ARR because CAC is brutal, brand is absent, and B2B is compliance-blocked."*

**Consequence:** the consumer-subscription layer is a **revenue trap with a hard ceiling**, not a beachhead. Any Ovexis plan that begins with consumer subscriptions inherits that ceiling.

### 2.4.2 How information flows

| Mechanism | Signal | Artifacts | Reading |
|---|---|---|---|
| **FHIR** | **525** | **20/21** | The declared universal substrate |
| Device SDK (HealthKit/Health Connect/BLE) | 325 | 16 | Consumer data's real path |
| Epic-specific | 175 | 7 | One vendor is its own protocol |
| **ABDM rails** | **151** | **14** | India's national substrate |
| Terminology (SNOMED/LOINC/ICD/RxNorm/CPT) | 110 | 8 | **⚠ Thin** |
| HL7v2 | 80 | 11 | *(corrected from 791 — see §2.0.2)* |
| Cerner/Oracle | 66 | 4 | |
| HIE/TEFCA/QHIN | 48 | 3 | US network layer, barely discussed |
| SMART-on-FHIR / CDS Hooks | 38 | 5 | **⚠ The actual clinical-app entry point, near-ignored** |
| Manual/fax/paper | 24 | 3 | Honest admissions |
| "No public API" | 23 | 3 | |
| **Screen/UI automation** | **13** | **2 (one is JARVIS)** | **⬅ Effectively unclaimed** |

**F-2.8 — FHIR is the declared standard; it is not the working one.** FHIR outscores terminology 4.8:1 (525 vs 110). Systems agree on *envelopes* while under-investing in *meaning* — a FHIR `Observation` whose code isn't LOINC-mapped is transport without semantics. 🟡 Strong Inference: the interoperability layer is **syntactically solved and semantically unsolved**. That gap is where an execution engine must live, because acting on data requires meaning, not just structure.

**F-2.9 — UI automation is the least-claimed mechanism in the entire market.** 13 mentions across 21 artifacts, and **one of those two carriers is JARVIS itself**. Meanwhile HPID's own (imputed) model rates UI-automation feasibility at 8/10 for 442 of 449 platforms while API quality sits at 4.88/10 mean.

Even discounting the imputation (DL-017), the *qualitative* asymmetry holds and is independently corroborated: 253 fragmented HMIS vendors cannot all expose good APIs; 3 mentions of "no public API"; RIS/PACS and Imaging AI score lowest on API quality (3.2 and 2.0).

> **This is the whitespace the entire Phase 6 hunt will return to.** The market has agreed that integration means APIs. The majority of the installed base cannot offer them. Nobody is systematically automating the interface layer that every one of those systems *does* have — the screen a human already uses.

### 2.4.3 How authority flows

Veto-actor mentions across the corpus: **CIO 13 · CFO 9 · committee 8 · compliance officer 2 · CNO 1 · CMIO 1.**

**F-2.10 — Authority is measured almost exclusively in *financial and technical* veto, not clinical veto.** The CMIO — the clinical-informatics officer who decides whether a tool is safe and usable at the bedside — appears **once**. This is a corpus blind spot with direct engineering consequence: the artifacts model buying as an IT/finance decision, when adoption is a clinical one.

The corpus itself supplies the counter-evidence, from G01's panel: *"The CMIO requires evidence that software improves clinical outcomes, reduces documentation burden, or enhances decision support"*, and *"Physicians need tools that save time without compromising clinical accuracy or liability."*

Authority chain as reconstructed:
```
Government (mandate: ABDM cert / info-blocking) 
   → sets the floor of what is permissible
CIO + Compliance (veto: security, integration, BAA/DPDP)
   → gates entry
CFO / committee (veto: budget, ROI)
   → gates scale
CMIO / clinical council (veto: safety, workflow fit)
   → gates ADOPTION  ⬅ under-measured by the corpus, decisive in practice
Clinician (silent veto: doesn't use it)
   → determines actual value realised
```
🟡 Strong Inference: **every layer above the clinician can approve a purchase; only the clinician can create value.** Procurement is necessary and insufficient.

### 2.4.4 How trust flows

Trust-mechanism signals: **provenance 55 · citation 55 · editorial 50 · source-linked 2 · peer-review 1.**

**F-2.11 — Trust is manufactured through traceability, not accuracy claims.** The three dominant mechanisms are all forms of *showing your work*. The corpus is explicit: *"every score should be explainable down to biomarkers, ranges, source lab, date, trend, and guideline"*; *"Treat compliance as product: consent ledger, audit logs, source provenance, deletion, BAAs/DPDP, and signed webhooks."*

Note the structural rhyme with §1.4.4: JARVIS's `resolution_gate.py` — *"I don't know how to control [platform] yet"* — is the **execution-layer equivalent of a citation**. Honest failure is provenance for actions. This is not an analogy; it is the same trust primitive applied to a different layer. It substantially raises my confidence that the protected asset identified in DL-011 is strategically central rather than merely tidy engineering.

### 2.4.5 How decisions flow — and where they stop

The corpus's own admissions of where software hands back to humans (28 unique statements):

- *"no structured clinical summary, no C-CDA export, no fax/direct messaging — the classic coordination primitives are absent"*
- *"A safe clinical workflow requires clinician review, correction, attribution and EHR sign-off"*
- *"positioned as a clinician-editable draft, not automated order execution"*
- *"the AI drafts, the coach sends"*
- *"laborious manual chart review"* (three independent artifacts)
- *"Confirmation unreliability — 'confirmed' appointments not communicated to clinic; patient travels, doctor absent"*
- *"Everything that would require persistent patient state … is architecturally absent"*
- *"Referral mechanics absent"* · *"closed-loop referrals, handoff receipt, tasks, results, escalation and care-team roles"* — listed as *missing*

**F-2.12 — The decision flow terminates at the same point in every artifact: the moment an action must be committed to a system of record.** Draft, don't send. Suggest, don't order. Recommend, don't book. This is the **automation inversion (F-2.3) expressed as workflow**, and it recurs across artifact classes.

**And it is precisely the pattern JARVIS's own self-audit found in its own code** (Phase 1, F-1.5): *"the first step of a multi-step action is consistently real; the last step (click Send/Post/Play) is consistently missing."*

> The healthcare software industry and the JARVIS repository have **independently converged on the same failure mode**: everything up to the commit step, nothing at the commit step. One found it in 149 fabricated adapters; the other lives it across a $B market. This is the strongest cross-class corroboration in the engagement so far — dossier corpus + primary code, satisfying DL-012 by a wide margin.

---

## 2.5 DEPARTMENTAL COVERAGE — WHERE THE MARKET LOOKS AND WHERE IT DOESN'T

| Department | Corpus hits | Artifacts covering |
|---|---|---|
| Radiology | 234 | 16 |
| Quality/compliance | 210 | 18 |
| Billing/RCM | 190 | 9 |
| Admin/management | 141 | 15 |
| IPD/ward | 107 | 15 |
| Emergency | 103 | 16 |
| Reception/front desk | 80 | 14 |
| Discharge/follow-up | 56 | 11 |
| **Laboratory** | **27** | **6** |
| **Pharmacy** | **27** | **5** |
| **Nursing** | **10** | **2** |
| **OPD consult** | **8** | **2** |
| **ICU** | **4** | **1** |
| **Insurance pre-auth** | **4** | **1** |
| **OT / surgery** | **2** | **1** |

### F-2.13 — The market ignores the departments where the work happens

**Nursing: 10 mentions across 21 artifacts.** Nurses are the largest clinical workforce in any hospital and the highest-volume documenters. **OT/surgery: 2. ICU: 4. Pre-auth: 4. OPD consult: 8.**

Meanwhile radiology (234) and quality/compliance (210) — the two most *digitised and image-centric* domains — dominate attention.

🟡 **Strong Inference: attention tracks data availability, not labour intensity.** Radiology produces clean digital artifacts that models can consume, so it attracts AI attention. Nursing produces continuous, messy, interstitial work that no model can currently consume — so the market looks away.

This inverts the standard whitespace narrative. The gap is not "an unserved *market*"; it is **unserved *work***, exactly as the Phase 6 brief will demand ("what important healthcare work still requires humans because software has failed?"). Phase 2 flags the leading candidates now: **nursing documentation, OT scheduling and turnover, ICU coordination, pre-authorisation, OPD consultation flow.**

Note also **billing/RCM: 190 hits but only 9 artifacts** — high intensity, narrow coverage. Money-adjacent workflows are studied deeply by the few who touch them and ignored by everyone else. In India, NHCX (29 platforms) makes claims a *national rail* problem, not a per-hospital one — a structural opening.

---

## 2.6 THE RECONSTRUCTED MARKET — SYNTHESIS

```
   GOVERNMENT LAYER  ── sets the floor ──────────────────────────────────
   India: ABDM/ABHA/HFR/HPR/NHCX — one national rail, free live API,
          409/449 platforms certified FHIR R4, govt-published usability ratings
   US:    ONC info-blocking, TEFCA/QHIN — commercial, fragmented, barely
          discussed in corpus (48 hits, 3 artifacts)
                                  │
   ┌──────────────────────────────┼──────────────────────────────┐
   │                    THE UNEXAMINED CENTRE                     │
   │   SYSTEM OF RECORD — HMIS / EMR / EHR                        │
   │   India: 253 HMIS vendors, no monopolist, mean API q ~5      │
   │   US:    ~5 vendors, one dominant, its own protocol (175)    │
   │   ▸ Occupied by 0 of 19 studied companies                    │
   │   ▸ Rarely replaced; always integrated-around                │
   └──────────────────────────────┼──────────────────────────────┘
                                  │
   ── everyone in this corpus arranged themselves around it ──
                                  │
   SENSOR (6)         MARKETPLACE (6)      KNOWLEDGE (4)
   biometric capture  discovery/txn        clinical reference
   hardware+subs      commission           editorial+citation
        │                   │                    │
        └───────────────────┼────────────────────┘
                            │
   DATA LAYER — FHIR 525 : terminology 110 (4.8:1)
   syntactically solved, semantically unsolved
                            │
   AI LAYER — 2,762 hits, universal, undifferentiated
                            │
   DECISION LAYER — 473 hits: recommendations produced
                            │
              ╔═════════════▼═════════════╗
              ║   THE COMMIT GAP          ║
              ║   draft ≠ sent            ║
              ║   suggest ≠ ordered       ║
              ║   recommend ≠ booked      ║
              ╚═════════════┬═════════════╝
                            │
   AUTOMATION LAYER — 208 hits (13.3× less than AI)
   UI automation: 13 hits, 2 artifacts, one is JARVIS
                            │
   ── work falls through to humans ──
                            │
   NURSING (10) · OT (2) · ICU (4) · PRE-AUTH (4) · OPD (8)
   the departments where labour actually is
```

**The market in one sentence:** *A crowded periphery of sensors, marketplaces and knowledge corpora produces an ever-increasing volume of recommendations that terminate at a commit gap, beyond which under-studied human labour — nursing, theatre, ICU, pre-authorisation — absorbs the cost.*

---

## 2.7 END-OF-PHASE DELIVERABLES — PHASE 2

### ✅ Completed
- Twelve-layer market model built from measured term density across all 21 artifacts (de-duplicated).
- Market occupancy grid: every artifact's structural position, normalised per 1,000 words.
- Supply-density map of India's certified universe (449 platforms, 19 categories) from primary government data.
- Five flow reconstructions: money, information, authority, trust, decisions.
- Departmental coverage map across 15 hospital functions.
- **Live probe of ABDM API** — Phase-1 gap G-1.4 closed.
- **HPID scoring methodology audited** — imputation discovered and quantified.
- One 10× measurement error caught, corrected and disclosed.

### 🟢 Verified Facts
| # | Fact | Evidence |
|---|---|---|
| VF-19 | ABDM partner API live, HTTP 200, `total: 445`, unauthenticated, 89 pages | Direct probe 2026-07-26 |
| VF-20 | ABDM integrator API live, 23 records with `productRating` (e.g. `"4.1"`) | Direct probe |
| VF-21 | India's certified universe: 253 HMIS, 81 HealthTech, 43 LMIS, 37 Insurance, 29 NHCX, **6 RIS/PACS, 4 EMR, 3 Imaging AI** | HPID CSV, 449 rows |
| VF-22 | 409/449 ABDM-certified; 397 private / 43 govt / 3 open-source | HPID CSV |
| VF-23 | Corpus attention: AI 2,762 vs automation 208 = **13.3× inversion** | Measured, de-duplicated |
| VF-24 | **0 of 19** competitor dossiers occupy system-of-record (max density 0.14/1k words) | Position grid |
| VF-25 | FHIR 525 vs terminology 110 = **4.8:1** | Corrected measurement |
| VF-26 | UI/screen automation: **13 hits, 2 artifacts**, one being JARVIS | Corrected measurement |
| VF-27 | Nursing 10 · OT 2 · ICU 4 · pre-auth 4 · OPD 8 hits corpus-wide | Department map |
| VF-28 | Veto actors: CIO 13, CFO 9, committee 8, **CMIO 1** | Verbatim extraction |
| VF-29 | Trust mechanisms: provenance 55, citation 55, editorial 50 | Verbatim extraction |
| VF-30 | HPID `score_ui_automation` has **2 distinct values across 449 rows**; 386 rows share one 5-score signature | Distribution analysis |

### 🔵 Code-Backed
| # | Fact | Evidence |
|---|---|---|
| CB-10 | HPID scores are formula-derived from `abdm_certified` + a 17-entry `OPEN_API` override dict, not per-platform measurement | `scripts/build_registry.py:112-140` |
| CB-11 | HPID SQLite ships 8 tables + `v_priority` view, already modelling `dossier`, `adapter`, `automation_method`, `module` — Phase-16 schema partly pre-built | `platform_registry.sqlite` |

### 📄 Supported by Documentation Only
- HPID's claim of *"405 signed certification PDFs"* and *"82 vendor demo videos"* — the `certificate`/`demoVideoUrl` fields are confirmed present in the live API, but the artifacts themselves were not downloaded or opened in this phase.
- The 16 NHA rating criteria are described in HPID's Phase-0 report; the live endpoint returns `productRating` as a flat string (`"4.1"`), so **per-criterion breakdown is documented but not yet re-verified from primary source**.

### 🧠 Architectural Inferences
| # | Inference | Justification |
|---|---|---|
| AI-09 | The market is **syntactically interoperable and semantically fragmented** — an execution engine must own terminology mapping, because acting requires meaning | FHIR:terminology 4.8:1 |
| AI-10 | India favours a **breadth-adapter** strategy (many shallow, one substrate); US favours **depth-integration** (few, fortified). Same product, inverted go-to-market | 253 vs ~5 record vendors; ABDM free rail vs commercial TEFCA |
| AI-11 | Consumer subscription is a **fallback with a hard ceiling**, not a beachhead — reached because payer/provider revenue is blocked | 19/21 discuss reimbursement; subscription 1.8× denser; corpus's own ARR-ceiling prediction |
| AI-12 | **Attention tracks data availability, not labour intensity** — hence radiology 234 vs nursing 10 | Department map |
| AI-13 | Honest-failure (resolution gate) is the **execution-layer analogue of citation** — the same trust primitive one layer down | Trust mechanisms all traceability-based; CB-05 |
| AI-14 | The commit gap is a **market-wide structural failure**, not a per-company deficiency, because it recurs in 100% of artifacts that reach the action step | F-2.12 |

### 🔴 Speculation
- The commit gap may persist because **liability, not capability**, blocks it — nobody wants to own an autonomous clinical action. Testable; would reframe the whole opportunity as a *governance* problem rather than an engineering one. **Flagged for Phase 7 and Phase 13; not load-bearing.**
- India's ABDM rail may make it the first market where autonomous clinical execution is *legally* tractable at scale (consent artefacts + national identity + certified endpoints). Highly speculative.

### ❓ Unknowns
1. Who actually owns the record layer in India by *installed base* (not vendor count)? HPID counts vendors, not deployments.
2. Are the 405 certification PDFs and 82 demo videos retrievable, and do the videos show real workflow UI? (Direct Phase-3/16 input.)
3. Does NHA's per-criterion rating breakdown survive in the live API, or only the flat score?
4. What is the real API quality of the top 20 Indian HMIS platforms? **Every current number is imputed (DL-017).** This is now the highest-value unknown in the engagement.
5. US-side: does the commit gap close inside Epic's own ecosystem (their protocol, their sandbox)? No dossier exists.
6. What does a completed clinical action actually cost in liability terms? Unmeasured anywhere.

### ⚠️ Contradictions
| # | Contradiction | Resolution |
|---|---|---|
| C-10 | HPID presented as a scored prioritisation engine ↔ scores are largely imputed constants | Inventory 🟢 trustworthy; scores 🟡 priors. Use HPID for *targeting*, not for *ranking*, until measured. **DL-017** |
| C-11 | Corpus treats FHIR as solving interoperability ↔ terminology investment is 4.8× lower | Both true. FHIR solves transport; meaning is unsolved. Not a contradiction in fact, but in *emphasis* |
| C-12 | Corpus models buying as CIO/CFO decision (22 mentions) ↔ its own G01 panel says CMIO/clinician determines adoption (1 mention) | Both true at different stages. Purchase ≠ adoption. Corpus systematically under-weights the adoption veto |
| C-13 | My own first interop measurement (HL7v2 = 791) ↔ corrected value (80) | **My error, disclosed.** Corrected value canonical. **DL-016** |

### 🕳️ Research Gaps
- **Carried:** no EHR-incumbent dossier; no payer dossier; no primary clinician/CIO research; 62 screenshots + 67 raw captures still unread; no dedicated regulatory dossier.
- **New G-2.1:** No installed-base data for Indian HMIS — vendor count ≠ market share.
- **New G-2.2:** API quality of major HMIS platforms is **entirely unmeasured**; 405 certification PDFs unopened.
- **New G-2.3:** US commit gap inside Epic's ecosystem unexamined.
- **New G-2.4:** Nursing, OT, ICU, pre-auth, OPD are the identified opportunity zones and have **almost zero corpus evidence** — Phase 6 will have to reason with little support.
- **New G-2.5:** No liability/medico-legal cost data for autonomous action anywhere in the corpus.

### 📒 Decision Ledger — Phase 2
| ID | Decision | Rationale | Reversible? |
|---|---|---|---|
| DL-016 | Every term-density measurement must be verbatim-spot-checked before becoming a finding | The `\borm\b` 10× error (F-2.0.2) | No |
| DL-017 | **HPID scores are 🟡 imputed priors, not measurements.** Use HPID for targeting; do not rank a backlog on its score columns until measured | `build_registry.py:112-140`; 386/449 identical signatures | Yes — on real measurement |
| DL-018 | **India-first sequencing within a both-markets mandate.** Structural fit favours India for an adapter/execution engine; US remains a target, entered later or via a different mechanism | 253 vs ~5 record vendors; free national FHIR rail; ABHA identity | Yes |
| DL-019 | **The commit gap is the canonical market frame for all later phases.** Phases 4, 6, 7, 11 must locate every opportunity relative to it | F-2.3 + F-2.12, corroborated across artifact classes |No |
| DL-020 | System-of-record is **out of scope as a build target** and **in scope as an integration target**. Ovexis does not attempt to replace the HMIS | 0/19 occupancy; corpus-wide integrate-around behaviour | Yes, but reversal requires extraordinary evidence |
| DL-021 | Under-studied departments (nursing, OT, ICU, pre-auth, OPD) are **elevated to primary Phase-6 candidates** despite thin corpus evidence, precisely because thin evidence is the signal | F-2.13 | No |

### 📊 Confidence Score — Phase 2

| Dimension | Score | Justification |
|---|---|---|
| Market layer structure | **HIGH** | Measured across 21 artifacts, de-duplicated, spot-checked after DL-016 |
| India supply density | **HIGH** | Primary government data, live-probe verified twice |
| Occupancy / system-of-record absence | **MEDIUM-HIGH** | Strong measurement, but partly a known corpus blind spot (F-1.2) |
| Money-flow reconstruction | **MEDIUM-HIGH** | Consistent across 19 artifacts; single-pipeline correlation still applies |
| Interoperability mechanics | **MEDIUM** | Corrected after a 10× error; term density ≠ deployment reality |
| Authority flow | **MEDIUM-LOW** | Derived from a corpus that under-samples clinical veto; no primary research |
| Departmental map | **MEDIUM** | Reliable as a map of *corpus attention*; only 🟡 as a map of *market reality* |
| **Overall Phase 2** | **MEDIUM-HIGH** | Structure is well-evidenced and cross-corroborated; magnitudes inherit Phase-1's evidence ceiling |

---

## 2.8 THE THREE THINGS PHASE 2 CHANGES

1. **The market's thinnest layer is the one JARVIS is built for.** AI attention exceeds automation attention 13.3×; UI automation is claimed by 2 artifacts, one of which is JARVIS. The thesis is structurally sound, not aspirational.
2. **The commit gap is the market's defining failure — and JARVIS's own codebase independently reproduced it.** Draft-not-send in healthcare; navigate-not-click in 149 adapters. One frame now explains both the market opportunity and the repo's technical debt. *(DL-019)*
3. **India and the US are structurally inverted for this product.** 253 fragmented record vendors over one free national FHIR rail vs ~5 fortified vendors over commercial networks. Both remain in scope per Q3; sequencing is now evidence-based rather than preferential. *(DL-018)*

---

## PHASE 2 COMPLETE

Machine-readable outputs:
- `ovexis/exports/phase2_market_model.{json,yaml}` — 12 layers, 21 occupancy records, 15 departments, 2 flow tables (`ovexis.hpid.phase2.market_model/v1`)
- `ovexis/exports/phase2_layers.csv`, `ovexis/exports/phase2_departments.csv`
- `ovexis/registry/phase2_{layer,money,interop,dept,position}_signals.json`, `phase2_quotes.json`, `phase2_human_required.json`

Stopping here as instructed. Phase 3 (Product DNA Extraction — Master Product Genome from ~1,277 pre-extracted feature rows) awaits `Continue`.
