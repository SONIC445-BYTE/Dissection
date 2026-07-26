# JARVIS Capability Ledger
Phase R · Branch `phase-2-adapter-wiring` @ 2026-07-23 · Analysed 2026-07-26

What JARVIS **verifiably does today**, separated from what is designed, wired, or intended.

---

## 1. Capability states

| State | Meaning |
|---|---|
| **VERIFIED** | Built, tested, and confirmed working by documented live verification |
| **BUILT** | Code exists and is tested, but not confirmed in the live path |
| **WIRED** | Reachable in the normal user path |
| **DARK** | Built but not reachable — no caller, or flag-disabled |
| **DESIGNED** | Documented only. No runtime code. |

> The **DARK** state is the one most competitive analyses miss entirely, and this repository has a notable amount of it. Dark capability is real engineering that produces zero user value until wired — it is inventory, not output.

---

## 2. Ledger

### 2.1 Execution / automation core — the strongest area

| Capability | State | Layer | Evidence |
|---|---|---|---|
| Command router (4 rounds of matching-bug fixes) | **VERIFIED** | L4 | 🟢 E1 — 5 distinct bug classes fixed structurally, each with regression tests |
| Resolution gate (3-branch: unknown / not-installed+offer / resolved) | **VERIFIED** | L4 | 🟢 E1 |
| 12 platform adapters, focus-safety-fixed | **VERIFIED** | L6 | 🟡 E2 — count from blueprint; adapter dir confirmed in tree |
| Browser automation, WhatsApp/Telegram Web | **VERIFIED** | L6 | 🟢 E1 — CAPTCHA/login-wall pause-and-resume documented |
| Desktop adapter launch-fallback | **BUILT** | L6 | 🟡 E2 — commit `31939c8`; blueprint states not independently verified |
| Honest-failure discipline (no silent no-ops, no guessed answers) | **VERIFIED** | L4/Govern | 🟢 E1 — `message_required_but_missing` flag; returns honest "I didn't catch that" **before any adapter is touched** |
| ODAV loop | **WIRED** | L4 | 🟡 E2 — bypasses `ui_agent` entirely; known incomplete gate-outcome handling |

**Assessment.** This is genuine, unglamorous, production-shaped engineering. The `message_required_but_missing` fix is the tell: distinguishing *"no message was intended"* from *"a message was intended but nothing was extractable"* — and checking it centrally before any adapter runs — is the kind of distinction that only gets made by someone who has watched an agent send garbage and decided it must never happen again.

Per `06-technology-ontology.md`, **error recovery and honest failure are CONTESTED-underserved capabilities.** Most agent demos skip them. This repo has them at the router level. That is a real, if narrow, asset.

---

### 2.2 Coding engine / Level6

| Capability | State | Layer | Evidence |
|---|---|---|---|
| Real LLM generation path (was silently stubbed) | **VERIFIED** | L9 | 🟢 E1 — described as most significant bug found |
| Mid-response fence stripping | **VERIFIED** | L9 | 🟢 E1 — regex fix + generalisation test |
| Context injection for editing existing code | **VERIFIED** | L9 | 🟢 E1 — mechanism built and live-verified |
| Upstream file identification ("edit file X" → read it) | **NOT BUILT** | L5 | 🟢 E1 — explicitly declared out of scope in commit |
| Level6 sandbox execution | **VERIFIED** | L6 | 🟢 E1 |
| Level6 LLM debug loop | **VERIFIED** | L4 | 🟢 E1 |
| Level6 LibCST AST transforms | **VERIFIED** | L9 | 🟢 E1 |
| Level6 approval-gated apply + rollback | **VERIFIED** | L4/Govern | 🟢 E1 — snapshot-first, refuses to write without snapshot, reverts on partial failure |
| Level6 enabled in conversation path | **WIRED** | — | 🟡 E2 — commit says flag untouched (`false`); blueprint says flipped since |

