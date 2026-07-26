# Evidence Rules
`v1.0.0` · Phase 0 · Enforced by `tools/validate.py`

The difference between intelligence and content is that intelligence can tell you how much to trust it.

---

## 1. The four tiers

| Tier | Marker | Name | Definition | Permitted sources |
|---|---|---|---|---|
| **E1** | 🟢 | **Verified** | Confirmed in primary artefact. Reproducible by a third party today. | Source code · official versioned docs · API responses · SEC/regulatory filings · signed papers · official pricing pages · public repos with commit refs |
| **E2** | 🟡 | **Corroborated** | Supported by official statements or ≥2 independent credible secondary sources that do not share an origin. | Vendor blog · conference talk · reputable trade press · analyst report · maintainer statement in issue tracker |
| **E3** | 🟠 | **Inferred** | Not stated anywhere. Deduced from architecture, behaviour, job posts, latency, error messages, pricing structure, or implementation patterns. | Reasoned deduction with the reasoning shown |
| **E4** | 🔴 | **Speculation** | Plausible, useful, unproven. Must state its own falsifier. | Analyst judgement |

**Every substantive claim carries exactly one marker.** Prose without a marker fails lint.

---

## 2. The Golden Rules

### 2.1 Inference never promotes to fact
An E3 claim becomes E1 **only** by adding a new primary source with its own source ID to the Evidence Register. Restating it more confidently, or repeating it in a later section, is not promotion — it is fabrication, and it is the mechanism by which most competitive research quietly becomes fiction.

### 2.2 Documentation describes intent; code describes reality
| Artefact | Maximum tier | Note |
|---|---|---|
| Source code, commit, test | E1 | The only artefact that cannot lie about what exists |
| Official versioned docs | E1 for API shape; **E2 for behaviour** | Docs drift from implementation |
| README | **E2 ceiling** | READMEs are marketing with monospace |
| Changelog / release notes | E1 for "shipped", E2 for "works well" | |
| Marketing site | **E4 unless corroborated** | |
| Conference demo | E2 for existence, **E4 for production-readiness** | Demos are staged by definition |
| Job posting | E3 only — signals intent, not capability | Strong signal for *direction* |
| Patent | E3 — proves filing, not shipping | Most patents never ship |
| Funding announcement | E1 for the amount, E4 for the strategy narrative | |

### 2.3 The shipping ladder
Never conflate rungs. Each requires its own evidence:

```
rumoured → announced → waitlist → private preview → public beta
        → GA → documented → SDK-supported → adopted at scale → depended upon
```

A capability at "announced" is **not** a competitive threat in the same sense as one at "adopted at scale". Dossiers must state the rung explicitly for every claimed capability.

### 2.4 Absence of evidence ≠ evidence of absence
If a capability cannot be found, the dossier records: *"No public evidence found for X as of {date}; searched {where}."* → filed under **Research Gaps**. It does **not** say "X does not have this."

### 2.5 Every number carries a date and a source
Revenue, users, stars, benchmarks, valuations, latency, pricing — all decay. `41,000 GitHub stars` is meaningless; `41,000 GitHub stars [S-014, 2026-04-08]` is evidence. Numbers older than 12 months are auto-flagged `STALE` by the linter.

### 2.6 Benchmarks are claims about benchmarks
A vendor-reported benchmark is E2 *about the vendor's claim*, not E1 about capability. Independent reproduction upgrades it. Contested benchmarks must record the contest — including who disputes it and with what counter-number. Benchmark saturation (everyone clustering at the top) must be noted, because a saturated benchmark has stopped measuring anything.

### 2.7 Speculation must be falsifiable
Every 🔴 E4 claim states: *"This would be confirmed by X / killed by Y."* Unfalsifiable speculation is deleted, not downgraded.

---

## 3. Source hierarchy

**Tier A — primary** (supports E1)
Source code · official API responses · versioned official docs · regulatory filings · peer-reviewed papers by the org · official pricing · signed legal documents · standards specifications

**Tier B — official secondary** (supports E2)
Vendor engineering blog · maintainer statements in public issue trackers · conference talks by employees · official changelogs · investor communications

**Tier C — independent secondary** (supports E2 when ≥2 non-shared-origin sources agree)
Reputable trade press with named reporting · independent benchmarks with published methodology · analyst reports naming their method · substantive technical teardowns

