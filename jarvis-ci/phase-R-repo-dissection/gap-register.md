# Gap Register — Blueprint vs. Repository Reality
Phase R · 2026-07-26

Consumed by Phases 7, 8, Ω. Tracks divergence between what the blueprint claims and what the repository shows.

---

## 1. Alignment check

The blueprint is **unusually accurate** about its own state. Most self-reported roadmaps overstate; this one repeatedly understates or correctly flags uncertainty. Verified matches:

| Blueprint claim | Repo evidence | Match |
|---|---|---|
| "commit 31939c8 on phase-2-adapter-wiring" | Branch exists, updated Jul 23 | ✅ |
| "Level6 all 4 build phases complete" | Phase D commit confirms apply() + rollback | ✅ |
| "2 of 3 graded-tier bugs fixed" | Commit `fc91956` documents exactly 2 | ✅ |
| "4 rounds of router matching bugs" | Commits document 5 distinct bug classes | ✅ (understated) |
| "Persistent memory built, boundary-tested" | Phase 3a commit; reused dead code | ✅ |
| "3b/3c/3d designed, not built" | Design doc, no runtime code | ✅ |
| "Import-time network call fixed" | Verified via `sys.modules` inspection | ✅ |
| "OPD module not yet built" | No healthcare code anywhere in tree | ✅ |
| "generate_stream() exists, nothing calls it" | Consistent with tree | ✅ (grep-verified per blueprint) |

**No overstatement found.** This is rare and materially raises confidence in every unverifiable blueprint claim.

---

## 2. Divergences

| # | Item | Blueprint says | Repo shows | Severity |
|---|---|---|---|---|
| D1 | Level6 flag | "Just flipped to `enabled: true` by you" | Phase D commit: "untouched, still `enabled: false`" | 🟡 Low — flip likely post-commit, but *unversioned*; a live capability whose enablement isn't in git is a state-tracking gap |
| D2 | Default branch | Work on `phase-2-adapter-wiring` | Default branch is `feature/improve-readme-presentation-…`, 30 commits behind | 🟠 Medium — the repo's public face is stale; anyone evaluating sees pre-work state |
| D3 | Adapter count | "12 real adapters ported" | Directory confirmed; count not verifiable from surface | 🟢 None — accepted E2 |
| D4 | `# --- ADDITION` sweep | "unclear from history whether completed" | Not resolvable from public surface | 🟡 Low — genuine unknown, correctly flagged |

---

## 3. Capability gaps vs. stated strategy

Ordered by strategic consequence.

### G1 — 🔴 CRITICAL: No healthcare capability
**Baseline:** L10 Integrate ⭐, L11 Conform. **Repo:** zero.
No FHIR, HL7, ABDM/ABHA, patient model, encounter model, OPD queue, clinical vocabulary, or consent primitives.
**Consequence:** T2 is unevidenced. JARVIS is not yet in the healthcare market in any technical sense.
**Blueprint status:** correctly identified, deferred.
**Recommendation:** Stage 0.5 (see `blueprint-review.md` §3.1).

### G2 — 🔴 CRITICAL: L3 is storage, not memory
**Baseline:** OWN ⭐. **Repo:** persistence + read/write API + safety boundary.
Missing: temporal validity, consolidation/forgetting, procedural memory, summarisation — precisely the four the technology ontology marks CONTESTED.
**Consequence:** T1 is half-true. The commodity half of L3 is built; the defensible half is not.

### G3 — 🟠 HIGH: STT contradicts local-first
**Baseline:** T3 privacy differentiation. **Repo:** STT drives headless Chrome → external Netlify URL.
**Consequence:** the primary input surface violates the primary differentiation claim. Clinical compliance issue, not a latency issue.
**Blueprint status:** treated as fixed infrastructure debt; **should be thesis-critical.**

### G4 — 🟠 HIGH: No physician validation gate before Stage 1
No point in the plan where a clinician uses the system before remote access and ambient mode are built.
**Consequence:** assumptions compound across three stages of build.

### G5 — 🟡 MEDIUM: No OCR
**Baseline:** L5 own the abstraction. **Repo:** screen capture only.
Indian clinical reality is paper-heavy: handwritten prescriptions, printed reports, mixed-script forms. `06-technology-ontology.md` marks Indic/handwritten medical OCR as **CONTESTED** — i.e. a real opportunity. Currently absent.

### G6 — 🟡 MEDIUM: Dark capability inventory
Text-emotion detection (built, wired to nothing), `jarvis_orb.py` (built, untested, unwired), `generate_stream()` (exists, uncalled).
**Consequence:** completed engineering producing zero user value. Wiring `generate_stream()` is hours of work for the largest available perceived-latency win.

### G7 — 🟡 MEDIUM: Import time ~16s
Down from 29s. Target for between-patient use is <3s.

### G8 — 🟢 LOW: Known open items
ODAV gate-outcome handling; `co_brain.py` retirement; `# --- ADDITION` sweep; 3 pre-existing test failures.

---

## 4. Off-mission investment

Not defects — genuinely good work — but layer-misaligned relative to the stated mission.

| Item | Layer | Baseline posture | Note |
|---|---|---|---|
| Level6 autonomous coding | L9 | "Compete selectively" | Sophisticated; not on healthcare path |
| Orb renderer | — | Cosmetic | Correctly lowest priority |
| Text-emotion detection | L5 | — | Blocked behind a deferred TTS decision |
| DEI / LoRA research | L1/L2 | "Abstract" / "Integrate" | May fail by design; correctly non-blocking |

**Pattern:** investment has flowed toward L4/L6/L9 — the layers with clear, satisfying engineering problems — while L3's hard half and L10/L11 entirely remain empty. This is the vertical-drift risk named in `blueprint-review.md` §2.2.

---

## 5. Genuine assets (feed Phase 8 moat engineering)

| Asset | Why it matters |
|---|---|
| **Honest-failure discipline** | CONTESTED-underserved ecosystem-wide; consistently applied here; **the clinical licence to operate** |
| **Approval gates + rollback** | Snapshot-first, refuses-without-snapshot, reverts-on-partial-failure. Retrofitting this is brutal; having it early is real |
| **Router bug-class discipline** | Fixed structurally, not per-instance. Compounding quality |
| **Verified-bytes-not-plan-content** | Correctness insight most implementations get wrong silently |
| **Evidence-based killing** | Early-exit killed on measured data. Rare and valuable |
| **Commit-message rigour** | Records what was *not* done. Makes the codebase auditable — which matters enormously in regulated contexts |

Assets 1, 2 and 6 are the seeds of a **clinical-safety moat** — slow, unglamorous, expensive to retrofit, and exactly what generic agent companies skip. Phase 8 should build on these.

---

## 6. Open questions for Phase 7

| # | Question |
|---|---|
| RQ-01 | Which OPD workflow is thinnest-but-real for Stage 0.5? |
| RQ-02 | Is WhatsApp automation validated physician need, or available capability? |
| RQ-03 | What local STT meets clinical latency on target hardware? |
| RQ-04 | Does the target machine have a discrete GPU? (gates Tier-2 inference work) |
| RQ-05 | What is RHINAL's scope, and where is its MCP server? |
| RQ-06 | Which Indian hospital tier is the first buyer? (determines whether L10 integration or greenfield) |
| RQ-07 | Who is the first physician, and when do they touch it? |
