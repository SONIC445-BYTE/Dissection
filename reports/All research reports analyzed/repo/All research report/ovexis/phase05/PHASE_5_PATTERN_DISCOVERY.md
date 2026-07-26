# PHASE 5 — COMMON PATTERN DISCOVERY
## 73 Patterns Measured · 28 Survive Corroboration · 37 Downgraded

**Engagement:** Ovexis / JARVIS Strategic Intelligence Synthesis (OISE)
**Phase:** 5 of 16 (+ Phase Ω)
**Date:** 2026-07-26 (Asia/Calcutta)
**Status:** COMPLETE — canonical
**Inputs:** Phases 0–4 (canonical)
**Machine-readable outputs:** `exports/phase5_patterns.{json,yaml,csv}`, `registry/phase5_patterns.json`

---

## 5.0 METHOD — DL-012 AS A MEASUREMENT, NOT A DISCLAIMER

Phase 1 established that this corpus is **not 19 independent observations**: 49 files share one label legend, all 21 artifacts carry the same date, 12 hit identical 27/27 canon coverage. Phase 5's method — counting recurrences — is therefore the single phase most exposed to mistaking *one generator's priors repeated nineteen times* for *market consensus*.

**DL-012 was implemented as a hard filter in the measurement itself**, not appended as a caveat:

| Label | Requirement |
|---|---|
| 🟢 **GREEN** | Corroborated **AND** ≥8 companies |
| 🟡 **YELLOW** | Corroborated **OR** ≥8 companies |
| ⚪ **WEAK** | Neither — **downgraded, not deleted** |

Where *corroborated* = **cross-geography** (≥2 India-carried AND ≥2 US-carried dossiers) **OR** **cross-artifact-class** (appears in primary data — G01 code ground truth or I01 government registry — plus ≥3 dossiers).

61 candidate patterns across 9 families were instrumented at a ≥3-mention participation bar, then 16 failure/bottleneck patterns were re-measured (see 5.0.1). **73 patterns final.**

### 5.0.1 A second regex failure, caught and corrected

My first failure/bottleneck pass returned near-zero: `bot_data_acquisition` 0, `onb_quiz_intake` 0, `fail_billing_cancellation` 0, `bot_clinician_time` 2 hits. That contradicted Phases 1–4, which surfaced abundant complaint evidence.

Probing the corpus's actual failure vocabulary showed the detectors were far too narrow:

| Term | Hits | Artifacts |
|---|---|---|
| trust | 800 | 20 |
| risk | 717 | 20 |
| cost | 449 | 20 |
| fail | 287 | 19 |
| gap | 278 | 20 |
| complaint | **176** | **17** |
| friction | **155** | **19** |
| weakness | 126 | 20 |
| churn | 91 | 16 |

All 16 failure/bottleneck patterns were re-specified against the corpus's real language and re-measured. Reported rather than silently fixed, per **DL-016** — this is the second such correction in the engagement (after the `\borm\b` 10× error in Phase 2), which is itself becoming a pattern worth noting about term-density methods.

---

## 5.1 THE 28 CORROBORATED PATTERNS

Ranked by corroboration, then ubiquity, then intensity. Full table in `exports/phase5_patterns.csv`.

