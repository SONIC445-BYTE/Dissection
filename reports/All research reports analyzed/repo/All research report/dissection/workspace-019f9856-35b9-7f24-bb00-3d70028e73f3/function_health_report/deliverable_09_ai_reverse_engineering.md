# DELIVERABLE 9 — AI REVERSE ENGINEERING
## FUNCTION HEALTH — MEDICAL INTELLIGENCE LAB & AI ARCHITECTURE
*Evidence-based inference of LLM usage, agent architecture, memory, RAG, safety, and clinical validation. All speculative elements clearly labeled.*

---

## 9.1 CONFIRMED AI FEATURES

### Confirmed from Press Release (Nov 19, 2025) 🟢

**Medical Intelligence Lab (MI Lab):**
- **Co-Directors:** Daniel K. Sodickson, MD, PhD (Chief Medical Scientist) + clinical/research team
- **Mission:** "Leverage AI to develop Medical Intelligence — a system designed to achieve the deepest view of each person's unique biology by unifying data from lab testing, imaging, wearables, IoT devices, and medical records, integrating it with global medical research and the expertise of leading clinicians."
- **Key Statement:** "Not AI replacing doctors; it's clinical expertise amplified by intelligent systems that never stop learning."

**Three New AI Capabilities:**
1. **Private AI Chat:** Context-aware responses informed by health data; provides explanations and actionable insights
2. **Protocols:** Translates complex health data into easy-to-understand steps members can practice immediately
3. **Upload Health Records:** Past lab results, visit notes uploaded to secure vault; informs AI Chat and Protocols

---

## 9.2 INFERRED AI ARCHITECTURE (BASED ON EVIDENCE)

### Confirmed Technical Foundation 🟢
- **Authentication:** Firebase Authentication (Google Identity Platform) — standard JWT flow
- **Backend:** Google Cloud Run (REST API v1)
- **Frontend:** Web application (`my.functionhealth.com`)
- **Data Storage:** Not explicitly documented; likely Firestore (Firebase ecosystem), Cloud SQL, or BigQuery for biomarker results
- **API Structure:** REST (not GraphQL); no official SDK; reverse-engineered endpoints

### Strong Inference — AI System Design 🟡

**LLM Provider (Unknown — Speculative):**
- **Likely candidates:** OpenAI (GPT-4/5), Anthropic (Claude), Google (Gemini), or a fine-tuned medical LLM
- **Evidence:** No model provider disclosed; no mention of "OpenAI" or "Anthropic" in documentation; "Private AI Chat" implies proprietary or white-labeled model
- **Inference:** Given the clinical sensitivity and need for control, Function may use either (a) a major LLM with strict prompt engineering and RAG, or (b) a fine-tuned model on medical literature and biomarker data
- **Confidence:** 🔴 Speculation (no direct evidence)

**Agent Architecture (Strong Inference):**
- **Hiring signal:** "Staff AI Engineer, Agentic Systems" (Austin, $171K-$257K) confirms multi-agent architecture
- **Inferred structure:**
  - **Health Data Agent:** Extracts and structures biomarker results, imaging reports, health records
  - **Interpretation Agent:** Applies clinical guidelines, optimal ranges, and research to explain biomarkers
  - **Recommendation Agent:** Generates personalized protocols based on out-of-range markers, health history, and evidence-based interventions
  - **Monitoring Agent:** Tracks longitudinal changes, detects trends, flags significant changes
  - **Safety/Guardrail Agent:** Ensures recommendations stay within safe, evidence-based boundaries; flags when specialist referral is needed
- **Orchestration:** Likely a central orchestrator (possibly using LangChain, LlamaIndex, or custom framework) that routes queries to appropriate agents
- **Memory:** Longitudinal biomarker data (`requisitionId`, `dateOfService`) provides persistent memory; health record uploads extend memory beyond Function's own testing

**RAG (Retrieval-Augmented Generation):**
- **Evidence:** AI Chat is informed by "health data" — implies RAG over biomarker results (`/results-report`), recommendations (`/recommendations`), clinician notes (`/notes`), and uploaded health records
- **Knowledge base:** Likely includes peer-reviewed medical literature, clinical guidelines, biomarker reference ranges, and Function's internal clinical protocols
- **Confidence:** 🟡 Strong Inference

**Context Management:**
- **Confirmed context sources:** User profile (`/user`), biomarker results (`/results-report`), recommendations (`/recommendations`), clinician notes (`/notes`), health record uploads, biological calculations, pending schedules
- **Inferred context window:** Given biomarker result complexity (160+ markers with descriptions, ranges, units, out-of-range status), the context window must accommodate thousands of tokens per user query
- **Potential challenge:** Biomarker explanation requires referencing both Function's optimal ranges and Quest reference ranges, plus clinical context, requiring precise retrieval and accurate citation

---

## 9.3 MEMORY & LONGITUDINAL TRACKING

