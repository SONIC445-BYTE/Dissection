# Canonical Taxonomy — Ecosystem Layers & Value Chain
`v1.0.0` · Phase 0

The single source of truth for "which layer is this?". Every company, technology, and standard in this knowledge base resolves to exactly one **primary layer** here.

---

## 1. The layer map (L0–L15)

| L | Layer | What it owns | Value capture | Commoditisation pressure | Default JARVIS posture |
|---|---|---|---|---|---|
| **L0** | Compute | Silicon, accelerators, datacentre capacity | Very high, concentrated | Very low | **Ignore** — depend, never contest |
| **L1** | Foundation Models | Pretrained weights, frontier capability | High but eroding | **High and rising** | **Abstract** — route across, bind to none |
| **L2** | Inference Runtime | Serving, quantisation, throughput, local execution | Low — near-commodity | **Very high** | **Integrate** — treat as swappable |
| **L3** | Memory | Persistence, recall, temporal truth, consolidation | Contested and unsettled | Medium | **OWN** ⭐ contested core |
| **L4** | Planning | Decomposition, orchestration, control flow, state | Contested | Medium-high | **OWN** ⭐ contested core |
| **L5** | Perception | Screen, DOM, accessibility tree, OCR, document understanding | Low individually, high in aggregate | High | **Own the abstraction, integrate parts** |
| **L6** | Execution | Clicking, typing, API calls, browser/desktop actuation | Low — commodity libraries | Very high | **Integrate** — never rebuild Playwright |
| **L7** | Voice | STT, TTS, wake-word, diarisation | Low and falling fast | Very high | **Integrate** — commodity within 24 months |
| **L8** | Operating System AI | OS-level assistant, system-wide context, default placement | **Extremely high** — distribution moat | Low | **Coexist / differentiate** ⚠ existential |
| **L9** | Applications | End-user AI apps, chat, IDEs, copilots | Medium, high churn | Medium | **Compete selectively** |
| **L10** | Healthcare Platforms | EMR/EHR/HIS/LIS/RIS/PACS systems of record | Very high, entrenched | Very low | **Integrate** ⭐ never replace |
| **L11** | Healthcare Standards | FHIR, HL7, SNOMED, LOINC, ABDM, NHCX | No direct capture; sets rules | N/A | **Conform + contribute** |
| **L12** | Automation Platforms | RPA, iPaaS, workflow engines | Medium, under AI attack | Medium-high | **Compete / absorb** |
| **L13** | Developer Platforms | SDKs, agent frameworks, protocols, registries | Low direct, high ecosystem | High | **Participate + own SDK** |
| **L14** | Enterprise AI | Deployment, governance, compliance, integration services | High, relationship-locked | Low | **Partner** |
| **L15** | Frontier / Unknown | Not yet a category; watched deliberately | Unknown | Unknown | **Monitor** — mandatory review each cycle |

**L15 is not a dumping ground.** It is a discipline: every discovery cycle must nominate at least one candidate for L15 and either promote it to a real layer or explain its dismissal. A taxonomy with no unknowns is a taxonomy that has stopped looking.

---

## 2. Layer assignment rules

**2.1 — Primary layer = where the company captures value**, not where it spends effort. NVIDIA writes enormous amounts of software; it captures value at L0.

**2.2 — Secondary layers** are recorded when a company holds a defensible position elsewhere. Microsoft: primary L8, secondary L0/L1/L2/L9/L10/L13/L14. Multi-layer presence is itself a strategic finding — it usually indicates either a platform play or an identity crisis, and distinguishing the two is the analyst's job.

**2.3 — Layer disputes** are resolved by the counterfactual: *if this company vanished tomorrow, which layer has a hole?*

**2.4** A company's layer may change. Re-classification requires a Decision Ledger entry with the trigger event.

---

## 3. Value chain

