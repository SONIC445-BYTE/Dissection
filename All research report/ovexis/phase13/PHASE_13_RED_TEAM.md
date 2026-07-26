# PHASE 13 — RED TEAM
## Attacking Every Recommendation

**Phase:** 13 of 16 (+ Ω) · **Date:** 2026-07-26 · **Status:** COMPLETE — canonical
**Outputs:** `exports/phase13_redteam.{json,yaml,csv}`

**Result: 2 CRITICAL · 4 HIGH · 2 MEDIUM. One recommendation blocked, two require replacement or reframing, three survive.**

---

## 13.1 THE ATTACKS


### RT01 — Beachhead: Indian hospital operational workflows  `CRITICAL`

**Attack:** The 253 HMIS vendors already ship OT/bed/roster modules; they just do not market them in an ABDM partner directory. The entire Tier-1 whitespace is a measurement artifact of looking at marketing copy.

- *Evidence supporting the attack:* G-4.2 explicitly unresolved; ABDM taxonomy has no nursing/OT category (C-19); HPID descriptions are vendor marketing
- *Does it survive?* UNPROVEN - must watch 82 demo videos before committing
- **Verdict: BLOCKED PENDING EVIDENCE**

### RT02 — Moat: adapter coverage x outcome data  `HIGH`

**Attack:** No moat exists for 12+ months. A funded competitor with 10 engineers reaches the same position faster. Coverage is not defensible - it is just work.

- *Evidence supporting the attack:* C-34 self-identified; DL-007 solo builder
- *Does it survive?* PARTIALLY - only if depth-first produces switching cost before a competitor notices the category
- **Verdict: WEAK - accept as real risk**

### RT03 — Category: operational execution agent  `HIGH`

**Attack:** There is no budget line for this. Hospitals buy HMIS, they buy devices, they buy consumables. A CFO cannot code an invoice for "execution agent".

- *Evidence supporting the attack:* Phase12 risk noted; LAW08 CFO veto; no procurement evidence G-6.4
- *Does it survive?* CONDITIONALLY - must attach to an existing budget line (HMIS AMC, or claims recovery %)
- **Verdict: REFRAME REQUIRED**

### RT04 — Pricing: per-completed-workflow  `HIGH`

**Attack:** Outcome pricing requires measurement infrastructure Ovexis must build AND the hospital must trust. Circular dependency: cannot measure outcomes until deployed, cannot deploy without a price.

- *Evidence supporting the attack:* Phase12 unknown 4; DL-034
- *Does it survive?* NO - needs a simpler entry price
- **Verdict: REPLACE with flat pilot fee, outcome pricing later**

### RT05 — JARVIS as the technical foundation  `MEDIUM`

**Attack:** 76% of code unreachable, safety stack orphaned, XOR encryption, zero healthcare code, untested on real hardware. Rewriting from scratch may be faster than wiring this.

- *Evidence supporting the attack:* F-11.1; CB-07; CB-08; G-1.1
- *Does it survive?* YES - the reachable execution stack (ui_executor, odav_loop, command_router, resolution_gate) is genuinely valuable and hard to rebuild
- **Verdict: SURVIVES with Stage 0 mandatory**

### RT06 — India-first sequencing  `HIGH`

**Attack:** India healthcare IT budgets are small; hospitals are price-crushing; enterprise sales cycles are long and relationship-driven. Revenue per hospital may never justify the integration effort.

- *Evidence supporting the attack:* No pricing/budget data exists (G-5.2, G-6.1); LAW11 fragmentation cuts both ways - many small buyers
- *Does it survive?* UNPROVEN - no unit economics data anywhere in corpus
- **Verdict: UNVALIDATED**

### RT07 — Staying out of clinical decisions  `MEDIUM`

**Attack:** Operational-only caps TAM severely and makes Ovexis an IT tool, not a healthcare company. Valuation narrative collapses.

- *Evidence supporting the attack:* Phase12 risk noted
- *Does it survive?* YES - LAW04 makes clinical entry unsafe for a solo builder; this is correct sequencing not permanent scope
- **Verdict: SURVIVES**

### RT08 — Commit gap thesis itself  `CRITICAL`

**Attack:** The gap may persist because completing actions is genuinely undesirable - clinicians WANT the final say. Automating the commit may be solving a problem nobody has.

- *Evidence supporting the attack:* LAW04; Phase7 F-7.5 human review is liability allocation; corpus: "clinician-editable draft, not automated order execution"
- *Does it survive?* PARTIALLY - true for CLINICAL commits, false for OPERATIONAL ones (bed assignment, theatre turnover, claim submission have no clinician judgement)
- **Verdict: SURVIVES ONLY FOR OPERATIONAL SCOPE - validates Phase12 restriction**

---

## 13.2 THE TWO CRITICAL ATTACKS

### RT01 is the one that could invalidate the entire engagement

Phases 4, 6 and 12 all rest on the claim that OT scheduling, bed flow, rostering and claim validation are unowned. That claim comes from two datasets — the dossier corpus and the ABDM registry — **and both measure marketing copy, not shipped modules.**

