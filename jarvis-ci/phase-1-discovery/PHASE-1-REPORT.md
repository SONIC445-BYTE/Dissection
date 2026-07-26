# Phase 1 — Company Discovery: Completion Report
`v1.0.0` · 2026-07-26 · **Status: COMPLETE** · Registry validated by `tools/registry.py`

---

## 1. What was produced

| Artefact | Content |
|---|---|
| `company-registry.yaml` | **112 entities** across all 16 layers — 108 scoreable, 1 self, 3 frontier |
| `discovery-protocol.md` | 7 discovery methods, inclusion criteria, tiering, cadence, 12 open questions |
| `tools/registry.py` | Dependency-free loader, validator, dashboard |

**Built without repo context**, per `09-repo-context-isolation.md`. The question asked was *"who owns value in each layer?"* — never *"who resembles JARVIS?"*

---

## 2. Distribution

```
L0  Compute            5    ██████
L1  Foundation Models  8    ██████████
L2  Inference Runtime  8    ██████████
L3  Memory ⭐         11    ██████████████
L4  Planning ⭐        8    ██████████
L5  Perception         8    ██████████
L6  Execution          7    █████████
L7  Voice              7    █████████
L8  OS AI ⚠            4    █████
L9  Applications       6    ████████
L10 Healthcare        21    ███████████████████████████  ← largest
L11 Standards          7    █████████
L12 Automation         4    █████
L13 Dev Platforms      3    ████
L14 Enterprise AI      2    ███
L15 Frontier           3    ████
```

**L10 is deliberately the largest block.** It's the differentiated market, it splits into three sub-populations that behave differently (global EMR giants, Indian platforms, ambient-scribe startups), and it holds all three post-mortems.

**L13/L14 are deliberately thin.** Neither is contested by JARVIS's posture. Registering more would be busywork.

---

## 3. Role hypothesis distribution — the anti-inflation check

| Role | Count | Share | Target | Status |
|---|---|---|---|---|
| 📡 Market Signal | 36 | 33.3% | 30–40% | ✅ |
| ⚙️ Technology Supplier | 33 | 30.6% | 20–25% | ⚠ high |
| 🔵 Foundational Dependency | 17 | 15.7% | 10–15% | ✅ borderline |
| 🟢 Integration Target | 13 | 12.0% | 15–20% | ⚠ low |
| 🔴 **Direct Competitor** | **7** | **6.5%** | 5–10% | ✅ **no inflation** |
| 🟣 Potential Partner | 2 | 1.9% | 5–10% | ⚠ low |

**The headline number is 6.5%.** Only seven entities out of 108 are hypothesised as Direct Competitors, and each will still have to pass the three-part contested-layer test in its dossier — several will likely fail it and demote to Technology Supplier or Market Signal.

The three deviations are informative rather than defective:

- **Technology Supplier high (30.6%)** — reflects genuine commodity density in L5/L6/L7. Browser drivers, OCR engines, STT/TTS are *supposed* to be numerous and interchangeable. This is the layer economics working as described.
- **Integration Target low (12%)** — a **real gap**, tracked as DQ-02. Indian tier-2/3 HIS vendors are largely invisible in English-language sources. This will need M4/M6 methods and probably non-English search.
- **Potential Partner low (1.9%)** — correct discipline, not an error. A partner requires a *named joint surface*; "they seem complementary" defaults to Market Signal. Expect this to rise as dossiers surface concrete surfaces.

---

## 4. The seven Direct Competitor hypotheses

Each contests L3 or L4 — the two layers the baseline marks OWN ⭐. No entity was assigned this role for being large.

| Entity | Layer | Contested capability |
|---|---|---|
| Mem0 | L3 | Persistent cross-session memory |
| Zep / Graphiti | L3 | Temporal validity — the capability JARVIS lacks |
| Letta | L3+L4 | Agent-OS framing; the closest whole-loop analogue |
| LangGraph | L4 | Orchestration / control flow |
| CrewAI | L4 | Multi-agent orchestration |
| OpenAI Agents SDK | L4 | Agent runtime, with L1 distribution behind it |
| Microsoft Copilot | L8 | ⚠ `COMPLEX` — high threat *and* high leverage |

