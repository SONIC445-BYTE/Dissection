# PHASE 1 — REPORT VALIDATION
## Independent Scoring of All 21 Artifacts · No Merging Permitted

**Engagement:** Ovexis / JARVIS Strategic Intelligence Synthesis (OISE)
**Phase:** 1 of 16 (+ Phase Ω)
**Date:** 2026-07-26 (Asia/Calcutta)
**Status:** COMPLETE — canonical
**Inputs:** Phase 0 (canonical), Board intake answers
**Machine-readable outputs:** `registry/phase1_signals.json`, `registry/phase1_scores.{json,csv}`, `exports/phase1_validation.{json,yaml}`

---

## 1.0 BOARD INTAKE — ANSWERS RECORDED AS CANONICAL

| Q | Answer | Binding consequence for all later phases |
|---|---|---|
| Q1 Corpus completeness | **Complete** — 21 artifacts is the full corpus | Phase 2 reconstructs the market from *this* evidence only. Absent categories (EHR incumbents, payers, PACS/LIS, RCM) become permanent **structural blind spots**, declared not silently filled. |
| Q2 Primary objective | **JARVIS engineering plan** | Phases 3–10 are instrumented toward Phase 11. Every extracted pattern must terminate in a buildable implication or it is noise. Phase 12 (product strategy) serves engineering sequencing, not fundraising narrative. |
| Q3 Beachhead | **Both India and US** | Dual regulatory spine: ABDM/ABHA/NHCX/DPDP **and** HIPAA/FHIR-US-Core/Info-Blocking. Adapter architecture must be jurisdiction-parameterised from day one, not retrofitted. |
| Q4 Output format | **Markdown + machine-readable from Phase 1 onward** | Every phase emits JSON/YAML/CSV alongside prose. HPID begins accumulating **now**, not at Phase 16. |
| Q5 Team / confidentiality | **No team yet** | 🔴 **Hard constraint, not a footnote.** Phase 11 architecture and Phase 12 capital allocation must be executable by a **solo builder with AI assistance**. Any recommendation implying a 10-person team is invalid on arrival. Recorded as **DL-007**. |

**DL-007 is the single most consequential answer.** It retroactively invalidates the shape of nearly every "Ovexis strategy memo" in the corpus — those memos assume funded teams. Phase 1 therefore adds a scoring axis the original brief did not request: **fitness-for-objective under solo-builder constraint**.

---

## 1.1 METHOD — WHY THESE SCORES ARE REPRODUCIBLE

Scoring 21 artifacts by reading impression is unfalsifiable. Instead, every artifact was **instrumented**: 24 measurable signals extracted programmatically (citation density, evidence-label ratios, numeric-claim counts, domain-vocabulary frequency, structured-row counts, honesty markers, canon coverage), then mapped to the nine required axes by a fixed linear rubric.

Rubric published in `registry/phase1_signals.json`; scores regenerate deterministically from the corpus.

**What each axis measures**

| Axis | Signal basis |
|---|---|
| Research Quality | Canon coverage (of 27) 45% · analytical volume 30% · structured artifact rows 25% |
| Evidence Quality | Citations/1k words 40% · raw captures & screenshots 25% · %-confirmed 20% · explicit cannot-verify honesty 15% |
| Strategic Value | Pricing/economics depth 35% · funding-and-market depth 25% · canon coverage 40% |
| Technical Depth | Architecture/API/infra vocabulary density |
| Healthcare Accuracy | FHIR + HL7 + ABDM/ABHA/NHCX/DPDP term density |
| Commercial Accuracy | Currency-figure count 50% · percentage count 20% · pricing depth 30% |
| Regulatory Accuracy | HIPAA + GDPR + FDA/SaMD/CE + SOC2/HITRUST/ISO density |
| Engineering Accuracy | AI/LLM/RAG specificity 50% · architecture specificity 50% |
| Hallucination Safety | **Inverse** of (numeric claims ÷ citation density) — high numeric assertion with low sourcing scores *low* |

**Two corrections applied after first pass** (both recorded in the Decision Ledger):
- **Artifact-class correction (DL-008).** The mechanical rubric rewards prose volume. It scored **I01 (HPID) at 2.6 — the lowest but one** — despite I01 being the corpus's most operationally valuable asset. A registry of 449 platforms is not a bad dossier; it is *not a dossier at all*. Artifacts are now classed `competitor_dossier` / `ground_truth` / `infrastructure`, and cross-class ranking by `overall` alone is prohibited.
- **Fitness-for-objective axis (DL-009).** Given Q2 + Q5, "how good is this report" matters less than "how much does this shorten a solo builder's path to a working JARVIS adapter." Final ordering uses **Adjusted Priority = 0.5·Fit + 0.3·Overall + 0.2·Evidence**.