| # | Pattern | Family | Cos | Geo✓ | Class✓ | Commit position |
|---|---|---|---|---|---|---|
| 1 | int_ehr_fhir | integration | **20** | ✓ | ✓ | before |
| 2 | sec_hipaa_baa | security | **20** | ✓ | ✓ | wrapper |
| 3 | ux_dashboard_home | ux | 19 | ✓ | ✓ | before |
| 4 | int_lab_network | integration | 19 | ✓ | ✓ | before |
| 5 | arch_llm_wrapper | architecture | 18 | ✓ | ✓ | before |
| 6 | **arch_agentic_multistep** | architecture | 18 | ✓ | ✓ | **AT COMMIT** |
| 7 | arch_api_platform | architecture | 17 | ✓ | — | before |
| 8 | ai_citation_grounding | ai | 17 | ✓ | ✓ | before |
| 9 | sec_encryption | security | 17 | ✓ | ✓ | wrapper |
| 10 | ai_confidence_calibration | ai | 16 | ✓ | — | wrapper |
| 11 | sec_soc2_iso | security | 16 | ✓ | ✓ | wrapper |
| 12 | **bot_incumbent_lockin** | bottleneck | **16** | ✓ | ✓ | non-product |
| 13 | arch_rag_over_corpus | architecture | 14 | ✓ | — | before |
| 14 | int_wearable_sdk | integration | 14 | ✓ | — | before |
| 15 | arch_mobile_first_app | architecture | 13 | ✓ | — | wrapper |
| 16 | arch_human_in_loop | architecture | 13 | ✓ | — | human fallback |
| 17 | arch_cloud_saas_multitenant | architecture | 12 | ✓ | ✓ | before |
| 18 | fail_billing_cancellation | failure | 12 | ✓ | — | non-product |
| 19 | int_abdm_national | integration | 11 | ✓ | ✓ | before |
| 20 | fail_engagement_dropoff | failure | 11 | ✓ | ✓ | non-product |
| 21 | bot_cac_distribution | bottleneck | 11 | ✓ | — | non-product |
| 22 | sec_dpdp_gdpr | security | 11 | ✓ | — | wrapper |
| 23 | fail_retention_churn | failure | 11 | ✓ | — | non-product |
| 24 | ux_streak_habit | ux | 10 | ✓ | — | wrapper |
| 25 | adopt_land_expand | adoption | 10 | ✓ | — | non-product |
| 26 | adopt_content_seo | adoption | 9 | ✓ | — | non-product |
| 27 | arch_data_lake_longitudinal | architecture | 8 | ✓ | — | before |
| 28 | ux_single_score | ux | 8 | ✓ | — | before |

**8 YELLOW:** arch_on_device_local (7), fail_hardware_compat_backlash (6), fail_privacy_consent_trust (6), fail_data_privacy (6), fail_clinical_regulatory_boundary (6), sec_consent_granular (5), plus 2 duplicates from the re-measurement.

---

## 5.2 THE FINDING THAT MATTERS MOST

### F-5.1 — Only 1 of 28 corroborated patterns operates at the commit layer

| Position | GREEN patterns |
|---|---|
| Before commit | **12** |
| Wrapper | 7 |
| Non-product (failure/bottleneck/adoption) | 7 |
| **At commit** | **1** |
| Human fallback | 1 |

The single at-commit pattern is `arch_agentic_multistep` (18 companies) — and Phase 3 already flagged the granularity problem here (**C-14**, DL-027): that concept conflates *routing/orchestration* with *execution*. Companies claiming "agents" overwhelmingly mean planners and tool-callers, not systems that complete transactions.

> **This is the fourth independent confirmation of the same structure**, each by a different method:
> - Phase 2: language density — AI 2,762 vs automation 208 (**13.3×**)
> - Phase 3: shipped features — 52.4% before commit vs 12.9% at commit
> - Phase 4: workflow ownership — patient journey break rate 0.00 vs institutional 1.00
> - Phase 5: **corroborated patterns — 12 before-commit vs 1 at-commit**
>
> Four methods, four datasets, one answer. Under DL-012's own logic this is the most robust finding in the engagement.

### F-5.2 — Incumbent lock-in is the strongest bottleneck in the market

`bot_incumbent_lockin`: **16 companies, 209 hits, corroborated on both geography and class** — the highest-scoring bottleneck and 12th-ranked pattern overall.

This is the measured form of Phase 2's F-2.4 (0 of 19 companies occupy the system of record) and directly validates the engagement brief's own proposed LAW 1 (*"Hospitals rarely replace their core HMIS"*) with cross-corroborated data rather than assertion.

Strategic consequence: **DL-020 (do not attempt to replace the HMIS) is now GREEN-corroborated**, not merely inferred.

### F-5.3 — Every pricing pattern failed corroboration

All 7 pricing patterns scored WEAK: annual membership (5 cos, **0 India**), hardware+subscription (5, 1 India), monthly (4), freemium (3), enterprise seat (3, 0 India), transparent flat (3), usage-based (2, 0 India).

This is DL-012 working exactly as designed. Pricing appears frequently in the corpus, but **almost exclusively in US-carried consumer dossiers**. There is no cross-geography evidence for *any* pricing model.

🟡 **Strong Inference:** Ovexis cannot inherit a pricing model from this corpus. Phase 12 must derive pricing from first principles or from primary research — not from the dossiers. Recorded as **DL-034**.

