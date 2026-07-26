# The Research Constitution
`v1.0.0` · Phase 0 · Created once · Amendable only by explicit versioned revision

This document governs every subsequent artefact in this knowledge base. Where any run prompt, template, or synthesis conflicts with this document, **this document wins.**

---

## Article I — Purpose

Build a **Competitive Intelligence Knowledge Base** that can answer, with traceable evidence, three questions:

1. **Who owns value in each layer of the AI ecosystem, and how durably?**
2. **For each of those owners, what is their correct strategic relationship to JARVIS?**
3. **What must JARVIS build, buy, integrate, abstract, or refuse — and in what order?**

It is explicitly *not* a market map, not a funding tracker, and not a feature comparison spreadsheet. Those are outputs of the process, never the goal.

---

## Article II — The Isolation Principle

> **One company. One complete run. One context window.**

**II.1** Each company dossier is produced in a research run that analyses *that company only*.

**II.2** A run may read the Constitution, the Taxonomy, the Evidence Rules, the Scoring Framework, the ontologies, the JARVIS baseline, and the *open research questions* emitted by prior runs. It may **not** read prior dossiers.

**II.3 — Rationale.** If all companies share one context, the analysis budget is consumed by whoever comes first. Company #1 gets architectural teardown; company #17 gets three bullet points and a shrug. The output then *looks* uniform while being wildly non-uniform in rigour, which is worse than obviously-uneven output because it defeats the reader's scepticism.

**II.4 — The only permitted cross-company channel in Phase 2** is the **Open Research Questions** register (Final Reflection Q8). Questions may flow forward. Findings, comparisons, and judgements may not.

**II.5** Any sentence in a Phase 2 dossier containing a comparative construction against another named company — *"unlike X"*, *"better than X"*, *"X does this too"* — is a **lint error**. Comparison is Phase 3 and Phase 6 work.

---

## Article III — Stage Discipline

Maturity is a property of the *thing being judged*, and criticism that ignores it is noise.

| Stage | Name | Definition | What may fairly be criticised |
|---|---|---|---|
| **S0** | Concept | README, manifesto, landing page, waitlist. No usable artefact. | Coherence of the idea; whether claims are physically possible |
| **S1** | Prototype | Runs for its author. Demo-quality. Breaks off the happy path. | Architecture choices; whether the core insight is validated |
| **S2** | Product | Third parties use it unaided. Docs exist. Bugs are filed by strangers. | UX, reliability, docs, integration surface, pricing coherence |
| **S3** | Platform | Production deployments at scale. SLAs, support, versioning, migration paths. | Operational maturity, security posture, ecosystem, governance |
| **S4** | Infrastructure | Depended upon by other platforms. Its failure is other people's outage. | Standards stewardship, backwards compatibility, neutrality, capture risk |

**III.1** Every dossier declares the subject's stage **per product line**, not per company. NVIDIA is S4 in CUDA and S1 in several software initiatives simultaneously.

**III.2** Criticism must be stage-adjusted. *"This S0 project lacks SOC 2"* is not a finding. *"This S3 platform lacks SOC 2"* is a serious one.

**III.3** Conversely — and this is the failure mode people miss — **do not credit an S0 project with S3 capabilities because its README describes them.** Stage discipline cuts in both directions.

**III.4** For JARVIS itself, stage honesty is mandatory in every "Lessons for JARVIS" section. A lesson that assumes JARVIS is S3 when it is S1 produces a roadmap that cannot be executed.

---

## Article IV — Evidence Supremacy

Full rules in `02-evidence-rules.md`. The constitutional core:

**IV.1** Every substantive claim carries exactly one evidence tier: 🟢 **E1** verified primary · 🟡 **E2** corroborated secondary · 🟠 **E3** structural inference · 🔴 **E4** speculation.

**IV.2** **Inference never promotes to fact.** An E3 claim becomes E1 only when a new primary source is added to the Evidence Register with its own source ID. Rewriting the sentence more confidently is not promotion; it is fabrication.

**IV.3** **Documentation describes intent; code describes reality.** A README claim is E2 at its absolute best, and E2 only when the documentation is official and versioned. Marketing pages are E4 unless corroborated.

**IV.4** **Roadmaps are not products.** The ladder is: *rumoured → announced → preview/beta → GA → adopted at scale.* Each rung requires its own evidence. Conflating them is the single most common error in competitive research.

**IV.5** **Absence of evidence is recorded as absence of evidence**, in the Research Gaps section — never silently converted to absence of the thing.

**IV.6** Speculation is permitted and often valuable. It must be labelled 🔴 and must state what evidence would confirm or kill it.

---

## Article V — Strategic Role Discipline

**V.1** Every company receives **exactly one primary Strategic Role** from the six defined in `07-strategic-role-classification.md`: Foundational Dependency · Integration Target · Direct Competitor · Potential Partner · Technology Supplier · Market Signal.

**V.2** Secondary roles are permitted but each requires explicit written justification naming the layer and the workflow in which the secondary role applies.

**V.3** **"Direct Competitor" requires proof of a contested layer.** The dossier must name (a) the specific ecosystem layer, (b) the specific JARVIS capability contested, and (c) the buyer or user who would choose one *instead of* the other. Without all three, the classification is wrong and defaults to Market Signal.

**V.4 — Rationale.** Calling everything a competitor is intellectually lazy and strategically expensive. It produces roadmaps built on fear, drives teams to rebuild commodities, and blinds them to the far larger set of companies that are actually free leverage.

---

## Article VI — The Synthesis Prohibition

**VI.1** No cross-company synthesis, pattern claim, ranking, or ecosystem conclusion may be produced until **Phase 2.5 Research Quality Audit passes**.

