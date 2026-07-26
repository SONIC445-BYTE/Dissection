# PHASE 15 — BOARD MEMO
## Ovexis / JARVIS · Executive Board Package

**Phase:** 15 of 16 (+ Ω) · **Date:** 2026-07-26 · **Status:** COMPLETE — canonical
**Outputs:** `exports/phase15_board_memo.{json,yaml}`, `exports/phase15_risks.csv`, `exports/phase15_roadmap.csv`
**Classification:** Internal — Board Strategy

---

## 1. EXECUTIVE SUMMARY

The healthcare software market has built an enormous capacity to produce recommendations and almost no capacity to execute them. Four independent measurement methods confirm it: AI language outweighs automation language **13.3×**; **52.4%** of shipped product DNA sits before the point of commitment versus **12.9%** at it; the patient journey has a handoff break rate of **0.00** while ICU, emergency and administration sit at **1.00**; and of 28 corroborated market patterns, **exactly one** operates at the commit layer — and it is orchestration mislabelled as execution.

This is the **commit gap**, and it is self-sealing. Because software stops at the recommendation, no outcome data is generated, so recommendations cannot improve, so trust never rises enough to permit execution.

JARVIS's two largest modules — UI execution and workflow orchestration — sit precisely in this gap. That is the opportunity.

**But the reachability audit found that 76% of JARVIS's production code never runs, and the entire safety stack — policy engine, permission engine, audit log, memory store — is orphaned with zero non-test importers.** Safety code that does not execute is worse than absent code, because it creates false confidence. Nobody, including two prior due-diligence panels and my own earlier phases, had measured this.

**Recommendation:** Ovexis should become the **operational execution agent** for Indian private hospitals, entering in shadow mode across disconnected operational and financial workflows. Before any of that: merge 9,713 unmerged lines, add CI, and wire the safety stack. And do not commit to the beachhead until the 82 ABDM demo videos answer whether HMIS vendors already cover these workflows.

---

## 2. INDUSTRY RECONSTRUCTION

Twelve layers measured by attention: **AI (2,762) · hospital (1,170) · patient (1,081) · workflow (1,017) · data (704) · infrastructure (593) · insurance (590) · identity (536) · clinical (491) · government (475) · decision (473) · automation (208).**

The market is a crowded periphery — 6 sensor companies, 6 marketplaces, 4 knowledge corpora — arranged around an **unexamined centre**: not one of 19 studied companies occupies the system of record. India has **253 HMIS vendors** where the US has ~5.

## 3. COMPETITIVE LANDSCAPE

19 dossiers scored on 9 axes (mean overall **4.55/10**, mean evidence quality **4.11/10**). All produced by one pipeline on one date — 49 files share a legend — so apparent consensus was treated as correlated, not corroborating.

## 4. FEATURE GENOME

**1,277 feature rows → 55 canonical concepts.** Highest strategic value: `protocol_commitment` (SI 9.6, highest user value in the entire genome, built by only 6 of 17 companies). JARVIS covers 13 of 55 concepts; **42 have zero code**, including every healthcare-domain concept.

## 5. WORKFLOW GENOME

**16 journeys × 137 stages, 84 measured.** 23 crowded · 24 contested · 18 unowned · **14 true gaps** · 5 discussed-not-owned. Nursing: 4 of 6 stages are true gaps and **0 of 449 government-certified platforms mention nursing at all**.

## 6. KNOWLEDGE GRAPH

Machine-readable across 8 export families — market model, product genome, workflow model, patterns, whitespace, first principles, system dynamics, architecture. See §24 and the HPID handoff in Phase 16.

## 7. MARKET LAWS (12)

LAW01 hospitals rarely replace the SoR · **LAW02 software that cannot complete an action cannot learn from it** · LAW03 attention follows data availability not labour intensity · LAW04 liability not capability bounds automation · **LAW05 standards govern exchange between institutions, never operations inside them** · LAW06 consumer subscription is the fallback of the institutionally blocked · LAW07 trust is manufactured by traceability · LAW08 only the clinician creates value · LAW09 continuity is inverse to institutional depth · LAW10 the most crowded capability is least defensible · LAW11 fragmentation raises interface value · **LAW12 government rails create counterparty networks before products exist**.

## 8. ENGINEERING LAWS (12)

Protocol over platform · Verification over automation · **Honest failure over silent success** · Policy over prompts · Adapters over replacements · Graduated autonomy per action class · Local reasoning for PHI · **Depth-first over breadth-first** · State lives in the system not the human · Provenance is a first-class output · **Unreachable code is not capability** · **Merge before you build**.

