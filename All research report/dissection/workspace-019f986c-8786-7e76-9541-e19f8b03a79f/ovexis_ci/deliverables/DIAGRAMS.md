# HEALTHIFY — ARCHITECTURE & FLOW DIAGRAMS
### Companion to the Master CI Report · 25 July 2026

Legend: 🟢 Confirmed · 🟡 Strong Inference · 🔴 Speculation · ❌ Absent (verified gap)

---

# 1. PRODUCT ARCHITECTURE DIAGRAM

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                        CLIENT LAYER                                          ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  📱 Android (com.healthifyme.basic) 🟢    📱 iOS 🟢                          ║
║  🌐 Web app (/accounts/login, /achievements, /socialq) 🟡  [de-emphasised]   ║
║  🖥️  Marketing: /us/ /in/ (static S3+CloudFront) 🟢                          ║
║  🛒 store.healthifyme.com — Shopify 🟢                                       ║
║  💊 rx.healthify.com — Cloudflare/Webflow-class, separate stack 🟢           ║
╚═══════════════════════════════╤══════════════════════════════════════════════╝
                                │
╔═══════════════════════════════▼══════════════════════════════════════════════╗
║                        EDGE / CDN LAYER 🟢                                    ║
║   Akamai (www, api) ·  CloudFront (cdn, static) · Cloudflare (rx)            ║
║   HSTS · X-Frame-Options: DENY · CSP report-only ⚠️ · nosniff                ║
╚═══════════════════════════════╤══════════════════════════════════════════════╝
                                │
╔═══════════════════════════════▼══════════════════════════════════════════════╗
║                     APPLICATION LAYER — Django/Python 🟢                      ║
║              (evidence: csrftoken, {% include %} leak, Django 404s)          ║
║  ┌────────────────────────────────────────────────────────────────────────┐  ║
║  │  api.healthifyme.com  — private first-party API (❌ no public API)      │  ║
║  └────────────────────────────────────────────────────────────────────────┘  ║
║  Services (from public TLS SAN enumeration 🟢):                              ║
║   • gpt-app        → LLM application service                                 ║
║   • audioforge     → voice/Whisper pipeline  [→ "Ria Voice Call coming soon"]║
║   • recipe         → recipe service                                          ║
║   • payment        → payment orchestration (PayU 🟢 via /payu_callback)      ║
║   • events         → event ingestion                                         ║
║   • gym            → gym/studio service                                      ║
║   • stream.berry   → live class streaming (HealthifyStudio)                  ║
║   • anomalisa      → anomaly detection                                       ║
║   • apps / apps2   → internal consoles (coach/ops) 🟡                        ║
║   • mis / insights / insights-public / analytics / datahealth → BI & data    ║
║   • sglink / acctsglinks / engagesglinks / internalsglinks → deep links      ║
║  Async: Celery + Flower 🟢  |  Broker: Redis/RabbitMQ 🟡                     ║
╚════════╤═══════════════════════════════════════════════════╤═════════════════╝
         │                                                   │
