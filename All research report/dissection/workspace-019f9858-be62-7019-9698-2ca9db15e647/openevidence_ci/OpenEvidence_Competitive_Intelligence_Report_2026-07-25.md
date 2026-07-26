# OpenEvidence — Competitive Intelligence & Ovexis Strategy Memo

**Public-source board research snapshot — 25 July 2026 (Asia/Kolkata)**  
**Target:** OpenEvidence | https://www.openevidence.com/ | Clinical AI Assistant  
**Prepared for:** Ovexis strategy and product leadership  

---

## Reader contract, scope and evidence protocol

🟢 **Scope:** This is a public-information investigation. Research used publicly accessible company pages, public app-store listings, public reporting, public research, and publicly visible community discussion listed in the Evidence Register. No account was created, no clinician credential was represented, no authenticated product area was accessed, no API was probed, and no unauthorised access or automated harvesting was attempted.

🟢 **Cut-off:** A claim is current only through 25 July 2026. “Current” company metrics are company-reported unless an independent source is explicitly identified. They are not audited operating metrics.

🟢 **Evidence key:** **🟢 Confirmed** means directly supported by a cited public source. **🟡 Strong Inference** means a testable conclusion drawn from multiple confirmed observations and explicitly names its assumptions. **🔴 Speculation** means a scenario or forecast; it is not a fact and should not enter a business case without validation.

🟢 **Source notation:** `[E##]` maps to the Evidence Register. “Company claim” means the assertion is published by OpenEvidence or quoted in its release; it is not independently audited. “Not publicly confirmed” is a research boundary, not proof of absence.

🟢 **Important limitation:** The request asks for every button, page, hidden workflow, API, permission, and screen. A verified-clinician product cannot responsibly be reverse engineered without credentials. This report inventories **publicly observable and explicitly disclosed** flows, distinguishes them from unknowns, and does not invent concealed functionality.

🟢 **Priority lens:** The deepest analysis is deliberately concentrated on clinical reasoning, retrieval-augmented generation (RAG), citation integrity, trust, safety, and clinician workflow because these are the decisive strategic layers for OpenEvidence and for Ovexis.

---

# 1. Executive summary

🟢 **What OpenEvidence is building:** OpenEvidence publicly positions itself as an AI-powered medical information and clinical decision-support platform for verified healthcare professionals. Its core interaction is a natural-language clinical question that yields a sourced, cited synthesis of peer-reviewed literature; the platform has expanded into DeepConsult research agents, Visits documentation, trial matching, and communications. [E01][E05][E06][E07][E08][E09]

🟢 **Why it exists — knowledge-work problem:** OpenEvidence’s stated premise is that clinical literature and guidelines outgrow a clinician’s ability to find, evaluate, and apply them during care. Its July 2025 release frames traditional evidence databases as fragmented and manual; its Wiley partnership frames the problem as reducing the research-to-practice lag. [E05][E12]

🟡 **Why it wins psychologically:** The clinician does not merely need a paper search. They need relief from the anxiety of missing a guideline, the humiliation of appearing uncertain in front of a patient, and the cognitive fatigue of opening multiple sources during a time-constrained encounter. Citation visibility turns “AI says” into “I can inspect the evidence,” which is the minimum viable trust bridge in medicine.

🟡 **Operational problem solved:** The product compresses several fragmented jobs—question formulation, search, source triage, evidence reading, drafting, documentation, patient communication, prior authorisation support, and trial discovery—into one fast interaction. The expansion from search to Visits and Dialer indicates that the company has learned that a correct answer outside the visit is weaker than an answer embedded in the visit. [E06][E07][E08]

🟢 **Primary customer and user:** Verified U.S. healthcare professionals are the public access target. Registration can require professional details, NPI/licence or equivalent documentation, and credential verification; marketing repeatedly says the core service is free to verified U.S. clinicians. [E01][E13][E14]

🟢 **Who is not the core customer:** The Terms say the service is intended for healthcare professionals and instruct consumers not to use it as a substitute for a clinician. The public product is therefore not a direct-to-patient diagnostic or care-management product. [E14]

🟡 **Economic customer:** The initial economic customer is likely the life-sciences/medical-device advertiser purchasing access to a verified professional audience, because the privacy policy states that advertising and partnership revenue supports a free service and the company acquired AI advertising company Amaro. Enterprise health systems and clinical-application partners are a second, increasingly visible buyer route, but public price cards are unavailable. [E13][E15][E16][E17]

🟢 **Category being created:** OpenEvidence calls itself a medical knowledge platform, AI copilot for doctors, and clinical decision-support/search platform. Its product trajectory supports the category label **evidence-native clinical intelligence layer**: an answer engine anchored in licenced medical content that is moving into the patient encounter. [E01][E05][E06][E07][E12]

🟡 **Category being displaced:** It is not simply replacing UpToDate, PubMed, medical society sites, ambient scribes, or telephony. It is attempting to replace the clinician’s *context-switching stack*—search tab, evidence reference, note tool, messaging/calling tool, and trial lookup—with a single evidence-grounded workspace.

🟢 **Core philosophy in public language:** The company describes a “gold in, gold out” approach: specialised medical models, peer-reviewed rather than open-web content, and sources a doctor can inspect. It also explicitly makes clinician access free and claims content partnerships with NEJM, JAMA, NCCN, Wiley and Cochrane. [E01][E12][E18][E19]

🟡 **Strategic thesis:** OpenEvidence’s true wedge is not an LLM. It is a three-sided compounding system: (1) licenced authoritative corpus and society relationships, (2) clinician habit formed by frictionless free access, and (3) a high-value verified professional advertising surface. Workflow modules raise query frequency and the opportunity to become the clinician’s default interface.

🟡 **Board conclusion:** OpenEvidence is formidable because it combines an unusually strong distribution motion with licensed-content credibility and a rapid workflow land-grab. Its primary fragility is the gap between *source-cited output* and *clinically faithful, patient-specific reasoning*. Citations can be present yet mismatched, selectively retrieved, weak, outdated, or over-interpreted. Independent and clinician commentary make this distinction material. [E20][E21][E22]

🟡 **Ovexis’s opening:** Do not try to out-market a medical search engine. Build a longitudinal, patient-governed **evidence-to-action control plane**: reconcile patient history and local care context, expose claim-level entailment and uncertainty, provide a longitudinal safety ledger, keep a human clinician accountable, and operate across jurisdictions with auditability designed in from day one.

---

## 1.1 Jobs-to-be-Done

| Job / moment | Status and analysis | OpenEvidence evidence | Ovexis implication |
|---|---|---|---|
| “When I face an unfamiliar clinical question, help me reach defensible evidence before the patient leaves.” | 🟢 OpenEvidence surfaces sources, citations and follow-up suggestions for clinician questions at point of care. [E05] | Core search, citations, content licences. | 🟡 Match speed; make the answer explicitly claim-evidence linked and show local applicability. |
| “When I document an encounter, help me finish the note without losing clinical quality.” | 🟢 Visits transcribes, supports custom templates, enriches assessment/plan, and supports document query. [E06] | Visits. | 🟡 Do not make documentation the product centre; use it to build a longitudinal, patient-approved record. |
| “When I call a patient, protect my privacy and retain a defensible record.” | 🟢 Dialer supports caller-ID selection, calls, messaging, fax, voicemail and optional Visit creation. [E07] | Dialer. | 🟡 Add consent-state, recording-state, communication preference, and follow-up ownership controls. |
| “When evidence is weak or conflicting, show me how much confidence I should have.” | 🟢 EvidenceGrade gives a real-time A–D / U assessment using a GRADE-inspired method; the company says it is an initial attempt, not a formal systematic review. [E09] | EvidenceGrade. | 🟡 This is the most important feature to surpass: show source hierarchy, directness to patient, contradiction, recency, and claim-level entailment—not one opaque grade. |
| “When a patient may qualify for research, find viable nearby trials.” | 🟢 Trial Matching compares trial criteria to patient characteristics/history and shows eligibility, status, location and contact details. [E08] | Trial matching. | 🟡 Add patient consent, eligibility evidence trail, site responsiveness, equity/access constraints, and referral handoff. |
| “When I must justify a plan to a payer or patient, draft a credible explanation.” | 🟢 OpenEvidence 2.0 supports prior-authorisation letters, handouts, calculators, drug modules and guideline modules. [E10] | Workflow generation. | 🟡 Generate only after a structured evidence and patient-context check; keep every factual assertion traceable. |

---

# 2. Company intelligence

## 2.1 Corporate facts, leadership, funding and milestones

🟢 **Founders:** OpenEvidence identifies Daniel Nadler (Harvard PhD) and Zachary Ziegler (Harvard PhD candidate) as founders. Public coverage identifies Nadler as CEO and Ziegler as co-founder/CTO. [E01][E23]

🟢 **Legal/operating footprint:** Terms identify OpenEvidence Inc. as a Delaware company; its public privacy/contact page lists a Miami address. Public releases use Miami and earlier Cambridge datelines. [E14][E13]

🟢 **Leadership visibility:** The public About page names a deep technical team and medical leadership including Samuel Finlayson (SVP Medical AI), Travis Zack (CMO), physicians, and an extensive medical-advisor network. This supports the presence of medical and research functions; it does not prove reporting lines or full-time status for every advisor. [E01]

🟢 **Series A:** OpenEvidence announced a $75M Series A led by Sequoia at a $1B valuation in February 2025, as reported by CNBC and referenced in company/investor coverage. [E23][E24]

🟢 **Series B:** OpenEvidence announced a $210M Series B at a $3.5B valuation on 15 July 2025, co-led by GV and Kleiner Perkins; the release named Sequoia, Coatue, Conviction, Greycroft and Thrive among participants. [E05]

🟢 **Series C:** Public reporting says OpenEvidence raised about $200M at a $6B valuation in October 2025, led by GV with multiple existing/new investors. [E24][E25]

🟢 **Series D:** OpenEvidence announced a $250M Series D at a $12B valuation on 21 January 2026; Thrive Capital and DST Global co-led. Reuters and CNBC independently reported the round. [E23][E24][E26]

🟢 **Revenue disclosure boundary:** CNBC reported Nadler said the company topped $100M in annual revenue in 2025. This is management-reported, not an audited financial statement. [E23]

🔴 **Latest valuation rumour:** A July 2026 report says OpenEvidence was *reportedly* exploring a $200M financing at a $20B valuation. The report explicitly says the company had not confirmed it. It must not be used as valuation fact. [E27]

🟢 **Acquisition — Amaro:** OpenEvidence announced acquisition of AI-native advertising company Amaro on 10 September 2025. The release said the purpose included modern, sustainable, user-first advertising infrastructure; consideration was not publicly disclosed. [E16]

🟢 **Acquisition — Vocode:** The public About page labels Ajay Raj and Kian Hooshmand as founders of Vocode, “Acquired by OpenEvidence.” A public acquisition date, consideration, and technical integration plan were not found in reviewed sources. [E01]

🟢 **Research:** The company announced that the paper *Do We Still Need Clinical Language Models?* won Best Paper at CHIL 2023; the paper was a collaboration with OpenEvidence/Xyla, MIT, Harvard Medical School, SickKids and Brigham and Women’s Hospital. [E28]

🟢 **Patents/open source boundary:** No OpenEvidence public developer platform, open-source project, or attributable patent portfolio was verified in the reviewed public sources. This is not evidence that none exists; it means no such conclusion should be assumed for diligence. [E60]

## 2.2 Timeline

| Date | Event | Status / strategic reading |
|---|---|---|
| 2023-06 | CHIL Best Paper announcement for *Do We Still Need Clinical Language Models?* | 🟢 Signals early research credibility and a specialty-model thesis. [E28] |
| 2024-08 | iOS and Android apps announced. | 🟢 Mobile turns a desk research tool into a bedside habit. [E29] |
| 2024-12 | OpenEvidence 2.0 announced: admin/clinical workflows, calculators and modules. | 🟢 First explicit move beyond retrieval. [E10] |
| 2025-02 | NEJM Group multi-year content agreement; HIPAA/BAA public announcement later in April. | 🟢 Licensed full text and PHI eligibility become trust/distribution accelerants. [E18][E30] |
| 2025-06 | JAMA Network multi-year content agreement. | 🟢 Strengthens full-text retrieval and citation moat. [E19] |
| 2025-07 | Series B and DeepConsult release. | 🟢 Introduces expensive, agentic deep-research path. [E05] |
| 2025-08 | Visits announced. | 🟢 Begins documentation and patient-record capture loop. [E06] |
| 2025-09 | Amaro acquired. | 🟢 Monetisation infrastructure is strategic, not incidental. [E16] |
| 2025-10 | Microsoft/Dragon Copilot collaboration and Veeva/Open Vista announced. | 🟢 Moves from destination app toward enterprise distribution and life sciences. [E11][E31] |
| 2025-12 / 2026-02 | Dialer limited release then full communications release. | 🟢 Extends into telephony, messaging, fax and voicemail. [E07][E32] |
| 2026-02 | Sutter/Epic workflow launch announced; Trial Matching launched. | 🟢 Evidence search reaches EHR workflow and patient-specific matching. [E08][E33] |
| 2026-03 | Wiley/Cochrane partnership announced. | 🟢 Adds systematic-review and specialty-reference depth. [E12] |
| 2026-04–07 | NCCN, specialty-society, EvidenceGrade, Cedars-Sinai patient-aware/Epic, NYP/Boston Children’s collaborations announced. | 🟢 The product roadmap is specialising and becoming institution/patient-context aware. [E09][E34][E35] |

## 2.3 Partnerships and ecosystem map

🟢 **Content partnerships:** NEJM Group agreement covers published content and multimedia from 1990 forward across several NEJM publications; JAMA agreement includes JAMA/JAMA Network content; Wiley provides 400+ journals/books plus Cochrane Database of Systematic Reviews and Cochrane Clinical Answers; NCCN guidelines/treatment algorithms are integrated. [E18][E19][E12][E34]

🟢 **Society density:** The public home/about pages name collaborations including NCCN, AAP, ACC, ADA, AAFP, NORD, ACOG, AUA, AAO, ACEP and more. A logo/partner page is evidence of a stated relationship, not necessarily a product integration depth or exclusivity term. [E01]

