# Company Ontology
`v1.0.0` · Phase 0

Defines what a "company" record contains, so that 80 dossiers written across 80 runs remain structurally comparable.

---

## 1. Entity types

Not everything in the registry is a company. Type determines which sections apply.

| Type | Definition | Sections that change |
|---|---|---|
| `commercial` | Venture/public company selling a product | Full dossier |
| `oss-project` | Community/foundation-governed open source | Business Model → *governance & sustainability model*; funding → *sponsorship* |
| `oss-commercial` | Open core with a company behind it | Full dossier + **open/closed boundary analysis** (critical: where is the paywall, and does it block evaluation?) |
| `standard` | Specification or protocol | No business model; add *governance, adoption, conformance, extension* |
| `government-infra` | State-run digital public infrastructure | No competitive scoring; add *mandate, policy risk, compliance obligations* |
| `research-lab` | Publishes rather than ships | Product Intelligence → *research agenda & transfer path* |
| `internal` | JARVIS/RHINAL — `self: true` | **Comparison only. Never scored.** |

---

## 2. Required identity fields

```yaml
id: mem0                          # slug, stable, never reused
name: Mem0
aka: [Embedchain]                 # former names, rebrands
type: oss-commercial
layer_primary: L3
layer_secondary: [L13]
hq_country: US
founded: 2023
entity_status: active             # active | acquired | dormant | dead | pivoted
self: false
priority_tier: 1                  # 1 = run first
```

`entity_status` matters more than it looks: dead and pivoted companies are often the **most instructive** dossiers, because failure evidence is cleaner than success narrative. A pivoted company tells you where a layer's value actually wasn't.

---

## 3. Dimensions every dossier must populate

### 3.1 Executive Intelligence
Mission · vision · category (self-declared vs actual) · jobs-to-be-done · target customer · **explicit non-customers** · pain solved · positioning · founding philosophy · long-term ambition

> **Non-customers are the highest-signal field here.** Who a company refuses to serve reveals its real strategy far more reliably than its mission statement.

### 3.2 Company Intelligence
History & timeline · founders & backgrounds · leadership · funding rounds (amount, date, investors) · valuation (with date) · patents · acquisitions (made and received) · hiring trends (roles reveal roadmap) · open-source footprint · research publications · partnerships · clinical/enterprise relationships · regulatory position · geographic footprint

> Hiring is E3 evidence for *direction* and among the most reliable early signals available. A memory company hiring compiler engineers is telling you something its blog is not.

### 3.3 Product Intelligence
Every visible feature · user workflows · navigation model · settings & configurability · permission model · notifications · AI interaction surfaces · developer workflows · admin workflows · **retention loops** · **growth loops** · monetisation triggers · undocumented/hidden capabilities · feature dependency graph

### 3.4 Technical Architecture
Frontend · backend · languages · frameworks · cloud/hosting · databases · caching · auth · observability · infrastructure · CI/CD · feature flags · SDKs · API architecture · security architecture · deployment models (SaaS / self-host / hybrid / air-gapped)

> Mark inference explicitly. Inferring Postgres from an error message is legitimate E3 — inferring the entire architecture from a marketing diagram is not.

### 3.5 AI Architecture
Model providers · reasoning approach · planning · memory · agent topology · context management · prompting strategy · evaluation · guardrails · RAG · knowledge graphs · multi-agent coordination · confidence estimation · safety posture

### 3.6 Developer Platform
SDKs · plugins/extensions · public APIs · internal APIs (observed) · extension model · marketplace · DX quality · documentation quality · community health · **MCP support** (increasingly the single most informative interop signal)

### 3.7 Distribution
SEO · community · enterprise sales · developer adoption · founder brand · partnerships · channel strategy · PLG mechanics · virality · open source as distribution

### 3.8 Business
Pricing (with date) · revenue model · sales motion · expansion mechanics · customer segments · switching costs · retention evidence · gross margin where public · **the open/closed boundary** for open-core

> For open-core: *where the paywall sits determines the company's real strategy.* A paywall that blocks production evaluation is a growth decision with competitive consequences, and it is frequently the exploitable weakness.

### 3.9 User Intelligence
Evidence from GitHub · Reddit · Hacker News · Product Hunt · G2 · Capterra · YouTube · LinkedIn · forums · Discord.
Extract: **complaints** (ranked by frequency) · praise · unexpected use cases · feature requests · churn reasons · power-user behaviour.

> Unexpected use cases are where new categories hide. Churn reasons are where attack plans come from.

### 3.10 Moat Analysis
Technology · data · workflow · distribution · regulatory · brand · developer · community moats · switching costs · network effects · compounding advantages · **and weaknesses in each**.

### 3.11 Failure Analysis
How could this company fail? Technical · business model · distribution · regulatory · AI-specific (model dependency, commoditisation) · market timing · organisational · capital allocation.

> Run this for *every* company, including dominant ones. Dominance is a snapshot; the failure modes are the forecast.

### 3.12 Competitive Attack Plan
If launching against them: what never to copy · which assumptions are wrong · blind spots · what architecture beats theirs · what GTM beats theirs · which customer is underserved.

> Write this even for Integration Targets and Dependencies. It is the fastest way to find *their* weaknesses — which is also how you find *your* leverage in a partnership negotiation.

### 3.13 Lessons for JARVIS
Principles (not features) · valuable architectural decisions · mistakes never to repeat · **what becomes commodity** · **what becomes durable moat** · ecosystem effect · layer placement · posture recommendation.

---

## 4. Comparability requirements

- Same section numbering in every dossier
- Same scoring dimensions
- Same evidence tiers
- Same stage vocabulary
- Same role taxonomy
- Same Final Reflection questions

**Depth may vary with importance; structure may not.** A Tier-3 Market Signal may have a thin section 3.4 — but the section exists and says *"insufficient public evidence; searched X, Y, Z."*

---

## 5. Handling difficult subjects

| Situation | Rule |
|---|---|
| **Private, opaque company** | Lean on job posts, patents, customer case studies, conference talks, ex-employee public writing. Mark E3 heavily. Do not invent. |
| **Giant multi-layer conglomerate** | **Scope to the relevant business unit.** A Microsoft dossier is not about Microsoft; it is about Copilot-as-OS-layer + Azure-as-dependency + Nuance-as-healthcare. Declare the scope in section 1. |
| **Pure OSS with no company** | Analyse governance, bus factor, funding, release cadence, maintainer burnout risk. Sustainability *is* the business model. |
| **Standard, not company** | Analyse governance, adoption rate, conformance testing, extension mechanism, capture risk. |
| **Dead or pivoted** | **High-value dossier.** Post-mortems are the cleanest evidence in the entire corpus. Prioritise the failure analysis. |
| **Direct JARVIS analogue** | Maximum rigour, maximum honesty. This is where motivated reasoning is strongest — require ≥3 uncomfortable findings, not 1. |