╔════════▼════════════════════════╗          ╔═══════════════▼══════════════════╗
║   AI LAYER 🟢 (OpenAI)          ║          ║   DATA LAYER 🟡                  ║
║  • GPT-4 Vision   → Snap        ║          ║  • RDBMS (Postgres/MySQL) 🟡     ║
║  • GPT-4 Turbo /                ║          ║  • Cache (Redis) 🟡              ║
║    GPT-3.5 (fine-tuned) → Ria   ║          ║  • Warehouse 🟡                  ║
║  • Whisper       → Copilot      ║          ║  • Object storage (S3) 🟢        ║
║  • Embeddings    → food match   ║          ║  • Food catalogue + embeddings 🟢║
║  + proprietary ensemble models  ║          ║  • Longitudinal behaviour logs 🟢║
║  + custom heuristic models      ║          ║  ❌ No FHIR store                ║
║  ⚠️ SINGLE VENDOR, NO FALLBACK  ║          ║  ❌ No clinical record           ║
╚═════════════════════════════════╝          ╚══════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                     INFRASTRUCTURE & OPS 🟢                                   ║
║  AWS ap-southeast-1 (Singapore) — primary                                    ║
║  Environments: PROD · alpha · beta · gamma · theta  (x123healthifyme.com)     ║
║  Monitoring: Grafana · Celery Flower · datahealth · anomalisa · Cyfe          ║
║  Analytics: GTM · internal events pipeline · Trackier (affiliate)             ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                     EXTERNAL INTEGRATIONS                                     ║
║  INBOUND 🟢:  Apple Health · Google Fit · Health Connect · Samsung Health     ║
║               Garmin · Fitbit · Abbott FreeStyle Libre Pro (NFC, LOCKED ⚠️)   ║
║               Smart Scale (BLE)                                               ║
║  COMMERCE 🟢: Shopify · PayU · Apple IAP · Google Play Billing · Amazon.in    ║
║  PARTNERS 🟢: Swiggy (order) · Tata 1mg (drugs+labs) · Novo Nordisk (PAP)     ║
║  OUTBOUND:    ❌ NONE.  No API · No SDK · No webhooks · No FHIR · No export   ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

# 2. AI ARCHITECTURE DIAGRAM

```
                          ┌───────────────────────────┐
                          │      USER INPUT           │
                          └─────────────┬─────────────┘
        ┌───────────────────────────────┼───────────────────────────────┐
        │                               │                               │
   ┌────▼──────┐                 ┌──────▼──────┐                 ┌──────▼──────┐
   │  PHOTO    │                 │    TEXT     │                 │   VOICE     │
   │  (Snap /  │                 │  (Ria chat) │                 │ (log / Ria) │
   │ Auto Snap)│                 └──────┬──────┘                 └──────┬──────┘
   └────┬──────┘                        │                               │
        │                               │                        ┌──────▼──────┐
        │                               │                        │  WHISPER 🟢 │
        │                               │                        └──────┬──────┘
        │                               │                               │
┌───────▼───────────────┐               └───────────────┬───────────────┘
│  GPT-4 VISION 🟢      │                               │
│  multi-item detection │                    ┌──────────▼───────────────────────┐
└───────┬───────────────┘                    │   CONTEXT ASSEMBLY 🟡            │
        │                                    │  • user profile & goals          │
┌───────▼───────────────┐                    │  • recent food/activity/sleep/   │
│ PROPRIETARY ENSEMBLE🟢│                    │    glucose/weight logs 🟢        │
│ (Indian-cuisine spec., │                   │  • conversation memory (200+     │
│  portion priors)      │                    │    msg threads 🟢)               │
└───────┬───────────────┘                    │  • RAG over Healthify literature🟢│
        │                                    └──────────┬───────────────────────┘
┌───────▼───────────────────────────────┐               │
│  EMBEDDINGS + COSINE SIMILARITY 🟢    │    ┌──────────▼───────────────────────┐
│  GPT food name  ⇄  Healthify catalogue│    │  FINE-TUNED ENSEMBLE 🟢          │
│  ← THE KEY ENTITY-RESOLUTION JOIN     │    │  GPT-4 Turbo + GPT-3.5           │
└───────┬───────────────────────────────┘    └──────────┬───────────────────────┘
        │                                               │
┌───────▼───────────────────────────────┐               │
│  CUSTOM HEURISTIC MODELS 🟢           │               │
│  user-preference priors, portions     │               │
└───────┬───────────────────────────────┘               │
        │                                               │
┌───────▼───────────┐                        ┌──────────▼───────────────────────┐
│ NUTRITION VALUES  │                        │  RIA RESPONSE                    │
│ + HEALTH SCORE 🟢 │                        │  • cross-domain temporal queries🟢│
│ ❌ no confidence   │                        │  • meal plans, recipes, lists    │
│    shown to user  │                        │  • proactive insights            │
└───────┬───────────┘                        └──────────┬───────────────────────┘
        │                                               │
        └────────────────────┬──────────────────────────┘
                             │
              ┌──────────────▼───────────────┐
              │  ⚠️ SAFETY / GUARDRAIL LAYER │
              │  🔴 NO PUBLIC EVIDENCE       │
              │  ❌ no published policy       │
              │  ❌ no ED safeguards          │
              │  ❌ no drug-interaction check │
              │  ❌ no escalation protocol    │
              │  ❌ no confidence gating      │
              │  Only: blanket ToU disclaimer│
              └──────────────┬───────────────┘
                             │
        ┌────────────────────┴────────────────────┐
        │                                         │
┌───────▼─────────────┐                 ┌─────────▼──────────────┐
│  DIRECT TO USER 🟢  │                 │  COACH COPILOT 🟢      │
│  (no human review)  │                 │  drafts → HUMAN COACH  │
│  Ria = ~50% of subs │                 │  REVIEWS → sends       │
│  handled AI-only    │                 │  300 clients/coach ⚠️  │
└─────────────────────┘                 └────────────────────────┘

  EVALUATION 🔴  no public evals · no benchmarks · no model cards · no calibration
  STATED NEXT 🟢 "autonomous health agents... order food or book gym classes"
```

