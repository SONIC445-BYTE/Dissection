# DELIVERABLE 4 — Product Reverse Engineering

Confidence legend: 🟢 Confirmed | 🟡 Strong Inference | 🔴 Speculation | ⚪ Cannot Verify

This file reconstructs the product surface from: the live login/store pages, App Store/Play listings, WK/UpToDate official product pages (editorial, mobile, integrations), user reports, and job posts. Where a surface is inferred, it is labelled.

---

## 4.0 Product map (verified surfaces)

```
UpToDate (web app · iOS · Android · EHR-embedded)
├── Core Reference Engine
│   ├── Global search (autocomplete, typo-tolerant)
│   ├── Topic pages (Summary & Recommendations → sections → references)
│   ├── GRADED recommendations (1A–2C)
│   ├── "What's New" + "Practice Changing UpDates"
│   ├── Key Points panels (search-result level)
│   ├── Graphics / algorithms / videos
│   ├── 200+ medical calculators
│   ├── Drug info (Lexidrug monographs, interactions analyser,
│   │   Rx Transitions antidepressant-switching tool, Kidney dosing)
│   └── Patient education ("The Basics" / "Beyond the Basics", ≤19 languages)
├── UpToDate Expert AI (2025–) ── conversational CDS agent
│   ├── Chat interface over the corpus (RAG + guardrails)
│   ├── One-click: Assumptions · Sources · Reasoning steps
│   ├── Lexidrug knowledge carousels (Nov 2025)
│   └── Enterprise admin/governance console
├── Personal layer
│   ├── Account/SSO (Microsoft, OpenAthens, institutional SSO)
│   ├── CME tracker (auto-logged reading → AMA PRA credit redemption)
│   ├── Search history
│   └── Settings (devices, renewal, 2-device mobile policy)
├── Institutional layer
│   ├── IP/range + SSO referral ("Continue without signing in")
│   ├── UpToDate Anywhere (registration + CME at institutions)
│   ├── Usage reporting for admins
│   └── EHR integration kit (Epic/Oracle Health/InterSystems Infobutton)
└── Portfolio adjacencies
    ├── UpToDate Lexidrug (standalone pharmacist app)
    ├── Medi-Span (API-level drug data in EHR/pharmacy systems)
    ├── Emmi (patient engagement programs)
    └── Sentri7 (hospital surveillance)
```

---

## 4.1 Core reference engine — feature by feature

### 4.1.1 Global search
- 🟢 Persistent search bar on every page; autocomplete with topic/drug/calculator/patient-ed entity recognition; tolerant of misspellings ("ACE inhibitors" → drug-class page).
- 🟢 Concurrent session model: searches from EHR Infobutton land pre-populated.
- 🟡 Relevance is editorial-weighted (KOL-maintained synopses rank above raw journal references); search covers corpus + drug monographs + graphics + calculators + patient leaflets, segmented by tabs/filters.
- 🟡 Search is the *prime data asset*: query logs feed "What's New" prioritisation and editorial gap analysis (new topics are commissioned partly from search-failure analytics — editorial policy acknowledges user feedback loop; the analytics depth is inference).
- 🔴 Likely technical basis: WK jobs reference **OpenSearch / Azure AI Search** for the GenAI platform; the classic topic search may still run on a legacy index unreplaced — treat with caution.

### 4.1.2 Topic page anatomy
🟢 Confirmed structure (editorial policy + app listing + user descriptions):
1. Author + section editor names and affiliations (accountable authorship) top-left.
2. **"Summary and Recommendations"** — the answer-first block: bullet recommendations with **GRADE badges (1A…2C)**.
3. Numbered sections (epidemiology → pathophysiology → diagnosis → management → prognosis), each with inline numbered citations.
4. Tables/graphics expandable; "related topics" sidebar links.
5. **References** list showing abstracts; some open-access links.
6. Disclosure statement; "last updated" date per section; contributor history (replaced authors acknowledged ≥1 year — confirmed in editorial policy).
- 🟡 Answer-first inverted-pyramid design is the product's soul: content is engineered so that *the first screen answers JTBD #1 in under 2 minutes*. Everything below the fold is for verification, teaching, or depth.

### 4.1.3 GRADE recommendation chips
🟢 Every major recommendation carries strength (1=strong, 2=weak) × quality (A/B/C) — unique among point-of-care tools per WK FAQ: "UpToDate does both [grades evidence and recommendations], which makes it unique." 🟡 For Ovexis: this is a *credential artefact* — the badge is what makes the content screenshot-able into clinical notes and litigation-defensible.

