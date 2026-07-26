# DELIVERABLE 8 — HEALTHCARE DATA ARCHITECTURE
## FUNCTION HEALTH — DATA FLOW, STANDARDS, INTEGRATIONS, AND CONSENT ARCHITECTURE
*Evidence-based mapping of healthcare data architecture. Confirmed from API documentation, site terms, and user reports.*

---

## 8.1 DATA ARCHITECTURE OVERVIEW

### Confirmed Architecture 🟢

```
MEMBER DATA (Profile, Health History, Consent)
    ↓
FIREBASE AUTHENTICATION (JWT: idToken, refreshToken)
    ↓
GOOGLE CLOUD RUN (REST API v1: production-member-app-mid-lhuqotpy2a-ue.a.run.app)
    ↓
DATA STORAGE (Inferred: Firestore, Cloud SQL, BigQuery for biomarker results; Firebase Auth for identity)
    ↓
LAB INTEGRATION (Quest Diagnostics — CLIA-certified; results delivered in batches via requisitionId)
    ↓
IMAGING INTEGRATION (Ezra — FDA-cleared AI MRI/CT; results integrated into dashboard)
    ↓
SUPPLEMENT INTEGRATION (SuppCo — TrustScore, TESTED program, supplement database)
    ↓
WEARABLE / IoT (Mentioned in MI Lab vision; no confirmed integration documented)
    ↓
HEALTH RECORD UPLOAD (Secure vault; informs AI Chat and Protocols)
    ↓
AI PROCESSING (LLM inference over biomarker + health record + clinical guideline data)
    ↓
CLINICIAN REVIEW (Human review of out-of-range biomarkers and AI protocols)
    ↓
MEMBER DELIVERY (Web dashboard; email notifications; potential SMS — marketing consent required)
```

---

## 8.2 DATA STANDARDS & FORMATS

### Confirmed 🟢

**FHIR (Fast Healthcare Interoperability Resources):**
- **Status:** Not confirmed implemented
- **Evidence:** No FHIR endpoints documented; API uses custom REST structure (`/results-report`, `/biomarkers`, `/user`); no FHIR resource types (Patient, Observation, DiagnosticReport) observed
- **Inference:** Function Health does not currently support FHIR; health record uploads are likely unstructured (PDF, image) rather than structured FHIR data
- **Implication:** Limited interoperability with EHR systems; no standard clinical data exchange

**HL7 (Health Level Seven):**
- **Status:** Not confirmed
- **Evidence:** Lab results delivered through Quest's internal systems; no HL7 message format mentioned; API returns custom JSON structures
- **Inference:** Function receives results from Quest through Quest's internal APIs or file transfers, not through standard HL7 v2 messages

**CCDA / CCD (Consolidated Clinical Document Architecture / Continuity of Care Document):**
- **Status:** Not confirmed
- **Evidence:** Health record uploads described as "past lab test results, visit notes, etc." — implies unstructured document upload rather than structured CCDA

---

## 8.3 DATA INTEGRATIONS

### Confirmed 🟢

**Apple Health:**
- **Status:** Not confirmed implemented
- **Evidence:** No Apple Health integration mentioned in site or API; MI Lab mentions wearables but no specific Apple Health connection
- **Inference:** Potential future integration; not current

**Google Health Connect:**
- **Status:** Not confirmed implemented
- **Evidence:** Same as Apple Health — mentioned in vision but not implemented

**Wearables:**
- **Status:** Mentioned in MI Lab vision only
- **Evidence:** "Unifying data from lab testing, imaging, wearables, IoT devices, and medical records"
- **Inference:** Not currently integrated; strategic priority for future

**Lab Data (Quest Diagnostics):**
- **Status:** Confirmed — primary lab partner
- **Evidence:** 2,000+ Quest locations; `questBiomarkerCode` in biomarker metadata; CLIA-certified
- **Data Flow:** Quest processes blood samples; results delivered to Function via internal API/file transfer; Function stores results with `requisitionId` grouping; clinician reviews; member notified

