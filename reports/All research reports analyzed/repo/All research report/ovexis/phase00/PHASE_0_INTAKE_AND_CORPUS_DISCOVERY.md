# PHASE 0 — INTAKE, SCOPE LOCK & CORPUS DISCOVERY
## Ovexis Intelligence Synthesis Engine (OISE) — Permanent Engagement Record

**Engagement:** Ovexis / JARVIS Strategic Intelligence Synthesis
**Phase:** 0 of 16 (+ Phase Ω)
**Date:** 2026-07-26 (Asia/Calcutta)
**Status:** COMPLETE — awaiting Board answers to five intake questions before Phase 1 begins
**Canonical:** Yes. This document becomes evidence for every subsequent phase.

---

## 0.1 WHAT PHASE 0 IS

Phase 0 is *not* analysis. Phase 0 exists to do four things and nothing more:

1. **Locate and verify the evidence base** — what actually exists, physically, before a single conclusion is drawn.
2. **Separate the two repositories permanently** — Dissection (research) vs JARVIS-Automation (implementation ground truth). These are never merged.
3. **Establish the evidence grammar** used for all sixteen phases.
4. **Ask the minimum set of questions** whose answers materially change the output, then stop.

No market conclusions, no product strategy, no synthesis appears below. That is Phase 2 onward.

---

## 0.2 REPOSITORY SCOPE — VERIFIED STATE

### Repository A — `SONIC445-BYTE/Dissection` (Primary Research Workspace)

| Attribute | Verified value | Source |
|---|---|---|
| Created | 2026-07-26T03:50:19Z | GitHub REST API `/repos/SONIC445-BYTE/Dissection` |
| Git tree | **Empty** — zero commits, `size: 0` | Repo landing page: *"This repository is empty."* |
| Default branch | `main` (unborn) | API |
| Open issues | 1 | API |
| **Actual payload location** | **Issue #1 "GH"** — 20 ZIP attachments on `github.com/user-attachments` | API `/issues?state=all` |

> **Critical Phase-0 finding (F-0.1).** The Dissection repository contains **no committed files**. The entire research corpus exists only as twenty ZIP archives attached to a single GitHub issue created 2026-07-26T03:54:57Z. This is a durability and provenance risk, not a content risk — the content is intact and has been retrieved. It is recorded in the Decision Ledger as **DL-000**.

**Retrieval performed:** all 20 archives downloaded (35 MB compressed), extracted to `/home/user/dissection/`, integrity confirmed — 434 files, 0 extraction errors.

### Repository B — `SONIC445-BYTE/JARVIS-Automation` (Engineering Ground Truth)

| Attribute | Verified value | Source |
|---|---|---|
| Created | 2026-02-12T19:34:16Z | GitHub REST API |
| Last push | 2026-07-23T12:47:25Z | API |
| Default branch | `feature/improve-readme-presentation-7944846130129777438` | API |
| Branches | 4 — default, `main`, `phase-1-code-engine-fix`, `phase-2-adapter-wiring` | API `/branches` |
| Language / licence | Python / GPL-3.0 | API |
| Stars / forks / open issues | 1 / 0 / 0 | API |
| Size | 324,647 KB | API |
| Files (default branch, shallow clone) | **1,156** | local `find` |
| Python files / LOC | **651 files / 36,291 lines** | local count |

**Phase-0 finding (F-0.2).** The *default branch is a README-cosmetics feature branch*, not `main`. Two work branches (`phase-1-code-engine-fix`, `phase-2-adapter-wiring`) exist and have not been merged. Any claim about "what JARVIS is" must state which branch it was measured on. All measurements in this engagement are taken from the **default branch** unless explicitly stated. Recorded as **DL-001**.

### The Firewall Rule (permanent)

```
Dissection  = OBSERVATION of the outside world  → informs strategy
JARVIS      = IMPLEMENTATION we control          → constrains strategy
Ovexis      = the COMPANY / platform thesis      → is neither of the above
```

JARVIS is a **component and proving ground**, not a synonym for Ovexis. No phase may write a sentence in which "JARVIS" and "Ovexis" are interchangeable. Violations are Phase-0 protocol breaches.

