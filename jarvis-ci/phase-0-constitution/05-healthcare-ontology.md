# Healthcare Ontology
`v1.0.0` · Phase 0 · India-first, standards-grounded

Healthcare is JARVIS's differentiated market. Generic AI analysis does not transfer: the buyer, the safety bar, the data model, and the failure consequences are all different.

---

## 1. Standards stack (L11)

### 1.1 Interoperability

| Standard | Role | JARVIS posture |
|---|---|---|
| **HL7 FHIR R4** | Modern resource-based API standard; JSON/XML over REST. Mandated by ABDM. | **Primary adapter surface** — rank 1 on the adapter ladder |
| **HL7 v2.x** | Legacy pipe-delimited messaging. Still the workhorse of hospital integration worldwide. | Support it. Reality outranks elegance. |
| **DICOM** | Imaging storage/transfer | Required for RIS/PACS adapters |
| **CDA / C-CDA** | Document-level clinical exchange | Lower priority |
| **MCP** | Agent-to-tool protocol; not healthcare-specific but rapidly becoming the interop default for agents | **Strategic** — the bridge between agent and clinical system |

### 1.2 Terminology

| Standard | Covers | Note |
|---|---|---|
| **SNOMED CT** | Clinical terms, findings, procedures | India has national licensing via NRCeS |
| **LOINC** | Lab and clinical observations | Essential for LIS adapters |
| **ICD-10 / ICD-11** | Diagnosis coding, billing | ICD-10 dominant in Indian claims |
| **RxNorm / national drug codes** | Medications | India lacks a single dominant national drug terminology — a real gap |
| **CPT / national procedure codes** | Procedures | Billing-critical |

> **Terminology mapping is the hidden cost of every healthcare integration.** Two systems can both "speak FHIR" and still disagree on what a diabetes diagnosis is called. Any dossier claiming easy interoperability without addressing terminology mapping is superficial.

### 1.3 India — ABDM (Ayushman Bharat Digital Mission)

Run by the National Health Authority. Federated by design: records stay with the originating facility and move only on explicit, time-bound, revocable consent.

| Block | Full name | Function |
|---|---|---|
| **ABHA** | Ayushman Bharat Health Account | 14-digit patient health identity; the anchor for linking records |
| **HFR** | Health Facility Registry | National directory of verified facilities |
| **HPR** | Healthcare Professionals Registry | National directory of verified professionals |
| **HIE-CM** | Health Information Exchange & Consent Manager | The consent gateway through which clinical records actually move |
| **UHI** | Unified Health Interface | Open network for health services discovery/booking |
| **NHCX** | National Health Claims Exchange | Claims and pre-auth between providers and payers |

**Roles:** *HIP* (Health Information Provider — generates records) · *HIU* (Health Information User — consumes on consent) · *Health Locker* (patient-side storage).

**Technical grounding:** FHIR R4 per the ABDM Implementation Guide maintained by NRCeS; ICD-10, SNOMED CT, LOINC as coding standards; sandbox at `sandbox.abdm.gov.in` before production certification.

> ⚠ **The strategic subtlety:** ABDM is genuinely large-scale national infrastructure, and integration is increasingly a commercial prerequisite for Indian health tech. But **ABDM adoption ≠ EMR adoption.** A facility can create ABHA IDs and link records while still running on paper, WhatsApp, and a Tally-style billing package. The gap between "ABDM-connected" and "digitally mature" is where JARVIS's actual opportunity lives — and mistaking one for the other is the most likely strategic error in the entire healthcare thesis. Every healthcare dossier must state which of the two it is measuring.

### 1.4 Regulatory & privacy

India: **DPDP Act 2023** · ABDM Health Data Management Policy · Clinical Establishments Act · CDSCO for software-as-medical-device · Telemedicine Practice Guidelines · NABH accreditation (drives documentation requirements).

Global reference: HIPAA (US) · GDPR (EU) · EU AI Act (high-risk classification for clinical AI) · FDA SaMD pathways.

> India lacks GDPR-equivalent health-specific enforcement maturity. This creates near-term freedom and long-term risk. Architect for the stricter future regime; retrofitting consent and audit is brutal.

---

## 2. Systems of record (L10)

