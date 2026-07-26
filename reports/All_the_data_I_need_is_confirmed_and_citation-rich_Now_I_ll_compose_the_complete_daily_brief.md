All the data I need is confirmed and citation-rich. Now I'll compose the complete daily brief.

---

## Subject: Daily Early-Diagnosis Brief — Pancreatic Ductal Adenocarcinoma (PDAC) — 2026-06-26

---

### 1) Snapshot (one line)

**Pancreatic Ductal Adenocarcinoma (PDAC)** — why early diagnosis fails in practice: the tumor is radiologically invisible and symptomatically silent during its only curable window, while the sole approved biomarker (CA 19-9) is both biologically inaccessible to ~15% of patients and clinically insensitive at Stage I, leaving >80% of cases discovered only after metastasis.

---

### 2) Why Early Diagnosis Fails (3–5 bullets)

- **Biological barrier:** PDAC sheds minimal circulating tumor DNA (ctDNA) in early stages; the pancreatic parenchyma masks structural changes on standard CT for 12–16 months before clinical detection; early symptoms (weight loss, back pain, new-onset diabetes) are non-specific and attributed to commoner conditions.
- **Test limitation:** CA 19-9 has only ~64% sensitivity at Stage I and is completely unproducible in 10–15% of the population (Lewis blood group antigen-negative individuals); standard CT misses early pancreatic masses in **38–48%** of cases that are later confirmed as PDAC; first-generation multi-cancer early detection (MCED) liquid biopsies (e.g., Galleri) achieve only ~55.6% sensitivity for Stage I PDAC.
- **System failure:** New-onset diabetes (NOD) in patients >50 — present in ~25% of PDAC patients 6–36 months before diagnosis — is universally managed as a standalone metabolic disorder, not as a potential paraneoplastic red flag; there is no systematic EHR-based reflex screening trigger.
- **Screening policy gap:** No population-level screening program exists for PDAC. High-risk genetic carriers (BRCA2, PALB2, ATM) without documented family history of PDAC are often excluded from surveillance protocols under current conditional ASGE/NCCN guidelines.
- **Surveillance fatigue:** IPMN (Intraductal Papillary Mucinous Neoplasm) follow-up programs suffer high patient dropout because most IPMNs never progress — yet malignant transformation within an IPMN is nearly indistinguishable on standard imaging, creating a dangerous false-security loop.

---

### 3) Detection Window & Gap (concise)

| Marker | Timepoint |
|---|---|
| **Earliest detectable signal (research/ideal)** | Molecular/radiomics signal on pre-diagnostic CT: **~386–475 days (12–16 months)** before clinical diagnosis; multi-omic liquid biopsy signals emerging at pre-Stage I in trial settings |
| **Typical clinical detection** | Symptomatic presentation → diagnosis: **Stage III/IV in >80% of cases**; average treatment delay after first symptom: **~3 months** due to 31% initial misdiagnosis rate |
| **Gap to close** | **12–16 months** of actionable pre-diagnostic signal exists on routine imaging TODAY — it is simply invisible to the human eye. Closing this gap via AI second-read or liquid biopsy reflex protocols could shift a meaningful fraction of diagnoses from Stage IV (3.2% 5-year survival) to Stage I/II (>30% 5-year survival), representing a **~10× survival multiplier** at the individual patient level |

---

### 4) What's Being Used Today (Gold Standard + Emergent)

**Gold Standards:**
- **CA 19-9 serum biomarker** — sensitivity ~64% at Stage I; useless in Lewis antigen-negative patients (~15% of population); elevated in benign biliary obstruction (poor specificity)
- **Contrast-enhanced CT / MRI abdomen** — primary imaging modality; misses 38–48% of early-stage tumors; radiologist sensitivity for visually occult PDAC: ~38.9%
- **Endoscopic Ultrasound with Fine Needle Aspiration (EUS-FNA)** — gold standard for tissue confirmation but requires specialist referral; only deployed after suspicion is already raised; not scalable for screening