### F-5.4 — The failure pattern that recurs most is commercial, not technical

Top corroborated failures: `fail_billing_cancellation` (12 cos, **206 hits**), `fail_engagement_dropoff` (11), `fail_retention_churn` (11, 94 hits), `bot_cac_distribution` (11, 91 hits).

Meanwhile `fail_accuracy_interpretation` (4 cos), `fail_manual_burden` (3), `fail_support_responsiveness` (3) all failed corroboration.

🟡 **Strong Inference:** these companies fail at **retention and unit economics**, not at technology. Combined with Phase 2's F-2.7 (reimbursement paradox — 19/21 discuss payer revenue, nearly all actually bill consumers), the picture is consistent: consumer-subscription healthcare has a structural retention problem, and the corpus's own dossiers say so about each other.

This strengthens **AI-11** (consumer subscription is a revenue trap with a hard ceiling) from inference toward corroborated pattern.

### F-5.5 — Security and compliance are table stakes, uniformly

`sec_hipaa_baa` (20 cos), `sec_encryption` (17), `sec_soc2_iso` (16), `sec_dpdp_gdpr` (11) — all GREEN, all cross-geography.

But `sec_consent_granular` scores only **5 companies (YELLOW)** — and Phase 4 found `compliance·consent_capture` is a *discussed-but-unowned* stage (8 hits, 4 companies, built by ~0).

🟡 **Strong Inference:** the market has converged on **perimeter security** (encryption, certifications, BAAs) and has *not* converged on **granular consent** — despite consent being the legal precondition for every data flow under both ABDM and HIPAA. This is a real asymmetry: compliance-as-certification is solved; compliance-as-runtime-capability is not.

### F-5.6 — Architecture has converged; the corpus shows one blueprint

Nine architecture patterns, seven GREEN: LLM wrapper (18), agentic multi-step (18), API platform (17), RAG over corpus (14), mobile-first (13), human-in-loop (13), cloud SaaS multi-tenant (12), data lake longitudinal (8).

The modal architecture in this market is: **mobile-first app → cloud multi-tenant SaaS → API surface → longitudinal data store → RAG over corpus → LLM → agentic planner → human in the loop before anything consequential.**

`arch_on_device_local` scores only 7 (YELLOW) — and its corroboration comes from **class, not geography**: the primary carrier is G01 (JARVIS itself, which is local-first by design).

🟡 **Strong Inference:** JARVIS's local-first architecture is **genuinely differentiated** — it is the one architectural choice in the engagement that the market has *not* converged on. Whether that is an advantage or an isolation is a Phase 7/13 question; Phase 5 records only that it is rare.

---

## 5.3 WHAT THE DOWNGRADE CAUGHT

37 patterns failed corroboration. The most important downgrades — claims the corpus asserts confidently that the evidence does **not** support as market-wide:

| Pattern | Cos | Why downgraded |
|---|---|---|
| ai_personalisation_context | 6 | **0 India carriers** — US-consumer-only |
| adopt_influencer | 5 | 0 India — a US consumer-brand tactic, not a healthcare pattern |
| pri_annual_membership | 5 | 0 India |
| pri_enterprise_seat | 3 | 0 India |
| onb_concierge_white_glove | 6 | 1 India — economics don't transfer |
| ai_red_team_eval | 6 | 1 India, no primary corroboration |
| fail_accuracy_interpretation | 4 | 0 India — surprisingly weak given AI ubiquity |
| ux_conversational | 2 | Near-absent as a *measured* pattern despite universal AI talk |
| bot_clinician_capacity | **0** | 2 hits corpus-wide — the corpus does not actually study clinician time |
| bot_integration_effort | 1 | 14 hits — **the corpus barely discusses integration cost** |

**F-5.7 — The corpus systematically under-measures the bottlenecks that matter to a builder.** Clinician capacity (0), integration effort (1), regulatory burden (1), data acquisition (1) all failed — while CAC/distribution (11) passed comfortably.

🟡 **Strong Inference:** these dossiers were written from a *go-to-market* perspective, not an *engineering* one. They know what blocks selling; they do not know what blocks building. Given Q2 (JARVIS engineering plan is the objective), this is a material limitation and directly bounds what Phases 10–11 can inherit. Recorded as **DL-035**.

---

## 5.4 END-OF-PHASE DELIVERABLES — PHASE 5

