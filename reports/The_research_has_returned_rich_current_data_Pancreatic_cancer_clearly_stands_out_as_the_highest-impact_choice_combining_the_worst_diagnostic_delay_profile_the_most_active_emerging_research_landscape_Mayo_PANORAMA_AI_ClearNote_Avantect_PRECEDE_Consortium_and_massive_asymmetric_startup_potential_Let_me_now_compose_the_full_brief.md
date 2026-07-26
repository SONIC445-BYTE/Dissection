The research has returned rich, current data. Pancreatic cancer clearly stands out as the highest-impact choice — combining the worst diagnostic delay profile, the most active emerging research landscape (Mayo PANORAMA AI, ClearNote Avantect, PRECEDE Consortium), and massive asymmetric startup potential. Let me now compose the full brief.

---

## Subject: Daily Early-Diagnosis Brief — Pancreatic Ductal Adenocarcinoma (PDAC) — 2026-07-20

---

### 1) Snapshot (one line)

**Pancreatic Ductal Adenocarcinoma (PDAC)** — why early diagnosis fails in practice: *tumors are biologically silent, radiologically invisible, and screened by a biomarker (CA19-9) that only triggers at late, unresectable stages — by which point 80%+ of patients have metastatic or locally advanced disease.*

---

### 2) Why Early Diagnosis Fails (5 bullets)

- **Biological barrier:** PDAC grows deep in the retroperitoneum with no visceral pain innervation until late invasion; early tumors (<2 cm) do not distort ductal anatomy or produce mass effect visible to the human eye on standard CT; the tumor microenvironment actively suppresses immune signaling that could generate symptoms.
- **Test limitation — CA19-9:** Sensitivity in Stage I/II disease is only ~47–69%; it is falsely negative in ~10% of patients who are Lewis antigen-negative (genetically unable to produce it); it rises meaningfully only at Stage III–IV, making it a staging tool masquerading as a screening tool.
- **Test limitation — Imaging:** Standard abdominal CT (the workhorse of hospital practice) misses visually occult lesions <1.5 cm. Mayo Clinic's 2026 PANORAMA/REDMOD data confirms these tumors were *present but undetected* on prior scans up to **3 years before diagnosis** — a pure human-reader failure, not a technology ceiling.
- **System failure — No population screening policy:** Unlike breast, colon, or cervical cancer, there is no guideline-endorsed general-population screening program for PDAC. High-risk individuals (BRCA2, PALB2, CDKN2A carriers; new-onset diabetes >50 yrs; IPMN patients) are screened inconsistently, and primary care rarely flags the new-onset diabetes → PDAC link.
- **System failure — Referral pathway compression:** Patients with vague epigastric pain, new diabetes, or weight loss undergo serial GI workups (endoscopy, H. pylori treatment, IBS management) before cross-sectional imaging is ordered — median GP-to-specialist delay: **4–6 months** in real-world UK/EU/US data.

---

### 3) Detection Window & Gap

| Milestone | Timepoint / Signal |
|---|---|
| **Earliest detectable signal (research/ideal)** | ctDNA / epigenomic cfDNA at Stage I: ~18–24 months before clinical presentation; CA19-9 elevation detectable up to **2 years** pre-diagnosis in retrospective serum banks (AACR, Lennon et al.) |
| **AI-CT signal (REDMOD/PANORAMA, 2026)** | Visually occult CT features identifiable **up to 3 years** before diagnosis on routine scans — already in the hospital system, unread |
| **Typical clinical detection** | Stage III–IV; median 4–8 months from first symptom to diagnosis; 80–85% of cases unresectable at diagnosis |
| **Gap to close** | **24–36 months** of exploitable pre-diagnostic window; closing it would shift resectability from ~20% → potentially 60–70%, translating to 5-year survival from ~12% → ~40–50% (PRECEDE Consortium target) |

---

### 4) What's Being Used Today (Gold Standard + Emergent)

**Gold Standards:**
- **CA19-9 serum assay** — cheap, widely available, but Stage I sensitivity ~47–69%; not approved for screening
- **CT abdomen/pelvis with contrast** — workhorse imaging; misses occult lesions; radiologist-dependent
- **EUS (Endoscopic Ultrasound)** — gold standard for lesion characterization once suspected; requires specialist, sedation, tertiary center access
- **ERCP** — for biliary obstruction workup; invasive, procedural risk

**Emerging Research / Tools (2024–2026):**

