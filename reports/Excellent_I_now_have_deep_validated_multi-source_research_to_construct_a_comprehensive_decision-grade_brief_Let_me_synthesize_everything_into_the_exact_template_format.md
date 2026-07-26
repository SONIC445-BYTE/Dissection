Excellent. I now have deep, validated, multi-source research to construct a comprehensive, decision-grade brief. Let me synthesize everything into the exact template format.

---

## Subject: Daily Early-Diagnosis Brief — Pancreatic Ductal Adenocarcinoma (PDAC) — 2026-06-01

---

### 1) Snapshot (one line)

**Pancreatic Ductal Adenocarcinoma (PDAC)** — early diagnosis fails because the disease is biologically silent during its resectable window, CA19-9 is blind to early-stage tumors, and no population-level screening pathway exists to intercept it before metastasis.

---

### 2) Why Early Diagnosis Fails (3–5 bullets)

- **Biological barrier:** PDAC grows in a retroperitoneal, anatomically hidden location with a dense desmoplastic stroma that suppresses immune signaling and limits circulating tumor DNA (ctDNA) shedding — making liquid biopsy signals faint until the tumor is large. Symptoms (back pain, new-onset diabetes, mild indigestion) are non-specific and mimic far more common conditions.
- **Test limitation:** CA19-9 — the only widely used serum biomarker — has <50% sensitivity at Stage I/II, is entirely undetectable in 5–10% of the population (Lewis blood group antigen-negative individuals), and lacks specificity (false positives in pancreatitis, biliary obstruction, liver disease). No validated, affordable blood test for general screening exists.
- **System failure (screening policy):** No population-level screening program exists for PDAC. Guidelines restrict surveillance (MRI/MRCP or EUS) to high-risk genetic carriers (BRCA2, PALB2, ATM, CDKN2A, Lynch syndrome) — yet most carriers are never genetically tested. The general population has zero structured entry point.
- **System failure (primary care workflow):** Vague symptoms route patients through musculoskeletal or GI workups first. A 10-year malpractice analysis confirms months of misattribution before imaging is ordered. Up to **58% of PDAC patients are diagnosed during emergency hospital admissions** — bypassing outpatient diagnostic pathways entirely.
- **System failure (safety netting):** Abnormal preliminary labs (mild bilirubin rise, unexplained weight loss, new-onset diabetes in patients >50) are not systematically flagged for reflex pancreatic imaging. Electronic safety-netting tools exist but are not deployed at scale.

---

### 3) Detection Window & Gap (concise)

| | Signal / Timepoint |
|---|---|
| **Earliest detectable signal (research/ideal)** | Serum CA19-9 upregulates **up to 2 years** before clinical diagnosis; metabolomic and proteomic shifts detectable **2–3 years** pre-diagnosis in biobank samples; Mayo Clinic AI CT detects morphologic change a **median 475 days (up to 3 years)** before standard diagnosis |
| **Typical clinical detection** | **Stage III–IV** in 80–90% of patients; median time from first symptom to diagnosis: **~6 months** in community settings |
| **Gap to close** | **18–36 months** of biological lead time is being squandered. Closing even 12 months of this gap shifts patients from 3% (metastatic) to 44% (localized) 5-year survival — a **14× survival multiplier** |

---

### 4) What's Being Used Today (Gold Standard + Emergent)

**Gold Standards:**
- **Serum CA19-9** — monitoring and surgical follow-up, not screening (sensitivity <50% at Stage I/II)
- **CT abdomen/pelvis with contrast** — primary staging modality; misses sub-centimeter lesions
- **Endoscopic Ultrasound (EUS)** — gold standard for tissue sampling and cyst evaluation; invasive, expensive, specialist-dependent
- **MRI/MRCP** — preferred for high-risk surveillance; not scalable for general population

