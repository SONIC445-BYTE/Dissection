# DELIVERABLE 4 — PRODUCT REVERSE ENGINEERING
## FUNCTION HEALTH — EVERY FEATURE, WORKFLOW, BUTTON, PAGE, AND HIDDEN FLOW
*Evidence-based reverse engineering. Confirmed via direct site observation, API documentation, user reviews, and press releases.*

---

## 4.1 PUBLIC-FACING WEBSITE ARCHITECTURE

### Confirmed Page Structure 🟢

| URL / Path | Purpose | Key Elements | Evidence |
|------------|---------|--------------|----------|
| `/` (Homepage) | Acquisition, value prop, trust signals | Hero: "Check your health"; 160+ tests; $365/year; award badges; celebrity endorsements; scientific advisory board photos; FAQ; site search | Direct observation |
| `/how-it-works` | Workflow explanation, conversion | 4 steps: Personalize & Test → Get Insights → Take Action → Monitor for Life; comparison table (Standard vs Function); concierge draw info; advanced add-ons (MRI, CT, Gut, Extended Panels) | Direct observation |
| `/what-we-test` | Biomarker inventory, transparency | 18 categories with biomarker lists; included markers marked; add-ons marked; icons; descriptions; link to individual biomarker pages | Direct observation |
| `/lab-locations` | Scheduling access, location finder | 2,000+ Quest/Getlabs locations; map illustration; state-level scheduling | Direct observation |
| `/faq` | Objection handling, conversion support | Detailed answers on frequency, results explanation, biomarker changes, insurance, action plans | Direct observation |
| `/journal` | Content marketing, SEO, trust | Articles on health topics; news announcements; scientific updates | Direct observation |
| `/article/function-announcement` | Press release (Nov 19, 2025) | MI Lab launch; $365 price reduction; leadership announcements | Direct observation |
| `/article/smart-scan-x-function` | Partnership announcement | MRI access expansion (Wisconsin) | Direct observation |
| `/article/function-acquires-suppco` | Acquisition announcement | Supplement intelligence integration | Direct observation |

---

## 4.2 SIGNUP & ONBOARDING FLOW (CONFIRMED FROM DIRECT OBSERVATION)

### Step 1: Marketing Entry Point 🟢
- User lands on homepage via organic search, social media, influencer referral, or paid advertising
- Hero message: "Every year. Starting with 160+ lab tests detecting 1000+ conditions. Just $365 per year—$1 per day."
- Primary CTA: "Start testing" → links to `https://my.functionhealth.com/signup`

### Step 2: Signup Form (my.functionhealth.com/signup) 🟢
**Form Fields (Confirmed):**
- Email
- Legal name ("Your name must match the ID you present at each lab visit")
- Phone number
- Consent checkbox for automatic texting system (marketing messages)
- Date of birth (MM/DD/YYYY)
- Biological sex (Female / Male)
- State selection ("Where will you be testing?")
- Access code (optional — "Don't have a code?")

**Consent Requirements (Confirmed):**
- Privacy Policy agreement
- Terms of Service agreement
- Request for Lab Results agreement
- Authorization for Use of Medical Information agreement

**Inferred Flow 🟡:**
- Form validation: Email format, name matching, valid date format, state selection required
- Access code likely used for referral tracking, corporate partnerships, or promotional pricing
- No immediate payment collected at signup — likely requires scheduling first visit or completing onboarding

### Step 3: Health History / Personalization 🟡
From homepage description: "Share your health history so we can tailor insights to you, then book your first test."
- Not directly observed in signup flow, but confirmed in "How It Works" description
- Likely includes: medical history, family history, current symptoms, supplements, medications, lifestyle factors
- This data feeds into clinician review and personalized protocol generation

### Step 4: Scheduling 🟢
- User selects date/time at 2,000+ Quest/Getlabs locations
- System generates requisition / lab order
- Confirmed issues: Scheduling errors (system refuses valid dates); changes must be made through Quest directly (does not sync back to Function); manual customer service often required
- Concierge blood draw option available in select areas (schedule 2-hour window; specialist visits location; results ~2 weeks)

---

## 4.3 LAB TESTING WORKFLOW (CONFIRMED FROM API DOCUMENTATION + USER REVIEWS)

### Confirmed Technical Flow 🟢

```
MEMBER SIGNUP → HEALTH HISTORY → SCHEDULE VISIT → LAB DRAW (1-3 VISITS OVER 2-4 WEEKS) → QUEST PROCESSES → RESULTS BATCHED (2 WEEKS) → CLINICIAN REVIEW → AI PROTOCOL GENERATION → MEMBER NOTIFIED → MEMBER VIEWS RESULTS → ACTION PROTOCOL → RETEST IN 3-6 MONTHS (MID-YEAR: 60+ BIOMARKERS)
```