---

# 3. HEALTHCARE DATA FLOW DIAGRAM

```
 SOURCES                    INGESTION            PROCESSING           CONSUMPTION
 ═══════                    ═════════            ══════════           ═══════════

 📷 Meal photo ────────┐
 🖼️ Photo gallery ─────┤    ⚠️ full gallery
    (Auto Snap)        │       permission
 🗣️ Voice ─────────────┤
 ⌨️ Manual/search ─────┼──► Snap pipeline ──► GPT-4V ──► embeddings
                       │                                  join 🟢
 ⌚ Apple Health ──────┤
 ⌚ Google Fit ────────┤                                    │
 ⌚ Health Connect ────┼──► Wearable sync ─────────────────┤
 ⌚ Samsung Health ────┤    (OAuth/HealthKit)              │
 ⌚ Garmin, Fitbit ────┘                                   │
                                                           ▼
 🩸 Abbott Libre Pro ──────► NFC ──► ⚠️ HEALTHIFY-ONLY ──►┌──────────────────┐
    (CGM)                            (won't work with     │  BEHAVIOURAL     │
                                      Abbott's own app)   │  LONGITUDINAL    │──► 📊 Daily /
 ⚖️ Smart Scale ───────────► BLE ────────────────────────►│  STORE 🟢        │    Weekly
                                                          │                  │    reports
 💬 Coach chat ────────────────────────────────────────► │  • food logs     │
 💬 Ria chat ──────────────────────────────────────────► │  • activity      │──► 🤖 Ria
 📞 Call audio ──────────► Whisper 🟢 ──────────────────► │  • sleep         │    insights
                                                          │  • glucose       │
 📝 Onboarding ────────────────────────────────────────► │  • weight/body   │──► 👤 Coach
    (goals, conditions)                                   │  • conversations │    (300:1)
                                                          │  • purchases     │
 💊 HealthifyRx intake ───────────────────────────────►  │                  │──► 🩺 Doctor
    (labs, Rx, doses,                                     │  ❌ NOT FHIR      │    (Rx only)
     side effects) 🟢                                     │  ❌ NOT coded     │
                                                          │  ❌ NO lab        │──► 📄 One-way
 🛒 Shopify / PayU ────────────────────────────────────► │     ingestion     │    "lifestyle
                                                          └──────────────────┘     report" to
                                                                   │                partner MD
                                                                   │
                                            ┌──────────────────────▼──────────┐
                                            │  🌐 CROSS-BORDER PROCESSING     │
                                            │  AWS ap-southeast-1 (Singapore) │
                                            │  → OpenAI API (US) 🟡           │
                                            │  ⚠️ OpenAI not named in the      │
                                            │     privacy policy               │
                                            └─────────────────────────────────┘

 ══════════════════ WHAT NEVER ENTERS THE SYSTEM ══════════════════
   ❌ Lab results (structured)    ❌ EHR / clinical records
   ❌ FHIR / HL7 / C-CDA          ❌ Diagnoses, ICD-10, SNOMED
   ❌ External medications        ❌ Claims / insurance
   ❌ Imaging (DICOM)             ❌ Genomics
   ❌ Allergies, family history   ❌ Immunisations
   ❌ Apple Health RECORDS (clinical FHIR — only fitness is synced)

 ══════════════════ WHAT NEVER LEAVES THE SYSTEM ══════════════════
   ❌ No data export       ❌ No API       ❌ No FHIR out
   ❌ No EHR write-back    ❌ No portability
```