### 4.1.4 What's New / Practice Changing UpDates
🟢 Editorial radar: high-impact updates piped into a dedicated feed per specialty; "Practice Changing UpDates" consolidates paradigm shifts. 🟡 Functions as the retention push channel in web+app+email; existence confirmed, churn-causation inferred.

### 4.1.5 Key Points panels
🟢 Search-result-level micro-summaries designed to "avoid diagnostic and treatment errors" (App Store copy, 2026) — the zero-click answer, competitors' featured-snippet equivalent inside the walled garden.

### 4.1.6 Calculators (200+)
🟢 Dose, risk-score, unit-conversion tools embedded in topics and searchable directly. 🟡 Strategically defensive against MDCalc (3.6M visits/3mo competitor benchmark) — keeps clinicians from leaving the garden.

### 4.1.7 Drug layer (Lexidrug inside UpToDate)
🟢 Monographs, interaction analysis tool, Rx Transitions (antidepressant switch steps), kidney/renal dosing, pharmacogenomics database (Lexidrug app), IV compatibility, shortage info; ~30% of UpToDate queries are drug-related (WK, Nov 2025) — explains why Expert AI had to assimilate Lexidrug first.
🟡 The pharmacist persona gets a separate SKU (Lexidrug app $29.99/mo) with offline database storage — evidence that offline resilience is valued in pharmacy workflow.

### 4.1.8 Patient education
🟢 "The Basics" (plain, ~4th–6th grade reading level) and "Beyond the Basics" (advanced lay) leaflets, printable/emailable, up to 19 languages. 🟡 This is the only patient-facing flow and it is *downstream of the clinician* — patients are recipients, never users.

---

## 4.2 UpToDate Expert AI (2025–2026)

