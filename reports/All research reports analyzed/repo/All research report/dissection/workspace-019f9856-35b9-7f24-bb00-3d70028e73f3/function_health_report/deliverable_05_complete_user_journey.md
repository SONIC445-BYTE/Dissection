# DELIVERABLE 5 — COMPLETE USER JOURNEY
## FUNCTION HEALTH — EVERY SCREEN, STEP, AND INTERACTION FROM ANONYMOUS VISITOR TO RENEWAL
*Evidence-based. All steps observed or strongly inferred from direct site exploration, API documentation, and user reviews.*

---

## 5.1 JOURNEY MAP OVERVIEW

```
ANONYMOUS VISITOR → MARKETING TOUCHPOINT → SIGNUP FORM → HEALTH HISTORY → SCHEDULING → CONSENT → VERIFICATION → LAB VISIT → RESULTS BATCH 1 → RESULTS BATCH 2 → RESULTS COMPLETE → CLINICIAN REVIEW → AI PROTOCOL → AI CHAT → HEALTH RECORD UPLOAD → ACTION PROTOCOL → RETEST (MID-YEAR) → SUBSCRIPTION RENEWAL → REFERRAL / SOCIAL SHARING → SUPPORT / CHURN
```

---

## 5.2 DETAILED JOURNEY STAGES

### Stage 1: Anonymous Visitor (Pre-Conversion) 🟢

**Entry Points (Confirmed):**
- Organic search ("preventive health testing," "biomarker testing," "longevity medicine")
- Social media (Instagram/TikTok via influencer referrals)
- Podcast mentions (Huberman, Hyman)
- Celebrity endorsements (social proof through celebrity investors)
- Paid advertising (likely Meta, Google, podcast ads)

**Homepage Experience (Direct Observation):**
- Hero: Large image/video; headline "Check your health"; subheadline "Every year. Starting with 160+ lab tests detecting 1000+ conditions. Just $365 per year—$1 per day."
- Trust signals: HSA/FSA eligible badge; award badges (TIME 100, Fast Company, Oprah Daily, LinkedIn Top Startups)
- Social proof: Celebrity endorsements (Huberman, Shetty, Voce, Llewellyn); scientific advisory board (Manson, Cosgrove, Sodickson, Raza, Chang, Diaz)
- Price anchor: "What could cost you $15,000 is $365"
- Comparison table: Standard Checkup (~26 biomarkers) vs Function (160+, 2x/year, personalized plan, imaging, no insurance)
- CTA: "Start testing" → `my.functionhealth.com/signup`

**Friction Points (Inferred):** 🟡
- No pricing calculator at homepage level
- No free trial or sample report
- No live chat for pre-purchase questions
- High cognitive load (160 biomarkers, 18 categories, multiple add-ons)

---

### Stage 2: Marketing Engagement (Pre-Signup) 🟢

**Content Consumption (Inferred):**
- Visitor reads homepage, scrolls through biomarker categories, views comparison table
- Clicks "How it works" to understand 4-step process
- Clicks "What we test" to explore biomarker depth
- Reads FAQ for objections (insurance, frequency, results explanation, action items)
- Views press release / news article for credibility
- Views scientific advisory board profiles
- Potentially searches for reviews (Reddit, YouTube, product comparison sites)

**Conversion Triggers (Confirmed):**
- Price reduction messaging ($499 → $365)
- Limited-time or scarcity messaging (not explicitly time-bound but implied through promotional pricing)
- Celebrity endorsements (Huberman quote: "I've been so impressed by Function")
- Award badges
- "What could cost $15,000 is $365" value anchor

---

### Stage 3: Signup Flow (Direct Observation) 🟢

**URL:** `https://my.functionhealth.com/signup`

**Step 1: Email & Basic Info**
- Email input
- "Get started" / "Continue" button
- System likely validates email format and checks for existing account

**Step 2: Personal Information**
- Legal name (with validation message: "Your name must match the ID you present at each lab visit")
- Phone number
- Marketing consent checkbox: "I consent to receive marketing messages from Function Health using an automatic texting system at the above phone number. My consent is not a condition of using this service."
- Date of birth (MM/DD/YYYY format)
- Biological sex: Female / Male (binary only)
- State selection dropdown (US states only)
- Access code input (optional — likely for referrals, promotions, or corporate partnerships)

**Step 3: Consent & Agreements**
- Checkbox: "I agree to Function's Privacy Policy, Terms of Service, and Request for Lab Results."
- Checkbox: "I agree to Function's Authorization for Use of Medical Information."
- Note: No payment information collected at this stage

**Inferred Post-Signup Steps (Not Directly Observed):** 🟡
- Email verification (confirmation link or code)
- Health history questionnaire (confirmed in "How It Works" description: "Share your health history so we can tailor insights to you")
- Scheduling interface (likely integrated with Quest scheduling system)
- First visit scheduling (date/time selection at 2,000+ locations)