---

## 0.3 CORPUS INVENTORY — WHAT ACTUALLY ARRIVED

**21 distinct intelligence artifacts** across 20 workspace archives (one archive contains two independent dossiers).
**365,728 words** of analytical markdown · **397 evidence-bearing files** · 62 screenshots/diagrams · 29 XLSX workbooks · 14 CSV registers · 67 raw HTML/JS/XML captures.

Machine-readable manifest written to:
- `/home/user/ovexis/registry/corpus_manifest.json`
- `/home/user/ovexis/registry/corpus_manifest.csv`

### 0.3.1 Competitor / platform dossiers (19)

| ID | Target | Category | Geo | Words | 🟢/🟡/🔴 | Raw evidence artifacts |
|---|---|---|---|---|---|---|
| D01 | Human API → LexisNexis Health Intelligence | Health-data aggregation API, EHR network | US | 9,141 | 127/71/9 | 20 screenshots, 14 DOM captures, 4 raw HTML, 5 XLSX |
| D02 | Regacore | Longevity / regenerative clinic platform | US | 10,274 | prose labels (no emoji) | 44 screenshots, JS bundle capture |
| D03 | Superpower Health | Preventive/longevity "AI health OS" | US | 20,983 | 253/85/35 | 41 raw captures incl. 19 JS chunks, sitemaps, robots |
| D04 | Function Health | Biomarker-testing membership | US | 35,322 | 215/113/12 | 23 markdown deliverables + 9 diagrams |
| D05 | Levels Health | CGM / metabolic health | US | 17,013 | 266/392/26 | 129 URL refs, feature inventory CSV+XLSX |
| D06 | OpenEvidence | Clinical AI answer engine (CDS) | US | 15,765 | 249/539/6 | 6 rendered diagrams, DOCX, XLSX |
| D07 | Glass Health | AI clinical decision support / DDx | US | 6,597 | 83/92/4 | XLSX feature inventory |
| D08 | AMBOSS | Clinical knowledge + med-ed | DE/US | 12,957 | 246/405/39 | 385 URL refs, evidence register CSV+XLSX |
| D09 | Apollo 24\|7 | Integrated care + e-pharmacy + telehealth | IN | 6,776 | 110/138/13 | XLSX inventory |
| D10 | Tata 1mg | E-pharmacy + diagnostics + teleconsult | IN | 13,006 | 227/51/41 | Feature inventory CSV |
| D11 | HealthifyMe / Healthify | AI nutrition & behaviour change | IN/US | 41,437 | 684/392/94 | 24 raw page captures, XLSX, evidence CSV |
| D12 | Apple Health / HealthKit | Device-native personal health substrate | US | 7,176 | 128/92/4 | XLSX inventory |
| D13 | Google Health | Platform + cloud healthcare AI | US | 13,841 | 353/337/6 | XLSX inventory |
| D14 | Oura Health | Wearable ring, longitudinal biometrics | FI/US | 13,399 | 246/39/9 | Standalone evidence register |
| D15 | Atropos Health | Real-world evidence generation OS | US | 9,131 | 271/159/12 | 5 XLSX (landscape, ledger, risk, evidence, features) |
| D16 | WHOOP | Wearable membership / performance intel | US | 21,655 | 641/259/23 | 15-file bundle, 5 XLSX, evidence CSV |
| D17 | Practo | Discovery + teleconsult + clinic/HMIS software | IN | 16,611 | 390/111/76 | 8 SVG diagrams, XLSX |
| D18 | UpToDate (Wolters Kluwer) | Clinical reference / evidence platform | US/NL | 54,638 | 913/913/149 | 28 deliverables, 4 SVG, 2 CSV |
| D19 | Ultrahuman | Wearable ring, metabolic/longevity | IN | 14,158 | 174/282/21 | 15 framework files, XLSX |

### 0.3.2 Engineering ground-truth artifacts (1)

