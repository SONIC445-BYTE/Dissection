# Strategic Role Classification
`v1.0.0` · Phase 0 · Mandatory per company · Enforced by `tools/validate.py`

> The purpose of this document is to prevent the single most expensive mistake in competitive strategy: **calling everything a competitor.**

Competitor inflation causes teams to rebuild commodities, fear their suppliers, ignore their best partners, and build roadmaps out of anxiety. Most of the ecosystem is leverage. This taxonomy forces that recognition.

---

## 1. The six roles

### 🔵 1. Foundational Dependency
*JARVIS depends on it. Its failure is a JARVIS failure.*

**Test:** if this vanished, would JARVIS stop working or require months of rework?

**Implications:** dependency risk must be measured; abstraction layers or second sources required for any entry with `Dependency_Risk ≥ 3.5`; monitor licence and pricing changes continuously.

**Never** classify a Foundational Dependency as a competitor merely because it is large or occasionally ships something adjacent. *Typical: silicon vendors, inference runtimes, model providers, core OSS libraries.*

---

### 🟢 2. Integration Target
*JARVIS should connect to it. Its install base is JARVIS's opportunity.*

**Test:** do JARVIS's target users already run this, and is JARVIS more valuable by reaching into it?

**Implications:** adapter ladder placement is mandatory (`Constitution VIII.2`); integration effort estimated; API/standards stability assessed; **replacement explicitly ruled out.**

This is the correct home for **every system of record**. Attacking an EMR head-on is the standard way healthcare startups die — the incumbent owns a decade of workflow, training, compliance sign-off, and switching cost measured in careers. *Typical: EMR/HIS platforms, national digital health infrastructure, practice management systems.*

---

### 🔴 3. Direct Competitor
*Contests the same strategic layer for the same user.*

**Test — all three required, no exceptions:**
1. **Named contested layer** — which L0–L15?
2. **Named contested capability** — which specific JARVIS capability?
3. **Named substitution** — which buyer or user picks one *instead of* the other?

**If any of the three is missing → the classification is wrong.** Default to Market Signal.

> A company can be enormous, adjacent, and fast-moving and still not be a Direct Competitor. Overlap of *vibes* is not overlap of *buyers*.

**Implications:** attack plan required; differentiation must be structural rather than feature-level; monitored every cycle.

---

### 🟣 4. Potential Partner
*Collaboration creates more value than competition.*

**Test:** is there a concrete joint offering, distribution swap, or integration where both sides gain more than either gains alone?

**Implications:** name the specific collaboration surface. "They seem nice" is not a partnership thesis. Record what each side gives and gets, and what would make the partnership sour. *Typical: complementary-layer players, distribution partners, standards bodies, systems integrators.*

---

### ⚙️ 5. Technology Supplier
*Provides a reusable capability, not a competing product.*

**Test:** could JARVIS consume this as a component inside its own architecture?

**Distinguishing from Foundational Dependency:** a supplier is **replaceable**; a foundational dependency is not. Playwright is a supplier (Selenium exists). CUDA is a dependency (it effectively doesn't).

**Implications:** evaluate licence, replaceability, abstraction cost. **Never rebuild a commodity supplier's product** — that is the L6/L7 trap. *Typical: browser drivers, OCR engines, STT/TTS, UI automation libraries, vector stores.*

---

### 📡 6. Market Signal
*Not a direct relationship, but its decisions shape the ecosystem.*

**Test:** would a major move by this company change JARVIS's plans even though JARVIS neither uses nor competes with it?

**Implications:** watch-list with named trigger events. Cheap to monitor, expensive to miss.

**This is the correct default** when a company is interesting but the relationship is unproven. *Typical: frontier labs' product direction, category-defining apps, well-funded adjacent startups, regulators.*

---

## 2. Decision tree

```
START
  │
  ├─ Does JARVIS's architecture consume this today or in the committed roadmap?
  │     ├─ YES → Would its disappearance break JARVIS or cost months?
  │     │          ├─ YES → 🔵 FOUNDATIONAL DEPENDENCY
  │     │          └─ NO  → ⚙️ TECHNOLOGY SUPPLIER
  │     └─ NO ↓
  │
  ├─ Do JARVIS's target users already run this as a system of record / daily tool?
  │     ├─ YES → Is JARVIS more valuable by reaching into it than by replacing it?
  │     │          ├─ YES → 🟢 INTEGRATION TARGET
  │     │          └─ NO  → continue ↓ (replacement thesis must be written and defended)
  │     └─ NO ↓
  │
  ├─ Can you name ALL THREE: contested layer + contested capability + substituting buyer?
  │     ├─ YES → 🔴 DIRECT COMPETITOR   (write the attack plan)
  │     └─ NO ↓
  │
  ├─ Is there a specific, nameable joint value surface?
  │     ├─ YES → 🟣 POTENTIAL PARTNER
  │     └─ NO ↓
  │
  └─ 📡 MARKET SIGNAL  (default — with named trigger events)
```

**The tree is ordered deliberately.** Dependency and integration are checked *before* competition, because the human instinct is to reach for "competitor" first. The tree makes you rule out the productive relationships before you're allowed to declare war.

---

## 3. Multiple roles

Exactly **one primary role**. Secondary roles permitted with written justification naming layer + workflow.

**Common legitimate combinations:**

| Combination | Example shape | Handling |
|---|---|---|
| Foundational Dependency + Market Signal | A model provider you depend on whose product moves reshape the category | Monitor dependency risk *and* strategic direction |
| Integration Target + Direct Competitor | A platform you integrate with that is building a competing native feature | ⚠ `COMPLEX` — the "coopetition squeeze"; needs an explicit exit trigger |
| Technology Supplier + Potential Partner | A component vendor who could co-market | Standard; low risk |
| Direct Competitor + Potential Partner | Competing today, complementary in a different segment | Rare and unstable; re-review every cycle |

**The dangerous one is Integration Target + Direct Competitor.** This is the platform-squeeze pattern: you build on someone who is building what you build. It requires a pre-agreed **exit trigger** — a specific observable event that flips the relationship — written *before* it happens, because it will not feel like the right time to leave when it does.

---

## 4. Anti-patterns

| Anti-pattern | Symptom | Correction |
|---|---|---|
| **Competitor inflation** | >30% of registry marked Direct Competitor | Re-run the three-part test on each; most will fail |
| **Supplier fear** | Treating a library as a competitor | Ask: do they sell to *your* buyer? |
| **Partner optimism** | Partner with no named joint surface | Demote to Market Signal until a surface exists |
| **Dependency denial** | Depending on something classified as Market Signal | Reclassify; add mitigation plan |
| **Giant reflex** | Classifying by company size | Classify by *layer overlap*, never by market cap |
| **Role drift** | Silent reclassification between cycles | Every change needs a Decision Ledger entry + trigger |

---

## 5. Expected distribution

A healthy registry of ~80 entities looks roughly like:

| Role | Expected share | Reality check |
|---|---|---|
| 📡 Market Signal | 30–40% | Most of the ecosystem is context |
| ⚙️ Technology Supplier | 20–25% | The build-vs-buy surface |
| 🟢 Integration Target | 15–20% | Where healthcare revenue lives |
| 🔵 Foundational Dependency | 10–15% | Small set, high consequence |
| 🟣 Potential Partner | 5–10% | Must be specific to count |
| 🔴 **Direct Competitor** | **5–10%** | **If this exceeds 15%, the analysis is fear-driven** |

The Phase 2.5 audit checks this distribution. A registry where a quarter of entries are "competitors" has not done the work — it has produced a threat list, and threat lists make teams defensive, imitative, and slow.
