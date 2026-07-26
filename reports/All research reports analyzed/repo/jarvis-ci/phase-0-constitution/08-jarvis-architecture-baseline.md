# JARVIS Architecture Baseline
`v0.2.0` · Phase 0 · ⚠ **PARTIALLY GROUNDED — remaining assumptions flagged**

> **v0.2.0 update (2026-07-26):** Repository and staged blueprint now supplied. Several assumptions are resolved below. Full evidence in `phase-R-repo-dissection/`.
>
> **Resolved:** Q1 local-first (confirmed as intent, ⚠ contradicted by STT path) · Q2 desktop agent · Q3 RHINAL is a separate project with its own MCP server pending · Q4 India-first · Q6 **Stage 0 substantially built, Stage 1+ not started**.
> **Still open:** Q5 (buyer: hospital / clinician / developer) · Q7 (team size, funding posture).
>
> ⚠ **Critical grounding:** the repository contains **zero healthcare code** as of 2026-07-23. Layer postures below for L10/L11 are therefore *intended*, not *current*. Dossiers must not assume JARVIS occupies any healthcare layer today.

> **Read this first.** Every dossier's "Lessons for JARVIS", every Strategic Role classification, and every D9/D10 score is computed *relative to this file*. If this file is wrong, 84 dossiers are wrong in a correlated way — the worst kind of error, because it is invisible inside any individual dossier.
>
> Items marked **[ASSUMED]** were inferred from the project brief and must be corrected by you.
> Items marked **[CONFIRMED]** were stated explicitly.

---

## 1. What JARVIS is

**[CONFIRMED]** JARVIS is the umbrella system this knowledge base serves. It has a healthcare mission, an adapter strategy, a plugin/SDK ambition, a marketplace ambition, and a developer-ecosystem ambition.

**[CONFIRMED]** RHINAL is a JARVIS component with a **memory layer** (stated: *"Mem0 for RHINAL's memory layer"* as a competitive example).

**[ASSUMED]** Working definition, to be corrected:

> JARVIS is a **local-first, privacy-preserving AI operating layer** that observes, remembers, plans, and acts across the applications a user already runs — with healthcare as its first deep vertical, expressed through adapters over existing systems of record rather than replacement of them.

**Open questions that materially change the analysis:**

| # | Question | Why it changes everything |
|---|---|---|
| Q1 | Local-first/on-device, cloud, or hybrid? | Determines whether L0/L1/L2 are dependencies or non-issues, and whether privacy is a real moat or marketing |
| Q2 | Desktop agent, server platform, or both? | Determines whether L8 (OS AI) is existential or irrelevant |
| Q3 | Is RHINAL the memory subsystem specifically, or a broader runtime? | Determines the L3 competitive set precisely |
| Q4 | India-first, or global with India as beachhead? | Reweights ABDM vs FHIR/HL7 priority |
| Q5 | Sell to hospitals, clinicians, or developers? | Determines whether L10 players are partners or channel |
| Q6 | Current honest stage (S0–S4)? | Stage discipline applies to JARVIS too; roadmaps that assume S3 when reality is S1 cannot execute |
| Q7 | Team size and funding posture? | Determines what "we could build that" actually means |

---

## 2. Assumed layer posture

⚠ All **[ASSUMED]** — this table drives every D9/D10 score.

| Layer | Posture | Reasoning |
|---|---|---|
| L0 Compute | **Ignore/depend** | Cannot and should not contest |
| L1 Models | **Abstract** | Route across providers; never bind to one |
| L2 Inference | **Integrate** | Commodity; support local + hosted |
| **L3 Memory** | **OWN** ⭐ | RHINAL's stated territory. Core differentiation. |
| **L4 Planning** | **OWN** ⭐ | The other half of the agent core |
| L5 Perception | **Own abstraction, integrate parts** | Unified interface over commodity engines |
| L6 Execution | **Integrate** | Never rebuild browser/UI drivers |
| L7 Voice | **Integrate** | Commoditising fast |
| L8 OS AI | **Coexist/differentiate** ⚠ | Existential distribution risk |
| L9 Apps | **Selective** | Compete only where healthcare workflow wins |
| **L10 Healthcare platforms** | **Integrate** ⭐ | Never replace the EMR |
| L11 Standards | **Conform + contribute** | FHIR, ABDM, MCP |
| L12 Automation | **Compete/absorb** | Legacy RPA is vulnerable |
| L13 Dev platforms | **Participate + own SDK** | Adapter SDK is the ecosystem play |
| L14 Enterprise AI | **Partner** | Systems integrators as channel |
| L15 Frontier | **Monitor** | Mandatory each cycle |