**VI.2** The audit checks: evidence coverage, depth variance across dossiers, unresolved contradictions, role-classification consistency, stage-discipline violations, and unanswered open research questions.

**VI.3** If the audit fails, the remedy is **re-running deficient dossiers**, not softening the audit.

**VI.4 — Rationale.** Synthesis is a lossy compression of its inputs. Compressing uneven inputs produces confident conclusions with invisible error bars, and those conclusions become load-bearing in funding decisions and architecture commitments long after anyone remembers which dossier was thin.

---

## Article VII — Self-Reference Rules

**VII.1** JARVIS and RHINAL are the *subject*, never the *object*, of competitive scoring.

**VII.2** RHINAL may appear in the registry and in layer analyses flagged `self: true`, for architectural comparison only. It receives no Threat Index, no Priority Score, and no competitive assessment.

**VII.3** Every dossier must contain at least one finding that is **uncomfortable for JARVIS** — a capability gap, an obsoleted assumption, a commoditised differentiator, or a reason a customer would rationally choose the subject instead. A dossier with zero uncomfortable findings is presumed insufficiently rigorous and fails audit.

**VII.4** The question *"does this company strengthen or weaken the strategic case for JARVIS?"* must be answered honestly, including when the answer is "weakens."

---

## Article VIII — Healthcare Adapter Philosophy

**VIII.1 — Healthcare is an adapter surface, not a rewrite.** JARVIS's healthcare capability is expressed as adapters over existing systems of record. JARVIS does not attempt to replace the EMR. The EMR is the incumbent's moat and the customer's 10-year sunk cost; attacking it directly is the standard way healthcare startups die.

**VIII.2 — The adapter ladder**, in strict order of preference:

| Rank | Adapter type | Use when | Durability |
|---|---|---|---|
| 1 | **Standards adapter** (FHIR R4, HL7 v2, ABDM/HIE-CM, NHCX) | A standard exists and the target implements it | Highest — survives vendor change |
| 2 | **Native/official API** | Vendor exposes a supported, versioned API | High — but vendor-controlled |
| 3 | **MCP server** | Target or community exposes MCP; agent-native access wanted | High and rising — protocol consolidating |
| 4 | **Database/HL7 feed adapter** | Read-only access to the system of record is grantable | Medium — brittle to schema change |
| 5 | **Browser automation** | Web UI is the only surface | Low — breaks on every UI release |
| 6 | **Desktop UI automation** (accessibility tree) | Thick-client legacy HIS | Low — but sometimes the only option in Indian tier-2/3 hospitals |
| 7 | **OCR / screen scraping** | Nothing else exists | Lowest — last resort, always flagged as tech debt |
| 8 | **Community adapter** | Long tail; JARVIS supplies the SDK, not the adapter | Variable — scales reach, not quality |

**VIII.3** Every healthcare-relevant dossier must place the subject on this ladder and justify the rank. Choosing rank 5–7 when rank 1–3 is available is an architectural error that must be called out.

**VIII.4** **Clinical safety outranks capability.** Any JARVIS recommendation touching diagnosis, medication, dosing, or orders must specify the human-in-the-loop checkpoint. An adapter that writes to a clinical record without an explicit confirmation gate is not a feature; it is a liability.

**VIII.5** India-first grounding is mandatory where relevant: ABDM (ABHA, HFR, HPR, HIE-CM, UHI, NHCX), FHIR R4 per the NRCeS ABDM Implementation Guide, and the reality that most Indian facilities below the large-chain tier run partial or no EMR at all.

---

## Article IX — Prohibited Practices

| # | Prohibition | Why |
|---|---|---|
| 1 | Treating README/marketing claims as implemented features | Manufactures phantom competitors |
| 2 | Promoting inference to fact by rewording | Corrupts the evidence chain irreversibly |
| 3 | Assuming roadmap items exist | Roadmaps are aspirations under NDA-free marketing pressure |
| 4 | Criticising S0 work by S3 standards (or vice versa) | Produces unfair and unusable conclusions |
| 5 | Cross-company comparison inside Phase 2 | Violates isolation; leaks unaudited findings into dossiers |
| 6 | Calling a company a competitor without contested-layer proof | Competitor inflation → fear-driven roadmap |
| 7 | Self-scoring RHINAL/JARVIS competitively | Circular reasoning |
| 8 | Synthesis before the 2.5 audit passes | Contaminates strategy with uneven inputs |
| 9 | Copying features without extracting the principle | Cargo-cult product management |
| 10 | Omitting uncomfortable findings | Turns intelligence into reassurance |
| 11 | Recommending "compete" as the default posture | Most layers should be integrated or abstracted, not fought |
| 12 | Unlabelled numbers (revenue, users, benchmarks) without source + date | Stale metrics outlive their truth |

---

## Article X — Definition of Done

A Phase 2 dossier is **ratified** only when all of the following hold:

- [ ] All 16 deliverables present and non-empty
- [ ] Every substantive claim carries an evidence tier
- [ ] Evidence Register complete, every source dated, every source ID referenced at least once
- [ ] Stage declared per product line
- [ ] Exactly one primary Strategic Role, with contested-layer proof if Direct Competitor
- [ ] Scorecard complete across all 10 dimensions with per-dimension justification
- [ ] Adapter ladder placement (if healthcare-relevant)
- [ ] ≥1 uncomfortable finding for JARVIS
- [ ] Zero cross-company comparative claims
- [ ] Research Gaps and Open Questions populated
- [ ] All 8 Final Reflection questions answered
- [ ] `tools/validate.py` exits 0

---

## Article XI — Amendment

This Constitution may be amended between phases, never during one. Amendments bump the version, are logged in a Decision Ledger entry, and **trigger revalidation of every dossier ratified under the prior version**. If an amendment would invalidate existing dossiers, the amendment is deferred to the next major phase boundary.
