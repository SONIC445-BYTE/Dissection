# Report J — Engineering Roadmap Reconstruction

## Phase 0 — Foundation, 0–3 months

- **🟡 Strong Inference.** Identity, consent ledger, raw observation store, provenance, normalized metric model, audit logging and deletion workflow.
- **🟡 Strong Inference.** HealthKit/Health Connect and at least two wearable connectors.
- **🟡 Strong Inference.** Timeline, data-quality dashboard, confidence labels and manual correction.

## Phase 1 — MVP, 3–6 months

- **🟡 Strong Inference.** Sleep, movement, HR/HRV, glucose and lab timeline.
- **🟡 Strong Inference.** Weekly evidence-backed brief, not an unrestricted chatbot.
- **🟡 Strong Inference.** Patient-shareable report and PDF/CSV export.

## Phase 2 — Clinical bridge, 6–12 months

- **🟡 Strong Inference.** FHIR R4 export, provider portal, clinician summary, medication capture, red-flag escalation and care-plan tracking.
- **🟡 Strong Inference.** Research consent and de-identified cohort export.

## Phase 3 — Intelligence moat, 12–24 months

- **🟡 Strong Inference.** Causal self-experiments, intervention ledger, personalized baseline model, evidence graph and calibrated digital-twin components.
- **🔴 Speculation.** Predictive models for specific diseases should not be assumed until clinical validation and regulatory strategy are complete.

## Technical debt to avoid

- **🟡 Strong Inference.** Do not store only aggregated scores.
- **🟡 Strong Inference.** Do not let an LLM become the system of record.
- **🟡 Strong Inference.** Do not make source-specific schemas leak into product logic.
- **🟡 Strong Inference.** Do not hide data gaps behind interpolated charts.
- **🟡 Strong Inference.** Do not postpone consent, audit and deletion architecture.

---
