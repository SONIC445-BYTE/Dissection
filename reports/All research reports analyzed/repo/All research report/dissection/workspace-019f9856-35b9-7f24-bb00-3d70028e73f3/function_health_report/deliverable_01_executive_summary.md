# DELIVERABLE 1 — EXECUTIVE SUMMARY
## FUNCTION HEALTH COMPETITIVE INTELLIGENCE REPORT
*Prepared for Ovexis Board Strategy — 2026-07-25*

---

## 1.1 WHAT ARE THEY BUILDING?

### Confirmed Core Product 🟢
Function Health operates a **direct-to-consumer preventive health membership** priced at **$365/year** ($1/day), delivering:
- **160+ laboratory biomarkers** tested biannually (annual visit: ~100+ markers; mid-year visit: ~60+ markers)
- **2,000+ Quest Diagnostics / Getlabs draw locations** across the US
- **Clinician-reviewed results** with personalized action protocols
- **Advanced imaging add-ons** via acquired Ezra AI: 22-minute full-body MRI ($499) and CT scans
- **Supplement intelligence layer** via acquired SuppCo: TrustScore ratings, ISO 17025-based TESTED program
- **Medical Intelligence Lab (MI Lab)**: AI-powered unification of lab + imaging + wearables + medical records + global research

### Confirmed Technical Architecture 🟢
- **Frontend:** Web app (my.functionhealth.com) — no native mobile app mentioned in primary evidence
- **Backend:** Google Cloud Run (REST API v1, Firebase Authentication)
- **Lab Integration:** Quest Diagnostics (CLIA-certified) — results delivered in batches over ~2 weeks via `requisitionId` grouping
- **Data Model:** Biomarker definitions with dual-range system (Function "optimal" vs Quest reference); biological age calculations; BMI; personalized recommendations; clinician notes; pending schedules; health record uploads

---

## 1.2 WHY DOES IT EXIST?

### Market Gap Confirmed 🟢
The standard US annual physical measures **~26 biomarkers**. Function Health measures **160+ biomarker tests** spanning heart, hormones, thyroid, liver, kidneys, heavy metals, nutrients, inflammation, cancer signals, aging factors, autoimmunity, brain health, and more — for $365 vs. $15,000+ for equivalent comprehensive testing through traditional channels.

### Foundational Philosophy Confirmed 🟢
From press release (Nov 19, 2025):
> "Function’s mission: empower people to live 100 healthy years. That starts by giving you a more complete view of your body through 160+ lab tests, advanced imaging, and insights from top doctors."

From homepage FAQ:
> "We created Function with a single mission: empower you to live 100 healthy years."

---

## 1.3 THE CUSTOMER PROBLEMS

### Customer Problem (Functional) 🟢
- **Fragmented health data:** Patients have lab results scattered across doctors, hospitals, and insurance portals with no longitudinal tracking
- **Reactive medicine:** Standard care detects disease after symptoms emerge; patients want early signals before disease manifests
- **Limited biomarker depth:** Standard checkups miss hormones, heavy metals, advanced lipid profiles, cancer signals (Galleri), biological age, autoimmunity markers
- **No personalized action:** Traditional lab reports provide numbers without contextual interpretation or lifestyle protocols

### Emotional Problem 🟡
- **Fear of invisible decline:** Anxiety about aging, undiagnosed conditions, and preventable death
- **Desire for control:** Consumers want to "own their health" rather than delegate to a slow, bureaucratic medical system
- **Status and identity:** Being a "Function member" aligns with biohacker culture, longevity optimization, and health-conscious identity (reinforced by celebrity endorsements: Andrew Huberman, Jay Shetty, Mark Hyman, etc.)
- **FOMO and urgency:** Marketing creates urgency through limited-time pricing ($499 → $365) and scarcity messaging ("What could cost $15,000 is $365")

### Operational Problem 🟡
- **Scheduling friction:** Users report scheduling errors, inability to reschedule through app, manual customer service required
- **Batch result delivery:** Results arrive in batches over 2+ weeks rather than a single report; no indicator of which results are new
- **Upsell fatigue:** Continuous promotion of add-ons ($269 for retest of missing biomarkers; $499 MRI; extended panels)
- **State regulatory complexity:** NY/NJ users face additional fees and must travel to other states for testing
- **Clinician notes perceived as AI-generated:** Users report notes feel "impersonal," "scripted," and less valuable than ChatGPT/Gemini analysis of the same data

---

## 1.4 WHO IS THE CUSTOMER?

### Confirmed Primary Persona 🟢
- **Age:** 30-55 (longevity-focused, health-optimized millennials/gen X)
- **Income:** $100K+ (able to afford $365/year out of pocket, plus optional $499 MRI, $3100+ extended panels)
- **Location:** US-focused (state-level scheduling required)
- **Behavior:** Health-conscious, podcast listeners (Huberman, Hyman, Shetty audiences), supplement users (post-SuppCo acquisition), wearable users (potential integration with wearables mentioned in MI Lab vision)
- **Psychographics:** Proactive, data-driven, skeptical of traditional medicine, willing to self-pay for deeper insight

