# JARVIS Product Decision Document
## From fragmented hospital software to an execution-oriented Healthcare Operations Fabric

**Decision date:** 2026-07-26  
**Evidence base:** `01_KNOWLEDGE_GRAPH_AND_NORMALIZED_PROBLEM_DATABASE.md`, derived from all 283 repository files. This document uses the normalized graph/database as its input; it does not treat the corpus as an equal vote count.

---

## 1. Executive summary

### The decision
JARVIS should become an **India-first Healthcare Operations Fabric**: an integration-light, audit-ready execution layer that turns fragmented hospital signals into a shared patient-journey event graph, role-specific work queues, next-action checklists, and closed-loop escalation.

It should **not** begin by replacing an HIS/EMR, being a generic AI copilot, building an autonomous diagnostic system, or becoming a standalone ambient scribe. Those are either saturated, too risky, too narrow, or too difficult to distribute as the first product.

### Initial wedge
The first commercial product should be **JARVIS Discharge-to-Claim Command Center** for 50–300-bed Indian multi-specialty hospitals and hospital chains:

1. Assemble the operational and documentation state for every inpatient encounter.
2. Identify discharge blockers, missing clinical/billing documents, authorisation/eligibility issues, and claim-readiness gaps.
3. Assign the next action to the accountable nurse, doctor, front desk, billing/coder, pharmacy, housekeeping, or payer liaison.
4. Escalate ageing exceptions and create an auditable, human-approved discharge/claim packet.
5. Feed bottleneck analytics back to COO/CFO/department heads.

This wedge compounds into bed throughput, revenue integrity, documentation, patient communication, referral, pharmacy, and eventually the cross-hospital network. It is an **operations-and-finance control plane**, not a billing tool.

### Why this wins the corpus test
The corpus repeatedly shows a connected failure spine:

> fragmented data and documents → invisible work/state → delayed or incomplete handoffs → delayed discharge and care → coding/claim defects → denials/cash pressure → understaffing/burnout → more fragmented work.

The strongest product opportunity is the layer that makes this state visible, assigns work, and closes the loop across departments. It addresses the highest-frequency, high-cost and cross-workflow nodes: interoperability (218 documents), documentation (183), coordination/handover (105), unstructured documents (102), claims denials (245), revenue leakage (181), ED/flow (225), workforce/burnout (236/231), and capacity/discharge (55/44). Frequency alone did not decide the product: generic documentation and pure claims are crowded; clinical autonomy is high-risk; the selected wedge has a credible buyer, quantifiable outcome, and a path to system lock-in.

### Product thesis in one sentence
**JARVIS is the hospital’s event-and-work orchestration layer: it sees the real patient journey across systems and documents, tells the right human what must happen next, and proves that it happened.**

---

## 2. Knowledge graph synthesis

### 2.1 Root causes, symptoms, and leverage points

| Layer | Root causes in the evidence | Symptoms | Product implication |
|---|---|---|---|
| Data foundation | Legacy/siloed HIS, paper/PDFs, inconsistent coding, missing interfaces, disconnected departmental systems | Duplicate entry, record chasing, unreliable dashboards, incomplete packets | Build a canonical event layer with source provenance; do not attempt to rip/replace the HIS. |
| Work execution | No shared task ownership, manual calls/WhatsApp/paper, weak escalation and handover | Delays, missed steps, queue opacity, informal workarounds | Make “owner, next action, due time, evidence, escalation” a first-class data object. |
| Economic loop | Documentation gaps, coding defects, rule complexity, payer friction, scheme administration | Denials, delayed cash, revenue leakage, staff rework | Link operational state to revenue readiness rather than automating only the last claim step. |
| Capacity loop | Staffing shortages, late discharge, uncoordinated bed/cleaning/transport, unpredictable arrivals | ED boarding, waits, conflict, burnout | Use event state to coordinate discharge/bed turnaround; do not sell black-box bed prediction alone. |
| Trust/governance | Unclear communication, incomplete consent/audit trail, slow grievance response | Violence, complaints, legal risk, defensive care | Produce a traceable timeline and event-triggered family updates with human governance. |
| Access loop | Rural scarcity, weak referral closure, incomplete longitudinal records | Late presentation, tertiary overload, unqualified care | Extend the same referral packet and closed-loop task model after hospital operations is proven. |

### 2.2 Highest-leverage normalized problem clusters