## 9. STRATEGIC OPPORTUNITIES

25 units of human work ranked and **stress-tested across 5 weightings including one that deletes JARVIS-readiness entirely**. Five survive every scenario: OT scheduling, claim validation, adjudication liaison, charge capture, claim submission. Four of five are the billing chain — and NHCX already has **38 partners live including 12 insurers and 4 TPAs**.

## 10. TOP RISKS

| Risk | Severity | Mitigation | Status |
|---|---|---|---|
| HMIS vendors already cover Tier-1 workflows | CRITICAL | 82 demo videos before commitment (DL-066) | **BLOCKING** |
| No moat for 12+ months | HIGH | Reframed to domain+policy+provenance; accept the exposure | **ACCEPTED** |
| No budget line exists for the category | HIGH | Attach to HMIS AMC or claims-recovery % (DL-068) | **MITIGATED** |
| CIO rejects unproven solo vendor | CRITICAL | SHADOW-mode entry (DL-069), already in feature_gate | **MITIGATED** |
| Indian unit economics never justify integration effort | HIGH | Validate with one hospital before scaling | **UNVALIDATED** |
| OpenAI commoditises computer-use | HIGH | Moat is domain+policy+provenance, not clicking (DL-070) | **MITIGATED** |
| Orphaned safety stack creates false confidence | CRITICAL | Stage 0 mandatory before features (DL-057) | **ACTIONABLE NOW** |
| Solo builder capacity | HIGH | Sequencing over volume (DL-052); no hires until proof (DL-064) | **STRUCTURAL** |

## 11. CAPITAL PRIORITIES

Stage 0 requires **zero capital**. If capitalised: (1) one design-partner hospital, (2) ABDM sandbox integration, (3) explicitly **not** marketing. No financial data about Ovexis exists in evidence — this advice is conditional.

## 12. HIRING PRIORITIES

**No hires until one workflow completes end-to-end in one hospital.** First hire is a hospital-operations person, not an engineer — the pivotal unknown is domain, not capacity.

## 13. 18-MONTH ROADMAP

| Period | Theme | Gate |
|---|---|---|
| Month 0-1 | **Stage 0 - Recover the baseline** — Merge branch; CI; wire policy/permission/audit; AES-GCM; quarantine 149 adapters; watch 82 demo videos | Test suite green in CI; G-4.2 answered |
| Month 2-4 | **Workflow engine + one workflow** — Build durable workflow engine (protocol_commitment); per-action-class autonomy; mandatory fail-closed verification | One workflow runs end-to-end in dry-run |
| Month 5-8 | **One hospital, shadow mode** — Design-partner hospital; SHADOW observation; measure break points; ABDM sandbox M1-M3 | Shadow data proves the disconnection thesis |
| Month 9-12 | **First completions** — Move from SHADOW to SUGGEST to FORCE on the single lowest-risk action class; NHCX claims client | First verified completed workflow; R6 flywheel starts |
| Month 13-18 | **Second workflow, second hospital** — Only after the first completes; institutional knowledge graph; first hire (hospital ops) | Two workflows, two hospitals, outcome data accumulating |

## 14. 5-YEAR VISION

The execution layer across 50+ Indian hospitals, with adapter coverage and completed-workflow outcome data compounding into a defensible position. Claims chain automated end-to-end on the NHCX rail. Selective US entry via a clearinghouse partnership — never by porting.

## 15. 10-YEAR VISION

**The system that completes healthcare work.** Every other layer recommends; Ovexis commits, verifies and proves. The moat is the accumulated record of what actually worked — data no competitor can buy because only completion generates it.

## 16. JARVIS ARCHITECTURE RECOMMENDATIONS

20 layers assessed: 6 reachable · 7 partial · 4 orphaned · 3 absent. **Priority order:** wire policy → wire audit → replace XOR → freeze adapters at 14 → build the workflow engine → ABDM/NHCX clients.

## 17. OVEXIS PLATFORM RECOMMENDATIONS

Single-tenant on-prem agent per hospital. Model-agnostic. Local inference for PHI, cloud for general reasoning. **No SDK until 10 workflows complete.**

## 18. ACQUISITION TARGETS

- None recommended - no capital, no team (DL-007). Listed for completeness only.
- If capitalised: a small ABDM-certified connector vendor (14 in Connectors category) for instant certification + customer list

## 19. PARTNERSHIP TARGETS

