# Phase 5 — Healthcare Intelligence Run Prompt
`v1.0.0` · 🔒 **Requires AUDIT-PASSED** · One domain per run

---

## Why healthcare gets its own phase

Generic AI analysis does not transfer to clinical settings. The buyer is different, the safety bar is different, the data model is different, and the consequence of failure is different. A wrong answer in a productivity tool is an annoyance; a wrong answer in a medication workflow is a patient safety event.

## Context

✅ Phase 0 constitution — especially `05-healthcare-ontology.md`
✅ Phase 2 dossiers (L10/L11 entities) · Phase 3 layer reports · Phase 4 technology reports
⚠ Baseline workflow list only
❌ JARVIS repo / dissection / blueprint

---

## Deliverable per domain

### For standards (`STD-{{NAME}}.md`)
Governance · adoption reality vs. mandate · conformance testing · extension mechanism · **implementation difficulty** · terminology mapping burden · capture risk · JARVIS conformance requirement.

### For workflows (`WF-{{NAME}}.md`)
Actors · steps · systems touched · data produced · pain points ranked by cost · **who has automated this already** · where the human checkpoint must sit · adapter ladder placement · India-specific variation.

### For systems (`SYS-{{NAME}}.md`)
Function · market position · integration surface · **adapter ladder rank with justification** · data model · switching cost · India presence.

---

## Domains to run

### Standards — priority 1
`FHIR R4` · `HL7 v2.x` · `ABDM (full stack: ABHA/HFR/HPR/HIE-CM/UHI/NHCX)` · `SNOMED CT` · `LOINC` · `DICOM` · `ICD-10/11`

### Workflows — priority 1
**`OPD / outpatient flow`** · `Clinical documentation` · `Order management` · `Diagnostics` · `Pharmacy` · `Revenue cycle & claims`

### Workflows — priority 2
`IPD / inpatient` · `Emergency` · `Operating theatre` · `ICU` · `Discharge` · `Administrative & accreditation`

### Systems — priority 1
`EMR/EHR` · `HIS/HMIS` · `LIS` · `Practice management` · `Insurance/TPA`

### Systems — priority 2
`RIS/PACS` · `Pharmacy systems` · `Healthcare ERP`

---

## Questions every report must answer

1. What is the **mandated** state vs. the **actual** state? (These diverge enormously in Indian healthcare.)
2. Who actually uses this, at what tier of facility?
3. What does integration genuinely cost — including terminology mapping?
4. Where must the human checkpoint sit?
5. What is the failure mode, and what is its clinical consequence?
6. **Is this measuring ABDM connectivity or actual digital maturity?**

> Question 6 is the recurring trap. A facility can create ABHA IDs and link records while running on paper and WhatsApp. The gap between "ABDM-connected" and "digitally mature" is where the real opportunity lives — and conflating them is the most likely strategic error in the entire healthcare thesis.

---

## Non-negotiable framing

Per `05-healthcare-ontology.md` §5, every report touching clinical action must specify:

1. Human-in-the-loop checkpoint location
2. Provenance requirement — one-step traceability to source record
3. Uncertainty surfacing — calibration is a safety feature
4. Audit trail — who/what/when/why for every read and write
5. Fail-safe default — stop and escalate, never guess forward
6. Consent enforcement at architecture level, not application level
7. Data residency

**These are also the moat.** Slow, unglamorous, expensive to retrofit — which is exactly why fast-moving generic agent companies skip them, and exactly why doing them well is defensible.

---

## Exit criteria
- [ ] All priority-1 standards, workflows and systems covered
- [ ] Adapter ladder placement justified for every system
- [ ] Mandated vs. actual state distinguished throughout
- [ ] Human checkpoint located for every clinical workflow
- [ ] Terminology mapping burden quantified
- [ ] India tier-2/3 reality addressed, not just large-chain reality