| Tool | Mechanism | Key Data |
|---|---|---|
| **Mayo REDMOD / PANORAMA AI** (Mukherjee et al., *Gut* 2026; *Lancet Oncol* 2025) | Deep-learning CT reader; detects visually occult PDAC | Detects cancer 3 yrs pre-diagnosis; non-inferior to expert radiologists in PANORAMA international study |
| **ClearNote Health — Avantect®** | Epigenomic cfDNA methylation profiling (liquid biopsy) | ASCO 2026 validation data; Stage I/II sensitivity significantly > CA19-9 alone |
| **CancerSEEK → Cancerguard™** (Lustgarten/Exact Sciences) | Multi-analyte: cfDNA + 8 protein biomarkers | ~70% PDAC sensitivity, 99% specificity; evolving to next-gen Cancerguard |
| **Circulating SDF4** (Kageyama et al., *medRxiv* 2025) | Stromal cell-derived factor 4 as plasma biomarker | Early-stage signal; pre-clinical validation ongoing |
| **Protein N-Glycosylation + CA19-9 panel** (Bogdanski et al., *Pancreas* 2025) | Glycoproteomic panel | Combined panel improves early detection AUC vs. CA19-9 alone |
| **ddPCR ctDNA** | Ultra-sensitive mutation detection (KRAS G12D/V) | Detects residual disease missed by NGS; ~48% sensitivity localized, >80% metastatic |
| **Alibaba Damo Panda AI** | CT-based AI, FDA Breakthrough Device designation | Speeds screening in high-volume radiology; commercial pipeline |
| **IMMray™ PanCan-d** (Immunovia) | Serum protein panel; high-risk surveillance | Designed for Stage I/II in familial risk cohorts |

**Main Limitations:** cfDNA tests remain expensive ($800–$2,500/test); ctDNA sensitivity in Stage I is still ~48% (misses half); AI CT tools require validation across diverse scanner protocols; no single test achieves the sensitivity+specificity threshold for general population screening.

---

### 5) Where Healthcare Is Failing (Operational Insight)

- **Screening point that drops the ball:** The **primary care new-onset diabetes workup**. New-onset diabetes after age 50 carries a 1–2% PDAC risk within 3 years — far exceeding general population risk — yet only ~5–8% of these patients receive pancreatic imaging in real-world practice. The signal is already in the EHR; no one is acting on it systematically.
- **Second failure point:** **Radiology reading of incidental abdominal CTs.** PANORAMA/REDMOD data proves PDAC was present on prior scans in a substantial fraction of patients. Radiologists reading CT KUB (kidneys, ureters, bladder) for stones, or CT chest for pulmonary emboli, are not algorithmically prompted to scrutinize the pancreatic parenchyma. This is a **pure workflow gap**, not a technology gap.
- **Bottleneck most fixable in 90 days:** **EHR-based new-onset diabetes (NOD) flagging + automated imaging referral.** An EHR rule triggering a pancreatic protocol CT for patients aged 50+ with new HbA1c ≥6.5% (no prior diabetes) and weight loss ≥5% over 6 months is implementable in a single Epic/Cerner build sprint. This is the single highest-yield, lowest-cost, 90-day operational fix.
- **High-risk population missed:** Patients with **new-onset diabetes + weight loss in community primary care settings** (not academic centers). These patients are diagnosed as T2DM, started on metformin, and followed up in 3 months — with no pancreatic imaging. Meanwhile, PDAC is the cause of diabetes in ~25–30% of these new-onset cases in older adults.

---

### 6) Three High-Leverage Solution Ideas (Practical, Ranked)

---

**🥇 Idea A — EHR-Triggered "PDAC Alert" for New-Onset Diabetes (30-Day Pilot, Hospital)**

*How to run it:*
- Partner with 1 academic medical center's Epic/Cerner team
- Build a **Best Practice Advisory (BPA) alert**: fires for patients aged 50–80, new HbA1c ≥6.5%, BMI change ≥5% in 6 months, no prior diabetes ICD code, no active cancer
- Alert prompts ordering clinician: *"New-onset diabetes in patient >50 with weight loss — consider pancreatic protocol CT to exclude PDAC per PRECEDE/PanCAN guidelines"*
- **Metrics to collect (30–90 days):** Alert fire rate, alert acceptance rate (%), number of pancreatic CTs ordered, PDAC detection yield (per 100 alerts), time-from-alert-to-imaging, false positive rate (benign findings requiring follow-up), clinician override reasons
- **Expected impact:** In a 500-bed hospital, ~200–400 new T2DM diagnoses/year in this age group; if 1–2% harbor PDAC, that's 2–8 early-stage detections per year per hospital — potentially all resectable
- **Cost:** <$15K to build + validate the BPA; near-zero marginal cost per alert

