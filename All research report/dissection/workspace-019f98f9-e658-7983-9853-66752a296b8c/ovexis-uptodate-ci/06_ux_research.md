# DELIVERABLE 6 — UX Research

Confidence legend: 🟢 Confirmed | 🟡 Strong Inference | 🔴 Speculation | ⚪ Cannot Verify

Method note: public-market research only (live login + store pages, App Store/Play listings, app-store review text, product screenshots on WK pages, user testimony). The authenticated app interior was not accessed; interior-UI claims are labelled 🟡/⚪ accordingly.

---

## 6.0 Headline finding

🟢 **The product with the strongest clinical brand in its category ships one of the weakest-rated flagship apps.** UpToDate iOS app: **3.6★ / 571 reviews** (Jul 2026); UpToDate Lexidrug app: **4.7★ / 4,749 reviews**. The two apps serve identical content-adjacent jobs with wildly different UX outcomes — proof that UX debt is a *choice product of priorities*, not inability.

---

## 6.1 Typography & content readability

- 🟡 **Document-era typography:** professional, dense, serif-adjacent body conventions inherited from medical publishing; long-form topic pages with numbered sections and dense tables. Readability for 60-second clinical scanning is achieved through *structure* (Summary & Recommendations block, bullet hierarchy) rather than through generous typographic design.
- 🟡 Grade badges (1A–2C) function as inline micro-typography that lets eyes skip to decision-grade statements — a genuinely excellent information-design pattern.
- 🔴 Font sizes/contrast tuned for desktop reading; mobile resizing historically awkward (user complaints reference UI jank, e.g., the reported screen-orientation flip bug in reviews).

## 6.2 Spacing & layout

- 🟡 Desktop layout = three-zone document view: top search/command bar, left nav/outline, main content column. Information density is high; whitespace budget is low — intentional for expert skimmers, punishing for novices.
- 🟡 Key Points panels and answer-first blocks demonstrate the team *does* understand progressive disclosure; it's applied unevenly (search layer modernised, topic layer still 2010s document).

## 6.3 Accessibility

- 🟢 Evidence of standards effort: store page carries browser-support/accessibility-angled notices and structured semantic HTML (observed fetch shows clean heading hierarchy); patient-education leaflets in plain language and 19 languages are genuine inclusion work.
- ⚪ No public WCAG audit / accessibility conformance report located. 🟡 Mobile app review corpus includes usability complaints consistent with weak zoom/responsive behaviour — speculative link to accessibility.

## 6.4 Navigation

- 🟢 Primary nav: Search-first (the search box IS the IA). Topic trees by specialty exist as browse fallback.
- 🟡 Elder IA pattern: specialty → topic → section → subsection anchors. Breadcrumbs minimal. Cross-links are content-hyperlinked (topics reference each other) — navigation by *hypertext*, not by app chrome.
- 🟡 Expert AI adds a second, chat-first IA; the shift creates a mode-splitting UX risk (search vs. ask) that WK manages by embedding source links to keep both loops wired to the same corpus.

## 6.5 Dark mode

⚪ Not publicly confirmed. 🟡 App Store screenshot set (as accessible in listing metadata) and absence of dark-mode marketing suggests dark mode is, at best, partial — a remarkable gap for a night-shift-heavy user base. **Copy? No — Ovexis should ship true clinical dark mode (low-blue, monitor-dimming) as table stakes.**

## 6.6 Trust signals (the strongest part of the UX)

| Signal | Detail | Conf. |
|---|---|---|
| Authorship transparency | Named authors + section editors + affiliations on every topic | 🟢 |
| Update recency | "Last updated" per topic/section; What's New stream | 🟢 |
| Evidence grammar | GRADE badges inline; numbered citations → references | 🟢 |
| Scale claims | "3M+ healthcare professionals"; "used in 190+ countries" | 🟢 (marketing claims) |
| Outcomes claim | "The only clinical decision support associated with improved patient outcomes" (Isaac–Jha study) repeated in store/App copy | 🟢 |
| AI transparency | Assumptions / Sources / Reasoning panels per answer | 🟢 |
| Conflict hygiene | Editorial policy commits to disclosure & no commercial bias | 🟢 |

