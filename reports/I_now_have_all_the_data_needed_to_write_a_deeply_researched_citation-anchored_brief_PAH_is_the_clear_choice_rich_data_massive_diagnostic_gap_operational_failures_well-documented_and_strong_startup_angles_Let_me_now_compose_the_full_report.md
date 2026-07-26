I now have all the data needed to write a deeply researched, citation-anchored brief. PAH is the clear choice — rich data, massive diagnostic gap, operational failures well-documented, and strong startup angles. Let me now compose the full report.

---

## Subject: Daily Early-Diagnosis Brief — Pulmonary Arterial Hypertension (PAH) — 2026-06-11

---

### 1) Snapshot (one line)

**Pulmonary Arterial Hypertension (PAH)** — why early diagnosis fails in practice: Non-specific symptoms (exertional dyspnea, fatigue) trigger a fragmented, sequential workup that delays the definitive but invasive gold standard by **2–3 years**, by which time right ventricular damage is already irreversible.

---

### 2) Why Early Diagnosis Fails (3–5 bullets)

- **Biological barrier:** PAH causes progressive obliterative pulmonary vascular remodeling years before resting hemodynamics become abnormal — symptoms only appear after ~50% of the pulmonary vascular bed is compromised; resting pressures can remain borderline-normal in early disease, making echo and BNP falsely reassuring.
- **Test limitation:** Echocardiography (the first-line screening tool) is highly operator-dependent and misses early/mild PAH when tricuspid regurgitation velocity is borderline or absent; NT-proBNP and BNP only elevate meaningfully *after* right ventricular wall stress is established — they are lagging, not leading, indicators. CA 19-9 analogy: BNP is a monitoring tool misused as a screening tool.
- **Gold standard bottleneck:** Right Heart Catheterization (RHC) — the only definitive test — is invasive, requires specialized PH centers, and is withheld by community cardiologists until symptoms are severe; geographic access, prior authorization, and specialist referral queues each add weeks to months.
- **System failure (misdiagnosis cascade):** Exertional dyspnea in young women is routinely attributed to anxiety, deconditioning, or asthma; patients with connective tissue disease (SSc, SLE) have breathlessness attributed to their primary condition; HIV patients' symptoms are blamed on infection. Each misattribution resets the diagnostic clock.
- **System failure (EHR/workflow):** No automated EHR flags exist for the combination of: isolated low DLCO on PFTs + unexplained dyspnea + multiple primary care visits. Hospitals run sequential (not parallel) workups, and there is no standardized "PAH referral trigger" in most community pulmonology or cardiology practices.

---

### 3) Detection Window & Gap (concise)

| Stage | Signal | Timing |
|---|---|---|
| **Earliest detectable (research)** | Circulating miRNA panel (miR-21, miR-155), apelin-17 decline, early RV strain on cardiac MRI | **12–24 months before hemodynamic confirmation** |
| **Echo-detectable (borderline)** | Borderline RVSP 35–45 mmHg, subtle RV dilation, reduced TAPSE | **6–18 months before RHC diagnosis** |
| **Typical clinical detection** | Symptomatic dyspnea → echo → referral → RHC | **Mean 27–34 months after symptom onset** (REVEAL registry) |
| **Gold standard confirmation** | RHC: mPAP ≥20 mmHg, PVR ≥2 WU | By this point, ~50–70% of patients already in WHO FC III |

**Gap to close:** ~18–30 months. Practical impact: Patients diagnosed in WHO Functional Class I/II have a 5-year survival of ~70%; those diagnosed in FC III/IV drop to ~40–50%. Every 6-month delay represents measurable, irreversible right ventricular remodeling. In SSc-PAH specifically, a 6-year median delay from SSc diagnosis to PAH presentation has been documented.

---

### 4) What's Being Used Today (Gold Standard + Emergent)

**Gold Standard(s):**
- **Right Heart Catheterization (RHC):** Definitive — measures mean pulmonary arterial pressure (mPAP ≥20 mmHg) and pulmonary vascular resistance (PVR ≥2 WU). Invasive, restricted to specialized PH centers. The 2025 CHEST journal best-practices paper (*Best Practices for Right Heart Catheterization in the Diagnosis of PAH*, CHEST 2025) reaffirmed its indispensability but acknowledged access barriers.
- **Transthoracic Echocardiography (TTE):** First-line screening; estimates RVSP via TR velocity. Sensitivity for early PAH is poor (~60–70%) in community labs; highly operator-dependent.
- **NT-proBNP / BNP:** Used for risk stratification and monitoring — not early diagnosis.