| System | Function | Adapter difficulty |
|---|---|---|
| **EMR/EHR** | Clinical records | Medium — FHIR if modern, DB/HL7 if not |
| **HIS/HMIS** | Hospital operations: registration, ADT, billing, beds | **Hard** — often bespoke, often no API |
| **LIS** | Laboratory | Medium — HL7 v2 common, LOINC mapping needed |
| **RIS/PACS** | Radiology + imaging | Medium — DICOM is mature and well-specified |
| **Pharmacy** | Dispensing, stock | Medium |
| **Practice management** | Scheduling, OPD queues, billing | Easy–medium; often the cleanest APIs |
| **Insurance/TPA** | Claims, pre-auth | Hard — 30+ TPAs, inconsistent formats; NHCX is the consolidation bet |
| **ERP** | Procurement, HR, inventory | Medium |

**Indian market reality that must inform every dossier:** large private chains run mature commercial HIS; government facilities run state or NIC systems; **the enormous middle — nursing homes, standalone clinics, tier-2/3 hospitals — runs partial digitisation, desktop-era software with no API, or paper.** For that segment the adapter ladder frequently bottoms out at UI automation and OCR. That is not a failure of analysis; it is the market. Any strategy that assumes FHIR everywhere is a strategy for the top 5% of facilities.

---

## 3. Clinical workflows

Each is an adapter target. Dossiers assess relevance per workflow.

**Outpatient (OPD):** registration → ABHA link → triage/vitals → consultation → documentation → orders (lab/imaging/Rx) → billing → follow-up
**Inpatient (IPD):** admission → bed allocation → rounds → nursing notes → medication administration → procedures → discharge summary → claims
**Emergency:** triage → resuscitation → rapid orders → disposition
**Operating theatre:** scheduling → pre-op → consent → intra-op notes → post-op → implant tracking
**ICU:** continuous monitoring → device data → protocols → family communication
**Diagnostics:** order → sample → processing → validation → report → critical value alerting
**Pharmacy:** prescription → verification → dispensing → interaction checks → stock
**Revenue cycle:** registration → coding → claim → pre-auth → adjudication → denial management → payment
**Administrative:** rostering, credentialing, procurement, compliance reporting, accreditation documentation

> **Documentation burden is the universal pain**, which is exactly why ambient documentation is the most crowded category in health AI. **Everything downstream of the note — orders, coding, claims, follow-up, denial management — is far less crowded.** A dossier that only evaluates a company's scribe capability is missing where the contested ground actually is.

---

## 4. Healthcare relevance scoring (D7 detail)

| D7 | Meaning | Test |
|---|---|---|
| 0 | Irrelevant | No healthcare presence |
| 1 | Generic tech usable in healthcare | No healthcare-specific work |
| 2 | Some healthcare customers | Opportunistic, no specialisation |
| 3 | Healthcare-specific features/compliance | HIPAA/DPDP posture, clinical features |
| 4 | Healthcare is a primary market | Deep workflow fit, clinical validation |
| 5 | Is healthcare infrastructure | System of record or national standard |

---

## 5. Clinical safety requirements

**Non-negotiable for any JARVIS healthcare capability:**

1. **Human-in-the-loop for clinical actions.** Diagnosis, medication, dosing, orders — never autonomous. The confirmation gate is an architectural component, not a UI checkbox.
2. **Provenance on every clinical assertion.** Which record, which timestamp, which source system. A clinician must be able to trace any claim to its origin in one step.
3. **Explicit uncertainty.** A confidently wrong medication suggestion is worse than no suggestion. Calibration is a safety feature.
4. **Complete audit trail.** Who/what/when/why for every read and write. Required for accreditation and indispensable in litigation.
5. **Fail-safe defaults.** On uncertainty or connectivity loss: stop and escalate. Never guess forward.
6. **Consent enforcement at the architecture level**, not the application level. Under ABDM, consent is the gateway — treating it as a UI concern is a compliance failure waiting to happen.
7. **Data residency.** Indian health data stays in India. Design for it from the start.

> These requirements are also a **competitive moat**, not merely a cost. They are slow, unglamorous, and expensive to retrofit — which is precisely why fast-moving generic agent companies skip them, and precisely why doing them well is defensible.

---

## 6. Healthcare-specific dossier questions

Every healthcare-relevant dossier answers:

1. Which clinical workflows does it touch?
2. Which standards does it implement — and at which shipping rung?
3. Is it a system of record, a workflow layer, or a point solution?
4. What is its India posture? ABDM-integrated? ABHA? NHCX?
5. What is its clinical safety model? Where is the human checkpoint?
6. Adapter ladder placement, with justification.
7. Would a hospital buy JARVIS *instead of* this, *alongside* it, or *through* it?
8. Does it hold clinical data that compounds into an unassailable moat?
9. **Is it measuring ABDM connectivity or actual digital maturity?** (see §1.3)