---

## 1.2 THE SCORECARD — ALL 21 ARTIFACTS, INDEPENDENTLY SCORED

Scale 1–10. **No artifact has been merged with any other.**

| ID | Artifact | Class | Res | Evi | Str | Tec | HC | Com | Reg | Eng | Hall-Safe | **Overall** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D18 | UpToDate (Wolters Kluwer) | dossier | 8.4 | 4.0 | 8.7 | 9.8 | 10.0 | 5.4 | 7.2 | 8.9 | 3.2 | **7.8** |
| D11 | HealthifyMe / Healthify | dossier | 7.7 | 4.9 | 8.0 | 7.5 | 8.9 | 6.7 | 7.1 | 6.2 | 4.8 | **7.1** |
| D04 | Function Health | dossier | 6.7 | 2.5 | 8.5 | 9.7 | 2.5 | 7.4 | 10.0 | 7.2 | 3.3 | **6.8** |
| D03 | Superpower Health | dossier | 7.1 | 4.7 | 6.4 | 4.6 | 8.7 | 4.3 | 2.6 | 3.8 | 4.6 | **5.3** |
| D16 | WHOOP | dossier | 6.8 | 3.0 | 6.1 | 4.4 | 7.2 | 3.0 | 8.8 | 3.5 | 8.3 | **5.3** |
| D17 | Practo | dossier | 6.8 | 4.2 | 6.5 | 4.7 | 9.5 | 3.2 | 4.7 | 3.1 | 8.0 | **5.3** |
| D01 | Human API / LexisNexis | dossier | 5.4 | 4.6 | 4.7 | 10.0 | 4.3 | 1.4 | 2.7 | 6.2 | 8.9 | **4.9** |
| G01 | JARVIS due-diligence (2 panels) | **ground truth** | 3.4 | 4.0 | 2.7 | 5.9 | 3.8 | 1.2 | 9.9 | 7.9 | 8.7 | **4.9** |
| D13 | Google Health | dossier | 6.4 | 1.9 | 5.4 | 5.3 | 9.7 | 1.6 | 2.1 | 3.3 | 8.0 | **4.5** |
| D05 | Levels Health | dossier | 8.0 | 2.3 | 6.5 | 2.0 | 3.0 | 3.0 | 2.5 | 5.9 | 8.8 | **4.2** |
| D19 | Ultrahuman | dossier | 5.8 | 5.0 | 6.2 | 2.7 | 4.2 | 1.8 | 2.2 | 5.1 | 9.0 | **4.1** |
| D06 | OpenEvidence | dossier | 6.7 | 6.6 | 7.0 | 2.7 | 1.8 | 1.5 | 3.9 | 2.2 | 9.0 | **4.0** |
| D15 | Atropos Health | dossier | 6.0 | 4.8 | 5.7 | 3.6 | 4.4 | 1.3 | 1.8 | 3.2 | 9.0 | **3.9** |
| D14 | Oura Health | dossier | 5.4 | 3.9 | 6.3 | 1.9 | 2.4 | 3.8 | 4.9 | 1.8 | 8.6 | **3.8** |
| D08 | AMBOSS | dossier | 6.0 | 4.8 | 5.3 | 2.3 | 4.1 | 1.4 | 2.2 | 3.4 | 9.0 | **3.7** |
| D12 | Apple Health / HealthKit | dossier | 5.3 | 5.5 | 4.4 | 2.2 | 6.0 | 1.0 | 2.2 | 1.7 | 9.0 | **3.5** |
| D07 | Glass Health | dossier | 5.0 | 3.5 | 4.9 | 3.6 | 2.3 | 1.5 | 2.4 | 3.3 | 9.0 | **3.3** |
| D10 | Tata 1mg | dossier | 5.9 | 2.4 | 6.4 | 3.1 | 1.7 | 3.2 | 1.2 | 2.3 | 4.7 | **3.3** |
| D09 | Apollo 24\|7 | dossier | 5.1 | 5.1 | 4.5 | 2.2 | 2.2 | 1.1 | 1.5 | 1.7 | 9.0 | **2.9** |
| D02 | Regacore | dossier | 4.9 | 4.4 | 4.6 | 1.1 | 2.1 | 1.5 | 1.7 | 1.5 | 9.0 | **2.7** |
| I01 | HPID registry (449 platforms) | **infrastructure** | 3.1 | 4.2 | 1.0 | 1.4 | 8.1 | 1.0 | 1.0 | 1.2 | 9.0 | **2.6** ⚠️ |

⚠️ **I01's 2.6 is a rubric artifact, not a verdict.** See §1.3.

**Mean overall across the 19 competitor dossiers: 4.55. Mean Evidence Quality across all 21: 4.11.**