**Emerging Research / Tools:**
| Tool | Type | Key Performance |
|---|---|---|
| **REDMOD (Mayo Clinic / AI-PACED consortium)** | AI radiomics on standard CT | 73% sensitivity for pre-diagnostic PDAC at median 16 months before diagnosis; **nearly doubles** radiologist sensitivity (73% vs. 38.9%, p<0.001); validated externally *(Gut BMJ, April 2026)* |
| **Avantect® (ClearNote Health)** | Multi-omic cfDNA blood test | 82.6% overall sensitivity; **76.8% sensitivity at Stage I/II**; 97.5% specificity; presented at ASCO 2026 & AACR 2026 |
| **Multi-omic liquid biopsy (ASCO 2025 dataset)** | RNA + methylation + cfDNA + ML | 92% sensitivity (52% specificity) — stage-agnostic in early trial data; NCI CDAS project reports 93% sensitivity for Stage I/II in 73-patient cohort |
| **ENDPAC Score (EHR-integrated)** | Clinical risk algorithm | Enriches NOD patients for PDAC screening; 5-fold risk elevation in NOD >50 within 3-year window |
| **miRNA expression panels** | Non-invasive blood biomarker | Actively studied; non-invasive; not yet clinically validated at scale |

**Main Limitations:**
- REDMOD: Not yet FDA-cleared; requires CT infrastructure and AI integration pipeline; trained on specific Mayo cohort — external generalizability being validated
- Avantect: ~$950–$1,000 out-of-pocket; not yet covered by major payers; laboratory-developed test (LDT) regulatory pathway
- Multi-omic panels: Specificity remains a challenge (52% in some datasets); clinical-grade validation in prospective cohorts pending
- All liquid biopsies: Low ctDNA shedding in early PDAC remains a fundamental biological hurdle

---

### 5) Where Healthcare Is Failing (Operational Insight)

- **Screening point that drops the ball:** The **primary care encounter for new-onset diabetes in patients >50** is the single highest-leverage missed opportunity. A patient presenting with NOD + mild weight loss has a ~5-fold elevated 3-year PDAC risk, yet the standard workflow sends them to endocrinology for glucose management — with zero pancreatic imaging or biomarker reflex.
- **Radiology workflow failure:** Abdominal CTs ordered for vague GI complaints or back pain are read by generalist radiologists without AI assistance. The result: 38–48% of early PDAC masses are missed on the very scan that could have caught them 12–16 months before clinical diagnosis. Even specialist radiologists achieve only 38.9% sensitivity for visually occult disease.
- **Bottleneck most fixable in 90 days:** **EHR-triggered ENDPAC score + reflex CA 19-9 + targeted pancreatic protocol MRI** for all patients >50 with new-onset diabetes. This is a pure workflow intervention — no new technology required, implementable via EHR rule engine in a single health system within 60–90 days.
- **High-risk population missed:** **Lewis antigen-negative patients** (10–15% of population) — CA 19-9 is biologically non-functional for them, yet they receive no alternative biomarker workup. Additionally, **BRCA2/PALB2/ATM carriers without family history** are excluded from surveillance under conditional guideline language, leaving a genetically defined high-risk cohort unscreened.

---

### 6) 3 High-Leverage Solution Ideas (Practical, Ranked)

**🥇 Idea A — EHR-Based NOD Reflex Screening Protocol (30–60 day pilot)**
- **What:** Build an EHR clinical decision support (CDS) rule that auto-flags all patients aged >50 with new-onset diabetes (HbA1c ≥6.5% or fasting glucose ≥126 mg/dL, no prior DM diagnosis) + any one of: weight loss >5%, vague abdominal/back pain, or elevated amylase/lipase. Trigger: automatic ENDPAC score calculation + reflex order for CA 19-9 + pancreatic protocol MRI if ENDPAC ≥3.
- **How to run the pilot:** Partner with a single academic health system's endocrinology + primary care network. Implement CDS rule in Epic/Cerner. Run for 60 days on all qualifying new encounters.
- **Metrics to collect:** (1) Number of patients flagged/week; (2) % who complete reflex imaging; (3) PDAC detection rate in flagged vs. unflagged NOD cohort; (4) Stage at detection; (5) Time-from-flag-to-diagnosis; (6) False positive rate (unnecessary imaging burden).
- **Expected impact:** Captures the ~25% of PDAC patients who have a 6–36 month pre-diagnostic diabetes window. Even a 10% pickup rate in this cohort shifts diagnoses earlier.

