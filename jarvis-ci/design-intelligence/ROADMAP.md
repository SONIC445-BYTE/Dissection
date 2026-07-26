# JARVIS Engineering Roadmap

**Generated** by `tools/route.py` from the registry substrate.
Not hand-written. Regenerates on every `evolve.py` run.

Current stage **0** · 7 blocking exit criteria open

> Stage discipline is enforced mechanically: no stage-N recommendation
> is emitted while stage-(N-1) blocking prerequisites remain open.
> Parked items are preserved with unpark triggers, never discarded.

| Pri | Score | Route | Stage | Subsystem | Recommendation | Cost | Conf |
|---|---|---|---|---|---|---|---|
| **P0** | 10.00 | adr | 0 | `audit-trail` | Clinical audit trail must be architected in, not retrofitted | m | HIGH |
| **P0** | 6.49 | issue | 0 | `rag-retrieval` | Knowledge retrieval: replace HTML scraping with API tiers + failover | m | HIGH |
| **P0** | 6.43 | issue | 0 | `llm-engine` | Wire generate_stream() — dark capability, largest latency win | xs | HIGH |
| **P0** | 6.19 | milestone | 0 | `opd-queue` | Build OPD queue — Stage 0 centerpiece and first clinical workflow | l | HIGH |
| **P1** | 5.10 | issue | 0 | `stt` | Replace external-URL STT with local speech recognition | m | HIGH |
| **P2** | 3.42 | milestone | 0 | `level6` | Freeze further L9 self-coding investment until Stage 0.5 ships | xs | HIGH |
| **P2** | 3.08 | rfc | 0 | `memory-store` | Unbounded memory growth will degrade retrieval | m | MEDIUM |
| **P2** | 2.83 | research | 0 | `memory-store` | Probe: is persistent memory the wrong architecture for clinical work? | s | LOW |
| **P2** | 2.61 | adr | 0 | `memory-store` | Memory architecture: vector-first vs temporal-graph-native | xl | MEDIUM |
| **P3** | 2.44 | research | 0 | `memory-store` | Memory consolidation — research before committing storage architecture | l | MEDIUM |
| **P3** | 2.24 | milestone | 0 | `audit-trail` | Clinical compliance posture is the highest-leverage moat | l | HIGH |
| **P3** | 1.19 | parked | 1 | `adapter-sdk` | MCP conformance for the adapter layer | m | HIGH |
| **P3** | 1.01 | parked | 1 | `adapter-sdk` | Adopt pluggable-backends pattern for the adapter framework | m | MEDIUM |
| **P4** | 0.29 | parked | 2 | `—` | Pricing: keep the differentiator inside the evaluation tier | xs | HIGH |
| **P4** | 0.00 | ignore | 0 | `memory-store` | Vector retrieval — integrate, never build | xs | HIGH |

## P0 — blocks stage exit

### R-001 · Clinical audit trail must be architected in, not retrofitted
- **Stage** 0 · **Subsystem** `audit-trail` · **Route** adr
- **Cost** m · **Maintenance** low · **Confidence** HIGH
- **User value** 2/5 · **Strategic value** 5/5
- **Dependencies** S0-E8
- **Review trigger** first clinical write path implemented
- **Source** `FAIL-005`

Retrofit cost grows with every adapter. Mem0 demonstrates the endgame: zero compliance posture closed regulated verticals entirely.

### R-007 · Knowledge retrieval: replace HTML scraping with API tiers + failover
- **Stage** 0 · **Subsystem** `rag-retrieval` · **Route** issue
- **Cost** m · **Maintenance** low · **Confidence** HIGH
- **User value** 3/5 · **Strategic value** 3/5
- **Dependencies** S0-E1, S0-E2
- **Review trigger** any silent retrieval failure in production
- **Source** `subsystem:rag-retrieval`

Live fragility on an already-reachable capability. ToS exposure. Already scoped in the blueprint; correctly queued.

### R-008 · Wire generate_stream() — dark capability, largest latency win
- **Stage** 0 · **Subsystem** `llm-engine` · **Route** issue
- **Cost** xs · **Maintenance** none · **Confidence** HIGH
- **User value** 4/5 · **Strategic value** 2/5
- **Dependencies** none
- **Review trigger** none — do it
- **Source** `subsystem:llm-engine`

Exists at llm_engine.py:161, called by nothing. Speech starts at token 1 instead of token 150. Hours of work. Dark capability is inventory, not output.

### R-005 · Build OPD queue — Stage 0 centerpiece and first clinical workflow
- **Stage** 0 · **Subsystem** `opd-queue` · **Route** milestone
- **Cost** l · **Maintenance** medium · **Confidence** HIGH
- **User value** 5/5 · **Strategic value** 5/5
- **Dependencies** S0-E1, S0-E2
- **Review trigger** first physician session completed
- **Source** `subsystem:opd-queue`

Blueprint's own words: the one thing that makes JARVIS a hospital tool rather than a generic automation tool. Uses only existing machinery. Puts a clinician in front of the system before Stage 1 compounds three stages of assumptions.

## Parked — future-stage, preserved

- **R-011** MCP conformance for the adapter layer — stage 1, unpark: _Stage 0 exit criteria complete_
- **R-009** Adopt pluggable-backends pattern for the adapter framework — stage 1, unpark: _stage prerequisites complete_
- **R-010** Pricing: keep the differentiator inside the evaluation tier — stage 2, unpark: _first paid customer conversation_