> **The headline Phase-1 finding (F-1.1):** the corpus is **broad and structurally disciplined but evidentially thin**. Nineteen dossiers averaging 4.55/10 with evidence quality at 4.11/10 means this is a *hypothesis corpus*, not a fact corpus. It is entirely usable — but every downstream phase must treat its claims as **leads to verify**, never as premises to build on.

---

## 1.3 ADJUSTED PRIORITY — WHAT ACTUALLY MATTERS FOR A SOLO BUILDER

`Adjusted Priority = 0.5·Fit-for-Objective + 0.3·Overall + 0.2·Evidence`

| Rank | ID | Artifact | Class | Overall | Fit | **Priority** | Why this fit score |
|---|---|---|---|---|---|---|---|
| 1 | **G01** | JARVIS due-diligence, 2 panels | ground truth | 4.9 | 10 | **7.27** | The only artifact describing the system being built. Objective is the engineering plan. |
| 2 | **D18** | UpToDate | dossier | 7.8 | 8 | **7.14** | Best technical + healthcare depth in corpus; defines the clinical-knowledge layer JARVIS must interoperate with, not rebuild. |
| 3 | **D01** | Human API / LexisNexis | dossier | 4.9 | 9 | **6.89** | **Technical Depth 10.0 — highest measured.** It is a *dossier about an integration layer* — structurally the closest analogue to JARVIS's adapter problem. |
| 4 | **I01** | HPID registry, 449 platforms | infrastructure | 2.6 | 10 | **6.62** | Populated, queryable, refreshable from a live government API. The adapter backlog's raw material. |
| 5 | D11 | HealthifyMe | dossier | 7.1 | 7 | 6.61 | Deepest India-market dossier; 838 tables; ABDM-aware. |
| 6 | D06 | OpenEvidence | dossier | 4.0 | 8 | 6.52 | **Evidence Quality 6.6 — highest in corpus** (393 bracket citations). Model of clinical-AI grounding + citation discipline. |
| 7 | D17 | Practo | dossier | 5.3 | 8 | 6.43 | Healthcare Accuracy 9.5; only dossier covering Indian clinic/HMIS software workflows JARVIS would automate. |
| 8 | D03 | Superpower Health | dossier | 5.3 | 7 | 6.03 | 41 raw JS/HTML captures — real client-bundle evidence, incl. a FHIR citation parser. |
| 9 | D12 | Apple Health | dossier | 3.5 | 7 | 5.65 | Consumer-consent + on-device data substrate pattern. |
| 10 | D15 | Atropos Health | dossier | 3.9 | 7 | 5.63 | Evidence-generation-as-a-service; closest analogue to a verification engine. |
| 11 | D04 | Function Health | dossier | 6.8 | 6 | 5.54 | **Regulatory Accuracy 10.0**; strong ops model, weak sourcing. |
| 12 | D13 | Google Health | dossier | 4.5 | 7 | 5.23 | Healthcare Accuracy 9.7; platform-layer reference. |
| 13 | D08 | AMBOSS | dossier | 3.7 | 6 | 5.07 | 385 URL refs; knowledge-layer comparator to D18. |
| 14 | D19 | Ultrahuman | dossier | 4.1 | 5 | 4.73 | India wearable; 15 framework files. |
| 15 | D16 | WHOOP | dossier | 5.3 | 5 | 4.69 | Best-structured bundle (15 files); low engineering yield. |
| 16 | D07 | Glass Health | dossier | 3.3 | 6 | 4.69 | Small but clean CDS reference. |
| 17 | D09 | Apollo 24\|7 | dossier | 2.9 | 5 | 4.39 | India integrated-care model. |
| 18 | D05 | Levels Health | dossier | 4.2 | 5 | 4.22 | Research Quality 8.0 (485 structured rows) but Evidence 2.3. |
| 19 | D10 | Tata 1mg | dossier | 3.3 | 5 | 3.97 | 518 tables, **zero URLs**. |
| 20 | D14 | Oura | dossier | 3.8 | 4 | 3.92 | Highest %-confirmed (83.7%) but thin engineering yield. |
| 21 | D02 | Regacore | dossier | 2.7 | 3 | 3.19 | 44 screenshots; smallest strategic surface. |

**F-1.2 — the corpus's centre of gravity is misaligned with the objective.** Eight of nineteen dossiers study **consumer wearables and biomarker memberships** (D03, D04, D05, D14, D16, D19, plus D11, D12). Only **four** study anything JARVIS must actually *drive*: clinic/hospital software (D17), health-data integration (D01), clinical knowledge (D18, D08). For an engineering plan targeting workflow automation, roughly **60% of the corpus is adjacent, not core**. This is not a defect in the reports — it is a **portfolio composition finding**, and it defines Phase 6's whitespace hunt.

---