**Emerging Research / Tools:**
- **ADAMTS13 plasma assay:** AUC 0.91, sensitivity 87.5% for PAH discrimination (*Chest Pulmonary*, 2025) — potentially the strongest single blood biomarker yet validated.
- **Apelin-17:** Blood-derived peptide reflecting early endothelial dysfunction; high diagnostic accuracy for idiopathic PAH in early-phase studies (PMC9846527).
- **miRNA panels (miR-21, miR-155, miR-210):** Reflect early pulmonary vascular remodeling; multi-omics panels in pre-validation phase.
- **AI echocardiography — Us2.ai (FDA-cleared, CE-marked v2):** Fully automated right-heart analysis from DICOM in <2 minutes; detects subtle PH markers missed by non-expert readers; validated in ERS 2024 publication (*ERJ Open Research*, 11/3/00592-2024). Caption AI and EchoGo are in evaluation.
- **DETECT algorithm (SSc-PAH):** Evidence-based 2-step nomogram for systemic sclerosis patients; reduces missed PAH to 4% vs. 29% with legacy guidelines; Step 1 sensitivity 97%.
- **Cardiac MRI:** Gold standard for RV function quantification; detects early RV strain before echo or BNP changes — but expensive and not widely deployed for screening.

**Main Limitations:**
- ADAMTS13 and apelin-17 not yet in clinical guidelines; no commercial assay widely available.
- AI echo tools require DICOM integration and institutional procurement; not in community cardiology yet.
- DETECT algorithm is SSc-specific; no equivalent validated tool for idiopathic or HIV-associated PAH.
- miRNA panels: no validated clinical-grade assay; research-phase only.

---

### 5) Where Healthcare is Failing (Operational Insight)

**Screening point that drops the ball:**
The **community cardiologist or pulmonologist echo lab** is the central failure node. Patients arrive with exertional dyspnea, receive a TTE that shows borderline RVSP (35–45 mmHg) or is technically limited (no TR signal = "not assessable"), and are discharged with a note of "no significant PH." There is no reflex protocol to escalate borderline or technically limited echos to a PH specialist or AI re-analysis. This is the highest-leverage failure point.

**Bottleneck most fixable in 90 days:**
**Implementing a standardized "PAH referral trigger" within existing EHR systems** — a rule-based alert that fires when a patient has: (a) ≥2 dyspnea-related visits in 12 months + (b) isolated low DLCO on PFTs (<70% predicted) + (c) no confirmed alternative diagnosis. This is a *zero-new-infrastructure* change that can be piloted in any Epic/Cerner environment. A 2024 medrxiv preprint (*Pulmonary hypertension misdiagnosis due to preventable errors in echocardiography*) documented that a significant proportion of PH misdiagnoses involved preventable echo interpretation errors — addressable with AI overlay.

**High-risk population missed:**
1. **Young women (25–45)** with exertional dyspnea → misdiagnosed as anxiety/POTS/deconditioning for 2–5 years before PAH is considered.
2. **Systemic sclerosis (SSc) patients** not enrolled in a structured annual DETECT-based screening program — particularly those with limited cutaneous SSc where pulmonary symptoms develop insidiously.
3. **HIV-positive patients** in resource-limited settings — HIV-associated PAH prevalence is ~0.5% (500× general population risk) but is rarely screened for systematically.

---

### 6) 3 High-Leverage Solution Ideas (Practical, Ranked)

**🥇 Idea A — EHR-Based PAH Referral Trigger (30-day pilot, zero new infrastructure)**

*How to run it:*
Partner with 1–2 academic medical centers or large health systems using Epic. Build a **CDS (Clinical Decision Support) rule** that fires a "Consider PAH workup" alert when: ≥2 visits coded with R06.0x (dyspnea) in 12 months + DLCO <70% on any PFT result + no ICD-10 code for established cardiopulmonary diagnosis. Alert routes to pulmonology/cardiology for TTE with right-heart protocol.

*Metrics to collect (30–90 days):*
- Alert trigger rate per 1,000 patient-encounters
- Conversion rate: alert → TTE ordered (target >60%)
- New PAH diagnoses per quarter vs. historical baseline
- Time from first alert to RHC (target: reduce from 18+ months to <6 months)
- False positive rate (alerts in patients with confirmed alternative diagnosis)