- The 13 NHA-rated HMIS vendors (govt-published quality scores) - free qualified target list
- Eka Care/Orbi Health (4.5), Drucare (4.5), MocDoc/Yro (4.4), Plus91 (4.3), HODO (4.1)
- NHCX connectors (6 registered) for the claims chain

## 20. RESEARCH PRIORITIES

- P0 BLOCKING: 82 ABDM demo videos - do HMIS vendors already cover Tier-1 workflows? (G-4.2, RT01)
- P0: Unit economics of one Indian hospital deployment (RT06, G-6.1)
- P1: Reachability of remaining 455 orphaned modules - wire or delete 18,558 LOC
- P1: Windows hardware validation of the 12 wired adapters (G-1.1)
- P2: Primary clinician/CIO interviews - entirely absent from corpus
- P2: Local model latency/cost for clinical text (G-1.5)

## 21. KILL LIST

- The 149 fabricated platform adapters - quarantine or delete (CB-04)
- Any dashboard-as-product ambition (LAW10, DL-045)
- Ambient scribing (19 competitors, automates a billing artifact) (DL-049)
- Consumer subscription revenue (R4 trap, hard ceiling) (LAW06)
- Multi-agent architecture (coordination failure modes a solo builder cannot debug)
- Outcome-based pricing as the ENTRY model (RT04 circular dependency)

## 22. NEVER BUILD LIST

- An EHR or HMIS - 0 of 19 companies occupy the SoR and all arranged around it (LAW01)
- A foundation model - arch_llm_wrapper GREEN at 18 companies = commodity
- Clinical decision support while solo - all clinical opportunities liability-blocked (LAW04)
- A platform/SDK before 10 workflows complete - repeats the 149-adapter mistake
- Nursing continuous observation - no digital artifact, highest liability, ranked 25/25

## 23. IMMEDIATE WINS

- Merge phase-2-adapter-wiring into main; make main default (9,713 lines, 325 vs 7 passing tests)
- Add CI running the existing test suite
- Wire policy_manager + permission_engine (338+301 LOC, currently ZERO non-test importers)
- Wire audit_log as append-only (307 LOC, orphaned)
- Replace memory_store XOR+hardcoded key with AES-GCM
- Watch the 82 ABDM demo videos - closes the single blocking unknown G-4.2

## 24. LONG-TERM BETS

- Durable workflow engine as protocol_commitment (Phase-3 highest-value concept, SI 9.6)
- Institutional knowledge graph of cross-departmental state (AN05)
- Agent-native claims rule acquisition learning from denial feedback (AN02)
- Voice-native nursing capture to CREATE the missing digital artifact (AN04)

---

## 25. DECISION REGISTER

**73 decisions logged (DL-000 → DL-073).** Load-bearing: DL-007 (solo constraint) · DL-010 (canonical branch) · DL-012 (corroboration rule) · DL-019 (commit gap frame) · DL-020 (never replace SoR) · DL-040 (digital artifact gate) · DL-046 (UI automation durable for internal ops) · DL-050 (trust loop is core) · DL-057 (Stage 0 first) · DL-066 (beachhead evidence-gated) · DL-071 (disconnected, not unowned).

## 26. CONFIDENCE REGISTER

| Domain | Confidence |
|---|---|
| Commit gap thesis | **HIGH** — 4 independent methods |
| JARVIS code ground truth | **HIGH** — reachability verified twice |
| Market structure | **MEDIUM-HIGH** |
| Beachhead selection | **MEDIUM-LOW** — evidence-gated (RT01) |
| Unit economics | **NONE** — no data exists |
| Pricing | **NONE** — all 7 patterns failed corroboration |
| Clinical benefit | **NOT ASSESSED** — absent from corpus |

## 27. EVIDENCE REGISTER

21 artifacts · 365,728 analytical words · 1,277 feature rows · 449-platform government registry · 4 JARVIS branches · 3 live API probes (ABDM partners, integrators, NHCX). **Two measurement errors found and disclosed** (`\borm\b` 10× over-count; failure-vocabulary under-detection).

## 28. OPEN QUESTIONS

1. **Do HMIS vendors already cover Tier-1 workflows?** (BLOCKING — 82 demo videos)
2. What are the unit economics of one Indian hospital deployment?
3. Is the 18,558 LOC of orphaned code abandoned or staged?
4. Do the 12 wired adapters work on real Windows hardware?
5. Would a CIO accept a shadow-mode agent from a solo founder?
6. What is Ovexis's actual capital, runway and traction? *(Never supplied.)*

---

## PHASE 15 COMPLETE — proceeding to Phase 16.