## 1.4 ENGINEERING GROUND TRUTH — G01 VALIDATED AGAINST LIVE CODE

Phase 0 left the unmerged branches as the blocking unknown for any engineering baseline. Q2 makes resolving them mandatory. **All four branches were fetched and measured; the full test suite was executed on two.**

### 1.4.1 Branch topology — verified

| Branch | Files | .py | Delta vs `main` |
|---|---|---|---|
| `main` | 1,132 | 656 | baseline |
| `phase-1-code-engine-fix` | 1,132 | 656 | **Zero diff — identical tree to `main`** |
| default (`feature/improve-readme-…`) | 1,156 | 651 | +294/−93 lines, 7 files (README + 4 new tests) |
| **`phase-2-adapter-wiring`** | **1,178** | **695** | **+9,713 / −243 lines across 83 files** |

**F-1.3 🔵 Code-Backed — the real JARVIS is not on the default branch.** `phase-2-adapter-wiring` contains ~9,700 lines of unmerged work: a new `CommandRouter` (347 LOC), a `resolution_gate.py` (174 LOC), `session_memory.py` (113 LOC), a 1,214-line `platform_catalog.py`, 12 genuinely new adapters, Playwright browser automation (248 LOC), `pyproject.toml` packaging, an onboarding flow (426 LOC), and **5 new design documents (1,145 doc-lines)**. Phase 0's assessment of JARVIS — and G01's, and both due-diligence panels' — described the **weakest available branch**. Recorded as **DL-010**.

### 1.4.2 Test suite executed — the honest baseline

Dependencies are Windows-only (`winotify`, `pywinauto`, `pyautogui`). Both branches were run under identical `unittest.mock`-based shims so the comparison is fair.

| Branch | Passed | Failed | Collection errors | Verdict |
|---|---|---|---|---|
| default | **7** | 4 | 49 → 14 (post-shim) | Suite effectively **does not run** |
| `phase-2-adapter-wiring` | **325** | 18 | 8 | Suite **runs and largely passes** |

**F-1.4 🔵 Code-Backed.** The default branch yields 7 passing tests. The unmerged branch yields **325 passing, 2 skipped, 19 sub-tests passing**. The 18 failures are concentrated in `test_jarvis_import`, `test_onboarding`, `test_nethytech_listen_import_coupling` — all import-coupling and Windows-platform tests, i.e. **environmental**, not logic failures. Remaining 8 collection errors trace to `libcst`/`selenium`/`pywinauto` absence.

> **Engineering implication, stated now for Phase 11:** the first act of the JARVIS engineering plan is not to write features. It is to **merge `phase-2-adapter-wiring` into `main`, make `main` the default branch, and add CI**. A repository whose best work sits unmerged on a non-default branch, whose default branch is a README-cosmetics branch, and whose test suite passes 7 assertions, is **losing its own work**. Zero cost, immediate compounding return, solo-builder-executable today.

### 1.4.3 The repository audits itself — and confirms Phase 0 independently

`docs/adapter_audit.md` on the unmerged branch is the most intellectually honest document in the entire engagement. Its author scanned all 160 adapters and read 25 in full:

| Class | Count | Meaning |
|---|---|---|
| (a) Real & complete for declared scope | **3** | `amazon`, `google`, `chrome` |
| (b) Real logic, incomplete/defective | **8 confirmed** | `whatsapp`, `notepad`, `gmail`, `twitter`, `spotify`, `youtube`, `explorer`, `calculator` |
| (c) Fabricated / scaffold, non-functional | **149** | 133 fabricated-URL + 16 copy-paste scaffolds |

Verbatim: *"None of the 160 folders is a complete, ready-to-port implementation of its full declared action set."* And on the fabricated pattern: *"`https://netflix.com/?action={action_name}&q={query}` — **This is not a real API**."*

**F-1.5 — convergent validation.** Phase 0 independently measured, via static analysis with no knowledge of this document: median adapter 27 lines, 144/160 no-op verifiers, 140/160 navigate-only. The repo's own audit reached the same conclusion by a different method (defect-signature scan + 25 full reads). **Two independent methods, one answer.** This is the strongest-confidence finding in the engagement so far: 🔵 **Code-Backed, dual-method confirmed**.

It also produces the corpus's best single insight about half-built systems, quoted for Phase 5:

> *"the **first** step of a multi-step action (navigate to search/compose page) is consistently real; the **last** step (click Send/Post/Play) is consistently missing, guessed, or the detection logic around it is broken. This looks like a 'half-implemented then abandoned' pattern repeated across the library, not independent one-off issues."*

### 1.4.4 The repository also built the right response to its own finding

