# Repo-Context Isolation Rule
`v1.0.0` · Phase 0 · Amendment to Article II · **Set by owner directive, 2026-07-26**

---

## 1. The rule

The JARVIS repository, the Dissection repository, and the Staged Development Blueprint are **strategy-layer inputs only.**

| Phase | JARVIS repo access | Rationale |
|---|---|---|
| Phase 1 — Discovery | ❌ **FORBIDDEN** | Discovery must ask "who owns value in this layer?", not "who looks like us?" |
| Phase 2 — Company Dossiers | ❌ **FORBIDDEN** | Prevents motivated reasoning: scoring a company against your own code invites both flattery and panic |
| Phase 2.5 — Quality Audit | ❌ **FORBIDDEN** | Audits check research integrity, not strategic fit |
| Phase 3 — Layer Intelligence | ⚠️ **LAYER MAP ONLY** | May use the layer posture table; may not use implementation detail |
| Phase 4 — Technology Intelligence | ⚠️ **CAPABILITY LIST ONLY** | May check "do we have this?"; may not shape the benchmark |
| Phase 5 — Healthcare Intelligence | ⚠️ **WORKFLOW LIST ONLY** | May scope to relevant workflows |
| **Phase R — Repository Dissection** | ✅ **FULL** | This is its subject |
| Phase 6 — Cross-Company Synthesis | ❌ **FORBIDDEN** | Patterns across companies must be found on their own terms |
| **Phase 7 — Opportunity Mapping** | ✅ **FULL** | Where repo reality meets ecosystem findings |
| **Phase 8 — Moat Engineering** | ✅ **FULL** | Moats are built from actual capabilities |
| **Phase Ω — Master Strategy** | ✅ **FULL** | The synthesis point |

---

## 2. Why this matters

**2.1 — Contamination is directional.** If a dossier author knows JARVIS uses Playwright, they will unconsciously score Playwright's alternatives as less interesting. If they know JARVIS has a memory layer, every memory company becomes a "threat." The dossier stops being a description of the world and becomes a mirror.

**2.2 — Discovery is the most vulnerable phase.** Searching for "competitors to my thing" returns things that resemble your thing. Searching for "who owns value in L6" returns the actual landscape, including the players who will commoditise you. The second question is only askable from ignorance of your own implementation.

**2.3 — Synthesis must be independently valid.** A cross-company pattern like *"nobody solves memory consolidation"* is either true of the world or it isn't. If it was derived while looking at JARVIS's memory module, it is unfalsifiable.

**2.4 — The strategy layer is where the value is.** Repo + Dissection + Blueprint against *clean* ecosystem findings produces a real gap analysis. Against *contaminated* findings it produces expensive confirmation.

---

## 3. Enforcement

- Phase 2 run prompts contain no JARVIS implementation detail beyond `08-jarvis-architecture-baseline.md` §2 (the layer posture table) and §3 (theses T1–T4, stated as *hypotheses to attack*).
- `tools/validate.py` flags any dossier referencing repo paths, module names, commit SHAs, or blueprint stage numbers.
- The baseline file deliberately contains **no code-level detail** — it stops at posture and thesis.

---

## 4. What the strategy layer receives

Phase R produces three artefacts consumed by Phases 7, 8, Ω:

| Artefact | Content |
|---|---|
| **Capability Ledger** | What JARVIS *verifiably* does today, evidence-tiered, stage-labelled |
| **Architecture Map** | Layer placement of every real subsystem |
| **Gap Register** | Blueprint claims vs. repo reality; what's designed, built, wired, verified |

These three — not the raw repo — are what meet the ecosystem findings in Phase 7.
