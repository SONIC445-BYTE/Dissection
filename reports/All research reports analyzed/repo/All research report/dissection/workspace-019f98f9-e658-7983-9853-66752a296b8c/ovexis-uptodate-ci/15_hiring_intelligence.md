# DELIVERABLE 15 — Hiring Intelligence

Confidence legend: 🟢 Confirmed | 🟡 Strong Inference | 🔴 Speculation | ⚪ Cannot Verify

Source: Wolters Kluwer job postings (Workday, foundit, hirist, BuiltinChicago, Glassdoor), 2025–mid-2026. Job posts are the most honest public roadmap a company publishes.

---

## 15.1 The signal-rich posting set

### Posting A — Senior Full-Stack Engineer, AI Platform & Agents (R0052281) 🟢
- Central GenAI Platform team; **~100-engineer remote-first org; sub-teams <10**; "20+ agents launched and many more in progress"; platform serves "hundreds of product teams."
- **Flagship: UpToDate Expert AI** — described verbatim as "a medical research and clinical reasoning agent... Millions of physicians will rely on it to accelerate differential diagnosis, refine treatment decisions, and reduce cognitive load — while maintaining rigorous safety, privacy, and guideline fidelity."
- Stack: TS/Node/React/Python/Rust; LangChain/LangGraph; **MCP/A2A**; AWS primary (+Azure/GCP); DocumentDB/DynamoDB/OpenSearch/Azure AI Search; Azure OpenAI/AWS Anthropic/Gemini; evals, canaries, rollout/rollback, cost+quality telemetry; secure SDLC; "hallucination reduction," "lower cost per query," "faster time-to-decision" as named KPIs.

### Posting B — Senior Python Full-Stack Engineer (Azure/AWS, LLM) 🟢
LLM-fluent full-stack roles inside product groups; skills include Amazon Bedrock (Knowledge Bases, Intelligent Prompt Routing, **AgentCore**, model distillation, **reinforcement fine-tuning**), Azure AI Foundry/Agent Service.

### Posting C — Legacy estate roles (Chennai et al.) 🟢
.NET Core + **AngularJS** maintenance; SQL Server; Azure DevOps; QA automation (Selenium/SpecFlow); DevOps (Terraform/Jenkins/Datadog); IT security compliance analysts.

### Posting D — Commercial 🟢
Field sales manager roles (India, US) — enterprise motion investment; strategy analysts in BD.

---

## 15.2 Roadmap inference from hiring

| Signal | Inference | Conf. |
|---|---|---|
| MCP/A2A in stack | Building agent-to-agent interop: UpToDate as a *callable agent/service* for third-party agents (EHR copilots, scribes) — the Evidence-API hypothesis | 🟡 |
| AgentCore / Bedrock Knowledge Bases | Productionising on AWS-managed agent runtime + knowledge stores; drug-topic knowledge bases already live (Lexidrug KBs, Nov 2025) | 🟢/🟡 |
| Model distillation + RFT skills | Cost curve attack: distill task-specific models (cheap specialist models for retrieval/routing/guard), frontier models only for hard reasoning | 🟡 |
| Rust in web-stack | Latency-critical inference paths / edge performance for streaming | 🟡 |
| Eval + canary infrastructure | Continuous clinical-quality regression gates; AI release trains | 🟢 |
| "Reduce cognitive load," "differential diagnosis" framing | Product ambition extends beyond Q&A toward *reasoning assistance* (ddx support) | 🟢 (words) / 🟡 (roadmap) |
| Continued AngularJS/IP roles | Legacy estate persists into 2026+; rewrite NOT planned wholesale | 🟢 |
| Field sales hiring (growth markets) | International enterprise push (India etc.) | 🟢 |

## 15.3 Team structure reconstruction 🟡

```
WK Health engineering
├── Legacy product teams (Chennai-centred): corpus web/mobile, entitlements, store
├── Integration teams: EHR/Infobutton, SSO, partner APIs
├── Central GenAI Platform (~100 eng, remote-first, US/EU; sub-teams <10)
│    ├── Platform services (retrieval, routing, evals, observability, identity)
│    ├── Flagship agents (UpToDate Expert AI core team)
│    └── Agent enablement for other WK divisions (legal/tax)
└── Security/compliance + DevOps shared services
```

## 15.4 Engineering maturity assessment

- 🟢 Maturity on: enterprise SLAs, SDLC gates, QA automation, security governance, multi-cloud, AI-ops discipline (unusually advanced for a "publisher").
- 🟡 Gaps by inference: frontend modernity lag; two-stack bifurcation tax (File 10); AI platform still ~2 years old — technical debt in agent systems accumulates differently (prompt chains, eval drift).
- 🟡 AI priorities decoded (ranked by hiring emphasis): 1) enterprise-grade reliability/governance of Expert AI; 2) unit-cost reduction (distillation/routing); 3) interop (MCP/A2A); 4) deeper reasoning (ddx); 5) platform reuse for adjacent WK divisions.

## 15.5 What Ovexis should poach and pattern-match

🟡 Hiring-market arbitrage: WK's own jobs market AJ-candidate their exact skill taxonomy — Ovexis can hire from the same pool (Chennai health-IT talent, Bedrock/Foundry engineers). Pattern to copy: <10-person sub-teams on a shared agent platform with eval-first CI. Pattern to avoid: splitting AI from product into an enablement org whose flagship is bound by a legacy entitlement system.