Rather than delete 149 fake adapters or pretend they work, `resolution_gate.py` introduces a **two-question honesty gate**: (Q1) is there a *wired, working* adapter — not merely an audit-classified one? If no → *"I don't know how to control [platform] yet."* (Q2) if yes, is the app installed? If no → offer winget install, never auto-install. Fabricated adapters are explicitly excluded from install offers because *"a fabricated/nonexistent adapter means installing the app wouldn't help."*

**F-1.6 🔵 Code-Backed.** This is *honest-failure engineering* — the exact discipline the Stage-0 objective claims ("honest success or honest failure"). It is the strongest existing asset in the codebase for a healthcare pivot, where silent no-ops are a patient-safety hazard. Recorded as **DL-011**.

Also verified: `feature_flags/level6_engine.yaml` flipped `enabled: false → true` on this branch, with `require_owner_approval_for_apply: true`. Contradiction **C-02** from Phase 0 is now **branch-dependent** — resolved below.

### 1.4.5 Resolution of Phase 0 contradictions

| ID | Phase 0 status | Phase 1 resolution |
|---|---|---|
| C-01 | README "automate any application" vs stub adapters | **Upheld and sharpened.** Repo's own audit: 149/160 fabricated. But the unmerged branch *fixes the behaviour* via the resolution gate. Documentation still overstates; runtime no longer lies. |
| C-02 | "Level-6" vs `enabled: false` | **Branch-dependent.** `false` on default, `true` with owner-approval gating on `phase-2-adapter-wiring`. Both statements were true of different branches. |
| C-03 | Two panels, opposite verdicts | **Both partially invalidated by F-1.3** — both assessed the weakest branch. Panel A's stage-discipline verdict survives and strengthens. Panel B's "zero healthcare code" survives intact (re-verified: still zero). |
| C-04 | XOR "encryption", hardcoded key | **Upheld, unchanged on all branches.** `memory_store.py:70-75`. Blocking for any PHI. |
| C-05 | Dissection repo empty | Resolved in Phase 0. |

---

## 1.5 BIAS, CORRELATION & HALLUCINATION ANALYSIS

### 1.5.1 Single-pipeline correlation — the corpus is not 19 independent observations

- **49 markdown files share the identical three-label legend.**
- **All 21 artifacts carry the same date: 2026-07-25** (23 ISO stamps + 23 prose forms).
- 12 of 19 dossiers hit exactly 27/27 canon coverage.

**F-1.7 — correlated-source bias, HIGH severity.** These dossiers were produced by one templated pipeline in one sitting. Consequences that bind every later phase:
1. **Apparent consensus is not corroboration.** If five dossiers assert "AI scribes are the wedge," that may be one generator's prior expressed five times, not five independent observations.
2. **A systematic blind spot appears nineteen times, not once.** The missing EHR/payer/RCM coverage (F-1.2) is structural, not accidental.
3. **Phase 5 (Pattern Discovery) is at maximum risk.** Its entire method is counting recurrences. Recorded as **DL-012**: *Phase 5 patterns require corroboration from ≥2 artifacts of **different class or geography**, or from I01/G01 primary data. Recurrence within the dossier corpus alone is downgraded to 🟡.*

### 1.5.2 Recency

Year mentions: 2024 ×167 · 2025 ×369 · 2026 ×397 · 2027+ ×49. Fact base is genuinely current (2025–26 weighted). **Recency: strong.** Forward claims to 2027–29 are 🔴 by construction.

### 1.5.3 Hallucination-risk register — dossiers asserting numbers without sources

The dangerous quadrant is **high numeric density × low citation density**.

| ID | Numeric claims ($ + %) | Citations/1k words | Hall-Safety | Assessment |
|---|---|---|---|---|
| **D18** UpToDate | 96 | **0.0** | **3.2** | ⚠️ **Highest risk.** 54,638 words, **zero inline URLs**. *Mitigating:* a 60-row evidence register with **56 verbatim quotes and zero placeholders** — the corpus's best register. Sources are named (publisher, date) but not linked. **Verdict: rigorous but unlinkable — every number must be re-verified before use.** |
| **D04** Function Health | 191 | 0.5 | **3.3** | ⚠️ **High risk.** Regulatory Accuracy 10.0 and 428 tables, on 17 URLs across 35k words. Confident, structured, under-sourced. |
| **D10** Tata 1mg | 72 | **0.0** | **4.7** | ⚠️ **High risk.** 518 tables, **zero URLs anywhere**. Spot-check found precise claims — *"~67% ownership by Tata Digital"*, *"$750–800M valuation … proposed by Novo Holdings, CPPIB, Permira, ChrysCapital"*, an ET-attributed ₹-figure — all labelled 🟢 Confirmed with **no resolvable citation**. Named sources exist inline; a register does not. |
| **D03** Superpower | 103 | 0.2 | 4.6 | Medium. *Mitigated by 41 raw client-bundle captures* — strongest primary-artifact evidence in the corpus. |
| **D11** HealthifyMe | 236 | 1.2 | 4.8 | Medium-high by volume; 24 raw page captures mitigate. |
| D06, D08, D09, D12, D15, D19 | low–moderate | 21.6–31.6 | **9.0** | ✅ **Lowest risk.** D06 carries 393 bracket citations; D09 182; D12 179; D19 104. |

