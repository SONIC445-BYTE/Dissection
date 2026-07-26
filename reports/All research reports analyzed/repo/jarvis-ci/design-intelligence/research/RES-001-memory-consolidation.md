# RES-001 — Is memory consolidation tractable, or is it a trap?

| | |
|---|---|
| **Status** | Open |
| **Stage** | 0 (does not block) |
| **Subsystem** | `memory-store` |
| **Source** | capability:memory-consolidation, OQ-01, FAIL-007 |
| **Confidence** | MEDIUM |
| **Priority** | P3 (2.44) |
| **Timebox** | 1 week, ending at the Zep/Graphiti dossier |

---

## Question

Does **any** production memory system implement a described consolidation or
forgetting mechanism — or is this confirmed negative space?

## Why it matters

The capability registry classes this `contested-hard`. Practitioner evidence
`[MEM0-C-041]` reports it unsolved **across the entire category**, not by one
vendor. FAIL-007 predicts the consequence: memories accumulate until searching
them costs more than reprocessing the original context, and the memory layer
becomes net-negative for the workload it was added to serve.

JARVIS has persistence and no consolidation. Same trajectory.

## The trap to avoid

An unclaimed problem in a well-funded category is **not automatically an
opportunity**. Two readings compete:

- **Neglected** — everyone is chasing demos; the unglamorous work is available
- **Genuinely hard** — better-resourced teams tried and failed quietly

The registry currently records `contested-hard`, i.e. the pessimistic reading.
This research exists to test that classification, because building on the wrong
reading is how startups die confidently.

## Falsifier

- **Confirmed unclaimed** if no system in the L3 registry describes a mechanism
  (not a marketing claim) after Zep/Graphiti, Letta and Cognee are analysed.
- **Killed** if any of them ships a described, evaluated consolidation mechanism —
  in which case this becomes an integration decision, not a research project.

## Constraint

**This research must never block delivery.** It runs alongside Stage 0 work. If
DEC-001 (memory architecture) is forced before this concludes, decide on current
evidence and record the uncertainty in the ADR.

## Review trigger

Zep/Graphiti dossier ratified.