🟢 **Health-system workflow partnerships:** Sutter says the platform will launch inside Epic workflows; Cedars-Sinai says it will integrate Epic patient context; NewYork-Presbyterian/Columbia/Weill Cornell announced expanded tools. [E33][E35][E36]

🟢 **Platform partnerships:** Microsoft says OpenEvidence technology is planned for integration into Dragon Copilot; Veeva and OpenEvidence announced Open Vista for clinical-trial access, unmet needs, drug development and adoption. These are announced collaborations, not evidence that every proposed integration is generally available. [E11][E31]

🟡 **Partnership strategy:** The company is systematically converting authority holders into both corpus suppliers and distribution validators. Each partnership improves retrieval coverage, clinician trust, sales credibility, and the difficulty of a competitor reproducing the corpus legally.

---

# 3. Founder psychology and likely internal strategy

🟢 **Observed founder antecedent:** Nadler previously founded Kensho, an AI information-synthesis company acquired by S&P Global; public company/investor sources draw the parallel between financial information overload and medical information overload. [E23][E37]

🟢 **Observed technical belief:** In public discussion and the CHIL paper announcement, the founding thesis is that domain-specialised medical models can outperform general approaches on in-domain tasks. The 2026 funding release further says OpenEvidence coordinates proprietary, medically specialised models through a central “conductor.” [E28][E26]

🟡 **Founder belief #1 — information asymmetry is a solvable systems problem:** Nadler appears to view medicine as a high-stakes knowledge-routing problem analogous to finance: the bottleneck is not only discovering information but synthesising the right evidence fast enough for expert action.

🟡 **Founder belief #2 — access is moral and strategic:** The free, verified-clinician model, including free DeepConsult despite stated high compute cost, implies an explicit conviction that enterprise procurement should not gate physician knowledge. It also creates a powerful consumer-like distribution advantage. [E05][E13]

🟡 **Founder belief #3 — authority must be borrowed before it can be earned:** Licensing NEJM/JAMA/Wiley/Cochrane and partnering with societies is a deliberate answer to the adoption barrier that a technically capable startup cannot solve with model performance alone.

🟡 **Decision framework:** Likely order of operations: **clinician value → frictionless adoption → trusted corpus → workflow frequency → monetisation/enterprise expansion**. The Amaro acquisition and privacy policy’s advertising mechanics support this sequence. [E13][E16]

🟡 **Risk tolerance:** High. Evidence: free access, costly agentic research, a rapid product surface expansion into documentation and telephony, and very high funding velocity. The counterweight is unusually strong investment in credentials, licences and security claims.

🟡 **Ten-year vision:** The public language “default operating system of medical knowledge” and “medical superintelligence” suggests a goal beyond search: a clinical-intelligence substrate present in every clinician surface, routing a patient/problem to specialised models and authoritative content. [E01][E26]

🟡 **Likely internal strategy 2026–2028:** (1) make each specialty’s answer visibly more authoritative than a generic model; (2) turn Visits/Dialer/EHR context into daily workflow lock-in; (3) sell the resulting verified professional attention and enterprise integration; (4) use health-system integrations to acquire patient-aware credibility; (5) defend with content rights and model evaluation.

🔴 **Key psychological risk:** A company that frames itself as saving lives can confuse speed of adoption with evidence of clinical outcome benefit. That risk rises when press and fundraising narratives outrun transparent, independent clinical validation.

---

# 4. Product reverse engineering — observed surface, inferred system, and unknowns

## 4.1 Publicly confirmed product inventory

| Product / capability | What is confirmed | Value / strategic role | Boundary |
|---|---|---|---|
| Conversational clinical search | 🟢 Natural-language clinical questions return research-grounded answers with citations/references and follow-up suggestions. [E05] | 🟡 Acquisition wedge; answers convert literature overload into action. | 🟢 Exact prompt, ranking and generation implementation is not public. |
| Licensed evidence corpus | 🟢 NEJM, JAMA, Wiley/Cochrane, NCCN and other content/society relationships are public. [E01][E12][E18][E19][E34] | 🟡 Quality and legal-access moat. | 🟢 Corpus completeness, refresh SLA, licensing economics and source hierarchy are not public. |
| DeepConsult | 🟢 Company says agents use advanced reasoning models to analyse/cross-reference hundreds of studies in parallel and are free for verified U.S. clinicians. [E05] | 🟡 Premium-compute feature that repositions from lookup to research delegation. | 🟢 Agent tools, checkpoints, latency, cost, and evaluation protocol are not public. |
| EvidenceGrade | 🟢 A–D/+/−/U grade based on per-paper quality/certainty/relevance and a GRADE-inspired body-of-evidence phase. [E09] | 🟡 A direct answer to “citation is not enough.” | 🟢 It is not presented as a formal GRADE review; criteria/weights are not fully externally validated. |
| Visits | 🟢 Transcription, templates, real-time evidence, note editing/literature search, document upload/organisation and record query. [E06] | 🟡 Converts episodic search into longitudinal usage. | 🟢 EHR write-back/export formats and retention behaviour are not fully public. |
| Dialer | 🟢 Call, configurable caller ID, secure messaging, fax, straight-to-voicemail, Create Visit, unlimited daily minutes for verified U.S. clinicians. [E07] | 🟡 Solves clinician privacy + communications fragmentation and generates workflow data. | 🟢 Telecom provider, consent workflow, transcription retention and emergency handling are not public. |
| Trial matching | 🟢 Matches criteria against patient characteristics/history; shows study details/status/sites/contact and location. [E08] | 🟡 Bridges evidence retrieval to trial enrolment workflow. | 🟢 Underlying registry coverage, update cadence, false-positive/negative performance and referral closure are not public. |
| 2.0 workflow tools | 🟢 Prior-auth letters, patient handouts, diagnostic reasoning support, 50+ calculators, drug and guideline modules, tables. [E10] | 🟡 Captures administrative moments with immediate ROI. | 🟢 List of calculators/modules and validation versioning are not public. |
| EHR/context-aware use | 🟢 Sutter/Epic launch is announced; Cedars says Epic patient context is used for the individual session and not stored after that session. [E33][E35] | 🟡 Critical move from generic evidence to patient-specific support. | 🟢 Broad availability and technical standard/API are not public. |
| Mobile | 🟢 iOS and Android apps exist; store descriptions show professional gate, cited answers and 300+ journals/FDA/CDC claims. [E29][E38][E39] | 🟡 Mobile is the frequency and bedside-retention channel. | 🟢 Feature parity by platform is not public. |
| Sharing | 🟢 HIPAA announcement says conversations are private by default and can be shared by email invite; public-link sharing is for non-PHI conversations. [E30] | 🟡 A collaboration loop with an explicit PHI boundary. | 🟢 Granular enterprise permissions and audit-log UX are not public. |

## 4.2 Public screen and workflow map

🟢 **Anonymous visitor:** The public website offers product positioning, content/society logos, security messaging, mobile download links, sign-up, cookie consent and “Do Not Sell or Share” controls. It presents free access for healthcare professionals. [E01][E13]

🟢 **Sign-up / account:** Terms say account registration requires name, email, profession, specialty and other registration fields; privacy policy says it may collect education, board/certification, school/graduation, NPI/licence or equivalent. [E13][E14]

🟢 **Verification:** The privacy policy states professional-credential verification may use third-party information and proof; access may be denied when verification is unsatisfactory. [E13]

🟢 **Consent / PHI:** Terms incorporate the BAA for covered entities transmitting PHI; users are responsible for required permissions/consent, and Visits records conversations so users must inform participants where law requires. [E14][E40]

🟢 **Search / answer:** Public releases confirm question input, research synthesis, citations/references, suggested follow-up, and—in appropriate workflows—patient details. [E05][E06]

🟢 **Visit workflow:** A public “New Visit” entry point creates an evidence-integrated documentation workspace; it supports transcription, templates, document repository and post-visit queries using visit context. [E06]

🟢 **Dialer workflow:** Mobile navigation includes “Dialer”; calls/messages/faxes/voicemail may lead to “Create Visit,” transcribing the interaction into a structured note. [E07]

🟢 **Trial workflow:** A patient-context question can trigger trial matching, ranked results, filters and location-aware site details. [E08]

🟢 **Unknown screens:** Exact navigation architecture, onboarding completion state, password reset, account settings, role/permission pages, audit-log views, enterprise admin console, subscription/paywall, notifications, support queue, EHR launch contexts, API credentials, and all hidden/feature-flagged flows are not publicly verified. Do not assume their presence or absence.

## 4.3 Conversion, retention and growth loops

🟡 **Primary acquisition loop:** Free gated access reduces price and procurement friction → clinician receives a fast cited answer → colleague sees/receives the answer or hears a recommendation → another verified clinician registers → a bigger verified audience improves advertiser value → ads fund free access → repeat. This is supported by free verified access, company-reported word-of-mouth growth, and the advertising policy; the causal loop itself is an inference. [E05][E13][E16]

🟡 **Retention loop:** High-frequency point-of-care questions create an episodic habit; Visits, patient document query, Dialer and trial matching attach the habit to real patient work; richer workflow context raises switching cost. [E06][E07][E08]

🟡 **Enterprise loop:** Individual use creates internal demand → health system integrates evidence access into Epic/Dragon → context-aware workflows increase utility → institutional trust improves adoption → partner provides a reference account for other systems. [E11][E33][E35]

🟡 **Content flywheel:** More clinician use increases publisher/society incentive to be present at the point of care → content breadth improves answer coverage/quality → clinician trust and use grow → publisher leverage grows. Content-rights costs and exclusivity constraints could break this loop.

---

# 5. Complete user journeys

## 5.1 Verified clinician, standalone evidence journey

1. 🟢 **Discover:** Clinician arrives via peer, app store, web, society/partner, press or search; public pages emphasise citations, named publishers, HIPAA and free access. [E01][E38]
2. 🟢 **Register:** User supplies professional/account details. [E13][E14]
3. 🟢 **Verify:** NPI/licence/equivalent and third-party credential information may be used; access can be denied. [E13]
4. 🟢 **Accept terms/privacy:** User accepts Terms; relevant PHI use brings the BAA into scope for covered entities. [E14][E40]
5. 🟢 **Ask:** User submits natural-language clinical question or patient case context. [E05]
6. 🟢 **Receive:** Platform returns a cited, literature-grounded answer; EvidenceGrade may contextualise evidence strength. [E05][E09]
7. 🟡 **Verify / act:** Clinician should inspect sources, reconcile with patient-specific facts and professional judgement, then decide. This is not optional product etiquette: Terms state content is educational/informational and not a substitute for individual assessment. [E14]
8. 🟢 **Extend:** User can request a deeper synthesis via DeepConsult, produce a letter/handout/calculation, or start a Visit. [E05][E06][E10]
9. 🟡 **Retain:** A useful answer, saved context, patient documentation and daily mobile access make the next question easier than reverting to separate sources.

## 5.2 Patient-visit journey

1. 🟢 **Initiate Visit:** Clinician starts a New Visit. [E06]
2. 🟢 **Capture:** Visit can transcribe the encounter; user can shape notes with templates/instructions. [E06]
3. 🟢 **Enrich:** System surfaces guidelines/research/recommendations in assessment and plan; user can ask it to edit notes or search. [E06]
4. 🟢 **Context:** Documents can be uploaded/organised and queried; enterprise Cedars workflow can use Epic context in-session. [E06][E35]
5. 🟡 **Review / sign:** A safe clinical workflow requires clinician review, correction, attribution and EHR sign-off. Public sources confirm drafting, not an autonomous order or signature function.
6. 🟢 **Post-visit retrieval:** Documentation/visit context can be used in subsequent questions. [E06]
7. 🟢 **Unknown:** Patient portal, patient approval screen, note export/write-back, signed-note status, and retention/deletion controls are not publicly confirmed.

## 5.3 Patient communication journey

1. 🟢 **Select identity:** Clinician selects hospital/practice caller-ID number/name. [E07]
2. 🟢 **Communicate:** Call, text, fax or send straight-to-voicemail. [E07]
3. 🟢 **Optional recording/documentation:** “Create Visit” transcribes into structured documentation with real-time evidence. Users bear legal duty to notify/obtain consent where required. [E07][E14]
4. 🟡 **Close loop:** Ovexis should require a disposition, responsibility owner, patient acknowledgement (where appropriate), and task/escalation state. No equivalent public OpenEvidence control was verified.

## 5.4 Enterprise journey

1. 🟢 **Commercial/security evaluation:** Terms anticipate MSAs, BAAs, SLAs and customer-specific agreements; security page presents HIPAA and SOC 2 Type II claims. [E14][E15]
2. 🟢 **Integration:** Sutter announced Epic workflow deployment; Microsoft collaboration is planned for Dragon Copilot; Cedars announced Epic patient-context integration. [E11][E33][E35]
3. 🟡 **Governance gap:** Public materials do not demonstrate the end-to-end enterprise rollout path: formulary/local-guideline controls, tenancy, access roles, audit exports, evaluation approvals, clinician training, uptime SLA, and incident runbooks. These must be diligence questions, not assumptions.

## 5.5 Patient journey / consumer journey

🟢 **Boundary:** There is no verified public evidence of an OpenEvidence patient account, patient longitudinal dashboard, consumer subscription, wearable ingestion, insurance claims import, pharmacy delivery or care-navigation journey. The only public patient-facing touchpoint observed is clinician-initiated communication through Dialer. [E07][E14]

---

# 6. UX and design research

🟢 **Public design signals:** The public site uses a restrained, clinical presentation, named-source/society logos, HIPAA messaging, high-contrast type, a cookie preference modal, and iOS/Android app calls to action. It includes light/dark logo assets, but public evidence does not prove a user-selectable dark mode. [E01][E13]

🟡 **Visual hierarchy:** The dominant trust hierarchy is **authority before interface**: NEJM/JAMA/NCCN/Cochrane logos, peer-review language, HIPAA/SOC2 language, physician testimonials, then product actions. This is appropriate for a high-risk category where an attractive chat box without provenance is not credible.

🟡 **Conversion design:** Verification creates friction but doubles as a trust signal and audience-quality filter. It excludes non-clinicians and makes free access financially meaningful to advertisers. The design trade-off is a smaller addressable top of funnel and geographic/licensing boundary.

