# Blueprint Review — "What do you say?"
Phase R · 2026-07-26 · Reviewed against `phase-2-adapter-wiring` @ 2026-07-23

---

## Verdict

**The direction is right and the discipline is unusually good. There is one structural flaw, and it is serious enough to undo the rest if it isn't fixed.**

Let me be specific about both halves.

---

## 1. What this blueprint gets right

### 1.1 Stage discipline is real, not decorative
Most staged roadmaps are marketing documents with the word "phase" in them. This one has teeth: Stage 2 and 3 are *intentionally blank*, with an explicit refusal to design them. That is the correct call and it is rare — and it directly matches `00-research-constitution.md` Article III, which I wrote before seeing your blueprint. Independent convergence on the same principle is a good sign.

### 1.2 The failure-mode grounding is correct
Citing Olive AI, Forward, and Plena as scope-creep deaths is the right reference class. Olive AI in particular is the canonical case: it raised enormous sums, promised an "AI workforce" for healthcare, sprawled across too many hospital functions, and was dismantled and sold for parts. Anchoring your process discipline to that pattern is sound.

### 1.3 Honest failure as an architectural principle
This is the strongest thing in the project. "Honest about failure" in Stage 0's definition, the CodeEngine fake-fallback fix, `message_required_but_missing`, "not a guessed answer if the chain fails" — this is a *consistent* principle applied across subsystems, not a slogan.

Per `06-technology-ontology.md`, confidence estimation and honest failure are **CONTESTED-underserved** across the entire agent ecosystem. Most agent products are confidently wrong by default. You've made not-being-confidently-wrong a house rule. **In a clinical context that is not a nice-to-have — it is the entire licence to operate.** Protect this above every other property.

### 1.4 Killing things with evidence
Explicitly killing runtime early-exit on the basis of measured oracle results (0.00%/0.10% skip ratios), and noting that suitability *decreases* with instruction-tuning while JARVIS sits at the wrong end of both axes — that is genuine research discipline. Equally good: "verify Brave Search's free tier directly before deciding; sources disagreed," and "test prefix/KV cache before building — Ollama may already do it."

The DEI falsifiers (>50ms adapter swap, or specialised-1.5B losing to generalist-7B) are properly falsifiable. This is exactly the evidence hygiene `02-evidence-rules.md` §2.7 demands.

### 1.5 Auth-before-remote, and the machine-off honesty
Treating authentication as a hard prerequisite rather than later hardening — with second factor, session timeout, and full audit trail — is correct and most people get it wrong. And refusing to solve machine-off with always-on cloud, accepting queued delivery instead, is intellectually honest: it keeps the local-first constraint intact rather than quietly abandoning it for convenience.

### 1.6 Ambient mode's consent posture
Never default-on, mandatory visible indicator, short timeout, re-confirmation, and — critically — **splitting the two consumers by risk** and blocking the recording/Rhinal handoff on real consent resolution rather than engineering. Recognising that meaningful consent from everyone in the room under DPDP + medical council rules + hospital policy is *not an engineering question* is exactly right, and it is the kind of thing that sinks health startups that treat it as a checkbox.

---

## 2. The structural flaw

### 2.1 Stage 0 has no healthcare in it

Read your own Stage 0 definition: *"Voice/text command in, verified action out, honest about failure."*

That is a **generic desktop automation agent**. Nothing in it is clinical. And the repository confirms it precisely — `capability-ledger.md` §4 finds **zero** healthcare code: no FHIR, no HL7, no ABDM/ABHA, no patient or encounter model, no OPD queue, no clinical vocabulary, no consent primitives.

You already know this. It's in your own document: *"OPD queue/patient-flow module — identified as Stage 0/1's actual missing centerpiece (the one thing that makes JARVIS a hospital tool rather than a generic automation tool) but not yet built."*

That sentence is the most important line in the blueprint, and it is filed under "Explicitly deferred, not started."

### 2.2 Why this is a structural flaw and not just a sequencing preference

Scope creep is not the only way products die. The blueprint is heavily defended against **horizontal** creep (expanding stages too early) and completely undefended against **vertical drift** — going ever deeper into a foundation that hasn't been validated against the actual user.

Consider what got built while the OPD module waited:

- A four-phase autonomous coding engine with AST transforms, sandbox execution, LLM debug loops, and approval-gated apply with rollback
- A terminal orb renderer with z-buffered ring occlusion
- Text-emotion detection, boundary-tested, wired to nothing
- A Layer-3 research programme (DEI, LoRA hot-swap, routing probes)

The Level6 work is genuinely excellent engineering. **It is also, by your own layer map, L9 — a layer marked "compete selectively" — and it is not on the healthcare path at all.** A self-coding agent is not what makes a physician adopt JARVIS.

Here is the uncomfortable framing: **Olive AI died of horizontal scope creep. Forward died of building beautiful infrastructure that patients didn't want. Your blueprint is armoured against Olive's death and exposed to Forward's.**

### 2.3 The validation gap compounds

Stage 1's gate is stated as *"do not begin designing Stage 2/3 until Stage 1 has real physician usage behind it."* Good. But **Stage 0 has no such gate.** There is no point in the current plan where a physician touches the system before Stage 1 is built.

So the sequence is: build a complete reliable execution layer → build remote access → build ambient mode → *then* find out what a physician actually needs. Every unvalidated assumption compounds across all three.

And the assumptions are load-bearing. That "12 adapters" list is WhatsApp, Telegram, browsers, desktop apps. **Ask the harder question: is WhatsApp automation what a physician needs, or is it what was buildable?** In Indian clinical practice WhatsApp genuinely *is* a real clinical communication channel — so this may well be right. But it is currently an assumption with a strong argument behind it, not a validated finding, and it should be labelled as such.