---

**🥈 Idea B — AI "Second-Read" Pancreas Layer on Existing Radiology CT Workflow (60–90 Day Pilot)**

*How to run it:*
- License or pilot-deploy **Mayo REDMOD** or **Alibaba Damo Panda** (both have FDA Breakthrough Device status pathways) as a background inference layer on all abdominal/pelvic CTs read at a high-volume radiology department
- AI flags cases with pancreatic parenchymal atrophy, ductal dilation, or texture anomalies consistent with occult PDAC → radiologist receives structured addendum prompt
- **Resource checklist:** DICOM routing agreement, IRB waiver (QI project), GPU inference server or cloud API contract, radiologist sign-off protocol, 90-day read audit log
- **Metrics:** Number of CT scans processed, AI flag rate (%), radiologist concordance rate, downstream EUS/biopsy conversion, PDAC detection yield vs. historical baseline, turnaround time delta
- **Expected impact:** Based on PANORAMA data — in a center reading 20,000 abdominal CTs/year, AI may flag 50–150 cases warranting pancreatic review; expected yield of 3–10 early-stage PDAC detections that would otherwise be missed
- **Collaborators:** Mayo Clinic AI Lab (REDMOD licensing); Alibaba Health (Damo Panda FDA pathway); institutional radiology QI committee

---

**🥉 Idea C — Prospective Liquid Biopsy + AI-CT Concordance Study in High-Risk Cohort (Research / Startup)**

*Concept:* The field's biggest gap is **prospective validation of combined liquid biopsy + AI-CT** in a pre-symptomatic high-risk population (BRCA2/PALB2 carriers, familial pancreatic cancer, NOD cohort). No study has yet co-enrolled patients for simultaneous cfDNA epigenomics (ClearNote Avantect) + REDMOD AI-CT + CA19-9 with 2-year follow-up.

*How to structure it:*
- Enroll 300–500 high-risk individuals at 3 academic centers (CAPS5 or PRECEDE network sites)
- Annual blood draw (Avantect + CA19-9 + SDF4 panel) + annual pancreatic protocol CT (REDMOD-read)
- Primary endpoint: sensitivity/specificity of combined vs. individual modalities for Stage I/II PDAC detection at 24-month follow-up
- **Tests needed:** IRB, biobank consent, CLIA-certified cfDNA lab, REDMOD API access
- **Collaborators to approach:** PRECEDE Consortium (precedestudy.org), PanCAN Early Detection Initiative, ClearNote Health (co-development), Mayo Clinic AI Lab, NCI EDRN (Early Detection Research Network)
- **Startup angle:** If combined sensitivity reaches >85% at Stage I, this becomes the regulatory package for a **multimodal PDAC screening platform** — the first of its kind. Estimated TAM: $3–5B (US high-risk surveillance market alone)
- **Timeline:** 30-day goal = consortium agreement + IRB submission; 90-day goal = first 50 patients enrolled

---

### 7) First-Principles Signal Hunt (What We Should Measure Earlier)

- **Hidden signal candidate #1 — Pancreatic exocrine dysfunction markers in stool/blood:** PDAC compresses the pancreatic duct early, reducing exocrine enzyme secretion months before tumor mass is visible. Fecal elastase-1 (FE-1) and serum trypsinogen-2 drop measurably in early PDAC. These are cheap, non-invasive, and almost never ordered in the pre-diagnostic workup. *This is an underexplored, low-cost early signal.*
- **Hidden signal candidate #2 — Host transcriptomic shift in peripheral blood:** PDAC induces a systemic inflammatory/immunosuppressive transcriptomic signature in circulating monocytes and NK cells detectable by blood RNA-seq before imaging positivity. Early data from PCDC suggests a 15-gene blood expression panel distinguishes early PDAC from benign pancreatic disease with AUC ~0.84.
- **Hidden signal candidate #3 — Gut microbiome dysbiosis:** Distinct oral and gut microbiome signatures (Porphyromonas gingivalis, Fusobacterium nucleatum enrichment; Bifidobacterium depletion) precede PDAC diagnosis by 1–2 years in prospective cohort data. Stool microbiome profiling is non-invasive and scalable.
- **Minimal sampling change needed:** A single **add-on blood tube** at the time of new diabetes diagnosis (for cfDNA + trypsinogen-2 + CA19-9 + SDF4) requires zero additional patient visits. This is a **zero-friction sampling upgrade** to an existing clinical touchpoint.

---

### 8) Strategic Value & Next Immediate Actions (CEO Lens)