🟢 Confirmed mechanics from launch materials and App Store listing:
- Conversational chat; answers composed strictly from UpToDate editorial content ("Clinical Intelligence" multi-layer validation).
- **Transparency triad:** per-answer single-click panels for **Assumptions** (what the AI inferred about your question's context), **Sources** (which UpToDate topics), **Step-by-step rationale** (reasoning trace).
- Guardrails: rejects answers without sufficient grounding ("embedded guardrails and oversight" per app listing); enterprise governance surfaces for admins (policy compliance).
- Packaging: US Pro Plus individual, trainee subs, select Enterprise Edition accounts first (land-and-expand pricing logic).
- Lexidrug expansion (Nov 2025): drug answers citing ~3,000 drug topics, "harmonised" with clinical topics to avoid contradictions.
🟡 Architectural reconstruction (from WK's own senior-engineer job post): agentic RAG with routing; multi-model (Azure OpenAI + AWS/Anthropic + Gemini); LangChain/LangGraph orchestration; OpenSearch/Azure AI Search retrieval over the corpus; eval harness with canary rollout; latency + hallucination metrics as first-class SLOs. Full reconstruction in File 09.
🔴 Deliberate missing features (as of Jul 2026): no patient-specific context ingestion (no chart data), no longitudinal memory of a patient, no voice interface — the agent mirrors the *reference* model, not the *patient-attached* model. This is the strategic seam.

---

## 4.3 Personal layer (account, retention, CME)

| Feature | Behaviour | Conf. |
|---|---|---|
| Login | Username/password; "Sign in with Microsoft"; OpenAthens; institutional SSO redirect; "Continue without signing in" (IP/LINK-authenticated institutional sessions, with optional personal login overlay) | 🟢 |
| CME engine | Every search/read accrues time-based CME; redeem for AMA PRA Category 1 / AANP hours; EHR-embedded searches also accrue | 🟢 |
| History | Search/read history visible; supports CME evidence and re-finding | 🟢 |
| Device policy | Mobile app access limited (2 devices); simultaneous-session friction for shared logins | 🟢/🟡 |
| Renewal engine | EzRenew flow; store page drives "Renew my subscription · purchase add-ons · upgrade to Pro Plus" | 🟢 |
| Notifications ⚪ | Partially verified: Practice Changing UpDates feed + likely email digests; granular push-notification matrix not publicly documented | ⚪ |

### 4.3.1 Retention loops (engineered, verified or strongly inferred)
1. 🟢 **CME ledger loop:** usage → credits → year-end redemption → switching cost (history dies with account).
2. 🟢 **Institutional revalidation loop:** 90-day re-authentication from institutional network keeps remote access alive → habitual institutional dependency.
3. 🟡 **Curiosity loop:** "What's New" per specialty pulls weekly re-engagement independent of clinical need.
4. 🟡 **Teaching loop:** graphics/handouts are used in front of patients and trainees → social reinforcement of value.
5. 🟢 **Workflow graft:** EHR Infobutton means the product is used *without a login decision* — the strongest retention mechanism is the absence of a re-choice moment.

### 4.3.2 Growth loops
- 🟡 **Prestige loop:** expert authorship is career currency → best authors join → content quality rises → brand deepens.
- 🟡 **Viral-by-necessity loop:** clinician without institutional access asks colleague to "check UpToDate" → exposure without free tier. (Reddit threads document login-sharing workarounds — evidence of pent-up demand UpToDate refuses to serve.)
- 🟢 **Enterprise-seeding loop:** residents/trainees imprint on UpToDate during training (discounted trainee SKUs) → demand it as attendings → institutional budget pressure.

### 4.3.3 Conversion flows (store.uptodate.com observed)
🟢 Wizard: Country → Role (Professional / Student-Resident / Group purchase / Other) → Profession (Physician, PA, Nurse, NP, Pharmacist) → Package (Pro vs Pro Plus; trainee tiers) → payment. Group SKU for 2–19; ≥20 routed to enterprise sales/contact form. 🟡 The flow is *pricing-segmentation-first* (status determines price before features), i.e., revenue-management design, not product-led growth. Built on Salesforce B2B Commerce (URL/marker evidence: `ccrz__` CloudCraze routes).

---

## 4.4 Institutional/admin layer

| Surface | Detail | Conf. |
|---|---|---|
| Admin dashboard | Usage reports for librarians/IT (uptime, search counts, top topics); typical of WK institutional tooling | 🟡 |
| Access control | IP ranges, referring URL, SSO (SAML via Microsoft/OpenAthens), EZproxy-compatible institutional routing | 🟢/🟡 |
| EHR integration kit | Epic Infobutton configuration docs; contextual links from problem list/meds/labs; PI (Promoting Interoperability) credit support | 🟢 |
| Governance (Expert AI) | Enterprise admin controls, policy compliance, governance marketing | 🟢 (existence) / 🟡 (depth) |
| Hidden workflow — authorship | External expert authors use an editorial portal (submissions, reviews, grading sign-off); existence implied by the documented editorial pipeline; portal UX not public | 🟡 |

---

## 4.5 Interaction logs — roles

**Doctor interaction (typical session, reconstructed):** 🟢 Hit app or Epic toolbar → search "hyponatremia workup" → Key Points card → topic "Summary and Recommendations" → calculator (urine osm gap) → drug check → CME silently logged → (2026) optional Expert AI thread to pressure-test a plan.
**Patient interaction:** 🟢 Clinician prints/emails "The Basics: ..." leaflet. No patient account, no portal. UpToDate is deliberately B2B2C.
**Admin interaction:** 🟡 License management, usage dashboards, SSO/EHR config, Expert AI governance policies.
**Pharmacist interaction:** 🟢 Lexidrug app monograph + interaction stack + IV compatibility; offline sync.

---

## 4.6 Security flows (visible surface)
🟢 SSO federation, 90-day institutional revalidation, device limits, subscription seat enforcement, app-store purchase receipt binding. 🟡 Account-level password policies and MFA for store accounts follow Salesforce Commerce defaults; institutional security relies on the customer IdP. Full treatment in File 12.

---

## 4.7 Notable absences (the reverse-engineering negative space)

| Absent capability | Why it matters for Ovexis | Conf. |
|---|---|---|
| No longitudinal patient model | Their EHR integrations are transitory context launches, not persistent patient twins | 🟢 |
| No patient-facing product with identity | Patient ed is leaflets, not an app | 🟢 |
| No population panel analytics for physicians | Admins see usage, clinicians don't see outcomes dashboards | 🟡 |
| No real-time vitals/wearables ingestion | None anywhere in public materials | 🟢 |
| No real-time collaborative features | No shared care plans, no team inbox | 🟢 |
| No self-serve developer API/content licenses | Distribution is partnership-gated | 🟢 |

> **Reverse-engineering conclusion:** UpToDate is a *read-optimised enterprise content appliance* with a new agentic front end. Everything that would require persistent patient state — the foundation of Ovexis — is architecturally absent, and bolting it on would collide with their own non-device CDS regulatory posture and corpus-centric engineering culture. 🟡
