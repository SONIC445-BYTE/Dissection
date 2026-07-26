# DELIVERABLE 12 — Security & Compliance Investigation

Confidence legend: 🟢 Confirmed | 🟡 Strong Inference | 🔴 Speculation | ⚪ Cannot Verify

## 12.1 Compliance posture

| Domain | Position | Conf. |
|---|---|---|
| HIPAA | UpToDate (reference) is largely **outside HIPAA scope as a content service**; clinician accounts contain no PHI by architecture. Where institutional flows touch EHR context (Infobutton), patient identifiers are not transmitted (only concepts/context). BAA discussion is relevant for enterprise Expert AI session logging; WK offers enterprise legal/compliance documentation (privacy policy publicly available) | 🟢 posture / 🟡 BAA specifics |
| GDPR | Global privacy policy; EU/SCC-style transfers via WK group policies; store supports 170+ country billing. 🟡 Corporate Group-level GDPR program confirmed via public privacy pages | 🟢/🟡 |
| SOC 2 / ISO | ⚪ No public SOC 2 Type II attestation or ISO 27001 certificate for UpToDate located. (WK enterprise procurement presumably handles via security questionnaires; treat as unverified.) | ⚪ |
| FDA | Non-device CDS framing — content authored by professionals, transparent sources; Expert AI designed to keep clinician-in-the-loop ("review recommendations, then decide next steps"), aligning with 21st Century Cures non-device CDS criteria | 🟡 |
| ONC / Promoting Interoperability | Explicit support marketed: linked CDS counts toward PI program (Epic page) | 🟢 |

## 12.2 Technical security controls (visible + inferred)

- 🟢 **Identity:** SSO federation (SAML/OIDC) via Microsoft Entra and OpenAthens; institutional IP/EZproxy; 90-day revalidation for remote institutional users; device limits on mobile.
- 🟡 **Encryption:** TLS everywhere (public endpoints); encryption at rest presumed at cloud posture (AWS/Azure managed storage) — not publicly attested (⚪).
- 🟡 **Audit logs:** enterprise governance logging for Expert AI is a marketing claim (policy compliance/oversight); legacy product audit depth unknown.
- 🟢 **Secure SDLC:** GenAI job post mandates threat modeling, least privilege, privacy-by-design — evidence of a formal program on the AI platform.
- 🟡 **AI-specific security:** RAG architecture constrains output to corpus (reduces injection surface vs open-web agents); guardrail layers unverified; MCP/A2A interop will raise new agent-identity security questions they're hiring to solve.

## 12.3 Threat model (independently constructed)

| Threat | UpToDate exposure | Severity for them |
|---|---|---|
| Credential sharing / seat abuse | Known phenomenon (Reddit documents sharing workarounds); mitigated by device limits, revalidation | Medium 🟢 |
| Account takeover of clinician accounts | Low PHI, but CME/identity + billing data at risk | Medium 🟡 |
| Corpus exfiltration (scraping/API abuse) | Historically their #1 IP threat — explains no public API, aggressive paywalling, session limits | High 🟡 |
| Prompt injection (Expert AI) | Corpus-only grounding reduces web-borne injection; drug-harmonisation adds second corpus; user-typed "patient context" is an injection path they must filter | Medium 🟡 |
| Judicial/product liability for AI answers | Managed by clinician-in-loop framing + transparency artefacts; the "non-device CDS" legal wall | High 🟡 |
| Insider editorial compromise | Author network is the supply chain; reputation-vetting and multi-layer editor review mitigate | Low–Med 🔴 |

## 12.4 Access control & BAA

- 🟢 Seat/subscription model with store-side account management; group admin roles exist for 2–19 cohorts; enterprise admin console for Expert AI governance.
- 🟡 Institutional contracts govern support/security terms; public details are not available (standard for enterprise-health vendors). BAA for Expert AI deployments is presumably negotiable — ⚪ not published.

## 12.5 Residual risk register (their blind spots)

1. 🟡 **Compliance-transparency gap:** in an era where OpenEvidence markets "HIPAA-compliant" loudly, UpToDate's public security documentation is thin for a 2026 buyer — procurement teams now expect attestation PDFs. WK relies on brand instead.
2. 🟡 **AI session data residency:** Expert AI runs across three clouds/providers (Azure OpenAI/AWS/Gemini). Data-residency explainability to European buyers is nontrivial; OpenEvidence *withdrew from EU/UK* — UpToDate has 190-country exposure and can't.
3. 🟢 **Editorial supply-chain integrity:** 7,600 external contributors is the largest trusted-third-party surface in clinical content — a conflict-of-interest or credential lapse anywhere is a brand event. (Their disclosure policies are strong; scale is the risk.)

**Ovexis design mandate (derived):** because Ovexis *will* hold PHI/longitudinal data, it must invert this profile: SOC 2 Type II + HITRUST roadmap from day one, BAA templates public, data-residency options, per-record consent receipts, and an agent-security program (signed tool calls, MCP auth) that becomes a sales asset rather than a questionnaire liability.🟡
