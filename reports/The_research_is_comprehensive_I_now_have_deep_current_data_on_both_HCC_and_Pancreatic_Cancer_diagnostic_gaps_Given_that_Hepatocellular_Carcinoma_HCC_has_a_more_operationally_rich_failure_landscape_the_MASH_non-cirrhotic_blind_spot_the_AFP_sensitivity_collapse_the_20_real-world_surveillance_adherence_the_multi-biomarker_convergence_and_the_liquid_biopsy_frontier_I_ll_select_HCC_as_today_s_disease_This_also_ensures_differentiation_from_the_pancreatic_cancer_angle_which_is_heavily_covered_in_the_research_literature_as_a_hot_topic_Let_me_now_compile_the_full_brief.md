The research is comprehensive. I now have deep, current data on both HCC and Pancreatic Cancer diagnostic gaps. Given that **Hepatocellular Carcinoma (HCC)** has a more operationally rich failure landscape — the MASH/non-cirrhotic blind spot, the AFP sensitivity collapse, the 20% real-world surveillance adherence, the multi-biomarker convergence, and the liquid biopsy frontier — I'll select HCC as today's disease. This also ensures differentiation from the pancreatic cancer angle (which is heavily covered in the research literature as a "hot" topic). Let me now compile the full brief.

---

## Subject: Daily Early-Diagnosis Brief — Hepatocellular Carcinoma (HCC / Primary Liver Cancer) — 2026-06-23

---

### 1) Snapshot (one line)

**Hepatocellular Carcinoma (HCC)** — why early diagnosis fails in practice: **surveillance programs reach only ~20% of eligible at-risk patients, AFP biomarker misses >50% of early tumors, and a rapidly expanding MASH/non-cirrhotic HCC population falls entirely outside current screening guidelines.**

---

### 2) Why Early Diagnosis Fails (3–5 bullets)

- **Biological barrier:** HCC develops silently over years of hepatic fibrosis/cirrhosis with no specific early symptoms; tumors <2 cm are radiologically occult on standard ultrasound, especially in obese/MASH patients with poor acoustic windows. Up to 20% of HCC tumors are AFP-non-secreting even at large sizes.
- **Test limitation:** AFP at the standard 20 ng/mL cutoff has only **49–71% sensitivity** for early HCC (<5 cm); >50% of patients at diagnosis have AFP below that threshold. Ultrasound alone has ~47% sensitivity for early-stage HCC in real-world (non-trial) settings — far below its theoretical performance.
- **Biomarker gap in MASH/non-cirrhotic HCC:** ~15–20% of MASH-related HCC arises in **non-cirrhotic livers** — a population entirely excluded from AASLD/EASL surveillance guidelines. These patients have no entry point into any screening program.
- **System failure (surveillance dropout):** Real-world adherence to biannual ultrasound + AFP is roughly **20%** in eligible cirrhotic populations. Reasons: unrecognized cirrhosis (patients never enrolled), fragmented care (primary care ↔ hepatology handoff fails), patient burden of 6-month imaging cycles, and no automated recall systems in most EHRs.
- **Staging-at-presentation:** Because of the above, **>60% of HCC cases are diagnosed at intermediate or advanced stage (BCLC B/C)**, where curative options (resection, transplant, ablation) are no longer applicable. Five-year survival at late stage: <20%. At Stage I: ~70%.

---

### 3) Detection Window & Gap (concise)

| Milestone | Time / Marker |
|---|---|
| **Earliest detectable signal (research/ideal)** | ctDNA methylation signatures / GALAD score elevation: **12–24 months before radiologic visibility** |
| **Earliest detectable on ultrasound (ideal conditions)** | Nodule ≥1 cm in a compliant cirrhotic patient on 6-month schedule |
| **Typical real-world clinical detection** | Symptomatic presentation (pain, jaundice, weight loss) or incidental imaging finding — **BCLC B/C, tumor >3–5 cm** |
| **Diagnostic gap to close** | **18–36 months** of missed window; translating this gap into curative-range staging could shift 5-year survival from ~18% (current population average) toward 50%+ |

**Practical impact of closing the gap:** If even 30% more HCC cases were caught at BCLC 0/A, an estimated **~40,000 additional lives/year** (globally) would enter curative-intent treatment pathways.

---

### 4) What's Being Used Today (Gold Standard + Emergent)

**Gold Standards:**
- **Biannual liver ultrasound ± serum AFP** — recommended by AASLD/EASL for all cirrhotic patients and HBV carriers; sensitivity ~47% (real-world) vs. 63% (trial setting) for early HCC
- **CT/MRI with LI-RADS criteria** — definitive non-invasive diagnosis for lesions ≥1 cm in cirrhotic liver; high specificity but used reactively, not as primary screen
- **Liver biopsy** — gold standard for non-cirrhotic or atypical lesions; invasive, sampling error risk

