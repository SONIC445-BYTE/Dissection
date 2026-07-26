# Phase 2 — Company Intelligence Engine: Completion Report
`v1.0.0` · 2026-07-26 · **Status: MACHINERY COMPLETE · EXEMPLAR RATIFIED**

---

## 1. What Phase 2 delivers

Phase 2 is not a document — it is a **repeatable engine**. Its deliverable is the machinery that produces 108 structurally identical dossiers without degradation, plus one worked exemplar proving the machinery holds.

| Artefact | Purpose |
|---|---|
| `_TEMPLATE/RUN-PROMPT.md` | The engine. One paste per company, fresh context. |
| `_TEMPLATE/DOSSIER-TEMPLATE.md` | 16-section standardized structure |
| `_TEMPLATE/evidence-register.csv` | Per-claim ledger schema |
| `_TEMPLATE/scorecard.yaml` | 10-dimension scoring schema |
| `Companies/Mem0/` | ⭐ **Reference exemplar — ratified, sets the bar** |
| `OPEN-QUESTIONS.md` | The only permitted cross-run channel |
| `tools/new_company.py` | Scaffolder — refuses unregistered and self entities |
| `tools/validate.py` | Constitution linter — 20+ rules |
| `tools/score.py` | Index computation + threshold interpretation |
| `tools/status.py` | Progress + **depth-variance** dashboard |
| `tools/gate.py` | Phase locks |

---

## 2. Toolchain verification

Every guard was tested against a real failure case, not assumed.

| Test | Expected | Result |
|---|---|---|
| Scaffold registered company | succeeds | ✅ Mem0 created |
| Scaffold unregistered company | **refuses** | ✅ "not in the registry — ad-hoc dossiers break discovery discipline" |
| Scaffold `self:true` entity | **refuses** | ✅ "RHINAL is flagged self:true. Article VII.2" |
| Validate empty scaffold | **22 errors** | ✅ rejected |
| Validate completed exemplar | 0 errors | ✅ **RATIFIABLE** |
| Score exemplar | 4 indices | ✅ threat 2.95 · partnership 3.25 · dependency 3.31 · priority 3.90 |
| Gate Phase 2.5 with 1/108 | **BLOCKED** | ✅ "107 dossiers not ratified" |
| Gate Phase 6 without audit | **BLOCKED** | ✅ "Article VI.1 — synthesis prohibited" |

The validator caught a real bug during testing: it counted template `EXAMPLE` rows as genuine evidence. Fixed — registers containing only template rows now fail.

---

## 3. The exemplar: what Mem0 proves

The dossier is 4,136 words with 44 registered claims across 10 sources. It was written to exercise every mechanism in the constitution:

### 3.1 The registry hypothesis was overturned

Mem0 entered the registry hypothesised as **Direct Competitor** — the obvious call. It does memory; JARVIS wants to own memory.

Applying the three-part test:

| Requirement | Result |
|---|---|
| Contested layer (L3) | ✅ pass |
| Contested capability (persistent cross-session memory) | ✅ pass |
| **Substituting buyer** | ❌ **fail** |

Mem0 sells to developers building agents. JARVIS serves clinicians. **No buyer chooses between them** — a clinician never evaluates a memory API. Demoted to **Technology Supplier**.

> This demotion is the single most important thing the exemplar demonstrates. The instinct "they do memory, we do memory, therefore competitor" is exactly the inflation Article V exists to prevent. Overlap of *capability* is not overlap of *buyer*.

A caveat was recorded honestly: if JARVIS pursues the developer-platform play (T4/L13), Mem0 becomes a genuine competitor for developer mindshare. Re-review at that decision point.

### 3.2 Contradictions preserved, not resolved by preference

Three genuine source conflicts were found and recorded rather than smoothed:
- **Funding:** $24M (E1, company release) vs $24.5M vs $20.5M (E2 aggregators)
- **Founding:** 2023 vs January 2024 → confidence UNKNOWN
- **Benchmarks:** LOCOMO figures revised by multiple parties with materially different numbers

The benchmark contest was handled per the Article II.5 exception: recorded as a contest with every claimant, **without drawing a comparative conclusion**. That is Phase 3's job.

### 3.3 Inference with shown reasoning