| ID | Artifact | Words | Nature |
|---|---|---|---|
| G01 | `JARVIS_StageDisciplined_Assessment.md` + `JARVIS_Healthcare_Evaluation.md` | 23,276 | **Two independent adversarial due-diligence panels on the same repository, reaching opposite verdicts.** One judges Stage-0 against Stage-0 objectives (favourable, disciplined); one judges the repo against healthcare procurement standards (damning). Both cite the same file paths. |

**Phase-0 finding (F-0.3).** G01 is the single most valuable artifact in the corpus *for engineering purposes*, because it is the only artifact where two evaluators disagree on identical evidence. That disagreement is not noise — it is the clearest available demonstration of the protocol rule *"never criticise missing Stage-3 capabilities in a Stage-0 repository."* Phase 1 will score both panels; neither is discarded.

### 0.3.3 Infrastructure / living-asset artifacts (1)

| ID | Artifact | Contents |
|---|---|---|
| I01 | **HPID — Healthcare Platform Intelligence Database, Phase-0 registry** | 449 platforms in JSON + YAML + CSV + **SQLite (9 tables, 1 view)**; 445 records from the ABDM/NHA official partner API; 23 government product-rating records across 16 scored criteria; 40 curated non-ABDM entries with VERIFIED/INFERRED flags; idempotent rebuild script. |

**Phase-0 finding (F-0.4) — the highest-leverage discovery in the corpus.** I01 already *is* the machine-readable substrate that the Phase-16 brief asks to be created. It is populated, queryable, source-cited, and refreshable from a live unauthenticated government API. Phase 16 will not build the HPID from scratch; it will **extend I01** with the feature, workflow, integration and concept ontologies. This changes the Phase-16 cost estimate by roughly an order of magnitude and is recorded as **DL-002**.

---

## 0.4 CORPUS COMPLETENESS AUDIT

Each dossier was tested against the 27-deliverable canon the corpus itself implies (executive summary → company intel → founder psychology → product RE → user journey → UX → healthcare workflow → data architecture → AI RE → technical RE → API → security → business model → growth → hiring → customer → decision ledger → dependency graph → backlog → landscape → moat → failure → attack plan → future → Ovexis strategy → feature inventory → evidence register).

| Coverage | Dossiers |
|---|---|
| **27/27** | D03, D04, D05, D06, D10, D11, D13, D15, D16, D17, D18, D19 (12 dossiers) |
| **24–26/27** | D01, D02, D07, D08, D09, D12, D14 (7 dossiers) |
| **Not applicable** (different artifact class) | G01 (12/27), I01 (5/27) |

Most common structural gaps: `technical_reverse_engineering` (5 dossiers), `competitive_attack_plan` (3), `engineering_backlog` (3).

---

## 0.5 EVIDENCE GRAMMAR (BINDING FOR ALL PHASES)

The corpus already uses a consistent three-label convention. This engagement adopts it verbatim and adds two labels required by the protocol's evidence rules.

| Label | Meaning | Promotion rule |
|---|---|---|
| 🟢 **Confirmed** | Directly observed in a cited public source, or directly read from code in this workspace | May be stated as fact |
| 🟡 **Strong Inference** | Follows from ≥2 confirmed observations; not stated by the subject | Must carry the word "inference" |
| 🔴 **Speculation** | Scenario or prediction | Never used as a premise for another conclusion |
| ⚪ **Cannot Verify** | Evidence would exist but was not accessible (login-gated, private) | Recorded as a Research Gap, never as absence |
| 🔵 **Code-Backed** | *(added)* Verified by reading a file in `JARVIS-Automation` at a named path on a named branch | Overrides any documentation claim |

**Overriding rules, restated as operating law:**
1. 🔵 Code-Backed **overrides** any 🟢 documentation claim about the same capability.
2. Documentation = intent. Roadmap = plan. Issue = discussion. None may be promoted.
3. "Not publicly verified" ≠ "does not exist." It is a Research Gap.
4. Stage discipline: a Stage-0 artifact is judged only against Stage-0 objectives.

---

## 0.6 END-OF-PHASE DELIVERABLES — PHASE 0

