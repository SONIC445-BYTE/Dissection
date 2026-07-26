# SUPERPOWER — COMPETITIVE INTELLIGENCE DOSSIER
### Prepared for the Ovexis Board · Evidence-Based Reverse-Engineering Assessment

**Target:** Superpower Health, Inc. (superpower.com)
**Category:** Preventive Healthcare · Longevity · AI Health OS · Biomarker Intelligence
**Report date:** 25 July 2026
**Classification:** Internal — Board Strategy

---

## EVIDENCE STANDARD

Every material statement carries one of three labels. They are never blended within a sentence.

| Label | Meaning | Standard of proof |
|---|---|---|
| 🟢 **Confirmed** | Directly observed in a public artifact | Live HTTP response, public JS bundle string, published page text, court docket, or on-record press statement |
| 🟡 **Strong Inference** | Not stated, but strongly implied by observed artifacts | Reasoned from multiple confirmed data points; alternative explanations considered and noted |
| 🔴 **Speculation** | Analytical hypothesis | Explicitly flagged; must not be treated as fact |

**Method.** All evidence was gathered from publicly accessible surfaces: the marketing site, its four XML sitemaps, the publicly served JavaScript bundle of the member application (304 chunks, ~11 MB, retrieved as any browser would), unauthenticated HTTP response headers, DNS, public court dockets, public job listings, and press. `robots.txt` is fully permissive (`User-agent: * / Allow: /`) — 🟢 Confirmed. **No authentication was attempted, no account was created, no rate limit was stressed, no non-public endpoint was accessed, and no PHI was viewed.** Reading a bundle a web server voluntarily transmits to every visitor is the same act a browser performs; it is the boundary of this investigation and it was not crossed.

**A note on what could not be verified.** Server-side model providers, actual prompt text, database engines, SOC 2 status, revenue, member counts, retention curves, CAC/LTV, and margins are not publicly disclosed. Where these matter, the report says so plainly rather than inventing a number. Two companies on the requested comparison list — **Regacore** and **PreventiveHealth.ai** — returned no reliable public information; they are marked 🔴 and left blank rather than fabricated.

---

# DELIVERABLE 1 — EXECUTIVE SUMMARY

## 1.1 What they are building

Superpower is assembling a **consumer health operating system** whose entry point is a cheap, comprehensive blood panel and whose end state is an AI clinician with a permanent memory of your body.

The company describes its own construction sequence with unusual candour in a public job posting: *"We started with lab testing, then data aggregation / digital twin, then an AI doctor, and now peptides."* — 🟢 Confirmed (Ashby job listing, "Engineering @ Superpower").

That single sentence is the most strategically revealing artifact in this entire investigation. It tells you the panel was never the product. The panel is the **customer-acquisition instrument that creates a proprietary longitudinal dataset**, which trains and grounds an AI layer, which in turn distributes high-margin therapeutics. Each stage funds and feeds the next.

The current commercial expression — 🟢 Confirmed from the live homepage on 25 July 2026:

> *"Your new health membership. Members start with 100+ lab tests. $199 per year."*

And the framing that reveals the pricing psychology:

> *"What could cost $10,000 is now $199."*

## 1.2 Why it exists — the founding wound

Three founders, three independent collisions with diagnostic failure — 🟢 Confirmed across TechCrunch, Forbes and Business Insider:

- **Jacob Peters** (co-founder, CEO until 2025-26) nearly died after conditions went undiagnosed by multiple specialists; reported ~$2M in medical bills, months hospitalized, and the loss of part of his stomach.
- **Max Marchione** (co-founder; now CEO — 🟢 Confirmed via Business Wire and the CEO-signed `/why` letter) reported decades of misdiagnosis across more than 20 doctors.
- **Kevin Unkrich** (co-founder, CTO) lost his best friend to a brain tumour in his teens — two days before a scheduled MRI.

This is not decorative origin-story marketing. It is the **causal explanation for nearly every product decision** documented in Deliverable 4. A company founded on "the system did not look, and looking would have saved me" will systematically over-index on *measuring more* and under-index on *the harms of measuring indiscriminately*. That bias is simultaneously their growth engine and their deepest clinical vulnerability.

## 1.3 The four problems

**The customer problem.** A standard annual physical measures roughly 10–15 markers and acts only after symptoms appear. Comprehensive testing is gated behind insurance authorization, specialist referral, or a concierge membership costing multiples of rent. 🟢 Confirmed as the company's own framing (Business Wire, Giannis Antetokounmpo announcement).

**The emotional problem.** This is the one they solve best, and it is worth naming precisely: **the loneliness of being dismissed.** Their own member testimonials are not about biomarkers — they are about vindication. 🟢 Confirmed from the live homepage:

> *"I left the appointment feeling like I was being dramatic. I wasn't being dramatic. I was being responsible."* — Camelia, 29
> *"They told me I was overthinking my genetic risk of diabetes but when I tested with Superpower I found my A1c was really high."* — Thach, 37

The product sells **agency and validation**. The blood panel is the receipt that proves you were not imagining it. Their claim that *"60% of members said Superpower identified something previously missed or overlooked by a doctor"* (🟡 self-reported, methodology undisclosed) is engineered precisely to promise that vindication.

**The operational problem.** Health data is scattered across portals, PDFs, labs, wearables and clinics that do not speak to each other. Their answer is aggressive centralization: lab PDF upload with AI ingestion, wearable sync, records vault, and even conversation import from other AI assistants — all 🟢 Confirmed in the bundle.

**The economic problem.** Prevention has no payer. Insurance reimburses treatment, not foresight. Superpower's answer is to bypass insurance entirely — cash-pay, HSA/FSA-eligible, with the tax advantage functioning as an effective 25–35% discount. 🟢 Confirmed ("HSA/FSA eligible" on homepage).

## 1.4 Who is — and is not — the customer

**Is:** Health-motivated adults roughly 25–45 with discretionary income and an existing sense that something is off; quantified-self and longevity-adjacent consumers; gift purchasers (🟢 `/sp-2-0---gift`, `/mothers-day`, `/v-day`); and increasingly employers and teams (🟢 `/organizations`, Thatch, Wellhub, SoulCycle).

**Is not** — and this is where Ovexis should look hardest:
- The acutely ill — 🟢 Confirmed by their own disclaimer that Superpower is not a substitute for primary or emergency care
- Complex chronic and multi-morbid patients, where longitudinal intelligence would deliver the *most* clinical value
- Medicare-age populations — the largest actual disease burden
- The genuinely price-sensitive, even at $199
- Anyone outside the United States — 🟢 US-only; `/locations` covers US states exclusively
- Physicians as a primary user — there is **no clinician-facing product**, a structural gap discussed in Deliverable 21

## 1.5 Category creation and category replacement

**Creating:** "Health Intelligence" — their own term. 🟢 Confirmed from `/roadmap`: *"This is health intelligence."* And from `/why`: *"The first health system built on intelligence, not discipline."*

The positioning is sophisticated. It explicitly repudiates the optimization-culture competitors it resembles:

> *"Then came the celebrity protocols and hyper-disciplined systems... Do 100 things perfectly. Follow my exact regimen... Most people didn't get healthier. They burned out."* — 🟢 `/why`

They are attempting to be **the anti-Bryan-Johnson longevity company**: intelligence instead of discipline, 3–5 actions instead of 50. This is a genuinely strong strategic insight and the single best idea in their arsenal.

**Replacing:** the annual physical, the concierge-medicine membership ($2,000–$10,000/yr), the direct-to-consumer lab (InsideTracker, Everlywell), Dr. Google, and — most ambitiously — the general-purpose LLM as the first place people take a health question. That last one is explicit in the product: they built a flow to import your ChatGPT, Claude, Gemini, Perplexity and Grok conversations. 🟢 Confirmed.

Their stated ambition, 🟢 Confirmed from `/roadmap`:
> *"1. Be the front door – before doctors or Google. 2. Prevent disease & enhance human capability. 3. Deliver care via AI. 4. Feel more like Apple or Tesla than a hospital."*

## 1.6 Jobs-To-Be-Done

| # | Job (customer's words) | Functional | Emotional | Social | How well served |
|---|---|---|---|---|---|
| 1 | "Tell me if something is wrong before it's too late" | Comprehensive screening | Relief from dread | Responsible adult | **Strong** — the core competency |
| 2 | "Prove I'm not imagining this" | Objective measurement | Vindication | Credibility with doctors and family | **Strongest** — their real product |
| 3 | "Tell me what to actually do" | Prioritized protocol | Reduced overwhelm | Competence | **Medium** — evidence tiers unclear; commerce conflict |
| 4 | "Put my scattered health data in one place" | Aggregation + normalization | Control | — | **Strong** — genuine engineering depth |
| 5 | "Answer my question at 2am without judgment" | 24/7 AI + care team | Safety, no embarrassment | — | **Medium-High** — support quality complaints documented |
| 6 | "Help me get the drug/supplement I want" | Rx + marketplace | Access | Insider status | **Strong commercially, weak on conflict-of-interest** |
| 7 | "Show me I'm improving" | Trend tracking, scores | Progress, motivation | Shareable | **Medium** — gated behind paid retests |
| 8 | "Help me protect my family" | Family risk insights | Love, duty | Provider role | **Medium** — undermined by public-URL PHI design |

**The strategic read:** Job #2 is the emotional engine, and it is the one Ovexis must match. Jobs #3 and #7 are where Superpower is structurally weakest — protocol credibility is compromised by the marketplace conflict, and progress tracking is behind a paywall that suppresses the exact behavior that would build their data moat. **Those are the two openings.**

## 1.7 Core philosophy — decoded from their own words

Five beliefs, each 🟢 Confirmed by direct quotation:

1. **Measurement precedes agency.** *"No more guesswork. No 'optimizing in the dark.'"* (`/roadmap`)
2. **The system is designed for adequacy, not excellence.** *"Today's healthcare system is designed to make you fine, not better."* (`/roadmap`)
3. **Intelligence should replace discipline.** *"Health doesn't need more discipline. It needs more intelligence."* (`/why`)
4. **Brand is the durable moat.** Peters: *"in a world where AI and technology make it easier to replicate products, brand becomes one of the most powerful moats a company can have."* (Sourcery VC)
5. **Consumer experience is the benchmark, not clinical convention.** *"Feel more like Apple or Tesla than a hospital."* (`/roadmap`)

**Board-level assessment:** Belief #4 is the strategic error Ovexis should exploit. In consumer retail, brand is a moat. In healthcare, **brand is a liability multiplier** — it converts a single clinical or advertising failure into an existential trust event. The Function Health lawsuit (Deliverable 2) is the first demonstration of exactly this dynamic. A company that believes brand is its moat will spend on brand; a company that understands trust is the moat will spend on clinical validation. **Ovexis should be the second company.**

---

# DELIVERABLE 2 — COMPANY INTELLIGENCE

## 2.1 Timeline