---

# 4. USER JOURNEY DIAGRAM

```
 ANONYMOUS VISITOR
   │ Google: "calories in roti" / "PCOS diet" → 1 of ~10–15k blog/recipe URLs 🟢
   │ Play Store search 🟢 · PR · Swiggy/1mg co-marketing
   ▼
 GEO-ROUTING 🟢  (HTTP 302 from / )
   ├──► /us/  "AI Meets Human Expertise" · "$25/mo FREE!" · Apple Health · Dietitian · CGM
   └──► /in/  "HealthifyRx: Medical Weight Loss That Lasts" · Snap · Ria
   ▼
 MARKETING / CONSIDERATION
   Trust: "40 Million+ Users" · testimonials with kg · "Healthify x OpenAI" · Stanford
   ▼
 APP INSTALL  →  SIGNUP (/launchSignUp) 🟢   [18+ required 🟢]
   ▼
 ONBOARDING QUIZ 🟡
   goal · weight · target · height · age · sex · activity · diet preference
   (veg/non-veg/vegan) · conditions (thyroid/PCOS/diabetes) · meal timings
   ▼
 ★ ACTIVATION MOMENT: personalised calorie + macro budget revealed
   ▼
 CONSENT 🟢  bundled ToU+Privacy · cookie banner (ACCEPT-ONLY ⚠️)
   ❌ no granular per-purpose consent   ❌ no AI-training opt-out
   ▼
 PERMISSIONS 🟡
   Camera · ⚠️ FULL PHOTO LIBRARY (Auto Snap) · Notifications · HealthKit/Health Connect
   · Bluetooth (scale) · NFC (CGM) · Microphone
   ▼
 DATA IMPORT — wearables, CGM, scale, gallery
   ▼
 FREE LOGGING (habit formation, days 1–7)
   Snap → 2× tracking vs manual 🟢
   ▼
 ╔══════════════ RETENTION LOOPS (running continuously) ══════════════╗
 ║ L1 Logging habit: cue→snap(2s)→calories+score+Ria comment          ║
 ║ L2 Auto Snap: zero-effort passive logging                          ║
 ║ L3 Proactive insight: Ria notification from data already held      ║
 ║ L4 Accountability: coach check-in  ⚠️ FAILING (see complaints)     ║
 ║ L5 Biometric curiosity: CGM spike alerts, 14-day repurchase        ║
 ║ L6 Medical dependency: Rx weekly dose + 5-phase protocol           ║
 ║ L7 Gamification: streaks, challenges, achievements, community      ║
 ╚════════════════════════════════════════════════════════════════════╝
   ▼
 PAYWALL TRIGGER — locked macros / locked Snap depth / locked Ria
   ▼
 /pricing  ⇄  /pricing/v2   ← LIVE A/B TEST 🟢
   ▼
 /pick-plan 🟢
   ▼
 PAYMENT — PayU 🟢 / Apple IAP / Google Play / Shopify / Amazon / EMI
   ▼
 ⚠️ OUTBOUND SALES CALL  → close  → ⚠️ "sales person stopped picking my calls" 🟢
   ▼
 COACH ASSIGNMENT (⚠️ default coach; only 1 switch allowed 🟢)
   ▼
 ONGOING SERVICE
   ├─ ✅ works: Snap, Ria, food DB, tracking
   └─ ⚠️ fails: coach absent · generic plans · no portion editing · support scripted
   ▼
 SUPPORT ── in-app chat · support@ · 1800-419-9501
   ⚠️ MouthShut 1.48/5 (n=1,148) · "the chat is a scam" · "please refresh"
   ▼
 RENEWAL ── auto-renew · ⚠️ 3–6 month minimums · ⚠️ Rx 45-day refund cut-off
   │
   ├──► CHURN → public negative review → higher CAC ↺ (the death spiral)
   │
   └──► RETAINED → upsell: CGM (₹4,499) → Rx (₹48k–1L) → renewal
   ▼
 REFERRAL 🟡 weak — coupon sites, community sharing; ❌ no formal programme
```