🟢 **Accessibility boundary:** No public VPAT, WCAG conformance statement, keyboard-navigation evidence, screen-reader test evidence, contrast audit, localised-language policy or accessibility roadmap was found in reviewed sources. Absence of public evidence is not evidence of non-compliance. [E60]

🟢 **Mobile evidence:** Native iOS/Android distribution is confirmed. Google Play describes professional verification and reports encrypted transit/data deletion options; store ratings are user-generated and should not be treated as clinical-quality evidence. [E38][E39]

🟡 **UX risk:** The more polished and conversational an answer appears, the more likely busy clinicians may mistake fluent synthesis for established fact. EvidenceGrade is therefore a necessary start, but an at-a-glance letter grade cannot show whether the cited sentence actually supports the output claim.

🟡 **Ovexis UX principle:** Make *epistemic friction* proportional to risk. A definitional question may show a concise answer; a treatment, dose, referral, prognostic or trial-matching output should require clear patient-context confirmation, claim-level evidence, uncertainty, contraindication scan, and an accountable human action.

---

# 7. Healthcare workflow and data architecture

## 7.1 Workflow coverage map

| Workflow | Publicly confirmed OpenEvidence coverage | Key gap / Ovexis attack |
|---|---|---|
| Clinical reasoning | 🟢 Cited research synthesis, DeepConsult, EvidenceGrade, guidelines and calculators. [E05][E09][E10] | 🟡 Add a structured patient-state graph and causal longitudinal timeline; do not rely on text recap alone. |
| Documentation | 🟢 Visit transcription, templates, notes, documents and query. [E06] | 🟡 Add source-of-truth provenance, signature state, addendum/versioning, structured extraction quality and EHR reconciliation. |
| Care coordination | 🟢 Dialer provides communication actions; clinical trial matching provides site/contact details. [E07][E08] | 🟡 Add closed-loop referrals, handoff receipt, tasks, results, escalation and care-team roles. |
| Hospital/EHR | 🟢 Sutter/Epic and Cedars/Epic patient-context partnerships announced. [E33][E35] | 🟡 Add institution-local policies/formulary/pathways and deployment-specific validation. |
| Payer / prior authorisation | 🟢 Prior-auth letters can be drafted. [E10] | 🟡 Add payer-specific rules, evidence packet assembly, submission/status/appeal workflow and outcome learning. |
| Lab / imaging | 🟢 No public evidence of direct lab or DICOM/PACS ingestion in the core standalone product. | 🟡 Ovexis can make provenance-preserving lab trends/imaging report integration a core advantage. |
| Pharmacy | 🟢 Drug monograph modules are public. [E10] | 🟡 No public e-prescribing, pharmacy claim, medication fill/adherence or interaction-management workflow was verified. |
| Patient longitudinal record | 🟢 Visits supports uploaded patient documents and Cedars describes EHR context in a session. [E06][E35] | 🟡 This is OpenEvidence’s most strategic whitespace: a patient-owned, reconciled, multi-source longitudinal intelligence layer. |

## 7.2 Data architecture — confirmed versus unknown

🟢 **Confirmed patient-context sources:** Patient documents may be uploaded and organised in Visits; Cedars says Epic data including procedures, comorbidities, medications, allergies and longitudinal data can support a patient-specific clinical session; Sutter says OpenEvidence launches within Epic workflows. [E06][E33][E35]

🟢 **Confirmed privacy behaviour for one integration:** Cedars’ announcement states EHR patient information will be used only for individual care decisions and will not be stored by OpenEvidence after the clinical session or used for another purpose. This is an integration-specific company statement; it must not be generalised automatically to every feature or customer. [E35]

🟢 **Standards boundary:** OpenEvidence has not publicly documented FHIR resource mappings, HL7 interfaces, C-CDA/CCD ingest, Apple Health, Google Health Connect, wearable, claims, genomics, DICOM, pharmacy or laboratory interfaces in reviewed first-party materials. [E60]

🟡 **FHIR inference:** An Epic workflow can be implemented through more than one integration pattern. It is reasonable to infer modern clinical-context exchange may use an interoperability mechanism such as FHIR, but the exact standard, scopes, resource set, refresh model, and write-back rights are not publicly confirmed and must not be asserted as fact.

🟡 **Minimal inferred data path (not a disclosed architecture):** credentialed clinician → authorised session/tenant → optional patient context/documents → context selection and minimisation → evidence retrieval + specialised reasoning → cited response/note/trial results → user review → optional downstream EHR/communication action. This is a product-function inference, not a network diagram.

## 7.3 Healthcare data flow diagram

```text
[🟢 Licensed journals / guidelines / society content]     [🟢 Public FDA/CDC etc. claimed in app listing]
                         \                                     /
                          \                                   /
                  [🟡 ingestion, parsing, rights/version control]
                                      |
                         [🟡 search + semantic/structured indexes]
                                      |
[🟢 verified clinician] --> [🟢 natural-language query] --> [🟡 retrieval/reranking]
                                                               |
                                           [🟢 specialised models / “conductor” claim]
                                                               |
                             [🟢 cited answer + 🟢 EvidenceGrade where applicable]
                                                               |
      [🟢 Visits documents / 🟢 Epic context in named partners]--+--[🟢 Dialer / note / trial matching]
                                                               |
                                        [🟡 clinician review and accountable action]
                                                               |
                                  [🟢 / unknown: EHR write-back or external closure]
```

🟢 **Diagram key:** Green-labelled nodes reflect disclosed capabilities or claims; yellow-labelled nodes are required implementation layers inferred from the disclosed user experience. Exact physical data stores, schemas, vendors, retention and cross-tenant isolation are not public. [E05][E06][E07][E08][E26][E33][E35]

---

# 8. AI reverse engineering — medical reasoning, RAG, citation engine and safety

## 8.1 What can be stated with confidence

🟢 **Specialised-model architecture:** The Series D release says OpenEvidence coordinates “an orchestra” of proprietary medically specialised models, each focused on a distinct sub-specialty, with a central conductor routing a physician question to the most relevant model. [E26]

🟢 **DeepConsult agents:** The Series B release says DeepConsult agents use advanced reasoning models to analyse and cross-reference hundreds of peer-reviewed studies in parallel. [E05]

🟢 **Retrieval-centred evidence layer:** The EvidenceGrade technical post says the system gathers relevant literature, optimises retrieval for relevant/informative/complementary papers, scores retrieved papers for quality/certainty/relevance, and grades the body of evidence. [E09]

🟢 **Citation engine:** Public releases say answers are source-cited and let clinicians drill into sources; licensed full text/figures/tables/multimedia are part of partnerships. [E05][E12][E18][E19]

🟢 **Evidence quality layer:** EvidenceGrade assesses individual papers and a body of evidence; it uses A–D, modifiers and U, and explicitly acknowledges real-time constraints relative to formal GRADE work. [E09]

🟢 **Patient-context reasoning ambition:** Cedars describes an agentic system that dynamically gathers relevant patient data, evaluates literature and synthesises context-aware answers. [E35]

🟢 **Model provider boundary:** OpenEvidence has not publicly named the base foundation-model providers, model weights, fine-tuning method, inference host, embedding model, vector database, agent tool set, long-context policy, prompt templates or evaluation harness in reviewed first-party sources. [E60]

## 8.2 RAG architecture assessment

🟡 **Most likely architecture:** The disclosed behaviour strongly supports a retrieval-augmented generation system, even where the company does not expose its full stack: question classification/routing → retrieval from licensed corpus → ranking/diversification → specialised synthesis → citation attachment → optional evidence grading. The central conductor and DeepConsult indicate the system may branch to multiple speciality/reasoning paths. [E05][E09][E26]

🟡 **What “RAG” does and does not solve:** Retrieving high-quality content constrains the answer space and makes review possible. It does **not** guarantee that (a) the right documents were retrieved, (b) a cited document entails a sentence, (c) the model preserves study population/intervention/outcome qualifiers, (d) contradictory evidence is surfaced, or (e) patient-specific application is safe.

🟡 **Likely context-management challenge:** Hundreds of studies cannot all fit as raw text in a single robust clinical answer without cost, latency and relevance failure. DeepConsult therefore likely uses staged search, filtering, summarisation and synthesis. Each stage risks information loss, source-selection bias and error propagation; this is why intermediate provenance matters.

🟡 **Citation engine maturity test:** A clinical citation system should be scored on four separate metrics: **retrieval recall**, **citation correctness** (the cited source supports the claim), **citation completeness** (material claims are supported), and **clinical applicability** (population/setting/recency map to the presented patient). Marketing commonly reports none of these separately; public OpenEvidence materials do not provide a full independent scorecard.

## 8.3 Medical reasoning assessment

🟢 **Product claim:** OpenEvidence says its platform supports clinical questions/case details with research-grounded answers and, in enterprise settings, considers patient history, procedures, comorbidities, medication and allergies. [E05][E35]

🟡 **Reasoning boundary:** “Reasoning” in a clinical system has at least five distinct tasks: interpret the question; extract/normalise patient facts; retrieve evidence; compare alternatives with contraindications and uncertainty; communicate a recommendation calibrated to evidence. A high USMLE score or fluent explanation does not demonstrate reliable performance across all five.

🟢 **Benchmark caveat:** OpenEvidence announced a perfect USMLE score in 2025. Such a test demonstrates knowledge-question performance under a defined benchmark, not prospective safety, citation faithfulness, calibration, workflow usability, diagnosis accuracy, or patient outcome improvement. [E41]

🟢 **Independent caution:** A December 2025 medRxiv preprint comparing OpenEvidence and DeepConsult on complex subspecialty board-style questions reported low absolute accuracy in its evaluated setting and said expert oversight remained important. It is a preprint, not a universal clinical-quality verdict. [E20]

🟢 **Independent caution:** A 2026 Nature Medicine evaluation reported frontier general-purpose LLMs outperformed the evaluated clinical AI tools—including OpenEvidence—on its MedQA, HealthBench and real-clinical-query benchmarks. This evaluates a particular system/version/benchmark, not all clinical usefulness. [E21]

🟢 **Clinician voice:** Public Reddit discussions include clinicians praising paper discovery and speed while warning that summaries may be wrong, citations can be mismatched, rare/specialist questions are riskier, and source reading remains necessary. One OpenEvidence representative acknowledged a guideline-ingestion citation crosswire in a thread and said it was being fixed. These are anecdotal reports, not incidence estimates. [E22][E42][E43]

🟡 **Clinical safety conclusion:** OpenEvidence’s safety posture is **better described as evidence-grounded decision support than hallucination-proof clinical reasoning**. The strongest safe user instruction is: use it to find and compare evidence; independently inspect key sources; never treat its synthesis as the final clinical decision.

## 8.4 Safety controls: observed strengths and outstanding gaps

| Safety dimension | Public strength | Public limitation / diligence question |
|---|---|---|
| Source quality | 🟢 Licensed peer-reviewed content, major journals/guidelines and Cochrane. [E12][E18][E19] | 🟡 Which source takes precedence when guideline, review, RCT and case report conflict? |
| Citation transparency | 🟢 Sources/references and source drill-down are central claims. [E05][E12] | 🟡 Is each atomic claim linked to supporting passage? Are citations automatically entailment-checked? |
| Evidence strength | 🟢 EvidenceGrade scores retrieved papers/body of evidence and emits U where no grade. [E09] | 🟡 It is a real-time, GRADE-inspired method; independent validation, inter-rater agreement and update policies need review. |
| Human oversight | 🟢 Terms say content is not medical advice and clinician remains responsible. [E14] | 🟡 Disclaimer is not a safety control. What prevents an unsafe action in a rushed workflow? |
| Credential gate | 🟢 Verified-professional access is required/possible; patient sharing is bounded. [E13][E30] | 🟡 Credentialing improves audience quality but does not prove competence, scope, or patient consent. |
| PHI handling | 🟢 HIPAA/BAA, encryption, SOC 2 Type II and named controls are claimed. [E15][E40] | 🟡 Need feature-specific data flow, retention, training-use, subprocessor and incident evidence. |
| Patient context | 🟢 Cedars says session-specific EHR context will not be stored after session. [E35] | 🟡 How are missing, stale, duplicated, contradictory or temporally misordered chart facts handled? |
| Monitoring | 🟢 Security page cites vulnerability testing, annual penetration test and policies. [E15] | 🟢 No public clinical error-reporting SLA, answer rollback, model card, sentinel-event protocol or prospective surveillance programme was found. [E60] |

## 8.5 AI architecture diagram

```text
                              🟢 Licensed / authoritative evidence
       NEJM · JAMA · NCCN · Wiley/Cochrane · society guidance · public sources
                                              |
                           🟡 rights-aware ingestion / parsing / versioning
                                              |
                          🟡 lexical + semantic + metadata retrieval indexes
                                              |
 Clinician question --> 🟡 intent/risk/specialty router --> 🟢 “conductor” routes model [E26]
                                              |                         \
                             🟡 retrieve/rerank/diversify                   🟢 DeepConsult agents [E05]
                                              |                                 |
      Optional patient/session context --> 🟡 fact extraction + relevance filter |
                                              \___________________  ___________/
                                                                  \/
                              🟡 synthesis constrained by retrieved evidence
                                              |
                   🟢 citations / source drill-down + 🟢 EvidenceGrade when gradeable [E09]
                                              |
                              🟡 safety UI: uncertainty, conflicts, missing data
                                              |
                                🟢 clinician review, judgement and action [E14]
```

🟢 **Diagram boundary:** Only the specialised/conductor model claim, DeepConsult, retrieval/evidence grading, citations and clinician-responsibility statement are publicly evidenced. All transformation stages are strong functional inferences, not confirmed internal components. [E05][E09][E14][E26]

## 8.6 Ovexis clinical-AI design requirements

🟡 **Non-negotiable 1 — claim-level provenance:** Every clinical claim should link to a specific evidence span, version, study type, population and timestamp. A citation list is insufficient.

🟡 **Non-negotiable 2 — patient-evidence fit:** Explicitly score whether patient age, sex/pregnancy state, renal/hepatic status, comorbidities, prior therapies, country/local formulary and care setting match the evidence population.

🟡 **Non-negotiable 3 — abstention and escalation:** The model should abstain or switch to “evidence insufficient / conflicting / high-risk” when support is weak, patient facts are incomplete, or a high-acuity decision crosses a risk threshold.