Note who is **absent**: Epic, Oracle Health, Practo, Bahmni, NVIDIA, Playwright. Enormous, entrenched, fast-moving — and none of them competes for a layer JARVIS intends to own. Epic is an Integration Target with 21 layer-mates. That distinction is the entire point of the role taxonomy.

---

## 5. Deliberate inclusions worth flagging

**Three post-mortems** (Olive AI, Forward Health, Pear Therapeutics) — all Tier 1 or 2. Per `04-company-ontology.md` §5, failure evidence is cleaner than success narrative. Olive AI in particular is the canonical healthcare scope-creep death and deserves a full dossier.

**Three unclaimed L15 slots** — these are not placeholders. They are the negative-space findings from method M7:

| Slot | Question | Why it matters |
|---|---|---|
| Memory consolidation/forgetting | DQ-01 | Universally named as unsolved. If nobody owns it, that is the opportunity. |
| Clinical adapter SDK | DQ-10 | Direct test of thesis T4 |
| Tier-2/3 Indian clinical middle market | DQ-11 | The gap between "ABDM-connected" and "digitally mature" |

If these stay unclaimed after Phase 2, that is the most commercially significant output of the entire discovery phase.

**Non-obvious entries** included on merit: `llama.cpp` (the engine beneath Ollama/LM Studio/Jan — the *real* L2 dependency), `Temporal` (durable execution, the non-AI answer to long-horizon reliability), `Microsoft UI Automation` (accessibility tree = the legacy-HIS adapter surface), `pywinauto` (thick-client HIS automation), `Jan` (closest local-first desktop analogue).

---

## 6. Known gaps

| # | Gap | Tracked as |
|---|---|---|
| 1 | Indian tier-2/3 HIS vendors underrepresented | DQ-02 |
| 2 | M4 (job-posting archaeology) not yet run | protocol §5 |
| 3 | M6 (adjacency walk) not yet run — needs dossiers first | protocol §5 |
| 4 | Insurance/TPA layer thin — 30+ Indian TPAs, none registered | new: DQ-13 |
| 5 | Non-English sources unsearched | DQ-02 dependency |

Gaps 2 and 3 are structural: both methods require inputs that don't exist yet. M6 in particular needs completed dossiers to walk *from*. Discovery re-runs after every 10 dossiers.

---

## 7. Exit criteria

- [x] All 16 layers populated, or explicitly justified as thin
- [x] ≥3 candidates per contested layer (L3: 11, L4: 8)
- [x] Registry machine-validated — 0 errors
- [x] Role distribution checked against anti-inflation targets
- [x] Direct Competitor share ≤15% (**6.5%**)
- [x] ≥1 L15 frontier nomination (**3**)
- [x] Post-mortem subjects included (**3**)
- [x] Self-entities flagged and excluded from scoring (**RHINAL**)
- [x] Tier-1 research order established (**31 entities**)

**Phase 1 is complete.** The gate to Phase 2 is open.

---

## 8. Phase 2 entry point

Research order is tier-1 first, beginning with the contested core:

```
L3 Memory      → Mem0, Zep/Graphiti, Letta          ← start here
L4 Planning    → LangGraph, OpenAI Agents SDK, Claude Code
L2 Inference   → Ollama, llama.cpp
L1 Models      → OpenAI, Anthropic, Google DeepMind, Qwen
L10 Healthcare → Epic, Practo, Bahmni, Abridge, Nuance DAX, Olive AI
L11 Standards  → HL7 FHIR, ABDM, MCP
L0/L5/L6/L7/L8/L9 → NVIDIA, Browser Use, Anthropic CU, Playwright, Whisper, MS Copilot, ChatGPT
```

Starting with L3 is deliberate: it is the layer with the largest gap between JARVIS's stated posture (OWN ⭐) and any evidence, so it is where research has the highest marginal value.

**Next:** Phase 2 machinery — run prompt, dossier template, evidence register schema, scorecard schema, and validation tooling.