**Emerging Research / Tools (2024–2026):**
| Tool | Mechanism | Performance |
|---|---|---|
| **GALAD Score** | Gender + Age + AFP-L3 + AFP + DCP (PIVKA-II) composite | AUC 0.89–0.93 for early HCC; outperforms AFP alone by wide margin |
| **AALP Model** (AFP + AFP-L3 + PIVKA-II) | Triple biomarker panel | 81% sensitivity / 95% specificity |
| **HelioLiver Dx** (Helio Health) | Multi-analyte blood test (protein + glycan) | More sensitive than US+AFP for early-stage; EASL 2024 data |
| **EvoLiver** (Mursla Bio) | Extracellular vesicle liquid biopsy | FDA Breakthrough Device designation (2024/2025); early cirrhosis HCC detection |
| **ctDNA methylation panels** (EarlyDx, AASLD 2025) | Tissue-of-origin methylation in cfDNA | Outperforms ultrasound+AFP at AASLD 2025; pre-radiologic signal |
| **AI-enhanced ultrasound** (deep learning) | Focal liver lesion detection & LI-RADS classification | Reduces operator-dependency; improves sensitivity in obese patients (Frontiers 2025, Nature npj 2025) |
| **LI-RADS US Surveillance v2024** | Updated ACR standardized reporting framework | Improved early HCC detection vs. prior versions |

**Main Limitations:** GALAD/AALP not yet reimbursed in most health systems. HelioLiver/EvoLiver lack large prospective RCT validation. ctDNA sensitivity at Stage 0 remains ~60–70%. AI ultrasound requires curated training data across diverse body habitus populations.

---

### 5) Where Healthcare Is Failing (Operational Insight)

**Screening point that drops the ball:**
The **primary care → hepatology transition** is the single biggest failure point. Most cirrhosis is diagnosed (or missed) in primary care. GPs rarely initiate or maintain HCC surveillance — they refer to hepatology, but only ~40–50% of cirrhotic patients are ever seen by a hepatologist. Of those, fewer than half are enrolled in active surveillance. The **EHR does not trigger automatic recall** — surveillance is entirely dependent on individual provider memory or patient self-advocacy.

**Bottleneck most fixable in 90 days:**
→ **Automated EHR-based surveillance recall + reflex PIVKA-II/AFP-L3 add-on at the time of AFP draw.** Most hospital labs already have PIVKA-II available (or can enable it via send-out). Adding it as a reflex test when AFP is ordered for a cirrhotic patient costs ~$40–80 and requires only a protocol change — no new infrastructure.

**High-risk population missed:**
- **Non-cirrhotic MASH/NAFLD patients** — ~15–20% of MASH-HCC arises without cirrhosis; no guideline-recommended screening exists; these patients present at late stage almost universally
- **Underserved/rural cirrhotic patients** — no access to 6-month ultrasound cycles; no hepatologist within reasonable distance
- **HBV carriers in immigrant/diaspora communities** — often undiagnosed, unlinked to care, and outside surveillance systems entirely

---

### 6) 3 High-Leverage Solution Ideas (Practical, Ranked)

---

**🅐 [Idea A — Quick Pilotable | 30–60 days] EHR-Triggered Surveillance Recall + Reflex Biomarker Protocol**

**What:** Configure EHR (Epic/Cerner) to: (1) flag all patients with ICD-10 codes for cirrhosis/chronic liver disease who have NOT had an ultrasound in >7 months; (2) generate an automated outreach (SMS/patient portal) + provider alert; (3) add PIVKA-II as a reflex test whenever AFP is ordered in a cirrhotic patient.

**How to run the pilot (30–60 days):**
- Site: Single hepatology clinic or GI practice with ≥200 active cirrhotic patients
- Week 1–2: IT build (Epic SmartList + BPA rule); lab contract for PIVKA-II reflex
- Week 3–8: Run program; track recall response rate
- **Metrics to collect:**
  - % of overdue patients successfully recalled (target: >40%)
  - % of AFP orders with PIVKA-II reflex triggered
  - New HCC detections vs. prior 6-month baseline
  - BCLC stage at detection (primary outcome: shift toward BCLC 0/A)
  - Cost per additional early-stage HCC detected

**Resources needed:** EHR analyst (40 hrs), lab director approval, patient outreach coordinator. Cost: ~$5,000–15,000 setup. **Expected impact:** 2–3x improvement in surveillance completion rates (literature benchmark from similar recall programs).