🟡 **Non-negotiable 4 — two-pass verification:** A generative/synthesis pass must be checked by an independent claim-entailment and citation-completeness pass before display; critical results should undergo deterministic calculator/rule checks.

🟡 **Non-negotiable 5 — longitudinal safety memory:** Track unresolved abnormalities, medication changes, missed follow-up, prior adverse events, active referrals and source provenance across time. This is distinct from chat history.

---

# 9. Technical reverse engineering and API investigation

## 9.1 Confirmed technical facts

🟢 **Hosting:** OpenEvidence says services are primarily hosted on Google Cloud Platform and Vercel. [E15]

🟢 **Web application clue:** Public site image URLs use a `/_next/image` path, making Next.js a reasonable frontend inference; this is not official framework documentation. [E01]

🟢 **Security transport/storage:** Company security page claims TLS 1.2 with SHA256 certificate for transit and AES-256 for database storage at rest. [E15]

🟢 **Account authentication:** Terms describe username/password accounts and account-settings password change; SSO, MFA, passkeys, SCIM and enterprise identity protocols are not publicly confirmed. [E14]

🟢 **Analytics/tracking:** Privacy policy says Google Analytics or similar may be used, plus cookies/pixels/local storage for security, analytics and advertising. [E13]

🟢 **Mobile platforms:** Native iOS and Android apps are publicly listed. [E29][E38][E39]

## 9.2 Inference map and unknowns

| Layer | Assessment |
|---|---|
| Frontend | 🟡 Likely React/Next.js web frontend because of public Next.js image path and Vercel hosting. Exact version, component system, mobile stack, state management, accessibility tooling and feature-flag system are unknown. |
| Backend | 🟡 Must support identity, content retrieval, model orchestration, conversations, document handling, telemetry and communications. Language, microservice/monolith choice, queues, data stores and deployment topology are unknown. |
| AI infrastructure | 🟢 Specialised/conductor-model architecture is claimed. [E26] 🟢 Model provider, inference service, GPU provider, embeddings/vector DB, cache, prompt service and evaluation infrastructure are unknown. |
| Data stores | 🟢 Databases exist by implication of service functionality; provider/type/schema/PHI tenancy not public. Do not infer PostgreSQL, BigQuery, Pinecone, Redis or similar. |
| Telephony | 🟢 Dialer exists. [E07] 🟢 Carrier/CPaaS vendor, call recording architecture, SMS compliance, fax vendor and data retention are unknown. |
| Email/payments | 🟢 Policy anticipates email and payment data for some paid products. [E13] 🟢 Vendors and commercial use are unknown. |
| Observability/CI/CD | 🟢 Secure development, change management, vulnerability scans and annual pen test are stated. [E15] 🟢 CI/CD, monitoring vendor, incident SLOs, tracing and uptime are unknown. |

## 9.3 API investigation

🟢 **Public developer experience:** No public REST/GraphQL/FHIR SDK, OpenAPI schema, developer portal, API pricing, API authentication method, webhooks, rate-limit documentation or public integration guide was found in the reviewed first-party sources. [E60]

🟢 **Integration evidence:** Epic workflow deployment/context-aware partnerships and planned Dragon Copilot integration confirm integration capability at least in named enterprise arrangements. They do not establish a general public API. [E11][E33][E35]

🟡 **Diligence question set for Ovexis:** Request supported standards and resources; launch contexts; OAuth/SMART scopes; data minimisation; read/write rights; patient matching; app registration; audit events; event/webhook support; rate limits; tenant isolation; source versioning; deletion/retention; and clinical-safety change control.

---

# 10. Security, privacy and regulatory investigation

## 10.1 Public compliance/security posture

🟢 **HIPAA and BAA:** OpenEvidence says it complies with HIPAA Privacy, Security and Breach Notification Rules, supports PHI under its BAA or customer-specific agreements, and publicly posts a BAA. [E15][E30][E40]

🟢 **SOC 2 Type II:** The company says it achieved SOC 2 Type II for the Security trust-services category. The full report is not publicly reviewed here; board diligence should request the current report under NDA. [E15]

🟢 **Named security practices:** Public security page says encryption at rest/in transit, code testing, regular vulnerability scans, annual external pen test, annual employee security training and policies for access, incident response, vendor management, SDLC and retention. [E15]

🟢 **Conversation privacy claim:** Privacy policy headline says user questions/conversations are not shared and PHI is not used to train AI models. [E13]

🟢 **Advertising/data use:** The same privacy policy permits profiling based on professional profile/on-platform activity; U.S. audience extension may share limited identifiers/interest categories with advertising/identity/measurement partners; it says question/conversation text is not shared for those purposes. [E13]

🟢 **Terms data-use caution:** Terms permit collection/use/transfer/sale of non-personal information and customer usage data, and grant a broad licence over submitted “User Content,” subject to the Privacy Policy. The terms also state PHI use is governed by the BAA for covered entities. [E14][E40]

🟡 **Privacy interpretation:** The public documents draw a material distinction between **question/conversation text and PHI** (claimed not shared / not used to train PHI models) versus **profile, activity, identifiers, inferred interests, aggregated/de-identified data and non-personal usage data** (used for service/advertising/partnership purposes). A health system should not reduce this to “we do not share questions”; it must contractually map every feature’s data fields and use.

🟢 **International position:** Privacy policy discusses EU-U.S./UK/Swiss Data Privacy Framework commitments and U.S. hosting/transfer. Separate 2026 reporting says access was withdrawn/geoblocked in EU/UK amid regulatory uncertainty. The facts should be reconciled directly with the company; DPF participation is not the same as product availability or AI Act/MDR readiness. [E13][E44]

## 10.2 Regulatory assessment

🟢 **Intended-use disclaimer:** Terms say OpenEvidence is not a healthcare provider; content is educational/informational, not medical advice, diagnosis/treatment or substitute for individual assessment. [E14]

🟡 **FDA status:** No FDA clearance/authorisation for the core OpenEvidence evidence-synthesis platform was verified in reviewed public sources. This does not prove the product is unregulated. The risk depends on intended use, claims, functionality, autonomy, and whether it meets the U.S. non-device CDS criteria.

🟡 **Regulatory pressure point:** The platform increasingly combines evidence retrieval with patient context, diagnostic reasoning support, trial matching, note generation and real-time recommendations. As output becomes more patient-specific/actionable, the distinction between transparent decision support and regulated clinical decision software becomes harder to maintain.

🟡 **European lesson:** A reported EU/UK withdrawal demonstrates that geographic availability is a product and regulatory feature, not a late legal checkbox. Ovexis must design local data controls, model governance, clinical-evaluation evidence and regional content/localisation from the architecture stage.

## 10.3 Security diligence matrix

| Topic | Public evidence | Required diligence before handling PHI at scale |
|---|---|---|
| BAA | 🟢 Public BAA. [E40] | 🟡 Feature-specific permitted uses; subprocessors; breach timing; return/destruction; model training prohibition; telecom/doc transcription coverage. |
| SOC 2 | 🟢 Company claims Type II Security. [E15] | 🟡 Current report, scope, exceptions, bridge letter, complementary user controls. |
| Encryption | 🟢 TLS/AES claim. [E15] | 🟡 KMS/HSM, key rotation, client-side options, backups, secrets, encryption in analytics/logs. |
| Identity | 🟢 Password account + credential verification. [E13][E14] | 🟡 MFA/SSO/SCIM, RBAC/ABAC, break-glass, session controls, provider lifecycle and delegated access. |
| Audit | 🟢 No public clinical/audit-log documentation found. | 🟡 Immutable who/what/when/which-source/model/version/patient-context log with exports. |
| AI safety | 🟢 Citations/EvidenceGrade/terms. [E09][E14] | 🟡 Evaluation dataset governance, safety cases, red-team results, drift monitoring, high-risk routing and rollback. |
| Data lifecycle | 🟢 Cedars session non-storage statement for named integration. [E35] | 🟡 Default retention by product, deletion SLA, document/call/transcript backup retention, eDiscovery, training use and tenant deletion. |

---

# 11. Business model and growth strategy

## 11.1 Revenue model

🟢 **Free clinician access:** The public site says free/unlimited for healthcare professionals; releases repeatedly say free for verified U.S. clinicians. [E01][E05][E06][E07]

🟢 **Advertising support:** The privacy policy says advertising and partnership revenues support free services; it describes interest-based sponsored content and audience extension. NBC reports Nadler said core OpenEvidence would remain free and is funded by ads including pharma/medical-device advertisers. [E13][E45]

🟢 **Advertising infrastructure acquisition:** Amaro acquisition was explicitly framed as enabling modern advertising infrastructure and preserving free physician access. [E16]

🟢 **Enterprise commercial route:** Terms reference MSAs, BAAs and SLAs for institutional users, while Sutter/Epic and Microsoft/Dragon collaborations show an enterprise route. Public per-seat pricing, contract values, take rate, gross margin, CAC, retention, and sales-cycle metrics are not disclosed. [E11][E14][E33]

🟡 **Business model canvas:**

| Block | Board view |
|---|---|
| Customer segments | 🟡 Clinicians/users; health systems/enterprise buyers; life-sciences and med-device advertisers; publishers/societies; platform partners. |
| Value proposition | 🟡 Fast, cited, authoritative medical evidence at point of care without individual clinician payment; increasingly documentation/communication convenience. |
| Channels | 🟢 Web, iOS, Android, word-of-mouth claims, societies/publishers, EHR/platform integrations. [E01][E05][E29] |
| Relationships | 🟡 Self-serve clinician relationship; contracted publisher/health-system relationships; advertiser partnerships. |
| Key resources | 🟡 Content rights, verified user audience, medical/AI team, specialised models, trust brand, workflow integration. |
| Key activities | 🟡 Content licensing/ingestion, retrieval/evaluation, clinical safety, product development, credential verification, advertiser operations, enterprise deployment. |
| Partners | 🟢 Named publishers/societies, Mayo platform history, health systems, Microsoft, Veeva, GCP/Vercel. [E01][E11][E12][E15] |
| Cost structure | 🟡 Content licences, model compute, engineering/clinical talent, cloud, communications, security/compliance, ads sales, enterprise integration. |
| Revenue | 🟢 Advertising/partnership revenue; 🔴 enterprise/API/life-science revenue expansion is plausible but public economics are not disclosed. [E13][E45] |

## 11.2 Unit economics and risk

🟡 **Economic strength:** A free product lowers clinician CAC and drives usage. A verified, specialty-labelled professional audience is scarce advertising inventory, particularly around point-of-care intent.

🟡 **Economic weakness:** DeepConsult and patient-aware workflows are compute-intensive, while quality content rights and medical review are expensive. If advertiser demand, brand safety, or content licensing economics weaken, the free-unlimited promise may be difficult to sustain.

🟡 **Trust tension:** The same query/session context that makes advertising valuable can make clinicians wary of commercial influence. Public policy says questions/conversations are not shared for advertising, but medical decision context is sensitive enough that perceived influence can damage trust even without direct data leakage.

## 11.3 Growth strategy

🟢 **Product-led growth claim:** Company releases/job descriptions attribute rapid adoption to word of mouth and report more than 40% of U.S. physicians logging in daily, 10,000+ sites and high monthly registrations. These are company-reported measures. [E05][E11][E46]

🟢 **Founder/PR distribution:** Prominent funding, TIME100 Health recognition for Nadler, mainstream media, publisher/society announcements and app stores provide credibility-led awareness. [E01][E05][E23]

🟡 **SEO limitation:** The clinical answer experience is credential-gated; public SEO is therefore more likely to focus on partnerships, authority pages, press and app listings than indexed medical answer pages. This preserves professional gating but sacrifices public organic answer traffic.

🟡 **Growth flywheel risk:** Free access accelerates initial use, but daily clinical adoption must be measured against active clinician denominator, depth per clinician, repeat specialty use, verified source review, and patient/outcome impact—not registrations or consultations alone.

---

# 12. Hiring intelligence and operating model

🟢 **Team composition:** Public About page lists a concentrated engineering/research group with MIT/Harvard/Stanford and clinical-advisor credentials, plus a commercial team. [E01]

🟢 **Engineering culture:** 2026 job postings describe a 30-person engineering team, autonomy/end-to-end ownership, evaluation/quantitative proof, and five-day in-person work in San Francisco or Miami. Job postings are employer claims and snapshots, not a verified headcount. [E46][E47]

🟢 **Priority signals:** Public roles include research scientist, data infrastructure, product/backend/infrastructure and platform security. They signal investment in model evaluation, scalable data/research workflows and compliance/resilience. [E46][E47]

🟡 **Operating-model inference:** The company appears to prefer small, high-output generalists rather than large specialised functional silos. This can produce speed and strong ownership; it can also make formal clinical governance, incident management and enterprise implementation bottlenecks as product scope expands.

🟡 **Roadmap signal:** Hiring data infrastructure and security alongside releases in evidence grading, EHR context, communications and specialist partnerships implies the near-term engineering agenda is not another chat UI. It is data rights/ingestion, model evaluation, patient context, specialty models, enterprise hardening and workflow reliability.

---

# 13. Customer intelligence and voice of market

🟢 **Praise themes:** App-store descriptions and clinician quotations emphasise faster paper finding, specificity, current evidence, convenience at bedside and value relative to manual PubMed search. These are testimonials or user reviews, not independent efficacy evidence. [E38][E39]

🟢 **Critical themes:** Reddit discussion repeatedly advises source verification, notes answer quality varies by question phrasing/rarity, cites examples of misinterpretation/mismatched citations, and positions the product as a sophisticated paper-finding tool rather than a final decision-maker. [E22][E42][E43]

🟡 **Most important customer insight:** Users trust OpenEvidence most when it behaves as a *search and evidence-navigation accelerator*. Trust erodes when it behaves as an authoritative clinical oracle. Ovexis should architect the former and visibly constrain the latter.

🟢 **Unexpected use cases surfaced publicly:** Prior authorisation letters, patient handouts, clinical calculators, medical notes, telephone documentation, fax/voicemail, and trial matching expand the product well beyond literature search. [E07][E08][E10]