### Detailed Visit Model 🟢
- **Annual Test:** ~100+ biomarkers; requires 1-3 lab visits over 2-4 weeks; all visits share `requisitionId`
- **Mid-Year Test:** ~60+ biomarkers; 1-3 visits; 3-6 months after initial
- **On-Demand Testing:** Any biomarker can be retested anytime for additional cost (member-only pricing)
- **Results Batch Delivery:** Results arrive as batches (e.g., Visit 1: 68 results; Visit 2: 45 results; total: 113) rather than single comprehensive report

### Confirmed User Experience Issues 🟢
- **No pending status indicator:** User must manually compare website list of paid tests against populated results
- **No new vs. viewed indicator:** Results appear without distinguishing new results from previously viewed ones
- **Batch timing:** "Months" mentioned by some users; 2 weeks mentioned in concierge description; actual time may vary by biomarker type
- **Scheduling limitations:** System only allows scheduling initial appointment; rescheduling requires Quest direct contact + manual Function support ticket

---

## 4.4 RESULTS & DASHBOARD FEATURES (REVERSE-ENGINEERED FROM API + USER REPORTS)

### Confirmed Data Endpoints 🟢

From reverse-engineered API (`https://production-member-app-mid-lhuqotpy2a-ue.a.run.app/api/v1`):

| Endpoint | Method | Purpose | Response Structure |
|----------|--------|---------|-------------------|
| `/user` | GET | Profile, membership status, scheduling eligibility | Profile with `patientMembership`: "annual" |
| `/biomarkers` | GET | Full biomarker definitions (names, codes, ranges) | Array of biomarker objects with `questBiomarkerCode`, categories, sex details, optimal/reference ranges |
| `/categories` | GET | Biomarker categories with nested biomarkers | Category objects with full biomarker arrays |
| `/results-report` | GET | Structured report with biomarker results | `biomarkerResultsRecord` array — each with biomarker metadata, `currentResult` (date, value, inRange, requisitionId), `outOfRangeType`, units, ranges |
| `/recommendations` | GET | Personalized health recommendations | Array: `id`, `category` (Nutrition, etc.), `title`, `description` |
| `/biological-calculations/biological-age` | GET | Biological age calculation | `biologicalAge`, `chronologicalAge` |
| `/biological-calculations/bmi` | GET | BMI data | `bmi`, `weight`, `height` |
| `/notes` | GET | Clinician notes | Array: `id`, `content`, `createdAt` |
| `/requisitions?pending=true` | GET | Pending (in-progress) test rounds | Array: `id`, `status`, `dateOfService` |
| `/requisitions?pending=false` | GET | Completed test rounds | Used for change detection |
| `/pending-schedules` | GET | Upcoming scheduled visits | Array: `id`, `scheduledDate` |

---

## 4.5 RESULTS VISUALIZATION (INFERRED FROM USER DESCRIPTIONS + API DATA)

### Confirmed / Strong Inference 🟢 / 🟡

**Biomarker Result Card:**
- Biomarker name (e.g., "Vitamin D, 25-OH")
- Description / why it matters
- Current result value (`displayResult` / `calculatedResult`)
- Units (e.g., ng/mL, mg/dL)
- Status indicator (`inRange`: true/false)
- Out of range type (`HIGH`, `LOW`, or empty)
- Function Health optimal range (`optimalRange`: "40-80")
- Quest reference range (`rangeString`: "30-100")
- Date of service (`dateOfService`)
- Requisition ID (groups visits)

**User Complaints Confirming Visualization Issues 🟢:**
- No indicator for new vs. previously viewed results
- No pending status for unpaid/unprocessed tests
- Format is "focused for someone with little to no medical background" — ignores practitioner-level data formatting
- Function blocks access to Quest website results for members (Quest has better formatting options)

---

## 4.6 AI INTERACTION FEATURES (CONFIRMED FROM PRESS RELEASE + API)

### Confirmed AI Capabilities 🟢

**Private AI Chat (Launched Nov 2025):**
- Context-aware responses informed by member's health data
- Can explain biomarker results, answer health questions, provide actionable insights
- Likely uses a large language model (provider not disclosed) with RAG architecture over biomarker data, clinician notes, recommendations, and uploaded health records
- User feedback: "These are great analyses, but you could pull any blood test report into AI and get the same thing" — suggests AI chat is not uniquely personalized beyond standard LLM capabilities

**Protocols (Launched Nov 2025):**
- Translates complex health data into easy-to-understand steps
- Likely personalized based on biomarker out-of-range markers, health history, and recommendations endpoint
- Format: Actionable steps (nutrition, supplements, lifestyle) rather than clinical prescriptions

**Upload Health Records (Launched Nov 2025):**
- Secure vault for past lab test results, visit notes, etc.
- Data informs Private AI Chat and Protocols
- Confirms data portability and integration vision

---

## 4.7 ADVANCED ADD-ON FEATURES (CONFIRMED)

### Confirmed 🟢

