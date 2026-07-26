# Atropos Health — Architecture and Journey Diagrams

## Product Architecture Diagram

```mermaid
flowchart TD
Website[Marketing Site] --> Portal[Evidence Portal]
Portal --> Auth[Auth0 / SSO]
Portal --> Orders[Order Workflow]
Portal --> Search[Library + AI Search]
Portal --> Projects[Projects / Cases]
Orders --> ChatRWD
Orders --> GreenButton
Orders --> Forge
Search --> Alexandria
ChatRWD --> Geneva[GENEVA OS]
GreenButton --> Geneva
Forge --> Geneva
Geneva --> Network[Evidence Network]
Geneva --> Local[Customer Cloud Data]
Geneva --> Quality[RWDS / RWFS]
Geneva --> Reports[Reports / pRWE / pEBF]
Reports --> Agent[Evidence Agent]
Agent --> EHR[EHR / ChatEHR]
Agent --> Dragon[Microsoft Dragon Copilot]
Agent --> Teams[Microsoft Teams]
Agent --> Databricks[Databricks MCP]
```

## AI Architecture Diagram

```mermaid
flowchart TD
Q[Clinical question or patient context] --> P[Question normalization / PICOT / phenotype mapping]
P --> RAG[Literature + guideline + Alexandria retrieval]
P --> RWD[RWD cohorting + statistical pipeline]
RWD --> Study[Observational study artifacts]
RAG --> Synth[LLM synthesis]
Study --> Synth
Synth --> Eval[Answered with Evidence evaluation]
Eval --> Badge[Quality badge and rationale]
Badge --> Human[Optional clinician / expert review]
Human --> Workflow[EHR / Teams / Portal / report]
```

## Healthcare Data Flow Diagram

```mermaid
flowchart LR
A[EHR / EMR] --> N[GENEVA OS]
B[Open and closed claims] --> N
C[Labs / vitals / Rx / CPT / ICD] --> N
D[Registries] --> N
E[Clinical notes / curated unstructured data] --> N
F[Specialty networks] --> N
G[Google HDE / BigQuery / Databricks / AWS] --> N
N --> T[Patient timeline objects]
T --> Q[ACE / TQL cohorting]
Q --> S[Automated analytics]
S --> R[Reports / pRWE / pEBF]
R --> U[Clinicians / researchers / life sciences / agents]
```

## User Journey Diagram

```mermaid
flowchart TD
A[Anonymous visitor] --> B[Evidence gap homepage]
B --> C[Persona solution page]
C --> D[Talk to sales / Request demo / Sign up]
D --> E[Auth0 login or signup]
E --> F[Email / Google / Instant Health Data / Stanford SSO]
F --> G[Onboarding: profile, terms, plan/pricing]
G --> H[Dashboard / Library / Order]
H --> I[Question type]
I --> J[Clinical question]
J --> K[PICOT + AI suggestions + phenotypes]
K --> L[Dataset selection + fitness]
L --> M[Submit or run ChatRWD/Forge]
M --> N[Pending / in progress / complete]
N --> O[Report / evidence summary / artifacts]
O --> P[Download / feedback / request review]
P --> Q[Rerun / reorder / project workspace]
Q --> R[Subscription / enterprise expansion / renewal]
```

## Feature Dependency Graph

```mermaid
flowchart TD
Consent[Consent / agreement / de-id basis] --> Identity[Identity resolution / hash / de-ID]
Identity --> Collection[EHR, claims, labs, registries]
Collection --> Normalize[ICD, CPT, RxNorm, LOINC, timelines]
Normalize --> Fitness[RWDS / RWFS]
Fitness --> Cohort[ACE / TQL / phenotypes]
Cohort --> Analytics[Statistics / observational templates]
Analytics --> AI[LLM orchestration / RAG]
AI --> Review[Answered with Evidence / AI review / clinician review]
Review --> Reports[Reports / pRWE / pEBF]
Reports --> Workflow[EHR / portal / Teams / Dragon / Databricks]
Workflow --> Action[Doctor / researcher / pharmacy / pharma]
Action --> Feedback[Feedback / rerun / reorder]
Feedback --> Analytics
```