### ✅ Completed
- 73 patterns across 9 families instrumented and measured across all 21 artifacts.
- DL-012 corroboration test implemented as a hard filter: 28 GREEN, 8 YELLOW, 37 WEAK.
- Failure/bottleneck families re-measured after first regex set was proven too narrow; both passes reported.
- Every GREEN pattern mapped to its Phase-3 genome concept and commit-gap position.
- Fourth independent confirmation of the commit-gap structure obtained.
- Downgraded patterns preserved, not deleted, with reasons recorded.

### 🟢 Verified Facts
| # | Fact | Evidence |
|---|---|---|
| VF-49 | 73 patterns measured; **28 GREEN, 8 YELLOW, 37 WEAK** under DL-012 | Corroboration test |
| VF-50 | GREEN by position: **12 before-commit, 7 wrapper, 7 non-product, 1 at-commit, 1 human-fallback** | Genome mapping |
| VF-51 | `int_ehr_fhir` and `sec_hipaa_baa` tie as most universal patterns (**20 of 21 artifacts**) | Measurement |
| VF-52 | `bot_incumbent_lockin` = 16 companies, 209 hits, corroborated both axes | Measurement |
| VF-53 | **All 7 pricing patterns failed corroboration**; 4 of 7 have zero India carriers | Measurement |
| VF-54 | Corpus failure vocabulary: complaint ×176 (17 artifacts), friction ×155 (19), churn ×91 (16) | Vocabulary probe |
| VF-55 | `bot_clinician_capacity` = **2 hits corpus-wide**; `bot_integration_effort` = 14 | Re-measurement |
| VF-56 | `arch_on_device_local` corroborated only via primary class (G01/JARVIS), not geography | Corroboration test |

### 📄 Supported by Documentation Only
- Pattern participation is measured by **term frequency in dossier prose**, which is evidence of *discussion*, not of *implementation*. A company scoring on `arch_agentic_multistep` may be described as agentic without shipping agents. Phase 5 measures the corpus's account of the market, one layer removed from the market.

### 🧠 Architectural Inferences
| # | Inference | Justification |
|---|---|---|
| AI-25 | The market has **one modal architecture**; differentiation is not architectural | 7 of 9 architecture patterns GREEN and cross-geographic |
| AI-26 | JARVIS's local-first design is the **single non-converged architectural position** in the engagement | arch_on_device_local: 7 cos, class-corroborated only via JARVIS itself |
| AI-27 | Compliance has bifurcated: **perimeter security converged, runtime consent did not** | sec_* all GREEN; sec_consent_granular YELLOW at 5; Phase-4 consent_capture unowned |
| AI-28 | These are **go-to-market dossiers, not engineering dossiers** — they measure selling friction, not building friction | F-5.7 |
| AI-29 | Consumer-subscription healthcare's dominant failure mode is **commercial (retention/CAC), not technical** | F-5.4 + Phase-2 F-2.7 |

### 🔴 Speculation
- `arch_agentic_multistep` at 18 companies may collapse to near-zero if re-measured against *shipped* agentic execution rather than described intent. Testable only with product access. **Would strengthen, not weaken, F-5.1.**
- Local-first may become a regulatory advantage under DPDP data-localisation pressure. Unverified; flagged for Phase 7.

### ❓ Unknowns
1. Do the 18 `arch_agentic_multistep` companies ship agents that *complete* actions, or only plan them? (Requires product access.)
2. Why does the corpus barely discuss integration cost (14 hits) when Phase 2 found 253 fragmented HMIS vendors? Likely the go-to-market lens (AI-28) — untested.
3. Is granular consent unowned because it is hard, or because nobody is paid for it?
4. Would pricing patterns corroborate against Indian primary sources outside this corpus?
5. 53 uninstrumented workflow stages (G-4.1) remain unpatterned.

### ⚠️ Contradictions
| # | Contradiction | Resolution |
|---|---|---|
| C-20 | `arch_agentic_multistep` is GREEN at-commit (18 cos) ↔ Phases 2/3/4 all found the commit layer nearly empty | Resolved by C-14/DL-027: the pattern captures *orchestration*, not *execution*. The label is aspirational. **Does not overturn F-5.1** |
| C-21 | `ux_conversational` scores 2 companies ↔ `arch_llm_wrapper` scores 18 | Chat *interface* is under-described while LLM *usage* is over-described. Measurement artifact of vocabulary, not a market fact. Logged per DL-016 |
| C-22 | My first failure-pattern pass returned ~0 ↔ corpus contains 176 "complaint" mentions | **My error, disclosed.** Corrected measurement canonical (§5.0.1) |