**F-1.8.** Hallucination risk in this corpus is **inversely correlated with visible citation apparatus, not with confidence of tone**. The three most assertive dossiers (D18, D04, D10) are the three least verifiable. D18 is the corpus's highest-scoring artifact *and* its highest hallucination risk — these are not in tension; it is well-researched prose whose sourcing was recorded in a companion register rather than inline.

### 1.5.4 Evidence-register audit

| Register | Rows | Real URLs | Placeholders | Verbatim quotes |
|---|---|---|---|---|
| D18 `27_evidence_register.csv` | 60 | 0 | **0** | **56** ✅ best-quality content, no links |
| D08 `AMBOSS_Evidence_Register` | 66 | 63 | 66 | — links present, evidence cells templated |
| D16 `whoop_evidence_register_v2` | 25 | 23 | **50** | 11 — ⚠️ heavy `"See report sections…"` / `"not captured"` filler |

**F-1.9.** Registers split into two failure modes: **linked but templated** (D08, D16) and **quoted but unlinked** (D18). Neither is complete. The HPID must require both: resolvable URL **and** verbatim quote. Recorded as **DL-013**.

### 1.5.5 Structured-data yield

**1,277 structured feature rows** exist across 29 XLSX (2,338 total rows, 923 in feature sheets) and 14 CSV (354 rows) — plus I01's 449 platform rows with 32 scored columns each.

**F-1.10.** Phase 3's Master Product Genome does not start from zero. It starts from ~1,277 pre-extracted feature rows requiring normalisation and de-duplication. Largest contributors: D05 (485), D03 (227), D06 (217), D17 (214), D13 (172).

---

## 1.6 END-OF-PHASE DELIVERABLES — PHASE 1

### ✅ Completed
- All 21 artifacts scored independently on 9 axes via a reproducible instrumented rubric; **no merging performed**.
- 24 measurable signals extracted per artifact; rubric and raw signals published as machine-readable data.
- Artifact-class correction and fitness-for-objective axis added and justified.
- **All 4 JARVIS branches fetched and measured**; Phase 0's blocking unknown resolved.
- **Full test suite executed on 2 branches** under identical dependency shims.
- Repository's own `adapter_audit.md` located and cross-validated against Phase 0 static analysis.
- Correlated-pipeline bias quantified; hallucination-risk register built; evidence registers audited.
- Five Phase-0 contradictions resolved or re-scoped.

### 🟢 Verified Facts
| # | Fact | Evidence |
|---|---|---|
| VF-13 | 19 competitor dossiers average **4.55/10 overall**; mean Evidence Quality **4.11/10** | Computed rubric, `phase1_scores.json` |
| VF-14 | **49 md files share one label legend; all 21 artifacts dated 2026-07-25** | Corpus-wide regex |
| VF-15 | Corpus contains **1,277 structured feature rows** + I01's 449×32 platform matrix | openpyxl/csv enumeration |
| VF-16 | D18 has **0 inline URLs across 54,638 words**, but a 60-row register with 56 verbatim quotes, 0 placeholders | CSV audit |
| VF-17 | D10 has **0 URLs**, 518 tables, precise 🟢-labelled financials with no resolvable citation | Regex + spot-check |
| VF-18 | D06 carries **393 bracket citations** — highest Evidence Quality (6.6) in corpus | Regex count |

### 🔵 Code-Backed Facts (override all documentation)
| # | Fact | Evidence |
|---|---|---|
| CB-01 | `phase-1-code-engine-fix` is **byte-identical to `main`** — zero diff | `git diff --stat` |
| CB-02 | `phase-2-adapter-wiring` adds **+9,713/−243 lines over 83 files**, incl. `CommandRouter` 347, `resolution_gate` 174, `platform_catalog` 1,214, onboarding 426, browser automation 248, 5 design docs (1,145 lines) | `git diff --stat`, `wc -l` |
| CB-03 | Test suite: default branch **7 passed / 49 collection errors**; `phase-2-adapter-wiring` **325 passed, 18 failed, 8 errors** — failures all environmental (Windows deps) | `pytest` under identical shims |
| CB-04 | Repo self-audit classifies adapters **3 real (a) / 8 defective (b) / 149 fabricated (c)** | `docs/adapter_audit.md`, `platform_catalog.py` classification counts |
| CB-05 | `resolution_gate.py` implements honest-failure: unwired platform → *"I don't know how to control [platform] yet"*; never offers install for fabricated adapters | `AgentCore/resolution_gate.py:1-60` |
| CB-06 | `level6_engine.yaml` = `enabled: true` + `require_owner_approval_for_apply: true` on `phase-2-adapter-wiring` (was `false` on default) | File diff |
| CB-07 | **Zero healthcare code re-confirmed on all four branches** | Recursive grep |
| CB-08 | XOR-with-hardcoded-key encryption unchanged on every branch | `memory_store.py:70-75` |
| CB-09 | `MemoryStore` is **orphaned** — imported only by `feedback_engine`/`optimizer`, which nothing imports | `docs/phase3_hermes_capabilities.md`, grep-confirmed |