```
              ┌──────────────────────────────────────────────────┐
              │  L11 STANDARDS  (rules; no direct value capture)  │
              │  FHIR · HL7 · SNOMED · LOINC · ABDM · MCP · A2A   │
              └───────────────────────┬──────────────────────────┘
                                      │ constrains everything below
  ╔═══════════════════════════════════▼═══════════════════════════════════╗
  ║ L0 COMPUTE        →  L1 MODELS      →  L2 INFERENCE                    ║
  ║ substrate            capability         delivery                       ║
  ║ margin: extreme      margin: eroding    margin: ~zero                  ║
  ╠════════════════════════════════════════════════════════════════════════╣
  ║              ⭐ THE AGENT CORE — where JARVIS must win ⭐               ║
  ║ L3 MEMORY  ⇄  L4 PLANNING  ⇄  L5 PERCEPTION  ⇄  L6 EXECUTION           ║
  ║ These four are a LOOP, not a stack. Value accrues to whoever owns      ║
  ║ the loop's state, not to whoever owns any single box.                  ║
  ╠════════════════════════════════════════════════════════════════════════╣
  ║ L7 VOICE  →  L8 OS AI  →  L9 APPS  →  L12 AUTOMATION  →  L13 DEV PLAT  ║
  ║ interface    distribution  surface     workflows         ecosystem     ║
  ╠════════════════════════════════════════════════════════════════════════╣
  ║ L10 HEALTHCARE PLATFORMS  →  L14 ENTERPRISE AI                         ║
  ║ systems of record            deployment & governance                   ║
  ╚════════════════════════════════════════════════════════════════════════╝
                                      │
              ┌───────────────────────▼──────────────────────────┐
              │  L15 FRONTIER — reviewed every discovery cycle    │
              └──────────────────────────────────────────────────┘
```

### 3.1 The Agent Core insight

L3–L6 are drawn as a loop deliberately. Memory informs planning; planning directs perception; perception feeds execution; execution produces outcomes that update memory. **Whoever owns the loop's persistent state owns the user**, regardless of who supplies any individual box.

This is the single most important structural claim in the taxonomy, and it is the strategic basis for JARVIS's posture of *owning L3+L4 while integrating L5+L6*. Vendors who own only one box in the loop — a memory API, a browser driver — are suppliers to whoever owns the loop.

**This claim must be tested, not assumed.** Phase 6 is required to look for disconfirming evidence: cases where a single-box owner successfully captured the loop, or where the loop-owner was disintermediated from above (L8) or below (L1).

### 3.2 Margin migration

Historical pattern to test in Phase 6: value migrates *up* the stack as lower layers commoditise, but **distribution (L8) can capture value from any layer above it at any time.** L8 is the layer that can eat L3–L9 by default placement alone, without ever being technically better. This is why L8 carries the ⚠ existential marker.

---

## 4. Layer economics — how to assess durability

For each layer, dossiers assess:

| Property | Question |
|---|---|
| **Capital intensity** | What does entry cost? (L0: billions. L6: a weekend.) |
| **Commoditisation velocity** | How fast does a paid capability become a free one? |
| **Switching cost** | What does a customer lose by leaving? |
| **Standardisation exposure** | Does an open standard erase the differentiator? (MCP did this to bespoke tool integrations.) |
| **Distribution dependence** | Can a platform owner cut off access? |
| **Data compounding** | Does usage make the product structurally better for the next user? |

A layer with low capital intensity, high commoditisation velocity, and low switching cost is a **bad layer to own** regardless of current revenue. L6 and L7 are the clearest examples.

---

## 5. Anti-patterns in layer thinking

| Anti-pattern | Description | Correct move |
|---|---|---|
| **Layer envy** | Wanting to own L0/L1 because they look powerful | Own where you can win and defend |
| **Layer sprawl** | Building in every layer to seem complete | Own 1–2, integrate the rest |
| **Commodity capture** | Investing heavily in L2/L6/L7 differentiation | Integrate; redeploy effort to L3/L4 |
| **Standards blindness** | Building proprietary where a standard is consolidating | Conform first, extend second |
| **Distribution denial** | Assuming a better product beats default placement | Plan explicitly for L8 hostility |
| **Loop fragmentation** | Outsourcing memory *and* planning | Never outsource both — that's the whole business |

---

## 6. Research ontology — how layers relate to the other Phase artefacts

```
LAYER (L0–L15)
  ├── contains → COMPANIES        (Phase 2 dossiers, one per company)
  ├── contains → TECHNOLOGIES     (Phase 4, benchmarked capability-by-capability)
  ├── governed by → STANDARDS     (L11; constrains adapters and interop)
  ├── analysed in → LAYER REPORT  (Phase 3, cross-company within one layer)
  └── produces → JARVIS POSTURE   (own / integrate / abstract / partner / ignore)

COMPANY
  ├── has exactly one → PRIMARY LAYER
  ├── may have → SECONDARY LAYERS (justified)
  ├── has exactly one → PRIMARY STRATEGIC ROLE (of 6)
  ├── has per-product-line → STAGE (S0–S4)
  ├── produces → SCORECARD (10 dimensions → 4 indices)
  └── produces → EVIDENCE REGISTER (every claim, tiered and sourced)
```
