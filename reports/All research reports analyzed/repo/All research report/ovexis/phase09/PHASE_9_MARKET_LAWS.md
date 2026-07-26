# PHASE 9 — MARKET LAWS
## Twelve Immutable Principles, Each Multi-Source Evidenced

**Phase:** 9 of 16 (+ Ω) · **Date:** 2026-07-26 · **Status:** COMPLETE — canonical
**Outputs:** `exports/phase9_market_laws.{json,yaml,csv}`

Derivation continued until no further law emerged that met the evidence bar (multiple independent reports **or** primary datasets). Twelve laws survived; the brief's four proposed examples are among them, now measured rather than asserted.

---

## THE TWELVE LAWS

### LAW 1 — Hospitals rarely replace their core system of record `HIGH`
**Evidence:** `bot_incumbent_lockin` GREEN, 16 companies, 209 hits, corroborated on both geography and artifact class (Phase 5); 0 of 19 companies occupy the SoR (Phase 2 F-2.4); balancing loop B2 (Phase 8).
**Implication:** Build beside the HMIS, never against it. *(DL-020)*

### LAW 2 — Software that cannot complete an action cannot learn from it `HIGH`
**Evidence:** the self-sealing R1 loop (Phase 8); 52.4% of product DNA before commit vs 12.9% at it (Phase 3); 149 fabricated adapters produced zero flywheel (Phase 8 F-8.2).
**Implication:** Execution is the *precondition* for improvement, not its reward. This is the deepest law in the set — it explains why the market's most-funded layer stopped improving.

### LAW 3 — Attention follows data availability, not labour intensity `HIGH`
**Evidence:** radiology 234 mentions vs nursing 10 (Phase 2 F-2.13); 0 of 449 ABDM platforms mention nursing (Phase 4); nursing ranks 25th of 25 for observation (Phase 6 F-6.3).
**Implication:** The largest gaps sit where no digital artifact exists. *(DL-040)*

### LAW 4 — Liability, not capability, bounds automation in healthcare `HIGH`
**Evidence:** all four highest-stakes work units score at the bottom on liability alone despite having artifacts and being technically approachable (Phase 6 F-6.4); human review survives for legal not quality reasons (Phase 7 F-7.5); loop B1 (Phase 8).
**Implication:** Liability allocation is a primary design variable. *(DL-041, DL-048)*

### LAW 5 — Standards govern exchange *between* institutions, never operations *inside* them `HIGH`
**Evidence:** 409 of 449 Indian platforms are FHIR-certified, yet ABDM M1/M2/M3 covers zero of OT scheduling, bed state, rostering, charge capture, claim scrubbing (Phase 7 F-7.3).
**Implication:** Internal operations are permanently API-poor — the durable home for computer-use automation. *(DL-046)*

### LAW 6 — Consumer subscription is the fallback of companies blocked from institutional revenue `MEDIUM-HIGH`
**Evidence:** 19 of 21 artifacts discuss reimbursement while nearly all bill consumers (Phase 2 F-2.7); churn and CAC both GREEN at 11 companies (Phase 5 F-5.4); trap loop R4 (Phase 8).
**Implication:** Enter on the operational budget, which requires no clinical validation.

### LAW 7 — Trust is manufactured by traceability, not by accuracy claims `HIGH`
**Evidence:** provenance 55 / citation 55 / editorial 50 dominate all trust language (Phase 2 F-2.11); `ai_citation_grounding` GREEN at 17 companies (Phase 5); trust primitives strengthen under autonomy (Phase 7 F-7.4).
**Implication:** Provenance is the product, not overhead. *(DL-047)*

### LAW 8 — Every layer above the clinician can approve a purchase; only the clinician creates value `MEDIUM`
**Evidence:** CIO 13, CFO 9, committee 8, **CMIO 1** across the entire corpus (Phase 2 F-2.10).
**Implication:** Procurement is necessary and insufficient. Confidence is MEDIUM because the corpus itself under-samples clinical veto — the law is inferred partly *from* that absence.

### LAW 9 — Workflow continuity is inversely proportional to institutional depth `MEDIUM-HIGH`
**Evidence:** patient journey — 16 stages, 12.2 owners, break rate **0.00**; ICU/emergency/administration/management — break rate **1.00** (Phase 4 F-4.7).
**Implication:** Opportunity is measured by break rate, not participant count. *(DL-029)*

### LAW 10 — The most crowded capability is usually the least defensible `MEDIUM-HIGH`
**Evidence:** `analytics_dashboard` is the most built concept (16 companies) and a pure legacy artifact; gamification 12, conversion 11, onboarding 7 — all compensating for pre-AI limitations (Phase 7 F-7.1).
**Implication:** Crowding is a signal that a capability compensates for a constraint that no longer exists. *(DL-045)*

### LAW 11 — Fragmentation of supply raises the value of the interface layer `MEDIUM-HIGH`
**Evidence:** 253 HMIS vendors in India vs ~5 in the US (Phase 2); UI automation claimed by 2 of 21 artifacts (F-2.9); avoidance loop R3 (Phase 8).
**Implication:** India structurally favours adapter strategies. *(DL-018)*

### LAW 12 — Government rails create counterparty networks before products exist `HIGH`
**Evidence:** live probe — NHCX 38 partners including 12 insurers and 4 TPAs; ABDM 445 partners with a free unauthenticated API (Phase 6, Phase 2).
**Implication:** In India the network precedes the product; in the US it must be bought. This is the strongest single argument for India-first sequencing.

---

## LAWS THAT DID NOT SURVIVE

Candidates rejected for failing the multi-source bar:

| Proposed | Why rejected |
|---|---|
| *"Doctors adopt software that saves time immediately"* | `bot_clinician_capacity` = **2 hits corpus-wide** (Phase 5). The corpus does not actually measure clinician time. Plausible, unevidenced here. |
| *"Integrations compound in value"* | `bot_integration_effort` = 14 hits. Asserted by the brief; not measurable in this evidence. |
| *"Pricing power follows clinical validation"* | All 7 pricing patterns failed corroboration (Phase 5 F-5.3). No basis. |
| *"Workflow beats features"* | True in spirit, but unfalsifiable as stated — folded into LAW 9. |

Recorded rather than quietly dropped, per protocol.

---

## DELIVERABLES

**🟢 Verified:** 12 laws, each multi-source; 6 HIGH, 5 MEDIUM-HIGH, 1 MEDIUM. Four proposed laws rejected for insufficient evidence.

**⚠️ Contradiction C-29:** The brief proposed *"Doctors adopt software that saves time immediately"* as LAW 2 ↔ the corpus contains almost no clinician-time evidence. **Resolution:** the brief's instinct is likely correct; this corpus cannot support it (DL-035 — these are go-to-market dossiers). Retained as a hypothesis for primary research, not promoted to law.

**❓ Unknowns:** Do LAWS 1–12 hold in the US as strongly as in India? LAW 5 and LAW 12 are India-verified; LAW 11 is explicitly geography-dependent.

**📒 DL-053:** Market laws are **binding constraints on all subsequent phases**. Any Phase 10–15 recommendation that violates a HIGH-confidence law must either be discarded or explicitly justify the exception.

**📊 Confidence — Phase 9: MEDIUM-HIGH.** Laws derived from measured findings across four independent methods; the weakest (LAW 8) is flagged as inferred partly from absence.

---

## PHASE 9 COMPLETE — proceeding to Phase 10.