---

# 5. FEATURE DEPENDENCY GRAPH

```
                        ┌─────────────────────────┐
                        │       CONSENT           │  🟢 bundled, coarse
                        │  ToU + Privacy + cookie │  ❌ not granular
                        └───────────┬─────────────┘
                                    │
                        ┌───────────▼─────────────┐
                        │       IDENTITY          │  🟡 email/phone + SSO
                        │  ❌ no MPI  ❌ no IAL2   │  🔴 MFA unverified
                        │  ❌ no MFA evidence      │  18+ gate 🟢
                        └───────────┬─────────────┘
                                    │
        ┌───────────────────────────┼──────────────────────────────┐
        │                           │                              │
┌───────▼────────┐         ┌────────▼─────────┐          ┌─────────▼─────────┐
│ DEVICE PERMS   │         │  ACCOUNT PROFILE │          │  ENTITLEMENT      │
│ camera 🟢      │         │  goals, prefs,   │          │  free / smart /   │
│ ⚠️ FULL GALLERY│         │  conditions 🟡   │          │  coach / CGM / Rx │
│ NFC 🟢 BLE 🟢  │         └────────┬─────────┘          └─────────┬─────────┘
│ HealthKit 🟢   │                  │                              │
└───────┬────────┘                  │                              │
        │                           │                              │
        └───────────┬───────────────┴──────────────────────────────┘
                    │
        ┌───────────▼──────────────────────────────────────────┐
        │              DATA COLLECTION 🟢                      │
        │  Snap · Auto Snap · voice · search · wearables ·     │
        │  CGM · scale · chat · Rx intake                      │
        └───────────┬──────────────────────────────────────────┘
                    │
        ┌───────────▼──────────────────────────────────────────┐
        │           NORMALISATION 🟢                           │
        │  ★ CRITICAL PATH: GPT-4V food names                  │
        │       ⇄ Embeddings cosine similarity                 │
        │       ⇄ Healthify food catalogue                     │
        │  ⚠️ SINGLE POINT OF FAILURE for all nutrition value  │
        └───────────┬──────────────────────────────────────────┘
                    │
        ┌───────────▼──────────────────────────────────────────┐
        │                 AI LAYER 🟢                          │
        │  Ria (GPT-4T/3.5 FT + RAG)  ·  Snap heuristics ·     │
        │  Coach Copilot (Whisper)                             │
        │  ⚠️ HARD DEPENDENCY: OpenAI (no fallback evidenced)  │
        └───────────┬──────────────────────────────────────────┘
                    │
        ┌───────────▼──────────────────────────────────────────┐
        │        REPORTS (daily / weekly) 🟢                   │
        └───────────┬──────────────────────────────────────────┘
                    │
        ┌───────────▼──────────────────────────────────────────┐
        │        INSIGHTS (proactive push) 🟢                  │
        └─────┬──────────────────┬───────────────────┬─────────┘
              │                  │                   │
      ┌───────▼──────┐   ┌───────▼────────┐  ┌───────▼─────────────┐
      │    USER      │   │     COACH      │  │      DOCTOR         │
      │ retention    │   │  Copilot-      │  │  ⚠️ one-way PDF     │
      │ loop closes  │   │  assisted      │  │     "lifestyle      │
      │ here 🟢      │   │  ⚠️ 300:1      │  │      report" only   │
      └──────────────┘   └────────────────┘  │  ❌ no EHR write-back│
                                             │  ❌ no FHIR          │
                                             │  ❌ NO CLOSED LOOP   │
                                             └─────────────────────┘

╔════════════════════ SINGLE POINTS OF FAILURE ════════════════════╗
║ SPOF-1  OpenAI API        → Snap + Ria + Copilot all degrade     ║
║ SPOF-2  Food catalogue join → all nutrition value collapses      ║
║ SPOF-3  Gallery permission → Auto Snap dies on OS policy change  ║
║ SPOF-4  Coach supply       → premium tier credibility collapses  ║
║ SPOF-5  Abbott             → sole CGM supplier                   ║
║ SPOF-6  Tata 1mg           → sole Rx fulfilment channel          ║
╚══════════════════════════════════════════════════════════════════╝
```