---

### Stage 4: Health History & Personalization 🟡

**Inferred Questions (Based on How It Works Description):**
- Medical history (chronic conditions, previous diagnoses)
- Family history (cancer, heart disease, diabetes, etc.)
- Current symptoms or health concerns
- Supplements and medications
- Lifestyle factors (diet, exercise, sleep, stress)
- Previous lab results (optional upload — confirmed in MI Lab announcement)

**Purpose (Confirmed):**
- Tailor insights to individual
- Inform clinician review
- Feed AI Protocol generation
- Inform personalized recommendations

---

### Stage 5: Verification & Consent (Confirmed) 🟢

**Legal Agreements Required:**
- Privacy Policy
- Terms of Service
- Request for Lab Results (authorization for Function to receive lab results from Quest)
- Authorization for Use of Medical Information (HIPAA-compliant authorization for clinical review and AI processing)

**Inferred Verification Steps:** 🟡
- Email verification (link click)
- Phone verification (optional — marketing consent)
- Identity verification at lab visit (must match legal name on signup with government ID)

---

### Stage 6: Scheduling (Direct Observation + User Reviews) 🟢

**Scheduling Process:**
- User selects date/time at 2,000+ Quest/Getlabs locations
- System generates lab requisition (shared `requisitionId` for annual/mid-year test rounds)
- User receives scheduling confirmation

**Confirmed Issues (User Reviews):** 🟢
- Scheduling system errors (refuses valid dates; claims dates "no longer available")
- Changes must be made through Quest directly; do not sync back to Function app
- Requires manual Function support ticket to update scheduling records
- Concierge blood draw available in select areas (schedule 2-hour window; specialist visits location)
- Multiple visits required for full annual test (1-3 visits over 2-4 weeks)

---

### Stage 7: Lab Visit & Blood Draw 🟢

**Visit Experience:**
- User presents government ID (must match legal name)
- Blood draw performed by Quest/Getlabs staff
- Approximately 10 vials collected (user report mentions 10 vials on first visit, 6 vials on second visit)
- User may need to return for additional visits (hormones, specialty markers, etc.)
- All visits share the same `requisitionId`

**Post-Visit:**
- Quest processes samples (typical lab processing time: days to 2 weeks)
- Results delivered in batches as each visit is processed
- No real-time status updates in Function app

---

### Stage 8: Results Delivery — Batch 1 🟢

**First Results Batch:**
- Approximately 68 results delivered (example from API documentation timeline)
- Includes CBC, metabolic panel, lipids, basic hormone markers
- Delivered via web dashboard and email notification
- User must check dashboard for new results; no indicator of new vs. previously viewed results

**Result Format (Confirmed from API):** 🟢
- Biomarker name (e.g., "Vitamin D, 25-OH")
- Description / "why it matters"
- Current result value (`calculatedResult` / `displayResult`)
- Units (e.g., ng/mL, mg/dL)
- Status: `inRange` (true/false)
- Out of range type: HIGH / LOW / empty
- Function optimal range: "40-80"
- Quest reference range: "30-100"
- Date of service
- Requisition ID

---

### Stage 9: Results Delivery — Batch 2 (and Beyond) 🟢

**Additional Batches:**
- Second visit results: approximately 45 additional results
- Specialty markers, hormone panels, vitamin/nutrient tests
- Total: 113 results (example from API docs; actual number varies by visit)

**User Experience Issues (Confirmed):** 🟢
- User must manually review comprehensive biomarker list on website and compare to populated results
- No "pending" status for unpaid/unprocessed tests
- No new/old indicator (user reports having to write down dates/times to track new results)

---

### Stage 10: Complete Results & Clinician Review 🟢

**Clinician Review Process (Confirmed):**
- Every result reviewed by clinician
- Clinician notes generated (`/notes` endpoint: `id`, `content`, `createdAt`)
- Personalized action plan/protocol generated (`/recommendations` endpoint: `id`, `category`, `title`, `description`)
- Out-of-range biomarkers flagged (`outOfRangeType`: HIGH / LOW)

**AI Protocol Generation:**
- Protocols translate complex health data into easy-to-understand steps (`/recommendations` endpoint)
- Likely includes nutrition recommendations, supplement suggestions, lifestyle modifications
- Informed by health history, biomarker patterns, and clinical guidelines

---

### Stage 11: AI Interaction — Private Chat 🟢

**Features (Confirmed from Press Release):**
- Context-aware responses informed by health data
- Members ask questions and receive explanations/actionable insights
- Informed by biomarker results, clinician notes, recommendations, uploaded health records, and global medical research