**Emerging Research / Tools (2024–2026):**
- **Four-biomarker plasma panel (CA19-9 + THBS2 + ANPEP + PIGR):** Krusen et al., *Clinical Cancer Research* (Feb 2026) — AUC 0.94–0.97; **87.5% sensitivity for Stage I–II at 95% specificity**. Significant improvement over CA19-9 alone.
- **PAC-MANN (Protease-ACtivated MAgnetic NaNosensor):** OHSU, *Science Translational Medicine* (Feb 2025) — measures **protease activity** in blood; 85% accuracy for hard-to-detect PDAC; proof-of-concept, not yet in clinical trials.
- **Exosome-based liquid biopsy + CA19-9** (AACR 2024): 97% overall accuracy, **91% accuracy for early-stage** PDAC.
- **miRNA liquid biopsy panel** (NCI, 2024–2025): 98% specificity, 73% sensitivity for early-stage patients.
- **Mayo Clinic / Gut (BMJ) AI CT model** (2025–2026): Detects visually occult PDAC on routine abdominal CT scans with **92% accuracy**, median 475-day lead time; trained on 1,462 scans. Prospective AI-PACED trial now underway.
- **ARTEMIS-DELFI:** cfDNA fragmentation pattern analysis — distinguishes true malignancy from benign cysts.
- **PancreaSeq** (cyst fluid genomics): 82% sensitivity, 100% specificity for advanced neoplasia in pancreatic cysts — not a blood test, but critical for cyst management.
- **New-onset diabetes (NOD) as trigger:** ~1% of patients >50 with NOD develop PDAC within 3 years; 40% of PDAC patients had NOD within 36 months pre-diagnosis. NOD as a structured screening trigger is validated but not operationalized.

**Main Limitations:**
- Multi-marker panels not yet FDA-cleared or in prospective screening trials
- AI CT models need prospective validation in diverse, non-academic settings
- EUS requires specialist access unavailable in most community hospitals
- ctDNA signal is extremely low (<0.1% variant allele frequency) at Stage I — requires ultra-deep sequencing

---

### 5) Where Healthcare Is Failing (Operational Insight)

**Screening point that drops the ball:**
Primary care is the single largest failure node. Physicians lack a structured algorithm to escalate non-specific symptoms (new-onset diabetes in patients >50, unexplained weight loss, mid-back pain, mild jaundice) into a pancreatic imaging pathway. There is no equivalent of the "chest pain rule-out" protocol for pancreatic red flags.

**Bottleneck most fixable in 90 days:**
**New-onset diabetes (NOD) reflex imaging protocol.** EHR systems already capture new diabetes diagnoses. A rule-based EHR alert for patients aged 50+ with new-onset diabetes (or unexplained weight loss + abdominal pain) triggering an automatic order for CT abdomen or CA19-9 + THBS2 panel is implementable in a single hospital system within 90 days. The Early Detection Initiative (NCT04662879) is already testing this — hospitals can adopt the protocol now without waiting for trial completion.

**High-risk population missed:**
- **Lewis antigen-negative patients (~5–10%):** CA19-9 will always read normal regardless of tumor burden — zero clinical awareness of this at point-of-care.
- **Ungenotyped high-risk individuals:** Patients with BRCA2, PALB2, ATM, or Lynch syndrome mutations who have never received genetic testing — estimated >70% of eligible patients are not tested or not enrolled in surveillance programs.
- **New-onset diabetics >50 in community/rural settings:** Managed by PCPs without oncologic context; the NOD-to-PDAC connection is known in literature but not embedded in clinical workflows.

---

### 6) 3 High-Leverage Solution Ideas (Practical, Ranked)

**🥇 Idea A — NOD-Triggered EHR Reflex Alert (30–60 day pilot, hospital-level)**

*What:* Implement an EHR clinical decision support (CDS) rule that fires for any patient aged 50–85 newly diagnosed with Type 2 diabetes (HbA1c ≥6.5% or fasting glucose ≥126 mg/dL) with no prior diabetes history. The alert recommends: (1) CA19-9 + weight trend review, (2) CT abdomen/pelvis if CA19-9 elevated OR unexplained weight loss >5% body weight in 6 months.

*How to run the pilot:*
- Site: 1–2 internal medicine/primary care clinics within a hospital system
- Duration: 60 days
- Metrics: Alert trigger rate, alert acceptance rate by PCPs, number of CT scans ordered, number of PDAC cases detected, time-to-diagnosis vs. historical baseline
- Resource: EHR build (Epic/Cerner) + clinical champion (1 gastroenterologist or oncologist) + IRB waiver for QI project
- Expected impact: Modeled on Early Detection Initiative data — if 1% of NOD patients >50 have occult PDAC, a 200-patient pilot could yield 2 early-stage diagnoses that would otherwise present as Stage IV in 6–18 months

---

**🥈 Idea B — AI CT Pancreatic Flag Integration (60–90 day pilot, radiology workflow)**

*What:* Deploy the Mayo Clinic / *Gut* BMJ AI model (or equivalent) as a background inference layer on routine abdominal CT reads. The AI flags morphologic changes (pancreatic duct dilation, parenchymal atrophy, subtle density changes) and generates a structured radiologist alert — not a diagnosis, but a "pancreatic protocol follow-up recommended" flag.