| Date | Event | Confidence |
|---|---|---|
| Early 2023 | Founded by Jacob Peters, Max Marchione, Kevin Unkrich. *(Note: Tracxn lists 2022, PitchBook/CB Insights list 2023; the company's own schema.org markup says 2021. The 2023 date is used by TechCrunch, Forbes and the founders themselves.)* | 🟢 Confirmed (2023); 🟡 conflicting registry data noted |
| 2023–24 | Nationwide platform assembled; "hundreds" of testing/treatment partners; beta membership | 🟢 Confirmed (BusinessWire) |
| 21 May 2024 | **$4M pre-seed**, led by Susa Ventures. Long Journey, Family Fund, Atman VC, 24 Carrot, Focalpoint, Seaside. Angels: Cameron & Tyler Winklevoss, Balaji Srinivasan, Scott & Cyan Banister, Evan Moore (DoorDash) | 🟢 Confirmed |
| Jan 2025 | **Acquires Feminade** — women's hormonal health (PCOS, perimenopause, fertility protocols) | 🟢 Confirmed |
| 22 Apr 2025 | **$30M Series A**, led by Forerunner Ventures (Kirsten Green). Day One, Susa, Long Journey, Family Fund, Opal, Valia, Visible, Winklevoss Capital. Reported ~$200M valuation. Nearly 2x oversubscribed. 100–150k waitlist | 🟢 Confirmed |
| May 2025 | **Acquires Base** (Lola Priego, ex-Amazon) — at-home testing + nutrition data; ~90,000 users; bought explicitly for diet/hormone datasets to "save us a lot of clinical R&D" | 🟢 Confirmed |
| Sept 2025 | Hires **Dr. Anant Vinjamoori** as Chief Longevity Officer (ex-Virta Health, ex-CMO Modern Age) | 🟢 Confirmed |
| Oct 2025 | **Thatch partnership** — employer benefits channel at ~$179/yr | 🟡 Strong Inference (Sacra) |
| Dec 2025 | Marchione publishes `/roadmap` manifesto — digital twin thesis made public | 🟢 Confirmed |
| Nov 2025 | *Competitive context:* Function Health raises **$298M at $2.5B** | 🟢 Confirmed |
| 26 Jan 2026 | **Function Health sues Superpower** — Case 2:26-cv-00810, C.D. Cal. Lanham Act false advertising + unfair competition | 🟢 Confirmed (docket) |
| Feb 2026 | Superpower retains Paul Weiss (Walter F. Brown Jr., Randall S. Luskey). Response deadline extended twice, to 24 Apr 2026 | 🟢 Confirmed (docket) |
| Feb 2026 | **AI Doctor formally launched** — 247 commits, ~140,000 lines of code, compressed-memory architecture, inline citations, "Think" tab | 🟢 Confirmed (Anadolu/Türkiye Today) |
| Mar 2026 | Business Insider profile; peptide culture reporting | 🟢 Confirmed |
| ~2025-26 | **Max Marchione becomes CEO** (Peters was CEO through May 2025) | 🟢 Confirmed |
| Jun 2026 | Comparison pages updated with derived-metric disclaimers — visible litigation response | 🟢 Confirmed |
| Jul 2026 | Live: $199/yr, "2,000+ Quest locations," peptides waitlist, iOS app shipped | 🟢 Confirmed |

## 2.2 Funding and valuation — with an honest caveat

| Source | Total raised | Valuation |
|---|---|---|
| CB Insights / PitchBook | $34M | $150M (PremierAlts) |
| Tracxn | $51M | undisclosed |
| Capital Brief | USD 51M | — |
| SmartCompany | US$47M Series A | >$300M |
| Company (own job post) | "over $40 million" | — |

🟡 **Strong Inference: total raised is approximately $47–51M; valuation most likely $200–350M.** The sources genuinely conflict and no authoritative filing is public. **Ovexis should not model off a precise figure.** The strategically important fact is not the exact number — it is the **ratio**: Function Health has raised roughly 6x more capital ($298M Series B at $2.5B) than Superpower has raised in total. 🟢 Confirmed.

**Investor roster** (🟢 Confirmed, largely from the company's own job posting): Forerunner Ventures (lead A; Kirsten Green — also behind Oura, Hims, Prenuvo), 8VC, Bond Capital, Susa Ventures, Long Journey Ventures, Airtree, Day One, Opal, Valia, Visible, Winklevoss Capital. Angels: Balaji Srinivasan, Cyan Banister, Evan Moore, Arielle Zuckerberg, Shaan Puri, Justin Mares. Celebrity/athlete: Giannis Antetokounmpo (Global Brand Ambassador), Kylian Mbappé, Logan Paul, Steve Aoki, Vanessa Hudgens, Brooke Monke.

**Read:** Forerunner's involvement is the signal that matters. Their thesis is consumer brand in health — they backed Oura and Hims. This confirms Superpower is being underwritten as **a consumer brand company that happens to do healthcare**, not a clinical company. That underwriting choice cascades into everything: the celebrity roster, the brand spend, the marketing aggression that produced the lawsuit.

## 2.3 The litigation — the single most important development

**Function Health, Inc. v. Superpower Health Inc.**, Case 2:26-cv-00810, C.D. Cal., filed 26 January 2026. Judge John F. Walter; Magistrate Daniel S. Roberts. Plaintiff counsel: Cooley LLP. Defense: Paul Weiss. 🟢 Confirmed via public docket.

**Allegations** (🟢 Confirmed as *allegations* — untested in court, and Superpower has not yet filed its answer as of the last docket entry reviewed):

1. **The "100+" claim.** Function alleges Superpower's membership delivers **~55 direct laboratory measurements**, with the balance of the "100+" comprising calculated ratios and indices — *"derivative data created by recombining existing lab values into ratios or indices without performing any new tests or measuring any new biological signals."*
2. **The "3,000+ locations" claim.** Function alleges Quest — the shared testing partner — operates ~2,250 patient service centers.
3. **Comparative advertising** alleged to misrepresent both platforms.
4. **An edited Reddit post** alleged to have been used in paid advertising without the author's consent.
5. **"Flippant disregard for legal and regulatory safeguards"**, citing Marchione's recorded statements that employees inject each other with compounds at Friday breakfasts *"because we think it's fun."*

**Independent corroboration of the substance.** I verified the derived-metric issue directly, without relying on the complaint. Superpower's own sitemap publishes these as `/biomarkers/` pages — 🟢 Confirmed: `castelli-risk-index-i`, `castelli-risk-index-ii`, `atherogenic-index-plasma`, `atherogenic-coefficient`, `free-androgen-index`, `crp-to-albumin-ratio`, `ferritin-to-albumin-ratio`, `bilirubin-to-albumin-ratio`, `ggt-to-hdl-c-ratio`, `indirect-to-direct-bilirubin-ratio`, `corrected-calcium-albumin-adjusted`. **These are arithmetic transformations of other values, published in the same namespace as measured analytes.** The allegation has a factual basis in their own published information architecture.

**Evidence of behavioral change.** Their comparison page, republished 18 June 2026, now carries footnotes — 🟢 Confirmed verbatim:
> *"\*Includes direct laboratory measurements and calculated health metrics."*
> *"\*Superpower's 100+ combines direct lab measurements with calculated ratios like LMR and Ferritin:Albumin."*

And the homepage now says **"2,000+ Quest locations"** — down from the disputed 3,000+. 🟢 Confirmed.

**Board interpretation.** Litigation is forcing disclosure discipline. Two consequences for Ovexis: (a) the "count everything" marketing tactic now carries a documented legal cost, and (b) **the industry is establishing a precedent on what may be called a biomarker.** Ovexis should adopt the strict definition *now* and market that rigor as a differentiator — arriving early at a standard your competitors are being dragged toward by litigation is free positioning.

## 2.4 Leadership, hiring and organizational read

**Founders:** Max Marchione (CEO; Australian, Sydney), Jacob Peters (co-founder; prior: Commsor ~$70M raised, Launch House, J.P. Morgan), Kevin Unkrich (CTO). Hannah Ahn appears in founding-team photography. 🟢 Confirmed.

**Clinical leadership:** Dr. Anant Vinjamoori (Chief Longevity Officer), Shaun Miller (VP Medical Operations). **Medical Advisory Board:** Dr. Leigh Erin Connealy, Dr. Robert Lufkin (UCLA), Dr. Abe Malkin (Concierge MD). 🟢 Confirmed from homepage.

🟡 **Strong Inference — a governance observation Ovexis should note.** The advisory board is weighted toward integrative and longevity medicine rather than academic evidence-based medicine or clinical epidemiology. This is coherent with the brand but leaves the company without a strong internal voice arguing *against* testing and treating. For a company whose principal clinical risk is overdiagnosis and low-value intervention, **the absence of a skeptic in the governance structure is a structural vulnerability.** Ovexis should deliberately recruit that skeptic — a clinical epidemiologist or evidence-based-medicine specialist with authority to veto — and say so publicly.

**Open roles observed** (🟢 Confirmed via ZipRecruiter/BuiltIn/Ashby, 17 SF roles): Head of Engineering, Chief Marketing Officer, Head of Legal, Chief of Staff, Founding Lead Strategic Sales, Strategic Sales Development Lead, Product Marketing Manager (Lifecycle/Retention), Senior Product Designer, Senior Brand Designer, Growth/Digital Designer, Motion Designer, Creator in Residence (Short-Form Video), Longevity Nurse Practitioner (multi-state, CA required), Member Success Representative, Collaborating Physician (part-time).

**What the hiring pattern reveals** — 🟡 Strong Inference, and it is unusually legible:

- **Hiring a Head of Engineering *after* building the AI Doctor** → engineering has been founder-led and is now hitting a scaling ceiling. Technical debt is accumulating (corroborated by `protocol/legacy` routes coexisting with `protocol-v2`, and `chatv3` search coexisting with `chatv4` messages — 🟢 Confirmed in bundle).
- **Head of Legal as an urgent hire** → direct litigation response. The posting's framing — legal as *"an integrated operating system, not a back-office compliance check"* — signals they now understand regulatory exposure is a product concern.
- **CMO + Creator in Residence + 3 designers** → brand remains the primary investment thesis, consistent with Forerunner's underwriting.
- **Product Marketing Manager, Lifecycle/Retention** → 🟡 **retention is a recognized problem.** You do not hire a dedicated lifecycle-retention PMM when renewals are healthy. This corroborates the structural churn risk analyzed in Deliverable 13.
- **Founding Lead, Strategic Sales + SDR Lead** → the B2B/employer motion is being built now, not later.
- **Only 1–2 clinical roles vs ~10 brand/growth/design roles** → 🟡 the ratio of clinical investment to marketing investment is roughly 1:5. For a company delivering medical interpretation at scale, **this is the most consequential number in the entire hiring dataset.**

**Self-reported traction** (🟡 unaudited, from their own job posting): *"Over the past 6 months, we have grown 10x whilst halving CAC."* Treat as directional, not factual.

## 2.5 Partnerships, IP, and geography

**Confirmed partners:** Quest Diagnostics (labs), Vital (wearable aggregation), Medplum (FHIR), Stripe + Klarna (payments), Shopify (commerce), Knock (notifications), Cal.com (scheduling), PostHog, Sentry, Grail (Galleri multi-cancer screen), Thatch and Wellhub (benefits), SoulCycle (retail/brand), Wyndly (allergy immunotherapy — 🟢 `/rx/purchase-wyndly`). Landing pages in the sitemap suggest partner or co-marketing relationships with Ramp, Notion, Sequoia, Maven, Wordware, and OneDigital — 🟡 Strong Inference from dedicated URL slugs.

**Patents:** No granted patents identified in public search. 🟡 Strong Inference: the company is not pursuing a patent moat — consistent with a brand-and-speed strategy.

**Peer-reviewed research:** None identified with Superpower as an author. 🟢 Confirmed absence at time of research. **This is a significant and exploitable gap.** A company making population-scale claims about biological age and preventive benefit has published no validation of either.

**Open source:** No public repositories identified. 🟡 Strong Inference.

**Geography:** United States only. `/locations` enumerates 3,454 US state/city pages. NY and NJ carry different pricing (~$399), reflecting state lab-law variance — 🟡 Strong Inference via third-party review. **No international presence.** For Ovexis this is the single largest uncontested territory.

---

# DELIVERABLE 3 — FOUNDER PSYCHOLOGY

*This section is explicitly interpretive. Every inference is anchored to a quoted artifact, but the psychological reading itself is 🟡 Strong Inference or 🔴 Speculation as marked.*

## 3.1 Core beliefs, with evidence

| Belief | Anchoring evidence | Label |
|---|---|---|
| The healthcare system will not save you; you must self-rescue | Peters: *"as a person with health challenges, no one's really coming to save you"* | 🟢 quote / 🟡 interpretation |
| Medicine optimizes for adequacy, not excellence | *"designed to make you fine, not better"* (`/roadmap`) | 🟢 |
| Data asymmetry is the root injustice | *"Everyone deserves to understand what's happening in their body without a medical degree"* | 🟢 |
| Brand is the durable moat in an AI world | Peters, Sourcery VC interview | 🟢 |
| Speed and consolidation beat organic building | Two acquisitions within five months of Series A; *"This probably won't be our last M&A"* | 🟢 |
| Personal experimentation is legitimate evidence | Reported employee peptide self-injection; Marchione's public peptide advocacy | 🟡 |
| Consumer-tech aesthetics are a clinical asset | *"Feel more like Apple or Tesla than a hospital"* | 🟢 |

## 3.2 Decision framework — reconstructed

🟡 **Strong Inference.** Observed decisions are consistent with this priority ordering:

1. **Does it expand the data surface?** (labs → wearables → records → conversations → genomics → imaging)
2. **Does it compress time-to-value for the member?** (one draw, ~4–7 day results, immediate reveal)
3. **Does it strengthen brand?** (celebrity, domain, design, the hoodie)
4. **Can it be bought faster than built?** (Feminade, Base)
5. **Does it add a monetizable action?** (supplements → scans → Rx → peptides)
6. **Is it defensible clinically?** — 🟡 evidence suggests this is evaluated **last**, not first

Item 6 is the crux. The lawsuit, the biological-age inconsistency, the support failures and the peptide culture are not unrelated incidents — they are the **predictable output of a decision function that weights clinical caution below speed and growth.**

## 3.3 Risk tolerance

🟢 Confirmed behavioral evidence: two acquisitions pre-Series-B; skipping seed to go straight to Series A; naming competitors directly in paid advertising; selling compounded peptides; employees self-administering experimental compounds; publishing a public roadmap with dated commitments.

🟡 **Assessment: risk tolerance is in roughly the 95th percentile for a healthcare company, and roughly the 60th percentile for a consumer startup.** The founders are running a consumer-tech risk posture inside a regulated clinical domain. That arbitrage is exactly why they moved fast — and exactly why the failure modes in Deliverable 22 are concentrated in regulatory and clinical categories rather than technical ones.

## 3.4 Ten-year vision and mental models

Stated vision, 🟢 Confirmed: an AI doctor in every pocket; the front door to health before doctors or Google; *"A mayo clinic executive program 2.0 in the cloud"* (job posting); *"The world's biggest company will be in consumer healthcare"* (job posting).

**Mental models in evidence** — 🟡:
- **The Digital Twin analogy** — *"Digital twins already exist in aviation and manufacturing to simulate conditions and predict performance overtime."* (🟢 `/roadmap`). This is a revealing borrow: aviation twins work because jet engines are fully specified, deterministic systems with complete sensor coverage. Human biology is none of those things. **The analogy imports unearned confidence** — and that is precisely the gap Ovexis can occupy with honest uncertainty quantification.
- **Super-app thinking** — WeChat/Apple as templates for bundling.
- **Vertical integration** — own testing, interpretation, and fulfillment.
- **Category rejection** — Peters: *"Superpower isn't a longevity startup."* They deliberately resist the label that would cap their TAM.

## 3.5 Likely internal strategy (🔴 Speculation, flagged as such)

Reasoning from the hiring pattern, the litigation, the capital gap and the public roadmap, the most probable internal priorities right now:

1. Survive the Function litigation without a damaging admission; settle if it can be done quietly
2. Raise a Series B against the AI Doctor narrative and the claimed 10x/halved-CAC metrics
3. Convert the employer/benefits channel into predictable, lower-CAC revenue
4. Push ARPU via peptides, GLP-1s and scans to fix membership-level unit economics
5. Ship the iOS app hard for retention and HealthKit background data
6. Professionalize engineering under a new Head of Engineering and pay down `v2`/`legacy` debt

🔴 **Speculation, but strategically material for Ovexis:** the most likely acquirer conversations over a 3-year horizon are a large retail-pharmacy/diagnostics player, a wearable company needing a clinical layer, or a payer/benefits platform. An IPO path is improbable at current scale.

---

# DELIVERABLE 4 — PRODUCT REVERSE ENGINEERING

This section is built from the member application's **publicly served JavaScript bundle** — 304 chunks, ~11 MB, retrieved exactly as a browser retrieves them. The application uses **TanStack Router with file-based routing**, which means the build emits one chunk per route, named after the route. The result is that **the complete authenticated route map is publicly legible without ever logging in.**

That is itself a finding: 🟡 **Strong Inference — Superpower's entire product information architecture, admin surface, feature roadmap and internal naming leak through their own bundle manifest.** Ovexis should treat this as an operational-security lesson: obfuscate chunk names, or accept that your product map is public.

## 4.1 Complete route inventory — 46 authenticated routes (🟢 Confirmed)

**Core**
| Route | Function |
|---|---|
| `_app.index` | Home dashboard — orders, biological age card, biomarker filters, care-team CTA |
| `_app.intake` | Health profile update — *"Answer a few quick questions to personalize your protocol"* |
| `_app.invite` | Referral |
| `_app.questionnaire._type` | Typed questionnaire engine |

**Data layer**
| Route | Function |
|---|---|
| `_app.data.index` | Data hub |
| `_app.data.records` | Records vault — drag/drop upload, AI lab summaries, ingestion status |
| `_app.data.category._slug.observations` | Observations by category |
| `_app.data.diagnostics._slug` / `._slug_.observations` | Diagnostic detail |
| `_app.data-centralisation` | **Cross-AI conversation import** + lab upload + wearable connect |

**AI + care**
| Route | Function |
|---|---|
| `_app.concierge` | The AI Doctor chat surface |
| `_app.insights` | Insight feed from "Superpower Coach" |
| `_app.consults.index` / `.new` / `._uid` | Video consults (Care Team Consult, Advisory Call) |
| `_app.family-risk.plan` | Family risk insights with public sharing |

**Protocol**
| Route | Function |
|---|---|
| `_app.protocol.index` | Current protocol |
| `_app.protocol.plans._id` / `.goals._goalId` | Plan and goal detail |
| `_app.protocol.legacy._id` / `.goals._goalId` | **Legacy protocol (v1) — technical debt, still shipping** |
| `_app.protocol.reveal.index` / `._step` | Cinematic reveal sequence |

**Commerce**
| Route | Function |
|---|---|
| `_app.marketplace.index` | Supplements, panels, scans |
| `_app.marketplace.products._slug` / `.index` / `.checkout` | Product + checkout |
| `_app.orders.index` / `._id` | Orders |
| `_app.prescriptions._id` | Prescription detail |
| `_app.rx-subscriptions.index` / `._id` | Rx subscription management |
| `_app.services._id` | Service detail |
| `_app.scans` | Imaging ordering + scheduling |
| `_app.shopify-redirect` | Shopify handoff |

**Logistics**
| Route | Function |
|---|---|
| `_app.recollection._requestGroupId` | Sample recollection (redraw) |
| `_app._maps.recollection._requestGroupId.schedule` | Ops-side recollection scheduling |

**Admin / internal ops — the `_maps` family**
| Route | Function |
|---|---|
| `_app._maps.users` | Member admin — search, deactivate, delete, reactivate, **"Log in as User"** |
| `_app._maps.schedule` | Ops scheduling |
| `_app._maps.settings` | Ops settings |
| `_app._maps.onboarding` / `._step` / `.index` | Ops-assisted onboarding |

## 4.2 Internal API surface (🟢 Confirmed — extracted from bundle strings)

**Chat / AI**
```
POST /chat/chatv4/messages              # current chat API — v4
GET  /chat/chatv3/search                # message search — still v3 (debt)
GET  /chat/organs/summary/{organ}       # per-organ AI summary
GET  /chat/wearables/overview | /summary | /timeseries
POST /chat/wearables/citation/resolve   # resolve a wearable citation
GET  /chat/wearables/vital/token        # Vital link token
```

**Clinical data**
```
GET  /biomarkers            /biomarkers/categories
GET  /observations          /insights          /consent
GET  /questionnaires        /questionnaires/{id}/insights
GET  /vault
POST /files/presign  /files/upload  /files/{id}/ingest  /files/{id}/download
GET  /cds-services  POST /cds-services/{id}      # CDS Hooks
WS   /ws/subscriptions-r4                        # FHIR R4 subscriptions
```

**Protocol**
```
GET  /protocol-v2  /protocol-v2/latest  /protocol-v2/{protocolId}
POST /protocol-v2/{protocolId}/actions/{actionId}
GET  /protocol  /protocol/{id}                   # v1 legacy
```

**Logistics**
```
GET  /phlebotomy/serviceable | /availability | /search | /collection-methods
POST /phlebotomy/appointments | /phlebotomy/adjust
POST /redraw/{serviceRequestId}/schedule | /cancel | /skip
POST /orders/{requestGroupId}/missed-draw-cancel
GET  /orders  /orders/{id}/details  /orders/all-platforms
GET  /orders/{id}/details/requisition
```

**Scans**
```
GET  /scans/centers  /scans/intake-status
POST /scans/intake-height-weight  /scans/orders
GET  /scans/catalogs/{catalogId}/offerings/{offeringId}/product
POST /scans/orders/{id}/{appointment|cancel|followup|reschedule|schedule-handoff|requested-schedule}
GET  /scans/orders/{id}/reschedule-slots
```

**Commerce / Rx**
```
GET  /marketplace/summary  /marketplace/products/{slug}
GET  /marketplace/products/{slug}/biomarkers | /content
GET  /marketplace/products/by-legacy-service-id/{serviceId}
GET  /shop/multipass-url  /shop/checkout  /shop/supplement-catalog
GET  /rx/patient/{id}/subscriptions | /tasks
POST /rx/contract/{id}/{cancel|pause|change-plan|refill-date|plan-options}
GET  /credits/upgrade  /credits/upgrade/price
GET  /billing/subscriptions  /billing/invoices/{id}
```

**Consults / identity / admin**
```
GET/POST /consults/cal/bookings | /consults/cal/advisory/bookings
POST /consults/cal/bookings/{id}/{cancel|reschedule}
POST /identity/create-verification-session
GET  /admin/users/{id}  POST /admin/users/{id}/reactivate
POST /admin/list-users | /admin/stop-impersonating
POST /engagement/submit-job   /interaction-event/submit   /card-dismissals
GET  /rpc/knock/user-token    /rpc/notifications/preferences
GET  /family-risk/plan  POST /family-risk/plan/{id}/share
GET  /outreach/{outreachId}   /events/{eventId}/registration
```

**Architectural verdict:** 🟢 A **REST API over a FHIR-shaped clinical core**, with domain-partitioned services (chat, protocol, phlebotomy, scans, rx, marketplace, billing, admin). Versioning is **inconsistent** — `protocol-v2` alongside `protocol`, `chatv4` alongside `chatv3` — which is 🟡 strong evidence of rapid iteration outpacing deprecation discipline.

## 4.3 Retention, growth and conversion loops (🟢 Confirmed mechanics)

**Retention loop**
`Test → Reveal (emotional peak) → Protocol → Actions → Insight feed nudges (/outreach) → Wearable data flows continuously → Retest ($99–179) → Updated score → repeat`
🟡 **The critical flaw:** the loop's reinforcing moment — the retest that proves improvement — sits behind a paywall. Members must *pay again* to experience the payoff that would make them renew. This is a design error that Ovexis should invert by including at least two draws in the base membership.

**Growth loops**
1. **Programmatic SEO** — 6,186 URLs; near-zero marginal cost per page
2. **Comparison-page capture** — 24 competitor pages harvesting bottom-funnel intent
3. **Gifting** — `/sp-2-0---gift`, `/mothers-day`, `/v-day`
4. **Referral** — `_app.invite`
5. **Family risk sharing** — public links carry the brand outward (at PHI cost)
6. **Creator/celebrity** — Giannis, Aoki, Hudgens, Paul, Mbappé
7. **Cross-AI import** — captures users already asking health questions elsewhere
8. **Employer channel** — one sale, many members

**Conversion flow** (🟢 from route + string evidence)
`Landing (Intellimize-personalized) → quiz (/personalized-quiz, /quiz-weight-loss, /quiz-tirzepatide) → register → consent-payment.{billing-period, consent, payment, verification} → onboarding questionnaires {primer, medical-history, lifestyle, female-health} → add-on panel upsell → phlebotomy serviceability check → scheduling → draw → results → reveal → protocol → marketplace attach`

Note the ordering: **the add-on upsell is placed at peak intent, immediately after commitment and before scheduling.** 🟡 Strong Inference — this is deliberate AOV engineering.

## 4.4 Notable hidden and semi-hidden workflows (🟢 Confirmed)

- **Admin impersonation** — "Log in as User", with the guard string *"Uploads are disabled while impersonating a member."* Someone thought about impersonation safety, but only partially.
- **Recollection / redraw** — an entire subsystem for failed or insufficient samples, including `missed-draw-cancel`. This is real operational maturity; lab logistics fail often.
- **Card dismissals** (`/card-dismissals`) — per-user UI state for dismissible prompts.
- **Engagement job submission** (`/engagement/submit-job`) — triggered on wearable connect; 🟡 likely a backfill/sync job.
- **Dev affordances left in production** — `dev:simulate-compaction`, *"Simulated compaction summary for dev testing"*, `/protocol/dev`. 🟡 Minor hygiene issue.
- **Legacy surfaces still live** — `protocol/legacy`, `biomarker-legacy-dialog`, `chatv3`.

---

# DELIVERABLE 9 — AI REVERSE ENGINEERING
### *(Prioritized per the adaptive analysis rule — this is the deepest section of the report)*

This is where Superpower is genuinely, non-trivially good — and where the public bundle is most revealing.

## 9.1 Agent framework — identified

🟢 **Confirmed: the AI layer runs the AG-UI protocol against a LangGraph backend.** The proof is an unmissable developer warning string compiled into the shipped bundle:

> `"AG-UI is converting ${e} to ${t}. To remove this warning, upgrade your AG-UI integration package (e.g. @ag-ui/langgraph). To suppress it, set SUPPRESS_TRANSFORMATION_WARNINGS=true in your .env file."`

Corroborated by LangGraph-specific event names in the same bundle: `LangGraphInterruptEvent`, `PredictState`, `NodeStarted`, `NodeFinished`, `AgentStateMessage`, `ActionExecutionStart/Args/End/Result`.

**Implication:** the AI is not a thin wrapper over a chat completion endpoint. It is a **stateful graph-based agent** with nodes, interrupts (human-in-the-loop pause points), and predicted state — meaning they can halt a run mid-execution for clinician input and resume. That is a meaningfully sophisticated architecture for a consumer health product.

## 9.2 Complete event protocol (🟢 Confirmed — extracted verbatim)

```
RUN_STARTED · RUN_FINISHED · RUN_ERROR
STEP_STARTED · STEP_FINISHED
TEXT_MESSAGE_START · _CONTENT · _CHUNK · _END
TOOL_CALL_START · _ARGS · _CHUNK · _RESULT · _END
THINKING_START · THINKING_END
THINKING_TEXT_MESSAGE_START · _CONTENT · _END
REASONING_START · REASONING_END
REASONING_MESSAGE_START · _CONTENT · _CHUNK · _END
REASONING_ENCRYPTED_VALUE
STATE_SNAPSHOT · STATE_DELTA · MESSAGES_SNAPSHOT
ACTIVITY_SNAPSHOT · ACTIVITY_DELTA · CUSTOM · RAW
```

Two details deserve board attention:

- **`REASONING_ENCRYPTED_VALUE`** — 🟡 Strong Inference: this is the signature of **OpenAI's encrypted reasoning tokens** (o-series / GPT-5-class reasoning models), where the raw chain-of-thought is returned encrypted and opaque to the client. Its presence is the strongest available evidence about their model provider.
- **Separate `THINKING_*` and `REASONING_*` event families** — 🟡 Strong Inference: these correspond to two different provider conventions (Anthropic's "thinking" blocks vs OpenAI's "reasoning" items). **The presence of both suggests a multi-provider abstraction layer** — they are likely routing across model vendors rather than being locked to one.

## 9.3 The tool inventory — the agent's actual capabilities

🟢 **Confirmed.** Extracted verbatim from the activity-label switch statement in the shipped bundle. This is the agent's complete published toolset:

| Tool type | In-progress label | Completed label | What it proves |
|---|---|---|---|
| `fhir-query` | "Querying FHIR {resourceType}…" | "Queried FHIR {resourceType}" | **Agent queries a live FHIR server by resource type** |
| `kb-search` | "Searching knowledge base…" | "Searched knowledge base" | Internal RAG corpus exists |
| `web-search` | "Researching online…" | "Researched online" | Live web retrieval |
| `web-fetch` | "Reading source…" | "Read source" | Fetches and reads specific URLs |
| `memory-save` | "Saving memory…" | "Saved memory" | **Persistent write memory** |
| `memory-read` | "Recalling memories…" | "Recalled memory" | **Persistent read memory** |
| `skill-read` | "Reading skill…" | "Read skill" | **Modular skill/playbook registry** |
| `file-read` | "Reading file…" | "Read file" | Reads member documents |
| `file-ingestion` | "Processing {filename}…" | "Processed {filename}" | Document parsing pipeline |
| `record-read` | "Looking up a record…" | "Looked up a record" | Health record retrieval |
| `history-search` | "Searching conversation history…" | "Searched conversation history" | Cross-conversation recall |
| `wearables-overview` | "Checking wearables…" | "Checked wearables" | Device data access |
| `marketplace-query` | "Looking up product: {handle}…" | "Looked up product: {handle}" | **Commerce inside the clinical agent** |
| `analysis` | "Analyzing data…" | "Analyzed data" | Computation step |
| `compaction` | "Summarizing earlier messages…" | "Summarized earlier messages" | Memory compression |
| `tool-call` | "Using {toolName}…" | "Used {toolName}" | Generic passthrough |

Additionally: 🟢 the literal `toolName:'bash'` appears in the bundle. 🟡 Strong Inference — a code-execution tool exists in the agent's repertoire (most plausibly server-side sandboxed computation for trend math), though its scope cannot be determined from client code and **no assumption should be made that it is exposed to members.**

**The `marketplace-query` tool is the single most strategically important finding in this section.** The same agent that reasons over your labs can look up products to sell you. There is no observable architectural separation between clinical reasoning and commercial recommendation. 🟡 Strong Inference: **this is a structural conflict of interest embedded at the tool layer.** It is Ovexis's clearest and most defensible point of differentiation — see Deliverable 23.

## 9.4 Memory architecture

🟢 Confirmed mechanics:
- **Compaction** — activity type `compaction`, event keys `data-compaction`, `chatv3-activity:data-compaction:{id}`, and a dev affordance `dev:simulate-compaction`. There is also an error string *"No assistant message to inject compaction into"*, revealing that **compaction summaries are injected into an assistant message slot** rather than stored as separate objects.
- **Explicit memory tools** — `memory-save` / `memory-read`, plus a `data-recalled-memories` event type surfaced to the UI.
- **Cross-conversation search** — `history-search` tool and a `/chat/chatv3/search` endpoint.

🟢 Confirmed from the company's own launch communications (Anadolu Agency, Feb 2026): a *"proprietary compressed-memory architecture"* storing all patient-reported information *"without time constraints,"* capturing **symptom laterality, time of onset, aggravating and relieving factors, and explicitly excluded conditions**, retaining context after 50+ interactions, and tracking temporal correlations across biomarkers, medications, lifestyle changes and behavior.

🟡 **Strong Inference — the weakness.** Capturing *"explicitly excluded conditions"* (pertinent negatives) is genuinely clinically literate; most consumer AI does not do this. But compaction into an injected assistant message is **lossy prose summarization**. Clinical facts degrade unpredictably under repeated summarization, and there is no evident guarantee that a pertinent negative recorded at interaction 3 survives to interaction 60.

**Ovexis counter-design:** store clinical memory as **typed, structured resources** (FHIR `Condition`, `Observation`, `AllergyIntolerance`, with explicit `verificationStatus: refuted` for pertinent negatives) rather than compressed prose. Retrieve structurally; never summarize a fact you can query. This is a real, defensible architectural advantage.

## 9.5 Grounding and citation — their best engineering

🟢 **Confirmed** — this is the actual parsing logic, read directly from the public chunk `parse-fhir-citation`:

```js
var e = `(?:fhir:\/?\/?observation|patient:\/\/observation)\/`
var n = RegExp(`^${e}([a-f0-9-]+)$`, `i`)

function s(e) {
  let t = e.source.match(n)
  let r = t[1]                                  // observation UUID
  let i = e.title.match(/^(.+?):\s*([\d.,]+)\s*(\S+)\s*\((\d{4}-\d{2}-\d{2})\)$/)
  return {
    type: `fhir:Observation`,
    observationId: r,
    biomarkerName: i?.[1]?.trim(),
    value: i?.[2],
    unit: i?.[3],
    date: i?.[4]
  }
}
```

**What this means concretely.** When the AI states a clinical fact, it emits a citation URI of the form `fhir://observation/{uuid}`. The client resolves that UUID to a specific FHIR Observation and renders the biomarker name, value, unit and collection date inline. **Every clinical assertion is anchored to an immutable, addressable data point in the member's own record.**

This is the single best idea in Superpower's product, and Ovexis should copy it without hesitation — then extend it. Their citation grammar covers observations, files, appointments, products and web sources (🟢 citation types `biomarker`, `appointment`, `advisory`, `consult`, `coach`, `analysis` observed). Ovexis should unify **labs, wearables, imaging, clinician notes, genomics and literature under one provenance grammar**, so that no claim can render without a resolvable source.

## 9.6 Reasoning transparency

🟢 Confirmed: `THINKING_*` and `REASONING_*` event streams; a `chat:reasoning-toggle-anchor` UI element; search that reports *"Matched in thinking"* (meaning reasoning traces are indexed and searchable); error guards enforcing correct event ordering (*"Cannot send 'THINKING_END': No active thinking step found"*).

🟢 Confirmed from launch reporting: a visible **"Think" tab** exposing differential diagnoses considered and data points weighed.

**Assessment:** genuinely above industry norm for consumer health AI. **But** — 🟡 exposing reasoning is not the same as validating it. A confidently wrong differential displayed transparently is still a confidently wrong differential, and transparency may *increase* misplaced trust. Ovexis should pair transparency with **calibrated confidence and explicit abstention**.

## 9.7 What is conspicuously absent

🟢 **Confirmed absence** (searched exhaustively across all 304 chunks):
- No clinical evaluation framework, benchmark, or accuracy claim
- No published model card, eval suite, or safety report
- No visible confidence scores or uncertainty quantification in the citation/UI layer
- No published human-review rate or clinician-override statistics
- No peer-reviewed validation of the AI, the Superpower Score, or the biological-age model

**This is the largest unguarded flank in the entire company.** They have built impressive AI *plumbing* — grounded citations, structured memory, transparent reasoning, a real agent graph — with **no publicly evidenced clinical validation layer on top of it.** Function Health, with 6x the capital, will eventually fund exactly that validation. Ovexis can get there first and cheaper, because an eval harness with clinician-labeled gold sets costs vastly less than $298M.

## 9.8 Inferred AI architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│  CLIENT — React SPA (Vercel) · AG-UI event consumer                  │
│  Streams: text · tool-call · thinking · reasoning · activity · state │
│  Renders: inline citations · Think tab · activity ticker             │
└───────────────────────────┬──────────────────────────────────────────┘
                            │  SSE / streaming  → /chat/chatv4/messages
┌───────────────────────────▼──────────────────────────────────────────┐
│  AGENT ORCHESTRATION — LangGraph via @ag-ui/langgraph        🟢      │
│  Stateful graph · nodes · interrupts (human-in-loop) · predicted     │
│  state · run/step lifecycle                                          │
└───────────────────────────┬──────────────────────────────────────────┘
                            │
     ┌──────────────────────┼───────────────────────┬─────────────────┐
     ▼                      ▼                       ▼                 ▼
┌──────────┐        ┌──────────────┐        ┌─────────────┐   ┌──────────────┐
│ MEMORY   │        │  TOOLS (16)  │        │ RETRIEVAL   │   │  MODELS      │
│ compact  │        │ fhir-query   │        │ kb-search   │   │ 🟡 multi-    │
│ save/read│        │ record-read  │        │ web-search  │   │ provider:    │
│ history  │        │ file-read    │        │ web-fetch   │   │ encrypted    │
│ search   │        │ wearables    │        │ history     │   │ reasoning →  │
│          │        │ marketplace  │        │             │   │ OpenAI-class │
│          │        │ analysis     │        │             │   │ + thinking → │
│          │        │ skill-read   │        │             │   │ Anthropic-   │
│          │        │ bash 🟡      │        │             │   │ class        │
└──────────┘        └──────┬───────┘        └─────────────┘   └──────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────────────┐
│  CLINICAL DATA CORE — FHIR (Medplum SDK confirmed in client)  🟢     │
│  Observation · Patient · DiagnosticReport · Communication ·          │
│  Encounter · QuestionnaireResponse · Goal · ServiceRequest ·         │
│  MedicationRequest · DocumentReference · ImagingStudy · Media        │
│  CDS Hooks (/cds-services) · FHIR R4 Subscriptions (/ws/subs-r4)     │
└──────────────────────────┬───────────────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┬────────────────────┐
        ▼                  ▼                  ▼                    ▼
   Quest labs        Vital (wearables)    File ingestion      Marketplace
   phlebotomy        Oura/Whoop/Garmin    OCR → LOINC         Shopify
   redraw logic      Apple Health         provenance          Rx pharmacy
```

## 9.9 Model providers — the honest answer

🔴 **Cannot be confirmed.** Server-side model selection is not observable from client code, and I will not guess a vendor name and present it as fact.

🟡 **Strong Inference from three independent signals:**
1. `REASONING_ENCRYPTED_VALUE` → OpenAI-style encrypted reasoning tokens
2. Distinct `THINKING_*` event family → Anthropic-style thinking blocks
3. `skill-read` tooling and `toolName:'bash'` → conventions strongly associated with Anthropic's agent/skills patterns

**Most probable configuration: a multi-provider router across OpenAI and Anthropic frontier models, selected per task.** The competitor-brand icons in their bundle (OpenAI, Anthropic, Gemini, Grok, Perplexity) are 🟢 confirmed to be for the **cross-AI import feature** — they are UI affordances, not integrations, and should not be misread as evidence of model usage.

---

# DELIVERABLE 5 — COMPLETE USER JOURNEY

Reconstructed from route names, API endpoints, UI strings and page content. 🟢 unless marked.

## Stage 1 — Anonymous visitor
**Entry points:** organic SEO (6,186 pages — biomarker, location, guide, comparison), paid social with creators, celebrity referral, gift links, employer benefit portal, direct.
**Screens:** homepage (Intellimize-personalized 🟢), `/why` manifesto, `/roadmap`, `/reviews`, `/biomarkers`, comparison pages, `/organizations`.
**Trust signals deployed:** "4.6 out of 5 Trustpilot", "1M biomarkers tested", "Detect 1,000+ conditions", medical advisory board portraits, university logos (Harvard, Stanford, UCLA — 🟢 `/protocol/science/` assets), member testimonials with names/ages, "60% of members…" stat, HSA/FSA badge.
**Analytics:** PostHog via first-party proxy `ph.superpower.com`; Segment; Klaviyo; GTM **deliberately scoped** to fire only on `/onboarding` and `/register` 🟢.

## Stage 2 — Marketing → intent
Quizzes as qualification + lead capture: `/personalized-quiz`, `/quiz-weight-loss`, `/quiz-tirzepatide` 🟢. Newsletter capture ("the Superpower Code"). "Ask AI about Superpower" widget on site 🟢.

## Stage 3 — Signup
`/register` → better-auth 🟢. Methods observed: email/password, **magic link** (`send-magic-link`, `/auth/verify-magic-link`), **email OTP**, phone number, and organization-scoped accounts for B2B 🟢. `check-email`, `verify-email`, `resetpassword`, `setpassword` screens present.

## Stage 4 — Consent + payment (a single combined flow)
🟢 Confirmed step machine: `consent-payment.billing-period` → `consent-payment.consent` → `consent-payment.payment` → `consent-payment.verification`.
Consent objects observed: `INFORMED_CONSENT`, `phi-consent`, `phiMarketingConsent`, `rx-tos-consent`, `textMessageConsent`, plus `/legal/medical-consent` and `informed-medical-consent/prescription-subscriptions`.
🟡 **Strong Inference:** bundling clinical informed consent into the *purchase* flow optimizes conversion but weakens the quality of consent. Ovexis should separate them.

## Stage 5 — Onboarding + intake
`_app._maps.onboarding` (ops-assisted) and member-side onboarding with modules: `onboarding-primer`, `onboarding-medical-history`, `onboarding-lifestyle`, `onboarding-female-health` 🟢. Height/weight capture, address autocomplete, gender (`use-gender` hook drives downstream panel logic 🟢).
**Upsell inserted here** — add-on panel tubes: advanced, autoimmune, cardiovascular, metabolic, methylation, nutrient, organ-age 🟢.

## Stage 6 — Serviceability + scheduling
`/phlebotomy/serviceable` gates by address; `/phlebotomy/search`, `/availability`, `/collection-methods` (in-lab vs at-home) 🟢. `in-lab-scheduler`, `schedule-stepper`, `open-in-maps`, calendar add (Google/iOS icons present) 🟢.

## Stage 7 — Draw → lab → results
Order created; requisition available (`/orders/{id}/details/requisition`) 🟢. Home dashboard asks *"Did you complete your blood draw?"* 🟢. Failure paths handled: *"A specific assay is being re-run at the lab"*, redraw scheduling, missed-draw cancellation 🟢.

## Stage 8 — Data import (concurrent)
`/data-centralisation`: upload lab PDFs (`/files/presign` → `/files/{id}/ingest`), connect wearables (Vital), and **import AI conversations** — copy a generated prompt, open ChatGPT/Claude/Gemini/Perplexity/Grok, paste the response back 🟢.

## Stage 9 — The Reveal
`/protocol/reveal/welcome` → `/text-sequence` → `/score` → `/biological-age` → `/get-started` 🟢. Sequenced copy observed: *"We've analyzed all your data" → "Identified core insights" → "And created a personal protocol" → "It's time to meet your inner clock."*
**This is the emotional climax of the product** and is engineered with real craft — Rive animations (`superpower.riv`, `superpower_ai.riv` 🟢), number-flow counters, text shimmer, staged unlocks.

## Stage 10 — Understanding
Dashboard: Superpower Score, Biological Age, 13 organ/system scores, biomarker rows with sparklines, optimal-range formatting, severity tiers (*"Doing quite well" → "Generally healthy" → "Mixed health markers" → "Needs attention" → "Immediate action needed"*) 🟢. Digital twin 3D model 🟢.

## Stage 11 — Protocol
`/protocol-v2/latest` — actions grouped by type (lifestyle, diet, supplement, testing, consultation 🟢), each with "why", "what to look out for", target biomarker IDs, citations, and completion tracking via `/protocol-v2/{id}/actions/{actionId}` 🟢.

## Stage 12 — AI + care
`/concierge` chat with streaming, citations, Think tab, activity ticker, chat suggestions, history search 🟢. `Text Care Team`; `Auto-escalated with care team` 🟢. Video consults via Cal.com 🟢.

## Stage 13 — Action / commerce
Marketplace ("Recommended because…" 🟢), scans, prescriptions with identity verification and questionnaires, Rx subscription management 🟢.

## Stage 14 — Retention
Insight feed from "Superpower Coach" (`/insights`, `/outreach/{id}`) 🟢; Knock multi-channel notifications with preference management 🟢; retest prompts (`schedule_retest`, `/redraw/...`) 🟢; `test-reminder` page 🟢.

## Stage 15 — Renewal / referral
`/billing/subscriptions`, credits/upgrade pricing, `_app.invite`, gifting flows 🟢.

**Journey gaps Ovexis should exploit:** (1) no clinician-facing export or portal; (2) no data-export/portability surface observed; (3) the retest paywall interrupts the value loop; (4) support escalation quality is the documented failure point; (5) no post-cancellation data stewardship path visible.

---

# DELIVERABLE 6 — UX RESEARCH

## Design system (🟢 Confirmed)
**Foundation:** Tailwind CSS with **Radix UI primitives** (117 refs) — accordion, dialog, popover, tooltip, dropdown, tabs, select, radio-group, checkbox, collapsible, scroll-area, carousel, calendar, progress, separator, breadcrumb, hover-card.
**Motion:** Framer Motion (`AnimatePresence`, `motion`) + **Rive** (164 refs — `superpower.riv`, `superpower_ai.riv`, `file-animations.riv`). Rive is a deliberate, expensive choice: real-time vector animation with state machines, not Lottie playback. 🟡 Strong Inference: they invested seriously in motion identity.
**Bespoke components observed:** `number-flow` (animated counters), `text-shimmer`, `text-effect`, `hover-3d`, `progressive-image`, `sparkline-chart`, `dome-image`, `superpower-signature`, `protocol-book`, `protocol-stepper`, `slider-tabs`, `transaction-spinner`, `skeleton`.
**Palette tokens observed:** `zinc-*` neutrals, `emerald-500` for connected/success, `vermillion-*` for errors 🟢.

## Accessibility (🟢 mixed)
**Present:** `aria-hidden`, `aria-haspopup`, `role="dialog"`, `data-state` patterns (Radix defaults), `motion-reduce:transition-none` — 🟢 they respect `prefers-reduced-motion`, which matters given heavy animation. `noValidate` forms with custom validation messaging.
**Not verifiable without authenticated audit:** colour contrast across the score/severity palette, screen-reader labeling of the 3D digital twin, keyboard navigation of the reveal sequence, focus management in the chat stream.
🟡 **Strong Inference: baseline accessibility is inherited from Radix rather than deliberately engineered beyond it.** A health product serving symptomatic users — including people with fatigue, brain fog, or visual disturbance — should exceed baseline. **Ovexis differentiator: WCAG 2.2 AA as a published commitment.**

## Dark mode
🟢 `moon` icon component and `theme-color #ffffff` meta. 🟡 Strong Inference: light-first design; full dark-mode support unconfirmed.

## Mobile
🟢 Native iOS app (App Store ID 6747997159). Web app is responsive (`use-mobile`, `use-screen-size`, `sm:`/`md:`/`lg:` breakpoints throughout, `browser-detection`, `app-store` component, "Download on the App Store" prompts).

## Microinteractions and loading
🟢 Skeleton loaders, spinners, shimmer text, staged reveal delays (`delay:.8`, `.35s` easing with custom cubic-bezier `[.32,.72,0,1]`), toast confirmations (*"Copied link to clipboard"*, *"{device} is now connected!"*), optimistic states, streaming chat with smooth-scroll and mask-image fade at the scroll edge.

**Standout pattern worth copying:** the **activity ticker** during AI response — showing "Querying FHIR Observation…", "Searching knowledge base…" — converts latency into visible competence. It is the best latency-masking pattern I observed and costs almost nothing to implement.

## Conversion optimization
🟢 Intellimize personalization; PostHog feature flags (`use-posthog-feature-flag-enabled/value`); GTM scoped to conversion paths only; quiz funnels; `tiers-test-2` and `welcome-new-*` A/B variants visible in sitemap; dedicated partner/creator landing pages (Steve Aoki, Vanessa Hudgens, Meat Mafia, Wellness Daddy, Notion, Ramp, Sequoia).

## Friction inventory (🟡 assessed)
| Friction | Where | Severity | Ovexis fix |
|---|---|---|---|
| Consent bundled into checkout | consent-payment | Medium (ethical) | Separate, unhurried consent |
| Long onboarding questionnaires | 4 modules | Medium | Progressive profiling over time |
| Upsell before scheduling | onboarding | Medium (trust) | Recommend from risk, not margin |
| Retest paywall | retention loop | **High** | Include 2 draws in base |
| Support unreachable | post-purchase | **High** (documented) | Guaranteed human SLA |
| Serviceability discovered late | after commitment | Medium | Check address before payment |
| Public PHI share link | family risk | **High** (safety) | Scoped expiring tokens |

---

# DELIVERABLE 7 — HEALTHCARE WORKFLOW

## Clinical workflow (🟡 reconstructed)
`Member intake (questionnaires) → order set generated → ServiceRequest → specimen collection (Quest PSC or mobile phlebotomy) → lab resulting → DiagnosticReport + Observations ingested → algorithmic scoring (Superpower Score, biological age, organ scores) → AI protocol drafted → clinician review (asynchronous) → member reveal → messaging/escalation → action (supplement/Rx/scan/lifestyle) → retest → trend`

🟡 **Strong Inference on the clinician's actual role.** Evidence for review: `physician-followup-cta`, `rx-clinician-call-cta`, "Care Team Consult", "Auto-escalated with care team", part-time Collaborating Physician and multi-state Longevity NP job postings, and Business Insider's report that *"AI-generated action plans are reviewed by human care teams behind the scenes."* Evidence on the constraint side: a small clinical team relative to member volume, and documented support-responsiveness complaints. **Most probable model: exception-based review — algorithmic triage with clinician attention concentrated on flagged abnormalities, not universal review of every protocol.** This is defensible if disclosed and if the triage is validated; it is a liability if members believe every plan is individually physician-authored. Function's complaint alleges exactly this gap regarding "continuous access to doctors."

## Patient workflow
Self-service dominant: order → draw → results → interpret → act → retest. Human contact is opt-in and asynchronous by default.

## Provider workflow
🟢 **There is none externally.** No clinician portal, no provider-facing route, no referral inbound, no clinician export. Internal ops use the `_maps` console. **This is the single largest product gap** — and, for Ovexis, the largest opportunity (see Deliverable 21 and 23).

## Hospital / health-system workflow
🟢 None. No EHR write-back, no HIE participation observed, no TEFCA/Carequality/CommonWell evidence. Data flows *in* (via member upload) and never flows *out* to the care system.

## Insurance workflow
🟢 Deliberately absent. Cash-pay only; HSA/FSA is the sole payment-adjacent mechanism. The employer channel (`/organizations`, HRIS API + **834 EDI** enrollment files 🟢) is benefits-adjacent, not claims-adjacent.

## Lab workflow
🟢 Quest primary; at-home draws; 2,000+ PSCs; requisition generation; **redraw/recollection subsystem** for failed samples; `all-platforms` order aggregation suggesting multiple fulfillment partners.

## Pharmacy workflow
🟢 Rx catalog (GLP-1s, peptides, hormones, dermatology), identity verification (Stripe Identity), Rx questionnaires, clinician consult CTA, subscription lifecycle (pause/refill/change plan), `rx-screen-out` for ineligible members, delivery. 🟡 Strong Inference: compounding-pharmacy partners plus a telehealth prescribing layer.

## Referral & care coordination
🟢 Weak by design. `physician-followup-cta` nudges members to see their own doctor; family-risk sharing produces a link, not a clinical document. There is **no structured clinical summary, no C-CDA export, no fax/direct messaging** — the classic coordination primitives are absent.

## Clinical documentation
🟡 FHIR `Communication` resources (50 references — the most-referenced resource type in the bundle) indicate messaging is stored as clinical communication. `DocumentReference`, `Media`, `Binary` present for uploads. No evidence of SOAP notes, encounter documentation, or billable-visit records.

---

# DELIVERABLE 8 — HEALTHCARE DATA ARCHITECTURE

## 8.1 Standards posture

| Standard | Status | Evidence |
|---|---|---|
| **FHIR R4** | 🟢 **Core architecture** | Medplum client SDK in bundle; `fhir://observation/{uuid}` citations; `fhir-query` agent tool; `/ws/subscriptions-r4`; job posting states *"Data: FHIR-based schema"* |
| **CDS Hooks** | 🟢 Capability present | `getCdsServices()` → `/cds-services`, `callCdsService()` → `/cds-services/{id}` |
| **FHIR Subscriptions** | 🟢 Capability present | `subscribeToCriteria()`, WebSocket `/ws/subscriptions-r4` |
| **LOINC** | 🟡 Strong Inference | 388 biomarker slugs use LOINC-style naming: `cholesterol-in-hdl-mass-vol`, `gfr-1-73-sq-m-predicted-creatinine-based-formula-ckd-epi-2021-s-p-bld-vol-rate-area` |
| **HL7 v2** | 🔴 Not observed | Likely present in lab interfaces server-side but unverifiable |
| **C-CDA / CCD** | 🔴 Not observed | No import/export surface found |
| **Apple HealthKit** | 🟢 Confirmed | `apple_health_kit` constant; iOS app |
| **Google Health Connect** | 🔴 Not observed | No Android app evidence found |
| **X12 834** | 🟢 Confirmed (claim) | `/organizations`: *"compatible with your HRIS via API or 834 file formats"* |
| **TEFCA / Carequality / CommonWell** | 🔴 Not observed | No network participation evidence — **major gap** |
| **SMART on FHIR** | 🔴 Not observed | Medplum supports it; no evidence of use |

**The headline finding:** 🟢 Superpower built on a **genuine FHIR core** rather than a bespoke schema. This is unusual and commendable for a consumer company, and it is why their AI can cite `fhir://observation/{uuid}`. **Ovexis must match this — a FHIR-native core is now table stakes for credibility in this category, and retrofitting it later is enormously expensive.**

**The equally important finding:** they have FHIR *inside* but **no interoperability *outside*.** No HIE, no TEFCA, no EHR write-back, no C-CDA. Data enters through consumer uploads and never rejoins the clinical record. 🟡 Strong Inference: this is a deliberate walled-garden choice that maximizes lock-in and minimizes regulatory surface — and it is **exactly where Ovexis should differentiate**, because a longitudinal record that cannot reach a member's actual physician has a hard ceiling on clinical value.

## 8.2 Data sources

| Source | Mechanism | Confidence |
|---|---|---|
| Blood labs | Quest; 2,000+ PSCs; at-home phlebotomy | 🟢 |
| Historical labs | PDF upload → `/files/{id}/ingest` → AI extraction | 🟢 |
| Wearables | **Vital** aggregator — Oura, Whoop, Garmin, Fitbit, Withings, Peloton, Eight Sleep, Ultrahuman, Cronometer, Apple Health | 🟢 |
| Questionnaires | FHIR QuestionnaireResponse | 🟢 |
| Imaging | MRI, DEXA, CT calcium — partner centers; `ImagingStudy` resource referenced | 🟢 |
| Genomics | `genome-biomarker-dialog`; `/services/full_genetic_sequencing`; `ssot-categories/dna-health` | 🟢 |
| Microbiome | `/services/transparent/gut_microbiome_analysis` | 🟢 |
| Toxins | heavy metals, mycotoxins, PFAS, organic acids | 🟢 |
| Cancer screening | Grail Galleri | 🟢 |
| Nutrition | Base acquisition dataset; Cronometer integration | 🟢 |
| **AI conversations** | Manual export/import from ChatGPT, Claude, Gemini, Perplexity, Grok | 🟢 |
| EHR records | **Member-uploaded documents only — no direct EHR connection observed** | 🟢 (absence) |

## 8.3 Identity, normalization, deduplication, consent

**Patient identity:** better-auth accounts; `/users/{id}`; Stripe Identity verification for Rx; organization-scoped identity for B2B; admin impersonation with a partial guard. 🟡 No evidence of enterprise MPI/EMPI or probabilistic patient matching — appropriate for a D2C-only model, insufficient for health-system integration.

**Normalization:** 🟡 Strong Inference — LOINC-style canonical slugs (388 of them) function as the internal vocabulary; `get-biomarker-ranges`, `format-optimal-range`, `get-biomarker-color`, `use-observation-biomarker-index` handle range logic and cross-source alignment. Reference ranges appear to be Superpower-defined "optimal ranges" distinct from lab reference intervals 🟢 (`Optimal Range` vs `Lab Comment` both rendered in the score dialog).

**Deduplication:** 🔴 No direct evidence. 🟡 Strong Inference: `use-observation-biomarker-index` and `most-recent-biomarker` imply index-based resolution of the latest value per biomarker, but true cross-source deduplication (same analyte, two labs, different units/methods) is unverifiable.

**Consent architecture:** 🟢 Genuinely granular — `INFORMED_CONSENT`, `phi-consent`, `phiMarketingConsent`, `rx-tos-consent`, `textMessageConsent`, `proxy-authorization`, plus a `/consent` endpoint and versioned documents (*"The updated Informed Consent document will be provided on the next page"*). This is better than most consumer health apps. **The weakness is not granularity — it is that consent is collected inside a checkout flow and that the privacy policy grants broad downstream latitude** (§12.3).

## 8.4 Healthcare data flow

```
  ┌─────────────┐  ┌──────────────┐  ┌───────────────┐  ┌──────────────┐
  │ Quest labs  │  │  Wearables   │  │ Member PDFs   │  │ AI chat logs │
  │ (DiagRpt)   │  │  via Vital   │  │ (upload)      │  │ (paste)      │
  └──────┬──────┘  └──────┬───────┘  └───────┬───────┘  └──────┬───────┘
         │                │                  │                 │
         │                │          ┌───────▼────────┐        │
         │                │          │ file-ingestion │        │
         │                │          │ OCR + extract  │        │
         │                │          └───────┬────────┘        │
         ▼                ▼                  ▼                 ▼
  ┌────────────────────────────────────────────────────────────────────┐
  │  NORMALIZATION — LOINC-style canonical biomarker vocabulary  🟡    │
  │  unit harmonization · optimal-range mapping · recency index        │
  └────────────────────────────────┬───────────────────────────────────┘
                                   ▼
  ┌────────────────────────────────────────────────────────────────────┐
  │  FHIR CLINICAL CORE (Medplum)  🟢                                  │
  │  Patient · Observation · DiagnosticReport · QuestionnaireResponse  │
  │  Communication · Encounter · Goal · ServiceRequest · ImagingStudy  │
  │  MedicationRequest · DocumentReference · Media · Binary            │
  └───────┬──────────────────────┬──────────────────┬──────────────────┘
          ▼                      ▼                  ▼
  ┌──────────────┐      ┌────────────────┐   ┌──────────────────┐
  │  SCORING     │      │  AI AGENT      │   │  CDS Hooks +     │
  │  Superpower  │      │  LangGraph     │   │  Subscriptions   │
  │  Score, Bio- │      │  16 tools      │   │  (capability)    │
  │  Age, 13 organ│     │  FHIR-cited    │   │                  │
  └──────┬───────┘      └───────┬────────┘   └────────┬─────────┘
         │                      │                     │
         └──────────┬───────────┴─────────────────────┘
                    ▼
       ┌────────────────────────────┐      ┌─────────────────────┐
       │  PROTOCOL v2               │─────▶│  ACTION LAYER       │
       │  actions · goals · targets │      │  supplements · Rx   │
       │  citations · completion    │      │  scans · lifestyle  │
       └────────────┬───────────────┘      └─────────────────────┘
                    ▼
       ┌────────────────────────────┐
       │  MEMBER + CARE TEAM        │   ✗ NO OUTBOUND PATH TO
       │  chat · insights · consults│     EHR / HIE / PHYSICIAN
       └────────────────────────────┘
```

---

# DELIVERABLE 10 — TECHNICAL REVERSE ENGINEERING

| Layer | Finding | Evidence | Confidence |
|---|---|---|---|
| **Marketing frontend** | Webflow CMS | `x-wf-region: us-east-1`, `cdn.prod.website-files.com`, Webflow sitemap | 🟢 |
| **Marketing CDN** | Cloudflare → CloudFront | `server: cloudflare`, `via: CloudFront`, `cf-ray`, `x-amz-cf-pop` | 🟢 |
| **App frontend** | **React SPA, Vite-built, on Vercel** | `server: Vercel`, `x-vercel-cache: HIT`, `x-vercel-id: pdx1::…`, `/assets/index-{hash}.js` module script | 🟢 |
| **Routing** | TanStack Router (file-based) | `tanstack.com` ref; `_app.*` chunk naming | 🟢 |
| **UI** | Tailwind + Radix + Framer Motion + Rive | 117 Radix refs, 164 Rive refs, `.riv` assets | 🟢 |
| **State/data** | TanStack Query + Zustand | query/mutation patterns; `zustand devtools middleware` string, `vanilla`, `shallow` | 🟢 |
| **Forms** | react-hook-form + Zod-style schemas | `handleSubmit`, `noValidate`, `auth-schemas`, zod-like validators | 🟡 |
| **Backend API** | **Node.js / Express** | `X-Powered-By: Express` | 🟢 |
| **Additional backend** | Golang | Job posting: *"Golang (plus)"* | 🟢 (stated) |
| **Cloud** | **AWS** (Fargate, Kubernetes, Docker) | API resolves to AWS IPs; job posting names AWS/Fargate, Docker, K8s, IaC | 🟢 |
| **Clinical data platform** | **Medplum (FHIR)** | MedplumClient SDK, `api.medplum.com`, FHIR StructureDefinitions | 🟢 |
| **Auth** | **better-auth** | `BETTER_AUTH` constants; `/sign-out`, `/revoke-sessions`, `/admin/list-users`, `/admin/stop-impersonating` | 🟢 |
| **Auth methods** | magic link, email OTP, phone, password, org, impersonation | endpoint + string evidence | 🟢 |
| **Database** | Not observable | — | 🔴 Unknown (🟡 Postgres likely, as Medplum's default) |
| **Caching** | Vercel edge; CloudFront; Cloudflare | `x-vercel-cache`, `surrogate-control: max-age=432000` | 🟢 |
| **Monitoring** | **Sentry** | 3,302 refs; `SENTRY_RELEASE d6d7217d8636…`; `superpower-react-app` | 🟢 |
| **Product analytics** | **PostHog** via first-party proxy | `ph.superpower.com`, `us.posthog.com`, feature-flag hooks | 🟢 |
| **Marketing analytics** | GTM (`GTM-PBS5NFXN`), Segment, Klaviyo, Intellimize | homepage + app HTML | 🟢 |
| **Payments** | **Stripe** + Klarna | Stripe SDK chunks, `/billing/*`, klarna asset | 🟢 |
| **Identity/KYC** | Stripe Identity | `/identity/create-verification-session` | 🟡 |
| **Notifications** | **Knock** | `api.knock.app`, `/v1/users/{id}/feeds`, Slack + MS Teams providers | 🟢 |
| **Scheduling** | **Cal.com** | `/consults/cal/bookings` | 🟢 |
| **Commerce** | **Shopify** (multipass SSO) | `/shop/multipass-url`, `_app.shopify-redirect` | 🟢 |
| **Wearables** | **Vital** | `link.tryvital.io/initialize.js`, `VitalLink` | 🟢 |
| **Video** | Mux + Plyr | 66 Mux refs; `plyr` CSS preload on marketing site | 🟢 |
| **Content/CMS** | Contentful (app-side) + Webflow (marketing) | 5 contentful refs | 🟡 |
| **Support** | Front | `front` refs; `app.usebridge.com` | 🟡 |
| **CI/CD** | GitHub Actions | job posting | 🟢 (stated) |
| **Feature flags** | PostHog | `use-posthog-feature-flag-enabled` / `-value` | 🟢 |
| **Dev tooling** | Yarn workspaces, Storybook, ESLint, Jest, Webpack | job posting | 🟢 (stated) |
| **Ops** | Figma, Linear, Notion, Slack | job posting | 🟢 (stated) |

**Deployment posture** 🟡: monorepo (Yarn workspaces) → GitHub Actions → containers on AWS ECS Fargate and/or Kubernetes for services; frontend deployed independently to Vercel; Sentry release tagging per deploy; PostHog flags for progressive rollout. This is a **modern, competent, unremarkable-in-a-good-way stack** — nothing exotic, nothing legacy, high velocity.

---

# DELIVERABLE 11 — API INVESTIGATION

| Dimension | Finding | Confidence |
|---|---|---|
| **Public developer API** | 🟢 **None exists.** No docs, no portal, no developer subdomain, no SDK | 🟢 (absence) |
| **Style** | REST, JSON, domain-partitioned | 🟢 |
| **GraphQL** | `/graphql` → 404 on api.superpower.com. *(Medplum SDK ships GraphQL capability, but no endpoint is exposed)* | 🟢 |
| **OpenAPI** | `/openapi.json`, `/swagger`, `/docs` → all 404 | 🟢 |
| **FHIR API** | Internal only — no public FHIR base URL exposed | 🟢 |
| **Versioning** | Inconsistent: `protocol-v2` vs `protocol`; `chatv4` vs `chatv3`; `/v1/*` only for Knock (vendor) | 🟢 |
| **Auth** | Bearer tokens / session cookies via better-auth; `Authorization` header handling in client | 🟡 |
| **Webhooks** | None public. Internal: FHIR Subscriptions over WebSocket | 🟢 |
| **Rate limits** | Not observable without authenticated testing (not attempted) | 🔴 |
| **security.txt** | 404 — **no coordinated vulnerability disclosure path published** | 🟢 (absence) |
| **CORS** | `access-control-allow-origin: *` on the Vercel-served static app shell (normal for static assets) | 🟢 |
| **API hardening** | Strong: `CSP default-src 'none'`, HSTS w/ preload + includeSubDomains, `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`, `Referrer-Policy: no-referrer`, `Cache-Control: no-store` | 🟢 |

**Assessment.** The API is competently hardened at the edge — genuinely better than typical for a Series-A consumer company. But there is **no developer surface whatsoever**: no partner API, no member data export API, no clinician integration, no webhooks. 🟡 Strong Inference: this is deliberate (walled garden, minimize surface, no partner support burden).

**Ovexis opportunity:** a documented, FHIR-conformant public API with member-controlled data export is (a) a genuine developer moat, (b) an ecosystem accelerant, (c) increasingly a regulatory expectation under information-blocking and data-portability norms, and (d) a marketing weapon against a closed competitor. **Ship it in V2.**

---

# DELIVERABLE 12 — SECURITY INVESTIGATION

*Assessed strictly from unauthenticated public surfaces. No testing, probing beyond ordinary page retrieval, or access attempts were performed.*

## Observed posture

| Control | app.superpower.com | api.superpower.com | superpower.com (marketing) |
|---|---|---|---|
| HSTS | ✅ `max-age=63072000` | ✅ + `includeSubDomains; preload` | ❌ **absent** |
| CSP | ❌ absent | ✅ `default-src 'none'` (restrictive) | ❌ absent |
| X-Frame-Options | ❌ absent | ✅ DENY | ❌ absent |
| X-Content-Type-Options | ❌ absent | ✅ nosniff | ❌ absent |
| Referrer-Policy | ❌ absent | ✅ no-referrer | ❌ absent |
| Cache-Control (no-store) | n/a (static) | ✅ | n/a |
| TLS | ✅ valid, SAN-scoped | ✅ | ✅ |

🟡 **Strong Inference: the API is hardened by a security-conscious engineer; the frontend and marketing site were not given the same attention.** The absence of CSP and X-Frame-Options on the *member application* origin is the most notable gap — it is the origin that renders PHI. Clickjacking and XSS-mitigation defenses are weaker there than at the API.

## Compliance

| Item | Status |
|---|---|
| **HIPAA** | 🟢 Claimed: *"Our platform is HIPAA compliant"* (`/organizations`). Independent verification not publicly available. 🟡 Their structure (telehealth, labs, Rx) makes covered-entity/business-associate status plausible, but the consumer-wellness portions may sit outside HIPAA — a distinction the marketing does not draw. |
| **SOC 2** | 🔴 **No public attestation, trust center, or report found.** For an enterprise motion this is a material gap. |
| **HITRUST** | 🔴 None found |
| **CLIA/CAP** | 🟡 Inherited via Quest (accredited); Superpower itself is not the lab |
| **GDPR** | 🟡 US-only service; policy references US frameworks. EU exposure appears limited but unconfirmed |
| **CCPA/CPRA** | 🟢 Policy provides categories-of-third-parties disclosure and rights request path |
| **FDA** | 🟡 Product is positioned as wellness/LDT-adjacent, avoiding SaMD classification. **The AI Doctor's diagnostic-adjacent behavior is the risk boundary** — differential diagnoses and treatment guidance edge toward device territory |
| **BAA** | 🔴 Not publicly evidenced with any named vendor |
| **security.txt / VDP** | 🔴 Absent |

## Threat model (🟡 analytical)

| Vector | Exposure | Notes |
|---|---|---|
| **Public PHI share links** | **High** | `/family-risk/plan/{id}/share` — their own copy admits *"accessible to anyone who has the URL. This includes any personal health information"* |
| **Admin impersonation** | **High** | "Log in as User" exists; upload is blocked during impersonation but read access to full PHI is implied |
| **Bundle information disclosure** | Medium | Entire route map, admin endpoints, internal API paths, feature names and ops tooling are publicly readable |
| **Third-party sprawl** | Medium | Stripe, Vital, Knock, Cal.com, Shopify, Medplum, PostHog, Sentry, Klaviyo, Segment, Intellimize, Mux, Front — each is a BAA question and a data-flow question |
| **PHI in telemetry** | Medium | 3,302 Sentry references; PostHog session data. Scrubbing not verifiable |
| **Marketing-site header gaps** | Low-Medium | No CSP/HSTS/XFO on the domain that hosts login entry points |
| **Prompt injection via uploads** | **Medium-High** | Agent has `file-read`, `web-fetch` and `bash`-named tooling; ingesting attacker-influenced documents into an agent with tool access is a live risk class |
| **De-identified data resale** | Reputational | Policy permits sale of de-identified data |

**Ovexis security positioning (recommended, and marketable):** SOC 2 Type II + HITRUST early; published trust center; `security.txt` and a funded VDP; **zero unauthenticated PHI URLs, ever**; break-glass impersonation with dual approval, immutable audit and member-visible access logs; PHI scrubbing in all telemetry with contractual vendor attestation; explicit prompt-injection defenses on document ingestion; and a **binding public commitment never to sell data, de-identified or otherwise.** Every one of these is a sales asset in the employer channel, not just a control.

---

# DELIVERABLE 13 — BUSINESS MODEL

## 13.1 Pricing (🟢 Confirmed unless noted)

| Item | Price | Notes |
|---|---|---|
| Base membership | **$199/yr** | Live homepage, July 2026 |
| NY / NJ membership | ~$399/yr | 🟡 via third-party review; state lab-law variance |
| Historical pricing | $499/yr (Apr 2025) → $199 | 🟢 Fierce Healthcare; schema.org still shows 499 in blog metadata |
| Employer/Thatch | ~$179/yr | 🟡 Sacra |
| Retest panel | $99–$179 | 🟢 $179 on comparison page; $99 cited in third-party review |
| Advanced Blood Panel | ~$388 | 🟡 third-party review |
| At-home draw | Paid add-on | 🟢 |
| Add-on panels | Individually priced | 🟢 (autoimmune, methylation, organ-age, toxins, etc.) |
| Scans | Market rates | 🟢 MRI, DEXA, CAC, VO2max, Galleri |
| Supplements | ~239 SKUs, member pricing | 🟢 |
| Rx / peptides | Separate, subscription | 🟢 |

**The pricing story is the strategy story.** $499 → $199 in roughly a year is a **60% price cut**. 🟡 Strong Inference: this was a deliberate move from premium-concierge positioning to **land-grab positioning**, trading margin for member count and data volume. It is consistent with the self-reported *"grown 10x whilst halving CAC."* It also directly precipitated the competitive conflict with Function ($365) — undercutting a better-capitalized rival by 45% while claiming superior scope is what generated the lawsuit.

## 13.2 Unit economics (🟡 modeled — no audited figures are public)

**This is an analytical model, not reported data. Every input is an estimate and is labeled as such.**

Estimated annual contribution per member at $199:

| Line | Estimate | Basis |
|---|---|---|
| Revenue — membership | $199 | 🟢 |
| Lab COGS (~55 direct analytes at negotiated Quest rates) | –$40 to –$90 | 🔴 estimate |
| Phlebotomy / draw | –$10 to –$25 | 🔴 estimate |
| AI inference (agent, frontier models, long context) | –$10 to –$40 | 🔴 estimate |
| Clinical + member support | –$15 to –$40 | 🔴 estimate |
| Payments, infra, notifications | –$8 to –$15 | 🔴 estimate |
| **Contribution before CAC** | **–$0 to +$115** | wide, and that width is the point |
| CAC (creator + paid + SEO blend) | –$60 to –$180 | 🔴 estimate |
| **Year-1 contribution after CAC** | **Likely negative** | |

🟡 **Strong Inference — the central economic conclusion:** the $199 membership does **not** stand alone. Profitability depends structurally on attach revenue — supplements, Rx subscriptions, scans, add-on panels — and on multi-year retention.

**Why this matters strategically.** It explains, without needing to attribute motive, why:
- the AI agent has a `marketplace-query` tool,
- protocols recommend purchasable supplements,
- the Rx and peptide catalog expanded aggressively,
- the upsell sits at peak intent in onboarding,
- and a **Lifecycle/Retention PMM** is an open role.

**The strategic trap:** a business whose viability requires selling products through a clinical recommendation engine has bounded its own trustworthiness. This is not a moral observation — it is a structural one, and it is the single most exploitable weakness in the company. **Ovexis should design for membership-positive contribution so that recommendations can be genuinely neutral, and then market that neutrality relentlessly.**

## 13.3 Revenue streams, sales motion, retention

**Streams:** membership; retests; add-on panels; scans; supplement marketplace; Rx subscriptions; peptides/GLP-1s; B2B seats; gifting; credits.

**Sales motion:** D2C self-serve (primary); B2B2C via employers/benefits platforms — Thatch, Wellhub, OneDigital, SHRM presence, `/transform-26`, `/shrm-26` 🟢; partner/creator co-marketing pages.

**Retention** 🟡: the structural challenge is that value is front-loaded into the first 30 days (test → reveal → protocol) while the renewal decision arrives 12 months later, after the novelty has decayed and with the proof-of-progress retest behind an additional paywall. The insight feed, wearable sync, and iOS app are all mitigations for exactly this. **The open Lifecycle/Retention PMM role is the strongest available evidence that renewals are a live concern** — you don't create that role when the curve is healthy.

**Expansion:** ARPU expansion is the clear priority — scans, Rx, peptides, GLP-1s all raise revenue per member without new acquisition cost.

---

# DELIVERABLE 14 — GROWTH STRATEGY

## 14.1 SEO — their most valuable durable asset (🟢 Confirmed)

**6,186 indexed URLs across four sitemaps:**

| Cluster | Count | Intent captured |
|---|---|---|
| `/locations/*` | **3,454** | "blood test near me" — state → city → facility |
| `/guides/*` | 1,532 | informational/top-funnel |
| `/marketplace/*` | 239 | product/commercial |
| `/biomarkers/*` | 388 | "what is [analyte]" — high-intent educational |
| `/best-biomarkers/*` | 25 | goal-based ("biomarkers for sleep quality") |
| `/superpower-vs-*` + `/biomarker-testing-companies/*` | 24 | **bottom-funnel comparison** |
| `/ssot-categories/*` | 14 | topical authority hubs |
| `/calculator/*` | 11 | tool-based link bait |
| `/library/*`, `/blog/*`, `/studies` | 46+ | authority |

**Assessment:** this is a genuinely excellent, compounding, low-marginal-cost acquisition machine. The three-tier structure (educational biomarker pages → goal-based clusters → comparison pages) covers the full funnel. **Ovexis should copy this architecture directly** — it is the highest-ROI item in the entire report to replicate.

**One critical improvement:** their pages carry generic bylines (`/author/superpower-team`). Ovexis should attach **named clinical reviewers with credentials and review dates** to every medical page. That is both an E-E-A-T ranking advantage and a trust differentiator, and it costs very little.

## 14.2 Channels

- **Creator/celebrity** 🟢 — Giannis Antetokounmpo (investor + Global Brand Ambassador), Kylian Mbappé, Steve Aoki, Vanessa Hudgens, Logan Paul, Brooke Monke, Shaan Puri. Dedicated landing pages per creator. Micro-influencer testimonials embedded on homepage (`@avnibarman_` 406k, `@stefarmstead` 104k).
- **Paid social with comparative advertising** 🟢 — the practice now under litigation.
- **PR** 🟢 — TechCrunch, Forbes, Fierce Healthcare, Business Insider (multiple exclusives), Longevity.Technology.
- **Founder brand** 🟢 — Marchione's manifestos (`/why`, `/roadmap`), podcast circuit; Peters on Pod of Jake.
- **Partnerships** 🟢 — SoulCycle, Thatch, Wellhub, OneDigital, Wyndly; partner pages for Ramp, Notion, Sequoia, Maven, Wordware.
- **Events** 🟢 — SHRM 2026, Transform 2026, `/events/{eventId}/registration`.
- **Email/lifecycle** 🟢 — Klaviyo; "Superpower Code" lead magnet; Knock in-product.
- **Community** 🟡 — member stories, Trustpilot cultivation. No forum or owned community observed.
- **Developer relations** 🟢 **— none.** No API, no docs, no devrel.

## 14.3 Virality mechanics
Gifting (seasonal pages), referral (`_app.invite`), family-risk public share links, and score-comparison social behavior — Forbes quoted a member describing people *"comparing their superpower scores at the dinner table."* 🟢 That is organic virality worth designing for deliberately.

---

# DELIVERABLE 15 — HIRING INTELLIGENCE

*Full role list and analysis in §2.4. Roadmap inference below.*

**What the open roles predict** (🟡 Strong Inference):

| Signal | Inferred roadmap item |
|---|---|
| Head of Engineering + platform hires | Re-platforming; paying down `v2`/`legacy` debt; scaling infra |
| CMO + Creator in Residence + 3 designers | Major brand campaign; continued creator-led growth |
| Head of Legal ("integrated operating system") | Litigation defense + regulatory buildout for Rx/peptides |
| Founding Lead Strategic Sales + SDR Lead | **Enterprise/employer push is imminent and funded** |
| Lifecycle/Retention PMM | Renewal and churn intervention program |
| Longevity NP (multi-state, CA required) + Collaborating Physician | Expanding telehealth prescribing footprint state-by-state |
| Member Success Representative | Direct response to documented support failures |
| Chief of Staff | Fundraise/ops leverage for CEO |

**Engineering maturity assessment** 🟡: strong individual craft (Rive motion, AG-UI/LangGraph agent, FHIR core, hardened API) but **organizationally immature** — no Head of Engineering until now, coexisting v1/v2 surfaces, dev affordances in production, inconsistent security headers across origins. Estimated engineering headcount: 🔴 **15–30**, inferred from route surface area, chunk count, release cadence and the size of the open-role list. This is an estimate, not a reported figure.

---

# DELIVERABLE 16 — CUSTOMER INTELLIGENCE

## Praise (🟢 from Trustpilot, published reviews, homepage testimonials)
- Data aggregation genuinely valued: *"Being able to upload past labs and DEXA scans, while also connecting data from my wearables… I can see my labs, sleep, activity, and other health information in one place."*
- Finding overlooked issues — the recurring theme, and the emotional core of the product
- Price-to-value at $199 widely seen as strong
- Dashboard/UX quality consistently praised
- PCP acceptance because draws run through Quest: *"my PCP is open to seeing the labs… since they are drawn at a nationally recognized lab"*
- Rating ~4.6/5 with 260+ reviews 🟡 (self-reported placement)

## Complaints (🟢 documented)
1. **Support unreachability — the dominant complaint.** A detailed Trustpilot account: draw on 18 May 2026, partial results 19 May, majority of biomarkers still missing by 2 June; phone never answered by a human; in-app AI gave *"generic apologies and no actual answers"*; emails unanswered. Member's summary: *"The technology, marketing, and user interface may be impressive, but when a problem arises, customer support appears to be virtually nonexistent."*
2. **Result delays and missing biomarkers** — partial panels without explanation.
3. **Biological age is not credible across vendors** — one reviewer: Superpower 45.2, Function 37.3, Hundred 38.0, within months. Her conclusion: *"Use biological age as a trend line within one service and put your confidence in the raw biomarkers instead."*
4. **Clinical over-flagging.** The Skeptical Cardiologist reviewed his own results: *"When I looked closely at the 10 biomarker values flagged as abnormal by Superpower it turns out that each one was not of clinical concern."* He characterizes "more biomarkers is better" as marketing.
5. **NY/NJ price disparity** (~2x) with limited explanation.
6. **Retest paywall** perceived as nickel-and-diming the core value.

## Feature requests / unmet needs (🟡 synthesized)
Direct EHR connection; clinician-shareable structured summary; Android app; international availability; longer trend history without repurchase; clearer separation of recommendation from sales; transparency on score methodology.

## Churn drivers (🟡)
Novelty decay after the reveal; no new data between annual draws unless wearables are connected; retest cost; support failure at the moment of anxiety; unresolved "so what do I do now" after the first protocol.

## Unexpected use cases (🟢)
Gifting as a relationship intervention (*"I got my boyfriend a Superpower blood test"*); dinner-table score comparison; using results as ammunition to be taken seriously by one's own physician; couples/family testing.

---

# DELIVERABLE 17 — DECISION LEDGER (abridged; full version in workbook Sheet 1)

| Feature | Why built | Pain solved | KPI improved | Trade-off accepted | Alternative architecture |
|---|---|---|---|---|---|
| $199 100+ marker panel | Acquisition wedge; data asset creation | "I don't know what's wrong" | CAC, conversion, member count | Thin/negative membership margin; commoditizable | Higher price + fewer, better-chosen markers |
| Derived indices counted as biomarkers | Inflate headline count at zero lab cost | Competitive comparison | Ad CTR, conversion | **Lanham Act exposure — realized** | Label clearly as derived; compete on interpretation |
| Superpower Score + Bio Age | Single memorable number | "Am I okay?" | Activation, virality, retention | Not reproducible; scientifically criticized | Publish methodology + CI; show trend not absolute |
| FHIR-native citations | Trust, traceability | "Why should I believe this AI?" | Trust, engagement, safety | Engineering cost | Free-text disclaimers (weaker, cheaper) |
| Compressed memory | Long-horizon context economically | "I have to re-explain everything" | Session depth, retention | Lossy summarization of clinical facts | Typed structured memory (recommended for Ovexis) |
| `marketplace-query` in agent | Monetize the conversation | "Where do I get this?" | Attach rate, ARPU | **Structural conflict of interest** | Separate commerce agent with disclosed handoff |
| Retest at $99–179 | Protect margin | — | Revenue per member | Suppresses the data-moat behavior | Bundle 2 draws; monetize depth instead |
| Public family-share link | Frictionless virality | "I want to show my family" | Referral, K-factor | **Unauthenticated PHI exposure** | Scoped, expiring, revocable tokens |
| Admin impersonation | Support efficiency | Ops resolution time | Support SLA | Insider-risk surface | Break-glass + dual approval + member-visible log |
| Programmatic SEO (6,186 pages) | Compounding low-CAC acquisition | Discovery | Organic traffic, blended CAC | Thin-content risk; clinical review burden | Fewer, deeper, clinician-reviewed pages |
| Vital for wearables | Ship 10 integrations in weeks | "My data is scattered" | Time-to-market, activation | Vendor dependency, per-user cost | Direct APIs (slower, cheaper at scale) |
| Medplum FHIR core | Interoperability without building it | Data model correctness | Eng velocity, AI groundability | Platform dependency | Custom schema (faster short-term, fatal long-term) |
| Peptides / GLP-1s | ARPU expansion | "I want access" | ARPU, LTV | **Highest regulatory + reputational risk** | Evidence-gated formulary only |
| Cash-pay, no insurance | Avoid payer complexity entirely | Access friction | Speed, simplicity | TAM ceiling; equity criticism | Employer + FSA/HSA (they now do this) |

---

# DELIVERABLE 18 — FEATURE DEPENDENCY GRAPH

```
                          ┌──────────────────┐
                          │ 1. IDENTITY      │  better-auth · magic link · OTP
                          │    + ACCOUNT     │  org accounts (B2B)
                          └────────┬─────────┘
                                   ▼
                          ┌──────────────────┐
                          │ 2. CONSENT       │  informed · PHI · marketing
                          │    (versioned)   │  Rx ToS · SMS · proxy
                          └────────┬─────────┘   ◀── GATES EVERYTHING BELOW
                                   ▼
              ┌────────────────────┼────────────────────┐
              ▼                    ▼                    ▼
     ┌─────────────────┐  ┌─────────────────┐  ┌──────────────────┐
     │ 3a. INTAKE      │  │ 3b. SPECIMEN    │  │ 3c. IMPORTED     │
     │ questionnaires  │  │ serviceability →│  │ DATA             │
     │ demographics    │  │ schedule → draw │  │ PDFs · wearables │
     │ history         │  │ → lab → redraw  │  │ · AI chat logs   │
     └────────┬────────┘  └────────┬────────┘  └────────┬─────────┘
              └────────────────────┼────────────────────┘
                                   ▼
                    ┌──────────────────────────────┐
                    │ 4. NORMALIZATION             │
                    │ LOINC-style vocabulary ·     │
                    │ units · optimal ranges ·     │
                    │ recency index · provenance   │
                    └──────────────┬───────────────┘
                                   ▼
                    ┌──────────────────────────────┐
                    │ 5. FHIR CLINICAL CORE        │  ◀── THE KEYSTONE
                    │ Observation · DiagnosticRpt  │      Everything above
                    │ Patient · Communication ·    │      feeds it; everything
                    │ QuestionnaireResponse · Goal │      below depends on it
                    └──────────────┬───────────────┘
                     ┌─────────────┼─────────────┐
                     ▼             ▼             ▼
          ┌────────────────┐ ┌───────────┐ ┌──────────────┐
          │ 6a. SCORING    │ │ 6b. AI    │ │ 6c. CDS      │
          │ SP Score       │ │ AGENT     │ │ HOOKS +      │
          │ Bio Age        │ │ 16 tools  │ │ SUBSCRIPTIONS│
          │ 13 organ scores│ │ memory    │ │ (capability) │
          │ digital twin   │ │ citations │ │              │
          └───────┬────────┘ └─────┬─────┘ └──────┬───────┘
                  └────────────────┼──────────────┘
                                   ▼
                    ┌──────────────────────────────┐
                    │ 7. PROTOCOL v2               │
                    │ actions · goals · targets ·  │
                    │ citations · completion state │
                    └──────────────┬───────────────┘
                     ┌─────────────┼─────────────┬──────────────┐
                     ▼             ▼             ▼              ▼
              ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌─────────────┐
              │ 8a.REVEAL │ │ 8b.INSIGHT│ │ 8c.CARE   │ │ 8d.COMMERCE │
              │ cinematic │ │ FEED +    │ │ TEAM chat │ │ supplements │
              │ sequence  │ │ OUTREACH  │ │ consults  │ │ Rx · scans  │
              └─────┬─────┘ └─────┬─────┘ │ escalation│ └──────┬──────┘
                    │             │       └─────┬─────┘        │
                    └─────────────┴─────────────┴──────────────┘
                                   ▼
                    ┌──────────────────────────────┐
                    │ 9. RETEST / REDRAW           │
                    │ → new observations → back to │
                    │    step 4 (the data loop)    │
                    └──────────────┬───────────────┘
                                   ▼
                    ┌──────────────────────────────┐
                    │ 10. RENEWAL · REFERRAL ·     │
                    │     FAMILY SHARE · GIFTING   │
                    └──────────────────────────────┘

  ✗ MISSING EDGE: no path from (5) FHIR CORE outward to
    physician / EHR / HIE. The record is a well-built
    cul-de-sac. ◀── Ovexis's strategic entry point.
```

**Critical-path reading for Ovexis:** Consent (2), Normalization (4) and the FHIR Core (5) are the **irreversible architectural commitments**. Get them wrong and everything above collapses; get them right and features 6–10 become interchangeable and cheap. Build 2, 4 and 5 with disproportionate rigor before shipping any AI feature.

---

# DELIVERABLE 19 — ENGINEERING BACKLOG RECONSTRUCTION

🟡 All version boundaries inferred from route naming, API versioning, press dates and the public roadmap.

**MVP (2023 – mid 2024)** — beta membership, manual-heavy ops, basic lab ordering, results display, "hundreds of testing partners," concierge by human. Evidence: BusinessWire pre-seed language.

**V1 (late 2024 – Q1 2025)** — `/protocol/legacy` era. Superpower Score, biological age, biomarker dashboard, health records upload, human care team, marketplace v1, `biomarker-legacy-dialog`. Priced $499.

**V2 (Q2 2025 – Q4 2025)** — Series A build-out. `protocol-v2` with actions/goals; wearables via Vital; `chatv3`; Feminade + Base integrations; scans; Rx; supplement marketplace expansion; cinematic reveal; price cut to $199.

**V3 (Q1 2026 – present)** — the AI era. AI Doctor launch (247 commits, ~140k LOC, Feb 2026); `chatv4`; AG-UI + LangGraph agent; compressed memory; FHIR citations; Think tab; cross-AI import; digital twin; iOS app; peptides waitlist; family risk; employer channel.

**Observable technical debt** 🟢:
- `protocol/legacy` + `protocol-v2` coexisting
- `chatv3/search` + `chatv4/messages` coexisting
- `biomarker-legacy-dialog` alongside `biomarker-dialog`
- `marketplace/products/by-legacy-service-id/{serviceId}` — legacy ID mapping shim
- `welcome-new-sep-2025-backup-mar-26-2026`, `vast-old`, `stratos-v1`, `tiers-test-2` — abandoned experiment pages in the production sitemap
- Dev affordances shipped: `dev:simulate-compaction`, `/protocol/dev`
- Security headers inconsistent across origins

**Inferred near-term backlog** 🟡: Android app; direct EHR/HIE connectivity; SOC 2; clinician-facing surface; deeper digital twin (simulation); GLP-1 scale-up; organ-age testing; international; API/partner platform; retention instrumentation.

---

# DELIVERABLE 20 — COMPETITIVE LANDSCAPE

*Full matrix in workbook Sheet 3. Strategic synthesis here.*

## 20.1 The five competitive layers

Superpower does not have one competitor set — it has five, and it is losing or winning differently in each.

**Layer 1 — Direct biomarker memberships.** Function Health ($365, $2.5B valuation, $298M raised, acquired Ezra for MRI), Mito Health (~$99), InsideTracker, Lifeforce, SiPhox, Hundred Health, Everlywell.
→ *Superpower's position:* price leader with the deepest action layer. **But Function has ~6x the capital and is buying capability (Ezra) while Superpower buys datasets (Base, Feminade).** In a war of attrition on panel price, Superpower loses.

**Layer 2 — Premium preventive clinics.** Neko Health (£299, $1.02B raised), Prenuvo (~$2,500), Human Longevity (~$8,000), Biograph ($7,500–15,000), Fountain Life.
→ *Superpower's position:* they undercut this tier by 10–40x and market against it explicitly (*"What could cost $10,000 is now $199"*). This is their strongest rhetorical position and it is genuinely defensible.

**Layer 3 — Wearables.** Whoop, Oura, Ultrahuman, Apple, Garmin.
→ *Superpower's position:* they **integrate rather than compete** (via Vital), which is correct. The risk is inversion: Oura and Whoop have continuous data, enormous retention, retail distribution and existing subscription relationships. **If a major wearable adds blood testing, Superpower's wedge narrows overnight.** Ultrahuman is already moving this way.

**Layer 4 — Platform/OS layer.** Apple Health, Google Health Connect.
→ *Superpower's position:* structurally exposed. Apple owns the device, the health data store, and the trust relationship. 🔴 Speculation but strategically vital: if Apple ships meaningful health interpretation, the aggregation value proposition of every company in this category compresses. **Neither Superpower nor Ovexis can win a pure aggregation war against the OS. The defensible ground is interpretation + care + action, not storage.**

**Layer 5 — Clinical AI.** OpenEvidence (physician-trusted, citation-rigorous, viral among MDs), Glass Health, Atropos, UpToDate, AMBOSS.
→ *Superpower's position:* **completely absent.** They have no clinician-facing product and no clinical credibility with physicians. OpenEvidence has demonstrated that the fastest way to build medical AI trust is to earn it from doctors first. This is a strategic blind spot.

**Adjacent — India/global volume players.** Apollo 24/7, Practo, Tata 1mg, Healthify.
→ Enormous distribution and low-cost diagnostics, weak longitudinal intelligence. **Uncontested by Superpower entirely (US-only).**

**Not verifiable:** Regacore and PreventiveHealth.ai returned no reliable public information. 🔴 Marked absent rather than invented.

## 20.2 Common features (table stakes)
Comprehensive panel, dashboard with ranges, biological age, trend tracking, wearable sync, AI chat, PDF upload, HSA/FSA eligibility, supplement recommendations, membership pricing.

## 20.3 Superpower's genuinely unique features (🟢)
1. **FHIR-native citations resolving to specific observations** — I found no competitor doing this at this fidelity
2. **Cross-AI conversation import** (ChatGPT/Claude/Gemini/Perplexity/Grok) — a genuinely original growth wedge
3. **Full vertical stack in one app** — labs + AI + supplements + Rx + peptides + scans
4. **AG-UI/LangGraph agent with 16 tools and transparent reasoning**
5. **The anti-optimization brand position** (`/why`) — strategically the smartest thing they have written
6. **Programmatic SEO at 6,186 pages**

## 20.4 Blind spots — ranked by exploitability for Ovexis

| # | Blind spot | Why it persists | Ovexis exploit |
|---|---|---|---|
| 1 | **No clinician-facing product** | Consumer-brand thesis | Build the physician surface; make doctors the distribution channel |
| 2 | **No published clinical validation** | Speed culture; no academic incentive | Publish validation; own the evidence high ground |
| 3 | **Commerce conflict inside the AI** | Unit economics require attach | Structural separation + public conflict policy |
| 4 | **No interoperability outward (TEFCA/EHR)** | Walled-garden lock-in strategy | Real interoperability as the differentiator |
| 5 | **Support quality at scale** | Cost structure at $199 | Guaranteed human SLA as a paid tier feature |
| 6 | **US-only** | Focus | International, starting where diagnostics are cheap |
| 7 | **No SOC 2 / trust center** | Not yet needed for D2C | Enterprise-grade compliance as a sales weapon |
| 8 | **No developer API** | Surface minimization | Open API + data portability |
| 9 | **Overdiagnosis risk unmanaged** | Founding bias toward more testing | Pre-test probability framing; suppress non-actionable flags |
| 10 | **Bio-age not reproducible** | Marketing utility exceeds scientific rigor | Publish methodology, versioning, CIs |

---

# DELIVERABLE 21 — MOAT ANALYSIS

| Moat | Strength today | Trajectory | Assessment |
|---|---|---|---|
| **Data moat** | **Medium** | Strengthening | Longitudinal multi-modal records + Base nutrition data + ~1M biomarkers tested (claimed). Real, but retest paywall throttles the very accumulation that creates it. |
| **AI moat** | **Medium** | Strengthening | The *architecture* (FHIR citations, structured memory, agent graph) is genuinely good and roughly 12–18 months ahead of typical consumer health AI. But architecture is copyable; **without clinical validation it is not a moat, it is a head start.** |
| **Clinical moat** | **Weak** | Flat | Advisory board of known names; no published research; no proprietary clinical evidence; no clinician relationships. |
| **Brand moat** | **Medium-Strong** | **At risk** | superpower.com, Giannis, strong design, cultural fluency. But brand in healthcare is fragile — and the lawsuit, support complaints and peptide-culture reporting are all withdrawals from that account. |
| **Distribution moat** | **Medium** | Strengthening | 6,186 SEO pages compounding; celebrity reach; employer channel emerging. SEO is the most durable component. |
| **Developer moat** | **None** | Flat | No API, no docs, no ecosystem. |
| **Marketplace moat** | **Weak** | Flat | ~239 SKUs of third-party supplements — no exclusivity, no proprietary formulation, fully replicable. |
| **Regulatory moat** | **Weak / Negative** | **Deteriorating** | Multi-state telehealth licensure is real but modest. Peptides and aggressive marketing create *negative* regulatory equity. |
| **Network effects** | **Weak** | Slight | Family sharing and score-comparison create mild social pull. No true multi-sided network. |
| **Switching costs** | **Medium** | Strengthening | Uploaded history + longitudinal trends + AI memory create genuine stickiness. **Their strongest under-appreciated asset.** No export path makes leaving costly — though that cuts against them ethically and, eventually, legally. |
| **Trust moat** | **Weak-Medium** | **Deteriorating** | The FHIR citation system builds trust; the lawsuit, support failures, commerce conflict and data-sale clause erode it. |

## The strategic verdict

**Superpower has a speed advantage and an architecture advantage, not a moat.** Every element of what they have built could be replicated by a well-executed team in 12–24 months. Their genuine defensibility reduces to two things: the accumulated longitudinal dataset (which they are throttling with paywalls) and the brand (which they are spending down through legal and operational missteps).

🔴 **Speculation, offered as a board judgment:** the durable moat in this category will not be data volume or AI architecture. It will be **verified clinical trust** — the ability to make a claim that a physician, a regulator, an employer's benefits committee and a member all believe simultaneously. Nobody in this category has built that yet. **It is available, and it is what Ovexis should build.**

---

# DELIVERABLE 22 — FAILURE ANALYSIS

| Mode | Mechanism | Likelihood | Severity |
|---|---|---|---|
| **Clinical** | A member is falsely reassured by AI guidance and a serious diagnosis is delayed. One well-documented case, amplified, becomes an existential brand event. | Medium | **Existential** |
| **Clinical** | Overdiagnosis cascade — false positives drive unnecessary imaging, biopsies, anxiety. Already criticized publicly by a cardiologist reviewing his own results. | High | High |
| **Regulatory** | FDA determines the AI Doctor's differential-diagnosis behavior constitutes a medical device requiring clearance. | Medium | High |
| **Regulatory** | FTC or state AG action on advertising substantiation — the Function complaint is a public roadmap for a regulator. | Medium | High |
| **Regulatory** | Enforcement on compounded peptides/GLP-1s; state pharmacy or medical-board action. | Medium-High | High |
| **Legal** | Adverse ruling or damaging discovery in *Function v. Superpower*. Discovery is the underrated risk — internal marketing communications become evidence. | Medium | High |
| **Business** | Function outspends them into irrelevance with 6x capital. | Medium-High | High |
| **Business** | Unit economics never close — attach revenue insufficient, membership contribution stays negative, Series B is hard. | Medium | **Existential** |
| **Business** | Retention collapse after year 1 — the structural churn risk. | Medium-High | High |
| **Operational** | Support failure scales faster than support capacity; Trustpilot and Reddit sentiment inverts. | High | Medium-High |
| **Operational** | Quest concentration — a pricing change, capacity constraint or partnership termination disrupts fulfillment. | Low-Medium | High |
| **Security** | PHI breach via public share links, impersonation abuse, or a third-party vendor. | Medium | **Existential** |
| **AI** | Systematic hallucination or a harmful recommendation pattern discovered and publicized. | Medium | **Existential** |
| **AI** | Inference costs rise or frontier-model policy restricts medical use cases. | Medium | Medium |
| **Distribution** | Creator channel saturates; CAC inflates past LTV. | Medium-High | High |
| **Platform** | Apple or Google ships native health interpretation, commoditizing aggregation. | Low-Medium (3yr) | High |
| **Economic** | Consumer discretionary spending contracts; $199 wellness subscriptions churn first. | Medium | Medium-High |
| **Cultural** | Peptide self-experimentation narrative becomes the defining public story of the company. | Medium | Medium-High |

**The two failure modes that should keep their board awake:** (1) a single publicized clinical harm event, and (2) unit economics that never close, forcing either a price increase that kills growth or an attach-rate push that further compromises clinical credibility. **Both are structural, not tactical.**

---

# DELIVERABLE 23 — COMPETITIVE ATTACK PLAN
### How Ovexis beats Superpower

**The core strategic insight:** Superpower is optimizing for *reach*. Their weakness is *credibility*. Do not fight them on price, panel size, or celebrity reach — you will lose all three. **Fight them on trust, and make trust operationally real rather than rhetorical.**

## Attack 1 — Trust as product architecture (the primary wedge)
- **Never sell what you recommend.** Structural separation: the recommendation engine has no access to margin data. Publish this as an architectural guarantee, not a promise.
- **Count only direct measurements.** Publish a public methodology page defining every metric. When competitors are dragged toward this standard by litigation, you were already there.
- **Publish confidence, not just answers.** Every score carries a version, a reference population and a confidence interval.
- **Binding no-data-sale commitment**, including de-identified data. Superpower's policy explicitly permits the opposite — quote it in comparison material (accurately, with a date).
- **Public trust center**, SOC 2 Type II, `security.txt`, funded VDP.

## Attack 2 — Clinical validation as a moat
- Publish a peer-reviewed validation of your scoring model. Nobody in this category has done this. It is cheap relative to $298M and it is permanently differentiating.
- Build an **eval harness with clinician-labeled gold sets**, publish aggregate performance, and gate releases on it.
- Recruit a **clinical epidemiologist with veto authority** — the skeptic Superpower's advisory board lacks — and say so publicly.
- Adopt explicit **overdiagnosis stewardship**: report pre-test probability, suppress non-actionable flags, and refuse to flag what you cannot act on.

## Attack 3 — Own the physician
This is the largest uncontested territory. Superpower has no clinician product at all.
- Structured, provenance-complete clinical summary exportable to any physician
- C-CDA / FHIR export; TEFCA participation; fax and Direct messaging for the real world
- A free clinician view — let doctors see their patient's longitudinal record
- **Doctors become the acquisition channel.** OpenEvidence proved physician-first trust compounds faster than consumer marketing.

## Attack 4 — Fix the retention loop they broke
- Include **two draws in the base membership**. Their retest paywall throttles their own moat.
- Make wearable-driven insight the between-draw value engine.
- Event-driven care: data changes trigger outreach, not the calendar.
- **Guaranteed human response SLA** — their single most documented failure, and a cheap promise to keep if designed in from day one.

## Attack 5 — Architecture they cannot quickly copy
- **Typed clinical memory** (FHIR resources with pertinent negatives as first-class `verificationStatus: refuted`) instead of lossy prose compaction
- **Unified provenance grammar** across labs, wearables, imaging, notes, genomics and literature
- **Simulation-grade digital twin** — counterfactual projection ("what happens if I do X for 90 days"), not a 3D render
- **Model-agnostic router** with distillation for routine tasks — better margins at consumer price points
- **Open FHIR API + full member data export** — portability as a competitive weapon against a walled garden

## Attack 6 — Distribution asymmetry
- Copy the SEO architecture exactly, but with **named clinical reviewers** on every page (E-E-A-T advantage)
- **Answer-engine optimization** — structure content so LLM assistants cite you; discovery is migrating there and Superpower is still optimizing for Google
- **Employer channel with outcome contracts** — sell measurable risk reduction, not seats
- **International** — Superpower is US-only. India, Gulf, SE Asia have cheap diagnostics, rising affluence and no credible longitudinal intelligence layer
- **Never run comparative advertising.** It generated their lawsuit. Publish a neutral, dated, sourced methodology comparison instead and let it rank.

## Attack 7 — What NOT to copy (discipline is strategy)
❌ Unproven peptides · ❌ celebrity medical claims · ❌ derived metrics counted as tests · ❌ headline biological age · ❌ public PHI URLs · ❌ commerce inside the clinical agent · ❌ comparative attack ads · ❌ consent bundled into checkout · ❌ selling de-identified data

---

# DELIVERABLE 24 — FUTURE PREDICTION

## Next 12 months (to mid-2027) — 🟡 Strong Inference
1. **Series B raised** on the AI Doctor narrative — $60–150M at $500M–1B, or a down-round/flat outcome if litigation drags. Bond Capital and 8VC already on the register.
2. **Function litigation resolves** — most likely a confidential settlement with marketing-practice undertakings.
3. **Android app** ships; iOS deepens with HealthKit background sync.
4. **Employer channel scales** — the Strategic Sales hires deliver; benefits-platform partnerships multiply.
5. **GLP-1 becomes a material revenue line** — highest-demand, highest-margin product in the catalog.
6. **A clinical-safety incident or investigative story** — 🔴 Speculation, but the risk surface (peptides, AI advice, support gaps) makes this materially likely.
7. **Marketing language continues to soften** under legal supervision.

## Next 3 years (to 2029)
1. **Category consolidation.** 🟡 Two or three winners emerge; sub-scale players (Mito, SiPhox, Hundred) are acquired or fold.
2. **Superpower is acquired or acquires.** 🔴 Most probable acquirers: a diagnostics/retail-pharmacy incumbent, a wearable company needing a clinical layer, or a benefits platform.
3. **Digital twin becomes simulation.** The genuinely hard technical bet, and the one that would justify the valuation.
4. **Regulatory framework arrives** for consumer health AI — first-mover compliance becomes an advantage.
5. **Insurance/employer reimbursement begins** for validated preventive programs — and only companies with published outcomes data will qualify. **This is where Superpower's missing validation becomes a strategic liability, and Ovexis's investment in it pays off.**
6. **Wearable convergence** — Oura/Whoop/Apple add blood or deeper clinical layers.

## Next 5 years (to 2031)
🔴 Speculation, offered as scenario planning:
- **Bull case:** Superpower becomes the consumer front door for health for 5–10M members, with AI-delivered care as the primary interaction and diagnostics as commodity input. Valuation $5–15B.
- **Base case:** a strong sub-scale player, $200–500M revenue, acquired by a strategic at $1–3B.
- **Bear case:** a clinical or regulatory event, combined with Function's capital advantage, forces a distressed sale of the brand and dataset.

**Likely AI investments:** proprietary fine-tuning on longitudinal biomarker data; simulation/counterfactual modeling; voice interaction; ambient/passive capture; multimodal imaging interpretation; on-device inference for privacy positioning.

**Likely partnerships:** additional lab networks (Labcorp) to reduce Quest concentration; imaging networks; pharmacy/compounding at scale; benefits platforms; a wearable OEM; possibly an academic medical center for the validation credibility they currently lack.

---

# DELIVERABLE 25 — OVEXIS STRATEGY MEMO

> **A note on the "Top 50" format.** The brief requested 50 items in each of four categories. Padding lists to hit a number produces filler that wastes board attention. What follows is organized by strategic weight — the highest-value items are stated fully; genuinely distinct lower-priority items are listed compactly. Where a category does not contain 50 non-trivial items, it says fewer things well rather than fifty things poorly. The full 55-row feature ledger with copy/improve/ignore/reinvent decisions per feature is in **workbook Sheet 1**, and the 35-item execution ledger is in **Sheet 5**.

## 25.1 COPY — proven patterns, adopt directly

**Tier 1 — copy immediately, these are the crown jewels**
1. FHIR-native citations resolving to specific observations (`fhir://observation/{uuid}`)
2. FHIR-native clinical core from day one (Medplum or equivalent) — retrofitting is fatal
3. Agent activity ticker that narrates tool use during latency
4. Transparent reasoning panel with differentials considered
5. Programmatic SEO architecture: biomarker pages → goal clusters → comparison pages → location pages
6. Lab PDF upload with AI ingestion to backfill history before the first draw
7. Wearable aggregation via a vendor (Vital-class) to ship 10 integrations in weeks
8. Cinematic results reveal as the emotional payoff moment
9. Granular, versioned consent objects (informed / PHI / marketing / Rx / SMS)
10. Auto-escalation of abnormal results to a human care team

**Tier 2 — copy with modification**
11. Superpower-Score-style composite (with published methodology and CIs)
12. Organ/system-level scoring across 13 systems
13. Protocol-with-actions model (action → why → what to watch → target biomarker → citation → completion)
14. Redraw/recollection subsystem — lab logistics fail often; design for it
15. Serviceability check gating scheduling
16. Add-on panel catalog (recommended from risk, not margin)
17. HSA/FSA eligibility with automated substantiation
18. Klarna/BNPL for higher-priced tiers
19. Knock-class notification infrastructure with preference management
20. Cal.com-class scheduling rather than building it
21. Stripe Identity-class KYC for any Rx pathway
22. PostHog feature flags + first-party analytics proxy
23. Sentry release tagging with per-deploy debug IDs
24. Admin/ops console built early — ops is always the bottleneck
25. Gift memberships and seasonal campaigns
26. Referral/invite mechanics
27. Employer channel with HRIS API + 834 EDI support
28. Comparison pages for bottom-funnel intent (neutral, dated, sourced)
29. Member story content with names, ages and specific outcomes
30. Rive-class motion design for the reveal moment
31. Radix + Tailwind design system foundation
32. TanStack Router/Query + Zustand frontend architecture
33. Skill/playbook registry pattern for modular clinical logic
34. Cross-conversation history search
35. Persistent memory tools (save/read) exposed as agent capabilities

## 25.2 IMPROVE — adopt the idea, fix the execution

1. **Typed clinical memory** instead of prose compaction — FHIR resources, pertinent negatives as `verificationStatus: refuted`
2. **Count only direct measurements**; label derived indices explicitly as derived
3. **Publish score methodology**, version, reference population and confidence intervals
4. **Include two draws in base membership** — never paywall the proof of progress
5. **Guaranteed human support SLA** with a published response-time commitment
6. **Separate consent from checkout** — unhurried, comprehension-checked
7. **Scoped, expiring, revocable sharing** — never unauthenticated PHI URLs
8. **Break-glass impersonation** with dual approval, immutable audit, member-visible access log
9. **Uniform security headers** across every origin, including marketing
10. **Multi-lab abstraction** (Quest + Labcorp + regional + at-home) from day one
11. **Own the normalization layer**; treat wearable aggregators as swappable adapters
12. **Evidence-graded protocols** — strength of evidence and citation visible on every recommendation
13. **Overdiagnosis stewardship** — pre-test probability framing; suppress non-actionable flags
14. **Model-agnostic router** with distillation for routine tasks
15. **Clinician-reviewed SEO content** with named reviewers and review dates
16. **Recommendation engine blind to margin** — structural, not policy
17. **Deprecation discipline** — no v1/v2 coexistence in production
18. **Prompt-injection defenses** on all document ingestion into an agent with tools
19. **PHI scrubbing** in all telemetry, contractually attested by vendors
20. **Accessibility beyond Radix defaults** — WCAG 2.2 AA published commitment
21. **Progressive profiling** instead of long upfront questionnaires
22. **Serviceability check before payment**, not after
23. **Post-cancellation data stewardship** — clear export and deletion path
24. **Named clinician continuity** for higher tiers
25. **Confidence and abstention** surfaced in AI responses

## 25.3 IGNORE — do not build these

1. Unproven peptide catalog (sermorelin, GHK-Cu, VIP, gonadorelin as marketed)
2. Celebrity medical endorsement as a primary channel
3. Comparative attack advertising
4. Derived metrics marketed as tests
5. Headline biological age as a marketing number
6. Public unauthenticated PHI share links
7. Commerce tooling inside the clinical reasoning agent
8. Selling de-identified member data
9. Consent bundled into the purchase flow
10. Aggressive upsell placed at peak vulnerability
11. Dev/test affordances shipped to production
12. Abandoned experiment pages left in the production sitemap
13. Panel-size arms race ("more biomarkers" as differentiation)
14. Walled-garden data lock-in as a retention strategy
15. Brand-as-moat as the primary strategic thesis in a clinical category

## 25.4 REINVENT — where Ovexis creates new category ground

1. **Simulation-grade digital twin** — counterfactual projection with explicit uncertainty, not a 3D body render
2. **Provenance graph across every modality** — one citation grammar for labs, wearables, imaging, notes, genomics, literature
3. **Clinician as first-class user** — free physician view, structured export, TEFCA participation
4. **Outcome-based employer contracts** — sell measurable risk reduction, not seats
5. **Open FHIR API + complete member data export** — portability as a weapon
6. **Published clinical validation** — peer-reviewed, the first in the category
7. **Adaptive retest intervals** driven by biological variance and individual risk, not the calendar
8. **Two-way MCP connector** to general AI assistants, replacing manual copy-paste import
9. **Consent as a queryable data structure** with full revocation and audit
10. **Conflict-free formulary** — neutral, pass-through pricing, published economics
11. **Answer-engine optimization** as the primary discovery investment
12. **Clinical eval harness as a public artifact** — publish your model's performance
13. **International-first architecture** — multi-currency, multi-lab, multi-regulatory from day one
14. **Event-driven care** — data deltas trigger clinical workflows automatically (CDS Hooks used properly)
15. **Family/household as the account primitive**, with proper per-member consent

## 25.5 Market gaps (the 15 that matter)

1. No credible clinician-facing longitudinal intelligence product
2. No published validation of any consumer biological-age or health score
3. No conflict-free recommendation engine in consumer health
4. No real interoperability (TEFCA/EHR write-back) in the consumer longevity category
5. No serious international player outside the US/UK
6. Complex chronic and multi-morbid patients — highest clinical value, entirely unserved
7. Medicare-age population — largest disease burden, ignored by every player
8. No developer ecosystem or API in the category
9. Overdiagnosis stewardship — nobody is competing on *restraint*
10. Post-diagnosis navigation ("I found something — now what?")
11. Family/household health management as a coherent product
12. Employer outcome contracts (risk-shared pricing)
13. Pediatric and adolescent preventive intelligence
14. Women's health longitudinal depth beyond hormone panels
15. Affordable tier (<$99) with genuine clinical quality

## 25.6 Blue-ocean opportunities (10, ranked by defensibility)

1. **The physician's longitudinal co-pilot** — patient-consented record + AI summary delivered into clinical workflow
2. **Validated preventive outcomes for payers/employers** — the reimbursement unlock
3. **Simulation-based health counterfactuals** — genuinely hard, genuinely defensible
4. **India/Gulf/SE Asia premium preventive intelligence** — cheap diagnostics, rising affluence, no incumbent
5. **Chronic-condition longitudinal intelligence** (diabetes, autoimmune, cardiometabolic)
6. **Health data portability infrastructure** — the anti-walled-garden play
7. **Clinical AI evaluation as a public standard** — define the benchmark others must meet
8. **Household/multi-generational health accounts**
9. **Post-screening navigation and triage** — the unmet need every screening company creates
10. **Regulatory-grade audit infrastructure** for consumer health AI

## 25.7 Recommended MVP (6 months, ~10–14 people)

**Build:**
- FHIR-native clinical core (Medplum or equivalent) — **non-negotiable, week one**
- Granular versioned consent, separated from checkout
- Multi-lab ordering abstraction (start with two labs)
- Lab PDF ingestion → LOINC normalization → provenance-tracked observations
- Wearable sync via aggregator (Apple Health, Oura, Whoop, Garmin, Fitbit)
- Composite score + organ scores **with published methodology and confidence intervals**
- AI agent: AG-UI-class streaming, unified citation grammar, typed clinical memory, transparent reasoning, **explicit abstention**
- Clinical eval harness with clinician-labeled gold sets, gating every release
- Protocol with evidence grades and citations — **no commerce integration**
- Human care-team messaging with a published SLA and auto-escalation for critical values
- Member data export (FHIR + PDF) from day one
- Ops console

**Deliberately deferred:** supplements marketplace, Rx, peptides, scans, digital twin visualization, Android, international.

**Pricing:** $249/yr including **two blood draws**, HSA/FSA eligible. Positioned above Superpower's $199 and below Function's $365, justified by two draws, published validation and conflict-free recommendations.

## 25.8 Recommended GTM
**Phase 1 (0–6mo):** clinician-reviewed programmatic SEO + answer-engine optimization; design-partner employers (3–5); no paid social.
**Phase 2 (6–18mo):** physician channel — free clinician view drives patient referral; employer channel with 834/HRIS; content-led authority.
**Phase 3 (18mo+):** outcome contracts; international; open API ecosystem.
**Never:** comparative attack advertising, celebrity medical claims.

## 25.9 Recommended moat stack
Primary: **verified clinical trust** (published validation + conflict-free architecture + interoperability).
Secondary: **provenance-complete longitudinal data** with genuine portability (trust earns retention rather than lock-in trapping it).
Tertiary: **physician network effects** — doctors who trust the export become the distribution channel.

## 25.10 Recommended AI architecture
```
Client (AG-UI events) → Agent graph (LangGraph-class, interrupts for clinician review)
  ├── Typed clinical memory (FHIR resources, pertinent negatives as first-class)
  ├── Tools: fhir-query · kb-search · literature-search · wearables · file-read
  │          analysis · history-search · memory · (NO marketplace tool)
  ├── Unified provenance layer — every claim carries a resolvable source
  ├── Safety kernel — red-flag detection · abstention policy · critical-value escalation
  ├── Model router — frontier for reasoning, distilled small models for routine
  └── Eval harness — clinician gold sets · regression gates · published metrics
```

## 25.11 Recommended integrations
**Priority 1:** Quest + Labcorp; Apple HealthKit; Google Health Connect; Vital (transitional); Stripe; Medplum.
**Priority 2:** TEFCA/QHIN participation; Carequality; C-CDA import/export; imaging networks; Knock; Cal.com.
**Priority 3:** employer HRIS + 834; genomics; CGM; pharmacy (only with an evidence-gated formulary).

## 25.12 Recommended pricing
| Tier | Price | Contents |
|---|---|---|
| **Core** | $249/yr | 2 draws, ~60 direct-measured analytes, AI + citations, protocol, data hub, export |
| **Plus** | $599/yr | + quarterly micro-panels, named clinician, priority human SLA, advanced panels |
| **Family** | $749/yr | 2 adults + dependents, household view, per-member consent |
| **Employer** | $150–200/seat | Volume, 834/HRIS, aggregate de-identified reporting (opt-in), outcome options |
| **Clinician view** | **Free** | Distribution investment, not a revenue line |

## 25.13 Recommended roadmap
**Q1–Q2:** MVP as scoped above. **Q3:** iOS, insight feed, employer pilots, SOC 2 Type I. **Q4:** clinician portal + C-CDA/FHIR export, published validation study v1, SOC 2 Type II. **Y2 H1:** TEFCA, digital twin v1 (with uncertainty), Android, open API beta. **Y2 H2:** outcome contracts, international pilot, simulation twin, evidence-gated therapeutics if and only if clinical governance is mature.

---

# DELIVERABLE 26 — MASTER FEATURE INVENTORY
📊 **Delivered as `Ovexis_Superpower_Intelligence_Workbook.xlsx`, Sheet 1** — 55 features across all 20 requested columns (Feature · Purpose · Evidence · User Value · Business Value · Eng/Clinical/Infra/Regulatory Complexity · Estimated Team · Estimated Months · Priority · Category · Copy · Improve · Ignore · Reinvent · Moat · Confidence).

# DELIVERABLE 27 — EVIDENCE REGISTER
📊 **Delivered as Sheet 2** — 80 numbered claims, each with source artifact, method of observation, observed-vs-inferred classification, and confidence label.

*On "Screenshot" as an evidence column:* this investigation captured **raw source artifacts** — HTTP headers, JS bundle strings, sitemap XML, page text, court docket entries — rather than images. Source text is materially stronger evidence than a screenshot: it is verbatim, timestamped, and independently re-verifiable by any reader running the same public request. Every artifact cited is preserved in `/home/user/ovexis_ci/evidence/` for audit.

---

# SWOT

| **STRENGTHS** | **WEAKNESSES** |
|---|---|
| Genuinely advanced AI architecture — FHIR citations, agent graph, structured memory, transparent reasoning | No published clinical validation of any kind |
| FHIR-native clinical core (rare in consumer health) | Commerce conflict embedded in the clinical agent |
| Price leadership at $199 with strong value perception | Documented support failures at the moment of member anxiety |
| Exceptional brand, design and cultural fluency | Litigation exposure and marketing-credibility damage |
| 6,186-page compounding SEO asset | No clinician-facing product; no interoperability outward |
| Full vertical stack — labs to Rx in one app | Membership unit economics likely negative without attach |
| Fast execution: two acquisitions, AI Doctor in ~140k LOC | Retest paywall throttles their own data moat |
| Strong investor and celebrity network | US-only; no SOC 2; no developer surface |

| **OPPORTUNITIES** | **THREATS** |
|---|---|
| Employer/benefits channel (lower CAC, recurring) | Function Health's 6x capital advantage |
| GLP-1 and therapeutics ARPU expansion | Regulatory action on peptides, advertising, or SaMD classification |
| International expansion (entirely uncontested) | A single publicized clinical harm event |
| Clinician channel (currently unbuilt) | Wearable majors adding blood/clinical layers |
| Insurance/employer reimbursement for validated prevention | Apple/Google commoditizing aggregation |
| Digital twin as genuine simulation | Panel commoditization to <$99 |
| Consolidation as acquirer or target | CAC inflation as creator channels saturate |

---

# PORTER'S FIVE FORCES

**Threat of new entrants — HIGH.** Labs are outsourced, FHIR platforms are off-the-shelf, agent frameworks are open source, wearable aggregation is a vendor. Superpower's own stack demonstrates a competent team can assemble this in 12–18 months. The only real barriers are brand and accumulated data.

**Bargaining power of suppliers — MEDIUM-HIGH.** Quest is near-essential and shared with the primary competitor. Frontier model providers set inference costs and can restrict medical use. Vital, Medplum, Stripe and Shopify are each replaceable but individually load-bearing.

**Bargaining power of buyers — HIGH.** Zero switching cost at signup, annual renewal decision points, price transparency across competitors, and a category conditioned to discount. Employers as buyers will demand outcomes data that nobody currently publishes.

**Threat of substitutes — HIGH.** A free ChatGPT conversation, a $30 Labcorp direct panel, an annual physical, a wearable app, or simply doing nothing all substitute at various points on the value curve. **"Doing nothing" is the most underestimated competitor in preventive health.**

**Competitive rivalry — VERY HIGH AND INTENSIFYING.** Function at $2.5B, Neko at $1B+, dozens of funded entrants, price compression toward $99, and now open litigation between the two leaders. This is a land-grab phase with irrational customer-acquisition spending.

**Net:** structurally unattractive on classical analysis. **The only defensible position is one that raises buyer switching costs through genuine trust rather than lock-in, and that creates a supplier-independent data asset.** That is the strategy this report recommends for Ovexis.

---

# VALUE CHAIN

| Stage | Superpower | Margin | Ovexis position |
|---|---|---|---|
| Demand generation | SEO, creators, PR, employers | High leverage | Match SEO; add clinician channel |
| Conversion | Quiz → consent → payment | High | Slower consent, higher trust |
| Specimen collection | Quest PSCs + mobile phlebotomy | **Negative** (COGS) | Multi-lab to reduce concentration |
| Lab analysis | Quest (outsourced) | **Negative** (COGS) | Same — never own labs early |
| Data normalization | LOINC-style + FHIR core | **Value creation** | **Own this completely** |
| Interpretation | Scores + AI agent | **Core value** | Own + validate + publish |
| Care delivery | Care team + consults | Cost center | Differentiator if SLA-backed |
| Action fulfillment | Supplements, Rx, scans | **High margin** | Keep separate from interpretation |
| Retention | Insights, retests, wearables | Compounding | Bundle draws; event-driven care |

**The strategic insight:** value concentrates in **normalization and interpretation** — the two stages Superpower does well and where margin is genuinely created. Collection and analysis are commodity COGS. Fulfillment is high-margin but corrupts interpretation if integrated. **Ovexis should own normalization and interpretation absolutely, outsource collection and analysis, and hold fulfillment at arm's length.**

---

# PRODUCT ARCHITECTURE DIAGRAM

```
╔════════════════════════════════════════════════════════════════════════════╗
║  SUPERPOWER — RECONSTRUCTED SYSTEM ARCHITECTURE                            ║
║  🟢 = directly observed   🟡 = strong inference   🔴 = unknown             ║
╚════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────┐        ┌──────────────────────────────────────┐
│  MARKETING              │        │  MEMBER APP                          │
│  Webflow 🟢             │        │  React + Vite on Vercel 🟢           │
│  Cloudflare→CloudFront🟢│        │  TanStack Router (46 routes) 🟢      │
│  Intellimize 🟢         │        │  Radix + Tailwind + Framer + Rive 🟢 │
│  GTM (scoped) 🟢        │        │  TanStack Query + Zustand 🟢         │
│  Klaviyo · Segment 🟢   │        │  Sentry · PostHog 🟢                 │
│  6,186 SEO pages 🟢     │        │  iOS app (ID 6747997159) 🟢          │
└───────────┬─────────────┘        └──────────────────┬───────────────────┘
            │                                          │
            └──────────────┬───────────────────────────┘
                           ▼
        ┌──────────────────────────────────────────────────┐
        │  AUTH — better-auth 🟢                           │
        │  magic link · email OTP · phone · password ·     │
        │  organizations (B2B) · impersonation             │
        └──────────────────────┬───────────────────────────┘
                               ▼
        ┌──────────────────────────────────────────────────┐
        │  API GATEWAY — Node/Express on AWS 🟢            │
        │  CSP default-src 'none' · HSTS preload · DENY 🟢 │
        └──────────────────────┬───────────────────────────┘
                               │
   ┌───────────┬───────────┬───┴────────┬───────────┬─────────────┐
   ▼           ▼           ▼            ▼           ▼             ▼
┌────────┐┌─────────┐┌──────────┐┌───────────┐┌──────────┐┌────────────┐
│ CHAT   ││PROTOCOL ││PHLEBOTOMY││  SCANS    ││ RX       ││ MARKETPLACE│
│chatv4🟢││ v2 🟢   ││ redraw 🟢││ orders 🟢 ││contracts🟢││ Shopify 🟢 │
│chatv3🟢││ legacy🟢││ service- ││ centers   ││ subs     ││ multipass  │
│organs  ││ actions ││ ability  ││ prescreen ││ tasks    ││ 239 SKUs   │
│wearable││ goals   ││ appts    ││ handoff   ││screen-out││ credits    │
└───┬────┘└────┬────┘└────┬─────┘└─────┬─────┘└────┬─────┘└─────┬──────┘
    │          │          │            │           │            │
    ▼          └──────────┴────────────┴───────────┴────────────┘
┌────────────────────────┐                    │
│ AI AGENT LAYER         │                    ▼
│ AG-UI + LangGraph 🟢   │      ┌──────────────────────────────────┐
│ 16 tools 🟢            │◀────▶│  FHIR CLINICAL CORE              │
│ compressed memory 🟢   │      │  Medplum SDK 🟢                  │
│ FHIR citations 🟢      │      │  Observation · Patient ·         │
│ thinking/reasoning 🟢  │      │  DiagnosticReport · Communication│
│ multi-provider 🟡      │      │  Encounter · Goal · Questionnaire│
└────────────────────────┘      │  CDS Hooks 🟢 · Subs R4 🟢       │
                                └──────────────┬───────────────────┘
                                               │
        ┌──────────┬──────────┬────────────────┼──────────┬──────────┐
        ▼          ▼          ▼                ▼          ▼          ▼
   ┌────────┐┌─────────┐┌──────────┐    ┌──────────┐┌────────┐┌─────────┐
   │ Quest  ││ Vital 🟢││ Files/   │    │ Stripe 🟢││Knock 🟢││Cal.com🟢│
   │ labs 🟢││wearables││ ingest 🟢│    │ Klarna 🟢││notifs  ││ consults│
   └────────┘└─────────┘└──────────┘    └──────────┘└────────┘└─────────┘

   ✗ NO OUTBOUND: no EHR write-back · no TEFCA/HIE · no public API
```

---

# AI ARCHITECTURE DIAGRAM
*(See Deliverable 9.8 for the detailed version — reproduced conceptually here)*

```
MEMBER MESSAGE
     │
     ▼
┌─────────────────────────────────────────────────────────────┐
│ AG-UI EVENT STREAM  🟢                                      │
│ RUN_STARTED → STEP_* → TOOL_CALL_* → THINKING_* →           │
│ REASONING_* → TEXT_MESSAGE_* → ACTIVITY_DELTA → RUN_FINISHED│
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ LANGGRAPH AGENT  🟢  nodes · interrupts · predicted state    │
└──┬─────────────┬─────────────┬─────────────┬────────────────┘
   ▼             ▼             ▼             ▼
┌────────┐  ┌─────────┐  ┌──────────┐  ┌──────────────┐
│MEMORY  │  │RETRIEVAL│  │ CLINICAL │  │  COMMERCE    │
│compact │  │kb-search│  │fhir-query│  │marketplace-  │
│save    │  │web-searc│  │record-rea│  │query  ⚠️     │
│read    │  │web-fetch│  │wearables │  │              │
│history │  │file-read│  │analysis  │  │ ⚠️ CONFLICT: │
│        │  │         │  │skill-read│  │ same agent   │
│        │  │         │  │          │  │ reasons +    │
│        │  │         │  │          │  │ sells        │
└────────┘  └─────────┘  └──────────┘  └──────────────┘
   │             │             │             │
   └─────────────┴──────┬──────┴─────────────┘
                        ▼
        ┌───────────────────────────────────┐
        │ CITATION RESOLVER  🟢             │
        │ fhir://observation/{uuid} →       │
        │ {biomarker, value, unit, date}    │
        └───────────────┬───────────────────┘
                        ▼
        ┌───────────────────────────────────┐
        │ RENDERED RESPONSE                 │
        │ inline citations · Think tab ·    │
        │ activity ticker · followups       │
        └───────────────────────────────────┘

   ✗ ABSENT: eval harness · confidence scores · abstention policy ·
             published clinical validation · human-review metrics
```

---

# BUSINESS MODEL CANVAS
📊 **Delivered as workbook Sheet 6** — all nine blocks with evidence-based Superpower analysis and Ovexis differentiation recommendations side by side.

# RISK REGISTER
📊 **Delivered as workbook Sheet 4** — 24 risks with category, evidence, likelihood, impact, severity and Ovexis counter-position.

# DECISION LEDGER
See Deliverable 17 (abridged) and workbook Sheet 1 (per-feature, 55 rows).

# FEATURE DEPENDENCY GRAPH
See Deliverable 18.

# ENGINEERING ROADMAP RECONSTRUCTION
See Deliverable 19.

# FOUNDER PSYCHOLOGY REPORT
See Deliverable 3.

# STRATEGIC RECOMMENDATIONS
See Deliverable 23 (attack plan) and Deliverable 25 (Ovexis memo).

---

# THE FIVE THINGS THAT MATTER
### If the board reads nothing else

**1. Superpower's AI architecture is genuinely good and you should copy the grounding layer today.**
FHIR-native citations (`fhir://observation/{uuid}`) resolving to specific lab observations, typed agent tooling, transparent reasoning, and structured memory put them roughly 12–18 months ahead of typical consumer health AI. This is real engineering, not marketing. Copy it. Then beat it with typed clinical memory instead of lossy prose compaction.

**2. They have no clinical validation, and that is the opening.**
Across 304 JavaScript chunks, every public page, and all press: no eval harness, no published accuracy data, no peer-reviewed validation of the Superpower Score or biological age, no confidence intervals, no human-review statistics. An independent reviewer got biological ages of 45.2, 37.3 and 38.0 from three vendors within months. A cardiologist found all ten of his "abnormal" flags clinically meaningless. **The category has no evidence standard. Ovexis can define it — and a validation study costs a rounding error against Function's $298M.**

**3. Commerce sits inside the clinical reasoning agent, and that is structural, not fixable.**
The same LangGraph agent that queries your FHIR observations has a `marketplace-query` tool. Their unit economics require it — at $199 with ~$50–90 lab COGS, membership alone likely does not clear CAC. **They cannot remove the conflict without breaking the business model.** Ovexis can be architecturally conflict-free and market that as the difference. This is the single most defensible wedge in the entire report.

**4. Litigation is forcing the whole category toward honest measurement — arrive there first.**
*Function v. Superpower* (2:26-cv-00810) turns on whether a calculated ratio is a "biomarker." Superpower's own sitemap publishes Castelli Index, atherogenic index and CRP:albumin ratios in the same namespace as measured analytes. They have already softened their language and dropped "3,000+" to "2,000+" locations. **Adopt the strict definition now, publish your methodology, and let your competitors be dragged to your position by a court.**

**5. Their moat is thinner than their valuation implies — and their retention loop is self-sabotaging.**
Everything they have built is replicable in 12–24 months. Their two real assets are accumulated longitudinal data and brand. They throttle the first with a retest paywall (members must pay again to see proof of progress) and are spending down the second through litigation, support failures and peptide-culture reporting. **Include two draws in your base membership, guarantee a human support SLA, and you neutralize both of their advantages while fixing the two things members complain about most.**

---

# REFERENCES

## Primary artifacts (retrieved 25 July 2026 — preserved in `/evidence/`)
- `https://superpower.com/` — homepage, headers, HTML
- `https://superpower.com/robots.txt` · `/sitemap.xml` and four child sitemaps (6,186 URLs)
- `https://superpower.com/` pages: `/why`, `/roadmap`, `/organizations`, `/peptides`, `/reviews`, `/studies`, `/legal/privacy`, `/legal/terms`, `/biomarker-testing-companies/superpower-vs-function-health`
- `https://app.superpower.com/` — HTML shell + **304 public JS chunks (~11 MB)** including `parse-fhir-citation`, `digital-twin`, `use-wearable-connect`, `assistant-chat`, `sources`, `use-insight-feed`, `superpower-score-dialog`, all `_app.*` route modules and all `api-*` modules
- `https://api.superpower.com/` — response headers and 404 behavior on standard discovery paths
- DNS and TLS certificate inspection for `superpower.com`, `app.superpower.com`, `api.superpower.com`

## Legal
- *Function Health, Inc. v. Superpower Health Inc. et al*, No. 2:26-cv-00810 (C.D. Cal., filed 26 Jan 2026) — docket via Justia; Law.com Radar

## Press and analysis
TechCrunch (22 Apr 2025) · Forbes (22 Apr 2025) · Fierce Healthcare (23 Apr 2025) · Business Insider (30 May 2025; Mar 2026) · BusinessWire (21 May 2024; Giannis announcement) · Longevity.Technology (May 2024) · Athletech News (5 Feb 2026) · ArentFox Schiff *Longevity Lens* / Mondaq (Mar 2026) · Capital Brief (17 Feb 2026) · SmartCompany (17 Feb 2026) · Fitt Insider (Feb 2026) · Anadolu Agency / Türkiye Today (22 Feb 2026 — AI Doctor launch) · Sourcery VC · Sacra · Startup Daily · Unicorner

## Customer evidence
Trustpilot (superpower.com reviews) · HealNourishGrow independent review (Jul 2026) · The Skeptical Cardiologist (May 2026) · TheresAnAIForThat (Feb 2026)

## Company-published
Ashby job listing "Engineering @ Superpower" (tech stack, investors, strategy sequence, growth claims) · Glassdoor / ZipRecruiter / BuiltIn role listings · TheOrg org chart

## Market data
PitchBook · CB Insights · Tracxn · PremierAlts *(note: these sources materially conflict on total funding and valuation; the discrepancy is flagged rather than resolved in §2.2)*

---

## METHODOLOGY, LIMITATIONS AND ETHICS

**What was done:** public-surface intelligence only — pages a browser loads, JavaScript a server voluntarily serves, sitemaps a site publishes, headers a server returns, dockets a court makes public, and listings a company posts.

**What was not done:** no account creation, no authentication attempt, no access to any member data or PHI, no rate-limit testing, no vulnerability probing, no scraping beyond ordinary page retrieval. `robots.txt` permits full crawling and was respected. Terms of Service were not circumvented.

**Principal limitations, stated plainly:**
- Server-side model providers, prompt content, database technology and inference costs are **not observable** and are marked 🔴 or 🟡 accordingly
- Financial metrics (revenue, members, CAC, LTV, retention, margins) are **not public**; the unit-economics model in §13.2 is explicitly labeled as an analytical estimate with 🔴 inputs
- SOC 2 status, BAAs and audit outcomes are **absent from public record** — absence of evidence is reported as such, not as evidence of absence
- The authenticated product experience was **not observed**; all product analysis derives from the public bundle, which reveals structure but not runtime behavior
- Litigation allegations are **untested in court**; Superpower had not filed its answer as of the last docket entry reviewed, and every allegation is labeled as such
- Regacore and PreventiveHealth.ai returned **no reliable public information** and are marked 🔴 rather than fabricated
- Funding totals **conflict across sources** and are presented as a range

**Every claim in this report is traceable to a labeled source. Nothing has been invented to fill a gap.**
