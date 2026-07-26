# Competitive Scoring Framework
`v1.0.0` · Phase 0 · Computed by `tools/score.py`

Scores exist to make judgements **comparable and auditable**, not to replace judgement. Every score carries a written justification and an evidence tier. A score without justification is deleted by the linter.

---

## 1. The ten dimensions

Each scored **0–5**. Anchors are defined so two analysts converge.

### D1 — Layer Ownership Strength
*How defensibly does this company own its primary layer?*

| Score | Anchor |
|---|---|
| 0 | Present but owns nothing; pure reseller |
| 1 | Minor participant, easily displaced |
| 2 | Credible player among many equals |
| 3 | Top-tier player; named in most buyer shortlists |
| 4 | Dominant; the default choice in its layer |
| 5 | Effectively *is* the layer; others define themselves relative to it |

### D2 — Technical Depth
*Is the engineering hard to replicate?*

| Score | Anchor |
|---|---|
| 0 | Thin wrapper over someone else's API |
| 1 | Standard engineering, no novel problems solved |
| 2 | Solid execution; a good team could match in ~6 months |
| 3 | Genuine hard problems solved; ~12–18 months to match |
| 4 | Deep systems work + accumulated operational knowledge; years to match |
| 5 | Research-frontier work others cannot currently reproduce |

### D3 — Distribution Power
*Can they reach users without permission from anyone?*

| Score | Anchor |
|---|---|
| 0 | No distribution; word of mouth only |
| 1 | Single narrow channel |
| 2 | Working channel, meaningful CAC |
| 3 | Strong PLG or established sales motion |
| 4 | Multiple compounding channels; brand pull |
| 5 | Owns a default surface (OS, browser, device, national infrastructure) |

### D4 — Data Advantage
*Does usage compound into structural advantage?*

| Score | Anchor |
|---|---|
| 0 | No proprietary data |
| 1 | Data exists, unused |
| 2 | Data improves product marginally |
| 3 | Clear feedback loop; usage → better product |
| 4 | Large proprietary corpus a competitor cannot assemble |
| 5 | Data asset is legally/practically impossible to replicate (e.g. multi-decade clinical records at national scale) |

### D5 — Ecosystem Gravity
*Do others build on them?*

0 none · 1 a few integrations · 2 real integration list · 3 active third-party developers · 4 large ecosystem with commercial dependents · 5 de-facto standard others must support

### D6 — Switching Cost Imposed
*What does leaving cost the customer?*

0 trivial (change one env var) · 1 hours · 2 days · 3 weeks + retraining · 4 months + data migration + workflow rebuild · 5 practically impossible within a decade (core system of record)

### D7 — Healthcare Relevance
*Does this matter to JARVIS's healthcare mission?*

| Score | Anchor |
|---|---|
| 0 | Irrelevant |
| 1 | Generic tech usable in healthcare |
| 2 | Some healthcare customers, no specialisation |
| 3 | Healthcare-specific features or compliance posture |
| 4 | Healthcare is a primary market; deep workflow fit |
| 5 | Is healthcare infrastructure — systems of record or national standards |

### D8 — Velocity
*Rate of meaningful shipping over the last 12 months.* Meaningful = capability change, not release-note churn.

0 dormant · 1 maintenance only · 2 steady minor · 3 regular meaningful releases · 4 rapid, category-shaping · 5 redefining the category faster than others can respond

### D9 — Strategic Threat to JARVIS
*Could they take JARVIS's position?* **Scored only against the contested layer, not general prowess.**

| Score | Anchor |
|---|---|
| 0 | No overlap |
| 1 | Adjacent; no realistic path to overlap |
| 2 | Could overlap if they chose to; no current signal |
| 3 | Overlapping ambitions; competing for the same user |
| 4 | Directly contesting a JARVIS core layer (L3/L4) today |
| 5 | Could make JARVIS structurally unnecessary |

### D10 — Leverage Value to JARVIS
*How much does JARVIS gain by using/integrating/partnering rather than fighting?*

0 nothing · 1 marginal · 2 useful component · 3 meaningful acceleration · 4 removes a whole workstream from the roadmap · 5 foundational — JARVIS is materially better and faster by depending on it

---

## 2. Computed indices