🟡 **UX lesson:** UpToDate's trust architecture is *authorship + recency + grading + citation*, not seals and certifications. It works — clinicians describe it as "gold standard" with no marketing exposure. This is the single most copyable UX asset for Ovexis.

## 6.7 Microinteractions & animations

🟡 Scarce. The interface is interaction-austere: expandable sections, calculator modals, print/email actions. Expert AI introduces typing/streaming affordances. 🟡 Instagram-grade delight engineering is entirely absent — consistent with the org's belief that polish is not clinical value.

## 6.8 Forms

- 🟢 Store wizard: country→role→profession progressive disclosure (observed live); clean, low-friction segmentation.
- 🟡 Login: remember-username, SSO-first affordances, institutional "continue without signing in" — mature enterprise patterns.
- 🟡 Calculators are the heaviest interactive forms; 200+ of them validated and maintained — a form-engineering asset competitors underestimate.

## 6.9 Loading & performance

- 🟡 Web topic delivery is fast (static-ish content, CDN-cached — inference from content nature + global audience; ⚪ CDN vendor not verified).
- 🟢 Voluntary evidence: Lexidrug offline-mode exists *because* connectivity in hospitals is unreliable — the org understands clinical-network reality (pharmacy offline database).
- 🔴 Expert AI latency is a named engineering SLO in WK job posts — internal awareness that streaming latency is the new page-speed KPI.

## 6.10 Visual hierarchy & illustrations

- 🟢 Medical graphics/algorithms/videos are professionally illustrated, consistent in style, and *teaching-optimised* (used by clinicians at the bedside — confirmed across reviews).
- 🟡 Marketing-site visual language (blue-clinical palette, restrained iconography) matches WK brand system; the app inherits rather than leads.

## 6.11 Conversion optimisation

🟢 Mechanisms observed: role-based pricing wizard; free-trial substitutes for Lexidrug (one-month iOS trial / 14-day Play trial — notably, **no free trial for the main UpToDate app**); EzRenew; institutional "contact sales" gating at ≥20 seats; CME-funds compatibility (an invisible conversion lubricant — buyers don't spend their own money).
🟡 Conversion philosophy is procurement-era, not product-led: the cheapest persuasion unit is not a growth loop, it's a budget line ("CME funds").
🔴 The absence of any trial/freemium for the core product in 2026 — while ChatGPT-for-Clinicians and OpenEvidence are free — is the single clearest UX-era mismatch on record.

## 6.12 Friction audit (verified complaints, app-store + Reddit)

| Friction | Evidence | Conf. |
|---|---|---|
| Login/device-limit pain | Review corpus + Reddit: session juggling across devices; workarounds documented (share logins, re-auth every 90 days) | 🟢 |
| Price | Dominant complaint theme; institutional cancellations | 🟢 |
| Dated mobile UX | Reported orientation bugs, clunky zoom; rating 3.6★ vs Lexidrug 4.7★ | 🟢 |
| Notification/intent confusion post-AI | 🟡 Mode split (search vs ask) emerging | 🟡 |
| Institutional cancellation shock | Users stranded mid-career when trust/hospital drops license | 🟢 |

## 6.13 Mobile vs desktop

- 🟢 Mobile: iOS + Android apps; Expert AI in app (2026 packaging); offline for Lexidrug (but not for core UpToDate corpus — a hospital Wi-Fi pain point).
- 🟢 Desktop/EHR: the dominant surface — Epic-infobutton flows keep desktop/EHR primary in hospitals.
- 🟡 Usage shape by surface (inferred): desktop/EHR = acute 90-second lookups; mobile = on-the-go dose checks + reading; app = CME ledger opportunistic use.
- 🟡 **Strategic UX conclusion:** UpToDate's interface is a *viewport on an editorial database*. Everything consumer-grade (delight, personalisation, dark mode, offline, proactive) is subordinate to the corpus. For Ovexis, inverting that ratio — proactive UX on top of a continuously updated personal data layer — is differentiation the incumbent is culturally incapable of matching quickly.