---

# 6. OVEXIS TARGET ARCHITECTURE (for contrast)

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  CAPTURE (free forever)                                                      ║
║  photo (on-device pre-filter) · voice · wearables · CGM (ANY vendor) ·       ║
║  scale/DEXA/BIA · labs · EHR (patient-mediated FHIR) · meds · symptoms       ║
╚═══════════════════════════════╤══════════════════════════════════════════════╝
                                ▼
╔══════════════════════════════════════════════════════════════════════════════╗
║  FHIR R4 CANONICAL STORE  +  terminology (LOINC/SNOMED/RxNorm/UCUM)          ║
║  provenance · confidence · consent scope on EVERY datum                      ║
╚═══════════════════════════════╤══════════════════════════════════════════════╝
                                ▼
╔══════════════════════════════════════════════════════════════════════════════╗
║  THE MEMBER MODEL — structured longitudinal timeline + derived features      ║
║  + DIGITAL TWIN (personal response models with uncertainty)                  ║
╚═══════════════════════════════╤══════════════════════════════════════════════╝
                                ▼
╔══════════════════════════════════════════════════════════════════════════════╗
║  REASONING — MODEL ROUTER (multi-vendor + open-weight fallback)              ║
║  RAG over GRADED CLINICAL EVIDENCE · deterministic calculators · tool use    ║
╚═══════════════════════════════╤══════════════════════════════════════════════╝
                                ▼
╔══════════════════════════════════════════════════════════════════════════════╗
║  SAFETY & GOVERNANCE  ★ the layer Healthify lacks                            ║
║  ED safeguards · hypo/hyper escalation · drug interactions · pregnancy ·     ║
║  self-harm pathway · scope enforcement · confidence gating · full audit log  ║
╚═══════════════════════════════╤══════════════════════════════════════════════╝
                                ▼
╔══════════════════════════════════════════════════════════════════════════════╗
║  DELIVERY                                                                    ║
║  Member app · Care team console (1:60) · Clinician portal (SMART on FHIR,    ║
║  bidirectional) · Employer dashboard · PUBLIC API + SDKs + webhooks          ║
╚═══════════════════════════════╤══════════════════════════════════════════════╝
                                ▼
╔══════════════════════════════════════════════════════════════════════════════╗
║  OWNERSHIP — one-click FHIR+CSV+PDF export · consent ledger with receipts ·  ║
║  verifiable deletion · continuous sync to user-controlled storage            ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

# 7. BUSINESS MODEL CANVAS — HEALTHIFY

