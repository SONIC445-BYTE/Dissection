I now have comprehensive, citation-rich data. Let me compile the full Daily Early-Diagnosis Brief on **Hepatocellular Carcinoma (HCC)** — selected as today's disease for its extraordinary combination of: fixable operational failures (63.7% receive zero surveillance), validated emerging biomarkers (GALAD, PIVKA-II), AI ultrasound breakthroughs, and a growing MASLD/NASH blind spot affecting hundreds of millions globally.

---

## Subject: Daily Early-Diagnosis Brief — Hepatocellular Carcinoma (HCC) — 2026-06-16

---

### 1) Snapshot (one line)

**Hepatocellular Carcinoma (HCC)** — why early diagnosis fails in practice: Over 63% of at-risk cirrhotic patients receive **zero guideline-recommended surveillance**, and the standard ultrasound + AFP screen misses ~45% of early tumors — particularly in the rapidly growing MASLD/NASH population who can develop HCC *before* cirrhosis even appears on records.

---

### 2) Why Early Diagnosis Fails (3–5 bullets)

- **Biological barrier:** HCC in MASLD/NASH patients develops in non-cirrhotic or minimally fibrotic livers, outside the current surveillance eligibility criteria; tumor shedding of ctDNA into peripheral blood is low at early stages (sub-centimeter lesions); and ~40% of HCC tumors are non-AFP-producing, creating a systematic biomarker blind spot.
- **Test limitation:** Ultrasound sensitivity for early-stage HCC is as low as **45%** in real-world settings, dropping further in obese patients due to poor acoustic windows and hepatic steatosis obscuring small nodules. AFP alone at a standard cutoff achieves only **41% sensitivity** 12 months before clinical diagnosis (vs. GALAD's 91%). TVUS is operator-dependent with no standardized quality threshold enforced in most hospital systems.
- **System failure (Surveillance adherence collapse):** A landmark multicenter cohort (Kramer et al., *JAMA Network Open*) of 629 HCC patients found **63.7% received NO surveillance** in the 36 months preceding diagnosis. Of failures: 82.4% were due to absent clinician orders or patient non-adherence; 17.6% due to unrecognized/undiagnosed cirrhosis. No automated registry-based recall system exists in most health systems to flag overdue surveillance patients.
- **Guideline gap:** AASLD surveillance guidelines still primarily target cirrhotic patients — leaving non-cirrhotic MASLD (a population of >1 billion globally) without a recommended surveillance pathway, despite evidence that MASLD-related HCC increasingly arises in non-cirrhotic livers.
- **Biomarker adoption lag:** The GALAD score (combining Gender, Age, AFP-L3, AFP, PIVKA-II) achieved Phase 3 validation in 2025 with 91% sensitivity / 85% specificity, yet is not yet integrated into routine clinical workflow or EHR order sets in most hospitals. Mayo Clinic Labs offers it as a panel (test #606585), but uptake is minimal outside academic centers.

---

### 3) Detection Window & Gap (concise)

| Milestone | Time / Marker |
|---|---|
| **Earliest detectable signal (research/ideal)** | ctDNA methylation patterns & GALAD score: **up to 12 months before** clinical diagnosis; sub-centimeter nodule on AI-enhanced ultrasound at ~0.5–1 cm |
| **Typical clinical detection** | Symptomatic or incidentally found at **2–5 cm** (BCLC B/C); often when portal hypertension or jaundice forces imaging |
| **Gap to close** | **12–18 months** of actionable lead time being wasted; 20% of patients diagnosed at BCLC C/D (advanced/terminal) — median survival 1–3 years vs. 10 years at BCLC 0/A |

**Practical impact:** Every month of diagnostic delay in HCC represents a stage migration that cuts curative treatment eligibility (resection, ablation, transplant) in half. The gap is not biological — it is operational and biomarker-adoption driven.

---

### 4) What's Being Used Today (Gold Standard + Emergent)

**Gold Standards:**
- **Semiannual liver ultrasound ± AFP** (AASLD/EASL guideline) — the de facto standard in most hospitals
- **CT/MRI with LI-RADS** — confirmatory imaging for positive screens; high specificity but expensive, not used as primary screen
- **Liver biopsy** — reserved for indeterminate LI-RADS 3–4 lesions

**Emerging Research / Tools:**
| Tool | Performance | Status |
|---|---|---|
| **GALAD Score** (Gender + Age + AFP-L3 + AFP + PIVKA-II) | AUC 0.91; 91% sensitivity, 85% specificity; detects HCC 12 months earlier than AFP alone | Phase 3 validated (Marsh et al., *Gastroenterology* 2025); available via Mayo Clinic Labs |
| **PIVKA-II / DCP alone** | Captures ~40% of AFP-negative tumors; higher positive rate than AFP pre-diagnosis | Clinically available; underutilized in US |
| **ctDNA Methylation Liquid Biopsy** | Up to 91% accuracy Stage I; FDA Breakthrough Device Designation granted | Pre-commercial; research phase |
| **AI-Enhanced Ultrasound (UniMatch + LivNet models)** | 95.6% sensitivity, 78.7% specificity; 54.5% reduction in radiologist workload | Multicenter validation (*npj Digital Medicine*, 2025); not yet FDA-cleared for HCC triage |
| **GAAD Score** (GALAD minus AFP-L3) | Comparable early-stage sensitivity to GALAD; simpler, cheaper | Validated; potentially easier to implement |

**Main Limitations:**
- GALAD requires AFP-L3 (a specialized assay not available in most hospital labs — requires send-out)
- AI ultrasound models are not yet FDA-cleared for autonomous triage
- ctDNA liquid biopsy: sensitivity drops below 50% for sub-1cm lesions; high cost (~$1,000–$2,000/test)
- PIVKA-II falsely elevated by warfarin/vitamin K antagonists — common in cirrhotic patients

---

### 5) Where Healthcare is Failing (Operational Insight)

**Screening point that drops the ball:**
The **hepatology/gastroenterology outpatient scheduling system** — specifically, the absence of an automated recall/registry mechanism. Unlike mammography or colonoscopy, HCC surveillance has no systematic population-level tracking. Patients fall off the radar after discharge, and no EHR system proactively flags a cirrhotic patient who is 6 months overdue for ultrasound. The ordering physician must manually remember to re-order — and 63.7% of the time, they don't.

**Bottleneck most fixable in 90 days:**
→ **EHR-based automated surveillance recall + GALAD/PIVKA-II reflex ordering protocol.** Any patient with a cirrhosis ICD-10 code (K74.x) who has not had an abdominal imaging order in >5 months should trigger an automated outreach (MyChart message + nurse phone call). Adding PIVKA-II to the existing AFP order as a reflex test requires only a lab order set change — zero new infrastructure.

**High-risk population missed:**
- **Non-cirrhotic MASLD patients** — ~25–30% of MASLD-HCC arises without advanced fibrosis; no surveillance guideline covers them
- **Patients with unrecognized cirrhosis** — 17.6% of surveillance failures; cirrhosis is underdiagnosed in primary care (FIB-4 score rarely calculated at PCP visits)
- **Underserved/uninsured populations** — transportation, financial barriers account for a disproportionate share of the 82.4% adherence failure; minority populations have higher MASLD burden and lower surveillance rates

---

### 6) 3 High-Leverage Solution Ideas (Practical, Ranked)

**🥇 Idea A — EHR Surveillance Registry + Automated Recall (30-day pilot, highest ROI)**

*How to run it:*
- Pull all patients with ICD-10 K74.x (cirrhosis), K76.0 (NAFLD), B18.x (chronic viral hepatitis) from the EHR
- Flag any who have not had abdominal ultrasound or CT in >5 months
- Trigger automated MyChart/SMS outreach + nurse navigator call within 48 hours
- Add PIVKA-II as a reflex test to all existing AFP liver surveillance orders (lab order set change — 1 meeting with lab director)

*Metrics to collect (30–90 days):*
- % of flagged patients who complete imaging within 30 days (target: >60% vs. current ~36%)
- New HCC diagnoses captured at BCLC 0/A vs. historical baseline
- False positive rate of PIVKA-II add-on (track unnecessary follow-up imaging)
- Cost per additional early-stage HCC detected

*Resource needs:* 1 informaticist (EHR build), 0.5 FTE nurse navigator, lab order set revision

---

**🥈 Idea B — GALAD Score Integration into Hepatology Workflow (60–90 day pilot)**

*How to run it:*
- Partner with Mayo Clinic Labs (or equivalent) to add GALAD panel as a standing order for all cirrhotic patients in hepatology clinic
- Build a simple GALAD score calculator into the EHR (Epic SmartForm or similar) using locally available AFP + PIVKA-II + age/sex — use GAAD variant if AFP-L3 send-out is too slow
- Define a risk-stratified response protocol: GALAD < −1.0 → continue semiannual US; GALAD −1.0 to 0 → add PIVKA-II q3mo; GALAD > 0 → expedited MRI within 2 weeks

*Resource checklist:*
- Lab contract with AFP-L3 assay capability (or use GAAD as interim)
- Hepatologist champion + tumor board buy-in
- Epic SmartForm build (2–4 weeks)
- IRB waiver for QI project (not research)

*Expected impact:* Based on Phase 3 data — shift 15–20% of currently missed early-stage HCC into the detectable window; reduce time-to-MRI confirmation for high GALAD scores

---

**🥉 Idea C — Non-Cirrhotic MASLD Surveillance Protocol + ctDNA Pilot (Research/Product, 90-day design)**

*Highest upside:*
The next frontier is the **non-cirrhotic MASLD population** — >1 billion people globally with no current surveillance recommendation. A risk-stratified protocol using FIB-4 score (calculable from routine CBC + LFTs) to identify MASLD patients with advanced fibrosis (FIB-4 >2.67) who should enter HCC surveillance even without confirmed cirrhosis — combined with annual ctDNA methylation liquid biopsy — could capture a massive missed population.

*Tests needed:*
- Prospective cohort: enroll MASLD patients with FIB-4 >1.3 at hepatology/endocrinology clinics
- Annual ctDNA methylation panel + GALAD score + ultrasound
- Primary endpoint: HCC incidence rate by FIB-4 tier; secondary: stage at detection

*Collaborators to approach:*
- NASH Clinical Research Network (NASH CRN) — existing multicenter infrastructure
- Grail (Galleri multi-cancer early detection) or Volition (epigenomics liquid biopsy) for ctDNA partnership
- AASLD Foundation for pilot grant ($50K–$200K range)

---

### 7) First-Principles Signal Hunt (What We Should Measure Earlier)

**Hidden signal candidate:**
**Serum PIVKA-II + AFP-L3 ratio trajectory** — not a single-point measurement, but a *velocity* metric. PIVKA-II begins rising 6–12 months before a tumor becomes ultrasonographically visible. Tracking the *rate of change* (delta PIVKA-II over two consecutive draws, 3 months apart) in high-risk cirrhotic patients may identify those on a pre-malignant trajectory before any lesion is detectable. This is analogous to PSA velocity in prostate cancer — underexplored in HCC.

**Secondary candidate:** Serum **Mac-2BP glycosylation isomer (M2BPGi)** — currently validated as a fibrosis staging marker — may serve as an upstream risk-stratifier to identify which MASLD patients are approaching the fibrosis threshold that confers HCC risk, enabling earlier enrollment into surveillance.

**Minimal sampling change needed:**
No new sample type required — peripheral venous blood. Add PIVKA-II to every AFP draw (one additional tube, same blood draw). For ctDNA: 10 mL EDTA tube, same venipuncture. Zero additional patient burden.

---

### 8) Strategic Value & Next Immediate Actions (CEO Lens)

**Public health impact:**
- ~900,000 new HCC cases globally per year; 3rd leading cause of cancer death worldwide (~830,000 deaths/year)
- 5-year survival: ~20% overall; **>70% if caught at BCLC 0/A** vs. **<5% at BCLC C/D**
- MASLD affects ~32% of the global population (~2.5 billion people) — a tidal wave of future HCC risk with no surveillance infrastructure
- US alone: ~40,000 new HCC cases/year; costs $3–5B annually in late-stage treatment; early detection would shift the majority to curative-intent therapy

**3 Immediate Actions for Ayan:**

| Timeline | Action |
|---|---|
| **Today** | Pull your institution's cirrhosis patient registry (ICD-10 K74.x) and calculate what % have had abdominal imaging in the past 6 months — this single audit will reveal the surveillance gap quantitatively and build the business case for Idea A |
| **7 days** | Contact Mayo Clinic Labs (test #606585) or your regional reference lab to get GALAD/PIVKA-II pricing and turnaround time; schedule a 30-min meeting with your hepatology lab director to discuss adding PIVKA-II as a reflex to AFP orders |
| **30 days** | Draft a QI protocol for EHR-based automated HCC surveillance recall (Idea A); identify your Epic/Cerner informaticist; define the 3-month pilot cohort (target: 200–500 cirrhotic patients); set baseline metrics for surveillance adherence rate and stage at HCC diagnosis |

---

### 9) One-Minute Mental Model

> *"HCC hides in plain sight inside a population we already know about — cirrhotic patients in our own EHR — but our system has no memory. The tumor grows for 12–18 months in a detectable window while the patient waits for a clinician to manually remember to order a scan. The single leverage point: give the EHR a memory and a voice — automate the recall, reflex the PIVKA-II, and the diagnostic window opens itself."*

**Search keywords / papers for immediate lookup:**
1. **"Marsh JW GALAD Phase 3 Gastroenterology 2025"** — the pivotal GALAD validation paper
2. **"Kramer JR JAMA Network Open HCC surveillance barriers multicenter"** — the 63.7% no-surveillance cohort study
3. **"AI-enhanced ultrasound UniMatch LivNet npj Digital Medicine 2025"** — the 54.5% workload reduction AI ultrasound study

---

### 10) Pattern Insight (Meta-Learning)

**Recurring diagnostic failure pattern confirmed:** *The "Known Population, Forgotten Patient" failure mode.*

This is the **second major pattern** emerging across these briefs — a failure that is distinct from the "no biomarker exists" problem. In HCC, we know *exactly* who is at risk (cirrhotic patients, their ICD codes are in every EHR), we have validated surveillance tools (ultrasound, AFP, and now GALAD), and yet **63.7% of patients receive zero surveillance**. The disease is not hiding — the *system* is not looking.

**Pattern generalization:** This same failure appears in:
- **Chronic Kidney Disease → AKI** (patients with CKD flagged in EHR but no automated creatinine trend alerts)
- **Atrial Fibrillation → Stroke** (paroxysmal AF known, anticoagulation not initiated)
- **HIV → AIDS** (patients lost to follow-up after initial diagnosis)

**The generalizable opportunity:** The highest-leverage intervention class across multiple diseases is not a new biomarker — it is **EHR-native, automated surveillance registry infrastructure with proactive recall**. This is a horizontal platform play: a disease-agnostic "surveillance gap closer" that maps known high-risk populations in EHR data, tracks protocol adherence, and triggers outreach. It would work for HCC, CKD, AF, and dozens of other conditions simultaneously.

**Breaking or reinforcing?** Reinforcing — and accelerating. As MASLD expands the at-risk population by orders of magnitude without triggering new guideline surveillance, the "known population, forgotten patient" gap will widen catastrophically unless systems-level recall infrastructure is built now.

---
*Brief prepared for Ayan Mukhopadhyay | June 16, 2026 | Sources: JAMA Network Open (Kramer et al.), Gastroenterology (Marsh et al. 2025), npj Digital Medicine (AI-US 2025), Frontiers in Microbiology, Mayo Clinic Labs, FDA Breakthrough Device Designation records, AASLD guidelines.*