| Cluster | Why it is strategically material | Why it is not the standalone company |
|---|---|---|
| Interoperability + documents + work coordination | It is upstream of care, capacity, revenue, compliance and trust; it recurs across system types. | A generic integration engine has slow sales and unclear user value unless attached to an outcome workflow. |
| Discharge/bed/flow | It joins nursing, clinicians, pharmacy, billing, housekeeping and patient communication; has daily executive visibility. | Bed-management dashboards alone are easy to ignore if they cannot coordinate the blockers. |
| Claim readiness/revenue integrity | Direct CFO value; repeated in 245 denial and 181 cash-flow documents; creates structured evidence requirements. | Pure RCM is crowded, payer-specific and can become a services business. |
| Documentation and handoff | High-frequency producer of clinical, revenue and legal defects; generates the event trail. | Ambient scribing by itself is becoming a commodity and does not solve downstream work. |
| Workforce/burnout | Largest human-system pain; affects all workflows and retention. | A wellbeing or scheduling app cannot cure upstream fragmentation, load and payment constraints. |
| Trust/communication/security | Urgent India-specific failure loop and a differentiator for operations data. | Security-only or grievance-only products have fragmented buyers and policy sensitivity. |

---

## 3. Problem database decision layer

The complete 38-node database, with root causes, workflow, stakeholders, sources, geographies, settings, impacts, existing-solution gaps, AI paths, difficulty, market and priority, is in `01_KNOWLEDGE_GRAPH_AND_NORMALIZED_PROBLEM_DATABASE.md`.

### 3.1 Opportunity selection logic

Each opportunity was assessed on: evidence frequency, economic/human urgency, cross-workflow leverage, incumbent gap, buyer clarity, integration burden, safety/regulatory exposure, and compounding data/workflow value. The following is a **product decision ranking**, not an assertion that one social problem matters more than another.

| Rank | Opportunity | Primary buyer | Primary users | Why it compounds | JARVIS fit /100 |
|---:|---|---|---|---|---:|
| 1 | Discharge-to-claim command center | COO + CFO | Ward nurse, discharge coordinator, billing/coder, doctor | Captures encounter state, documents, tasks, financial readiness and bottleneck data | **91** |
| 2 | Patient-journey event graph / interoperability fabric | CIO/COO | All operational teams | Shared substrate for every later module and cross-facility data | **90** |
| 3 | Cross-department task/handoff orchestration | COO/CNO | Nursing, front desk, lab, pharmacy, billing | Creates daily habit, ownership and workflow lock-in | **89** |
| 4 | Scheme/claim document readiness | CFO/RCM head | Billing, coders, clinicians | Direct cash impact; produces payer rule/evidence graph | **88** |
| 5 | Bed turnover and discharge readiness | COO/CNO | Ward, housekeeping, transport, billing | Converts work-state data into capacity/flow control | **87** |
| 6 | Unstructured document ingestion with provenance | CIO/COO | Records, billing, clinical ops | Unlocks legacy data and creates reusable document intelligence | **86** |
| 7 | Patient/family status communications | COO/patient-experience head | Front desk, patient liaison, families | Reduces status-chasing; trust data attaches to journey | **83** |
| 8 | Referral/transfer packet and closure | COO/clinical director | Referral desk, clinicians, ambulance | Extends event graph beyond hospital boundary | **82** |
| 9 | ED flow/triage operations command center | COO/ED director | Triage nurse, ED doctor, bed manager | High urgency but requires mature real-time operational data | **80** |
| 10 | Workload/capacity intelligence | COO/CNO | Unit managers | Helps staffing decisions once task telemetry exists | **78** |
| 11 | Government-scheme workflow workbench | CFO/RCM head | Scheme desk, billing, clinicians | India-specific distribution and rules dataset | **78** |
| 12 | Consent/audit/event-timeline ledger | COO/legal/quality | Clinicians, records, legal | Trust and evidence layer across workflows | **75** |
| 13 | Medication reconciliation and shortage tasks | CMO/pharmacy head | Pharmacists, nurses | Valuable, but clinical safety validation and pharmacy integration increase scope | **71** |
| 14 | Equipment readiness worklists | COO/biomedical head | Biomedical, maintenance, ED/ambulance | Event-driven maintenance data can attach to operations fabric | **68** |
| 15 | AI-assisted resident logbook/documentation | Medical-college leadership | Residents, faculty | Accessible wedge but narrower buyer and category crowding | **67** |
| 16 | Credential/privilege guardrails | Quality/HR/clinical director | HR, scheduling, unit managers | Important trust layer but registry/policy dependency | **64** |
| 17 | Chronic-care outreach worklists | Care-delivery head | Care coordinators | Large market but weak immediate hospital data/ownership | **62** |
| 18 | Procurement and stock-out intelligence | COO/procurement head | Store, pharmacy, procurement | Valuable only after reliable demand/master data | **60** |
| 19 | Security/crowd-response workflow | COO/security head | Security, ED, patient liaison | Human value is high; privacy/procurement/physical-response dependence | **56** |
| 20 | Autonomous diagnostic/triage copilot | CMO | Clinicians | Clinical risk, validation burden and incumbent competition make this later—not first | **47** |

### 3.2 JARVIS fit scoring rubric