### ✅ Completed
- Both repositories located, authenticated against the GitHub REST API, and state-verified.
- Dissection payload recovered in full from Issue #1 (20 archives → 434 files, 0 errors).
- JARVIS-Automation cloned; branch topology, file count, LOC and module tree measured.
- 21 intelligence artifacts identified, classified, word-counted and evidence-profiled.
- Machine-readable corpus manifest emitted (JSON + CSV).
- Evidence grammar defined and made binding.
- Repository firewall (Dissection ≠ JARVIS ≠ Ovexis) established.
- Deliverable-coverage audit of all 21 artifacts completed.

### 🟢 Verified Facts (code- or artifact-backed)
| # | Fact | Evidence |
|---|---|---|
| VF-01 | Dissection repo has **zero commits**; all research lives in Issue #1 attachments | GitHub API `size:0`; landing page "This repository is empty" |
| VF-02 | Corpus = **21 artifacts, 365,728 analytical words, 397 files** | Local extraction + count |
| VF-03 | JARVIS default branch is a **README branch**, not `main`; 4 branches, 2 unmerged work branches | GitHub API `/branches` |
| VF-04 | JARVIS = **651 Python files, 36,291 LOC, 1,156 files total** | Local `find`/`wc` on default branch |
| VF-05 | **160 platform adapters** exist under `AgentCore/platform_adapters/`; **173 feature-flag YAMLs**, of which **160 are `platform_*.yaml`** | Local `ls`/count |
| VF-06 | Adapter median size is **27 lines**; only **17 of 160** exceed 40 lines; **144 of 160** implement `verify_action_result` as literal `return True`; **140 of 160** only emit a `navigate` step | Local static analysis of `adapter.py` files |
| VF-07 | `AgentCore/memory_store.py` encrypts with **base64(XOR)** and a hardcoded default key; the file's own comment reads *"In production, use proper AES-256 encryption"* | `memory_store.py:70-75` |
| VF-08 | **Zero healthcare-domain code** in JARVIS: no match for `fhir`, `patient`, or `hospital` in any `.py`/`.yaml`/`.md` (sole binary match is `chromedriver.exe`) | Recursive grep, default branch |
| VF-09 | Core reasoning modules are real, not empty: `agent_brain.py` 487 LOC, `policy_manager.py` 338, `odav_loop.py` 316, `memory_store.py` 315, `audit_log.py` 307, `validation_engine.py` 286 | `wc -l` |
| VF-10 | HPID registry contains **449 platforms** with 32 scored columns, in JSON/YAML/CSV/SQLite, rebuildable from a live unauthenticated ABDM Strapi API | `platform_registry.csv` (450 lines incl. header); `PHASE0_DISCOVERY_REPORT.md` |
| VF-11 | The Government of India publishes **per-criterion product quality ratings** for certified platforms (16 criteria incl. "Ease of data capture by doctor", "OP Consultation", "Billing Module") | `sources/abdm_integrators_clean.json`; HPID §1.2 |
| VF-12 | Corpus evidence-label totals: **5,573 🟢 · 4,470 🟡 · 592 🔴** across all markdown | Emoji count across corpus |

### 📄 Supported by Documentation Only
- JARVIS README claims "Level-6 Autonomous Coding", "UI Vision & Automation ... automate *any* application", "Persistent Wake Service". `feature_flags/level6_engine.yaml` and `auto_mode.yaml` both carry `enabled: false`. **Documented intent, not implemented capability.**
- HPID README declares Phases 2–3 (dossiers, adapter architecture) as `PENDING` with `0/449` dossiers written.
- The 27-deliverable canon is a convention observed across dossiers; no governing spec document was found in the corpus.

