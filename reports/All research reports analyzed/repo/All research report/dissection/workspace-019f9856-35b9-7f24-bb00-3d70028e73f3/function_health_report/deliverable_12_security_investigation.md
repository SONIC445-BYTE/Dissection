# DELIVERABLE 12 — SECURITY INVESTIGATION
## FUNCTION HEALTH — HIPAA, SOC2, GDPR, ENCRYPTION, THREAT MODEL, AND COMPLIANCE
*Evidence-based evaluation. All gaps clearly identified.*

---

## 12.1 HIPAA COMPLIANCE

### Confirmed 🟢
- **HIPAA Statement:** Confirmed on homepage: "Built to HIPAA-standards"
- **BAA Not Confirmed:** No Business Associate Agreement (BAA) documentation publicly available; standard for lab partners (Quest) but Function's own BAA status not verified
- **Consent Architecture:** Multiple consent forms required before signup (Privacy Policy, Terms, Lab Results Release, Medical Info Authorization) — aligns with HIPAA authorization requirements
- **Access Control:** Firebase Authentication with JWT tokens; role-based access not confirmed but implied by clinician review process
- **Audit Logs:** Not confirmed; no audit log endpoint documented; open-source project does not reference audit functionality

---

## 12.2 SOC 2 / ISO 27001 / HITRUST

### Confirmed Gaps 🟢
- **SOC 2:** Not mentioned on site, in press releases, or in documentation
- **ISO 27001:** Not mentioned
- **HITRUST:** Not mentioned
- **Security Certifications:** Only HIPAA claim exists; no third-party security audit evidence

---

## 12.3 GDPR (GENERAL DATA PROTECTION REGULATION)

### Confirmed 🟢
- **Geographic Scope:** US-only; no EU operations confirmed
- **GDPR Readiness:** Not mentioned; no GDPR compliance documentation; no EU data processing agreements
- **Data Portability:** Members can download and share results (confirms basic portability) but no structured export format confirmed
- **Right to Deletion:** Not mentioned; HIPAA retention requirements may conflict with GDPR deletion rights

---

## 12.4 ENCRYPTION

### Confirmed 🟢
- **Transport Encryption:** Standard HTTPS (implied by web application and API use)
- **Firebase Authentication:** Google Identity Platform uses industry-standard encryption
- **Cloud Run:** Google Cloud standard encryption for data in transit

### Confirmed Gaps 🟢
- **Encryption at Rest:** Not explicitly confirmed; likely Google Cloud default encryption for Firestore/Cloud SQL but not documented
- **End-to-End Encryption:** Not mentioned for AI chat, health records, or biomarker results
- **Encryption Key Management:** Not documented; likely Google-managed keys

---

## 12.5 THREAT MODEL (INFERRED)

### Confirmed Threats 🟢
- **Unauthorized API Access:** Reverse-engineered API exists (github.com/daveremy/function-health-mcp); no rate limits documented; no API key management confirmed; JWT tokens can be refreshed automatically
- **Data Breach Risk:** Health data (biomarkers, health records, imaging) is highly sensitive; no public breach history but no security certification either
- **Social Engineering:** Customer support reported as offshore/scripted; potential vulnerability to social engineering attacks
- **Insider Threat:** Clinician review process requires access to member data; no role-based access details confirmed
- **Third-Party Risk:** Quest Diagnostics (lab partner), Ezra (imaging), SuppCo (supplements), Google Cloud (hosting) — multiple third-party data processors

---

## 12.6 IDENTITY & ACCESS MANAGEMENT

### Confirmed 🟢
- **Authentication:** Firebase Authentication (Google Identity Platform)
- **Token Management:** JWT (`idToken`, `refreshToken`) with 1-hour expiry
- **User Identification:** UUID (`id`) + `patientIdentifier` (e.g., "P001")
- **Role-Based Access:** Not explicitly documented; clinician access implied by review process

### Confirmed Gaps 🟢
- **Multi-Factor Authentication (MFA):** Not mentioned; no 2FA for account access
- **Single Sign-On (SSO):** Not mentioned; likely not available for enterprise/organizational accounts
- **Account Lockout:** Not confirmed; no brute-force protection details
- **Password Policy:** Not confirmed

---

## 12.7 COMPLIANCE SUMMARY

| Requirement | Status | Evidence |
|-------------|--------|----------|
| HIPAA | Confirmed claim only | Site statement; consent forms |
| Business Associate Agreement (BAA) | Not confirmed | No documentation available |
| SOC 2 Type II | Not confirmed | Not mentioned |
| ISO 27001 | Not confirmed | Not mentioned |
| HITRUST | Not confirmed | Not mentioned |
| GDPR | Not applicable (US-only) | No EU presence; no GDPR docs |
| State Lab Regulations | Confirmed (Quest CLIA) | Lab partner certification |
| FDA (Testing Platform) | Not required (DTC biomarkers) | Only Ezra imaging has FDA clearance |

---

## 12.8 RISK MITIGATION RECOMMENDATIONS FOR OVEXIS

### Strategic Inference 🟡
- Achieve SOC 2 Type II, ISO 27001, and HITRUST before scaling
- Implement 2FA / MFA for all accounts
- Publish security whitepaper and penetration testing results
- Implement granular consent management (opt-in/opt-out for AI processing, marketing, research)
- Build audit logging for all data access and clinical review actions
- Implement end-to-end encryption for health records and biomarker data
- Create GDPR-ready architecture even if US-only initially
- Conduct regular third-party security audits
- Build secure developer sandbox with rate limits and API key management

---

*Sources: Site terms; Signup consent forms; API documentation; Job listings; News coverage; User reviews.*