**User Feedback (Confirmed):** 🟢
- Analysis is comprehensive but feels generic: "These are great analyses, but you could pull any blood test report into AI and get the same thing"
- No unique personalization beyond standard LLM capabilities

**Inferred Interaction Flow:** 🟡
- Member opens AI Chat in web app
- System retrieves user profile, biomarker results, recommendations, health history
- LLM generates response using RAG over clinical guidelines and user data
- Response includes explanation + action recommendation
- No clinician review of AI chat responses (only clinician review of biomarker results)

---

### Stage 12: Health Record Upload 🟢

**Feature (Confirmed):**
- Secure vault for past lab results, visit notes, medical records
- Uploads inform Private AI Chat and Protocols
- Data remains in secure storage (Firebase/Cloud infrastructure)

**Inferred Upload Flow:** 🟡
- User navigates to upload section
- Selects files (PDF, image, text) from device
- System processes/upload validates file
- Data integrated into AI context and clinician review

---

### Stage 13: Action Protocol & Implementation 🟢

**Protocol Components (Inferred from User Reviews + API):** 🟡
- Nutrition recommendations (food choices, supplements)
- Lifestyle modifications (exercise, sleep, stress management)
- Supplement recommendations (post-SuppCo integration: TrustScore ratings, TESTED program results)
- Retest scheduling recommendations (for out-of-range biomarkers)
- Specialist referral recommendations (inferred; not explicitly confirmed)

**Implementation (User Experience):**
- User reviews protocol steps
- May implement recommendations independently
- No structured tracking or adherence monitoring confirmed
- No direct integration with pharmacy, supplement retailers, or lifestyle apps

---

### Stage 14: Mid-Year Retest (3-6 Months) 🟢

**Retest Process:**
- Member schedules second visit (60+ biomarkers retested)
- Not all 160 biomarkers included (user reviews confirm only ~60 markers retested; many important markers — cholesterol, ANA titer — excluded)
- Results delivered in batches (similar process to initial test)
- Member compares to initial results to track changes

**User Complaints (Confirmed):** 🟢
- "While they tout the 2x/year program, that's not really what it is... On the 2nd visit they only retest 60 of the original biomarkers."
- "If you are out of range in one or more of the 100 tests they don't repeat, you have to pay another $269 to get those."
- "So, for the original 160 to be tested twice it really costs $638 — an additional 73%."

---

### Stage 15: Subscription Renewal 🟢

**Renewal Process (Inferred):** 🟡
- Annual membership ($365) requires renewal
- Member receives renewal notification (likely email, app notification, SMS — given marketing consent)
- Member can renew through web app or cancel
- No evidence of automatic renewal opt-out process

**Retention Mechanisms:**
- Biannual testing creates natural renewal points
- Longitudinal tracking creates data investment (members have historical results)
- Protocol recommendations may require retesting to validate improvement
- Health record uploads create switching costs

---

### Stage 16: Referral & Social Sharing 🟡

**Confirmed Features:**
- Access code field in signup suggests referral tracking
- No explicit referral program documented
- Celebrity endorsements and influencer marketing serve as indirect referral mechanism
- Social media sharing likely encouraged (award badges, health results)

**Inferred Social Features:** 🟡
- Members may share results with doctors, family members, or social networks
- No confirmed social sharing features within app (e.g., share biomarker trends on social media)
- No community features (forums, groups, challenges)

---

### Stage 17: Support & Service 🟢

**Support Channels (Confirmed from User Reviews):**
- Chat support (offshore/scripted; slow response; unhelpful)
- Email support (slow response; script-based)
- No direct phone support
- Concierge scheduling assistance (manual; requires support ticket)

**Support Experience Issues (Confirmed):** 🟢
- "The app support chat/emails are awful. They clearly farm their Support Chats offshore and all they do is regurgitate the same FAQ bs on their site."
- "There is no direct phone support, and chat responses take hours."
- "Even after handing over the additional $269 they continued to hammer me for more 'add-ons'."

---

### Stage 18: Churn & Exit 🟡

**Churn Triggers (Inferred from User Reviews):**
- Scheduling frustration
- Batch result delivery delays
- AI note quality dissatisfaction
- Upsell fatigue
- Incorrect biomarker range interpretation
- Cost concerns (hidden retest fees)
- Lack of specialist referral for serious findings
- Preference for competitor platforms (Mito Health, Superpower mentioned in comparisons)

**Exit Process (Inferred):**
- Member cancels subscription (likely through account settings or support)
- Data retention policies apply (HIPAA requires data retention; member may download results before cancellation)
- No evidence of data deletion process or portability upon cancellation

---

*Sources: Direct site observation; User reviews (Reddit r/Function_Health); Press releases; API documentation; Job listings; News coverage.*
