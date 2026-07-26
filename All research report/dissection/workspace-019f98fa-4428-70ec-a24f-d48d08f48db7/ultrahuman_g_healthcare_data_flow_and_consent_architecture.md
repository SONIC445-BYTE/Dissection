# Report G — Healthcare Data Flow and Consent Architecture

```mermaid
flowchart LR
 U[User] --> C[Granular consent]
 C --> I[Identity resolution]
 I --> S[Source connectors]
 S --> D[Raw immutable data]
 D --> P[Provenance and data quality]
 P --> N[Normalized health model]
 N --> L[Longitudinal record]
 L --> A[AI / rules / analytics]
 A --> V[User view]
 A --> H[Patient-authorized clinician view]
 H --> F[FHIR / export / care coordination]
 C --> R[Revocation and retention policy]
 R --> D
```

## Required controls

- **🟡 Strong Inference.** Consent must be purpose-specific: personalization, research, clinician sharing, employer reporting, and model improvement should not be one bundled checkbox.
- **🟡 Strong Inference.** Every derived insight should retain source observations, algorithm version, timestamp and confidence.
- **🟡 Strong Inference.** Revocation should stop future processing and trigger a documented downstream deletion or de-identification process where legally permitted.
- **🟢 Confirmed.** Ultrahuman’s public policy states that data is encrypted at rest and in transit and discusses cross-border processing and GDPR. [R12](https://www.ultrahuman.com/us/privacyPolicy/)
- **🟢 Confirmed / not publicly verified.** Ultrahuman’s full FHIR/HL7/CCDA, hospital, payer, pharmacy and imaging architecture was not publicly verified.

---
