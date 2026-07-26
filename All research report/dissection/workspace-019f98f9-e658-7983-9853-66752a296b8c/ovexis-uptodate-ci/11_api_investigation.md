# DELIVERABLE 11 — API Investigation

Confidence legend: 🟢 Confirmed | 🟡 Strong Inference | 🔴 Speculation | ⚪ Cannot Verify

## 11.1 Public / integration surfaces

| Surface | Type | Status | Conf. |
|---|---|---|---|
| HL7 Infobutton integration (Epic, Oracle Health, InterSystems TrakCare) | Standards-based knowledge-request URL API (context: patient age/sex, problem/med/lab concepts in coded terms) | 🟢 Documented integration guides on uptodate.com/home/epic | 🟢 |
| Embedded search links (toolbar/deep links) | URL-based deep links into search results | 🟢 Documented (Cerner Organizer top toolbar, TrakCare banner) | 🟢 |
| Medi-Span drug data APIs | Licensed drug data objects/APIs embedded in EHR/pharmacy/dispensing stacks | 🟢 WK product family (industry infrastructure) | 🟢 |
| Lexidrug content (licensing) | Content licensing for integration (e.g., within reference suites) | 🟡 Industry-standard licensing; no public self-serve docs | 🟡 |
| Abridge integration | Private partner API: UpToDate evidence into ambient documentation (context-aware CDS) | 🟢 Partnership + GA announced | 🟢 (existence) / ⚪ (spec) |
| Public REST/GraphQL content API | ❌ None found | ⚪ no developer portal, no OpenAPI spec, no SDKs located | 🟢 (absence) |
| Public FHIR server | ❌ None found | — | 🟢 (absence) |
| Webhooks | ❌ None public | — | 🟢 (absence) |
| Developer docs / sandbox | ❌ None public | Integration decks are sales-gated PDFs | 🟢 |

## 11.2 Authentication & entitlements (machine-facing)

- 🟢 Institutional: IP-range, referring-domain ("link resolver") patterns, SAML SSO (Microsoft/OpenAthens), EZproxy. For Infobutton: entitlement validated via the institutional referrer/session.
- 🟡 Partner APIs (Abridge class): contractual + key/secret or federated trust — mechanism not public.
- 🟢 Individual: username/password + subscription seat checks; device limits enforced.

## 11.3 Infobutton request anatomy (standards reconstruction)

🟡 Per HL7 Infobutton standard as documented in UpToDate's Epic page: the EHR sends the clinical concept (diagnosis/med/lab with code system metadata) plus patient context (age, sex) and task context; UpToDate resolves concept → topic(s) via its terminology services (Health Language-class infrastructure) and returns a rendered results page. This is **read-side knowledge resolution**, not data exchange — no clinical data crosses; that is a product/regulatory choice (PHI never touches UpToDate servers by design).

## 11.4 Rate limits, versioning, DX

- ⚪ Rate limits: not published (no public API).
- 🟡 Versioning: Infobutton is standard-pinned (HL7 v2-era knowledge-request infobutton context); internal APIs (app↔backend) evolve silently (mobile app version requirements hint at API churn).
- 🟢 **Developer experience verdict: UpToDate has no developer ecosystem.** Zero hackathons, zero public SDK, zero community. 🟡 Rationale: corpus control = copyright protection; API = leak risk. This is why distribution to AI companies happens via negotiated partnerships (Abridge), not keys.

## 11.5 What Expert AI changes

🟡 Expert AI introduces two new integration surfaces: (1) the enterprise AI governance hooks (session logging, policy) and (2) the partner evidence API implied by Abridge GA. Expect a formalised "UpToDate Evidence API for AI" — likely private/whitelist — within the 12-month window (prediction, File 24). 🟢 Confirmed directional signal: marketing language "established ecosystem approach embeds UpToDate in top tech platforms, AI scribes, and EHRs" is platform-compatible language, and model-context-protocol (MCP/A2A) skills in hiring posts suggest they are internalising agent-interop standards early.

## 11.6 Ovexis API strategy implications

1. 🟡 **Inverse posture:** Ovexis should ship an open, FHIR-R4/R5 + agent-protocol-native (MCP) API from day one — a redistribution surface UpToDate has structurally refused to build. Every developer they ignore is an Ovexis integrator.
2. 🟡 **Webhook/event model** (new lab result, new prescription, risk-score change) is greenfield: UpToDate's read-only world has no events to emit.
3. 🟢 The one integration they *will* defend is EHR-context launch (Infobutton/Cerner millenium patterns). Ovexis must support CDS Hooks + SMART-on-FHIR launch to reach parity there, then win on persistence.