**Public Health Impact:**
- ~500,000 new PDAC cases/year globally; ~60,000 in the US alone
- 5-year survival: **~12%** overall; **~42%** if caught at Stage I (but only ~10–15% are caught at Stage I)
- PDAC is projected to become the **2nd leading cause of cancer death** in the US by 2030
- Economic burden: $4.9B direct annual US healthcare costs; enormous indirect burden from working-age deaths (median diagnosis age: 70, but rising incidence in 40–60 age group)
- Asymmetric opportunity: **A technology that shifts Stage I detection rate from 15% → 40%** would save ~18,000 US lives/year and generate enormous clinical + commercial value

**3 Immediate Actions for Ayan:**

| Timeline | Action |
|---|---|
| **Today** | Pull and read: Mukherjee et al., *Gut* 2026 (REDMOD AI) + PANORAMA study, *Lancet Oncology* 2025 — these two papers define the current AI-CT state of the art and the implementation blueprint |
| **7 Days** | Contact PRECEDE Consortium (precedestudy.org) and PanCAN's Early Detection Initiative to understand current open collaboration/co-investigator slots; simultaneously request a pilot demo of ClearNote Health's Avantect cfDNA platform |
| **30 Days** | Spec out the **EHR-BPA alert pilot** (Idea A) with one institutional partner — draft the Epic/Cerner logic, identify a clinical champion in endocrinology or GI, and submit as a QI project (no full IRB needed); simultaneously draft a 1-page concept note for the multimodal concordance study (Idea C) for NCI EDRN R01 or PanCAN grant cycle |

---

### 9) One-Minute Mental Model

> *"PDAC hides by being retroperitoneal, silent, and pre-symptomatic for 3+ years — but it leaves three traceable footprints during that window: it disrupts exocrine function (measurable in blood/stool), it sheds cfDNA into plasma (detectable by epigenomic profiling), and it leaves subtle parenchymal texture changes on CT scans (readable by AI but invisible to human radiologists). The single highest-leverage point is the new-onset diabetes clinical encounter at age 50+ — where all three signals are already accessible but no one is looking."*

**Search keywords / paper lookups:**
1. `Mukherjee S et al. "Next-generation AI for visually occult pancreatic cancer detection" Gut BMJ 2026` — REDMOD validation
2. `PANORAMA study Lancet Oncology 2025 — Alves N et al. AI vs radiologist pancreatic cancer CT`
3. `PRECEDE Consortium pancreatic cancer early detection 2025 — precedestudy.org` + `Lennon AM et al. CA19-9 upregulated 2 years pre-diagnosis Clin Cancer Res`

---

### 10) Pattern Insight (Meta-Learning)

**Recurring diagnostic failure pattern reinforced today:**

> 🔁 **"The Latent Signal / Wrong Touchpoint" Pattern**

This is the third consecutive disease class (after neurodegenerative pre-clinical stages and endometriosis) where the core failure is *not* a missing biomarker — **the signal exists and is detectable** — but it is being sought at the wrong clinical touchpoint, too late, by the wrong specialist, using the wrong test order logic.

In PDAC:
- The **CT signal** exists 3 years early — but radiology workflows don't prompt pancreatic scrutiny on non-pancreatic scans
- The **diabetes signal** exists 1–2 years early — but endocrinology/GP workflows treat it as metabolic disease, not a cancer flag
- The **cfDNA signal** exists 18–24 months early — but liquid biopsy is ordered post-diagnosis, not pre-symptomatically

**Generalizable opportunity forming:**
The cross-disease pattern is clear: **the bottleneck is not biomarker discovery — it is signal routing.** The highest-leverage platform play across PDAC, Alzheimer's, endometriosis, and rare diseases is a **clinical decision intelligence layer** that sits inside EHR workflows and reroutes existing clinical signals (lab values, imaging findings, symptom clusters) to the right diagnostic pathway at the right time. This is a **workflow AI** problem, not a biomarker science problem — and it is fundable, pilotable in 90 days, and applicable across 10+ disease areas.

> 🔑 **Meta-principle:** *"The diagnostic gap is not in the lab. It's in the routing logic between the signal that already exists and the specialist who needs to act on it."*

---
*Brief generated: 2026-07-20 | Sources: Mukherjee et al. Gut 2026 · PANORAMA Lancet Oncol 2025 · PRECEDE Consortium · ClearNote Health ASCO 2026 · Bogdanski et al. Pancreas 2025 · Kageyama et al. medRxiv 2025 · de Leon Pisani et al. ScienceDirect 2025 · PanCAN Early Detection Initiative · PCDC Biomarker Bakeoff AACR*