**Assessment.** The apply() safety sequence is the best-engineered thing in the repository. Copying *verified sandbox bytes* rather than *plan content* — because an AST step's real output only exists in the sandbox — is a correctness insight that most implementations get wrong and never notice.

⚠️ **Strategic observation:** this is a self-coding agent inside a clinical automation product. It is impressive, and it is in **L9, a layer the baseline marks "compete selectively."** It is not on the healthcare path. See `gap-register.md` §4.

---

### 2.3 Memory

| Capability | State | Layer | Evidence |
|---|---|---|---|
| Persistent cross-session memory (Phase 3a) | **BUILT** | L3 | 🟢 E1 — storage + minimal read/write API; reused existing dead code rather than duplicating |
| Memory/confirmation-gate boundary | **VERIFIED** | L3/Govern | 🟢 E1 — memory can never bypass confirmation gates |
| Conversation token budgeting + time-based trimming | **BUILT** | L3 | 🟢 E1 — `_trim_to_budget()` |
| Context summarisation | **NOT BUILT** | L3 | 🟢 E1 — explicitly verified absent |
| Temporal validity / invalidation | **NOT BUILT** | L3 | 🟠 E3 — no evidence in tree or commits |
| Consolidation / forgetting | **NOT BUILT** | L3 | 🟠 E3 — no evidence |
| Procedural memory | **NOT BUILT** | L3 | 🟠 E3 — no evidence |
| Sub-agent spawning (3b), NL scheduling (3c), skill proposals (3d) | **DESIGNED** | L4 | 🟢 E1 — design doc exists, no runtime code |

**Assessment — and this is the most strategically important finding in the ledger.**

The architecture baseline names **L3 Memory as a layer JARVIS must OWN** ⭐. The repository has storage, a read/write API, and a well-tested safety boundary. It does not have the four capabilities that `06-technology-ontology.md` classifies as CONTESTED in L3: temporal validity, consolidation/forgetting, procedural memory, summarisation.

**Storage is not memory.** Storage is the commodity part; every vector DB has it. The contested, defensible part of L3 is deciding *what to keep, what to invalidate, and what to forget* — and that is precisely the part that isn't built. As of today JARVIS does not own L3 in any defensible sense; it has a persistence layer with a good safety property.

This is not a criticism of the work done — Phase 3a was explicitly scoped as groundwork. It is a statement about the distance between current state and the stated strategic claim, and that distance is the single most important number in this analysis.

---

### 2.4 Voice / perception

| Capability | State | Layer | Evidence |
|---|---|---|---|
| Wake-word detection | **VERIFIED** | L7 | 🟢 E1 — Unicode crash fixed |
| STT (NetHyTechSTT) | **WIRED** | L7 | 🟢 E1 — but see below |
| STT import-time network call | **FIXED** | — | 🟢 E1 — was a live Chrome launch + external URL fetch at import; caused a 59-min test hang |
| TTS | **WIRED** | L7 | 🟡 E2 — on hold pending Qwen3-TTS latency evaluation |
| Text-emotion detection | **DARK** | L5 | 🟢 E1 — built, boundary-tested, **wired to nothing** |
| Screen capture / vision | **BUILT, decoupled** | L5 | 🟢 E1 — `mss` no longer loaded on import |
| OCR | **NOT FOUND** | L5 | 🟠 E3 — no evidence in tree |

⚠️ **The STT architecture is a genuine liability.** A speech-to-text component implemented by driving a headless Chrome instance to an external Netlify URL is not a local-first component — it is a browser-automation dependency on a third-party web page. The import-time hang was fixed; **the architecture was not.** If privacy/local-first is a differentiation thesis (T3), the voice input path currently contradicts it, and in a clinical setting that is a compliance question, not a performance one.

---

### 2.5 Knowledge retrieval

| Capability | State | Layer | Evidence |
|---|---|---|---|
| RAG engine → SERP fetcher | **WIRED, FRAGILE** | L3/L5 | 🟢 E1 — answered a real weather query; scrapes Google HTML directly |
| Real search API tiers (SerpApi/Serper) | **DESIGNED** | — | 🟢 E1 — scoped in detail, not built |
| Quota tracking + failover | **DESIGNED** | — | 🟢 E1 |