🟡 **Churn triggers likely to matter:** source/citation error; local-guideline mismatch; no EHR integration; concern that ads influence recommendations; inability to handle complex rare disease; latency; clinician fear of medico-legal risk; regional unavailability; and lack of patient longitudinal context. These are plausible retention risks, not disclosed churn data.

---

# 14. Competitive landscape

## 14.1 Positioning matrix

🟢 **Method note:** This matrix is a strategic category map. It uses public vendor positioning links listed in the Evidence Register where available and does **not** claim a complete feature audit, current price audit, or regulatory certification audit for each company. “Overlap” and “attack” are 🟡 strategic inferences.

| Comparator | Publicly described / category lens | Overlap with OpenEvidence | Strategic read for Ovexis |
|---|---|---|---|
| Regacore | 🟢 Public positioning not sufficiently verified in this research snapshot. [E60] | 🟢 Unknown. | 🟡 Do not make a factual comparison until entity/product is disambiguated. |
| Superpower | 🟡 Consumer preventive/longevity health intelligence. [E48] | Low direct evidence-search overlap. | 🟡 Benchmark consumer longitudinal engagement, not CDS trust. |
| Function Health | 🟡 Consumer lab testing and health insights. [E49] | Low. | 🟡 Benchmark lab logistics/results experience. |
| Levels | 🟡 Metabolic-health and sensor/data interpretation. [E50] | Low. | 🟡 Benchmark continuous biomarker education. |
| PreventiveHealth.ai | 🟢 Public positioning not sufficiently verified in this snapshot. [E60] | Unknown. | 🟡 Validate separately. |
| Glass Health | 🟡 Clinician AI/evidence/workflow competitor. [E51] | Direct clinician-workflow overlap. | 🟡 Compare clinical reasoning transparency and notes workflow. |
| Atropos Health | 🟡 Real-world evidence / evidence generation for care. [E52] | Adjacent evidence layer. | 🟡 OpenEvidence retrieves published evidence; Atropos-like tools may compete on local RWE. |
| AMBOSS | 🟡 Medical knowledge/reference and education platform. [E53] | Direct knowledge-reference overlap. | 🟡 Incumbent structured content and education trust. |
| UpToDate | 🟡 Curated clinical reference/CDS. [E54] | Direct incumbent reference overlap. | 🟡 Benchmark editorial accountability and topic completeness. |
| Apollo 24/7 | 🟡 India consumer care/telehealth ecosystem. [E55] | Low direct U.S. clinician-search overlap. | 🟡 Benchmark patient care navigation in India. |
| Practo | 🟡 India provider discovery/consumer health platform. [E56] | Low. | 🟡 Distribution and provider network benchmark. |
| Tata 1mg | 🟡 India pharmacy/diagnostics/consumer health. [E57] | Low. | 🟡 Pharmacy/lab fulfilment benchmark. |
| Healthify | 🟢 Entity is ambiguous (multiple health products use this name); no definitive comparison made. [E60] | Unknown. | 🟡 Disambiguate market/product before diligence. |
| Apple Health | 🟡 Consumer health data aggregation/longitudinal personal record. [E58] | Complementary, not direct clinical evidence search. | 🟡 Benchmark consent, consumer trust and device data. |
| Google Health / Health Connect | 🟡 Consumer/device health-data platform. [E59] | Complementary. | 🟡 Benchmark interoperability and Android data permission model. |
| Human API | 🟡 Health-data connectivity/aggregation. [E61] | Complementary data layer. | 🟡 Potential integration or archetype for record acquisition. |
| Whoop | 🟡 Wearable/recovery data platform. [E62] | Adjacent. | 🟡 Benchmark engagement loops; avoid medical overclaim. |
| Oura | 🟡 Wearable/readiness data platform. [E63] | Adjacent. | 🟡 Benchmark consumer longitudinal trends. |
| Ultrahuman | 🟡 Wearable/metabolic-health platform. [E64] | Adjacent. | 🟡 Benchmark hardware/data UX. |

## 14.2 OpenEvidence’s actual competitive set

🟡 **Direct battlefield:** UpToDate/DynaMed/AMBOSS/ClinicalKey, PubMed/Google Scholar, clinician AI assistants and evidence-native startups compete for the same “what should I know now?” moment.

🟡 **Workflow battlefield:** Ambient scribes, EHR-native copilots, Doximity-style physician platforms, messaging/telehealth tools and trial-matching systems compete once OpenEvidence enters Visits/Dialer.

🟡 **Longitudinal battlefield:** Apple/Google, data-connectivity platforms, wearables, lab companies and preventive-health platforms compete for patient data continuity—but OpenEvidence does not yet publicly demonstrate a patient-owned longitudinal platform.

🟡 **Most dangerous competitor:** EHR incumbents, because an evidence system inside the clinical workspace has lower context-switching friction and privileged access to patient/local data. OpenEvidence’s Sutter/Cedars/Microsoft initiatives acknowledge this reality rather than eliminate it.

---

# 15. Moat analysis

| Moat | Rating | Evidence / assessment |
|---|---|---|
| Content rights | **Strong, but purchasable** | 🟢 Major publisher/guideline/society partnerships provide lawful full-text/multimedia access. [E12][E18][E19][E34] 🟡 Rights are expensive, non-exclusive unless proven, and publishers can partner elsewhere. |
| Clinician distribution | **Strong** | 🟢 Company reports 40%+ U.S. physician daily use and large registration velocity; free verified access aids PLG. [E05][E11] 🟡 Exact active metrics/retention are unverified. |
| Brand / trust | **Medium–Strong** | 🟢 NEJM/JAMA/Cochrane/NCCN association, medical advisors, citations and HIPAA/SOC2 messaging. [E01][E09][E15] 🟡 One highly visible harmful answer could damage trust. |
| AI / model | **Medium** | 🟢 Specialised/conductor architecture and research capability are public. [E26][E28] 🟡 Frontier models rapidly commoditise; independent benchmarks/question complexity challenge superiority claims. [E20][E21] |
| Clinical workflow | **Emerging** | 🟢 Visits, Dialer, trial matching and named Epic integrations. [E06][E07][E08][E33][E35] 🟡 EHR-native incumbents have home-field advantage. |
| Data moat | **Emerging / constrained** | 🟢 Patient documents/context are used in some workflows. [E06][E35] 🟡 PHI/consent limits, non-storage promise in Cedars integration, and lack of public longitudinal record make this not yet a confirmed data flywheel. |
| Advertising / marketplace | **Medium** | 🟢 Verified HCP audience, audience extension policy, Amaro acquisition. [E13][E16] 🟡 Commercial targeting can weaken clinical trust; advertising market is cyclical. |
| Regulatory | **Weak–Medium** | 🟢 HIPAA/BAA/SOC2 claims. [E15][E40] 🟡 EU/UK withdrawal shows regulatory posture is not a global moat. [E44] |
| Switching cost | **Medium, rising** | 🟡 Search alone has low switching cost; patient documents, templates, call identity/history, institutional integration and habits create higher cost. |
| Network effects | **Weak direct / medium indirect** | 🟡 Clinician usage improves advertiser/publisher attraction, but one clinician’s answer quality does not inherently improve another’s unless product feedback/benchmarking loop is governed. |

---

# 16. Strategy frameworks

## 16.1 SWOT

| Strengths | Weaknesses |
|---|---|
| 🟢 Licensed authority-rich corpus; cited answers; EvidenceGrade; strong public adoption/funding; free verified access; mobile; growing workflows. [E01][E05][E09][E12] | 🟢 Opaque internal model/evaluation/API details; no public independent safety scorecard; terms disclaim clinical advice; user reports of citation/interpretation problems. [E14][E20][E21][E22] |
| Opportunities | Threats |
| 🟡 Become embedded evidence layer in EHR/ambient/documentation/communications; build speciality models; enterprise governance; local evidence. | 🟡 EHR/major-model vertical integration; regulatory reclassification; publisher leverage; safety incident; ad-trust conflict; computation/content cost; regional withdrawal. |

## 16.2 Porter’s Five Forces

🟡 **Supplier power — High:** Publishers, guideline owners, cloud/model providers, EHRs and telecom vendors control critical inputs. Content partnerships mitigate but do not remove dependence.

🟡 **Buyer power — Split:** Individual clinicians have low price sensitivity at free but high trust sensitivity; enterprise systems have high procurement/negotiation power; advertisers have measurable ROI demands.

🟡 **Threat of new entrants — Medium:** A chat UX is easy; legal content rights, trust, clinical evaluation, security and distribution are hard.

🟡 **Threat of substitutes — High:** Human colleagues, UpToDate, PubMed, EHR tools, generic frontier models, society guidance and medical search remain substitutes.

🟡 **Rivalry — High and accelerating:** General models, EHR vendors and reference incumbents can bundle features. Differentiation must be measured clinical trust and workflow integration, not chat capability.

## 16.3 Value chain

🟡 **Acquire rights → ingest/structure/version evidence → retrieve/rank → specialty reasoning → cite/grade → clinician review → document/communicate/act → measure quality and outcomes.** OpenEvidence is visibly strong in rights, retrieval, answer experience and distribution. The least public portion is post-answer outcome measurement and closed-loop clinical governance.

---

# 17. Decision ledger

| Feature decision | Why built / pain | KPI likely improved | Trade-off | Alternate architecture |
|---|---|---|---|---|
| Free verified access | 🟡 Remove procurement/price barrier; create verified audience. | Registration, activation, daily use, advertiser inventory. | Ad-trust tension; subsidised compute. | Paid individual / employer licence. |
| NPI/licence gate | 🟢 Credential verification and professional access. [E13] | Audience quality, trust, ad value. | Excludes learners/international/non-NPI users. | Open access + risk-tiered consumer mode. |
| Licensed content | 🟢 Authoritative evidence coverage. [E12][E18][E19] | Answer trust, retrieval quality, partner brand. | Cost/licence dependency/rights complexity. | Open-access-only corpus, editorial summaries. |
| Cited chat | 🟢 Sources/references and drill-down. [E05] | Activation, trust, repeat use. | Citation can create false confidence if mismatched. | Search-first evidence cards, no generation. |
| DeepConsult | 🟢 Parallel deep research across studies. [E05] | Complex-query satisfaction, differentiation. | High compute/latency; opaque agent failure. | On-demand asynchronous analyst queue / static review templates. |
| EvidenceGrade | 🟢 Evidence-strength context. [E09] | Trust calibration, safe action. | A single grade can hide nuance; grading may be wrong. | Per-claim GRADE-like rubric + visual evidence graph. |
| Visits | 🟢 Documentation with real-time evidence/context. [E06] | Daily active use, workflow stickiness. | PHI/consent/security/accuracy liability. | Standalone ambient scribe with evidence links. |
| Dialer | 🟢 Privacy-preserving clinician communication and documentation. [E07] | Frequency, retention, patient reach. | Telecom compliance and support burden. | Integrate with existing telephony APIs only. |
| Trial matching | 🟢 Patient-to-trial relevance/location. [E08] | High-value oncology/specialty use, life-science strategic value. | Eligibility error, stale site data, equity bias. | Curated navigator referral service. |
| Epic patient context | 🟢 Patient-aware answers in named partners. [E33][E35] | Enterprise value, answer relevance. | Integration complexity/PHI risk/local governance. | User-entered structured context. |
| Amaro acquisition | 🟢 Advertising infrastructure. [E16] | Monetisation and ad operations. | Brand conflict in clinical decision setting. | External ad-tech vendor or subscription model. |

---

# 18. Feature dependency graph

```text
🟢 Credential verification / account
             |
🟡 Identity, role, organisation, policy
             |
🟢 Consent / BAA / patient authority (when PHI used)
             |
🟢 Data collection: clinician question + 🟢 documents/EHR context where enabled
             |
🟡 Normalisation, patient matching, temporal reconciliation, provenance
             |
🟢 rights-aware evidence retrieval + 🟢 specialised/agentic reasoning
             |
🟢 citations + 🟢 EvidenceGrade + 🟡 safety/uncertainty checks
             |
🟢 search answer / note / trial candidate / communication documentation
             |
🟡 clinician review / decision / sign-off / referral / follow-up ownership
             |
🟡 outcome capture, error reporting, evaluation and model/content improvement
```

🟡 **Critical dependency insight:** OpenEvidence’s public product is strong from query through answer. A longitudinal-health intelligence platform must differentiate in the lower half: identity resolution, provenance, reconciliation, accountable action and outcome learning.

---

# 19. Engineering backlog reconstruction

| Horizon | Likely scope | Confidence |
|---|---|---|
| MVP / 2023–24 | 🟢 Medical search, citation-linked answer experience, credential gate, early speciality models, mobile. [E28][E29] | High |
| V2 / late 2024–mid 2025 | 🟢 Administrative tasks, calculators, licensed NEJM/JAMA content, HIPAA/BAA, DeepConsult. [E05][E10][E18][E30] | High |
| V3 / late 2025–2026 | 🟢 Visits, Dialer, trial matching, content/society expansion, EHR context, EvidenceGrade. [E06][E07][E08][E09][E12][E33][E35] | High |
| Current hard problems | 🟡 Content versioning/rights, speciality routing, agent reliability, citation faithfulness, clinical evaluation, PHI minimisation, EHR interoperability, telecom compliance, enterprise governance. | High inference |
| Near roadmap | 🟡 More specialty-specific models/guidelines, deeper EHR embedding, evidence-grade refinement, more health-system partnerships, local workflow modules. | Medium inference |
| Technical debt hotspots | 🟡 Cross-product patient identity/context, documentation source-of-truth, precise permissioning, answer reproducibility, citation drift, content licence entitlements, observability and clinical incident handling. | Medium inference |

---

# 20. Failure analysis and risk register