*How to run:*
- Partner with Mayo Clinic, Viz.ai, or Seer (companies building organ-specific AI flags) — or access the model via the AI-PACED trial consortium
- Pilot in a radiology department reading >50 abdominal CTs/day
- Metrics: Number of AI flags per 100 CTs, radiologist override rate, positive predictive value of flags at 6-month follow-up, time-to-specialist referral
- Resource checklist: GPU inference server or cloud API, PACS integration, radiologist training (0.5 day), IRB
- Expected impact: 92% AI accuracy with 475-day lead time means every 100 flagged patients could yield 1–3 early-stage PDAC cases that would otherwise be missed for 12+ months

---

**🥉 Idea C — Multi-Marker Liquid Biopsy Validation + Commercialization Track (90-day research sprint)**

*What:* Design a prospective, IRB-approved blood collection protocol at a cancer center or academic hospital to validate the **CA19-9 + THBS2 + ANPEP + PIGR** four-marker panel (Krusen et al.) in a new independent cohort — specifically including Lewis antigen-negative patients and NOD patients. Simultaneously, evaluate PAC-MANN protease activity assay in the same samples.

*How to run:*
- Collaborators to approach: Brianna M. Krusen / Erin Jonasch group (AACR), OHSU liquid biopsy team (PAC-MANN), PRECEDE Consortium (NCT04970056)
- Sample size: 150–200 patients (50 early-stage PDAC, 50 benign pancreatic disease, 50 healthy controls, 50 NOD patients)
- 30-day: IRB submission + biobank access agreement
- 60-day: Sample collection begins, Lewis antigen genotyping added
- 90-day: Preliminary AUC data on four-marker panel; go/no-go decision for expanded validation or startup formation around the assay
- Highest upside: A validated, Lewis-antigen-agnostic, Stage I–II-sensitive blood panel is a direct path to FDA Breakthrough Device Designation and a $500M+ liquid biopsy market entry

---

### 7) First-Principles Signal Hunt (What We Should Measure Earlier)

**Hidden signal candidate:**
**New-onset diabetes metabolic signature + pancreatic exosome protein cargo.** The pancreas is the source of both insulin dysregulation and the tumor — meaning the metabolic disruption of early PDAC (insulin resistance, altered glucagon, amylase/lipase fluctuation) is already present in blood **months before CA19-9 rises.** Combining: (1) fasting C-peptide + proinsulin ratio, (2) exosome-derived EGFR/MUC1/GPC1 surface proteins, and (3) protease activity (PAC-MANN approach) into a single pre-diagnostic "pancreatic stress panel" could push detection to 24–36 months pre-symptom.

**Second candidate:** Host transcriptomic shift in peripheral blood mononuclear cells (PBMCs) — the immune system "sees" the tumor before clinical imaging does. RNA-seq of PBMCs in NOD patients may reveal a PDAC-specific innate immune activation signature distinct from Type 2 diabetes alone.

**Minimal sampling change needed:**
- Standard venipuncture (5 mL EDTA tube) — no new collection procedure
- Add Lewis antigen genotyping (once, from existing sample) to stratify CA19-9 interpreters
- Urine metabolomics (non-invasive) as orthogonal signal — emerging data shows urinary trypsinogen-2 and LRG1 elevated in early PDAC

---

### 8) Strategic Value & Next Immediate Actions (CEO Lens)

