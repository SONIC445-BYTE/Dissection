# DELIVERABLE 18 — Feature Dependency Graphs

Confidence legend: 🟢 Confirmed | 🟡 Strong Inference | 🔴 Speculation
Scripts in Mermaid. Confidence applies to the existence of dependencies; internal wiring is 🟡 where reconstructed.

---

## 18.1 UpToDate's actual dependency graph (reconstructed)

```mermaid
graph TD
  J[Journals, guidelines, FDA feeds] --> AUTH[7,600 expert authors/editors]
  AUTH --> EDIT[Editorial pipeline: deputy editors, section editors, grading team]
  EDIT --> CORPUS[Graded corpus · 13k topics · continuous publishing]
  TERMS[Terminology services · Health Language] --> CORPUS
  DRUG[Lexidrug drug database] --> CORPUS
  CORPUS --> SEARCH[Search engine · autocomplete · Key Points]
  CORPUS --> TOPIC[Topic pages · GRADE chips · calculators · graphics]
  DRUG --> INTERACT[Interaction analysis · Rx Transitions · kidney dosing]
  CORPUS --> RAG[Retrieval layer · chunking · knowledge bases]
  RAG --> EAI[Expert AI agent · multi-model router · validators]
  EDIT --> EAI[Human oversight loop]
  EAI --> TRI[Transparency triad: Assumptions · Sources · Reasoning]
  TOPIC --> CME[CME ledger → AMA PRA redemption]
  SEARCH --> CME
  EAI --> GOV[Enterprise governance logs]
  ID[Identity: SSO · IP · OpenAthens · seats] --> SEARCH
  ID --> CME
  EHR[Epic/Oracle/InterSystems Infobutton] --> SEARCH
  CME --> RET[Retention & renewal]
  TRI --> RET
  RET --> REV[Institutional & individual license revenue]
  REV --> EDIT[Editorial payroll funded]
  EAI --> ABR[Abridge evidence-at-documentation · partner API]
```

**Key dependency insight (🟢):** UpToDate's graph is a **star around CORPUS**: remove the corpus and every node dies. There is no upstream patient-data spine.

## 18.2 The architectural counter-graph Ovexis needs (consent → identity → data → AI → insights → clinician ↔ patient)

```mermaid
graph TD
  CONSENT[Granular consent engine · purpose-limited · revocable] --> PID[Patient identity · MPI-grade resolution · dedup]
  PID --> INGEST[Ingestion · FHIR R4/R5 · SMART on FHIR · Apple Health · Health Connect · labs · pharmacy · imaging metadata · PDFs/OCR]
  INGEST --> NORM[Normalisation: RxNorm, LOINC, SNOMED, UCUM units, timezone/device mapping]
  NORM --> DDUP[Deduplication & entity resolution · provenance graphs]
  DDUP --> TWIN[Longitudinal patient twin · event-sourced timeline · feature store]
  TWIN --> EVID[Evidence layer · guidelines/corpus adapters · GRADE-weighted citations]
  TWIN --> AGENT[Ovexis agent: hybrid retrieval over twin + evidence · risk models]
  EVID --> AGENT
  AGENT --> VAL[Validators: source-support, interaction checks, red-flag escalation, confidence gating]
  VAL --> REPORTS[Clinician-grade reports · lineage panels · datestamped]
  REPORTS --> INSIGHT[Patient insights · nudges · shared care plan]
  INSIGHT --> DOC[Physician workspace · pre-visit brief · in-visit assist]
  DOC --> FB[Clinician feedback → model & content improvement]
  INSIGHT --> PAT[Patient app · explainable insights · questions to ask]
  PAT --> FB
  FB --> TWIN
  REV2[Subscriptions: patient freemium → premium; clinician per-panel; enterprise] --> ENG[Engineering & clinical safety ops]
  ENG --> CONSENT[Consent engine maintained]
```

**Dependency-strategy notes:**
- 🟡 Consent must sit *below* identity below ingestion: inverting it (scrape first, ask later) is the industry's chronic HIPAA/GDPR failure mode.
- 🟡 The twin is the only node from which value compounds: every added data source raises insight density super-linearly — the opposite topology from UpToDate's flat corpus star.
- 🟢 This graph mirrors the exact sequence required by the brief (Consent↓Identity↓Data Collection↓Normalisation↓AI↓Reports↓Insights↓Doctor↓Patient) and adds the feedback loop that turns usage into better models (the network-effect seed).