A 253-vendor HMIS market where nobody ships bed management is *implausible on its face*. The likelier truth is that these modules exist, are poor, and are not marketed in a government partner directory.

**This does not necessarily kill the strategy** — 'exists but is poor' is still an opening, and Phase-4's break-rate finding (1.00 in admin/ICU/ED) suggests these modules do not connect even where present. But the strategy as written claims *unowned*, and that claim is **not evidenced**.

> **Verdict: BLOCKED PENDING EVIDENCE.** DL-065 already requires watching the 82 ABDM demo videos before committing. Red team elevates this from prudent to mandatory.

### RT08 attacks the thesis itself, and sharpens it

The commit gap may persist because clinicians *want* the final say. If so, automating the commit solves a problem nobody has — and four phases of confirmation would be measuring a feature, not a failure.

This survives, but only in a restricted form. It is **true for clinical commits** (prescribing, diagnosis, disposition — where LAW04 and Phase-7 F-7.5 show human review is deliberate liability allocation) and **false for operational commits** (bed assignment, theatre turnover, claim submission — where no clinician judgement exists and the human is merely a transport mechanism).

> **This attack independently validates Phase 12's restriction to operational scope.** The strategy was already narrowed to exactly the region where the thesis holds.

---

## 13.3 WHAT EACH COMPETITOR WOULD DO

| Actor | Move | Impact | Defence |
|---|---|---|---|
| **Epic** | Ships operational modules inside the existing licence at zero marginal price | CRITICAL in US, LOW in India (Epic is NICHE tier there) | India-first (DL-018) is structurally a defence against Epic |
| **Google** | Vertex AI Search for Healthcare + Cloud Healthcare API absorbs the data layer | MEDIUM - attacks before-commit layer, not execution | Execution layer is not their pattern; they sell infrastructure |
| **OpenAI** | Computer-use agents become a commodity capability | HIGH - directly commoditises ui_automation_execution | Domain adapters + healthcare policy + audit are the durable part, not the clicking |
| **Microsoft** | Nuance DAX + Copilot bundled into hospital IT agreements | HIGH in scribing (already excluded), LOW in operations | DL-049 already excludes scribing |
| **HMIS incumbent (Practo/KareXpert/HealthPlix)** | Adds the workflow natively; they own the data and the relationship | CRITICAL - this is RT01 | Partner rather than compete (DL Partnership); or move faster than a 253-vendor fragmented market can coordinate |
| **Hospital CIO** | Rejects: unproven vendor, no BAA/DPDP posture, no references, solo founder, agent touching production systems | CRITICAL - blocks entry entirely | Start in SHADOW mode (feature_gate already supports it): observe and recommend before acting |

### The most dangerous actor is not a competitor

**The hospital CIO is the highest-severity threat.** An unproven vendor with no BAA/DPDP posture, no references, a solo founder, and an agent that touches production systems is a straightforward procurement rejection — LAW08's CIO veto (13 mentions, the most-cited authority in the corpus).

The defence already exists in the codebase: **`feature_gate` supports SHADOW mode.** Enter by observing and recommending, never acting, until trust is established — which is precisely the R5 trust-compounding loop's entry condition. The technical answer to the commercial objection is already built.

### The most dangerous competitor move is OpenAI's

Commodity computer-use agents directly attack `ui_automation_execution` — JARVIS's largest reachable asset. **Defence:** the clicking was never the moat. Domain adapters, healthcare policy, graduated autonomy and audit provenance are the durable parts (ENG04, ENG06, ENG10). If Ovexis's value is that it can click, it has no value.

---

## 13.4 DELIVERABLES

### 📒 Decision Ledger
| ID | Decision | Reversible? |
|---|---|---|
| DL-066 | **RT01 blocks beachhead commitment.** The 82 ABDM demo videos must be reviewed before any build targeting OT/bed/roster | No |
| DL-067 | **Pricing replaced: flat pilot fee first, outcome pricing only after measurement exists** (RT04) | Yes |
| DL-068 | **Category must attach to an existing budget line** — HMIS AMC uplift or claims-recovery percentage — not invent one (RT03) | Yes |
| DL-069 | **Enter every hospital in SHADOW mode.** Observe-and-recommend before act, as both trust mechanism and CIO defence | No |
| DL-070 | **The moat is domain + policy + provenance, never the automation itself** (OpenAI defence) | No |

### ❓ Unknowns Elevated to Blocking
1. **G-4.2 (do HMIS vendors already cover Tier-1?)** — now blocking, not merely open.
2. **Unit economics of an Indian hospital deployment** — RT06 unvalidated, no data anywhere in the corpus.
3. **Would a CIO accept a shadow-mode agent from a solo founder?** No procurement evidence exists.

### 📊 Confidence — Phase 13: **HIGH**
The red team found two critical attacks, one of which blocks a core recommendation. A red team that had confirmed everything would have been evidence of insufficient adversarial effort.

---

## PHASE 13 COMPLETE — proceeding to Phase 14 (Blue Team).