### Confirmed Secondary Personas 🟢
- **Biohackers / Quantified Self practitioners:** Track biomarkers over time, compare to reference ranges, seek optimization
- **Pre-disease / high-risk individuals:** Family history of cancer, diabetes, heart disease; want early detection
- **Women’s health focus:** Dedicated women’s health medical director (Dr. Tiffany Lester); specific hormone panels (AMH, SHBG, estradiol, progesterone, FSH, LH, prolactin)
- **Athletes / High Performers:** NBPA exclusive biomarker partner for active/retired NBA players (per Sacra source)

### Confirmed Non-Customer 🟢
- **Insurance-dependent patients:** Function explicitly states "No insurance needed" — this is a feature for some but excludes those who rely on insurance-covered preventive care
- **Low-income / price-sensitive:** $365/year + optional add-ons exceeds budget healthcare options; no sliding scale or subsidy program mentioned
- **Clinically acute patients:** Function does not treat acute conditions, provide emergency care, or manage chronic disease actively (it detects and recommends action, not treatment)
- **International users:** US-only currently; no global expansion documented
- **Elderly / less tech-savvy users:** Digital-first experience (app-based results, online scheduling, AI-generated notes) creates accessibility barriers

---

## 1.5 MARKET CATEGORY ANALYSIS

### Category Created 🟢
**Consumer Preventive Intelligence** — a hybrid category combining:
- Direct-to-consumer laboratory testing (Everlywell, LetsGetChecked model)
- Longevity / biohacking medicine (prenatal-like depth for adults)
- AI-powered health interpretation (ChatGPT-like health coaching + clinician oversight)
- Advanced imaging access (Ezra MRI model)
- Supplement intelligence (SuppCo model)

This is NOT traditional diagnostics (Quest, LabCorp serve providers) NOR traditional telemedicine (Teladoc serves acute needs) NOR wellness apps (Whoop serves athletes). Function creates **"Preventive Intelligence"** — continuous, deep, consumer-controlled health monitoring with AI interpretation.

### Category Being Replaced 🟡
- **Annual physical / primary care preventive visit:** Function positions itself as superior to "standard checkup" (26 biomarkers vs 160+)
- **Concierge medicine:** Offers similar depth ($15K+ concierge practices) at 1/40th the price
- **Fragmented specialist visits:** Consolidates cardiology, endocrinology, oncology screening, nutrition, and aging medicine into one platform

---

## 1.6 JOBS-TO-BE-DONE ANALYSIS

### Confirmed Primary Jobs 🟢
1. **Detect invisible disease before symptoms appear:** Cancer signals (Galleri), autoimmunity, hormone imbalances, metabolic dysfunction
2. **Establish longitudinal health baseline:** Track 160+ biomarkers over years to spot trends, not just point-in-time abnormalities
3. **Translate complex data into action:** Protocols translate lab numbers into food/supplement/exercise recommendations
4. **Own health data independently:** Upload past results, download reports, share with any provider — data portability
5. **Reduce anxiety through information:** Understanding body reduces fear of unknown; AI chat provides 24/7 explanation

### Inferred Secondary Jobs 🟡
6. **Social signaling:** Membership aligns with longevity culture, influencer endorsements, and biohacker identity
7. **Supplement optimization:** Post-SuppCo acquisition, members can link biomarker data to evidence-based supplement choices
8. **Family health intelligence:** Users share results with family members; some may use for family planning (fertility markers: AMH, hormones)

---

## 1.7 VALUE PROPOSITION

### Confirmed Value Proposition 🟢
> "Your health shouldn't depend on insurance. $1/day for 160+ lab tests, clinician-reviewed insights, personalized protocols, advanced imaging access, supplement intelligence, and a continuously learning AI health system — tracked for life."

### Value Components (Evidence-Based):
- **Depth:** 160+ biomarkers (6x standard physical)
- **Frequency:** 2x/year testing (vs 1x/year standard)
- **Access:** 2,000+ locations + concierge blood draws (select areas)
- **Interpretation:** Clinician-reviewed results + AI protocols + private AI chat
- **Longevity:** Biological age tracking, aging biomarkers (DHEA-S, IGF-1, SHBG, homocysteine, vitamin D)
- **Prevention:** Early cancer signals, heart risk beyond cholesterol (ApoB, Lp(a), LDL small, hs-CRP), heavy metals (lead, mercury), mold toxicity
- **Integration:** Lab + imaging + supplement intelligence + health record uploads
- **Transparency:** No insurance, no hidden fees (though upsells exist for add-ons)

---

## 1.8 CORE PHILOSOPHY

### Confirmed Principles 🟢
1. **Prevention > Reaction:** "Most testing starts after a problem. Function tracks your data over time to reveal patterns and early signs unique to you."
2. **Depth > Convenience:** 160+ biomarkers with no shortcuts; includes markers standard medicine ignores (lead, mercury, mold, biological age)
3. **Consumer Sovereignty:** "It's time you own your health." Data is portable, transparent, and user-controlled.
4. **Medical Intelligence > Artificial Intelligence:** "Not AI replacing doctors; it's clinical expertise amplified by intelligent systems that never stop learning."
5. **Longevity as Mission:** "Empower everyone to live 100 healthy years." Not just health optimization, but lifespan extension.

---

*Evidence sources: Homepage, How It Works, What We Test, Press Release (Nov 19, 2025), FAQ, User Reviews (Reddit), Reverse-Engineered API Documentation.*