```python
Threat_Index      = (D9*3 + D1*2 + D3*2 + D8*1.5 + D2*1) / 9.5     # 0–5
Partnership_Index = (D10*3 + D5*2 + D7*1.5 + D2*1.5) / 8           # 0–5
Dependency_Risk   = (D6*2 + D3*2 + D1*1.5 + (5 - D5)*1) / 6.5      # 0–5
Priority_Score    = max(Threat_Index, Partnership_Index) * (1 + D7/10)
```

**Reading them:**

- **Threat Index ≥ 3.5** → Direct Competitor classification must be seriously considered; if not chosen, justify why in writing.
- **Partnership Index ≥ 3.5** → integration or partnership path must be explicitly evaluated before any "build our own" recommendation.
- **Dependency Risk ≥ 3.5** → a mitigation plan is **mandatory**: abstraction layer, second source, or exit path. No exceptions.
- **Priority Score** sets research and roadmap ordering. The `D7/10` multiplier deliberately biases toward healthcare relevance, because that is JARVIS's differentiated market.

**Threat and Partnership are not opposites.** A company can score high on both (NVIDIA, Microsoft, Epic). That combination — high threat *and* high leverage — is the most strategically demanding relationship and must be flagged `COMPLEX` for explicit handling in Phase 7.

---

## 3. Scoring discipline

**3.1** Every dimension needs 1–3 sentences of justification citing claim IDs. Bare numbers fail lint.

**3.2 — Anchor to the stage.** An S1 project scoring 4 on D2 needs strong evidence; small teams *can* have deep tech, but the claim must be earned.

**3.3 — Score what exists, not what is announced.** D8 velocity counts shipped capability. Roadmaps score zero.

**3.4 — Do not inflate D9.** The instinct to rate everything a 4 is exactly the competitor inflation this framework exists to prevent. Most companies score 0–2 on D9. If your registry averages above 2.5, you are scoring fear, not evidence.

**3.5 — D10 is usually higher than people expect.** Most of the ecosystem is leverage, not enemies.

**3.6 — RHINAL and JARVIS are never scored.** `self: true` entries are excluded by `score.py`.

**3.7 — Scores are versioned.** Re-scoring requires a Decision Ledger entry naming the trigger. Score drift without a trigger is a lint warning.

---

## 4. Worked calibration examples

Illustrative anchors so runs converge. These are **calibration references, not pre-judgements** — real dossiers must derive scores from evidence.

| Company | Layer | D1 | D2 | D3 | D9 | D10 | Expected shape |
|---|---|---|---|---|---|---|---|
| NVIDIA | L0 | 5 | 5 | 5 | 0–1 | 5 | Foundational Dependency. Threat ≈ 0, leverage maximal, dependency risk high. |
| A hosted memory API startup | L3 | 2–3 | 3 | 2 | 3–4 | 2–3 | The genuine D9=4 case: contests a JARVIS core layer. |
| Playwright | L6 | 4 | 3 | 4 | 0 | 5 | Technology Supplier. Rebuilding it would be self-harm. |
| Epic | L10 | 5 | 4 | 4 | 1 | 4 | Integration Target. Enormous, entrenched, *not* a competitor. |
| Microsoft (Copilot/OS) | L8 | 4 | 4 | 5 | 4 | 4 | `COMPLEX`: high threat AND high leverage. Distribution is the threat. |
| ABDM (as institution) | L11 | 5 | — | 5 | 0 | 5 | Not a company. Standards conformance target. |

Note the pattern: **the highest-threat entries are rarely the biggest companies.** They are the ones contesting L3/L4 specifically. Size correlates with leverage; layer overlap correlates with threat.

---

## 5. Scorecard file format

```yaml
company: Mem0
layer_primary: L3
layer_secondary: [L13]
stage:
  - product: Mem0 OSS
    stage: S2
  - product: Mem0 Platform (hosted)
    stage: S2
strategic_role_primary: Direct Competitor
strategic_role_secondary: [Technology Supplier]
contested_layer_proof:
  layer: L3
  jarvis_capability: persistent cross-session memory
  buyer_substitution: "a developer choosing a memory layer picks one, not both"
scores:
  D1: {value: 3, justification: "...", claims: [MEM0-C-004]}
  # ... D2–D10
indices:            # computed, do not hand-edit
  threat: 0.0
  partnership: 0.0
  dependency_risk: 0.0
  priority: 0.0
flags: []           # COMPLEX | STALE | CONTESTED | LOW-EVIDENCE
```