---

## 3. Assumed differentiation thesis

**[ASSUMED]** JARVIS's defensibility rests on four claims, each of which the research must **attack rather than confirm**:

| # | Claim | Strongest counter-argument the research must test |
|---|---|---|
| T1 | **Owning the L3+L4 loop beats owning any single box** | Loop-owners can be disintermediated from above by L8 default placement, regardless of technical merit |
| T2 | **Healthcare workflow depth is a durable moat** | Incumbent EMRs are shipping native AI agents and own the workflow already |
| T3 | **Local-first/privacy is a differentiator** | Users demonstrably trade privacy for convenience; regulators may not force the issue in time |
| T4 | **Adapters over legacy systems are a moat** | Adapters are brittle, unglamorous, and can be commoditised by a standards wave (as MCP did to bespoke tool integrations) |

> **Every dossier must test at least one of T1–T4 against its subject and report whether the evidence strengthens or weakens it.** This is the mechanism that keeps the knowledge base from becoming an elaborate confirmation exercise. Article VII.3 (mandatory uncomfortable finding) exists to enforce it.

---

## 4. Non-goals

**[ASSUMED]** JARVIS does not: train frontier models · build inference runtimes · replace EMRs · build browser engines · compete on STT/TTS quality · sell general-purpose chat.

Recommendations that violate a non-goal must either be rejected or explicitly argue the non-goal is wrong.

---

## 5. How dossiers use this file

```
For each company:
  1. Locate its primary layer
  2. Read JARVIS's posture for that layer (§2)
  3. Apply the Strategic Role decision tree
  4. Score D9 (threat) ONLY against layers where JARVIS's posture is OWN or COMPETE
  5. Score D10 (leverage) against JARVIS's actual architectural needs
  6. Test ≥1 of T1–T4 (§3) against the evidence
  7. Produce ≥1 uncomfortable finding
```

**D9 is scored against contested layers only.** A company dominating a layer JARVIS ignores or depends on is not a threat — it is context or leverage. This single rule prevents most competitor inflation.

---

## 6. Change control

Changes to §1–§4 **invalidate all D9/D10 scores** and require re-scoring every ratified dossier. Substantive changes should therefore land *before* Phase 2 begins.

| Version | Date | Change | Impact |
|---|---|---|---|
| v0.1.0-DRAFT | 2026-07-26 | Initial baseline with assumptions flagged | None — no dossiers yet |
| v0.2.0 | 2026-07-26 | Grounded against repo + blueprint. Q1–Q4, Q6 resolved. L10/L11 marked intended-not-current. Theses T1–T4 status recorded. | None — no dossiers yet |

---

## 7. Thesis status after repository grounding

| Thesis | Status | Evidence |
|---|---|---|
| **T1** — own the L3+L4 loop | **HALF-TRUE** | L4 genuinely strong; L3 is storage + safety boundary. Temporal validity, consolidation, procedural memory all absent. |
| **T2** — healthcare depth is a moat | **UNEVIDENCED** | Zero healthcare code exists. Intention, not artefact. |
| **T3** — local-first/privacy differentiates | **CONTRADICTED** | STT drives headless Chrome to an external URL. Primary input surface violates the claim. |
| **T4** — adapters over legacy systems | **PARTIALLY PROVEN** | Proven for consumer apps (WhatsApp/Telegram); untested against clinical systems, which are categorically harder. |

Dossiers testing T1–T4 must use these statuses, not the original aspirational framing.
