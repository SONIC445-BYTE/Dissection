# DELIVERABLE 9 — AI Reverse Engineering: UpToDate Expert AI

Confidence legend: 🟢 Confirmed | 🟡 Strong Inference | 🔴 Speculation | ⚪ Cannot Verify

Primary evidence (unusually solid): Wolters Kluwer's own Senior Full-Stack Engineer (AI Platform & Agents) job posting describes the flagship build ("UpToDate Expert AI — a medical research and clinical reasoning agent") with the actual stack and team topology; launch materials (Sept/Nov 2025) describe the layered validation design; WK fiscal reporting and interviews describe rollout scale.

---

## 9.1 Model providers & inference architecture

🟢 **Multi-model by design.** Job post requires/production-lists: **Azure OpenAI, AWS Anthropic (via Bedrock), Google Gemini**; cloud **AWS (primary), Azure, GCP**. 🟡 Rationale: model-agnostic routing hedges single-vendor risk, negotiates leverage, and lets them A/B quality/cost/latency per query type (job post cites "Amazon Bedrock Intelligent Prompt Routing", "Foundry", "Knowledge Bases" skills).

- 🟢 Orchestration: **LangChain/LangGraph**, with MCP/A2A (agent-to-agent protocol) in the stack listing.
- 🟢 Retrieval stores: **Amazon DocumentDB, DynamoDB, OpenSearch, Azure AI Search**; drug-topic knowledge projected into retrieval ("Bedrock Knowledge Bases" skill).
- 🟢 Languages: TypeScript/Node.js, React, Python, plus **Rust** (inference-latency-critical paths — strong inference).
- 🟢 Serving ops: Docker + Terraform + GitHub Actions; observability and **cost/quality telemetry per query**, canary rollouts, rollout/rollback, eval gates.

🟡 Reconstructed serving pattern:

```
Query → guardrail triage → router (light/factual vs deep/reasoning model)
      → retrieval (corpus RAG over topic chunks + Lexidrug)
      → grounded generation w/ citations → post-hoc validators
      (source-support check, contraindication check, red-flag escalation)
      → answer + Assumptions/Sources/Reasoning artefacts → stream
```

## 9.2 Agent architecture ("Clinical Intelligence")

