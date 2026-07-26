# Harvest Markers — Template Addendum
`v1.0.0` · Mitigates extension risk **R2 (harvest brittleness)**

---

## Why

`tools/evolve.py` parses dossier prose to populate 12 registries. Parsing prose is
fragile. Verified live against the Mem0 exemplar: sections **15.2, 15.4, 15.5 and 11**
returned **0 harvestable rows** because their content is written as narrative
paragraphs rather than structured rows.

The content is present and correct. It is simply not *addressable*.

Rather than force every dossier into rigid tables — which would damage the analytical
quality the constitution exists to protect — dossiers add **explicit harvest markers**
around structured emissions. Prose stays prose; the machine gets a clean target.

---

## Usage

Append a marker block at the end of the relevant section. Prose above is unchanged.

```markdown
### 15.2 Architectural decisions worth emulating

Their pluggable-backend design is the standout choice — nineteen vector stores
behind one interface means users never face a fork-or-accept decision...

<!-- harvest:pattern
- id: PAT-011
  name: Pluggable backends behind a stable interface
  category: extensibility
  observed_approach: "19 vector backends behind one interface"
  evidence: [MEM0-C-027]
  jarvis_recommendation: adopt
-->
```

## Marker types

| Marker | Section | Target registry |
|---|---|---|
| `harvest:capability` | 5.1 | capability-registry |
| `harvest:pattern` | 15.2 | pattern-library |
| `harvest:failure` | 13, 14 | failure-library |
| `harvest:principle` | 15.1 | principle-library |
| `harvest:radar` | 15.4, 15.5 | technology-radar |
| `harvest:valuechain` | 11 | value-chain-registry |
| `harvest:moat` | 12 | moat-register |
| `harvest:decision` | any | decision-register |
| `harvest:unknown` | 16.4 | unknown-unknowns |
| `harvest:contradiction` | 16 | contradiction-ledger |

## Rules

1. **Every marker carries `evidence: [claim_ids]`.** Unsourced records are rejected — Article IV applies to registries exactly as it applies to prose.
2. **Markers never contradict the prose above them.** The prose is the analysis; the marker is its structured index.
3. **Markers are HTML comments** — invisible in rendered Markdown, so readability is untouched.
4. **Missing markers produce a loud warning, never a silent skip.** Audit check C9 fails a dossier whose harvest is incomplete.
5. **Do not invent content for a marker.** If a section genuinely has nothing generalisable, emit `<!-- harvest:none reason="..." -->`.

## Retrofit

The Mem0 exemplar was seeded manually into the registries, so its records are correct
and complete. Markers should be added to it during Milestone 2 so it also validates
mechanically — and so it demonstrates the pattern for the 107 dossiers that follow.
