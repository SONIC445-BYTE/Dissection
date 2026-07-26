# DELIVERABLE 10 — Technical Reverse Engineering (Stack)

Confidence legend: 🟢 Confirmed | 🟡 Strong Inference | 🔴 Speculation | ⚪ Cannot Verify

Evidence base: Wolters Kluwer engineering job postings (2025–2026, verbatim stacks), live-page artefacts (store/login), app-store binaries metadata, and standard forensic signals. UpToDate sits inside WK's engineering estate, so we report three stratum: **(A) Legacy product stratum, (B) Modernisation stratum, (C) GenAI platform stratum.**

---

## 10.A Legacy product stratum (the corpus-serving monolith estate)

| Layer | Evidence | Conf. |
|---|---|---|
| Languages | C# / .NET & .NET Core heavily listed in WK Health/Chennai roles; PHP legacy roles also appear | 🟢 (for Health estates) |
| Frontend | AngularJS (1.x) still maintained + newer Angular; TypeScript | 🟢 |
| Data | MS SQL Server; "NoSQL" adjacent in .NET roles | 🟢 |
| Platform | Azure PaaS, Azure DevOps pipelines, Agile SDLC with gate reviews | 🟢 |
| Testing | Selenium, SpecFlow/Cucumber, REST-API test automation (QA roles) | 🟢 |
| Geographic footprint | Chennai (large), plus global WK offices — cost-effective maintenance of legacy estate | 🟢 |

🟡 **Read:** the topic-serving application (web app, mobile backends) is a long-lived .NET/Azure estate with an Angular-era SPA and SQL-backed content stores. This matches the visible UX vintage. "If it serves 1.6M topic views/day without drama, nobody rewrites it."

## 10.B Modernisation stratum

- 🟢 DevOps hiring: Terraform, Ansible, Jenkins; **Datadog** listed among DevOps skill sets; Kubernetes/EKS-style containerisation; Node.js/React appear in web-modern roles; MySQL/NoSQL mixes.
- 🟢 SSO federation: SAML/OIDC via Microsoft Entra and OpenAthens (login page); EZproxy/IP referral institutional auth.
- 🟢 E-commerce: **Salesforce B2B Commerce (CloudCraze)** — irrefutable from `ccrz__` routes on store.uptodate.com; renewal/CRM flows in Salesforce ecosystem.
- 🟢 Mobile: native iOS (App Store, iOS 16/18 requirements) and Android apps; offline sync for Lexidrug (SQLite-class local store — 🟡).

## 10.C GenAI platform stratum (2024–)

🟢 From the AI Platform & Agents engineering posting (verbatim requirements):
- **Languages:** TypeScript, Node.js, React, Python, Rust
- **Orchestration:** LangChain / LangGraph; MCP / A2A protocols
- **Clouds:** AWS primary; Azure; GCP (multi-cloud)
- **Data stores:** Amazon DocumentDB, DynamoDB, OpenSearch, Azure AI Search
- **Models:** Azure OpenAI; AWS Anthropic (Bedrock); Google Gemini; skills include Bedrock Knowledge Bases, Intelligent Prompt Routing, AgentCore, model distillation, reinforcement fine-tuning, Azure AI Foundry
- **Platform practices:** Docker, Terraform, GitHub Actions; evals; canaries; rollout/rollback; cost & quality telemetry; secure SDLC, threat modeling, least privilege; ~100-engineer remote-first org, sub-teams <10
- 🟢 Team topology: central platform serves "hundreds of product teams" — classic enablement-platform pattern; 20+ agents already launched across WK.

## 10.D Cross-cutting services (inferred best-effort)

| Service | Inference | Conf. |
|---|---|---|
| CDN | Global audience + static-heavy content ⇒ CDN fronting (vendor ⚪ — Akamai/CloudFront unverifiable) | 🟡 |
| Caching | Topic pages cache-friendly; Edge caching + search index caching | 🟡 |
| Monitoring | Datadog (DevOps postings); LLM-specific telemetry per GenAI posting | 🟢/🟡 |
| Product analytics | Institutional usage reports exist (must be fed by an internal pipeline); vendor tooling ⚪ | 🟢 existence / ⚪ vendor |
| Email/CRM | Salesforce ecosystem (store + renewals); marketing automation vendor ⚪ | 🟡 |
| Messaging (in-app) | None consumer-style; admin/enterprise comms via account teams | 🟡 |
| Payments | Card processing via Salesforce Commerce integrations; IAP via App Store/Play (Lexidrug) | 🟢 |
| Feature flags | Canary/rollout language in GenAI posting implies flag infrastructure (vendor ⚪) | 🟡 |
| CI/CD | Azure DevOps (legacy) + GitHub Actions (GenAI) | 🟢 |
| Observability for AI | Per-query cost + quality + latency SLOs, hallucination metrics | 🟢 |

## 10.E The engineering-culture reconstruction

🟡 Two engineering civilisations coexist: **Chennai-centred legacy guardianship** (C#, AngularJS, gate reviews) and **startup-mode GenAI platform** (remote-first, "manager of one" culture, Rust/TS, evals, canaries). This is the classic incumbent bifurcation — and its predictable failure mode is *innovation quarantine*: the new platform owns the agent, but the legacy estate owns identity, entitlements, billing and the corpus. Expert AI must therefore straddle both — explaining packaging friction (which SKUs get AI) and the deliberate enterprise-first rollout.

**Ovexis counter-architecture lesson (summary):** one civilisation, not two — a single event-driven, FHIR-native platform where identity, data ingestion, evidence retrieval and agents share one type system. UpToDate cannot collapse its two stacks without rewriting 20 years of estate; a greenfield entrant has no such tax. 🟡
