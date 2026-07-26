I now have all the data needed to produce a rich, decision-grade brief. I'll select **Pancreatic Ductal Adenocarcinoma (PDAC)** as today's disease — it has the highest asymmetric diagnostic gap, the most active 2025–2026 research landscape, and enormous public health + startup opportunity. Let me now compose the full report.

---

**Subject: Daily Early-Diagnosis Brief — Pancreatic Ductal Adenocarcinoma (PDAC) — 2026-06-10**

---

## 1) Snapshot (one line)

**Pancreatic Ductal Adenocarcinoma (PDAC)** — why early diagnosis fails in practice: tumors grow silently for 10–15 years in an anatomically hidden organ, and the only FDA-recognized biomarker (CA 19-9) has ≤45% sensitivity for Stage I disease, leaving >80% of patients diagnosed at unresectable Stage III/IV.

---

## 2) Why Early Diagnosis Fails (3–5 bullets)

- **Biological barrier:** The pancreas sits retroperitoneally with no mucosal surface accessible to endoscopy; early tumors are microscopic, avascular, and cause zero organ dysfunction — symptoms (jaundice, weight loss, back pain) only emerge when the tumor obstructs the bile duct or invades adjacent structures, typically at Stage III/IV. Median tumor diameter at diagnosis is ~3 cm; Stage I tumors are <2 cm and largely asymptomatic.

- **Test limitation:** CA 19-9 — the only FDA-cleared serum biomarker — achieves only **45% sensitivity for Stage I PDAC** (vs. 85% for Stage III/IV); it is falsely elevated in pancreatitis, cholestasis, and biliary obstruction, and is completely negative in Lewis antigen-negative patients (~10% of population). No single-biomarker blood test is recommended for population screening.

- **System failure (primary care):** New-onset diabetes after age 50 (NOD50) is a well-established PDAC red flag — ~1% of NOD50 patients harbor occult pancreatic cancer within 3 years — yet zero major EHR systems have automated oncology referral triggers for this cohort. Primary care physicians are not trained to consider PDAC in the differential of new-onset diabetes.

- **System failure (imaging):** Routine abdominal CT scans (ordered for GI complaints, back pain, or other reasons) frequently miss sub-centimeter pancreatic lesions — a 2026 Mayo Clinic AI study (*Gut*, April 2026) showed that radiologists miss subtle pancreatic parenchymal changes that AI can detect **up to 3 years before** clinical diagnosis on the *same CT scan*.

- **High-risk population gap:** Patients with germline mutations (BRCA1/2, PALB2, ATM, CDKN2A), familial pancreatic cancer (FPC ≥2 first-degree relatives), or chronic pancreatitis qualify for surveillance — but fewer than **5% of eligible high-risk individuals** are enrolled in any formal surveillance program in the US.

---

## 3) Detection Window & Gap

| Milestone | Time / Marker |
|---|---|
| **Earliest detectable signal (research)** | ctDNA methylation signatures / exosomal miRNA / PAC-MANN protease assay — detectable at Stage I (~T1N0M0, <2 cm) |
| **AI-assisted CT signal** | Mayo Clinic PANDA model detects parenchymal changes **up to 36 months** before clinical diagnosis on routine CT |
| **CA 19-9 becomes clinically informative** | Stage II–III (typically when tumor >2–3 cm or biliary obstruction present) |
| **Typical clinical detection** | Stage III/IV in ~80% of patients; median time from first symptom to diagnosis: **0.6–1.2 months** — but the pre-symptomatic window is **10–15 years of silent growth** |
| **Gap to close** | **~24–36 months** of missed early-stage window where curative resection is still possible (5-year survival: Stage I = 44% vs. Stage IV = 3%) |

**Practical impact of closing the gap:** Shifting even 20% of diagnoses from Stage IV to Stage I/II would save ~8,000–12,000 lives/year in the US alone.

---

## 4) What's Being Used Today (Gold Standard + Emergent)

### Gold Standards:
- **CT Abdomen/Pelvis with contrast** — workhorse imaging; misses lesions <1 cm; operator and protocol dependent
- **Endoscopic Ultrasound (EUS)** — highest sensitivity for small lesions (>90% for >1 cm); invasive, requires sedation, not scalable for population screening
- **ERCP** — diagnostic + therapeutic for biliary obstruction; invasive, high complication risk
- **CA 19-9 serum test** — monitoring tool, not a screening tool; sensitivity 45% (Stage I), 72% (pooled all-stage)