---

**🥈 Idea B — AI Second-Read (REDMOD-Style) Overlay for High-Risk Abdominal CTs (60–90 day pilot)**
- **What:** Deploy an AI radiomics second-read tool (REDMOD framework or equivalent) as a background overlay on all abdominal/chest CTs ordered for patients with ≥1 PDAC risk factor (NOD, family history, IPMN on record, BRCA2/PALB2/ATM carrier status, chronic pancreatitis, smoker >20 pack-years). AI flags scans with anomalous pancreatic texture → radiologist review alert.
- **Resource checklist:**
  - [ ] IRB approval for retrospective validation on existing CT archive
  - [ ] IT/PACS integration for AI overlay (DICOM-compatible API)
  - [ ] Radiology department buy-in (champion radiologist)
  - [ ] Risk-stratification EHR flag to trigger AI second-read
  - [ ] Outcome tracking dashboard (flag → biopsy → pathology)
- **Expected impact:** REDMOD achieves 73% sensitivity vs. 38.9% for radiologists — nearly doubling early detection in the highest-risk imaging pool. In a system reading 500 abdominal CTs/month with 5% high-risk flag rate, this could surface 1–2 additional early-stage cases per month that would otherwise be missed for 12–16 months.

---

**🥉 Idea C — Multi-Omic Liquid Biopsy + ENDPAC Enrichment Study (Research/Product, 90-day setup)**
- **What:** Design a prospective enrichment study pairing the ENDPAC score (to select highest-risk NOD patients) with a blood draw for Avantect® or equivalent multi-omic cfDNA test. This creates a staged, cost-effective screening funnel: ENDPAC score (free, EHR-derived) → Avantect ($950 blood test, ordered only for high-scorers) → EUS-FNA confirmation.
- **Tests needed:** Prospective cohort of 200–300 ENDPAC-high NOD patients; 12-month follow-up; primary endpoint: PDAC detection rate and stage at detection vs. matched historical controls.
- **Collaborators to approach:** Mayo Clinic AI-PACED consortium (Dr. Sovanlal Mukherjee); ClearNote Health (Avantect partnership for discounted research pricing); NCI Early Detection Research Network (EDRN); PanCAN's Precision Promise network.
- **Highest upside:** Validates a two-stage, cost-gated screening funnel that could become the first evidence-based PDAC early detection protocol scalable to primary care — and forms the clinical evidence base for a startup or spinout.

---

### 7) First-Principles Signal Hunt (What We Should Measure Earlier)

- **Hidden signal candidate:** **Pancreatic texture radiomics on routine abdominal CT** — subtle parenchymal density changes and ductal irregularities are present 12–16 months before visible tumor formation and are quantifiable by AI but invisible to the human eye. Secondary candidate: **plasma methylation signatures** (cell-free methylome) which reflect epigenetic silencing of tumor suppressor genes in PDAC precursor cells — detectable before ctDNA shedding becomes measurable.
- **Third candidate:** **Fasting C-peptide + insulin resistance trajectory** in NOD patients — the rate of beta-cell dysfunction (not just absolute glucose) may encode a PDAC-specific metabolic signature distinguishable from Type 2 DM, measurable from standard metabolic panels already ordered in primary care.
- **Minimal sampling change needed:** No new sample type required. Blood (already drawn for HbA1c/glucose in NOD workup) is sufficient for CA 19-9 reflex + cfDNA add-on. Routine abdominal CT (already ordered for GI complaints) is sufficient for AI radiomics overlay. Zero new patient touchpoints — pure workflow and algorithmic augmentation.

---

### 8) Strategic Value & Next Immediate Actions (CEO Lens)

**Public health impact:**
- **67,530** new PDAC diagnoses estimated in the US in 2026; **~52,740 deaths** — 3rd leading cause of cancer death
- 5-year survival rate: **13% overall; 3.2% at Stage IV; >30% at Stage I/II**
- Only **10–15%** of patients are currently diagnosed at a resectable stage
- Global incidence rising ~1% per year; median age at diagnosis: 70; but NOD-associated cases skew younger and are systematically missed
- Asymmetric startup value: a tool that shifts even 15% of diagnoses from Stage IV → Stage I/II is worth billions in QALYs and is commercially defensible (no FDA-cleared competitor exists for population-level PDAC screening)

