# Phase R — Repository Dissection

**Subject:** `github.com/SONIC445-BYTE/JARVIS-Automation`
**Branch analysed:** `phase-2-adapter-wiring` (HEAD, 2026-07-23) — 30 commits ahead of default
**Analysed:** 2026-07-26
**Method:** Public repository surface — tree structure, branch state, commit history and messages. No local clone; no file-content inspection beyond what commit messages document.

---

## Purpose

Phase R produces the three artefacts that Phases 7/8/Ω consume:

| File | Content |
|---|---|
| `capability-ledger.md` | What JARVIS **verifiably does today**, evidence-tiered and stage-labelled |
| `architecture-map.md` | Layer placement (L0–L15) of every real subsystem |
| `gap-register.md` | Blueprint claims vs. repository reality |
| `blueprint-review.md` | ⭐ Direct assessment of the staged development blueprint |

Per `phase-0-constitution/09-repo-context-isolation.md`, these artefacts are **forbidden inputs to Phases 1, 2, 2.5 and 6** and **required inputs to Phases 7, 8 and Ω**.

---

## Evidence note

This dissection assigns unusually high evidence tiers to commit messages, which requires justification under `02-evidence-rules.md` §2.2.

Normally a commit message is E2 — a developer's *claim* about their own work. In this repository the commit messages are materially different in kind: they record root cause, the measurement that confirmed it, the verification performed, the test count, and — critically — **an explicit statement of what was *not* done and why.**

Examples of that last property, which is what earns the tier upgrade:

- *"Did not build the upstream file-identification/reading capability itself… that's new NLU/file-lookup surface, a separate, undecided piece of scope, not 'wiring a dead parameter'."*
- *"feature_flags/level6_engine.yaml is untouched, still enabled: false -- flipping it live is a separate, explicit decision, not part of this commit."*
- *"Also noticed a 'No module named speech_recognition' fallback warning and a seemingly-hallucinated conversation-loop transcript during this test run… not investigated further here."*

A commit message that volunteers unresolved problems and refuses to claim adjacent scope is not marketing. It is a lab notebook. Such messages are treated as **E1 for "this change was made and verified as described"** and **E2 for "the subsystem works in production"** — because verification in a test harness is not the same as verification under clinical load.

**Standing caveat, applied throughout:** the analysis rests on documented self-report. It has not been independently reproduced by running the code. Every capability claim below inherits that ceiling.