### Confirmed 🟢
- **Biomarker history:** Stored via `requisitionId` grouping; previous results preserved; new results added for retesting
- **Biological Age:** Calculated over time (`biologicalAge` vs `chronologicalAge`) — requires historical biomarker patterns
- **BMI:** Tracked historically
- **Recommendations:** Updated as new results arrive
- **Notes:** Clinician notes accumulate (`createdAt` timestamps)

### Strong Inference 🟡
- **Memory architecture:** Likely uses a structured database (SQL/NoSQL) for biomarker results plus a vector database (e.g., Pinecone, Weaviate, or custom) for semantic retrieval of health records, notes, and recommendations
- **Change detection:** The open-source MCP project includes `diffMeta()`, `detectAndSaveChanges()`, and notification persistence — Function's internal system almost certainly includes similar change tracking to alert members of significant biomarker shifts
- **Digital Twin:** Not confirmed. The MI Lab vision implies a continuously updated health model ("continuously learning model of your health"), which is conceptually a digital twin, but no explicit digital twin feature is documented

---

## 9.4 REASONING & EVALUATION

### Confirmed Elements 🟢
- **Range comparison:** Each biomarker result compares `calculatedResult` against `optimalRange` (Function) and `questRefRange` (Quest standard)
- **Status determination:** `inRange` boolean based on optimal range; `outOfRangeType` indicates HIGH or LOW
- **Category grouping:** Biomarkers organized into 18 categories for logical reasoning
- **Clinical review:** Every result reviewed by clinician before member notification

### Inferred Reasoning Pipeline 🟡

```
BIOMARKER RESULT → RANGE COMPARISON → OUT-OF-RANGE DETECTION → CATEGORY CONTEXT → HEALTH HISTORY CONTEXT → RESEARCH INTEGRATION → PROTOCOL GENERATION → SAFETY CHECK → CLINICIAN REVIEW → MEMBER DELIVERY
```

**Reasoning Types:*
- **Rule-based:** If biomarker > optimal range, flag HIGH; if < optimal range, flag LOW; if within range, confirm healthy
- **Pattern-based:** Compare current result to previous results (longitudinal trend analysis); detect acceleration/deceleration
- **Correlational:** Identify relationships between biomarkers (e.g., insulin resistance + high triglycerides + low HDL; hormone imbalances + nutrient deficiencies)
- **Evidence-based:** Match biomarker patterns to published research (e.g., high hs-CRP + elevated Lp(a) = increased cardiovascular risk)
- **Personalized:** Adjust recommendations based on sex details (`Male`/`Female`/`All` ranges), biological sex, age, health history, and uploaded records

**Evaluation Metrics (Inferred) 🟡:**
- **Accuracy:** Alignment between AI explanations and clinician-reviewed notes (user complaints suggest gaps)
- **Safety:** Rate of incorrect range interpretations; rate of missed serious conditions; rate of inappropriate supplement recommendations
- **Engagement:** Usage of Private AI Chat; protocol adoption rates; retest scheduling rates
- **Clinical Outcomes:** Not publicly measured; no peer-reviewed studies published by Function Health

---

## 9.5 PROMPT ENGINEERING & GUARDRAILS

### Confirmed Safety Approach 🟢
- **Clinician review required:** "Clinicians review every result and flag issues"
- **No AI replacement of doctors:** Explicit messaging in all AI announcements
- **Personalized protocols, not prescriptions:** Action plans describe lifestyle/nutrition/supplement recommendations, not pharmaceutical prescriptions
- **Evidence-based approach:** References to "thousands of hours of research" in result explanations

### Inferred Guardrail System 🟡

**Safety Guardrails (Likely Implemented):**
- **Medical disclaimer requirement:** All AI responses likely include standard disclaimers ("This is not a substitute for professional medical advice")
- **Range validation:** AI must reference Function's optimal ranges and Quest reference ranges; incorrect range references must be caught before delivery
- **Supplement recommendation limits:** Post-SuppCo, recommendations must reference TrustScore ratings and TESTED program results; unsafe supplement combinations must be blocked
- **Specialist referral triggers:** High-risk biomarkers (e.g., extremely high cancer signals, severe hormone imbalances, abnormal imaging) should trigger referral recommendations rather than self-management protocols
- **Age/sex appropriateness:** Protocols must match biological sex and age (biomarker ranges vary by sex; pregnancy markers only relevant for certain users)

### Confirmed User Complaints (Safety/Quality Issues) 🟢
- **Incorrect magnesium interpretation:** Function marked 4 mg/dL as "barely average" when standard reference is 1.8-2.6 mg/dL (potential hypermagnesemia)
- **Generic AI notes:** "Nothing personal or bespoke"; feels like automated text generation
- **No specialist referral mechanism:** User with high ANA titer had no pathway to specialist care through Function
- **Aggressive upselling:** Continuous promotion of add-ons ($269 retest, $499 MRI, extended panels) may conflict with clinical priorities

---

## 9.6 HUMAN REVIEW & CLINICAL VALIDATION