---

**🅑 [Idea B — Scalable Tech/Workflow | 60–90 days] AI-Assisted Ultrasound Read + Standardized LI-RADS v2024 Reporting**

**What:** Deploy an AI-assisted focal liver lesion detection tool (e.g., integrated with existing ultrasound machines or PACS) and mandate LI-RADS US Surveillance v2024 structured reporting for all liver surveillance ultrasounds. Pair with a radiologist micro-training module (1-hour CME) on LI-RADS v2024 changes.

**Resource checklist:**
- [ ] AI vendor evaluation (GE HealthCare, Siemens, or research-grade tools from Nature npj 2025 paper)
- [ ] PACS integration or standalone workstation
- [ ] Radiology dept. buy-in + structured report template deployment
- [ ] Baseline audit: current % of liver US reports using LI-RADS structured format (likely <30% at most community hospitals)

**Expected impact:** Studies show AI-assisted ultrasound improves sensitivity for sub-2cm lesions by 15–25% over unassisted reads; LI-RADS standardization reduces "indeterminate" report rates, cutting unnecessary follow-up delays. In a 500-patient cohort, expect 3–8 additional early-stage HCCs detected per year.

---

**🅒 [Idea C — Research/Product | Highest Upside] MASH/Non-Cirrhotic HCC Liquid Biopsy Screening Cohort Study**

**What:** Design a prospective observational cohort study enrolling non-cirrhotic MASH patients (FIB-4 >1.3, no established cirrhosis) with serial ctDNA methylation + GALAD score measurements every 6 months. Primary endpoint: time-to-HCC detection vs. historical comparator (symptomatic presentation). Secondary: define a biomarker threshold that triggers cross-sectional MRI.

**Why this is the highest upside:** Non-cirrhotic MASH-HCC is the fastest-growing HCC subtype globally, entirely outside current guidelines, and has **zero validated screening strategy**. The first prospective biomarker dataset in this population would be landmark.

**Tests needed:**
- ctDNA methylation assay (EarlyDx platform or GRAIL Galleri as comparator)
- GALAD score (AFP + AFP-L3 + PIVKA-II + age + sex) — quarterly
- Liver elastography (FibroScan) at enrollment + annually
- Abdominal MRI at 12 months or on biomarker trigger

**Collaborators to approach:**
- NASH/MASH clinical networks: NASH CRN, TARGET-NASH registry
- Industry: Mursla Bio (EvoLiver), Helio Health (HelioLiver Dx), EarlyDx
- Academic hepatology centers with large MASH cohorts (UCSF, Mayo, Toronto General)

**Pilot size:** 300–500 patients, 2-year follow-up minimum. Grant pathway: NCI EDRN (Early Detection Research Network) or PCORI.

---

### 7) First-Principles Signal Hunt (What We Should Measure Earlier)

**Hidden signal candidate:**
**Circulating extracellular vesicle (EV) cargo + cfDNA 5-hydroxymethylcytosine (5hmC) tissue-of-origin patterns.** EVs released by pre-malignant hepatocytes carry surface proteins (GPC3, EpCAM fragments) and miRNA signatures that precede AFP elevation by months. ClearNote-style 5hmC profiling of cfDNA identifies liver-of-origin signal before a radiologically visible mass forms. Combined with PIVKA-II (a direct marker of hepatocyte metabolic dysfunction preceding malignant transformation), this tri-signal panel may detect HCC 12–18 months before current methods.

**Minimal sampling change needed:**
**Standard EDTA blood draw (10 mL)** — no special collection tube beyond what's used for CBC. Split-tube protocol: one aliquot for cell-free DNA extraction (5hmC/methylation), one for PIVKA-II/AFP-L3 ELISA. This is entirely compatible with existing phlebotomy workflows. **No change in patient-facing procedure.**

**Additional proxy signal worth exploring:** Gut microbiome dysbiosis signatures (fecal) — specific microbial shifts (↑*Bacteroides*, ↓*Lactobacillus*) precede HCC in cirrhotic patients and are detectable 6–12 months before tumor emergence in small cohort studies. Stool-based surveillance adjunct is non-invasive and scalable.

---

### 8) Strategic Value & Next Immediate Actions (CEO Lens)

**Public Health Impact:**
- **~900,000 new HCC cases/year globally** (2022 GLOBOCAN); 5th most common cancer, **2nd leading cause of cancer death worldwide**
- US: ~42,000 new cases/year; median survival without curative treatment: **6–20 months**
- **Economic burden:** Average cost of late-stage HCC management (sorafenib/atezolizumab + supportive care) = $80,000–$150,000/patient vs. ~$15,000–$30,000 for curative ablation/resection at early stage
- **Addressable diagnostic gap:** If real-world surveillance adherence moved from 20% → 50%, and biomarker panels replaced AFP-alone, conservative modeling suggests **15,000–25,000 additional early-stage diagnoses/year in the US alone**

