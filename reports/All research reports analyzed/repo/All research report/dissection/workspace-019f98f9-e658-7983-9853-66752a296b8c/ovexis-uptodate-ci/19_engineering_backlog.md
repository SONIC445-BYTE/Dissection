# DELIVERABLE 19 — Engineering Backlog & Roadmap Reconstruction

Confidence legend: 🟢 Confirmed | 🟡 Strong Inference | 🔴 Speculation | ⚪ Cannot Verify

## 19.1 Version epochs reconstructed

| Epoch | Years | What shipped | Conf. |
|---|---|---|---|
| **V0 — Diskette** | 1992–~1997 | Nephrology topics on floppy disks; mailed updates; DOS/early Windows | 🟢 |
| **V1 — CD/Web 1.0** | ~1997–2006 | Web subscription; specialty expansion; multi-author editorial pipeline formalised; institutional licensing emerges | 🟡 |
| **V2 — Evidence web** | 2006–2012 | GRADE integration; topic structure canonicalised; institutional scale; mobile apps (iOS by 2011); WK acquisition resources | 🟢 |
| **V3 — Workflow graft** | 2012–2019 | UpToDate Anywhere (SSO+CME); EHR Infobutton kits (Epic/Cerner/InterSystems); calculators maturation; patient education tiers; UpToDate Advanced pathways (2016–19); WK portfolio assimilation (Lexi-Comp→Lexidrug, Medi-Span, Health Language, Emmi, Sentri7) | 🟢 |
| **V4 — Platform prep** | 2020–2024 | Cloud consolidation (Azure estate; AWS footprint grows); corpus machine-readable transformation; two-year Expert AI co-development; GenAI platform team formed; Abridge partnership (Oct 2024) | 🟡 |
| **V5 — Agentic re-launch (current)** | 2025– | UpToDate Expert AI GA path (Sep 2025 announce; Q4-25 enterprise preview; Nov-25 Lexidrug KBs; 2026 Pro Plus + trainee+select enterprise packaging; Abridge CDS GA Mar 2026); multi-model routing, eval gates, governance console | 🟢 |

## 19.2 Reconstructed current backlog (evidence-anchored)

**Confirmed ships-in-progress:** 🟢 Expert AI enterprise rollout scale-up (50+ systems); Lexidrug-in-Expert-AI expansion series ("first in a series of planned expansions"); packaging into Pro Plus/trainee (done, US); iOS/Android Expert AI app parity.

**Strongly inferred (🟡):**
1. Calculators as first-class agent tools (structured tool-calling from 200+ calculators — natural next "expansion").
2. Patient-ed content in Expert AI outputs ("Beyond the Basics" synthesis mode).
3. Multilingual AI responses (190-country base + 19-language patient ed skeletons exist).
4. Context passthrough from EHR (Infobutton → Expert AI session with chart-context qualifiers).
5. Conversation persistence + clinic libraries (team-shared AI threads for enterprises).
6. Formal evidence/licensing API for partners (MCP/A2A skills signal).
7. Usage- & AI-governance analytics GA for enterprise admins.
8. Distilled specialist models for guardrails/routing (cost program per hiring skills).

**Speculative but aligned (🔴):** voice input for hands-busy clinicians; integration into Epic-native AI surfaces; specialty-agent variants (pharmacist agent on Lexidrug corpus); UK/EU-compliant AI packaging with regional model endpoints; acquisition of an AI clinical-workflow startup (Legal division's Libra deal is the template).

## 19.3 Technical-debt ledger 🟡

| Debt | Evidence/grounding | Severity |
|---|---|---|
| AngularJS-era frontend | Continued AngularJS maintenance hiring in 2026 | High (UX ceiling) |
| Two-stack bifurcation (legacy entitlements vs GenAI platform) | Distinct stacks/teams in hiring | High (feature friction — packaging complexity is the symptom) |
| Search index generation gap | Key Points are curated panels; unified semantic search pending | Medium |
| Content-schema heterogeneity across acquisitions | Harmonisation program had to be *marketed* — implies unresolved internal inconsistency | Medium–High |
| App rating debt (3.6★) | Public rating | Medium |
| Offline gap in core app | Only Lexidrug is offline-first | Medium |

## 19.4 Engineering size & infrastructure maturity

- 🟢 WK Health FTEs: 3,571 (2025) total (all functions); central GenAI platform ~100 engineers; legacy+product engineering distributed across US/India/EU (Chennai major).
- 🟡 Infra maturity: multi-cloud, IaC (Terraform), CI/CD dual-track (Azure DevOps legacy + GitHub Actions modern), Datadog-class observability, canary AI release vehicles — **a genuinely modern enterprise platform grafted onto a pre-cloud product core.** Maturity score vs FAANG: high on governance, medium on velocity, low on product-side iteration speed (app releases measured in quarters, AI releases in cohorts).

## 19.5 Implications for Ovexis backlog phasing (preview of File 25)

🟡 Ovexis cannot out-scope them; it must out-sequence them: (1) consent+identity spine (3–4 months), (2) FHIR/consumer ingestion + normalisation (4–6), (3) twin + minimal agent with lineage panels (3–4), (4) clinician workspace + evidence adapters (3–4) — i.e., reach UpToDate-relevant answers *with a patient attached* inside ~12–15 months with a 15–25 person elite team, exploiting their 2-year enterprise co-development cadence as a speed arbitrage window.
