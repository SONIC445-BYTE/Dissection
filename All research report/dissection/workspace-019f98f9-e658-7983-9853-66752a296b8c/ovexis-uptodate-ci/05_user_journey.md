# DELIVERABLE 5 — Complete User Journey (Screen-by-Screen)

Confidence legend: 🟢 Confirmed | 🟡 Strong Inference | 🔴 Speculation | ⚪ Cannot Verify

Journeys reconstructed from the live login page, live store wizard, App Store listings, institutional-access documentation and user reports. Three personas are tracked because UpToDate's funnel is discontinuous:

- **Persona A — Anonymous web visitor (SEO/evaluator)**
- **Persona B — Institutional clinician (the ~most common real user)**
- **Persona C — Individual self-paying clinician/trainee (the DTC transaction)**

---

## 5.1 Persona A — Anonymous visitor → evaluator

| # | Screen / Touchpoint | What happens | Conf. |
|---|---|---|---|
| 1 | Google result (e.g., "hyponatremia treatment uptodate", wolterskluwer.com product pages, or a patient-ed leaflet) | UpToDate content is largely paywalled; discovery happens at marketing surfaces and via word-of-mouth/brand queries | 🟢/🟡 |
| 2 | `uptodate.com` root | **Immediate gate: "Sign in" page.** Username field, "Remember my username," SSO buttons (Microsoft, OpenAthens), "Sign in Another Way," "Continue without signing in," and a "Subscribe" link to the store | 🟢 (fetched live) |
| 3 | Store link (`store.uptodate.com`) | Persona wizard: **Select Country** (170+ countries listed) → **Select Role & Profession** (Professional / Student or Resident / Purchase for groups / Other) | 🟢 (fetched live) |
| 4 | Package selection | Pro vs Pro Plus; trainee discounts; add-ons (e.g., mobile access add-on historically; Lexidrug add-ons) — pricing individualized by country/role | 🟢/🟡 |
| 5 | Checkout (Salesforce B2B Commerce) | Account creation or login, payment, EzRenew opt-in | 🟢/🟡 |
| 6 | Email receipt + credentials | First login → licence binding | 🟡 |

**Notable journey pathology:** 🟡 the anonymous visitor hits authentication *before value* — no free-topic sample index comparable to OpenEvidence's try-before-signup. The funnel is purely brand-pull: nobody converts who didn't already believe.

## 5.2 Persona B — Institutional clinician (the workhorse path)

| # | Step | Detail | Conf. |
|---|---|---|---|
| 1 | Arrival at institution | IT/library provisions access: IP range, EZproxy, or SSO (frequently via Epic toolbar link) | 🟢/🟡 |
| 2 | First use in workflow | Clicks UpToDate link in EHR (Epic Infobutton/toolbar, Cerner Organizer, TrakCare) or library portal; lands on search page without a personal account — friction ≈ 0 | 🟢 |
| 3 | (Optional) Personal registration | UpToDate Anywhere: associate personal login with institutional entitlement to unlock mobile app + remote access + CME | 🟢 |
| 4 | Consent & verification | Account T&Cs, medical-professional attestation; institutional entitlement verified silently by network/SSO | 🟢/🟡 |
| 5 | 90-day revalidation clock | Remote users must re-authenticate via institutional network/SSO every ~90 days (documented in library guides) | 🟢 |
| 6 | Daily usage loop | Search → Key Points → Summary & Recommendations → calculators/drug checks; CME accrues silently | 🟢 |
| 7 | Year-end | Redeem CME log → cv/licensing file → dependency deepens | 🟢 |
| 8 | Attrition risk event | **Hospital drops license** (cost) → clinician faces personal $500+ decision or migrates to DynaMed/OpenEvidence (extensively documented on Reddit) | 🟢 |

## 5.3 Persona C — Individual buyer (Pro / Pro Plus / trainee)

| # | Screen | Detail | Conf. |
|---|---|---|---|
| 1 | Marketing/price discovery | wolterskluwer.com product pages; word of mouth; Reddit price threads | 🟢 |
| 2 | Store wizard | Country → role → profession (observed) | 🟢 |
| 3 | Package page | Pro (~$579/yr US) vs Pro Plus (~$699/yr, includes Expert AI per 2026 packaging); trainee/resident/other-professional tiers; multi-year discounts | 🟢/🟡 |
| 4 | Verification | Profession claims; trainee status verification for discounts (⚪ exact verification vendor not public) | 🟡 |
| 5 | Consent | EULA, privacy policy, content are "decision support not medical advice" disclaimers; app listing adds "designed for medical professionals" gate | 🟢 |
| 6 | Payment | Card via Salesforce Commerce; app-store IAP for Lexidrug mobile | 🟢 |
| 7 | Onboarding | First-run app: sign-in → entitlement sync (2 mobile devices) → search tutorialisation is minimal (power-user assumption) | 🟡 |
| 8 | Data import | **None. Zero.** Journeys contain no personal data import — the product intentionally accumulates no user data beyond usage history | 🟢 |
| 9 | AI onboarding (Pro Plus) | Expert AI chat with transparency panels; guardrail disclaimers; US-only at launch | 🟢 |
| 10 | Retention | CME ledger + What's New + workflow habit + EzRenew | 🟢 |
| 11 | Support | Help centre, institutional liaisons, account pages; community-style support is absent (⚪ no public forum) | 🟢/⚪ |
| 12 | Renewal | Pre-expiry emails → EzRenew → price-increase negotiation only for groups | 🟢/🟡 |
| 13 | Referral | **No referral program exists publicly**; virality is informal (trainee imprinting, conference presence, author prestige) | 🟢 |

## 5.4 AI-era journey delta (Expert AI, observed 2025–2026)

```
Clinician asks question (chat)
   → guardrail triage (in-scope? drug? emergent?)
   → retrieval from graded corpus (topics + Lexidrug)
   → answer + Assumptions/Sources/Reasoning panels
   → clinician taps through to underlying topic (classic product)
   → CME still accrues; governance logs capture the session for the enterprise
```
🟢 The journey is engineered to *loop back into the classical product* (source links) — AI is a front door, not a destination. 🟡 Deliberate design: every AI answer manufactures a page-view event that sustains the legacy unit of value (topic views/day), which is how WK reports engagement to enterprises.

## 5.5 Journey gaps Ovexis inherits an advantage on

1. 🟢 No anonymous value sample → Ovexis can offer a real free longitudinal preview (import 1 record set, see insights).
2. 🟢 No data-import stage exists → Ovexis's import-onboarding (FHIR pull, Apple Health, PDFs) becomes a magic moment UpToDate structurally cannot copy without becoming a different product.
3. 🟢 No patient-side identity → Ovexis owns the B2C2B counter-position.
4. 🟢 Referral mechanics absent → plum gap for debtor-in-possession virality (share-a-summary with your doctor).
5. 🟡 Support/community invisible → an open clinician community around longitudinal cases would be differentiation by daylight.