Google HTML scraping is fragile and likely ToS-violating; the blueprint already identifies this and has scoped the fix well. Correctly queued.

---

### 2.6 Infrastructure / hygiene

| Item | State | Evidence |
|---|---|---|
| Import-time network calls eliminated (3 chains) | **VERIFIED** | 🟢 E1 — verified by `sys.modules` inspection |
| Import time 28.96s → ~15.6–16.3s | **VERIFIED** | 🟢 E1 — measured, 3 stable runs |
| Lazy loading via PEP 562 `__getattr__` | **VERIFIED** | 🟢 E1 |
| pytest discovery scoping | **VERIFIED** | 🟢 E1 — collection 59-min hang → ~38s |
| Test suite | **177 passing** | 🟢 E1 — 3 pre-existing unrelated failures, stable baseline |
| Onboarding, status box, availability rescanning | **VERIFIED** | 🟡 E2 |
| `jarvis` on PATH | **BUILT** | 🟡 E2 |
| Orb renderer (`jarvis_orb.py`) | **DARK** | 🟢 E1 — built, untested on Windows terminal, not wired |
| `co_brain.py` legacy system #1 | **NOT RETIRED** | 🟢 E1 |

⚠️ **~16 seconds of import time is still a lot** for something a clinician invokes between patients. It was 29s; it is now 16s; the target should be under 3s. This is a product-viability number, not a developer-convenience number.

---

## 3. Summary by layer

| Layer | Baseline posture | Actual state | Verdict |
|---|---|---|---|
| L3 Memory | **OWN** ⭐ | Storage + safety boundary only | ⚠️ **Largest gap vs. stated strategy** |
| L4 Planning | **OWN** ⭐ | Router + gates + ODAV + Level6 loop — genuinely strong | ✅ **Strongest asset** |
| L5 Perception | Own abstraction | Screen capture built; emotion dark; **no OCR** | ⚠️ Thin |
| L6 Execution | Integrate | 12 adapters + browser automation | ✅ Correct posture |
| L7 Voice | Integrate | Works, but STT architecture contradicts local-first | ⚠️ Liability |
| L9 Applications | Selective | Level6 self-coding — sophisticated, off-mission | ⚠️ Scope question |
| **L10 Healthcare** | **Integrate** ⭐ | 🔴 **NOTHING** | 🔴 **Zero healthcare code exists** |
| **L11 Standards** | Conform | 🔴 **NOTHING** — no FHIR, HL7, ABDM | 🔴 **Zero** |

---

## 4. The finding that matters most

**JARVIS today is a well-engineered, honest, local desktop automation agent with a strong planning/execution core and a self-coding subsystem. It contains no healthcare functionality of any kind.**

Not partial. Not prototype. **Zero.** No FHIR, no HL7, no ABDM/ABHA, no OPD queue, no patient/encounter model, no clinical vocabulary, no consent handling. The blueprint acknowledges this precisely — the OPD module is listed as "Stage 0/1's actual missing centerpiece… not yet built."

This is the correct thing to know before any competitive analysis begins, and it should discipline every subsequent conclusion:

- Every healthcare company in the registry is currently an **Integration Target or Market Signal**, never a competitor — JARVIS does not yet compete in L10 because JARVIS is not yet in L10.
- Thesis **T2** ("healthcare workflow depth is a durable moat") is presently **unevidenced by the artefact**. It is an intention.
- Thesis **T3** ("local-first/privacy differentiates") is **actively contradicted** by the STT path.
- Thesis **T1** ("owning the L3+L4 loop") is **half-true**: L4 is real, L3 is storage.
- Thesis **T4** ("adapters over legacy systems") is **proven in consumer apps** (WhatsApp/Telegram) and **untested in clinical systems** — which are a categorically harder target.

The engineering quality is high. The strategic distance to the stated mission is also high. Both are true, and the second is invisible from inside the commit log.