🟢 Marketed as a **multi-layer validation framework** "emulating how expert clinicians reason" and "expert-driven at every step of an interaction" (7,600-expert leverage). Decomposed, that means:
1. 🟡 **Query understanding/planner** — classifies clinical intent (dx, tx, dose, ddx, drug), asks clarifying assumptions (the visible "Assumptions" panel is the planner's notes exposed).
2. 🟡 **Retriever** — chunk-level RAG over graded topics + drug monographs, tuned to prefer graded-recommendation sections (Key Points/Summary blocks give near-canonical spans).
3. 🟡 **Reasoner** — stepwise chain (the exposed "step-by-step rationale" is a structured reasoning trace, human-readable).
4. 🟡 **Verifier(s)** — support-check that each claim maps to cited text; contradiction check against Lexidrug harmonisation (post-Nov-2025); policy guardrails (no unsupported advice; refusal when evidence insufficient — OpenEvidence markets a similar refusal behaviour; WK marketing emphasises guardrails without listing heuristics — ⚪ specifics).
5. 🟡 **Provenance renderer** — per-answer citation objects + "assumptions" disclosure (unique differentiator vs OpenEvidence's inline-citation style).

## 9.3 Memory & context management

- 🟢 Session memory: conversational threads (chat product). 
- 🟢 **No patient memory.** No chart ingestion, no longitudinal state; contexts are entered per-question (user-typed qualifiers). Confirmed by absence across all materials and by the Abridge integration supplying "context" externally instead.
- 🟡 User memory: search history/profile for CME, not clinical reasoning personalisation. Personalisation depth ⚪.

## 9.4 Digital twin

🟢 **None.** Confirmed absence: UpToDate has no patient twin. The *corpus* is their twin — a twin of medical knowledge, not of a person. (This sentence is the shortest possible explanation of the Ovexis opportunity.)

## 9.5 Reasoning & confidence estimation

- 🟡 Confidence is expressed via **GRADE semantics on the sources** (the retrieved recommendations carry 1A–2C grades), plus assumption disclosure — i.e., they surface *epistemic structure* rather than a numeric model-confidence score. No public claim of calibrated confidence numbers (⚪).
- 🟡 Exposure of the reasoning trace doubles as a *verification UI* — clinicians audit rather than trust. This is a deliberate anti-automation-bias design: Expert AI sells "assist and show work," not "autopilot."

## 9.6 Evaluation

- 🟢 Job post makes evals first-class: eval harness in CI/CD, canaries, rollout/rollback, quality telemetry; hallucination-reduction explicitly named as an engineering target ("Improvements you ship — latency, reliability, hallucination reduction — translate directly into... care").
- 🟡 Evaluation layers inferred: retrieval faithfulness, citation-support rate, clinician-rated answer quality (health-system co-development for ~2 years pre-launch), regression suites on medical QA sets.
- ⚪ **No public benchmark numbers** (no MedQA/USMLE-score marketing to date) — conspicuous vs OpenEvidence/AMBOSS which publicise benchmarks. Watch: if WK ever publishes, it will be framed as *outcome* or *safety* metrics, not leaderboard scores.

## 9.7 Prompt engineering

🟡 Corpus-constrained system prompting with strict source-bound generation (claims must resolve to retrieved spans); assumption-extraction prompts; drug-harmonisation prompts (post-Lexidrug integration); refusal templates. Speculation-level: they likely generate *answer skeletons* from graded-recommendation spans first, then expand into prose — the output structure mirrors the topic template. 🔴

## 9.8 Guardrails & safety

| Layer | Evidence | Conf. |
|---|---|---|
| Input scope-gates (clinical Q&A only?) | "Embedded guardrails and oversight" (app listing) | 🟢/🟡 |
| Grounding requirement (no source → no claim) | Transparency-artefact existence + grounding marketing | 🟡 |
| Human review loop | "Expert-driven at every step"; 7,600-expert leverage; CMO-led clinical org | 🟢/🟡 |
| Enterprise governance | Admin policy controls, audit logging marketed to enterprises | 🟢 |
| Regulatory posture | Non-device CDS framing; decision authority remains with clinician | 🟡 |

## 9.9 Clinical validation

🟢 Pre-launch: ~2 years co-development with health systems (Samios). 🟢 Post-launch: 50+ major US health systems deploying within ~2 months (Fellin). ⚪ No peer-reviewed validation study of Expert AI published yet — the strategic question is whether WK can extend the Isaac–Jha outcomes tradition to the AI product (they know evidence = procurement armor).

## 9.10 What WK's AI choices reveal (Ovexis analysis)

1. 🟢 **They built a platform team, not a bolt-on:** central GenAI platform (~100 engineers, 20+ agents org-wide) with UpToDate Expert AI as flagship. Competence is real.
2. 🟡 **Multi-cloud/multi-model is procurement armour as much as tech** — enterprise trust posture.
3. 🟡 **The agent consumes static knowledge.** Everything in the architecture — RAG over topics, grading sources, refusal on thin evidence — assumes the *world knowledge* is the corpus and the *patient* is a sentence in the prompt. A longitudinal platform's agent must invert this: the patient is the primary context (persistent, structured, private), and the corpus is a citation source.
4. 🟢 **Transparency triad (Assumptions/Sources/Reasoning) is genuinely good AI UX** — Ovexis should copy the pattern and extend it with *patient-data-lineage panels* (which records informed this insight, when, with what quality).
5. 🟡 **Abridge-style push integration will be their distribution crown** — expect UpToDate evidence to appear in Epic-native AI, Microsoft surfaces. Ovexis needs interop alliances (or an acquisition wedge) before this locks.
