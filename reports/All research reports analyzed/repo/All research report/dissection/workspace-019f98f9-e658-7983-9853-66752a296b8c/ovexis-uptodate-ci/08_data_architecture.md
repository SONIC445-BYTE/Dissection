# DELIVERABLE 8 — Healthcare Data Architecture Map

Confidence legend: 🟢 Confirmed | 🟡 Strong Inference | 🔴 Speculation | ⚪ Cannot Verify

UpToDate's data architecture is — by design — a **one-way evidence-distribution network**, not a patient-data system. This file maps every interoperability dimension: what exists, what is deliberately absent, and the inferred internal architecture of the corpus itself.

---

## 8.1 Standards & interfaces inventory

| Domain | UpToDate position | Detail | Conf. |
|---|---|---|---|
| **HL7 v2 Infobutton** | ✅ Core standard | Context-aware knowledge requests from EHR (problem list, meds, labs, allergies); Epic/Oracle Health/InterSystems all documented | 🟢 |
| **FHIR** | 🟡 Limited/partner-level | No public FHIR API for UpToDate content; FHIR appears via partners (Epic CDS Hooks ecosystems, Abridge) rather than native UpToDate resources. WK job posts reference modern integration work but no public UpToDate FHIR endpoint | 🟢 (absence) / 🟡 |
| **CCDA / CCD** | ❌ None public | No document-based exchange; UpToDate never ingests patient records | 🟢 |
| **Apple Health / Health Connect** | ❌ None | No consumer-health ingestion anywhere | 🟢 |
| **Wearables** | ❌ None | — | 🟢 |
| **Labs (LOINC)** | 🟡 Terminology-level | Health Language (2013 acquisition) maintains terminology mapping (ICD/SNOMED/LOINC-style assets) used across WK systems; UpToDate topics reference lab interpretation curated by experts, not coded streams | 🟢 acquisition / 🟡 use |
| **Imaging (DICOM)** | ❌ None | Educational graphics only; no imaging intake | 🟢 |
| **Genomics** | 🟡 Content-level | Pharmacogenomics database inside Lexidrug; no patient genotype ingestion | 🟢 |
| **Pharmacy (NCPDP etc.)** | ✅ Indirect | Medi-Span drug data feeds dispensing/e-prescribing systems industry-wide | 🟢 |
| **Insurance/claims (X12)** | ❌ None | — | 🟢 |
| **Patient identity (MPI)** | ❌ None by design | No patient identity layer exists; user identity = clinician account or institutional entitlement | 🟢 |
| **Consent architecture** | 🟡 Clinician-side only | T&Cs, privacy policy, professional-use disclaimers; enterprise governance controls for Expert AI; **no patient consent primitives** | 🟢 |

---

## 8.2 The corpus data model (reverse inferred)

🟡 The crown jewel is not patient data but the *editorial knowledge graph*:

```
Topic (13,000+)
 ├── Sections (canonical order: definition → epidemiology → ... → management → prognosis)
 ├── Graded Recommendations (strength × certainty, linked to references)
 ├── Citations → PubMed-linked references (abstracts)
 ├── Entities: drugs (Lexidrug IDs), conditions, procedures, labs, calculators
 ├── Graphics/Algorithms (asset library with alt metadata)
 ├── PatientEd mirrors (plain-language variants keyed to topic)
 └── Version history (continuous publishing; per-section timestamps)
```

- 🟡 Health Language provides the terminology backbone (synonym/code mapping) that lets a drug entity reconcile across UpToDate topic, Lexidrug monograph, and Medi-Span dataset — corroborated (Nov 2025) by the *harmonisation* work marketing for Expert AI drug answers ("fully harmonised with UpToDate content... avoid contradictions").
- 🟡 Expert AI retrieval required this corpus to become machine-consumable: chunked, entity-resolved, version-stamped, source-addressable. The Nov-2025 Lexidrug integration is public proof of an internal **unified retrieval schema** project.
- 🔴 Likely future artefact: an **Evidence Graph API** — topics as queryable knowledge objects with GRADE metadata. If offered, it would be the first true developer product; none exists publicly (⚪).

## 8.3 Data flows (operational)

| Flow | Direction | Conf. |
|---|---|---|
| Journals/guidelines → authors/editors → updated topics → CDN → clinician eyeballs | In → curate → out (read) | 🟢 |
| Usage/query logs → editorial analytics → commissioning priorities | telemetry in | 🟡 (process confirmed in principle: editorial policy references user feedback; analytics-loop depth inferred) |
| Search events → CME ledger → credit redemption | telemetry in | 🟢 |
| EHR context (diagnosis/med/lab terms) → Infobutton → search results | context in, evidence out, **no persistence** | 🟢 |
| Enterprise AI sessions → governance logs | telemetry in | 🟢 (marketing claim of governance) |

🟢 **Decisive observation:** every patient-context touchpoint is **transient** — Infobutton inputs are query parameters, not stored records. There is no PHI lake on the UpToDate side by architecture. This is simultaneously their regulatory safety (minimal HIPAA footprint beyond usage telemetry) and their ceiling (no longitudinal value can compound).

## 8.4 Normalisation / deduplication

🟡 In-corpus normalisation: editorial style engine + terminology services enforce uniform drug names, units, and section schemas (visible in output consistency). Cross-corpus dedup is the harmonisation program (Lexidrug↔UpToDate contradiction management). 🟢 Patient-level normalisation/deduplication/entity resolution: **none — no patient data exists to normalise.**

## 8.5 What this architecture means for Ovexis

| Asset UpToDate has | Asset Ovexis must build differently |
|---|---|
| Human-graded corpus + terminology backbone | Machine-graded personal evidence layer that *consumes* such corpora as one source among many (guidelines, claims, labs, wearables) |
| Terminology services (Health Language-type) | FHIR-native normalisation pipeline: USCDI resources, LOINC labs, RxNorm meds, SNOMED conditions, unit harmonisation, device mapping (Apple Health, Health Connect, CGM) |
| Zero PHI posture | Consent-native PHI lakehouse: per-user encryption, purpose-limited access, patient-mediated sharing — this is a different regulatory and engineering posture, and it's the cost of admission for longitudinal intelligence |
| Transient context (Infobutton) | Persistent context ("patient digital twin") updated in near-real-time |

🟢 UpToDate's architectural choices are *rational for a publisher* and *fatal for a longitudinal platform*. Interoperability for them = being callable; for Ovexis it must = continuously listening.
