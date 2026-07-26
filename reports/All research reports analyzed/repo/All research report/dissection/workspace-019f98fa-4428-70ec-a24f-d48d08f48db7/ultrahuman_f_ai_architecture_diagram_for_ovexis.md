# Report F — AI Architecture Diagram for Ovexis

```mermaid
flowchart TB
 S[Source data] --> V[Validation, units, provenance]
 V --> G[Longitudinal health graph]
 G --> F[Feature store and temporal windows]
 F --> R[Rules and clinical safety engine]
 G --> E[Evidence retrieval]
 F --> C[Causal / statistical models]
 R --> L[Constrained language model]
 E --> L
 C --> L
 L --> U[User explanation with citations]
 U --> P[Patient action plan]
 U --> D[Clinician summary]
 P --> O[Outcome tracking]
 O --> G
 R --> H[Human review / escalation]
```

- **🟡 Strong Inference.** This architecture is recommended for Ovexis because it separates measurement, inference, evidence, language generation and safety.
- **🟡 Strong Inference.** LLMs should not directly calculate medical metrics, fabricate missing values, make unreviewed diagnoses or change medications.
- **🟡 Strong Inference.** Required evaluation metrics include factuality, citation correctness, temporal reasoning, calibration, subgroup performance, abstention quality, harmful-advice rate and action outcomes.
- **🟢 Confirmed / not publicly verified.** Ultrahuman’s specific LLMs, RAG, agent design, prompts and evaluation system are not publicly disclosed in the reviewed sources.

---
