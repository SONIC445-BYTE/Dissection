The research is comprehensive and rich. Now I have everything needed to produce today's definitive Early-Diagnosis Brief on **Pancreatic Ductal Adenocarcinoma (PDAC)**. This is the strongest candidate — it has the most asymmetric diagnostic gap, the most actionable 2025-2026 data, and high startup + hospital improvement potential. Let me compile the full report.

---

## Subject: Daily Early-Diagnosis Brief — Pancreatic Ductal Adenocarcinoma (PDAC) — 2026-07-06

---

### 1) 🔍 Snapshot (one line)

**Pancreatic Ductal Adenocarcinoma (PDAC)** — early diagnosis fails in practice because the tumor is biologically silent for 1–3 years before symptoms emerge, the only approved biomarker (CA 19-9) is useless for screening, and no population-level surveillance infrastructure exists outside of a handful of tertiary centers.

---

### 2) ❌ Why Early Diagnosis Fails (3–5 bullets)

- **Biological barrier:** PDAC is anatomically hidden in the retroperitoneum, grows without a lumen to obstruct or bleed into, and sheds negligible ctDNA into circulation at Stage I–II (~40–65% sensitivity on liquid biopsy alone). The tumor is physically present on CT scans **16–36 months** before it triggers symptoms — but those early radiomic signatures are invisible to the unaided human eye.

- **Test limitation:** CA 19-9 — the *only* FDA-cleared biomarker — is approved solely for *monitoring*, not screening. It is falsely normal in early-stage disease, elevated in benign biliary/inflammatory conditions, and biologically unproducible in 3–7% of the population (Lewis antigen-negative). No single-biomarker blood test currently clears the sensitivity + specificity bar for population screening.

- **System failure — surveillance enrollment:** High-risk surveillance programs (CAPS, PRECEDE Consortium) demonstrably improve survival (median 9.8 years when enrolled vs. ~12 months for unmonitored Stage IV), yet they are confined almost entirely to major academic medical centers. Community physicians and regional hospitals lack the referral pathways, genetic testing integration, and EUS capacity to enroll the eligible high-risk population.

- **System failure — new-onset diabetes (NOD) as a missed signal:** Individuals aged ≥50 presenting with new-onset diabetes have a **~5× elevated risk** of PDAC within 3 years. This signal typically precedes clinical cancer diagnosis by **8–36 months** — a golden window. Yet primary care physicians almost universally treat NOD as a metabolic disease, not an oncologic alarm. The ENDPAC scoring model (validated, trial-active at NCT04662879) is not embedded in any major EHR at scale.

- **System failure — radiology blind spots:** >36% of patients with PDAC had evidence of the cancer on a prior CT/MRI scan that was missed or dismissed. Staging via standard imaging is inaccurate in up to **80%** of early cases (Cedars-Sinai). Radiologists have no AI-assist deployed routinely in PACS to flag these isodense, sub-centimeter lesions.

---

### 3) ⏱️ Detection Window & Gap (concise)

| Parameter | Data |
|---|---|
| **Earliest detectable signal (research/ideal)** | Radiomic changes on CT: 16–36 months pre-diagnosis (Mayo REDMOD AI, *Gut* 2026). Exosome microRNA + CA 19-9 panel: Stage I/II sensitivity 97% (AACR 2024). New-onset diabetes: 8–36 months pre-diagnosis. |
| **Typical clinical detection** | Stage III/IV in >80% of patients; median diagnosis ~12–18 months after first nonspecific symptom |
| **Gap to close** | **16–36 months of actionable biological signal that goes undetected.** If caught at Stage I: 44% 5-year survival. If caught at Stage IV: 3.2%. This gap is the difference between life and death for ~60,000 Americans diagnosed annually. |

---

### 4) 🧪 What's Being Used Today (Gold Standard + Emergent)

**Gold Standards:**
- **Endoscopic Ultrasound (EUS):** Sensitivity 89–94% for small tumors in high-risk individuals. Contrast-enhanced EUS (CE-EUS): 84% sensitivity, 78% specificity. Operator-dependent, invasive, not scalable for population screening.
- **CT/MRI abdomen:** Standard first-line imaging, but misses >36% of early lesions. Staging accuracy for early PDAC: ~20%.
- **CA 19-9:** Monitoring only. Sensitivity 68–93%, specificity 76–100% — too variable for screening. Useless in Lewis antigen-negative patients.