### 🧠 Architectural Inferences (with justification)
| # | Inference | Justification |
|---|---|---|
| AI-01 | The 160 adapters are a **declared-surface strategy**, not a built integration layer — a namespace reservation that lets the planner route by platform before any real automation exists | 27-line median, 144/160 no-op verifiers, 140/160 navigate-only, all flags `enabled:false` |
| AI-02 | JARVIS's genuine intellectual asset is the **ODAV control loop plus policy/feature-gate/audit scaffolding**, not the adapters | Those modules carry the real LOC; adapters carry almost none |
| AI-03 | The dossier corpus was produced by a **single templated pipeline** run per target (same 27 deliverables, same emoji grammar, same 2026-07-25 date) | 12/21 hit 27/27 canon coverage; identical label legends across independent targets |
| AI-04 | Ovexis' implicit thesis, read from what was chosen for study, is a **longitudinal AI health-intelligence platform** sitting between consumer biometrics (D05, D12, D14, D16, D19), clinical evidence (D06, D07, D08, D15, D18) and Indian care delivery (D09, D10, D11, D17) | The selection itself is the signal; no explicit thesis doc exists in the corpus |

### 🔴 Speculation (isolated, never load-bearing)
- The empty Dissection repo plus issue-attachment delivery suggests corpus assembly outran repository hygiene — a process observation, not a finding.
- The unmerged `phase-2-adapter-wiring` branch may contain materially more adapter logic than the default branch. **Untested. Must be verified in Phase 1, not assumed.**

### ❓ Unknowns (require evidence)
1. Do `phase-1-code-engine-fix` and `phase-2-adapter-wiring` contain implementation absent from the default branch?
2. Is the 21-artifact corpus complete, or is this batch 1 of N?
3. Does an Ovexis product/thesis document exist outside these two repositories?
4. Is there a real Ovexis codebase distinct from JARVIS?
5. What is the funding/runway/team state? Nothing in the corpus states it — this bounds Phase 12 (capital allocation) and Phase 15 (hiring priorities).
6. Are the XLSX/CSV feature inventories richer than their markdown counterparts? (Not yet parsed; Phase 3 input.)

### ⚠️ Contradictions (documentation vs implementation)
| # | Contradiction | Resolution rule |
|---|---|---|
| C-01 | README: "automate *any* application" ↔ 144/160 adapters cannot verify their own success | 🔵 Code wins. Adapters are stubs. |
| C-02 | README: "Level-6 Autonomous Coding" ↔ `level6_engine.yaml: enabled: false` | 🔵 Code wins. Deferred, not delivered. |
| C-03 | **G01 panel A** ("clear stage discipline, appropriate deferral") ↔ **G01 panel B** ("does NOT represent a product healthcare organisations would pay for") | **Both are correct against different yardsticks.** Protocol requires judging each stage against its declared objective → Panel A is the admissible verdict for *today's* repo; Panel B is admissible only as a *Stage-3 gap register*. Recorded as **DL-003**. |
| C-04 | README markets a privacy-first local assistant ↔ `memory_store.py` ships XOR "encryption" with a hardcoded key | 🔵 Code wins. Stage-0 technical debt, blocking for any PHI. |
| C-05 | Dissection described as containing dossiers ↔ repository is empty | Resolved: content is in Issue #1. Provenance risk, not content gap. |

### 🕳️ Research Gaps
- Unmerged branches unexamined (blocking accurate Phase 11 baseline).
- 29 XLSX / 14 CSV inventories not yet parsed — these hold the structured feature data Phase 3 needs.
- 62 screenshots and 67 raw HTML/JS captures unread — these are the strongest 🟢 evidence in the corpus and the only defence against inherited hallucination.
- No payer, hospital-CIO, or clinician primary research anywhere in the corpus. Every claim about buyer behaviour is currently second-hand.
- No pricing/contract evidence for enterprise HMIS or EHR incumbents (Epic, Cerner, Meditech absent as dossier targets).
- Regulatory corpus is thin: DPDP Act 2023, ABDM policy, HIPAA, EU AI Act, FDA SaMD are referenced but no dedicated regulatory dossier exists.