### Emerging Research / Tools (2025–2026):

| Tool | Sensitivity | Specificity | Stage | Status |
|---|---|---|---|---|
| **PAC-MANN assay** (OHSU, PubMed 39937880) — protease nanosensor + CA 19-9 | **85%** (Stage I) | **96%** | I | Research / validation |
| **Avantect® cfDNA test** (ClearNote Health) — multiomics cell-free DNA | **82.6%** (overall) | **76.8%** | I–II | LDT launched; ASCO 2026 data |
| **PancreaSure** (Immunovia) — 5-biomarker serum panel | **78%** | **92%** | I–II | Launched US Sep 2025; CPT code Oct 2025 |
| **PANDA AI model** (Mayo Clinic) — CT-based parenchymal change detection | Detects 3 yrs pre-Dx | — | Pre-clinical | FDA Breakthrough Device Designation |
| **Exosome liquid biopsy + CA 19-9** (AACR 2025) | Improved vs CA 19-9 alone | High | I–II | Research |
| **miRNA-based assays** (Goel lab, ASCO GI 2025) | Promising | Under validation | I | Research |

### Main Limitations:
- PAC-MANN: not yet commercially available; needs multi-site prospective validation
- Avantect: specificity (76.8%) implies meaningful false-positive rate in a low-prevalence population — NNT/NNS economics challenging for general screening
- PancreaSure: currently limited to 8 US surveillance centers; insurance coverage not yet established
- PANDA AI: requires retrospective CT — needs prospective integration into radiology workflows

---

## 5) Where Healthcare Is Failing (Operational Insight)

**Screening point that drops the ball:**
> **Primary care / endocrinology at the moment of new-onset diabetes diagnosis in patients >50 years.** This is the single highest-yield missed trigger. ~1% of NOD50 patients harbor pancreatic cancer — a prevalence 6–8× higher than the general population. No EHR system currently auto-flags these patients for GI/oncology referral or biomarker testing. The window between NOD50 and pancreatic cancer symptom onset averages **6–18 months** — exactly the window where intervention is still curative.

**Bottleneck most fixable in 90 days:**
> **EHR-based clinical decision support (CDS) alert for NOD50 + weight loss + elevated CA 19-9 (even in "normal" range trending up).** This is a pure software/workflow change requiring no new hardware. A rule-based CDS alert in Epic/Cerner can be deployed in 30–60 days at a single health system. Pilot metric: number of high-risk patients flagged → referred → imaged within 30 days.

**High-risk population missed:**
- **NOD50 patients** — ~1.5 million new T2DM diagnoses/year in US; ~15,000 may harbor occult PDAC
- **BRCA1/2 / PALB2 / ATM germline carriers** — estimated 1–2M in US; <5% in formal pancreatic surveillance
- **Familial pancreatic cancer (FPC) kindreds** — first-degree relatives of PDAC patients have 9× elevated risk; most never referred to high-risk programs
- **Chronic pancreatitis patients** — 5–15× elevated PDAC risk; rarely enrolled in systematic surveillance

---

## 6) Three High-Leverage Solution Ideas (Practical, Ranked)

### 🥇 Idea A — EHR-Triggered NOD50 Reflex Protocol (30-Day Pilot)
**Concept:** Deploy a clinical decision support rule in Epic/Cerner that auto-alerts the ordering physician when a patient aged 50–80 receives a new T2DM diagnosis AND has ≥1 of: unexplained weight loss (>5% in 6 months), CA 19-9 trending upward (even within normal range), or pancreatic duct dilation on prior imaging. Alert triggers a standardized referral order to GI/pancreatic oncology.

**How to run the pilot (30–60 days):**
- Partner with 1 academic medical center with Epic access
- Define CDS rule logic with biomedical informatics team (2 weeks)
- Deploy as "advisory" (non-blocking) alert; track alert firing rate, provider acceptance rate, time-to-referral, time-to-imaging
- **Metrics:** # alerts fired / # accepted / # patients imaged within 30 days / # PDAC detected / stage at detection
- **Resource checklist:** Epic analyst (1 FTE, 2 weeks), GI champion, IRB waiver for quality improvement
- **Expected impact:** Even 10% alert acceptance rate at a 500-bed hospital could identify 2–5 early-stage PDAC cases/year that would otherwise be missed

---

