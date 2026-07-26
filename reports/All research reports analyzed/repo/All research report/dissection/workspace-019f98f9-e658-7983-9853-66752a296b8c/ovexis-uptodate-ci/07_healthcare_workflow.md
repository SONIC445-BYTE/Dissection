# DELIVERABLE 7 — Healthcare Workflow Reverse Engineering

Confidence legend: 🟢 Confirmed | 🟡 Strong Inference | 🔴 Speculation | ⚪ Cannot Verify

Scope: how UpToDate touches each real-world healthcare workflow, where its influence stops, and what Ovexis can infer about owning the untouched remainder.

---

## 7.1 Clinical workflow (point of care)

🟢 **Insertion points (verified):**
1. **Pre-encounter:** physician searches differentials/management; reviews algorithms.
2. **In-encounter:** Epic/Cerner Infobutton from problem list/med/lab context launches targeted UpToDate search; Key Points give zero-click answers; calculators run; drug interactions checked.
3. **Post-encounter:** deeper read; CME accrual; patient education printed/emailed.
4. **Ambient (2024–2026):** within Abridge documentation sessions, UpToDate-powered context-aware CDS surfaces inside the note — the workflow has moved from *physician pulls* to *system pushes relevant evidence during documentation*.

🟡 **Mechanics that matter:** UpToDate's workflow leverage comes from zero-decision insertion: no login, 90-second answer, then exit. Its session is *episodic* (question-bounded). It never owns the encounter; it annotates it.

## 7.2 Patient workflow

🟢 Footprint: leaflets ("The Basics"/"Beyond the Basics"), Emmi interactive multimedia programs (procedure prep, chronic coaching; opioid use programs documented), patient education in 19 languages.
🟢 Hard limit: patient never authenticates, never uploads, never returns — no loop. 🟡 Implication: UpToDate's patient workflow is **broadcast**; there is no telemetry on whether patients read, understood, or adhered.

## 7.3 Provider workflow (ambulatory/clinic)

- 🟢 Group subscriptions (2–19 seats) self-serve via store; enterprise ≥20 via sales.
- 🟢 Mobile + desktop across clinic, home, on-call; 2-device policy.
- 🟡 CME funds create buyer nexus: practice funds replace hospital license.
- 🟡 No practice-management, scheduling, or inbox integration — UpToDate resists owning operational surfaces.

## 7.4 Hospital workflow

- 🟢 Enterprise license + SSO + EHR integration kits (Epic/Oracle Health/InterSystems); librarian-administered usage reporting; Promoting Interoperability support via linked CDS.
- 🟢 Pharmacy layer: Lexidrug/Medi-Span inside order verification; Sentri7 inpatient surveillance flags (opioid safety programs documented).
- 🟢 Governance layer (2025+): Expert AI admin policies for AI oversight committees.
- 🟡 Institutional politics observed: renewals are budget-line knife-fights (CFO vs CMO); UpToDate uses physician-preference pressure as leverage ("doctors revolt if removed" — supported by Reddit revolt evidence).

## 7.5 Insurance / payer workflow

🟢 Adjacent, not core: "UpToDate for Healthcare Businesses" SKU serves payers/pharma/CROs as knowledge seats. 🟡 Medi-Span powers formulary/benefit checks inside payer/pharmacy stacks (drug data is infrastructure across the industry). 🔴 No evidence of prior-authorisation automation plays by UpToDate — a top-3 hospital AI-priorities area they have ceded to others.

## 7.6 Lab workflow

🟢 Interpretation content (lab test topics, calculators). 🟡 No LIS integration; no result-level flagging — labs are *explained*, never *ingested*. Gap.

## 7.7 Pharmacy workflow

🟢 Deepest non-reference workflow: Lexidrug monographs, IV compatibility, pharmacogenomics database, shortage intelligence; Medi-Span datasets embedded in dispensing systems; interaction screening at dispense; offline pharmacist app. 🟡 Pharmacy is the template for WK's "content as infrastructure" strategy — drug data already behaves like an API business; clinical content is next (Expert AI/Abridge).

## 7.8 Referral workflow

🟢 Content support only (when-to-refer guidance in topics). No referral network, no provider directory, no order routing. Gap.

## 7.9 Medical records / clinical documentation

- 🟢 UpToDate does not write to the record — until Abridge. The Abridge integration is the first mechanism by which UpToDate-derived recommendations can *land inside generated notes* (GA March 2026, all Abridge customers).
- 🟡 Copy-citation behaviour: clinicians paste graded recommendations into notes as defensive documentation (observed culture, inferred scale).
- 🟢 CME documentation flow (reading → credit → transcript export) is the only "documentation" UpToDate itself generates.

## 7.10 Care coordination

⚪ Essentially absent: no shared care plans, no task routing, no secure messaging, no longitudinal adherence tracking. Emmi offers patient program assignment, which is the closest artefact. 🟡 This absence is architectural philosophy ("evidence layer, not workflow layer") — and it defines the entire Ovexis opportunity map.

---

## 7.11 Workflow synthesis — the "UpToDate donut"

```
        ┌────────────────────────────────────────────┐
        │  UpToDate touches: ASK → ANSWER → CITE      │
        │  (question in, evidence out, credit logged) │
        └────────────────────────────────────────────┘
   Everything else — capture, record, order, document, coordinate,
   monitor, follow up, adhere — happens OUTSIDE the product.
```

🟢 Confirmed by integration inventory: every integration is *read-side* (Infobutton, search embed, Abridge evidence) except data licenses (Medi-Span out). **Read-only architecture = bounded liability + bounded value.** Ovexis's wedge is the write-side and longitudinal-side workflows UpToDate will not touch without becoming a regulated device-adjacent workflow vendor — a line their legal posture has so far refused to cross. 🟡