### 📒 Decision Ledger — Phase 0
| ID | Decision | Rationale | Reversible? |
|---|---|---|---|
| DL-000 | Treat Issue #1 attachments as the canonical Dissection corpus; snapshot locally to `/home/user/dissection/` | Repo is empty; issue attachments are the only source | Yes — supersede if repo is populated |
| DL-001 | All JARVIS measurements taken on the **default branch**, stated explicitly; other branches are separate evidence | Prevents silent conflation of branch states | No |
| DL-002 | **Phase 16 extends HPID (I01); it does not rebuild it.** HPID becomes the schema spine of the Healthcare Platform Intelligence Database | I01 is already populated, queryable and refreshable from a live govt API | Yes, if schema proves unfit |
| DL-003 | Where G01's two panels conflict, Panel A (stage-disciplined) governs *current-state* claims; Panel B is retained in full as the *Stage-3 gap register* | Protocol: judge each stage against its declared objective | No |
| DL-004 | Adopt the corpus's 🟢/🟡/🔴 grammar, extended with ⚪ Cannot-Verify and 🔵 Code-Backed | Continuity with source dossiers + protocol's code-over-docs rule | No |
| DL-005 | Permanent firewall: Dissection ≠ JARVIS ≠ Ovexis; no phase may equate them | Explicit engagement instruction | No |
| DL-006 | Phase 1 will score all 21 artifacts on 9 axes **without merging any of them** | Protocol prohibits merging before validation | No |

### 📊 Confidence Score — Phase 0

| Dimension | Score | Justification |
|---|---|---|
| Corpus location & retrieval | **HIGH** | Every artifact downloaded, extracted, counted; zero errors |
| Repository state verification | **HIGH** | GitHub REST API + local clone; all numbers reproducible |
| JARVIS implementation baseline | **HIGH** *(default branch only)* | Direct static analysis; 3 unmerged branches unexamined → drops to MEDIUM for "what JARVIS is overall" |
| Dossier content quality | **NOT YET ASSESSED** | Deliberately deferred to Phase 1 — Phase 0 counts, it does not judge |
| Corpus completeness | **LOW** | Unknown whether 21 artifacts is the full intended set — Intake Question 1 |
| Ovexis business context | **LOW** | No funding, team, runway, or thesis document exists in evidence |
| **Overall Phase 0 confidence** | **HIGH for what was measured; LOW for what was not supplied** | The evidence base is real, large and usable. Its boundaries are unknown until the Board answers below. |

---

## 0.7 THE MINIMUM INTAKE QUESTIONS

Only five. Each one changes the output materially; nothing else is asked.

**Q1 — Corpus completeness.** Are these 21 artifacts the complete intended corpus, or is this batch 1 of several? *(Phase 1 scoring and Phase 2 market reconstruction change shape if more dossiers — especially EHR incumbents or payers — are coming.)*

**Q2 — Primary decision objective for the next 90 days.** Which single decision must this engagement serve first: (a) JARVIS Stage-1 engineering plan, (b) Ovexis category positioning and beachhead choice, (c) an investor/board fundraising narrative, or (d) a build-vs-buy/partnership map? *(This sets what Phases 11, 12 and 15 optimise for.)*

**Q3 — Beachhead geography.** Is Ovexis' first market India (ABDM/DPDP/NHCX rails, where I01's 449-platform registry is a direct weapon), the US (HIPAA/FHIR/payer rails, where 13 of 19 dossiers sit), or explicitly both? *(This determines the entire regulatory and integration strategy.)*

**Q4 — Output format and depth per phase.** Preferred deliverable shape: (a) one canonical markdown file per phase in the workspace (my default), (b) markdown + machine-readable JSON/CSV/SQLite from Phase 1 onward rather than only at Phase 16, or (c) formal DOCX/PPTX board packages at the milestone phases (15 and Ω)?

**Q5 — Confidentiality and unstated context.** Is there anything confidential I should hold to the workspace only, and — more importantly — does material exist that is *not* in these two repositories (an Ovexis codebase, funding state, team size, existing hospital pilots or LOIs, a founder thesis document)? *(Right now Phases 12 and 15 would be written with zero knowledge of Ovexis' actual capital, team or traction. I would rather ask than infer.)*

---

## PHASE 0 COMPLETE

Stopping here as instructed. Phase 1 (Report Validation — independent scoring of all 21 artifacts on 9 axes, no merging) will begin only on your instruction, and will incorporate your answers above.