```
┌──────────────────┬──────────────────┬──────────────────┬──────────────────┬──────────────────┐
│ KEY PARTNERS     │ KEY ACTIVITIES   │ VALUE            │ CUSTOMER         │ CUSTOMER         │
│                  │                  │ PROPOSITIONS     │ RELATIONSHIPS    │ SEGMENTS         │
├──────────────────┼──────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ OpenAI 🟢        │ AI/ML dev 🟢     │ "Where AI Meets  │ AI coach 24/7 🟢 │ Free trackers 🟢 │
│ Abbott (CGM) 🟢  │ Food DB curation │  Human Expertise"│ Human coach      │ AI-only subs     │
│ Tata 1mg 🟢      │  🟢              │                  │  (300:1) ⚠️      │  (~50%) 🟢       │
│ Novo Nordisk 🟢  │ Coach network    │ • Effortless     │ Community 🟡     │ Coach subs 🟢    │
│ Swiggy 🟢        │  ops 🟢          │   logging (Snap) │ ⚠️ Support: 1.48 │ CGM users 🟢     │
│ Apple/Google 🟢  │ Content/SEO 🟢   │ • 24/7 AI coach  │    /5 MouthShut  │ Rx patients      │
│ Amazon 🟢        │ Rx clinical ops  │ • Cultural fit   │ ⚠️ Outbound      │  (BMI≥30/27+) 🟢 │
│ Manipal/Medanta/ │  🟢              │   (Indian food,  │    telesales     │ US consumers 🟢  │
│  Apollo (legacy) │ Device commerce  │   11 languages)  │ ⚠️ 3–6mo minimums│ Corporates:      │
│  🟢              │  🟢              │ • ₹208/mo        │                  │  Amazon,         │
│ Shopify/PayU 🟢  │                  │ • Doctor-led GLP1│                  │  Accenture,      │
│ NIN (food data)🟢│                  │                  │                  │  Micro Labs 🟢   │
│                  ├──────────────────┤                  ├──────────────────┤                  │
│                  │ KEY RESOURCES    │                  │ CHANNELS         │ NOT customers:   │
│                  ├──────────────────┤                  ├──────────────────┤ <18 · clinically │
│                  │ Indian food DB 🟢│                  │ SEO ~10–15k URLs │ complex · devs · │
│                  │ 10yr behaviour   │                  │  🟢              │ US enterprise    │
│                  │  data (1B+ meals)│                  │ App stores 🟢    │ (no BAA) ·       │
│                  │  🟢              │                  │ Founder PR 🟢    │ genomics users   │
│                  │ 600+ coaches 🟢  │                  │ Swiggy/1mg/Novo🟢│                  │
│                  │ Brand (India) 🟢 │                  │ Amazon 🟢        │                  │
│                  │ Django/AWS 🟢    │                  │ Corporates 🟢    │                  │
│                  │ ❌ No API/FHIR   │                  │ ⚠️ Coupon sites  │                  │
├──────────────────┴──────────────────┴──────────────────┴──────────────────┴──────────────────┤
│ COST STRUCTURE                              │ REVENUE STREAMS                                 │
├─────────────────────────────────────────────┼─────────────────────────────────────────────────┤
│ Coach salaries (largest variable) 🟡        │ FY25 TOTAL: ₹178 Cr (−14%) 🟢                   │
│ OpenAI inference (scales w/ engagement!) 🟡 │  • Domestic coaching  ₹99 Cr (−23.2%) 🟢        │
│ Drug COGS on Rx (margin killer) 🟡          │  • Devices            ₹18.6 Cr (+11%) 🟢        │
│ Engineering ~120–200 🟡                     │  • Exports            ₹60 Cr (flat) 🟢          │
│ Ads: ₹13 Cr FY25 (was ₹73.5 Cr, −82%) 🟢    │  • HealthifyRx ₹48k–1L per programme 🟢         │
│ TOTAL EXPENSES ₹182.6 Cr (−38%) 🟢          │  • US ARR ~$2M 🟢                               │
│ Cost to earn ₹1 = ₹1.03 (was ₹1.43) 🟢      │ LOSS: ₹4.7 Cr (−96%) 🟢                         │
└─────────────────────────────────────────────┴─────────────────────────────────────────────────┘
```