**Medical Imaging (Ezra / Smart Scan):**
- **Status:** Confirmed — acquired and integrated
- **Evidence:** Full-body MRI ($499, 22 min, FDA-cleared AI); CT scans; available at 100+ US locations
- **Data Flow:** Ezra AI processes MRI/CT scans; results integrated into Function dashboard; likely stored as structured reports and images

**Supplement Intelligence (SuppCo):**
- **Status:** Confirmed — acquired May 2026
- **Evidence:** TrustScore ratings; ISO 17025 TESTED program; 35,000+ products; 500,000+ supplement routines
- **Data Flow:** Supplement database integrated with biomarker recommendations; member recommendations include supplement suggestions with verification ratings

---

## 8.4 DATA NORMALIZATION & DEDUPLICATION

### Confirmed / Inferred 🟢 / 🟡

**Biomarker Normalization:**
- **Standard Reference Ranges:** Quest reference ranges (`questRefRangeLow` / `questRefRangeHigh`) — standardized by Quest for clinical use
- **Function Optimal Ranges:** Function's tighter optimal ranges (`optimalRangeLow` / `optimalRangeHigh`) — customized by Function's clinical team
- **Sex-Specific Ranges:** `sexDetails` array includes `Male`, `Female`, `All` — allows gender-appropriate range comparison
- **Unit Standardization:** Units defined per biomarker (e.g., ng/mL, mg/dL, U/L) — consistent within biomarker definition

**Data Deduplication:**
- **Requisition ID Grouping:** All visits for one test round share same `requisitionId` — prevents duplicate test tracking
- **Visit Date Grouping:** `dateOfService` tracks individual visit dates within requisition
- **Previous Results:** `currentResult` represents latest result; historical results implied but not documented in API response
- **Health Record Upload:** Member-uploaded past results likely stored separately; deduplication method not confirmed

---

## 8.5 PATIENT IDENTITY & LONGITUDINAL RECORDS

### Confirmed 🟢

**Patient Identity:**
- **Firebase Authentication:** JWT tokens (`idToken`, `refreshToken`) linked to `localId` (Firebase user ID)
- **Profile:** `/user` endpoint returns `id` (UUID), `patientIdentifier` (e.g., "P001"), name, DOB, biological sex, contact info
- **Membership:** `patientMembership`: "annual" — confirms subscription model tracking

**Longitudinal Tracking:**
- **Requisition-Based:** `requisitionId` groups all visits for one annual/mid-year test round
- **Biomarker History:** `currentResult` contains `dateOfService`; previous results implied but not explicitly returned in documented endpoint
- **Biological Age:** Calculated over time (`biologicalAge` vs `chronologicalAge`) — requires historical biomarker patterns
- **Change Detection:** Open-source MCP project includes `diffMeta()`, `detectAndSaveChanges()`, notification persistence — Function's internal system almost certainly tracks changes

---

## 8.6 CONSENT ARCHITECTURE

### Confirmed 🟢

**Consent Forms Required Before Signup:**
1. **Privacy Policy** — data use and protection
2. **Terms of Service** — service terms, liability, cancellation
3. **Request for Lab Results** — authorization for Function to receive lab results from Quest
4. **Authorization for Use of Medical Information** — HIPAA authorization for clinical review and AI processing

**Marketing Consent:**
- **SMS/Text Consent:** Separate checkbox for marketing messages; not required for service use
- **Automatic Texting System:** Confirmed consent mechanism

**Inferred Consent Management:** 🟡
- **No granular consent options observed:** Members consent to all data uses (clinical review, AI processing, marketing) as a bundle; no option to opt out of AI processing while maintaining clinical review, or vice versa
- **No data deletion process documented:** HIPAA requires data retention; no evidence of member-initiated data deletion
- **No third-party data sharing consent:** Health record uploads, supplement recommendations, and wearable integration (future) would require additional consent

---

*Sources: API documentation (github.com/daveremy/function-health-mcp); Site terms and signup form; Press releases; User reviews.*