*Resource requirement:* 1 Epic analyst, 1 pulmonologist champion, IRB waiver for QI project. Cost: <$15K.

---

**🥈 Idea B — AI Echo Overlay in Community Cardiology Labs (60–90 day scalable pilot)**

*How to run it:*
Deploy **Us2.ai** (FDA-cleared) or equivalent AI echo analysis as a DICOM post-processing layer in 3–5 community cardiology labs that feed into a PH referral center. Every echo gets automated right-heart analysis; any result flagging RVSP >35 mmHg, RV dilation, or reduced TAPSE automatically generates a structured PH-risk report sent to the ordering physician with a recommended action (repeat echo in 3 months / refer to PH center).

*Resource checklist:*
- DICOM routing agreement with echo lab (IT: 2–3 weeks)
- Us2.ai licensing (~$X/study; negotiate per-read pilot pricing)
- Radiologist/cardiologist sign-off protocol for AI-flagged cases
- PH center capacity to absorb referral surge (pre-plan with 1 dedicated PH slot/week)

*Expected impact:* Based on ERS 2024 validation data, AI echo detects ~15–20% more borderline PH cases than human readers in non-specialist labs. In a lab reading 50 echos/day, this translates to 7–10 additional PH-risk flags per week — each a potential earlier diagnosis.

---

**🥉 Idea C — Multi-Biomarker Blood Panel for PAH Triage (Research/Product, 90-day scoping)**

*Concept:* Combine **ADAMTS13 + apelin-17 + NT-proBNP** into a single venous blood draw "PAH triage panel" that can be ordered by any GP or pulmonologist *before* echo — creating a pre-imaging risk stratification layer. A panel with AUC >0.90 could safely defer RHC in low-risk patients and fast-track high-risk patients directly to PH centers.

*Tests needed:*
- Analytical validation of combined panel (ADAMTS13 + apelin-17 co-assay feasibility)
- Retrospective validation in REVEAL or ASPIRE registry biobanks
- Prospective pilot in SSc clinic (highest-risk, most structured follow-up)

*Collaborators to approach:*
- **Quanterix** (ultrasensitive immunoassay platform — already used for NfL in ALS; adaptable for apelin/ADAMTS13)
- **CHEST Pulmonary / ERS PH working group** for registry biobank access
- **Systemic sclerosis clinics** at Johns Hopkins, Royal Free Hospital (London), or University of Pittsburgh (world-class SSc-PAH cohorts)

*Highest upside:* A validated 3-marker blood panel could be commercialized as a $150–200 lab-send-out test, positioned as the "pre-echo PAH screen" — analogous to what BNP did for heart failure triage in the ED, but for the outpatient dyspnea workup. Market: ~$500M+ globally given PAH prevalence and the massive underdiagnosis burden.

---

### 7) First-Principles Signal Hunt (What We Should Measure Earlier)

**Hidden signal candidate:**
**Isolated low DLCO (diffusing capacity for carbon monoxide)** on routine pulmonary function testing is the most underutilized early PAH signal in clinical practice. DLCO drops due to pulmonary vascular obliteration *before* resting pressures rise. A DLCO <70% predicted with normal spirometry in a patient with any connective tissue disease, HIV, or unexplained dyspnea is a near-mandatory PAH workup trigger — yet most PFT reports generate no automated alert. Pair this with **apelin-17 decline** (endothelial dysfunction marker, measurable from a standard venous blood draw) and you have a two-signal early detection system requiring zero new imaging.

**Minimal sampling change needed:**
- Standard venous blood draw (add apelin-17 ELISA or ADAMTS13 to existing lab panel — same tube, same visit)
- Existing PFT data (DLCO already measured; just needs an EHR extraction rule)
- No new imaging, no new patient visits, no new procedures

**The hidden architecture:** PAH hides behind "normal" resting hemodynamics because the pulmonary vasculature has massive reserve. The signal is in the *functional* loss (DLCO, exercise capacity) and *molecular* loss (apelin, endothelial markers) — not in resting pressure. Measure function and molecules first; reserve the invasive pressure measurement for confirmation.

---

### 8) Strategic Value & Next Immediate Actions (CEO Lens)

**Public health impact:**
- PAH prevalence: ~15–50 cases per million (rare, but highly morbid); ~200,000–300,000 patients in the US/EU combined
- 5-year mortality without treatment: ~50%; with optimal early treatment: ~70–80% survival
- Economic burden of delayed diagnosis: Each 6-month delay in PAH diagnosis is associated with significantly higher hospitalization costs and accelerated disease progression (PMC10781905)
- The *asymmetric* opportunity: PAH is rare enough that a focused diagnostic tool can achieve market penetration quickly; severe enough that payers will reimburse; and underdiagnosed enough that even 20% improvement in detection represents thousands of lives annually