| Criterion | Weight | What received credit |
|---|---:|---|
| Mission alignment | 20 | Reduces operational friction while improving care continuity and staff dignity |
| Can become infrastructure | 20 | Creates reusable state, identity, documents, tasks, rules or integration assets |
| AI advantage | 15 | Requires contextual extraction, prioritisation or natural-language workflow—not simple CRUD |
| Data advantage | 10 | Produces proprietary labelled workflow/outcome data with customer consent |
| Offline capability | 10 | Can operate through mobile, asynchronous sync, cached worklists and document capture |
| Cross-workflow leverage | 10 | Reused by multiple departments and journey stages |
| Global scalability | 5 | Generalises beyond India with configurable rules/connectors |
| Indian urgency | 5 | Directly matches Indian hospital and scheme friction |
| Engineering feasibility | 5 | Can be launched safely in a 12–16-week pilot without replacing core systems |

**Score interpretation:** a high score is a sequencing recommendation, not a guarantee of adoption. No clinical-autonomy use case can bypass local validation, quality governance, privacy/security controls, or human accountability.

---

## 4. System failure loops

### Loop 1 — Documentation-to-cash-to-staffing loop
Incomplete notes / scanned documents / missed signatures  
→ coding and claim packet defects  
→ denials and delayed reimbursement  
→ cash pressure  
→ delayed hiring / understaffed RCM and wards  
→ rushed documentation and more defects.

**Intervention point:** real-time encounter completeness and accountable exception worklists before discharge/claim submission.

### Loop 2 — Capacity-to-violence-to-attrition loop
Understaffing and poor bed/discharge coordination  
→ ED/OPD waits and crowding  
→ families receive insufficient status information  
→ conflict/violence and staff distress  
→ burnout, absenteeism and migration  
→ lower capacity and longer waits.

**Intervention point:** shared flow state, discharge blocker ownership, ETA/status updates, and escalation—not surveillance alone.

### Loop 3 — Fragmented-data-to-manual-work loop
Siloed HIS/LIS/RIS/ERP plus paper/PDF/WhatsApp  
→ re-entry and record chasing  
→ late/incomplete handoffs  
→ missed tasks and poor data quality  
→ distrust of dashboards and more shadow tools  
→ deeper fragmentation.

**Intervention point:** source-linked event ingestion and a work layer that demonstrates value without forcing a full migration.

### Loop 4 — Scheme-friction-to-access loop
Complex eligibility/package/document rules  
→ rejection/delay and costly rework  
→ hospital cash losses/withdrawal from scheme  
→ poorer patient access and public-system load  
→ overload and rushed documentation  
→ more scheme friction.

**Intervention point:** policy/rule-aware packet readiness, evidence provenance and human-managed exceptions.

### Loop 5 — Referral-to-late-presentation loop
Rural scarcity/offline records/unclear referral paths  
→ incomplete transfer and delayed specialist review  
→ late tertiary presentation and crowding  
→ poor outcomes/trust erosion  
→ bypass of primary care and further tertiary overload.

**Intervention point:** offline referral packet, destination/appointment status and closed-loop handoff.

### Loop 6 — Audit/trust/defensive-medicine loop
Incomplete consent/event evidence and slow grievance response  
→ allegations and legal/reputation threat  
→ defensive tests/documentation burden  
→ costs/waits and patient distrust  
→ more complaints and conflict.

**Intervention point:** consent-aware event timeline, transparent status updates and retrieval—not clinical decision automation.

---

## 5. Stakeholder analysis