| Risk | Type | Likelihood | Impact | Leading indicator | Mitigation / Ovexis lesson |
|---|---|---:|---:|---|---|
| Citation supports wrong claim | Clinical/AI | 🟡 Medium | 🟡 Critical | User reports, correction tickets, entailment-failure tests. [E22][E42] | 🟡 Automated claim–passage verifier; visible support quote; rollback. |
| Confident summary overweights weak/old/irrelevant evidence | Clinical | 🟡 High | 🟡 Critical | Case reports ranked alongside RCTs; source recency mismatch. | 🟡 Evidence hierarchy + directness + contradiction UI. |
| Patient context missing/stale/misattributed | Data/clinical | 🟡 Medium | 🟡 Critical | Duplicate patients, stale med list, timeline conflict. | 🟡 Reconciliation layer and human patient-context confirmation. |
| EHR incumbents bundle evidence AI | Business/distribution | 🟡 High | 🟡 High | Epic/Oracle/general-model launch adoption. | 🟡 Interoperable, patient-owned cross-system layer; avoid destination-only UX. |
| Publisher renegotiation / content cost | Business | 🟡 Medium | 🟡 High | Licensing concentration, rights restrictions. | 🟡 Diversified open/authoritative content and provenance architecture. |
| Advertising undermines clinical trust | Brand/regulatory | 🟡 Medium | 🟡 High | Clinician complaints, regulator scrutiny, ad adjacency concerns. | 🟡 Strict separation of evidence and commercial modules; no query-based ads. |
| Deep agent compute economics fail | Economic | 🟡 Medium | 🟡 High | Cost/query rises faster than revenue/use. | 🟡 Risk-tiered model routing, async deep research and budget guardrails. |
| PHI/telecom breach | Security/operational | 🟡 Low–Medium | 🟡 Critical | Misconfigured sharing, transcription/fax incident. | 🟡 Data minimisation, feature-specific BAA, zero-trust audit, incident drills. |
| Regulation/reclassification / regional withdrawal | Regulatory | 🟡 Medium | 🟡 High | Stronger clinical claims, EU/UK restrictions. [E44] | 🟡 Design documentation, intended-use controls, regional deployments from day one. |
| Reputational clinical event | Brand/clinical | 🟡 Medium | 🟡 Critical | Viral wrong answer or missed contraindication. | 🟡 Harm-model testing, high-risk abstention, transparent correction history. |
| Workflow sprawl reduces reliability | Product/operational | 🟡 Medium | 🟡 High | Support volume and cross-feature errors. | 🟡 Make evidence/provenance shared platform; do not accumulate disconnected AI features. |

---

# 21. Competitive attack plan — how a well-funded challenger could beat OpenEvidence

🟡 **Attack thesis:** Do not compete as “another ChatGPT for doctors.” Win the trust layer that OpenEvidence has not publicly proven: patient-specific evidence applicability, longitudinal continuity, institutional governance and measured clinical safety.

1. 🟡 **Technology:** Build a deterministic patient timeline + clinical knowledge graph first; use LLMs as interpreters, never as the system of record.
2. 🟡 **Evidence:** Require claim-to-passage alignment, cite source version, label evidence type and calculate patient–study similarity.
3. 🟡 **Safety:** Publish a model card, benchmark methodology, failure taxonomy, correction changelog and a health-system safety case.
4. 🟡 **Clinical:** Launch narrow, high-value pathways (polypharmacy, CKD, oncology navigation, discharge follow-up) where longitudinal context creates a measurable advantage.
5. 🟡 **Pricing:** Avoid point-of-care ads. Offer transparent B2B/B2B2C per-covered-life or per-clinician pricing with a free read-only safety timeline for patients.
6. 🟡 **Distribution:** Partner with regional health systems, payers, labs, pharmacies and care coordinators—not only journals. Solve transitions of care and data fragmentation.
7. 🟡 **Brand:** Position “show your work, show what you do not know, and close the loop,” not “medical superintelligence.”
8. 🟡 **Enterprise:** Make governance a product: local protocol library, formulary rules, review queues, audit logs, tenant evaluation, source controls and regional deployment.
9. 🟡 **Consumer:** Give patients a longitudinal, consented record and explainable preparation layer; OpenEvidence’s provider-only gate leaves this experience open.
10. 🟡 **International:** Build India-first/region-first standards, multilingual evidence/local guidelines and data-residency controls rather than treating global expansion as US product export.

---

# 22. Future prediction

## Next 12 months

🟡 **Likely:** More health-system/EHR partnerships and speciality content/model launches are likely, because 2026 announcements already cluster around Epic context, oncology, societies and EvidenceGrade.

🟡 **Likely:** More workflow extension around prior authorisation, coding, referrals, trials, follow-up and documentation is likely, because the company is converting answers into daily operational touchpoints.

🟡 **Likely:** A public push for evaluation/safety proof is likely, because independent benchmark results, clinician discussion and regulatory scrutiny make citation presence insufficient.

🔴 **Possible:** A new financing at a much higher valuation is possible but unconfirmed; do not plan against the reported $20B figure. [E27]

## Next 3 years

🟡 **Likely:** The company may evolve into an embedded clinical-intelligence service exposed through EHR, ambient, mobile and communications surfaces rather than a destination website.

🟡 **Likely:** Publisher/society relationships may expand into specialty-specific “authoritative modes,” local guideline integration and continual evidence updates.

🟡 **Likely:** Health systems will demand policy controls, evaluation, auditability and local knowledge integration as patient-context features spread.

🔴 **Possible:** Acquisitions of ambient-scribing, interoperability, evaluation/clinical-safety, provider network or patient-communications assets are plausible. No specific target is evidenced.

## Next 5 years

🟡 **Likely:** The long-term market may split into (a) global foundation-model clinical workspaces, (b) EHR-native copilots, (c) evidence/rightsholder platforms, and (d) longitudinal data/control planes. OpenEvidence’s current path aims to sit between (a), (b) and (c).

🟡 **Ovexis chance:** A persistent cross-system longitudinal patient intelligence layer can be category-defining if it earns patient/provider trust, withstands regulation and produces outcome evidence. That is a different moat than more medical search.

---

# 23. Ovexis strategy memo

## 23.1 Top 50 ideas to copy

1. 🟡 Make source provenance a first-class UI object.
2. 🟡 Gate high-risk clinical tools to verified professionals.
3. 🟡 Use a free or very-low-friction clinical entry point.
4. 🟡 Start with a single urgent clinician job, not a broad health portal.
5. 🟡 Secure rights to authoritative content where lawful and economic.
6. 🟡 Present citations inline, not in a hidden appendix.
7. 🟡 Build mobile-first point-of-care access.
8. 🟡 Support natural-language clinical questions.
9. 🟡 Let clinicians ask follow-up questions against preserved context.
10. 🟡 Partner with respected clinical societies.
11. 🟡 Recruit practising clinicians into design and safety review.
12. 🟡 Make patient handouts evidence-linked and editable.
13. 🟡 Support structured calculators only when versioned and tested.
14. 🟡 Support prior-auth evidence packets.
15. 🟡 Treat content freshness as product quality.
16. 🟡 Use speciality routing rather than one universal answer prompt.
17. 🟡 Separate fast lookup from deep-research mode.
18. 🟡 Offer a citation drill-down action.
19. 🟡 Put evidence in the documentation workflow.
20. 🟡 Preserve clinician privacy in patient communication.
21. 🟡 Integrate trial discovery into care conversations.
22. 🟡 Use named partners as trust accelerators.
23. 🟡 Publish security/compliance posture early.
24. 🟡 Provide a public BAA process for relevant customers.
25. 🟡 Make conversations private by default.
26. 🟡 Use explicit non-PHI rules for public sharing.
27. 🟡 Build a clear professional identity/credential system.
28. 🟡 Optimise onboarding for speed after verification.
29. 🟡 Use a source-quality signal in answers.
30. 🟡 Build content ingestion/versioning as a core competency.
31. 🟡 Measure source coverage by specialty/question type.
32. 🟡 Make deep work asynchronous where latency is unavoidable.
33. 🟡 Build clinician feedback/error reporting into answers.
34. 🟡 Invest in security engineers before enterprise scale.
35. 🟡 Invest in data infrastructure before patient context scale.
36. 🟡 Let product usage create enterprise demand.
37. 🟡 Make EHR integration a strategic milestone.
38. 🟡 Use product announcements to make roadmap credible.
39. 🟡 Be explicit about human clinical responsibility.
40. 🟡 Design branded evidence trust signals consistently.
41. 🟡 Support medical text, tables and figures where licensed.
42. 🟡 Minimise workflow context switching.
43. 🟡 Build physician word-of-mouth, not only paid acquisition.
44. 🟡 Give clinicians a reason to return every shift.
45. 🟡 Create a rigorous model-evaluation culture.
46. 🟡 Treat publisher relationships as product partnerships.
47. 🟡 Treat health-system partnerships as design partnerships.
48. 🟡 Use role-appropriate answers, not consumer-facing clinical jargon.
49. 🟡 Make trust visible before asking users to upload sensitive data.
50. 🟡 Turn every answer into a defensible clinical artefact.

## 23.2 Top 50 ideas to improve

1. 🟡 Link every atomic recommendation to a quoted evidence span.
2. 🟡 Show citation entailment score, not merely citation count.
3. 🟡 Show evidence population versus patient similarity.
4. 🟡 Surface contradictory studies/guidelines by default.
5. 🟡 Add local guideline/formulary precedence controls.
6. 🟡 Display publication/version/withdrawal status.
7. 🟡 Differentiate diagnostic, therapeutic, prognostic and administrative evidence grading.
8. 🟡 Add explicit low-evidence/absence-of-evidence language.
9. 🟡 Provide a “why not” comparison for alternatives.
10. 🟡 Require medication/allergy/renal/pregnancy checks for treatment outputs.
11. 🟡 Use structured data to verify calculated values.
12. 🟡 Preserve patient timeline provenance for each fact.
13. 🟡 Make missing/stale/conflicting patient data conspicuous.
14. 🟡 Show local availability and insurance constraints separately from clinical efficacy.
15. 🟡 Make source access/rights transparent to users.
16. 🟡 Create a clinician-visible answer correction history.
17. 🟡 Publish independent prospective evaluation.
18. 🟡 Publish citation correctness/completeness metrics.
19. 🟡 Add specialty-specific red-team benchmarks.
20. 🟡 Design high-risk abstention rather than verbose hedging.
21. 🟡 Add a human escalation path for complex cases.
22. 🟡 Add structured referral/order follow-through.
23. 🟡 Add task ownership and closed-loop notifications.
24. 🟡 Make note suggestions distinguish observation from inference.
25. 🟡 Require confirmation before copying generated content into final records.
26. 🟡 Build patient consent/versioning into recording and sharing.
27. 🟡 Give patients a readable explanation and correction channel.
28. 🟡 Build regional guidelines and languages natively.
29. 🟡 Treat international compliance as product configuration.
30. 🟡 Make advertising physically and semantically separate from evidence.
31. 🟡 Prohibit commercial adjacency to a treatment recommendation.
32. 🟡 Expose ad-personalisation controls plainly.
33. 🟡 Give organisations policy-as-code controls.
34. 🟡 Support SSO/SCIM/RBAC/ABAC and full audit export.
35. 🟡 Let an organisation select allowed evidence sources.
36. 🟡 Let an organisation lock guideline versions for audits.
37. 🟡 Track model/content version on every answer.
38. 🟡 Offer offline/low-connectivity emergency evidence packs.
39. 🟡 Instrument outcome—not only answer consumption.
40. 🟡 Measure diagnostic/treatment time saved without measuring overreliance.
41. 🟡 Connect trial matches to navigator/site workflow and eligibility audit.
42. 🟡 Include social determinants/access burden in trial/referral match.
43. 🟡 Add lab/imaging/claims reconciliation.
44. 🟡 Use event-driven follow-up for abnormal trends.
45. 🟡 Offer a patient-owned longitudinal record layer.
46. 🟡 Make every document upload provenance-preserving.
47. 🟡 Create precision safety settings by role/specialty.
48. 🟡 Make user feedback create transparent model/content fixes.
49. 🟡 Disclose model capability boundaries by task.
50. 🟡 Design clinical safety governance as a product, not a policy PDF.

## 23.3 Top 50 ideas to ignore or avoid copying

1. 🟡 Do not market a model as hallucination-proof.
2. 🟡 Do not equate USMLE performance with patient safety.
3. 🟡 Do not make a citation list the sole safety mechanism.
4. 🟡 Do not rely on disclaimers to manage clinical risk.
5. 🟡 Do not build an opaque single-letter confidence score without drill-down.
6. 🟡 Do not optimise solely for answer speed.
7. 🟡 Do not allow fluent prose to conceal missing patient facts.
8. 🟡 Do not show ads near treatment recommendations.
9. 🟡 Do not monetise sensitive patient data or question text.
10. 🟡 Do not make clinician attention the only business asset.
11. 🟡 Do not use ad-targeting logic to decide clinical content rank.
12. 🟡 Do not ship broad global access before regional readiness.
13. 🟡 Do not treat GDPR/AI Act readiness as a legal afterthought.
14. 🟡 Do not capture PHI when de-identified or structured fields suffice.
15. 🟡 Do not default to indefinite transcript/document retention.
16. 🟡 Do not silently write back AI text to the EHR.
17. 🟡 Do not remove an answer’s model/content version from auditability.
18. 🟡 Do not hide conflict in evidence to make recommendations seem decisive.
19. 🟡 Do not automate diagnosis/treatment action beyond validated scope.
20. 🟡 Do not imply that a patient record is complete because an EHR feed exists.
21. 🟡 Do not let users share PHI by public link.
22. 🟡 Do not expand into every workflow before governance matures.
23. 🟡 Do not let a product surface become a collection of disconnected AI demos.
24. 🟡 Do not sell “clinical superintelligence” before publishing safety proof.
25. 🟡 Do not make rare-disease outputs look more certain than evidence permits.
26. 🟡 Do not use unreviewed research as guideline-equivalent.
27. 🟡 Do not treat guideline age as a proxy for wrongness without context.
28. 🟡 Do not conflate absence of evidence with evidence of absence.
29. 🟡 Do not rank trial eligibility without showing each criterion match/miss.
30. 🟡 Do not bury jurisdictional availability constraints.
31. 🟡 Do not assume clinician verification proves informed patient consent.
32. 🟡 Do not use generic chat history as a patient longitudinal record.
33. 🟡 Do not let source licensing dilute independent critical appraisal.
34. 🟡 Do not infer quality from prestigious journal branding alone.
35. 🟡 Do not use engagement metrics as outcome metrics.
36. 🟡 Do not use black-box advertiser attribution for trust-sensitive care.
37. 🟡 Do not make role permissions a later enterprise add-on.
38. 🟡 Do not minimise incident-response and correction workflow investment.
39. 🟡 Do not hide telemetry in a vague privacy promise.
40. 🟡 Do not interpret “HIPAA compliant” as a complete security assessment.
41. 🟡 Do not make patients invisible in a supposedly patient-aware system.
42. 🟡 Do not optimise documentation text volume over clinical signal.
43. 🟡 Do not default to US guidance in non-U.S. care.
44. 🟡 Do not ignore social/access constraints in recommendations.
45. 🟡 Do not accept data-source duplicates without reconciliation.
46. 🟡 Do not omit provenance after normalisation.
47. 🟡 Do not use estimated risk without calibration/validation by population.
48. 🟡 Do not collapse clinician, organisation and patient consent into one checkbox.
49. 🟡 Do not force clinical users to reverse engineer model limitations.
50. 🟡 Do not substitute product charisma for clinical governance.

