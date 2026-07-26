# DELIVERABLE 10 — TECHNICAL REVERSE ENGINEERING
## FUNCTION HEALTH — FRONTEND, BACKEND, INFRASTRUCTURE, SECURITY, AND DEPLOYMENT
*Evidence-based technical inference from site observation, API documentation, user reports, and job listings.*

---

## 10.1 FRONTEND ARCHITECTURE

### Confirmed 🟢
- **Web Application URL:** `https://my.functionhealth.com/` (primary member interface)
- **Public Website:** `https://www.functionhealth.com/` (marketing, information, conversion)
- **AI Portal:** `https://function.ai/` (Medical Intelligence Lab information)
- **Framework:** Not explicitly documented; likely modern React or Vue.js (based on interactive dashboard, state management needs for biomarker results, scheduling)
- **Mobile:** No native mobile app confirmed; web responsive design likely
- **Browser Support:** Standard modern browsers (Chrome, Safari, Firefox, Edge)

### Inferred 🟡
- **State Management:** React Context, Redux, or Zustand for biomarker result state, user profile, scheduling
- **Data Visualization:** Custom charts for biomarker trends (not confirmed in screenshots but implied by longitudinal tracking)
- **Authentication:** Firebase Auth SDK (JavaScript) for JWT handling
- **Real-Time Updates:** No WebSocket or SSE (Server-Sent Events) confirmed; results delivered via batch updates
- **Accessibility:** No WCAG compliance evidence confirmed

---

## 10.2 BACKEND ARCHITECTURE

### Confirmed 🟢
- **Cloud Provider:** Google Cloud Platform (GCP)
- **Compute:** Google Cloud Run (serverless containers)
- **Base URL:** `https://production-member-app-mid-lhuqotpy2a-ue.a.run.app/api/v1`
- **API Style:** REST (JSON)
- **Authentication:** Firebase Authentication (Google Identity Platform)
- **API Versioning:** `/api/v1` — implies versioned API; no documentation for v2 or future versions
- **Headers Required:** `Authorization: Bearer <idToken>`, `Content-Type: application/json`, `Accept: application/json`, `User-Agent`, `fe-app-version`, `x-backend-skip-cache`, `referer`

### Inferred 🟡
- **Backend Language:** TypeScript or Python (API documentation references TypeScript open-source project; job listings mention TypeScript skills for engineering roles)
- **Framework:** Express.js, FastAPI, or similar REST framework
- **Database:** Firestore (Firebase ecosystem), Cloud SQL (PostgreSQL/MySQL), or BigQuery for analytics
- **Caching:** `x-backend-skip-cache: true` header suggests caching layer exists; likely Cloud CDN or Redis
- **Monitoring:** Google Cloud Monitoring, Firebase Performance Monitoring, or custom analytics
- **CI/CD:** GitHub Actions or Google Cloud Build; deployment to Cloud Run via container registry
- **Feature Flags:** Not confirmed; job listings mention feature flag management potentially through `fe-app-version` header (frontend version tracking)

---

## 10.3 DATABASE & DATA STORAGE

### Confirmed 🟢
- **Biomarker Definitions:** Stored with `questBiomarkerCode`, categories, sex details, optimal/reference ranges
- **Results:** Structured JSON (`biomarkerResultsRecord`) with biomarker metadata, current result values, units, range status
- **User Profiles:** Firebase Auth (identity); additional profile data in application database
- **Recommendations:** Personalized recommendation objects (`category`, `title`, `description`)
- **Clinician Notes:** Text content with timestamps
- **Requisitions:** Grouping mechanism (`requisitionId`) for test rounds

### Inferred 🟡
- **Data Volume:** 50M+ lab tests since 2023; 75M+ results delivered; implies significant database scale
- **Data Retention:** HIPAA requires long-term retention; likely multi-year storage
- **Backup & Recovery:** Google Cloud standard backup; no specific evidence
- **Data Deduplication:** `requisitionId` prevents duplicate test tracking; previous results preserved

---

## 10.4 AUTHENTICATION & SECURITY

### Confirmed 🟢
- **Authentication Provider:** Firebase Authentication (Google Identity Platform)
- **Token Type:** JWT (`idToken`, `refreshToken`)
- **Token Expiry:** 3600 seconds (1 hour) for `idToken`
- **Refresh Mechanism:** `POST https://securetoken.googleapis.com/v1/token?key=...` with `grant_type: refresh_token`
- **Request Headers:** `Authorization: Bearer <idToken>` required for all API requests
- **Version Checking:** `fe-app-version` header checked; outdated versions may return errors

### Confirmed Security Gaps 🟢
- **No Multi-Factor Authentication (MFA) / 2FA:** Not mentioned in documentation
- **No SOC 2 / HITRUST / ISO 27001 Certification:** Not mentioned in site or documentation
- **No Encryption Details:** Only HIPAA claim; no specific encryption at rest or in transit details
- **No Penetration Testing Evidence:** Not mentioned
- **No Security Whitepaper:** Not available

---

## 10.5 THIRD-PARTY INTEGRATIONS & SDKs

### Confirmed 🟢
- **Lab Integration:** Quest Diagnostics (CLIA-certified)
- **Imaging Integration:** Ezra (FDA-cleared AI MRI)
- **Supplement Integration:** SuppCo (TrustScore, TESTED)
- **Cloud:** Google Cloud Platform (Cloud Run, Firebase, likely BigQuery, Cloud Storage)

### Inferred 🟡
- **Analytics:** Google Analytics, Firebase Analytics, Mixpanel, Amplitude, or custom analytics
- **Email:** SendGrid, Mailgun, Amazon SES, or Firebase email extensions
- **Messaging:** SMS via Twilio, Firebase Cloud Messaging, or similar
- **Payments:** Stripe, PayPal, or similar for $365 annual subscription
- **Image Storage:** Google Cloud Storage for MRI/CT images, member profile images, document uploads
- **Notification:** Firebase Cloud Messaging, email, or SMS for scheduling reminders, result notifications

---

## 10.6 MONITORING, ANALYTICS, & PERFORMANCE

### Confirmed 🟢
- **Rate Limiting:** No explicit headers; aggressive parallel requests trigger errors; project serializes requests with 250ms spacing and exponential backoff
- **Version Tracking:** `fe-app-version` header (e.g., "0.84.0") — allows backend to check frontend compatibility
- **Performance Monitoring:** Not confirmed; likely Google Cloud Monitoring

### Inferred 🟡
- **User Analytics:** Tracking user journeys (anonymous → signup → scheduling → results → renewal); conversion funnels; retention metrics; feature usage
- **Clinical Analytics:** Biomarker out-of-range rates; protocol adoption; retest scheduling; clinician review times
- **AI Analytics:** Chat usage; recommendation acceptance; health record upload rates; biological age calculation frequency
- **Business Metrics:** Customer Acquisition Cost (CAC), Lifetime Value (LTV), retention rate, upsell conversion, referral rate

---

*Sources: Direct site observation; Reverse-engineered API docs (github.com/daveremy/function-health-mcp); Press releases; Job listings; User reviews.*