The claim *"vector-first with graph as enhancement, not graph-native"* is E3 with HIGH confidence, and the dossier shows all three independent signals supporting it. This is the correct use of inference: not a guess dressed as fact, but a conclusion with visible scaffolding.

### 3.4 Three uncomfortable findings

Article VII.3 requires ≥1. The exemplar produced three, and they are genuinely uncomfortable:

- **U1** — the commodity half of memory is free, excellent, and self-hostable. Any JARVIS work amounting to storage + retrieval rebuilds something a funded team gives away.
- **U2** — *"we own the memory layer"* is a scope statement, not a strategy statement. Mem0 owns L3 about as well as anyone and scores **2/5 on technology moat**. Its real moat is a rented AWS distribution deal.
- **U3** — nobody has solved forgetting, and that is a warning as much as an opportunity. A problem this visible staying unsolved across a well-funded category suggests it is *genuinely hard*, not merely neglected.

### 3.5 Thesis testing produced a split verdict

**T1 (own L3+L4) — WEAKENED.** **T2 (healthcare depth) — STRENGTHENED**, because Mem0's total absence of compliance posture demonstrates regulated verticals are structurally closed to horizontal infra players.

Net conclusion: *JARVIS's differentiation must come from the vertical, not the layer.* That is a strategically consequential finding from a single dossier, and it emerged from evidence rather than assumption.

---

## 4. Depth-variance instrumentation

`tools/status.py` computes coefficient of variation across ratified dossiers on both word count and claim count. **CV > 0.40 triggers a warning** and, at the Phase 2.5 gate, blocks progress.

This is the direct countermeasure to the failure that motivated the whole pipeline: company #17 receiving one-tenth the depth of company #1 while looking superficially uniform. The metric makes uniformity measurable rather than assumed.

Baseline established by the exemplar: **~4,100 words, ~44 claims, 10 sources**. Tier-1 dossiers should land near this. Tier-3 may be thinner in *depth* but must retain all 16 sections with explicit gap notes.

---

## 5. Running the remaining 107

```bash
python3 tools/new_company.py "Zep / Graphiti"    # scaffold
# open _TEMPLATE/RUN-PROMPT.md → FRESH context window → substitute → run
python3 tools/validate.py Zep-Graphiti           # must exit 0
python3 tools/score.py Zep-Graphiti
python3 tools/status.py                          # watch depth variance
```

**Research order** (from Phase 1, tier-1 first):
`Zep/Graphiti → Letta → LangGraph → OpenAI Agents SDK → Claude Code → Ollama → llama.cpp → OpenAI → Anthropic → Google DeepMind → Qwen → Epic → Practo → Bahmni → Abridge → Nuance DAX → Olive AI → HL7 FHIR → ABDM → MCP → NVIDIA → Browser Use → Anthropic CU → Playwright → Whisper → MS Copilot → ChatGPT`

Starting with L3 remains correct: **OQ-01 is now the highest-priority open question in the entire knowledge base**, and Zep/Graphiti is the most likely place to answer it.

---

## 6. Exit criteria

- [x] Run prompt written, with isolation and repo-contamination rules embedded
- [x] 16-section template covering all required deliverables
- [x] Evidence register + source table schema
- [x] Scorecard schema with contested-layer proof field
- [x] Scaffolder, validator, scorer, dashboard, gate — all tested
- [x] Validator enforces: sections, reflection, tiers, falsifiers, promotion violations, cross-company comparison, repo contamination, stage discipline, contested-layer proof, uncomfortable findings, dependency mitigation
- [x] Depth-variance instrumentation live
- [x] Cross-run channel established (`OPEN-QUESTIONS.md`)
- [x] **One dossier ratified end-to-end** proving the machinery
- [x] Gates verified to block

**Phase 2 machinery is complete.** 107 dossiers remain as execution — each an independent run against this engine.

---

## 7. Honest status

**1 of 108 dossiers ratified (0.9%).**

The remaining 107 are genuine research runs, each requiring a fresh context window and substantial primary-source work. The engine is built and proven; the corpus is not. The Phase 2.5 gate will correctly refuse synthesis until they exist — and per Article VI.3, the remedy is running them, never softening the gate.

Phases 3–Ω below are built as **locked, ready-to-execute machinery** with their exit criteria defined, so the pipeline is complete end-to-end and unlocks automatically as the corpus fills.