---

**3 Immediate Actions for Ayan:**

| Timeline | Action |
|---|---|
| **Today** | Pull the 2025 PMC review *"Current and new strategies for hepatocellular carcinoma surveillance"* (PMC12145176) — this is the most current synthesis of GALAD, HelioLiver, ctDNA, and AI-US in one paper. Read the GALAD score validation section specifically. |
| **7 Days** | Map the HCC surveillance workflow at one target hospital: audit how many ICD-10 K74.x (cirrhosis) patients had a liver ultrasound in the past 12 months vs. how many were due. This single query (ask the informatics/EHR team) will reveal the true surveillance gap at your institution and is the foundation for Idea A pilot design. |
| **30 Days** | Draft a one-page protocol for the EHR recall + reflex PIVKA-II pilot (Idea A). Identify: (1) the hepatology attending who will champion it, (2) the lab director who can enable PIVKA-II reflex ordering, (3) the EHR analyst for the BPA rule. Submit as a QI (Quality Improvement) project — this bypasses full IRB and can launch in 60 days. Simultaneously, contact Helio Health or Mursla Bio for a site collaboration conversation on Idea C. |

---

### 9) One-Minute Mental Model

> *"HCC hides inside a disease (cirrhosis) that is itself underdiagnosed — so the screening program for the cancer never even starts; and when it does start, it uses a biomarker (AFP) that the tumor has already learned to evade in half of cases. The single leverage point: intercept the patient at the cirrhosis diagnosis moment, enroll them automatically into surveillance via EHR, and replace AFP-alone with a multi-analyte panel that the tumor cannot fully escape."*

**2–3 search keywords / paper names for immediate literature lookup:**
1. **"GALAD score hepatocellular carcinoma early detection validation 2024"** — search PMC/PubMed
2. **PMC12145176** — *"Current and new strategies for hepatocellular carcinoma surveillance"* (2025 review)
3. **"EvoLiver extracellular vesicle HCC FDA Breakthrough Device"** — Targeted Oncology / Mursla Bio press release

---

### 10) Pattern Insight (Meta-Learning)

**Recurring diagnostic failure pattern identified:**

Today's HCC brief reinforces a **"layered invisibility" pattern** that is emerging across multiple diseases in this series:

> **Layer 1 — The upstream disease is underdiagnosed** (cirrhosis, just as pre-diabetes precedes pancreatic cancer risk, or MGUS precedes myeloma). The cancer screening program is built on top of a population that was never properly identified.
>
> **Layer 2 — The biomarker used is a late-stage artifact, not an early signal** (AFP rises when the tumor is already large enough to bleed into the portal system; CA 19-9 in pancreatic cancer; PSA in prostate). These markers were validated in symptomatic/late-stage cohorts and then reverse-applied to early screening — a fundamental methodological error.
>
> **Layer 3 — The surveillance infrastructure exists on paper but collapses in execution** (20% real-world adherence in HCC; ~30% colonoscopy follow-up adherence post-polyp; ~40% mammography adherence in underserved populations). The protocol is correct; the operational system to deliver it is broken.

**Is today's disease reinforcing or breaking the pattern?**
**Strongly reinforcing.** HCC is the clearest example of all three layers stacking simultaneously.

**Generalizable opportunity forming across diseases:**
The cross-disease opportunity is not in discovering new biomarkers — it is in **building the operational infrastructure to actually deliver existing and emerging tests to the right patients at the right time.** The highest-ROI intervention in early cancer detection right now is not a new assay — it is an **EHR-native, automated, risk-stratified patient identification and recall engine** that works across HCC, colorectal, lung, and pancreatic cancer simultaneously. This is a platform play: one infrastructure product that solves the "Layer 3" failure for every cancer with an established screening protocol. The startup opportunity here is not a diagnostic device — it is a **clinical operations platform for surveillance program management**, deeply integrated with EHR data, lab ordering, and patient outreach.

---

*Brief compiled: 2026-06-23 | Sources: PMC12145176, PMC12227495, PMC12846323, CGH Journal (S1542-3565), Targeted Oncology (EvoLiver), AASLD 2025 (EarlyDx), Nature npj Digital Medicine 2025, LI-RADS US v2024 (ACR), Gut BMJ 2026 (AI pancreatic cancer — cross-reference), PRECEDE Consortium, ClearNote Health Avantect press release Feb 2026.*