**Emerging Research / Tools:**
- **Mayo Clinic REDMOD AI** (*Gut*, April 2026): Radiomics-based model applied to routine abdominal CT — identifies 73% of pre-diagnostic cancers at a median of 16 months (up to 3 years) before clinical diagnosis. Deployable in existing PACS. ⭐ *Highest near-term clinical leverage.*
- **Exosome-based liquid biopsy (8-microRNA panel + CA 19-9):** 97% sensitivity for Stage I/II PDAC (AACR 2024). ClearNote Health's **Avantect** test: 82.6% sensitivity, 97.5% specificity overall. In clinical validation.
- **ENDPAC Model / PanCAN Early Detection Initiative (NCT04662879):** Prospective scoring system applied to new-onset diabetes patients — ENDPAC score >0 triggers abdominal imaging referral. Active trial, not yet EHR-embedded at scale.
- **Plasma proteomics panels** (*Nature Medicine*, 2025): Multi-protein blood panels predicting PDAC trajectory up to 3 years pre-diagnosis. Validated in European cohorts.
- **Northwell iNav AI:** Operational AI that cuts time from suspicious imaging to biopsy-confirmed diagnosis in half. Deployed in select Northwell sites.
- **ctDNA liquid biopsy (standalone):** Only 40–65% sensitivity at Stage I. Clinically useful post-surgery for minimal residual disease; insufficient alone for screening.

**Main Limitations:**
- Exosome tests and plasma proteomics: not yet FDA-cleared; require prospective validation in diverse populations
- REDMOD: requires CT scan as input (not a blood test); still needs prospective RCT-level validation
- EUS: access bottleneck outside academic centers; requires sedation and GI specialist

---

### 5) 🏥 Where Healthcare Is Failing (Operational Insight)

**Screening point that drops the ball:**
> **Primary care + endocrinology at the moment of new-onset diabetes diagnosis.** This is the single highest-yield missed window. A 50-year-old presenting with unexplained weight loss + new hyperglycemia should trigger an ENDPAC score calculation and imaging referral — but in >95% of real-world encounters, it triggers a metformin prescription and HbA1c monitoring. No EHR has ENDPAC built in as a clinical decision support (CDS) alert.

**Bottleneck most fixable in 90 days:**
> **EHR-embedded ENDPAC CDS alert at primary care + endocrinology.** The ENDPAC model is validated, free, and requires only age, BMI, and blood glucose trend data already in the chart. A 90-day pilot at a single health system could embed this as a BPA (Best Practice Advisory) in Epic/Cerner, measure referral rates, imaging yield, and stage-at-detection shift. Zero new technology required.

**High-risk population missed:**
> **Community-dwelling adults aged 50–70 with new-onset diabetes, no genetic testing, and no access to tertiary surveillance programs.** This group carries a 5× elevated risk but is invisible to CAPS/PRECEDE because they never get referred. Disproportionately affects rural, low-income, and minority populations with limited access to academic medical centers. Additionally: patients with *deteriorating* previously controlled diabetes (Type 3c phenotype) — a signal validated in 2025 UK/EU data — are almost never flagged in real-world practice.

---

### 6) 💡 3 High-Leverage Solution Ideas (Practical, Ranked)

---

**🥇 Idea A — EHR-Embedded ENDPAC Clinical Decision Support Alert (Quick Pilot, 30–60 days)**

*How to run the pilot:*
- Partner with a single health system (Epic or Cerner shop) with a large primary care + endocrinology footprint
- Build a Best Practice Advisory (BPA) that fires when: patient age ≥50 + new diabetes diagnosis (ICD-10 E11.x first occurrence) + BMI decline >5% in 6 months
- BPA calculates ENDPAC score from structured EHR data; if score >0, surfaces a one-click referral to pancreatic imaging (MRCP or abdominal CT)
- Run for 60 days across 5–10 primary care clinics

*Metrics to collect:*
- ENDPAC alert fire rate per 1,000 new diabetes diagnoses
- Clinician acceptance rate (click-through vs. dismiss)
- Imaging referral completion rate within 30 days
- Yield: number of pancreatic lesions / PDAC cases identified per 100 imaged
- Stage at detection vs. institutional historical baseline