**3 Immediate Actions for Ayan:**

| Timeline | Action |
|---|---|
| **Today** | Read the landmark REDMOD validation paper: *"Next-generation AI for visually occult pancreatic cancer detection in standard CT"* — Gut BMJ, April 2026 (gut.bmj.com/content/early/2026/04/22/gutjnl-2025-337266). Map the AI pipeline architecture — understand what data inputs REDMOD uses and whether your institution's CT archive is compatible. |
| **7 days** | Contact the Mayo Clinic AI-PACED consortium (PI: Sovanlal Mukherjee, PhD) and ClearNote Health's clinical partnerships team. Frame the conversation around a joint NOD-enriched liquid biopsy + AI imaging pilot. Simultaneously, pull your institution's EHR data: How many patients >50 were diagnosed with new-onset diabetes in the last 24 months? What % received any pancreatic imaging? This is your baseline gap metric. |
| **30 days** | Draft a 1-page pilot protocol: *"EHR-triggered ENDPAC + Avantect reflex screening in new-onset diabetes patients >50"* — specify inclusion criteria, EHR rule logic, biomarker reflex pathway, imaging protocol, and primary endpoint (PDAC detection rate at Stage I/II). Submit for IRB pre-review and present to your GI/oncology department as a quality improvement initiative. |

---

### 9) One-Minute Mental Model

> *"PDAC hides inside a 16-month window of radiological silence and metabolic camouflage — the tumor is molecularly present but visually absent on CT, while its earliest symptom (new-onset diabetes) is being treated as a metabolic problem rather than a cancer signal. The single leverage point: intercept the new-onset diabetes encounter in primary care and reflex it into a pancreatic screening pathway — because the cancer is already there, we just haven't looked."*

**2–3 immediate literature/search keywords:**
1. **`"REDMOD" pancreatic cancer AI Gut BMJ 2026`** — for the landmark AI validation paper
2. **`"ENDPAC score" new-onset diabetes pancreatic cancer screening`** — for the EHR-implementable risk enrichment algorithm
3. **`"Avantect" ClearNote Health ASCO 2026 sensitivity Stage I`** — for the most advanced cfDNA liquid biopsy performance data

---

### 10) Pattern Insight (Meta-Learning)

**Recurring diagnostic failure pattern identified:** This brief reinforces what is emerging as the **"Symptom Camouflage + Biomarker Floor" pattern** — a recurring dual failure seen across multiple high-mortality diseases:

| Disease | Camouflage mechanism | Biomarker floor failure |
|---|---|---|
| PDAC (today) | NOD treated as metabolic, not paraneoplastic | CA 19-9 insensitive at Stage I; absent in 15% |
| Ovarian cancer | Bloating/GI symptoms attributed to IBS | CA-125 non-specific; no Stage I screen |
| ATTR amyloidosis | Carpal tunnel/HF attributed to aging | No routine biomarker screen in primary care |
| ALS (prior pattern) | Fasciculations attributed to anxiety/fatigue | No blood biomarker approved for presymptomatic phase |

**What's generalizing:** In every case, the earliest biological signal exists — but it is either (a) misread as a benign condition at the primary care encounter, or (b) falls below the sensitivity floor of the available biomarker. The fixable intervention is consistently **not a new biomarker** — it's a **workflow rule that recontextualizes an existing clinical signal** (NOD → PDAC risk; carpal tunnel → ATTR risk; fasciculations → ALS risk) and triggers a reflex diagnostic pathway.

**Asymmetric opportunity forming:** The generalizable product opportunity across all these diseases is an **EHR-native clinical decision support engine** that pattern-matches existing routine data (labs, vitals, diagnoses, prescriptions) to flag patients in the pre-diagnostic window — disease-agnostic, zero new sample types, deployable in 30–90 days per disease module. This is the meta-platform hiding inside each individual disease brief.

---
*Brief generated: Friday, June 26, 2026 | Sources: Gut BMJ (April 2026), Mayo Clinic News Network (May 2026), ClearNote Health ASCO 2026, ASCO JCO 2025, PanCAN 2026, NCI SEER, PMC/NIH literature*