### 🥈 Idea B — High-Risk Surveillance Clinic + Liquid Biopsy Integration (60–90 Day Pilot)
**Concept:** Stand up or expand a dedicated "Pancreatic High-Risk Clinic" at an academic center, integrating PancreaSure (Immunovia) or Avantect (ClearNote Health) blood testing into existing surveillance protocols alongside annual EUS/MRI for BRCA/FPC patients.

**How to run:**
- Identify 50–100 eligible high-risk patients (BRCA2, PALB2, FPC) currently in surveillance
- Add annual liquid biopsy (PancreaSure or Avantect) as adjunct to standard EUS/MRI
- Collect: test positivity rate, concordance with imaging, patient acceptance, turnaround time, cost per test
- **Metrics:** sensitivity/specificity in this real-world cohort; time from blood draw to result; cost-effectiveness vs. EUS alone
- **Resource checklist:** GI oncology champion, phlebotomy protocol, lab courier agreement with Immunovia/ClearNote, IRB approval (~30 days)
- **Expected impact:** Validates real-world performance of emerging tests; generates publishable data; builds case for payer coverage

---

### 🥉 Idea C — AI-Augmented Radiology Screening (PANDA Integration Research Partnership)
**Concept:** Partner with Mayo Clinic or a radiology AI vendor to deploy the PANDA CT-screening AI model as a background "second reader" on all abdominal CT scans performed for any indication in patients >50. Flag cases where the model detects subtle pancreatic parenchymal changes for radiologist review.

**Tests needed:**
- Prospective validation in a non-Mayo population (external validation cohort)
- False-positive rate characterization in general radiology population
- Workflow integration study (radiologist burden, turnaround time)
- Health-economic model: cost per QALY gained vs. standard of care

**Collaborators to approach:**
- Mayo Clinic AI lab (PANDA team, *Gut* 2026 paper authors)
- Nuance/Microsoft (PowerScribe integration)
- NCI Early Detection Research Network (EDRN)
- GRAIL / Exact Sciences (multi-cancer early detection ecosystem)

**Highest upside:** If PANDA achieves prospective validation, this becomes a zero-cost-per-patient "passive screening" layer on top of existing imaging infrastructure — potentially the highest-leverage intervention in the history of pancreatic cancer detection.

---

## 7) First-Principles Signal Hunt (What We Should Measure Earlier)

**Hidden signal candidate:**
> **Pancreatic exosomal microRNA signatures in plasma (miR-196a, miR-217, miR-10b) + host transcriptomic shift in peripheral blood mononuclear cells (PBMCs) reflecting tumor-induced immune suppression.** These signals precede CA 19-9 elevation by months and are detectable at Stage I. Additionally, **serum/plasma proteomics via PAC-MANN-class protease nanosensors** represent a fundamentally different signal class — measuring enzymatic *activity* (not antigen concentration), which is amplified even at low tumor burden.

**Minimal sampling change needed:**
> **Standard 10 mL EDTA whole blood draw** — the same tube used for routine CBC. No special collection protocol, no fasting required, no invasive procedure. The bottleneck is not sample collection — it's the downstream assay infrastructure. A reflex testing protocol ("if NOD50 + age >50 → add PAC-MANN/PancreaSure panel to existing blood draw") adds zero patient burden.

**Second candidate signal:** Subtle pancreatic duct morphology changes (main duct diameter trending from 2mm → 3mm over 2 years) on routine MRI/MRCP — currently not systematically tracked in longitudinal imaging reports. A structured reporting template that captures duct diameter at every abdominal MRI could create a passive surveillance dataset.

---

## 8) Strategic Value & Next Immediate Actions (CEO Lens)

### Public Health Impact:
- **US incidence:** ~68,000 new cases/year (2026 estimate); **~64,000 deaths/year** — among the highest cancer-specific mortality rates
- **5-year survival:** Overall ~13%; Stage I = 44%; Stage IV = 3%
- **Economic burden:** ~$4.9B direct medical costs/year in US; average cost of late-stage treatment ($180K+) vs. early surgical resection ($80–120K with curative intent)
- **Global:** 510,000 new cases/year; 5th leading cause of cancer death in developed nations
- **Asymmetric opportunity:** A diagnostic intervention that shifts 20% of diagnoses from Stage IV → Stage I/II would save ~10,000 lives/year in the US — equivalent impact to a new drug with a fraction of the regulatory burden

### 3 Immediate Actions:

| Horizon | Action |
|---|---|
| **Today** | Read: *"Next-generation AI for visually occult pancreatic cancer detection"* — Gut, BMJ, April 2026 (gutjnl-2025-337266). Understand the PANDA model's validation cohort and false-positive rate — this is the highest-leverage research asset in the space right now. |
| **7 Days** | Map the NOD50 patient population at your affiliated hospital: pull Epic data on patients aged 50–80 with new T2DM diagnosis in the past 12 months. Cross-reference with CA 19-9 orders, GI referrals, and abdominal imaging. Quantify the gap — how many NOD50 patients had zero pancreatic workup? This is your pilot dataset. |
| **30 Days** | Draft a 90-day pilot protocol: EHR CDS alert for NOD50 + PancreaSure reflex testing. Identify a GI oncology champion, biomedical informatics lead, and IRB pathway (quality improvement exemption). Contact Immunovia (PancreaSure) and ClearNote Health (Avantect) for research partnership/LDT access. Submit pilot concept to your institutional Cancer Center. |

---

## 9) One-Minute Mental Model

> *"Pancreatic cancer hides in plain sight for a decade — it is not that we lack the biology to detect it early, but that we have no systematic trigger to look. The single leverage point is the new-onset diabetes signal: a 1% cancer prevalence in a readily identifiable population, a 6–18 month action window, and a blood test that now exists (PancreaSure, Avantect) — but no EHR rule to connect the dots. The entire diagnostic failure is a workflow problem masquerading as a biology problem."*

### 📚 Literature / Search Keywords:
1. **`"PAC-MANN" pancreatic cancer protease assay CA 19-9 Stage I`** → PubMed ID 39937880 (OHSU, Feb 2025)
2. **`"PANDA" AI pancreatic cancer CT detection visually occult`** → *Gut* BMJ, April 2026 (gutjnl-2025-337266); also Targeted Oncology: FDA Breakthrough Device Designation
3. **`"new-onset diabetes" pancreatic cancer screening NOD50 SAFE-D trial`** → ClinicalTrials.gov NCT06803771 (Avantect/SAFE-D study)

---

## 10) Pattern Insight (Meta-Learning)

### 🔁 Recurring Diagnostic Failure Pattern Emerging:
**"The Trigger Gap" — diseases where the biology of early detection exists, but the clinical workflow trigger to deploy it does not.**

This is not a technology problem. The PAC-MANN assay, Avantect, PancreaSure, and PANDA AI all exist in 2026. The failure is upstream: **no systematic clinical rule, EHR alert, or population-level screening policy connects the at-risk patient to the test.** The same pattern appears across:

| Disease | Hidden Trigger | Missed Population |
|---|---|---|
| PDAC (today) | New-onset diabetes >50 | NOD50 patients, BRCA carriers |
| ATTR Cardiac Amyloidosis | HF + carpal tunnel + low-voltage ECG | Elderly HFpEF patients |
| Alzheimer's (preclinical) | APOE4 + subtle memory complaints | Primary care patients with "normal" cognition |
| Ovarian Cancer | CA-125 trajectory (not single cutoff) | Women with vague GI symptoms |
| PAH | Unexplained dyspnea + normal echo | Young women, connective tissue disease patients |

### 🔓 Generalizable Opportunity Forming:
> **The highest-ROI diagnostic startup of the next 5 years is not a new biomarker company — it is a clinical decision support layer that systematically connects existing at-risk patient populations to existing (but underdeployed) early-detection tests.** The moat is not the assay; it is the EHR integration, the risk-stratification algorithm, and the referral pathway. Think: a "diagnostic orchestration" platform that sits on top of Epic/Cerner, identifies trigger events (NOD50, HFpEF + ECG pattern, APOE4 + cognitive complaint), and auto-initiates the appropriate early-detection workup. This pattern is disease-agnostic and scalable.

**Breaking or reinforcing the pattern?** → **Strongly reinforcing.** PDAC is the clearest example yet of the Trigger Gap — where a decade of biology research has outpaced clinical deployment by years. The actionable insight: **build the bridge, not the biomarker.**

---

*Brief prepared for: Ayan Mukhopadhyay | System time: Wednesday, June 10, 2026, 09:00 UTC | Research sources: PubMed, ClinicalTrials.gov, ASCO/AACR 2026, BMJ Gut, AJMC, ACG 2025, ClearNote Health, Immunovia, Mayo Clinic AI Lab*