*Why this wins:* Zero new technology. Uses validated model. Directly closes the most actionable real-world gap. Publishable as a QI study. Scalable to any EHR system globally.

---

**🥈 Idea B — Opportunistic AI-PACS Integration for Radiomics Screening (Scalable Tech, 60–90 days)**

*How to run:*
- License or collaborate with Mayo Clinic's REDMOD team (or build a comparable model) to deploy a radiomics AI plugin into the hospital PACS system
- Target: all abdominal CT scans ordered for *any* indication in patients aged 40+ (opportunistic screening)
- AI flags subtle pancreatic radiomic changes → generates a structured radiology alert → triggers a pancreatic protocol CT or EUS referral
- Pilot at 1–2 high-volume radiology departments for 90 days

*Resource checklist:*
- PACS API access + DICOM routing permissions
- IRB approval for retrospective + prospective validation
- Radiologist workflow integration (alert fatigue mitigation protocol)
- Multidisciplinary pancreatic team to handle downstream referrals

*Expected impact:* If REDMOD replicates its 73% pre-diagnostic sensitivity in real-world deployment, a 500-CT/day radiology department could identify 2–5 pre-symptomatic PDAC cases per month that would otherwise be missed for 1–3 years.

---

**🥉 Idea C — Multi-Biomarker Blood Test Validation Consortium (Research/Product, 90-day setup)**

*Concept:*
- Establish a prospective biobank + clinical validation study combining: (1) exosome microRNA panel (8-miRNA), (2) CA 19-9, (3) plasma proteomics (top 5 proteins from *Nature Medicine* 2025 panel), (4) ENDPAC score
- Target population: new-onset diabetes patients aged 50–75 across 3–5 sites
- Primary endpoint: sensitivity/specificity of the combined panel for Stage I–II PDAC at 12-month follow-up

*Collaborators to approach:*
- **ClearNote Health** (Avantect test — clinical validation partner)
- **PRECEDE Consortium** (existing high-risk registry infrastructure)
- **PanCAN Early Detection Initiative** (NCT04662879 — potential add-on biomarker sub-study)
- **Mayo Clinic AI/Radiology** (REDMOD integration)

*Highest upside:* A validated 4-component panel achieving >90% sensitivity + >95% specificity in the NOD population would be the first clinically deployable blood test for PDAC early detection — a regulatory and commercial breakthrough. FDA Breakthrough Device Designation likely achievable.

---

### 7) 🔬 First-Principles Signal Hunt (What We Should Measure Earlier)

**Hidden signal candidate:**
> **Exosome-encapsulated microRNAs (particularly miR-196a, miR-217, miR-10b) + plasma ceruloplasmin mRNA + glycemic trajectory slope** — these three signals exist in blood months to years before imaging-detectable tumor. The glycemic trajectory (rate of HbA1c rise + BMI decline velocity) is already in every EHR and costs nothing to compute. The exosome panel is the most sensitive early-detection signal identified to date (97% Stage I/II sensitivity when combined with CA 19-9).

**Minimal sampling change needed:**
> **Standard venipuncture (5 mL whole blood → plasma separation)** — no new sample type required. The exosome/microRNA panel and plasma proteomics both operate on plasma from routine blood draws. The key operational change is *when* to draw: at the moment of new-onset diabetes diagnosis, not after symptoms of cancer appear. This is a **protocol change, not a technology change**, in the first instance.

**Additional first-principles signal:**
> **Pancreatic duct diameter on incidental imaging** — a duct >3mm on any abdominal CT (ordered for any reason) is an early, often-ignored radiologic red flag. Embedding automated duct measurement into PACS AI (alongside REDMOD) would create a zero-cost secondary alert layer on every existing abdominal CT.

---

### 8) 📊 Strategic Value & Next Immediate Actions (CEO Lens)

**Public health impact:**
> PDAC is the **3rd leading cause of cancer death** in the US (~66,000 new cases, ~51,000 deaths in 2026). 5-year survival is 13% overall — among the lowest of any cancer. The economic burden exceeds $20B annually in the US alone. Global incidence is rising 1–2% per year, driven by aging populations, obesity, and T2DM prevalence. The asymmetry is brutal: Stage I detection = near-curative surgery. Stage IV = median survival of 6–12 months. Every month of detection delay costs lives at scale.

