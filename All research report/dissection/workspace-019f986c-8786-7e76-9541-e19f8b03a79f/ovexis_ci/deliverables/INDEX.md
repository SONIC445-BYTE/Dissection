# HEALTHIFY COMPETITIVE INTELLIGENCE — DOCUMENT INDEX
### Prepared for Ovexis · 25 July 2026

| File | Contents | Size |
|---|---|---|
| **`00_MASTER_REPORT.md`** | Deliverables 1–24 + 27: Executive Summary · Company Intelligence · Founder Psychology · Product Reverse Engineering · User Journey · UX Research · Healthcare Workflow · Healthcare Data Architecture · AI Reverse Engineering · Technical Reverse Engineering · API Investigation · Security · Business Model · Growth · Hiring · Customer Intelligence · Decision Ledger · Dependency Graph · Engineering Backlog · Competitive Landscape · Moat Analysis · Failure Analysis · Attack Plan · Future Prediction · Evidence notes + References | ~27,000 words |
| **`25_OVEXIS_STRATEGY_MEMO.md`** | Deliverable 25: Top 50 Copy · Top 50 Improve · Top 50 Ignore · Top 50 Reinvent · Top 50 Market Gaps · Top 20 Blue Ocean · Recommended MVP, GTM, Moat, AI Architecture, Integrations, Pricing, Roadmap | ~7,600 words |
| **`DIAGRAMS.md`** | Product Architecture · AI Architecture · Healthcare Data Flow · User Journey · Feature Dependency Graph · Ovexis Target Architecture · Business Model Canvas | 7 diagrams |
| **`FRAMEWORKS.md`** | SWOT (14 S / 25 W / 13 O / 15 T) · Porter's Five Forces · Value Chain · Risk Register (25 scored risks) | ~3,600 words |
| **`26_FEATURE_INVENTORY.xlsx`** | Deliverable 26: 92 features × 19 columns, colour-coded, filterable, with a README sheet | 2 sheets |
| **`27_EVIDENCE_REGISTER.csv`** | Deliverable 27: 106 claims with source, verbatim evidence, observed-vs-inferred, confidence | 106 rows |

**Raw research artifacts** (captured HTML, HTTP headers, extracted text, DNS/TLS output) are preserved in `/home/user/ovexis_ci/research/`.

---

## THE FIVE FINDINGS THAT MATTER MOST

1. **Their highest-margin product has the weakest clinical outcome.** 🟢 Stanford/Michigan/IIM-A (n≈65,000): AI-only coaching produced **1.22 kg over 3 months** vs 2.12 kg with a human. ~50% of Indian subscribers are on the AI-only tier, and users are already substituting free ChatGPT.

2. **They have behaviour without biochemistry.** 🟢 No lab ingestion, no EHR, no FHIR, no HL7, no LOINC, no genomics. A decade of the deepest behavioural data in Indian consumer health, sitting on top of almost no clinical data. **This is Ovexis's wedge.**

3. **Advertising fell 82%; revenue fell only 14%.** 🟢 FY25 RoC filings. Their organic/SEO engine in India is far stronger than assumed — **do not attack them in India.** Attack the US, where they have ~$2M ARR, no brand, and no HIPAA/SOC 2/BAA.

4. **A 3-point gap between product ratings and service ratings.** 🟢 Google Play 4.5/5 (568,603 ratings) vs MouthShut 1.48/5 (1,148 reviews). Root cause: a 300:1 coach ratio their unit economics require. **They cannot fix it without breaking their business model.**

5. **They bet against data portability.** 🟢 A CGM sensor deliberately configured so it *"may not work with the Abbot app"*, no export, no API. That bet runs against US Information Blocking rules, EU EHDS and India ABDM — and it is the one thing they cannot copy without repudiating a decade of doctrine.

---

## METHOD & ETHICS

All intelligence is from publicly accessible sources. `robots.txt` was read before any retrieval and only `Allow`-ed paths were fetched. No authentication was attempted, no account created, no paywall bypassed, no private API called, no Terms of Service violated. The internal service topology in D10 was read from the **public TLS certificate's Subject Alternative Name field** — a Certificate Transparency artifact — and **none of those hosts were contacted**.

Every claim is labelled 🟢 Confirmed / 🟡 Strong Inference / 🔴 Speculation, and these are never mixed. Where public data could not answer a question, the report says so: **§27.4 of the Master Report lists 22 explicit unknowns**, including valuation, cap table, MAU/DAU, churn, CAC/LTV, patent portfolio, and whether Ria has any safety layer at all. Unsourced content-farm claims about ownership percentages and board composition were located and **deliberately rejected**.
