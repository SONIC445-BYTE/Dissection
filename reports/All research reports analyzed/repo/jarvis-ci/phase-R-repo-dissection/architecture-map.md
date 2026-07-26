# Architecture Map — JARVIS Subsystems by Layer
Phase R · Branch `phase-2-adapter-wiring` @ 2026-07-23

Maps real repository subsystems onto the canonical taxonomy (L0–L15). Consumed by Phases 7, 8, Ω.

---

## 1. Map

```
L0  COMPUTE            (external — Ollama host machine)
      └── ⚠ GPU presence unverified → gates Tier-2 inference work

L1  FOUNDATION MODELS  (external — via Ollama)
      ├── PREFERRED_MODELS — hardcoded fallback list, no runtime tier choice
      └── DEI/LoRA research — DESIGNED, may fail by design

L2  INFERENCE RUNTIME  Ollama
      ├── llm_engine.py — generate() [WIRED]
      ├── generate_stream()          [DARK — exists, uncalled]
      ├── warm-up / keep-alive       [ABSENT]
      └── num_gpu / device config    [ABSENT]

L3  MEMORY  ⭐ posture: OWN
      ├── Persistent cross-session store (3a)  [BUILT]
      ├── Memory ↛ confirmation-gate boundary  [VERIFIED] ← real asset
      ├── conversation_manager._trim_to_budget [BUILT]
      ├── rag_engine → serp_fetcher            [WIRED, FRAGILE]
      ├── summarisation                        [ABSENT]
      ├── temporal validity                    [ABSENT]
      ├── consolidation / forgetting           [ABSENT]
      └── procedural memory                    [ABSENT]
          └── ⚠ storage built; the contested half is not

L4  PLANNING  ⭐ posture: OWN — STRONGEST AREA
      ├── IntentRouter.classify()  [VERIFIED] canned/context/action/code/llm
      ├── CommandRouter            [VERIFIED] 5 bug classes fixed structurally
      ├── Resolution gate          [VERIFIED] 3-branch
      ├── UIExecutor.execute_intent [VERIFIED] central pre-adapter validation
      ├── ODAVLoop                 [WIRED] ⚠ incomplete gate-outcome handling
      ├── Level6 debug loop        [VERIFIED]
      ├── Approval gates + rollback [VERIFIED] ← real asset
      ├── Sub-agent spawning (3b)  [DESIGNED]
      └── NL scheduling (3c)       [DESIGNED]

L5  PERCEPTION  posture: own abstraction
      ├── screen_capture (mss)     [BUILT, decoupled]
      ├── Vision/                  [BUILT, unverified]
      ├── text-emotion detection   [DARK — wired to nothing]
      └── OCR                      [ABSENT] ⚠ gap for Indian clinical reality

L6  EXECUTION  posture: integrate ✅ correct
      ├── 12 platform adapters     [VERIFIED] focus-safety-fixed
      ├── browser_automation       [VERIFIED] CAPTCHA/login-wall resume
      ├── desktop launch-fallback  [BUILT] unverified
      ├── Level6 SandboxRunner     [VERIFIED]
      └── LibCST AST transforms    [VERIFIED]

L7  VOICE  posture: integrate
      ├── WakeService              [VERIFIED]
      ├── NetHyTechSTT             [WIRED] 🔴 headless Chrome → external URL
      ├── Vosk                     [PRESENT]
      └── TTS                      [WIRED] on hold pending Qwen3-TTS eval

L8  OS AI                          [N/A — not contested]

L9  APPLICATIONS  posture: selective
      ├── code_engine              [VERIFIED]
      ├── Level6 (4 phases)        [VERIFIED] ⚠ off healthcare path
      ├── jarvis CLI on PATH       [BUILT]
      └── onboarding / status box  [VERIFIED]

L10 HEALTHCARE PLATFORMS  ⭐ posture: INTEGRATE
      └── 🔴 EMPTY — no EMR/HIS/LIS adapter, no OPD queue, no patient model

L11 HEALTHCARE STANDARDS  posture: conform
      └── 🔴 EMPTY — no FHIR, HL7, ABDM, ABHA, SNOMED, LOINC

L12 AUTOMATION PLATFORMS           [N/A]
L13 DEVELOPER PLATFORMS
      ├── feature_flags/           [BUILT]
      ├── platform_adapters/       [BUILT] — adapter pattern is SDK-shaped
      └── RHINAL MCP integration   [BLOCKED on RHINAL's own MCP server]

L14 ENTERPRISE AI                  [N/A]
L15 FRONTIER
      └── DEI / 8-layer routing probe [DESIGNED, falsifiable]

CROSS-CUTTING — GOVERN  ← the genuine differentiator
      ├── Honest-failure discipline     [VERIFIED] consistent across subsystems
      ├── Confirmation gates            [VERIFIED] memory cannot bypass
      ├── Approval-gated apply          [VERIFIED] snapshot-first, reverts
      ├── RollbackManager               [VERIFIED]
      ├── guards/ safety/ policy/       [PRESENT]
      ├── human_loop/                   [PRESENT]
      ├── Audit trail (remote commands) [DESIGNED — Stage 1a]
      └── Consent (ambient recording)   [BLOCKED — correctly, on legal input]
```

---

## 2. Structural observations

**2.1 — The centre of gravity is L4+L6.** Planning and execution are where the real engineering lives, and they're good. This matches the baseline's "OWN L4" but leaves "OWN L3" mostly unstarted.

**2.2 — GOVERN is the sleeper asset.** It isn't a layer in the taxonomy — it's cross-cutting — and it's the most consistently well-built part of the system. Confirmation gates, rollback, honest failure, and boundary tests appear across every subsystem, not just where convenient. For a clinical product this is the hardest thing to retrofit and the easiest thing to underrate. Phase 8 should treat it as the moat foundation.

**2.3 — The stack is inverted relative to the mission.** Deepest investment sits at L4/L6/L9 (general automation and self-coding); L10/L11 (the mission) are empty; L3's defensible half is empty. Engineering has flowed toward tractable problems rather than mission-critical ones — the vertical-drift pattern.

**2.4 — L13 is accidentally well-positioned.** The adapter pattern plus feature flags is already SDK-shaped. If the adapter SDK thesis (T4) is pursued, the scaffolding partly exists. This is unplanned optionality worth noting.

**2.5 — L7 is the architectural liability.** Voice is the primary input surface and its STT path is a third-party web dependency. Everything else in the system is local; this one thing isn't, and it's the one the user talks into.