| Add-On | Description | Price / Access | Evidence |
|--------|-------------|---------------|----------|
| **Advanced MRI & CT** | Full-body MRI (22 min, FDA-cleared AI, detects 50+ cancer types, aneurysms, fatty liver, spinal issues, body composition); CT scans (lung cancer, heart plaque) | $499 (MRI); member-only pricing for CT | Homepage, Ezra acquisition news |
| **Concierge Blood Draws** | Certified specialist comes to home/office; schedule 2-hour window; results ~2 weeks | Member-only; available in select areas | Homepage |
| **Extended Panels** | More biomarkers across heart, nutrients, heavy metals | Member-only pricing | Homepage |
| **Gut Testing** | Coming soon | Not available | Homepage |
| **Galleri Multi-Cancer Test** | Blood-based multi-cancer early detection (GRAIL technology) | Add-on | What We Test page |
| **Alzheimer's Detection / Brain Testing** | Brain health markers; MRI with skeletal/neurological assessment; brain injury screening | Add-on | What We Test page |
| **Mold Reactivity Testing** | Chronic Inflammatory Response (Mold Response) | Add-on | What We Test page |
| **Genetic Testing** | Genetic Heart Risks; MTHFR Gene | Add-on | What We Test page |

---

## 4.8 CLINICAL REVIEW WORKFLOW (INFERRED FROM API + USER FEEDBACK)

### Confirmed Elements 🟢
- Every result reviewed by clinician
- Clinician notes (`/notes` endpoint) created for members
- Personalized action plan generated
- Flags for out-of-range biomarkers (`outOfRangeType`: HIGH/LOW)

### Confirmed Issues 🟢
- **AI-generated feel:** Users describe notes as "so AI generated it’s offensive"; "nothing personal or bespoke"; "feels like it should come with a crappy 90s robot voice"
- **Incorrect range interpretation:** User reports magnesium (4 mg/dL) marked as "barely average" by Function but actually "extremely high" by standard references (1.8-2.6 mg/dL) — suggests either range errors or miscommunication
- **No specialist referral:** If biomarkers indicate serious conditions (e.g., high ANA titer), Function does not provide direct specialist referrals; user must seek their own care

---

## 4.9 SECURITY & PRIVACY FEATURES (CONFIRMED FROM TERMS + API)

### Confirmed 🟢
- **HIPAA-compliant** (stated on homepage)
- **Firebase Authentication** (Google Identity Platform) — JWT tokens (`idToken`, `refreshToken`)
- **Authorization headers** required for all API requests
- **Consent architecture:** Multiple consent forms required before signup (Privacy Policy, Terms, Lab Results Release, Medical Information Authorization)
- **No evidence of 2FA / MFA** mentioned in API documentation
- **No evidence of encryption details** (at-rest, in-transit) beyond standard Firebase/Cloud Run defaults

---

## 4.10 RETENTION & GROWTH LOOPS (INFERRED)

### Confirmed Retention Mechanisms 🟢
1. **Biannual Testing:** Annual + mid-year visits create natural retention points
2. **Results Batch Delivery:** Multiple visits over 2-4 weeks create multiple touchpoints; members return to check each batch
3. **Protocol Updates:** Personalized recommendations may update as new results arrive
4. **AI Chat Access:** Private AI chat provides ongoing engagement beyond test results
5. **Upload Health Records:** Members who upload records have invested data in the platform

### Confirmed Growth / Conversion Loops 🟢
1. **Influencer Marketing:** Mark Hyman's audience; celebrity endorsements; social media presence
2. **Award Badges:** TIME, Fast Company, Oprah, LinkedIn — trust signals for conversion
3. **Celebrity Investors:** Matt Damon, Magic Johnson, etc. — social proof
4. **Scarcity / Urgency:** Price reduction messaging; limited-time pricing (original $499 → $365)
5. **Referral Program Potential:** Access code field in signup suggests referral tracking; no explicit referral program documented
6. **NBPA Partnership:** B2B2C distribution to NBA players; potential employer/corporate expansion

---

## 4.11 HIDDEN WORKFLOWS & UNDOCUMENTED FEATURES

### Inferred from API + User Reports 🟡
- **Change Detection System:** The open-source MCP project includes change detection features (`diffExports`, `detectAndSaveChanges`, `MetaChanges`) — Function's internal system likely tracks biomarker changes over time and may notify members of significant changes
- **Notification System:** API includes `/notifications` or similar logic (inferred from open-source notification persistence in `~/.function-health/changes/`)
- **Export / Download:** Users mention downloading results for sharing; no confirmed download endpoint documented
- **Data Migration:** Open-source project includes migration logic for version updates (`v0.3` → `v0.4`) — Function likely maintains data compatibility across platform updates
- **State-Level Restrictions:** `canScheduleInBetaStates` flag in user profile suggests some states may have restricted scheduling capabilities (likely NY/NJ regulatory limitations)

---

*Sources: Direct site observation (homepage, signup, how-it-works, what-we-test, FAQ, journal, press releases); Reverse-engineered API docs (github.com/daveremy/function-health-mcp); User reviews (Reddit r/Function_Health); Job listings; News coverage (Fierce Healthcare, HIT Consultant, Practical Patient Care, Nutraceuticals World).*