### 2.4 Two theses the repo currently contradicts

From `08-jarvis-architecture-baseline.md`:

**T3 — local-first/privacy is a differentiator.** The STT path drives a headless Chrome to an external Netlify URL. That is not local-first; it is a browser-automation dependency on a third-party web page, and voice is the *primary input surface*. The import-time hang was fixed; the architecture was not. In a room with a patient in it, this is a compliance question rather than a latency one. **This should be reclassified from "infrastructure debt" to "thesis-critical."**

**T1 — own the L3+L4 memory/planning loop.** L4 is genuinely strong. L3 is storage plus a good safety boundary. The contested, defensible parts of memory — temporal validity, consolidation/forgetting, procedural memory, summarisation — are all absent, and `06-technology-ontology.md` classifies exactly those as the underserved frontier. Storage is the commodity half. Right now the claim to own L3 is aspirational.

---

## 3. What I'd change

### 3.1 Add a Stage 0.5 — "One real clinical workflow, end to end"

Not a full OPD module. **One workflow, one physician, real use.** Candidate: *the OPD queue* — patient list, current patient, next patient, simple status transitions, spoken queries and updates. No EMR integration, no FHIR, no ABDM. Local state, voice in, verified action out — reusing exactly the Stage 0 machinery you've already built.

Why this specifically:
- It uses the strong parts (router, gates, honest failure) and requires nothing that doesn't exist
- It's the smallest thing that makes JARVIS a *hospital* tool rather than a generic one
- It puts a physician in front of the system **before** remote access and ambient mode are built
- It converts T2 (healthcare depth is a moat) from intention into evidence
- Everything learned reshapes Stage 1's priorities — probably substantially

**Gate Stage 1 behind it.** Remote access and ambient mode are far more valuable when you know which workflow they're serving. Ambient mode with no clinical workflow underneath it is a recording feature; ambient mode attached to a live OPD queue is a product.

### 3.2 Reclassify the STT architecture as thesis-critical
Move it out of general infrastructure debt. Local STT (Vosk appears to be present already; Whisper-family models are the obvious candidate) is a **precondition for the privacy claim**, not an optimisation. If a physician asks "does my voice leave this machine?", the answer must be no, and today it isn't.

### 3.3 Name the L3 gap honestly in the blueprint
Add a line: *"Memory today is persistence + safety boundary. Temporal validity, consolidation/forgetting, and procedural memory are not built. Owning L3 requires them."* This isn't self-criticism, it's scope clarity — and per §1.3 above, honesty is your differentiating property. It should apply to the roadmap too.

### 3.4 Put Level6 behind a stage gate
It's done and it's good — leave it enabled. But formally mark **further L9 self-coding investment as out of scope until Stage 0.5 ships.** The tier-6 remainder, 3b sub-agent spawning, 3d skill-writing: all of these deepen a layer that isn't the mission. The blueprint defends against horizontal creep; this is the vertical-creep equivalent and it needs the same explicit fence.

### 3.5 Add an anti-vertical-drift check
Alongside the existing stage discipline, one question at every planning point:

> **"Does this item move a physician closer to using JARVIS, or does it make JARVIS more impressive to an engineer?"**

Both are legitimate answers — infrastructure work is real work. But the ratio needs watching, and right now the honest count over the last cycle is heavily weighted toward the second.

### 3.6 Keep the import time in view
~16s from 29s is good progress. For something invoked between patients, the target is under 3s. Not urgent yet; will become an adoption blocker the moment a real physician uses it in clinic.

---

## 4. Sequencing I'd recommend

| Order | Item | Rationale |
|---|---|---|
| 1 | Close the 3-engine audit formally | Already your call; perpetual "in progress" hides state |
| 2 | Verify the desktop adapter fix | Small, blocks the queue |
| 3 | Knowledge-retrieval fix | Scoped well; live fragility; ToS exposure |
| 4 | **Stage 0.5 — OPD queue, one physician** | **The change I'm actually arguing for** |
| 5 | Local STT | Thesis-critical; do before ambient mode exists |
| 6 | Tier-1 inference wins (streaming, warm-up, token budgets) | Hours each, large perceived-latency payoff |
| 7 | Stage 1a remote access | *After* 0.5 tells you what to make remote |
| 8 | Stage 1b ambient (suggestions only) | *After* 0.5; recording still consent-blocked |
| — | Orb, emotion wiring, DEI, further Level6 | Genuinely nice; not on the path |

Note that items 1–3 are exactly your existing queue. I'm not reordering your near-term work — I'm inserting 0.5 ahead of Stage 1 and promoting local STT.

---

## 5. Answering the question directly

**Is this the right direction?** Yes. The stage discipline, the evidence hygiene, the honest-failure principle, and the consent posture are all better than most funded healthtech teams manage. The engineering quality visible in the commit history is genuinely high — the Level6 apply() correctness reasoning and the router bug-class fixes are the work of someone who understands why systems fail.

**Is there something to fix?** Yes, one thing: **you have built a foundation for a healthcare product without yet touching healthcare, and your blueprint's own discipline mechanism doesn't catch that, because it's designed to prevent expanding too fast rather than deepening in the wrong place.**

The fix is small and doesn't disturb what you've built: **one real clinical workflow, one real physician, before Stage 1.** Everything you've engineered so far is the right substrate for it. The risk isn't that the foundation is wrong — it's that it keeps getting deeper while the question it exists to answer stays unasked.

---

*Assessment based on public repository surface and the blueprint as supplied. Not independently reproduced by running the code — see `README.md` evidence note.*