## 23.4 Top 50 ideas to reinvent

1. 🟡 Reinvent search as a longitudinal clinical question graph.
2. 🟡 Reinvent citations as claim-level verifiable evidence packets.
3. 🟡 Reinvent “confidence” as uncertainty, applicability and contradiction dimensions.
4. 🟡 Reinvent chat history as patient-owned timeline memory.
5. 🟡 Reinvent notes as structured, provenance-linked clinical events.
6. 🟡 Reinvent patient context as reconciled multi-source truth with conflict flags.
7. 🟡 Reinvent trial matching as consented access/navigation workflow.
8. 🟡 Reinvent prior auth as payer-rule execution plus evidence packet.
9. 🟡 Reinvent referral as a closed-loop clinical contract.
10. 🟡 Reinvent care plans as time-bound, accountable tasks.
11. 🟡 Reinvent “AI answer” as a reviewable decision brief.
12. 🟡 Reinvent specialist routing as a multidisciplinary virtual case conference.
13. 🟡 Reinvent guideline integration as locally versioned executable pathways.
14. 🟡 Reinvent alerts as risk-ranked, explanation-first signals.
15. 🟡 Reinvent health records as patient-consented portable data vaults.
16. 🟡 Reinvent consent as granular, revocable purpose-based permissions.
17. 🟡 Reinvent data import as source-scored event reconciliation.
18. 🟡 Reinvent medication lists as indication/timeline/adherence/contraindication graphs.
19. 🟡 Reinvent lab review as trend and follow-up intelligence.
20. 🟡 Reinvent imaging reports as actionable longitudinal evidence.
21. 🟡 Reinvent wearable data as clinically contextualised, not engagement-only signals.
22. 🟡 Reinvent patient handouts as shared-decision evidence summaries.
23. 🟡 Reinvent safety review as a live error/correction ledger.
24. 🟡 Reinvent quality dashboards as patient-outcome and evidence-use dashboards.
25. 🟡 Reinvent commercial model as transparent care-network value, not attention resale.
26. 🟡 Reinvent ads as prohibited in clinical decision paths.
27. 🟡 Reinvent enterprise configuration as policy-as-code.
28. 🟡 Reinvent EHR integration as bidirectional, provenance-safe interoperability.
29. 🟡 Reinvent evaluation as continuous local calibration.
30. 🟡 Reinvent model selection as risk/cost/quality routing with audit trail.
31. 🟡 Reinvent deep research as a structured evidence review with stop rules.
32. 🟡 Reinvent source quality as task-specific evidence fitness.
33. 🟡 Reinvent rare disease support as networked expert escalation.
34. 🟡 Reinvent primary care support as longitudinal prevention/coordination.
35. 🟡 Reinvent chronic care as care-gap closure over time.
36. 🟡 Reinvent discharge as a monitored recovery pathway.
37. 🟡 Reinvent claims data as care-continuity signals.
38. 🟡 Reinvent pharmacy data as medication safety and adherence signals.
39. 🟡 Reinvent patient messaging as consented, triaged clinical tasks.
40. 🟡 Reinvent clinician productivity as safe decisions per cognitive minute.
41. 🟡 Reinvent patient engagement as agency over data and decisions.
42. 🟡 Reinvent interoperability as a product experience, not a backend project.
43. 🟡 Reinvent international expansion as local evidence and governance modules.
44. 🟡 Reinvent governance as an operational workbench for clinical leaders.
45. 🟡 Reinvent audit logs as readable clinical reasoning provenance.
46. 🟡 Reinvent source partnerships as transparent, non-exclusive public benefit networks.
47. 🟡 Reinvent evidence update as impact-aware change management.
48. 🟡 Reinvent clinician education as feedback from real evidence questions.
49. 🟡 Reinvent preventive care as patient-context predictions with evidence limits.
50. 🟡 Reinvent the category as **longitudinal evidence-to-action intelligence**.

## 23.5 Top 50 market gaps

1. 🟡 Claim-level citation faithfulness.
2. 🟡 Patient-specific evidence applicability.
3. 🟡 Reconciled cross-EHR longitudinal record.
4. 🟡 Patient-controlled consent/portability.
5. 🟡 Local formulary and guideline integration.
6. 🟡 Regional/non-U.S. clinical guidance.
7. 🟡 Multilingual clinician/patient workflows.
8. 🟡 Explicit evidence contradiction detection.
9. 🟡 Transparent evidence-grade validation.
10. 🟡 Independent clinical outcome evidence.
11. 🟡 Structured AI incident reporting and rollback.
12. 🟡 Local calibration by health system/population.
13. 🟡 Audit-ready answer/model/source versioning.
14. 🟡 Closed-loop referral/care coordination.
15. 🟡 Payer evidence workflow and appeals.
16. 🟡 Trial navigator and equity-aware matching.
17. 🟡 Imaging/lab/pharmacy/claims reconciliation.
18. 🟡 Maternal, paediatric and geriatric applicability checks.
19. 🟡 Rare-disease expert-network escalation.
20. 🟡 Clinical social-determinants/context integration.
21. 🟡 Patient-readable shared decision evidence.
22. 🟡 Medication indication/deprescribing longitudinal graph.
23. 🟡 Follow-up ownership and missed-care-gap monitoring.
24. 🟡 Hospital-to-home continuity.
25. 🟡 Privacy-preserving cross-institution patient matching.
26. 🟡 Local data-residency / sovereign deployment.
27. 🟡 AI Act/MDR-ready safety case tooling.
28. 🟡 Ad-free clinical trust model.
29. 🟡 Sustainable pricing that does not sell clinician attention.
30. 🟡 Provider burnout measurement with safety safeguards.
31. 🟡 Nursing/pharmacy/allied-health role-specific tools.
32. 🟡 Community/rural resource-aware recommendations.
33. 🟡 Offline emergency evidence.
34. 🟡 Evidence translation to operational order sets.
35. 🟡 Consented genomic/family-history contextualisation.
36. 🟡 Continuous remote-monitoring clinical significance.
37. 🟡 Post-market clinical model surveillance.
38. 🟡 Source-access rights transparency.
39. 🟡 Economic and equity impact measurement.
40. 🟡 Clinical quality-review queue for model outputs.
41. 🟡 Explainable risk prediction with calibration.
42. 🟡 Machine-readable guideline versioning.
43. 🟡 High-risk pediatric dosage guardrails.
44. 🟡 Cross-specialty multi-morbidity decision support.
45. 🟡 Patient communication preference/health-literacy adaptation.
46. 🟡 Respectful patient data correction/dispute process.
47. 🟡 Enterprise-wide evidence governance.
48. 🟡 Clinician training and competency support around AI outputs.
49. 🟡 Product-level clinical safety transparency.
50. 🟡 Trusted longitudinal health intelligence for emerging markets including India.

## 23.6 Top 20 blue-ocean opportunities

1. 🟡 A patient-owned, provider-usable longitudinal evidence ledger.
2. 🟡 “Evidence applicability score” for a specific person, not generic confidence.
3. 🟡 Cross-system medication safety/deprescribing navigator.
4. 🟡 Closed-loop abnormal-result and follow-up intelligence.
5. 🟡 India-first multilingual longitudinal health record and clinician evidence layer.
6. 🟡 Consent-native family/caregiver care coordination.
7. 🟡 Clinical AI safety operating system for hospitals.
8. 🟡 Evidence-to-payer automated medical-necessity workflow.
9. 🟡 Equity-aware trial/referral access navigation.
10. 🟡 Longitudinal chronic-disease digital case conference.
11. 🟡 Patient-facing “why this plan” evidence explainer with clinician co-sign.
12. 🟡 Care transition monitor spanning hospital, lab, pharmacy and home data.
13. 🟡 Local-guideline compilation and executable pathway marketplace.
14. 🟡 Provenance-safe multimodal timeline for labs, reports, images and documents.
15. 🟡 Independent evaluation and audit network for clinical AI.
16. 🟡 Community health worker/primary-care evidence workflow in low-resource settings.
17. 🟡 Longitudinal adverse-effect and treatment-response learning network with consent.
18. 🟡 AI-assisted clinical governance co-pilot for hospital committees.
19. 🟡 Privacy-preserving federated evidence applicability analytics.
20. 🟡 A “do not know yet” care pathway that routes uncertainty to test, expert or follow-up.

## 23.7 Recommended Ovexis MVP

🟡 **MVP category:** “Longitudinal Evidence-to-Action Workspace for complex chronic care and care transitions.”

🟡 **User:** One clinical champion team (e.g., primary care + care coordinator + pharmacist) and consenting patients with multi-morbidity, polypharmacy and fragmented records.

🟡 **MVP scope:** (1) patient-authorised record import; (2) provenance-preserving normalised timeline for problems/medications/labs/documents; (3) clinical question composer tied to selected timeline facts; (4) curated evidence retrieval with claim-level source spans; (5) applicability/conflict/missing-data panel; (6) clinician-reviewed action plan with owner/due date; (7) patient-readable plan; (8) audit log.

🟡 **Explicit non-goals:** autonomous diagnosis, autonomous prescribing, broad general-purpose chat, paid point-of-care advertising, generic wearable dashboard, patient emergency triage, and direct EHR write-back before governance validation.

🟡 **MVP success metrics:** time to reconcile chart; percentage of claims with supporting source span; citation entailment pass rate; clinician correction rate; time to close follow-up task; medication discrepancy detection; patient understanding; safety escalations; 30/90-day care-gap closure. Do not use “messages sent” or “tokens generated” as primary success.

## 23.8 Recommended GTM, moat, integrations, pricing and roadmap

🟡 **GTM:** Start with 2–4 design-partner care teams in one geography and one measurable care-transition/chronic-care pathway. Sell safety, reconciliation and closed-loop care—not AI novelty. Publish a jointly governed prospective evaluation.

🟡 **Moat:** Build the **longitudinal provenance graph + patient consent graph + local clinical-policy graph + outcome/feedback graph**. This combination is harder to copy than an LLM/RAG stack.

🟡 **Integrations priority:** (1) FHIR/SMART-on-FHIR read-only EHR launch; (2) C-CDA/document ingestion; (3) labs; (4) pharmacy/medication history; (5) patient consent/identity; (6) secure communications; (7) claims; (8) wearables only when clinically justified.

🟡 **AI architecture:** Risk router → structured patient fact extractor with evidence/provenance → retrieval from versioned authoritative corpus + local policy → synthesis → independent claim/citation verifier → contraindication/temporal conflict rules → clinician review → decision/action ledger → post-action monitoring. Use smaller specialised models where proven; use frontier models only behind evaluation and constrained tools.

🟡 **Pricing:** Offer transparent B2B pricing per enrolled complex-care patient or care-team seat, with a platform minimum and no advertising in clinical decision surfaces. Include a free limited patient access tier paid for by the provider organisation, not by sale of patient attention.

🟡 **Roadmap:** 0–6 months: timeline/evidence/action MVP. 6–12: local policy, care tasks, FHIR deployment and evaluation. 12–24: pharmacy/lab/claims reconciliation, referral/trial modules, multilingual India region. 24–36: federated outcome learning, regional clinical governance and scalable consumer-consented record portability.

---

# 24. Final board recommendations

1. 🟡 Treat OpenEvidence as a credible leader in **evidence retrieval and clinician PLG**, not as proof that clinical reasoning is solved.
2. 🟡 Respect its licensed-content and distribution moat; do not spend Ovexis’s first year on undifferentiated medical search.
3. 🟡 Build patient longitudinal context, provenance and closed-loop action as Ovexis’s core product—not an integration afterthought.
4. 🟡 Require every recommendation to show evidence support, applicability, uncertainty, alternatives and accountable next step.
5. 🟡 Make safety/clinical governance product surfaces that clinicians and boards can inspect.
6. 🟡 Adopt a transparent business model that protects clinical trust; avoid advertising in decision paths.
7. 🟡 Start narrow and measure prospective impact with health-system partners before broadening capability claims.
8. 🟡 Design for Indian/global data fragmentation and multilingual/local-guideline realities from the beginning; OpenEvidence’s U.S.-centred/European availability history is a warning.

---

# 25. Evidence register and references

🟢 **Evidence quality legend:** A = first-party primary/company/legal document; B = reputable independent reporting or app store; C = preprint/community/competitor or analyst source, used with explicit limitation; D = research boundary/no source found. “Screenshot” denotes public visual evidence linked in source, not a capture of authenticated UI.