| Stakeholder | Daily work and manual friction | Pain / decision power / buying power | JARVIS opportunity |
|---|---|---|---|
| Physicians/consultants | Assess, order, document, sign, respond to queries, coordinate discharge | High pain; high clinical influence; variable budget authority | Minimum-click evidence review, missing-item prompts, sign-off queue; never auto-sign. |
| Residents/interns | Rounds, notes, logbooks, orders, handoffs, patient/family updates | Very high pain; low purchasing power | Structured capture, task/handoff list, logbook draft with supervisor review. |
| Nurses | Intake, monitoring, medication, discharge education, coordination and handovers | Very high pain; high operational influence; low direct budget | Mobile worklist, due/overdue tasks, role handoff, discharge checklist, escalation. |
| Front desk/reception | Registration, eligibility, appointments, status calls, billing questions | High pain; moderate influence | Identity/eligibility capture, status scripts, ETA updates, unresolved-case routing. |
| Discharge coordinators/ward clerks | Chase signatures, reports, pharmacy clearance, bill, transport, family readiness | Very high pain; moderate influence | Command-center queue with blocker owner, due time, evidence, escalation and completion proof. |
| Billing/coders/RCM | Read charts, code, submit, follow claims, answer payer queries/appeals | High pain; high CFO influence | Evidence-linked packet, rule/completeness checks, coding review queue, denial learning. |
| CNO/nursing leadership | Staffing, quality, throughput, incident response | High pain; strong champion, moderate budget | Unit load/ageing dashboard, workload and handoff exceptions, quality audit trail. |
| COO/administrator | Throughput, patient experience, department coordination, operating cost | High pain; strongest operational buyer | System-wide bottleneck view, SLA/escalation controls, measurable throughput. |
| CFO/owner | Cash, claims, cost, capex, risk | High pain; highest financial buying power | Discharge-to-cash conversion, prevention of avoidable leakage, audit-ready ROI. |
| CIO/IT | Integration, security, uptime, vendor sprawl, compliance | High pain; veto/architecture authority | Connector strategy, data minimisation, on-prem/hybrid option, audit/security controls. |
| Patients/families | Wait, unclear status/cost, fragmented follow-up and grievance | High human pain; low buying power but high adoption influence | Consent-based multilingual status, discharge plan, transparent next steps and escalation. |
| Payers/TPAs/scheme administrators | Complete evidence, rule adherence, fraud/risk control | Moderate pain; external gatekeeper | Standardised, evidence-linked packet and traceable submission—not adversarial automation. |
| Pharmacy/procurement | Verify/dispense, stock, approvals, vendor follow-up | High local pain; moderate buying power | Event-triggered clearance and stock exception worklists. |
| Lab/radiology | Order completeness, queue, result verification, communication | High pain; moderate influence | Missing-order/result escalation, status events, turnaround exception queues. |
| Housekeeping/transport | Bed cleaning/turnover, transfer and task confirmation | High pain; low buying power | Mobile assignment, proof of completion, bed-release trigger. |
| Biomedical/maintenance | Asset checks, preventive maintenance, emergency repair | High safety pain; niche buyer | Asset readiness and maintenance exception integration in later phase. |
| Security | Crowd/incident response, coordination with ED and police | High human risk; moderate buyer | Human-led escalation protocol and event timeline; no default biometric surveillance. |
| Government/regulators | Scheme compliance, reporting, access, standards | High policy influence | Configurable rules, audit trail, ABHA/ABDM-aligned exchange where applicable. |

---

## 6. Workflow matrix

| Workflow | Inputs → outputs | Current bottlenecks/manual work | Automation/AI opportunity | Phase |
|---|---|---|---|---|
| Registration/OPD | Identity, appointment, eligibility → encounter | Re-entry, queues, incomplete demographics | Assisted capture, duplicate/eligibility checks, wait-status updates | 2 |
| ED | Arrival, symptoms, capacity → disposition | Manual triage calls, invisible beds, crowding | Operational queue/bed escalation; clinician-owned triage support | 3 |
| Admission | Order, bed, record → occupied bed/active case | Calls, duplicate records, missing documents | Admission checklist and source-linked event start | 1 |
| Inpatient/ward | Orders, observations, tasks → care/discharge readiness | Handover, task ownership, missing signatures | Role worklists, ageing task escalation, evidence capture | 1 |
| ICU | Monitoring, orders, capacity → transfer/discharge | High-acuity complexity/integration | Later operational handoff/readiness use only | 4 |
| Operation theatre | Booking, consent, clearance → procedure record | Consent/documents/coordination | Consent/clearance event checklist; no autonomous clinical control | 4 |
| Lab | Order/specimen → verified result | Order/result chase, TAT exceptions | Result-status events and exception routing | 2 |
| Radiology | Order → image/report → acknowledgement | Scheduling, result follow-up | Status events and abnormal-result acknowledgement workflow | 2–3 |
| Pharmacy | Prescription/order → dispense/clearance | Discharge medication readiness, stock checks | Discharge clearance task and shortage exception | 1–2 |
| Discharge | Clinical clearance, meds, bill, summary, transport → departure | Multi-owner blockers, family uncertainty | **Core v1:** shared readiness state, owner/escalation, summary/packet draft | 1 |
| Billing/claims | Services, documents, codes, eligibility → clean claim/remittance | Chart chase, missing evidence, rule drift | **Core v1:** readiness checks, evidence packet, human review and claim worklist | 1 |
| Prior authorisation | Policy/evidence → submission/decision | Payer portals, calls/fax, status chase | Policy-aware document assembly/status worklist | 3 |
| Medical records | PDFs/scans/notes → usable verified event/evidence | OCR, retrieval, incomplete data | **Core v1:** OCR/extraction, provenance, confidence review | 1 |
| Bed/housekeeping/transport | Discharge order → clean available bed | Calls and unclear ownership | **Core v1:** turnover task chain and real-time status | 1 |
| Referral/transfer | Patient context/capacity → accepted handoff/outcome | Paper/phone, no closure | Referral packet and closed-loop tracking | 3 |
| Government schemes | Eligibility/package/docs → claim/audit | Rule complexity and rejection rework | Rule profiles, document completeness, audit timeline | 2 |
| Procurement/inventory | Consumption/requisition → stock availability | Manual counts, delayed purchase | Demand/exception view after trustworthy events exist | 4 |
| Biomedical/security | Asset/incident → resolved safe state | Reactive tickets, disconnected context | Asset/incident worklists, escalation, audit timeline | 4 |

---