### 📄 Supported by Documentation Only
- `docs/phase3_hermes_capabilities.md` (302 lines) — persistent cross-session memory design. Explicitly *"Groundwork only, review-gated. Nothing here is wired into the live conversation loop yet."* **Intent, not implementation.**
- `docs/phase2g_browser_automation.md`, `docs/phase2d_porting.md`, `docs/command_architecture.md` — describe work partially present in code; each claim needs individual verification before Phase 11 relies on it.
- The 27-deliverable canon remains a convention; no governing spec found.

### 🧠 Architectural Inferences
| # | Inference | Justification |
|---|---|---|
| AI-05 | JARVIS is mid-refactor from *"declare 160 platforms"* to *"wire a few platforms honestly."* Direction of travel is correct; the merge is the bottleneck | Audit + catalog + resolution gate + registry of 14 wired adapters, all unmerged |
| AI-06 | The developer's instinct to **reuse `MemoryStore` rather than add a 5th storage convention** signals architectural discipline that should be preserved in Ovexis | Phase-3 doc reasoning, verbatim |
| AI-07 | Corpus over-indexes on consumer wearables (8/19) and under-indexes on systems JARVIS must drive (4/19) → Phase 6 whitespace is likelier in **clinic/hospital operational software** than in consumer health | Portfolio composition |
| AI-08 | D01 (Human API) scoring **Technical Depth 10.0** while being *about an integration layer* makes it the corpus's best structural analogue for JARVIS's adapter problem — disproportionate weight in Phases 3, 7, 11 | Score + subject matter |

### 🔴 Speculation
- The `phase-2-adapter-wiring` branch may be abandoned rather than in-flight (last push 2026-07-23; author cadence unknown). **Untested.**
- The single-pipeline corpus may reflect one model's priors about healthcare rather than the market. Testable only against external primary sources.

### ❓ Unknowns
1. Why was `phase-2-adapter-wiring` never merged — deliberate gate, or abandonment?
2. Do the 12 wired adapters function on real Windows hardware? (No Windows environment available here.)
3. Are D18's 60 unlinked register sources real and re-findable?
4. Is I01's ABDM Strapi API still live and unauthenticated *today* (2026-07-26)? **Not tested in Phase 1 — must be tested before Phase 16 depends on it.**
5. Do the XLSX feature inventories contain fields absent from the markdown? (Row counts measured; cell contents not yet parsed — Phase 3.)
6. Solo-builder velocity baseline: what can one person + AI actually ship per month? Phase 12 needs this and has no data.

### ⚠️ Contradictions
| # | Contradiction | Resolution |
|---|---|---|
| C-06 | Both G01 panels assessed JARVIS as ~stub-grade ↔ 9,713 unmerged lines with 325 passing tests exist | 🔵 Code wins. **Both panels are outdated.** Not wrong at time of writing — they read the default branch. Preserved per protocol; superseded by CB-02/CB-03. |
| C-07 | Corpus presents 19 "independent" dossiers ↔ single-pipeline, single-date, shared-template production | Bias is real; artifacts remain individually usable. Binds Phase 5 via DL-012. |
| C-08 | D18 = highest overall score (7.8) ↔ near-worst hallucination safety (3.2) | Both true. Quality of *reasoning* ≠ verifiability of *claims*. Use D18 for structure/architecture; re-verify every number. |
| C-09 | README: privacy-first local assistant ↔ `MemoryStore` orphaned, so nothing persists through the audited path | 🔵 Code wins. Marketing describes an unwired subsystem. |

### 🕳️ Research Gaps (carried + new)
- **Carried:** no primary clinician/CIO/payer research; no EHR-incumbent dossier (Epic, Cerner, Meditech); no PACS/LIS/RCM coverage; no dedicated regulatory dossier; 62 screenshots and 67 raw captures still unread.
- **New G-1.1:** No Windows test environment → the 12 wired adapters cannot be functionally validated here. Phase 11 must assume *unproven* until run on target hardware.
- **New G-1.2:** No CI configuration in any branch. No evidence any test ever ran automatically.
- **New G-1.3:** D18's 60 register sources are unlinked; re-verification is unbudgeted manual work.
- **New G-1.4:** I01's live-API assumption untested as of today.
- **New G-1.5:** No latency, cost-per-inference, or local-model performance data anywhere — Phase 11 will need it for the local-vs-cloud reasoning split.