### 🕳️ Research Gaps
- **Carried:** no EHR-incumbent/payer dossier; no primary clinician research; 62 screenshots + 67 raw captures unread; no clinical-benefit data; no solo-builder effort model; 82 ABDM demo videos unopened (DL-033).
- **New G-5.1:** No engineering-side bottleneck evidence anywhere in the corpus (AI-28). Phases 10–11 must source this independently.
- **New G-5.2:** Pricing has no corroborated basis; Phase 12 cannot inherit one.
- **New G-5.3:** Pattern measurement is one layer removed from implementation — patterns describe descriptions.

### 📒 Decision Ledger — Phase 5
| ID | Decision | Rationale | Reversible? |
|---|---|---|---|
| DL-034 | **Pricing may not be inherited from this corpus.** Phase 12 derives it from first principles or primary research | All 7 pricing patterns failed corroboration; 4 have zero India carriers | Yes, on primary research |
| DL-035 | **The corpus is a go-to-market instrument, not an engineering one.** Phases 10–11 must treat its bottleneck claims as unreliable and source engineering constraints from code and primary data | clinician_capacity 2 hits, integration_effort 14 hits vs CAC 91 | No |
| DL-036 | **`bot_incumbent_lockin` is GREEN-corroborated** → DL-020 (never replace the HMIS) is upgraded from inference to corroborated pattern | 16 cos, 209 hits, both corroboration axes | No |
| DL-037 | Local-first is recorded as **JARVIS's one non-converged architectural position** — protected for evaluation in Phase 7, neither assumed advantage nor liability | AI-26 | Yes |
| DL-038 | All 37 WEAK patterns **retained in the export with reasons**; may be revived by future evidence, never silently reinstated | Protocol: preserve, don't delete | No |

### 📊 Confidence Score — Phase 5

| Dimension | Score | Justification |
|---|---|---|
| Corroboration discipline | **HIGH** | DL-012 implemented as a filter; 37 of 73 patterns downgraded, including all pricing |
| Commit-gap confirmation | **HIGH** | Fourth independent method reaching the same result |
| GREEN pattern validity | **MEDIUM-HIGH** | Cross-geography or cross-class verified; still term-frequency based |
| Failure/bottleneck patterns | **MEDIUM** | Corrected after a measurement error; corpus's own lens is commercial (AI-28) |
| Pricing patterns | **LOW** — deliberately | Zero corroboration; declared uninheritable |
| Engineering bottlenecks | **VERY LOW** | Corpus does not contain this evidence (G-5.1) |
| **Overall Phase 5** | **MEDIUM-HIGH** | What survived is well-corroborated; what didn't is explicitly quarantined |

---

## 5.5 THE THREE THINGS PHASE 5 CHANGES

1. **The commit gap now has four independent confirmations.** Language density, shipped features, workflow ownership, and corroborated patterns — 12 before-commit patterns against 1 at-commit, and that one is orchestration mislabelled as execution. This is the most robust finding in the engagement and the foundation for Phases 6, 7 and 11.
2. **DL-012 removed 37 of 73 patterns, including every pricing model.** Half the corpus's apparent consensus was single-pipeline echo. Ovexis cannot inherit pricing, personalisation-as-differentiator, concierge economics, or influencer distribution from this evidence. *(DL-034)*
3. **The corpus knows selling, not building.** Clinician capacity: 2 hits. Integration effort: 14. CAC: 91. Given the objective is a JARVIS engineering plan, Phases 10–11 must source engineering constraints from code and primary data, not from these dossiers. *(DL-035)*

---

## PHASE 5 COMPLETE

Machine-readable outputs:
- `ovexis/exports/phase5_patterns.{json,yaml,csv}` — 73 patterns × 14 fields, ranked, with corroboration flags (`ovexis.hpid.phase5.patterns/v1`)
- `ovexis/registry/phase5_patterns.json` — raw per-pattern carrier lists and hit counts

Stopping here as instructed. Phase 6 (White Space Intelligence — *"what important healthcare work still requires humans because software has failed?"*) awaits `Continue`.