### Confirmed 🟢
- **Every result reviewed by clinician** — stated on homepage and how-it-works
- **Clinician notes generated** — stored in `/notes` endpoint
- **Medical & Scientific Board:** Mark Hyman (CMO), JoAnn Manson (Harvard/Brigham), Andrew Huberman (Stanford), Toby Cosgrove (Cleveland Clinic), Daniel Sodickson (NYU), Azra Raza (Columbia), Eddie Chang (UCSF), Luis Diaz (MSKCC)
- **Chief Medical Scientist:** Daniel Sodickson directs MI Lab predictive modeling

### Strong Inference 🟡
- **Clinician workload:** With 50M+ lab tests completed (since 2023) and potentially hundreds of thousands of members, clinician review at scale requires either (a) a large clinical team, (b) AI-assisted review with clinician sign-off, or (c) selective review (only out-of-range biomarkers reviewed in detail)
- **Clinical validation gap:** No peer-reviewed studies, clinical trials, or outcome studies published by Function Health validating that 160 biomarkers improve health outcomes, that AI protocols improve biomarker values, or that the platform reduces disease incidence
- **FDA status:** Only Ezra AI imaging holds FDA clearance. Function's biomarker reporting, AI recommendations, and protocols are not FDA-approved or cleared as medical devices

---

## 9.7 MODEL PROVIDERS & INFERENCE ARCHITECTURE

### Confirmed / Speculative 🟢 / 🔴

| Component | Evidence | Inference | Confidence |
|-----------|----------|-----------|------------|
| **LLM Provider** | Not disclosed | Could be OpenAI, Anthropic, Google, or custom; given clinical sensitivity, likely a major provider with strict terms | 🔴 Speculation |
| **Inference Platform** | Google Cloud Run | Likely uses Google Cloud AI Platform, Vertex AI, or custom containerized inference | 🟡 Strong Inference |
| **Fine-Tuning** | Not mentioned | May fine-tune base model on biomarker literature, clinical guidelines, and Function's internal protocols; or use RAG without fine-tuning | 🔴 Speculation |
| **Model Size** | Not disclosed | Given context complexity (160 biomarkers, clinical notes, health records), likely uses a large model (70B+ parameters) or multiple specialized models | 🔴 Speculation |
| **Latency Requirements** | Not specified | Real-time AI chat requires sub-2-second response; batch recommendations can tolerate longer processing | 🟡 Strong Inference |
| **Cost Structure** | Not disclosed | LLM inference costs at scale (potentially 100K+ members) could be significant; likely a major cost center alongside lab partner fees | 🟡 Strong Inference |

---

## 9.8 CONFIDENCE ESTIMATION

### Confirmed Approach 🟢
- **Range-based confidence:** `inRange` boolean provides binary confidence; no probability scores documented
- **Clinical review:** Human clinician acts as confidence validator for out-of-range results
- **Evidence citations:** Protocol recommendations likely cite research; no specific citation format observed

### Inferred Confidence System 🟡
- **Biomarker-level confidence:** Low confidence for new/tested biomarkers; high confidence for well-established markers (cholesterol, glucose, vitamin D)
- **Recommendation-level confidence:** Higher confidence for lifestyle/nutrition recommendations; lower confidence for supplement recommendations where evidence is mixed
- **Trend confidence:** Higher confidence for consistent longitudinal changes vs. single-point anomalies
- **Safety confidence:** Low tolerance for clinical errors — any high-risk biomarker should trigger clinician escalation regardless of AI confidence

---

## 9.9 DATA FLOW — AI ARCHITECTURE DIAGRAM (INFERRED)

```
MEMBER INPUT (Health History Upload, Biomarker Results, Imaging, Wearables, Records)
    ↓
FIREBASE AUTHENTICATION (JWT Token Validation)
    ↓
DATA RETRIEVAL LAYER (REST API: /user, /results-report, /notes, /biomarkers, /categories)
    ↓
CONTEXT ASSEMBLY (Biomarker Values + Ranges + Health History + Previous Notes + Uploaded Records)
    ↓
RETRIEVAL AUGMENTED GENERATION (RAG over Clinical Guidelines, Biomarker References, Research Database)
    ↓
LLM INFERENCE (Private AI Chat / Protocol Generation / Recommendation Engine)
    ↓
AGENT ORCHESTRATION (Agentic System: Data Agent → Interpretation Agent → Recommendation Agent → Safety Agent)
    ↓
CLINICAL REVIEW GATE (Clinician validates out-of-range results, high-risk recommendations, protocol accuracy)
    ↓
SAFETY GUARDRAILS (Medical Disclaimer, Supplement Safety Check, Specialist Referral Triggers, Age/Sex Validation)
    ↓
OUTPUT DELIVERY (Results Report, Protocol Steps, AI Chat Response, Notification)
    ↓
LONGITUDINAL MEMORY (Results stored with requisitionId; Change Detection; Biological Age Update)
```

---

*Sources: Press Release (Nov 19, 2025) — https://www.functionhealth.com/article/function-announcement; Homepage AI feature descriptions; Reverse-Engineered API docs (github.com/daveremy/function-health-mcp); Job listings (Agentic Systems, Data Platform); User Reviews (AI note quality complaints).*