**Tier D — community signal** (supports E3 at best; strong for *sentiment*, weak for *fact*)
GitHub issues/discussions · Reddit · Hacker News · Product Hunt · G2/Capterra · YouTube reviews · LinkedIn posts · Discord/Slack communities

> Tier D is where the *truth about user experience* lives even though the *facts* are unreliable. A hundred people saying "the graph tier pricing blocked our evaluation" is genuine evidence about the go-to-market, even if no individual post is citable for a technical fact. Record sentiment as sentiment, tiered E2 (pattern across many sources) or E3 (a few).

**Tier E — untrusted** (E4 only, or excluded)
SEO content farms · AI-generated listicles · vendor-sponsored "comparisons" · pages with no author, no date, no method · competitor marketing about competitors

**⚠ Circular sourcing:** three articles citing the same original blog post are **one** source, not three. Corroboration requires *independent origin*. This is the most common way E4 rumours are laundered into E2 "facts" across the AI-content ecosystem.

---

## 4. Confidence levels

Tier is about *provenance*. Confidence is about *how much weight the conclusion can bear*.

| Confidence | Meaning | Typical basis | Decision weight |
|---|---|---|---|
| **HIGH** | Bet real resources on it | Multiple E1, or E1 + strong E2 | Architecture commitments |
| **MEDIUM** | Plan for it, keep a hedge | Solid E2, or E1 with age/scope caveats | Roadmap sequencing |
| **LOW** | Monitor; don't build on it | E3, or thin/conflicting E2 | Watch-list |
| **UNKNOWN** | Explicitly not established | Contradictions or no data | Research gap → next cycle |

A claim can be **E1/LOW** (verified but narrow — one benchmark, one config) or **E3/HIGH** (inferred but overdetermined — every architectural signal points the same way). Tier and confidence are orthogonal and both are required.

---

## 5. Contradiction protocol

When sources conflict:

1. **Record both.** Never silently pick a winner.
2. **Tier each side** independently.
3. **Date each side** — recency often resolves it.
4. **Look for origin** — is one side merely echoing the other?
5. **Name the contest** in the Evidence Register with a `CONTESTED` flag.
6. If unresolved → confidence drops to **UNKNOWN**, entry goes to Research Gaps.
7. **Contested vendor benchmarks are recorded as contests**, with every disputed figure and its claimant, never as a single number.

Unresolved contradictions are surfaced to the Phase 2.5 audit, which checks whether they were carried forward honestly or quietly resolved by preference.

---

## 6. Evidence Register schema

Every dossier ships `evidence-register.csv`:

| Column | Description |
|---|---|
| `claim_id` | `{COMPANY}-C-###` |
| `claim` | The assertion, one sentence |
| `section` | Dossier section number |
| `tier` | E1 / E2 / E3 / E4 |
| `confidence` | HIGH / MEDIUM / LOW / UNKNOWN |
| `source_ids` | Semicolon-separated `S-###` |
| `source_type` | code / docs / api / filing / paper / blog / press / community / inference |
| `accessed` | ISO date |
| `shipping_rung` | rumoured…depended-upon, or `n/a` |
| `contested` | yes / no |
| `falsifier` | Required if tier=E4 |
| `notes` | Reasoning, especially for E3 |

Plus a source table: `source_id`, `title`, `url_or_ref`, `publisher`, `date`, `tier` (A–E), `origin_independent` (yes/no).

---

## 7. Lint rules (machine-enforced)

| Rule | Severity |
|---|---|
| Substantive claim without tier marker | ❌ ERROR |
| E1 claim whose sources are all Tier C/D | ❌ ERROR |
| E4 claim with no falsifier | ❌ ERROR |
| Source ID referenced but not in source table | ❌ ERROR |
| Source in table never referenced | ⚠ WARN |
| Numeric claim without date | ❌ ERROR |
| Source older than 12 months | ⚠ WARN `STALE` |
| Capability claim without shipping rung | ⚠ WARN |
| Comparative construction naming another company (Phase 2) | ❌ ERROR |
| Same claim at different tiers in different sections | ❌ ERROR (promotion violation) |
| Zero E3 or E4 claims in an entire dossier | ⚠ WARN — implausible certainty, likely unlabelled inference |
| Zero uncomfortable findings for JARVIS | ❌ ERROR |
