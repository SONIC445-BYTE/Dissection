# DELIVERABLE 22 — Failure Analysis: How UpToDate Could Fail

Each scenario: vector, mechanism, evidence of early onset, probability/impact, and the Ovexis lesson. Ratings 🟡 analyst judgments on 🟢 evidence.

## 22.1 Business failure vectors

| # | Vector | Mechanism | Early-onset evidence | P×I | Ovexis lesson |
|---|---|---|---|---|---|
| B1 | **Price-anchor collapse** | Free AI tools reset CFO willingness-to-pay; renewals trade down or lapse | NHS trust cancellations; academic hospitals switching to DynaMed/OpenEvidence (Reddit, 2025) | Medium × High | Publish transparent, user-fair pricing; never price on "total staff" |
| B2 | **Trainee-pipeline inversion** | Next-gen clinicians imprint on free tools; UpToDate becomes "the thing attendings nostalgise" | OpenEvidence free for students; Reddit trainees cite cost | Medium × Very High | Win the trainee/student segment with a genuinely free tier and educational programs |
| B3 | **Enterprise cannibalisation paradox** | Expert AI reduces topic page views (the metric institutions pay on) → pricing model confusion | Packaging shows engagement rhetoric shifting | Low × Medium | Align pricing with outcomes, never with pageviews |
| B4 | **Portfolio margin squeeze** | Editorial COGS + AI inference COGS double-run while revenue growth is +5% organic | FY25 Health +5% vs margin expansion needs | Medium × Medium | Keep AI COGS on distillation economics from day one |
| B5 | **Ad-model moral panic benefits rivals then collapses** | OpenEvidence's pharma ads trigger clinician distrust; if OpenEvidence monetises differently (or exits EU-style), market re-rates paid tools | EU/UK withdrawal Apr 2026 | Low × Medium | Never build clinician trust on advertiser funding |

## 22.2 Technical failure vectors

| # | Vector | Mechanism | Evidence anchor | P×I |
|---|---|---|---|---|
| T1 | **Agent trust incident** | A hallucinated or mis-graded AI answer causes publicised patient harm; brand (the only asset) takes the hit | Expert AI is GA; scale rising fast | Low × Catastrophic |
| T2 | **Corpus-harmonisation contradictions** | Drug vs topic contradictions surfaced inside one AI answer destroy "harmonised" claim | Harmonisation explicitly marketed Nov 2025 | Medium × High |
| T3 | **Legacy UX drag** | 3.6★ app in the smartphone-native clinician era; ChatGPT-class UX resets expectations | App rating; AngularJS hiring | Medium × Medium |
| T4 | **Two-stack integration failure** | Entitlement/Packaging bugs across legacy↔AI boundary (wrong users get AI, or billing errors) | Packaging already confusing (ProPlus/trainee/Enterprise gating) | Medium × Medium |

## 22.3 Clinical failure vectors

| # | Vector | Mechanism | Evidence | P×I |
|---|---|---|---|---|
| C1 | **Grading disputes at AI scale** | Subjective GRADE calls amplified 10,000×/day; societies publicly disagree | GRADE subjectivity acknowledged in own policy | Medium × Medium |
| C2 | **Guideline fragmentation** | Regional practice divergence (UK vs US) makes one global corpus feel "American"; local competitors (NICE-grounded tools) win | iatrox critique: "Neither retrieves NICE..." | Medium × Medium |
| C3 | **Evidence-lag scandal** | A practice-changing update published late becomes a story ("UpToDate was six months behind") — fatal to the freshness covenant | Continuous-publishing promise | Low × High |

## 22.4 Regulatory failure vectors

| # | Vector | Mechanism | P×I |
|---|---|---|---|
| R1 | **CDS-device reclassification** | FDA/EU-MDR/AiAct interpretations pull deep CDS into device regulation; compliance costs explode; ad-supported rivals already fled EU — the tread is real (OpenEvidence EU/UK exit Apr 2026) | Low × High |
| R2 | **Data-residency enforcement** | Multi-cloud AI (Azure/AWS/Gemini) fails EU sovereignty requirements for hospital data | Medium × Medium |
| R3 | **Antitrust/tying scrutiny** | EHR-distribution bundling patterns + total-staff pricing provoke complaint cycles | Low × Medium |

## 22.5 Operational & distribution vectors

| # | Vector | Mechanism | P×I |
|---|---|---|---|
| O1 | **Editor-supply fragility** | 7,600-expert network ages out; prestige currency declines as LLM-assisted rivals offer scale-economics to contributors | Medium × High (slow) |
| O2 | **EHR-vendor repudiation** | Epic (with its own AI strategy + Microsoft), inhaling evidence partnerships, marginalises third-party CDS hooks | Medium × Very High |
| D1 | **Quiet war: the answer moves into the model** | Frontier LLMs trained on textbooks/journals answer "well enough" without paying any corpus; content layer commoditises beneath every vendor in File 20 | Medium × Catastrophic (industry-wide) |

## 22.6 The meta-failure mode (synthesis)

🟡 **UpToDate fails if "knowing medicine" decouples from "owning the clinical interface."** Three actors are fighting for that interface simultaneously: Epic (system of record), OpenAI/OpenEvidence (system of answers), and ambient scribes (system of documentation). UpToDate owns none; it rents all three. The 2024–2026 strategy (embed everywhere, govern everywhere) is the correct defence — but a landlord can only collect until the tenants build their own library.

**Ovexis adversarial use:** every failure vector above is a design requirement — own an interface (the patient's), keep trust costs near zero (privacy, transparency, pricing), treat outcomes evidence as R&D, and build distribution on rails you don't rent (consumer app stores + FHIR rails + patient-mediated exchange).