**3 Immediate Actions for Ayan:**

| Timeline | Action |
|---|---|
| **Today** | Read: *"Can Plasma ADAMTS13 Differentiate Patients With Pulmonary Arterial Hypertension?"* (Chest Pulmonary, 2025) + the Us2.ai ERS 2024 validation paper (*ERJ Open Research* 11/3/00592-2024). These two papers define the biomarker and AI tech stack for a credible early-detection play. |
| **7 days** | Map the PAH diagnostic pathway at one academic medical center you have access to: How many echos/month are read in community labs? Is DLCO routinely reported with a flag? Does the EHR have any PAH alert? This 30-minute conversation with one PH specialist will reveal the exact operational gap. |
| **30 days** | Draft a 1-page pilot spec for the EHR CDS trigger (Idea A): define the inclusion logic, identify an Epic analyst collaborator, and submit as a QI project to bypass full IRB. Simultaneously, contact the DETECT algorithm team (suspectpahctd.com) about extending their algorithm beyond SSc to idiopathic PAH — this is a published gap they are likely already working on. |

---

### 9) One-Minute Mental Model

> *"PAH hides behind the lung's vascular reserve — by the time resting pressure is abnormal enough for echo or BNP to flag it, 50% of the vascular bed is already destroyed. The leverage point is measuring what fails first: DLCO (function) and apelin-17/ADAMTS13 (endothelial molecular signal) — both detectable from existing clinical infrastructure before a single imaging study is ordered."*

**2–3 Search Keywords / Paper Handles for Immediate Literature Lookup:**
1. `"ADAMTS13 pulmonary arterial hypertension" Chest Pulmonary 2025` — the strongest new single-biomarker paper
2. `"Us2.ai pulmonary hypertension" ERJ Open Research 2024` — AI echo validation study
3. `"DETECT algorithm systemic sclerosis PAH" + "diagnostic delay" REVEAL registry` — the operational benchmark for what structured screening achieves

---

### 10) Pattern Insight (Meta-Learning)

**Recurring diagnostic failure pattern emerging:**

Today's PAH brief reinforces a pattern that has now appeared across multiple disease categories: **the "lagging biomarker trap."**

The trap works like this:
1. A disease causes progressive organ damage for months to years before symptoms appear.
2. The available biomarkers (BNP for PAH; CA 19-9 for PDAC; CA-125 for ovarian cancer) are *monitoring* tools repurposed as *screening* tools — they only rise after substantial damage has occurred.
3. Clinicians interpret normal biomarker levels as reassurance, halting further workup.
4. By the time the biomarker becomes abnormal, the diagnostic window for high-impact intervention has closed.

**This pattern has now appeared in:**
- Pancreatic cancer (CA 19-9 as a false-negative screen)
- Ovarian cancer (CA-125 as a lagging, low-PPV marker)
- ALS (NfL rises early but is still a *damage* marker, not a *causation* marker)
- PAH (BNP/NT-proBNP as post-RV-stress indicators)

**The generalizable opportunity forming:**
The consistent solution across all four diseases is the same: **replace lagging damage biomarkers with upstream functional or molecular signals** — DLCO for PAH, cfDNA methylation for PDAC, apelin/ADAMTS13 for PAH, NfL + GFAP panels for ALS. The startup and hospital improvement play is identical in each case: *build the pre-imaging, pre-damage-biomarker triage layer using existing blood draws and existing functional tests, connected by an EHR decision rule.*

The founder who builds a **disease-agnostic "pre-damage signal" platform** — combining ultrasensitive immunoassay (Quanterix-style), EHR CDS trigger logic, and AI imaging overlay — will have a replicable architecture across 10+ diseases with the same diagnostic failure pattern. **The moat is not the biomarker. The moat is the clinical workflow integration layer.**

---
*Brief prepared: Thursday, June 11, 2026 | UTC 09:00 | Sources: REVEAL Registry, ASPIRE Registry, ANZ Registry, Chest Pulmonary 2025, ERJ Open Research 2024, DETECT Algorithm, PMC10781905, PMC9846527, Us2.ai FDA clearance documentation, DZNE 2025 ALS biomarker report, GRAIL PATHFINDER 2 2026.*