| ID | Source | Type | Key public evidence used | Confidence | Screenshot / observation |
|---|---|---|---|---|---|
| E01 | [OpenEvidence Home & About](https://www.openevidence.com/about) | A | Mission, team, advisors, society/content logos, free access. | High | Public page/brand assets observed. |
| E02 | [OpenEvidence Home](https://www.openevidence.com/) | A | Public marketing, mobile, investor logos, cookie banner. | High | Public page observed. |
| E03 | [Announcements index](https://www.openevidence.com/announcements) | A | Partnership/release chronology through July 2026. | High | Public announcement thumbnails. |
| E04 | [OpenEvidence security](https://www.openevidence.com/security) | A | HIPAA/SOC2 claim, GCP/Vercel, encryption, tests/policies. | High for self-report | Text-only public observation. |
| E05 | [Series B + DeepConsult](https://www.openevidence.com/announcements/openevidence-the-fastest-growing-application-for-physicians-in-history-announces-dollar210-million-round-at-dollar35-billion-valuation) | A | Funding, adoption claims, evidence search, DeepConsult. | High for announcement | Public release. |
| E06 | [Visits](https://www.openevidence.com/announcements/visits-real-time-medical-intelligence) | A | Transcription, templates, documents, context query. | High | Public product images. |
| E07 | [Dialer full release](https://www.openevidence.com/announcements/messaging-faxing-and-voicemail-are-now-live-in-the-openevidence-dialer) | A | Calls, texts, fax, voicemail, Create Visit. | High | Public product image. |
| E08 | [Clinical Trial Matching](https://www.openevidence.com/announcements/new-feature-clinical-trials-matching-in-openevidence) | A | Trial matching attributes and locations. | High | Public product images. |
| E09 | [EvidenceGrade technical post](https://www.openevidence.com/blog/introducing-evidencegrade-grading-the-strength-of-medical-evidence-in-real-time) | A | GRADE-inspired two-phase grading/retrieval discussion. | High for method description | Public diagrams. |
| E10 | [OpenEvidence 2.0](https://www.openevidence.com/announcements/openevidence-20) | A | Prior auth, handouts, calculators, modules. | High | Public product image. |
| E11 | [Microsoft / Dragon Copilot](https://www.openevidence.com/announcements/openevidence-collaborates-with-microsoft-to-expand-ai-leadership-in-healthcare-bringing-clinical-evidence-and-guidelines-to-enterprise-clinician-workflows) | A | Planned Dragon integration, adoption claims. | High for announcement | Public release image. |
| E12 | [Wiley / Cochrane](https://www.openevidence.com/announcements/wiley-and-openevidence-partner-to-deliver-trusted-research-to-physicians-at-the-point-of-care) | A | Wiley, Cochrane, 400+ journals/books, evidence layer. | High | Public release image. |
| E13 | [Privacy policy](https://www.openevidence.com/policies/privacy) | A | Registration, advertising/profile/data use, questions/PHI claims, transfers. | High | Public policy. |
| E14 | [Terms](https://www.openevidence.com/policies/terms) | A | Registration, professional use, disclaimer, User Content/data terms. | High | Public policy. |
| E15 | [Security / trust centre](https://trust.openevidence.com/) | A | Security/compliance controls. | High for self-report | Public trust portal. |
| E16 | [Amaro acquisition release](https://www.prnewswire.com/news-releases/openevidence-acquires-google-ventures-backed-ai-startup-amaro-302547047.html) | A/B | AI advertising acquisition/rationale. | High | Public PR release. |
| E17 | [Mergr Amaro transaction](https://mergr.com/transaction/openevidence-acquires-amaro) | C | Reported transaction date. | Medium | Text listing. |
| E18 | [NEJM Group content agreement](https://www.openevidence.com/announcements/openevidence-and-nejm) | A | NEJM full text/multimedia from 1990. | High | Public release. |
| E19 | [JAMA content agreement](https://www.openevidence.com/announcements/openevidence-and-the-jama-network-sign-strategic-content-agreement) | A | JAMA/JAMA Network content agreement. | High | Public release. |
| E20 | [medRxiv complex-question evaluation](https://www.medrxiv.org/content/10.64898/2025.11.29.25341091v1.full.pdf) | C | Preprint performance/repeatability caution. | Medium; preprint | PDF, not product screenshot. |
| E21 | [Nature Medicine independent evaluation](https://www.nature.com/articles/s41591-026-04431-5) | B | Benchmark comparison against frontier models. | High for reported study | Article figures. |
| E22 | [r/medicine discussion](https://www.reddit.com/r/medicine/comments/1mslx0z/openevidence_not_quite_as_accurate_as_id_have/) | C | Clinician anecdotal praise/caution. | Low for incidence | Community comments. |
| E23 | [CNBC Series D](https://www.cnbc.com/2026/01/21/openevidence-chatgpt-for-doctors-doubles-valuation-to-12-billion.html) | B | Series D, leadership, revenue/adoption statements. | High | News page. |
| E24 | [Reuters Series D](https://www.reuters.com/business/healthcare-pharmaceuticals/medical-ai-startup-openevidence-doubles-valuation-12-billion-latest-round-2026-01-21/) | B | Funding/valuation confirmation. | High | News page. |
| E25 | [Series C reporting](https://www.fiercehealthcare.com/ai-and-machine-learning/open-evidence-raises-200m-6b-valuation-rapid-adoption-doctors-continues) | B | Series C/adoption reporting. | Medium–High | News page. |
| E26 | [BusinessWire Series D](https://www.businesswire.com/news/home/20260121029132/en/OpenEvidence-Raises-$250-Million-to-Build-Medical-Superintelligence-for-Doctors) | A | Multi-model/conductor architecture. | High for company claim | PR release. |
| E27 | [Reported $20B fundraising](https://www.digitalhealthnews.com/openevidence-reportedly-seeks-200m-funding-at-20b-valuation-amid-rapid-ai-healthcare-growth) | C | Unconfirmed financing rumour. | Low | News page. |
| E28 | [CHIL Best Paper](https://www.openevidence.com/announcements/openevidence-wins-best-paper-award-at-chil-2023) | A | Research paper/award. | High | Public release. |
| E29 | [iOS/Android launch](https://www.openevidence.com/announcements/openevidence-is-now-available-for-ios-and-android) | A | Mobile availability. | High | Public release. |
| E30 | [HIPAA announcement](https://www.openevidence.com/announcements/openevidence-is-now-hipaa-compliant) | A | BAA, PHI, conversation sharing. | High for company claim | Public release. |
| E31 | [Veeva/Open Vista](https://www.openevidence.com/announcements/openevidence-and-veeva-announce-open-vista-partnership) | A | Life-sciences partnership. | High | Public release. |
| E32 | [Dialer initial release](https://www.openevidence.com/announcements/openevidence-hipaa-secure-dialer-now-available) | A | Initial iOS/Android dialer features. | High | Public release. |
| E33 | [Sutter / Epic](https://www.openevidence.com/announcements/sutter-health-collaborates-with-openevidence-to-bring-evidence-based-ai-powered-insights-into-physician-workflows) | A | Epic workflow launch. | High | Public release image. |
| E34 | [NCCN collaboration](https://www.openevidence.com/announcements/openevidence-collaborates-with-nccn-to-integrate-canonical-oncology-treatment-algorithms-at-the-point-of-care) | A | NCCN guidelines/algorithms. | High | Public release. |
| E35 | [Cedars-Sinai patient-aware AI](https://www.openevidence.com/announcements/openevidence-partners-with-cedars-sinai-to-create-patient-aware-clinical-intelligence-with-agentic-clinical-ai) | A | Epic context and session non-storage claim. | High for announcement | Public release image. |
| E36 | [NYP/Columbia/Weill Cornell](https://www.openevidence.com/announcements/openevidence-and-newyork-presbyterian-columbia-university-and-weill-cornell-medicine-expand-clinical-ai-tools-across-new-york-city-and-westchester) | A | NYC health-system collaboration. | High | Public announcement. |
| E37 | [Contrary company research](https://research.contrary.com/company/openevidence) | C | Founder/Kensho background and market analysis. | Medium | Analyst page. |
| E38 | [Apple App Store](https://apps.apple.com/us/app/openevidence/id6612007783) | B | Mobile description/features/rating snapshot. | Medium–High | Store screenshots are public. |
| E39 | [Google Play](https://play.google.com/store/apps/details?id=com.openevidence) | B | Android availability, verification, data-safety label/rating. | Medium–High | Store screenshots are public. |
| E40 | [BAA](https://www.openevidence.com/policies/baa) | A | PHI obligations, safeguards, subcontractors, breach terms. | High | Public legal text. |
| E41 | [100% USMLE announcement](https://www.openevidence.com/announcements/openevidence-creates-the-first-ai-in-history-to-score-a-perfect-100percent-on-the-united-states-medical-licensing-examination-usmle) | A | Benchmark claim. | High for claim | Public announcement. |
| E42 | [r/hospitalist discussion](https://www.reddit.com/r/hospitalist/comments/1je4ria/open_evidence/) | C | Citation mismatch anecdote/company response. | Low for incidence | Community comments. |
| E43 | [r/Residency discussion](https://www.reddit.com/r/Residency/comments/1nofa70/open_evidence_examples_of_ai_hallucination/) | C | Rare disease/specialty caution. | Low for incidence | Community comments. |
| E44 | [Lancet Regional Health Europe geoblocking note](https://www.thelancet.com/journals/lanepe/article/PIIS2666-7762(26)00130-4/fulltext) | B | EU/UK availability/regulatory uncertainty reporting. | Medium–High | Article page. |
| E45 | [NBC coverage](https://www.nbcnews.com/tech/tech-news/openevidence-ai-doctor-medical-physician-login-app-what-npi-uptodate-rcna341064) | B | Free/ad-supported model and expansion commentary. | High | News page. |
| E46 | [Research Scientist job](https://jobs.ashbyhq.com/openevidence/80ca886f-2c07-43b2-8978-07c37542a207) | A | Team/culture/evaluation/in-person claims. | High for employer claim | Job posting. |
| E47 | [Data Infrastructure job](https://jobs.thrivecap.com/companies/openevidence-2/jobs/81122458-software-engineer-data-infrastructure) | A/B | Data-infrastructure/culture signal. | High for employer claim | Job posting. |
| E48 | [Superpower](https://superpower.com/) | A | Comparator category reference. | Low–Medium | Vendor page not feature audited. |
| E49 | [Function Health](https://www.functionhealth.com/) | A | Comparator category reference. | Low–Medium | Vendor page not feature audited. |
| E50 | [Levels](https://www.levels.com/) | A | Comparator category reference. | Low–Medium | Vendor page not feature audited. |
| E51 | [Glass Health](https://glass.health/) | A | Comparator category reference. | Low–Medium | Vendor page not feature audited. |
| E52 | [Atropos Health](https://www.atroposhealth.com/) | A | Comparator category reference. | Low–Medium | Vendor page not feature audited. |
| E53 | [AMBOSS](https://www.amboss.com/) | A | Comparator category reference. | Low–Medium | Vendor page not feature audited. |
| E54 | [UpToDate](https://www.wolterskluwer.com/en/solutions/uptodate) | A | Comparator category reference. | Low–Medium | Vendor page not feature audited. |
| E55 | [Apollo 24|7](https://www.apollo247.com/) | A | Comparator category reference. | Low–Medium | Vendor page not feature audited. |
| E56 | [Practo](https://www.practo.com/) | A | Comparator category reference. | Low–Medium | Vendor page not feature audited. |
| E57 | [Tata 1mg](https://www.1mg.com/) | A | Comparator category reference. | Low–Medium | Vendor page not feature audited. |
| E58 | [Apple Health](https://www.apple.com/health/) | A | Comparator category reference. | Low–Medium | Vendor page not feature audited. |
| E59 | [Android Health Connect](https://developer.android.com/health-and-fitness/guides/health-connect) | A | Comparator/interoperability reference. | Low–Medium | Developer page. |
| E60 | Research boundary | D | No public evidence found in reviewed sources for asserted absent docs/features. | N/A | No screenshot. |
| E61 | [Human API](https://www.humanapi.co/) | A | Comparator category reference. | Low–Medium | Vendor page not feature audited. |
| E62 | [WHOOP](https://www.whoop.com/) | A | Comparator category reference. | Low–Medium | Vendor page not feature audited. |
| E63 | [Oura](https://ouraring.com/) | A | Comparator category reference. | Low–Medium | Vendor page not feature audited. |
| E64 | [Ultrahuman](https://www.ultrahuman.com/) | A | Comparator category reference. | Low–Medium | Vendor page not feature audited. |

---

## Appendix A — research questions for management diligence

1. 🟡 What percentage of atomic output claims pass automated and clinician-reviewed citation-entailment tests by specialty/risk tier?
2. 🟡 What percentage of material claims have complete citations, and how are source conflicts handled?
3. 🟡 What is the retrieval corpus inventory, source hierarchy, update SLA, revision/withdrawal handling, rights restriction and regional availability policy?
4. 🟡 Which base models, specialised models, tools and providers are used per product; what data can each see; and how are prompts/outputs retained?
5. 🟡 What is the versioned evaluation suite for point-of-care, patient-context, documentation, trial matching and communications scenarios?
6. 🟡 What is the model-error correction/rollback SLA and clinician-visible changelog?
7. 🟡 How are patient facts extracted, temporally resolved, deduplicated, source-scored and presented for confirmation?
8. 🟡 What exact EHR standards/resources/scopes are used; are integrations read-only; where is PHI retained; and who can audit?
9. 🟡 What is the data retention/deletion policy per chat, Visit, document, call, fax, transcript, trial query, backup and telemetry record?
10. 🟡 Are any user inputs, outputs or de-identified derivatives used for model training, product analytics, advertiser segmentation or third-party sharing by product/contract?
11. 🟡 How are advertising surfaces separated from treatment/evidence rank; is there a written clinical-commercial firewall?
12. 🟡 What is net revenue retention, active clinician retention, compute cost/query, content cost, ad fill/yield, and enterprise gross margin?
13. 🟡 Which SOC 2 controls are in scope, which exceptions exist, and what is the current pen-test/incident history?
14. 🟡 What safety case supports each jurisdiction and intended-use statement, including FDA, EU AI Act/MDR, UK and India?
15. 🟡 What prospective evidence shows improved decision quality, time, equity or patient outcomes without increased overreliance?

## Appendix B — deliverables index

🟢 **Executive Summary:** Sections 1 and 24.  
🟢 **Company Intelligence / Founder Psychology:** Sections 2–3.  
🟢 **Product/User/UX/Healthcare workflow:** Sections 4–7.  
🟢 **AI/Technical/API/Security:** Sections 8–10.  
🟢 **Business/Growth/Hiring/Customer:** Sections 11–13.  
🟢 **Competitive landscape/Moat/Frameworks:** Sections 14–16.  
🟢 **Decision ledger/Dependency/Roadmap/Risk/Attack/Future:** Sections 17–22.  
🟢 **Ovexis recommendations, 50-idea sets and blue oceans:** Section 23.  
🟢 **Evidence Register/References:** Section 25.  
🟢 **Master Feature Inventory spreadsheet:** Companion workbook `OpenEvidence_Master_Feature_Inventory_2026-07-25.xlsx`.