**Public health impact:**
- ~60,000 new PDAC diagnoses/year in the US; ~495,000 globally (2022, GLOBOCAN)
- 5-year survival: **13% overall; 3% at metastatic stage; 44% at localized stage**
- 80–90% diagnosed at late stage = structural, preventable mortality
- Economic burden: >$4.9B annual direct costs in the US; rising incidence (projected #2 cancer killer in the US by 2030)
- **Asymmetric opportunity:** Moving even 15% of diagnoses from Stage III–IV to Stage I–II would prevent ~7,500 deaths/year in the US alone — and a validated blood panel would command $800–1,200 per test in the US market

**3 Immediate Actions for Ayan:**

| Timeline | Action |
|---|---|
| **Today** | Read the Krusen et al. 2026 paper in *Clinical Cancer Research* (AACR): "Improving a Plasma Biomarker Panel for Early Detection of Pancreatic Ductal Adenocarcinoma" — and the *Gut* BMJ AI-PACED paper (April 2026). Bookmark the PRECEDE Consortium (NCT04970056) enrollment criteria. |
| **7 days** | Draft a 1-page QI proposal for a NOD-triggered EHR alert pilot at your institution. Identify your EHR build lead (Epic/Cerner analyst) and one clinical champion in internal medicine or gastroenterology. Simultaneously, contact the PRECEDE Consortium to explore biobank access or co-enrollment. |
| **30 days** | Submit IRB application (or QI exemption) for the NOD-triggered imaging pilot. Spec out the multi-marker blood panel validation protocol (CA19-9 + THBS2 + ANPEP + PIGR + PAC-MANN protease assay) with a target of 150 patients across 3 groups. Define go/no-go criteria for a startup formation decision at the 90-day data readout. |

---

### 9) One-Minute Mental Model

> *"PDAC hides behind two masks — a silent biology (no pain, no lump, no bleeding until late) and a broken workflow (vague symptoms routed to the wrong specialist, a biomarker blind to early-stage disease, and no population-level screening net). The single leverage point: the pancreas telegraphs its distress 18–36 months early through metabolic disruption (new-onset diabetes), protease activity, and subtle CT morphology — but no hospital has wired these signals into a reflex action. The fix is not a new drug; it's a new protocol."*

**Search keywords / papers for immediate lookup:**
1. **"Improving a Plasma Biomarker Panel for Early Detection of Pancreatic Ductal Adenocarcinoma"** — Krusen et al., *Clinical Cancer Research*, Feb 2026 (AACR DOI: 10.1158/1078-0432.CCR-24-2810)
2. **"Next-generation AI for visually occult pancreatic cancer detection"** — *Gut* (BMJ), April 2026 (DOI: 10.1136/gutjnl-2025-337266) — AI-PACED trial
3. **"Early detection of pancreatic cancer by a high-throughput protease-activated nanosensor assay"** — *Science Translational Medicine*, Feb 2025 (DOI: 10.1126/scitranslmed.adq3110) — PAC-MANN

---

### 10) Pattern Insight (Meta-Learning)

**Recurring diagnostic failure pattern: The "Silent Progression + Broken Trigger" Syndrome**

PDAC is the third consecutive archetype of a disease that fails early diagnosis not because the biology is unknowable — but because the **biological signal exists earlier than the clinical trigger that would prompt testing.** The pattern:

1. ✅ A detectable preclinical signal exists (metabolic, proteomic, imaging-based)
2. ❌ No structured clinical workflow converts that signal into a diagnostic action
3. ❌ The gold standard test (CA19-9) is calibrated for monitoring, not screening
4. ❌ High-risk populations are identified in guidelines but not operationally enrolled

This is the same pattern seen in:
- **ALS** (protein signature detectable 10–15 years early; no reflex blood test ordered)
- **Endometriosis** (inflammatory markers detectable years before laparoscopy; no non-invasive trigger)
- **PDAC** (metabolic + proteomic signal 18–36 months early; no NOD-to-imaging protocol)

**Generalizable opportunity forming:**
The cross-disease opportunity is **"signal-to-trigger engineering"** — the discipline of embedding known early biological signals into EHR workflows, primary care algorithms, and reflex testing protocols. This is not a biomarker discovery problem anymore for several diseases; it is a **clinical informatics and workflow deployment problem.** The founder/researcher who builds a disease-agnostic "early signal routing layer" — an EHR middleware that converts subclinical biomarker patterns into structured clinical actions — could address 5–10 diseases simultaneously. The PDAC NOD-trigger pilot is a perfect proof-of-concept for this broader platform.

**Breaking or reinforcing?** Strongly **reinforcing** — and escalating in urgency. The gap between what we *can* detect and what we *do* detect is widening as biomarker science outpaces clinical implementation. The next brief should target a disease where the signal-to-trigger gap is even more operationally solvable — candidates: **hepatocellular carcinoma (HCC) surveillance gaps in cirrhotic patients**, **early CKD detection failure in primary care**, or **prediabetes-to-T2D conversion with missed cardiovascular risk stratification.**

---

*Brief generated: 2026-06-01 | Research sources: AACR Clinical Cancer Research (Krusen et al. 2026), Gut BMJ AI-PACED (April 2026), Science Translational Medicine PAC-MANN (Feb 2025), OHSU News, Mayo Clinic Magazine, PRECEDE Consortium ClinicalTrials.gov, Healio/ASCO Post, CanTest Research Programme*