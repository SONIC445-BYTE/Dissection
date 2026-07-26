# HEALTHCARE DATA FLOW DIAGRAM — FUNCTION HEALTH

```
MEMBER (Patient / Consumer)
    │
    ├─→ Health History Questionnaire (Personalization)
    ├─→ Government ID Verification (Lab Visit)
    ├─→ Consent (Privacy, Terms, Lab Release, Medical Auth)
    ├─→ Health Record Upload (Past Labs, Visit Notes, Medical Records)
    ├─→ Wearable Data (Future — Apple Health, Oura, Whoop)
    └─→ Lifestyle Data (Nutrition, Exercise, Sleep, Stress)
         │
         ▼
FIREBASE AUTHENTICATION (Identity)
    │ JWT Token (idToken, refreshToken)
    │ User Profile (/user endpoint)
    ▼
DATA RETRIEVAL LAYER (REST API v1)
    │ /biomarkers → /categories → /results-report
    │ /recommendations → /notes → /requisitions
    │ /pending-schedules → /biological-calculations
    ▼
LAB INTEGRATION (Quest Diagnostics — CLIA-Certified)
    │ 2,000+ Locations → Blood Draw (1-3 Visits)
    │ Requisition ID (Groups Visits for Annual/Mid-Year)
    │ Batch Processing (~2 Weeks)
    │ Results: Numeric Values + Qualitative (Positive/Negative) + Inequalities (<0.2, >100)
    ▼
IMAGING INTEGRATION (Ezra — FDA-Cleared AI MRI/CT)
    │ Full-Body MRI (22 min, $499, 100+ Locations)
    │ CT Scan (Lung Cancer, Heart Plaque)
    │ AI-Powered Image Analysis → Structured Reports
    ▼
SUPPLEMENT INTEGRATION (SuppCo — TrustScore, TESTED)
    │ 35,000+ Products → 500,000+ Routines
    │ ISO 17025-Based Testing → Label Accuracy Verification
    │ Supplement Recommendations → Biomarker Correlation
    ▼
CLINICAL REVIEW WORKFLOW
    │ Clinician Reviews Every Result
    │ Out-of-Range Detection (HIGH / LOW / Empty)
    │ Range Comparison (Function Optimal vs Quest Reference)
    │ Clinician Notes Generation (/notes endpoint)
    │ Protocol Generation (/recommendations endpoint)
    ▼
AI PROCESSING (Medical Intelligence Lab)
    │ Private AI Chat (Context-Aware Responses)
    │ Protocol Translation (Complex Data → Action Steps)
    │ Health Record Integration (Past Data Informs AI)
    │ Predictive Modeling (Future — MI Lab Vision)
    ▼
MEMBER DELIVERY
    │ Web Dashboard (Results, Protocols, AI Chat, Health Records)
    │ Email Notifications (New Results, Scheduling Reminders)
    │ SMS/Marketing (Opt-In Consent Required)
    │ Mobile App (Future — Not Confirmed)
    ▼
LONGITUDINAL TRACKING
    │ Requisition History → Change Detection
    │ Biological Age Calculation → Aging Trajectory
    │ BMI Tracking → Weight/Height History
    │ Recommendation Updates → Protocol Adjustments
    ▼
RETENTION & RENEWAL
    │ Annual Subscription ($365) → Mid-Year Retest (60+ Biomarkers)
    │ On-Demand Retesting (Additional Cost — Member-Only Pricing)
    │ Health Record Upload → Data Investment → Switching Cost
    │ Protocol Action → Supplement Tracking → Biomarker Improvement
    ▼
ENTERPRISE / B2B (Future / Partial)
    │ NBPA (NBA Players) → Employer Wellness (Potential)
    │ Healthcare System Partnerships (Potential)
    │ Insurance Integration (Potential — Not Confirmed)
    ▼
INTERNATIONAL (Future — US Only Currently)
    │ UK / EU / Australia / UAE / Asia (Potential)
    │ GDPR Compliance → Multilingual → Local Lab Partnerships
    │ Cross-Border Health Data Portability
