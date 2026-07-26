# DELIVERABLE 17 — Decision Ledger (Why each major feature exists)

Confidence legend: 🟢 Confirmed | 🟡 Strong Inference | 🔴 Speculation | ⚪ Cannot Verify

| Feature | Why it was built | Pain it solves | KPI it improves | Trade-offs accepted | Viable alternative architecture | Conf. |
|---|---|---|---|---|---|---|
| Question-first topic pages | Rose's founding doctrine: answer the clinical question, not describe the disease | 90-second answer retrieval at bedside | Time-to-answer; daily active use; decision-change rate | Content must be commissioned per-question (expensive editorial ops) | Disease-ontology pages (textbook model) | 🟢 |
| Summary & Recommendations block at top | Clinicians read top-down under time pressure | Answer before evidence; reduces scroll-search | First-screen answer rate | Deep readers lose narrative flow | Chronological narrative (Monograph style) | 🟢 |
| GRADE (1A–2C) inline | 2006 decision to make strength/quality machine-visible per recommendation | "How much should I trust this?" anxiety | Trust/NPS; medico-legal defensibility | Expensive grading team; subjective judgments disputed by users | Single evidence-score or none (DynaMed earlier) | 🟢 |
| Continuous publishing | Knowledge decay = patient harm; print editions were the enemy | Staleness anxiety | Update freshness; renewal justification | Permanent editorial payroll (no "done") | Editioned releases (lower cost) | 🟢 |
| What's New / PCU feed | Practice changes missed between readings | Stale-practice risk | Re-engagement (weekly actives) | Alert fatigue risk | Silent in-line updates only | 🟢 |
| Named authorship + disclosures | Accountability = trust; prestige loop for authors | Credibility verification | Brand trust; author acquisition | Slower corrections (human pipeline) | Anonymous house-style (BMJ) | 🟢 |
| Search-first IA | Product is used as an oracle, browsed rarely | Findability across 13,000 topics | Search success rate | Browse/discoverability weakens | Browse-first specialty trees | 🟢 |
| Key Points panels | Not every query justifies a topic open | Zero-click micro-answers | Search-result CTR→answer conversion | Editorial curation load | Snippet auto-extraction only | 🟢 |
| 200+ calculators | Stop leakage to MDCalc; calculators are decision objects | On-the-spot dosing/risk scoring | Session completeness; app opens | Maintenance of validated logic | Partner/link out | 🟢 |
| Lexidrug assimilation (2025) | ~30% of queries are drug-related; AI answers needed drug truth | Contradiction risk between drug DB and topics | AI answer completeness; pharmacist churn defence | Massive harmonisation engineering | Keep siloed databases | 🟢 |
| Patient education (2 tiers, 19 langs) | Clinician must explain & document understanding | Adherence + explanation burden | Consult efficiency; enterprise value | Maintaining dual-register content | Third-party leaflets (Emmi covers some too) | 🟢 |
| CME auto-accrual | Monetise habit into switching costs | Licence compliance burden of reading | Retention/renewal; daily use | Regulatory accreditation ops | External CME only | 🟢 |
| UpToDate Anywhere / SSO | Enterprise needs usage accountability + personal remote access | "Who uses our license?" + remote clinicians | Institutional renewal; CME attach | Auth complexity; 90-day revalidation friction | Pure IP access | 🟢 |
| EHR Infobutton integration | Workflow graft: kill the "open another tab" moment | Context switching | EHR-sourced sessions; PI compliance help | Integration maintenance per EHR | App-only strategy | 🟢 |
| Institutional IP/SSO "no-login" access | Friction kills clinical adoption at Elshift change | Login friction | Activation rate | Credential-sharing leakage | Strict named-user auth | 🟢 |
| 2-device mobile policy | License enforcement | Seat abuse | ARPU protection | User anger (anecdata) | Softer concurrent-session policy | 🟢/🟡 |
| Total-staff enterprise pricing | Capture full value of enterprise embedment | — (vendor revenue design) | ACV | Alienates CFOs; de-adoption risk | Active-user pricing (fairer, lower ACV) | 🟢/🟡 |
| UpToDate Advanced/pathways | Standardised practice variation play (~2016–2019) | Protocol divergence across clinicians | Enterprise ACV; VA wins | Low adoption of rigid pathways vs flexible topics | Order-set partnerships | 🟢/🟡 |
| Expert AI (2025) | Existential answer to OpenEvidence/ChatGPT; convert corpus to agent | Clinicians' new "ask" behaviour | Enterprise AI deployments; Pro Plus upgrades | Cannibalises page-view model; AI cost per query | Ignore GenAI (BMJ path) | 🟢 |
| Transparency triad (Assumptions/Sources/Reasoning) | Enterprise AI governance sales requirement + clinician-in-loop compliance | AI black-box distrust | Enterprise procurement wins | Slower answers; more engineering | Vanilla chat UI | 🟢 |
| Multi-model routing (Azure OAI/Anthropic/Gemini) | Avoid vendor lock; optimise cost/quality per task | Price/performance of inference at scale | Cost per query; uptime | 3× integration burden | Single-model strategy | 🟢 (evidence: job post) |
| Abridge integration | Evidence at the point of documentation; keep UpToDate "inside" AI scribes | Post-encounter evidence chase | Partner-embedded usage | Shares surface/billing with partner | Build own scribe | 🟢 |
| No public API / no free tier | Protect corpus IP + price integrity | Piracy, commoditisation | Revenue integrity | Forfeits developer/PLG era | Open API + freemium (OpenEvidence path) | 🟢 |

**Ledger meta-pattern (for Ovexis):** 🟡 nearly every decision trades *openness for control* and *polish for quality*. Their KPI tree (topic views/day, decisions changed/day, renewals, ACV) is a **content-consumption KPI tree**. No metric in their public vocabulary measures patient-level outcome *of an individual* — because they never see the patient. Ovexis's KPI tree should be built exactly there.