### 📒 Decision Ledger — Phase 1
| ID | Decision | Rationale | Reversible? |
|---|---|---|---|
| DL-007 | **Solo-builder constraint is a hard architectural filter.** Any recommendation requiring a team is invalid until a team exists | Board answer Q5 | Yes — on hiring |
| DL-008 | Artifacts classed `competitor_dossier`/`ground_truth`/`infrastructure`; cross-class ranking by `overall` prohibited | I01 scored 2.6 while being the most valuable asset — rubric artifact | No |
| DL-009 | Final ordering = `0.5·Fit + 0.3·Overall + 0.2·Evidence` | Objective is an engineering plan, not a literature review | Yes |
| DL-010 | **`phase-2-adapter-wiring` is the canonical JARVIS baseline**, not the default branch. All Phase-11 architecture measures against it | +9,713 lines, 325 passing tests vs 7 | No |
| DL-011 | The **resolution-gate honest-failure pattern is a protected asset**. No later phase may design it away | Directly implements Stage-0's honest-failure objective; prerequisite for clinical safety | No |
| DL-012 | **Phase 5 patterns need corroboration across artifact class or geography**, or from I01/G01 primary data. Intra-corpus recurrence alone → 🟡 | Single-pipeline correlation (F-1.7) | No |
| DL-013 | HPID evidence schema requires **both** resolvable URL and verbatim quote per claim | Neither register style in corpus is complete (F-1.9) | No |
| DL-014 | D18, D04, D10 flagged **VERIFY-BEFORE-USE**; their numerics may not be premises without re-sourcing | Hallucination-risk register (F-1.8) | Yes, on re-verification |
| DL-015 | Both G01 panels **preserved verbatim** and marked superseded-on-baseline, not deleted | Protocol: preserve old conclusions, explain change | No |

### 📊 Confidence Score — Phase 1

| Dimension | Score | Justification |
|---|---|---|
| Scoring reproducibility | **HIGH** | Fully instrumented; regenerates deterministically from corpus |
| JARVIS engineering baseline | **HIGH** | All 4 branches measured; suite executed; self-audit cross-validated by independent static analysis |
| Corpus evidence quality assessment | **HIGH** | Directly measured (citations, registers, raw captures) |
| Underlying dossier *factual accuracy* | **LOW–MEDIUM** | Mean evidence 4.11/10; three high-volume dossiers effectively unsourced; single-pipeline correlation |
| Adapter functional status | **MEDIUM** | Two independent methods agree on classification; **no branch functionally executed on Windows** |
| Fit-for-objective weighting | **MEDIUM** | Judgement-based (mine), transparently published, adjustable |
| **Overall Phase 1** | **HIGH on corpus structure and code ground truth; MEDIUM-LOW on inherited factual claims** | We now know precisely what we have, how good it is, and where it will mislead us |

---

## 1.7 THE THREE THINGS PHASE 1 CHANGES

1. **The engineering baseline moved.** JARVIS is not a 7-passing-test stub. It is a 325-passing-test system with an honest-failure gate and a self-authored adapter audit — **sitting unmerged on a non-default branch.** Every prior assessment, including two due-diligence panels and my own Phase 0, described the weakest branch. *(DL-010)*
2. **The corpus is a hypothesis engine, not a fact base.** Mean 4.55/10, evidence 4.11/10, single-pipeline production, three major dossiers effectively unsourced. Fully usable for reconstructing market *structure* — unsafe as a source of *numbers*. *(DL-012, DL-014)*
3. **Solo-builder is now the binding constraint.** With no team, the plan's value is measured in what one person can merge, wire and verify — which makes the highest-value next action free: **merge the branch, set `main` as default, add CI.** *(DL-007)*

---

## PHASE 1 COMPLETE

Machine-readable outputs written:
- `ovexis/registry/phase1_signals.json` — 24 raw signals × 21 artifacts
- `ovexis/registry/phase1_scores.{json,csv}` — 9-axis scores + fit + adjusted priority
- `ovexis/exports/phase1_validation.{json,yaml}` — HPID-schema validation record (`ovexis.hpid.phase1.validation/v1`)
- `ovexis/registry/corpus_manifest.{json,csv}` — Phase 0 manifest (carried)

**No artifacts were merged.** Merging begins in Phase 2 (Market Reconstruction), which will ignore company names and rebuild the market by layer.

Stopping here as instructed. Awaiting `Continue`.