## 7. Competitor map — real companies only

**Method:** Proposed ventures from the repository are excluded. This is a directional market map, not a procurement recommendation or exhaustive vendor list. Validate country, deployment, integration, security, pricing and claims before selection.

| Problem/category | Real companies/platforms | What they do well | Open gap relevant to JARVIS |
|---|---|---|---|
| India HIS/HMS | Practo Insta/Ray, MocDoc, KareXpert, HealthPlix, Attune, Caresoft, SoftClinic, Healthray, DocPulse, Eka Care | Core registration-to-billing modules, EMR, departmental features; Eka publicly positions FHIR/ABDM APIs and tools across EMR/hospital management. [Eka Care](https://www.eka.care/) | Hospitals remain heterogeneous; JARVIS must coexist and execute cross-department exceptions rather than replace them. |
| Open-source/public-health stack | Bahmni, OpenMRS, OpenELIS, OpenEMR, Odoo | Configurable, low-resource deployment; Bahmni is built on OpenMRS/OpenELIS/Odoo and documents FHIR/ABDM support. [Bahmni](https://github.com/bahmni) [interoperability note](https://bahmni.atlassian.net/wiki/spaces/BAH/pages/3176333313/Bahmni+support+for+Open+Global+Standards+Interoperability+OpenHIE+-+2023+Roadmap) | Implementation capacity and customisation; opportunity for a lightweight operational layer and connectors. |
| Global EHR/enterprise | Epic, Oracle Health/Cerner, MEDITECH, athenahealth | Deep clinical/financial system of record and installed base | In India, mixed/legacy environments; operational work across paper, third parties and local systems remains a gap. |
| RCM, coding, denials | Waystar, AKASA, CodaMetrix, Adonis, Candid Health, Fathom, Nym, athenahealth | Mature US-oriented claims, coding and denial automation; reported offerings span coding, CDI, authorisation and claims. [market review](https://omnimd.com/blog/top-ai-medical-billing-platforms/) | India/scheme rules and upstream inpatient operational/document state; avoid competing as a generic coding vendor. |
| Prior authorisation / utilisation management | Cohere Health, Availity, Edifecs, HealthEdge, Inovalon, MHK, eviCore, Infinitus, CoverMyMeds | Payer/provider workflow tooling, medical-policy workflows and communications; CMS PA APIs shape US market. [vendor landscape](https://rxalmanac.com/articles/ai-prior-auth-vendors/) | India-specific scheme/private-payer integration and hospital-side evidence capture/handoffs. |
| Ambient documentation | Microsoft Dragon Copilot/Nuance DAX, Abridge, Suki, Nabla, Ambience, DeepScribe, Heidi, Freed | Speech/document generation and increasingly EHR integration; Abridge, Nuance and Suki are major enterprise names. [overview](https://physicianaihandbook.com/practical/documentation.html) | A note is not an execution layer. JARVIS should use ambient/document AI only to create reviewed events/tasks. |
| Patient engagement/communications | Practo, Eka Care, WhatsApp Business ecosystem, hospital CRMs | Appointment, telehealth, reminders, patient access | Status messages are often detached from actual workflow state; JARVIS can send only event-grounded communications. |
| Workflow/automation platform | ServiceNow, Microsoft Power Platform, UiPath, Salesforce, generic task tools | Configurable automation and enterprise integration | Do not understand hospital roles, patient-context safety, provenance, clinical/RCM policy and local deployment constraints. |
| Imaging/diagnostic AI | Qure.ai, Lunit, Aidoc, Viz.ai, numerous PACS/RIS vendors | Narrow diagnostic/imaging models | JARVIS should orchestrate result status and acknowledgement, not replicate specialised diagnostic models. |

### Competitive position
JARVIS competes **indirectly** with HMS modules, task tools, RCM vendors and document AI. Its differentiation must be: **vendor-neutral event graph + India-specific workflow packs + role-based execution + source provenance + hybrid/offline deployment + measurable discharge-to-cash/throughput outcome.**

---

## 8. Technology landscape and recommended architecture

### 8.1 Architecture decision

**Recommended architecture: a modular Healthcare Operations Fabric, not a monolithic Hospital OS.**

```text
Existing HIS / EMR / ERP / LIS / RIS-PACS / payer portals / ABHA-ABDM / PDFs / voice / CSV
                                  │
                   connectors + secure ingestion + OCR + mapping
                                  │
        canonical patient-journey event graph (source, time, actor, confidence, consent)
                                  │
          rules engine + workflow state machine + policy configuration + audit ledger
                                  │
  role worklists / command center / mobile offline app / integrations / patient communications
                                  │
    analytics: throughput, task ageing, discharge blockers, documentation gaps, claim readiness
```

### 8.2 Non-negotiable product principles

1. **System of action, not initial system of record.** Read/write through governed interfaces or export/import; preserve source links.
2. **Human accountability.** AI drafts, extracts, prioritises and explains. Clinicians/coders/authorised staff approve clinical, coding and financial decisions.
3. **Event provenance.** Every fact shows source system/document, timestamp, actor, extraction confidence and review state.
4. **Configurable workflow, not hard-coded hospital dogma.** Implement versioned hospital/scheme/payer policy packs and local SOPs.
5. **Offline-tolerant.** Mobile worklists cache assigned tasks, support delayed sync and expose conflicts rather than silently overwriting.
6. **Integration-light first.** Start with daily/near-real-time exports, document inboxes, barcode/QR where needed, FHIR/HL7/API connectors where available. Do not make perfect integration a precondition for value.
7. **Security by design.** Tenant isolation, least privilege, consent-aware access, encryption, audit export, retention controls, local hosting/hybrid deployment options.
8. **No silent automation of diagnosis, prescriptions, code selection, claim submission or patient-risk decisions.** These are human-reviewed workflow outputs.

### 8.3 AI components that genuinely create advantage

| Component | Role | Guardrail |
|---|---|---|
| Multimodal document intelligence | Extract document type, fields, evidence and missing items from scans/PDFs/notes | Confidence thresholds; source preview; human verification for consequential data |
| Clinical/operational event extraction | Convert reviewed notes/orders/results into event candidates and tasks | No creation of facts without source/provenance; clinician controls clinical record |
| Policy/rules retrieval | Match claim/scheme/discharge requirements to encounter evidence | Version policies; cite the policy/version; route ambiguity to humans |
| Exception prioritisation | Rank cases by ageing, blocker dependency, financial/care impact | Explain priority; allow local override; monitor bias/workload consequences |
| Task/communication drafting | Draft internal tasks or patient messages from actual state | Approved templates, multilingual review, no invented status or medical advice |
| Learning analytics | Discover bottleneck patterns and predict likely blocker classes | Start observationally; validate before prescriptive automation |

---

## 9. Moat analysis — top 10

| # | Moat | How it is earned | Why it is defensible |
|---:|---|---|---|
| 1 | Patient-journey event graph | Reconcile heterogeneous system, document and human-work events with provenance | It becomes the local operational truth used daily across departments. |
| 2 | Workflow lock-in | Role worklists, ownership, escalation and completion evidence become part of every discharge | Replacing it disrupts coordination habits, not merely a dashboard. |
| 3 | Integration library | Reusable connectors/mappings for Indian HIS, LIS, billing, scheme and document environments | Deployment cost and time decline with each compatible hospital. |
| 4 | Local policy/rule graph | Versioned scheme, payer, discharge and hospital-SOP requirement packs | It requires continuous local evidence mapping and operational feedback. |
| 5 | Exception-resolution data flywheel | Each resolved blocker links event, document gap, owner, action and outcome | Produces a unique labelled workflow dataset—not just note text. |
| 6 | Cross-role network effect | More departments contribute state, increasing usefulness for each role | A billing-only or nurse-only tool cannot see the full dependency graph. |
| 7 | Audit/provenance trust | Source-linked history, review state and consent/access trail | Quality/compliance stakeholders become advocates and integration gatekeepers. |
| 8 | Distribution through measurable ROI | Discharge time, bed turnover, claim readiness and rework reduction | CFO/COO renewal is grounded in operations, not discretionary AI experimentation. |
| 9 | Offline/hybrid competence | Reliable mobile and low-integration deployment in constrained facilities | Global cloud-first vendors often underinvest in this operational edge case. |
| 10 | Multi-facility benchmark layer | De-identified, consented operational patterns across chains (only after governance) | Enables better configuration and forecasting while preserving tenant boundaries. |

**Moat warning:** data access alone is not a moat. The defensible asset is a trusted, permissioned, source-provenance workflow graph with a demonstrated ability to close exceptions.

---

## 10. Product evolution and roadmap

### Final architecture identity
**JARVIS evolves from a workflow automation layer into a Healthcare Operations Fabric and, later, a multi-facility Operations OS.** It is neither a clinical decision system nor a complete replacement hospital information system.

### Stage 0 — Design-partner discovery (0–8 weeks)
- Select 2–3 design partners: 50–300-bed multi-specialty hospitals with inpatient billing/scheme volume, one executive COO champion and CFO/RCM co-owner.
- Instrument a 30-day baseline: discharge order-to-departure time, discharge blockers by department, chart-completeness defects, claim-ready rate at discharge, rework touches, denial categories, bed turnaround.
- Map local SOPs and system inventory; identify one small set of read-only exports/document channels.
- Establish security, consent/access, data-processing and human-review design.

**Exit criterion:** a confirmed, named set of high-volume blockers with baseline and an integration path that does not require core HIS replacement.

### Stage 1 — MVP: Discharge-to-Claim Command Center (months 2–6)
- Inpatient encounter board and canonical status model.
- Document inbox/OCR with source preview and confidence-based verification.
- Discharge readiness checklist: clinical sign-off, summaries, diagnostic results, pharmacy, billing, payer/scheme evidence, transport, family communication.
- Department worklists, owner/due time/escalation and audit trail.
- Claim-readiness evidence checklist and coder/RCM review workspace; **no autonomous submission**.
- COO/CFO operational dashboard and pilot measurement.

**Success measures:** percentage of cases with named blocker owner; time from discharge order to departure; claim-ready rate; missing-document rework; user task closure; no material safety/privacy incident.

### Stage 2 — Flow and revenue intelligence (months 6–12)
- Bed turnover chain: discharge → clearance → housekeeping → transport → available bed.
- Configurable rule packs for top scheme/private payer workflows.
- Source-linked coding/documentation query support and denial-reason learning.
- Event-grounded patient/family communications.
- FHIR/HL7 and common Indian HIS connector expansion; offline mobile worklists.

**Exit criterion:** repeatable deployment in 8–12 weeks and verified economic value across at least three facilities.

### Stage 3 — Hospital Operations Fabric (years 2–3)
- ED-to-bed flow operations, lab/radiology result exception workflow, referral/transfer packet and closed-loop tracking.
- Workforce workload/capacity intelligence based on observed tasks—not speculative productivity scoring.
- Multi-facility command view for chains with strict tenant/data controls.
- Workflow marketplace/configuration studio for local SOPs, payer/scheme packs and integrations.

### Stage 4 — Network and decision intelligence (years 3–5)
- Consent-governed cross-facility referral/transfer network.
- Benchmarking using de-identified aggregate operational patterns only where lawful and contractually authorised.
- Predictive exception prevention, simulation and resource planning, introduced workflow by workflow with validation.
- Extension to PHC/referral and government programme flows through offline-first packages.

### Long-term vision
A hospital can run clinical and administrative systems of record of its choice. JARVIS becomes the **operational nervous system** that maintains current state, coordinates people and systems, and measures whether every critical patient and revenue workflow is actually closed.

---

## 11. Feature prioritisation

| Must build | Why |
|---|---|
| Canonical encounter/event model with source provenance | Essential platform primitive; without it JARVIS becomes another task list. |
| Inpatient discharge readiness board | Highest-value, bounded initial workflow with cross-department dependency. |
| Role worklists, ownership, SLA and escalation | Converts visibility into execution and creates daily lock-in. |
| Document ingestion/OCR with confidence review | Works with the corpus’s paper/PDF reality and unlocks claim/discharge evidence. |
| Claim/scheme evidence completeness checklist | Direct CFO value; connects operational work to cash without becoming a generic RCM vendor. |
| Audit trail, RBAC, consent-aware access and export | Required for trust, security and deployment. |
| Baseline/ROI analytics | Required to prove value and avoid AI theatre. |
| Mobile/offline-tolerant task experience | Needed for wards and uneven connectivity. |

| Should build | Why |
|---|---|
| Bed turnover/housekeeping/transport chain | Natural adjacency after discharge readiness. |
| Patient/family status messages | Reduces status work and trust friction only when grounded in real events. |
| FHIR/HL7/API connectors plus CSV/SFTP/document adapters | Lowers deployment friction and expands data freshness. |
| Rule-pack manager for scheme/payer/SOP requirements | Builds local defensibility; must be versioned and human governed. |
| Denial-reason and documentation-query workbench | Valuable after evidence pipeline is reliable. |
| Lab/radiology result exception queue | Cross-workflow expansion with clear status semantics. |
| Referral/transfer packet | Builds network graph after internal handoffs work. |

| Could build later | Why |
|---|---|
| Ambient voice capture | Useful input modality; not differentiating product core. |
| Workforce forecasting | Requires trustworthy event/task history and careful governance. |
| Procurement forecasting | Needs reliable inventory/master data and observed demand. |
| Equipment readiness integration | Valuable but niche and device/CMMS dependent. |
| Quality/compliance reporting | Strong adjacency once audit data exists. |
| Clinical decision support | Only narrow, evidence-grounded, validated use cases after operational trust. |
| Security incident command workflow | Valuable but physical response/privacy dependencies require focused design. |

| Avoid as initial product | Why |
|---|---|
| Full HIS/EMR replacement | Long implementation, incumbent entrenchment, diffuse scope and weak wedge. |
| Autonomous diagnosis, prescribing or triage | Safety/regulatory/validation burden and high liability; violates human-governed sequencing. |
| Generic chatbot for hospital staff | Weak workflow lock-in, hallucination risk, no measurable operational outcome. |
| Consumer medical-debt app | Different distribution, regulatory and customer economics from hospital operations. |
| Payer-only prior-auth platform | Requires payer integrations and competes in a mature, jurisdiction-specific market. |
| CCTV emotion/violence surveillance as v1 | Privacy, bias, procurement and physical-response risk; solve state/communication first. |
| Blockchain-first consent product | Immutable storage does not solve incomplete capture, workflow ownership or retrieval. |

---

## 12. Founder insights

### What repeated research misses
1. **The unit of failure is not a feature; it is an unresolved cross-role exception.** A missing report, signature, clearance, bed, payer field or family update becomes expensive because nobody owns the next action across systems.
2. **“Interoperability” is not the customer outcome.** The outcome is a completed discharge, clean claim, accepted referral or acknowledged result; integration is the enabling substrate.
3. **The hospital’s real state lives outside the HIS.** It is distributed across paper, calls, PDFs, verbal handoffs, device systems, WhatsApp and staff memory.
4. **Revenue-cycle defects are frequently created upstream in care operations.** An appeal tool sees the symptom; a discharge-to-claim work graph can prevent part of it.
5. **Workforce shortage is amplified by coordination debt.** Better execution does not replace hiring, but it removes wasteful cognitive and clerical load.
6. **Patient trust is operational telemetry.** Missing updates and uncertain timelines predict desk load, conflict and reputation risk; it should not be relegated to a CRM.
7. **A dashboard without an owner is observational software.** The moat comes from task assignment, SLA/escalation and proof of completion.
8. **AI’s credible advantage is translation and prioritisation, not unsupervised medical authority.** Documents, policies and workflow status are the immediate high-value input space.
9. **The India-specific advantage is messy heterogeneity.** A product that works with mixed systems, rules, languages and intermittent connectivity can be globally relevant.
10. **The best initial buyer coalition is COO + CFO + CNO, with CIO as design authority.** A doctor-only buyer does not own the cross-department workflow; a CIO-only sale has no outcome urgency.

### Recurring assumptions to reject
- “More AI features” will solve operational fragmentation.
- A new EHR is necessary before automation can create value.
- High document frequency alone establishes willingness to pay.
- A clinically impressive model automatically fits a hospital workflow.
- Payer denial is purely a billing-team issue.
- Surveillance is the primary answer to violence; information, throughput and response ownership are upstream.
- AI-generated documentation is complete unless a human review process makes it so.

### Boring infrastructure with the highest moat
**A canonical, source-provenance patient-journey event graph plus a configurable task/state engine.** It is less glamorous than diagnosis, but it lets the same underlying capability power discharge, claims, bed turnover, referrals, result follow-up, patient updates, audits and staffing intelligence.

---

## 13. Top 10 biggest founder mistakes

1. Building a chatbot before mapping the workflow state machine and accountable roles.
2. Attempting to replace the HIS/EMR in the first sale.
3. Selling a dashboard with no work queue, ownership or escalation mechanism.
4. Treating OCR/LLM extraction as fact rather than a confidence-scored, reviewed source candidate.
5. Automating clinical, coding or claim decisions without appropriate human approval and auditability.
6. Starting with a US workflow and merely translating the interface for India.
7. Ignoring the COO/CFO/CNO coalition and selling only to individual clinicians.
8. Counting pilots/AI usage instead of discharge time, claim readiness, rework and task closure.
9. Collecting broad PHI before a specific workflow, access model, retention policy and value exchange exist.
10. Adding every department before proving one repeated cross-functional workflow at one hospital type.

## 14. Top 10 implications the reports strongly support but do not always state explicitly

1. The hospital needs a workflow/state layer between systems of record and humans doing the work.
2. The first defensible dataset is not medical notes; it is labelled operational exceptions and their resolution paths.
3. Discharge is a strategic “join” between care quality, bed capacity, patient experience and revenue.
4. Claim quality starts at encounter capture and handoff—not at the billing desk.
5. The same missing-event logic can prevent both patient delay and financial leakage.
6. Trust can be operationalised through accurate, time-bound status and traceable events.
7. Offline-first design is a distribution and reliability advantage, not merely a rural feature.
8. Workflow configuration is a product capability; custom services must not become the delivery model.
9. A hospital chain creates a future data advantage only after tenant-level trust and workflow adoption are earned.
10. The winning AI product will make humans more accountable and less burdened, rather than pretend to remove responsibility.

---

## 15. Board-level recommendation

### Recommended product vision
**Build JARVIS as the Healthcare Operations Fabric for fragmented hospitals: a source-provenance event graph and AI-assisted execution layer that closes cross-department patient, discharge and revenue workflows.**

### Recommended MVP
**Discharge-to-Claim Command Center** in 50–300-bed Indian multi-specialty hospitals, with document intelligence, role worklists, task ownership/escalation, discharge/bed-turnover coordination, and human-reviewed claim/scheme evidence readiness.

### The one-company answer

> **If I had to build only ONE company from this entire corpus, I would build JARVIS as a hospital operations fabric—beginning with discharge-to-claim orchestration—because the most repeated and economically consequential failures are created by fragmented data and unowned handoffs across care, capacity and revenue; a shared event-and-execution layer can solve those failures repeatedly, compound into workflow lock-in and proprietary exception-resolution data, and grow into the hospital’s operational nervous system.**