**3 Immediate Actions:**

| Timeline | Action |
|---|---|
| **Today** | Read the Mayo Clinic REDMOD paper (*Gut*, April 2026: *"Next-generation AI for visually occult pancreatic cancer detection in routine CT scans"*) + the ENDPAC validation paper (PMC12712999). Map which EHR your target health system uses (Epic vs. Cerner) and identify the CDS/BPA team lead. |
| **7 Days** | Contact PanCAN (Pancreatic Cancer Action Network) and the PRECEDE Consortium (precedestudy.org) to explore a site partnership. Draft a 1-page pilot spec for the ENDPAC BPA alert — include inclusion criteria, alert logic, referral pathway, and 60-day metrics dashboard. |
| **30 Days** | Submit IRB pre-review application for the ENDPAC BPA pilot at a partnering health system. Simultaneously, request a collaboration call with ClearNote Health (Avantect) to explore a biomarker sub-study within the NOD population. Define the 90-day pilot KPIs: alert fire rate, imaging yield, stage-at-detection shift. |

---

### 9) 🧠 One-Minute Mental Model

> *"PDAC hides in a biological dead zone — no lumen, no early pain, no reliable biomarker — for 2–3 years while the tumor is physically detectable by AI on scans that are already being ordered. The single leverage point is the new-onset diabetes signal: a 5× risk flag that fires 8–36 months before symptoms, sits in every EHR, and is universally ignored because no one built the alert. The fix is an ENDPAC BPA in Epic, not a new blood test."*

**📚 Attach — 3 search keywords / paper titles for immediate literature lookup:**
1. `"Next-generation AI for visually occult pancreatic cancer detection"` — *Gut* / BMJ, April 2026 (REDMOD paper)
2. `"Enriching New-Onset Diabetes for Pancreatic Cancer ENDPAC"` — PMC12712999 / NCT04662879
3. `"Exosome-based liquid biopsy early detection pancreatic cancer microRNA"` — AACR 2024 press release + ClearNote Health Avantect

---

### 10) 🔁 Pattern Insight (Meta-Learning)

**What recurring diagnostic failure pattern is emerging?**

PDAC reinforces the **"signal-in-plain-sight" pattern** — the most powerful recurring theme across early-diagnosis failures:

> *The early signal exists and is measurable. It is not hidden by biology alone — it is hidden by workflow, incentive structure, and the absence of a single point-of-care alert or protocol that converts the signal into clinical action.*

This pattern has appeared across multiple disease categories:
- **HIV/HCV:** Virus detectable early → missed because no routine screening reflex in primary care
- **HCC:** Cirrhosis patients known → missed because ultrasound surveillance adherence is <50%
- **Ovarian cancer:** CA-125 + transvaginal ultrasound exist → missed because no systematic screening trigger
- **PDAC:** New-onset diabetes + radiomic signatures exist → missed because no ENDPAC alert and no AI in PACS

**Is today's disease reinforcing or breaking the pattern?**
> **Strongly reinforcing.** PDAC is the most extreme version of this pattern — the gap between "biologically detectable" and "clinically detected" is 16–36 months, and the mortality consequence of that gap is near-total. The fix in every case is not primarily a new diagnostic technology — it is a **workflow integration of an existing validated signal into the clinical decision pathway**.

**What generalizable opportunity is forming across diseases?**
> The meta-opportunity is **"Signal-to-Alert Infrastructure"**: a layer that sits between validated research biomarkers/models and real-world clinical workflows. Every disease in this series has a validated early signal. Almost none have a functioning alert system that converts that signal into clinical action at the point of care. The startup opportunity is not another biomarker company — it is the **middleware layer** that embeds validated signals (ENDPAC, REDMOD, AFP-L3, NfL) into EHRs as actionable, evidence-based CDS alerts, with outcome tracking to close the feedback loop. This is a horizontal platform play with enormous public health leverage.

---

*📅 Report Date: Monday, July 7, 2026 | Prepared for: Ayan Mukhopadhyay | Focus: Research + Hospital Improvement + Partial Startup*