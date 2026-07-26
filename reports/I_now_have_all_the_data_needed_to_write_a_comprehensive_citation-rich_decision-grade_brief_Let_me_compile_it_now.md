I now have all the data needed to write a comprehensive, citation-rich, decision-grade brief. Let me compile it now.

---

**Subject: Daily Early-Diagnosis Brief — Pancreatic Ductal Adenocarcinoma (PDAC) — 2026-07-04**

---

## 1) Snapshot (one line)

**Pancreatic Ductal Adenocarcinoma (PDAC)** — why early diagnosis fails in practice: The pancreas is morphologically normal on standard imaging during its entire curable preclinical phase, and no validated population-level screening test exists, so 85%+ of cases are diagnosed at an unresectable stage where only palliation is possible.

---

## 2) Why Early Diagnosis Fails (3–5 bullets)

- **Biological barrier:** PDAC is a "low-shedder" — its dense desmoplastic stroma physically impedes ctDNA release into blood; the pancreas shows zero macroscopic imaging changes during stage 0 disease ("imaging-occult" state), meaning even expert radiologists miss ~61% of pre-diagnostic scans on re-review. CA 19-9 is not produced at all in 5–10% of patients (Lewis-negative genotype, le/le).

- **Test limitation:** CA 19-9 has a PPV of only 0.5–0.9% in asymptomatic populations, making it useless as a screening tool. ctDNA alone detects only ~30% of resectable PDACs. Endoscopic ultrasound (EUS) — the most sensitive imaging modality — is invasive, expensive, operator-dependent, and not scalable. No single biomarker clears the sensitivity + specificity bar needed for sporadic population screening.

- **System failure:** No established population-level screening program exists for sporadic PDAC (85–90% of all cases). High-risk surveillance programs (BRCA, CDKN2A carriers) catch only 10–15% of the PDAC burden. New-onset diabetes (NOD) — a validated 3-year risk signal at ~3.6%, nearly 20× the general population — is routinely missed in primary care as a trigger for imaging. Routine abdominal CTs ordered for unrelated reasons (the largest incidental opportunity) are read by radiologists who detect only 39% of occult pre-diagnostic lesions.

- **Operational failure:** Median diagnostic delay from symptom onset to confirmed diagnosis is **2 months** (IQR 1–5 months; up to 25% of patients wait >6 months). But the deeper problem is the pre-symptomatic window — the cancer is biologically detectable on CT up to 3 years before any symptom, yet no triage system captures this.

- **Awareness gap:** Vague presenting symptoms (back pain, new-onset fatigue, indigestion, unexplained weight loss) are attributed to benign causes by primary care. Median number of GP visits before referral: 3–4. Symptom-to-referral delay accounts for the bulk of the diagnostic gap.

---

## 3) Detection Window & Gap (concise)

| Stage | Earliest Detectable Signal | Typical Clinical Detection | Gap |
|---|---|---|---|
| Imaging-occult (Stage 0) | CT radiomic signal: **475 days** (median) before diagnosis — REDMOD AI, *Gut* 2026 | Symptomatic presentation, Stage III/IV | **~13–16 months of lost lead time** |
| Liquid biopsy (ctDNA) | Multi-analyte panels (ctDNA + protein + methylation): Stage I/II sensitivity ~64% | Stage III/IV (80%+ of cases at Dx) | **~2–4 years of missed window** |
| CA 19-9 elevation | Detectable up to 2 years pre-diagnosis in some patients | Used only after symptoms trigger imaging | **12–24 months of unused signal** |
| NOD as risk signal | New-onset diabetes precedes PDAC by median **~8 months** (ENDPAC score ≥3 = 20× risk) | Rarely triggers pancreatic imaging in primary care | **6–12 months actionable window routinely ignored** |

**Gap to close:** 13–24 months of clinically actionable but operationally abandoned pre-diagnostic window. At Stage I, 5-year survival is ~40%. At Stage IV (current median presentation), it is ~3%. Closing this gap by even 6 months at scale would represent tens of thousands of lives annually.

---

## 4) What's Being Used Today (Gold Standard + Emergent)

**Gold Standards:**
- **Contrast-enhanced CT / MRI:** First-line imaging — but detects only macroscopic masses; misses imaging-occult stage 0 disease entirely
- **Endoscopic Ultrasound (EUS) ± FNA:** Most sensitive imaging modality for small lesions; gold standard for tissue diagnosis — but invasive, operator-dependent, not scalable
- **CA 19-9 serum marker:** Sensitivity 79–81%, specificity 82–90% in *symptomatic* patients; PPV <1% in asymptomatic populations; fails completely in Lewis-negative patients (5–10% of population)
- **ERCP:** For biliary obstruction workup; diagnostic but procedural risk

**Emerging Research / Tools (2025–2026):**

| Tool | Mechanism | Performance | Status |
|---|---|---|---|
| **REDMOD** (Mayo Clinic / *Gut* 2026) | CT radiomic AI — 40-feature wavelet-texture ensemble (LR + RF + XGBoost) | Sensitivity 73% vs radiologist 39% (p<0.001); AUC 0.82; 475-day median lead time; specificity 81–88% across institutions | Externally validated; ready for prospective high-risk cohort trials |
| **ExoVita™ Pancreas Assay** | Blood-based 7-protein extracellular vesicle/exosome classifier | Sensitivity **90%**, specificity 92.8% for Stage I/II PDAC vs healthy controls | Independent validation published (*Nature*); complements CA 19-9 especially in Lewis-negative patients |
| **ClearNote Health Avantect®** (Enhanced) | cfDNA 5-hydroxymethylcytosine (5hmC) + genomic + glycan markers + ML | Overall sensitivity 82.6%, specificity 97.5%; Stage I/II sensitivity **76.8%** | Validated in EpiDetect Study (NCT05188573); $52M raised; presented at ASCO 2026 |
| **Multi-analyte ctDNA panels** | ctDNA mutations + protein markers (TIMP1/LRG1) + methylation | Stage I/II sensitivity ~64%, specificity 99.5% | Research phase; CHIP interference remains key technical challenge |
| **ENDPAC + EHR-based NOD flagging** | Algorithmic risk scoring in new-onset diabetes patients in EHR | 3-year PDAC risk ~3.6% (20× baseline) in ENDPAC ≥3 | PanCAN EDI trial (NCT04662879): 8,800+ enrolled, now in follow-up phase |
| **Mayo Clinic Deep Learning CT AI** | Deep learning on routine abdominal CT | Detects signs up to **3 years** before diagnosis | Landmark validation study published April 2026 |

**Main Limitations:**
- REDMOD: needs prospective validation in true screening (not retrospective) cohorts; no cost-effectiveness data yet
- ExoVita: validated vs healthy controls, not vs benign pancreatic disease (the harder clinical challenge)
- Avantect: EpiDetect trial still in follow-up; real-world PPV in general population unknown
- ctDNA: low shedding + CHIP noise = high false negative/positive rates at early stages
- All liquid biopsies: performance drops significantly when benchmarked against chronic pancreatitis or IPMN (the real differential)

---

## 5) Where Healthcare Is Failing (Operational Insight)

**Screening point that drops the ball:**
> Primary care encounters with new-onset diabetes, unexplained weight loss, or new back pain — the 3 highest-prevalence PDAC prodromal signals — trigger zero pancreas-specific workup in >95% of cases. EHRs contain this data but no automated alert fires. NICE now recommends urgent imaging for age ≥60 + new-onset diabetes + weight loss, but real-world compliance is minimal.

**Bottleneck most fixable in 90 days:**
> **EHR-based ENDPAC score auto-calculation + automated imaging referral trigger for new-onset diabetes patients.** This requires no new test — only an EHR rule engine querying existing labs (fasting glucose, HbA1c, weight trend, age). This is a pure workflow fix that can be piloted in any hospital with an Epic/Cerner system in 30–60 days.

**High-risk population missed:**
- **Sporadic PDAC patients** (85–90% of all cases) — no surveillance program exists for them; only hereditary/familial cohorts (BRCA2, CDKN2A, STK11) get any surveillance
- **Lewis-negative patients** — CA 19-9 is biologically uninformative; labs don't routinely test Lewis antigen status before ordering CA 19-9, creating false reassurance
- **New-onset diabetes in 50–80 year-olds** — the single most scalable risk-enrichment strategy, but primary care is not trained to recognize this as a PDAC signal
- **Patients with incidental abdominal CTs** — millions of CTs are read annually for other indications; REDMOD-class AI deployed on this stream would represent the largest early detection opportunity in oncology

---

## 6) Three High-Leverage Solution Ideas (Practical, Ranked)

### 🥇 Idea A — EHR-Based ENDPAC Auto-Flag + Imaging Reflex (30-day pilot, highest ROI)

**What:** Build an automated EHR alert (Epic/Cerner CDS rule) that calculates ENDPAC score in real-time for any patient newly coded with T2DM or pre-diabetes (ICD-10: E11.x, E09.x) aged 50–80. If ENDPAC ≥3, auto-generate a "Pancreatic Cancer Risk Flag" that recommends abdominal CT or EUS within 3 months.

**How to run the 30–90 day pilot:**
- Site: 1 academic medical center with Epic + active endocrinology/primary care volume
- Build: Epic CDS Hooks rule (ENDPAC = weight loss % + fasting glucose delta + age); ~2 weeks IT build
- Trigger: Flag fires on any new diabetes diagnosis; routes to ordering PCP with a soft alert + 1-click CT order
- Metrics to collect:
  - Alert fire rate (expected: 3–8% of new DM diagnoses)
  - Imaging compliance rate (% who get CT within 90 days of flag)
  - PDAC detection yield (cases found per 1,000 flagged)
  - False positive rate (benign findings requiring follow-up)
  - Time-to-diagnosis vs historical baseline
- Expected impact: In a hospital diagnosing 500 new DM cases/month, 15–40 ENDPAC ≥3 patients flagged; expected PDAC yield ~1–3 cases/quarter at earlier stage than standard care

**Resource checklist:** Epic analyst (1 FTE, 3 weeks), gastroenterology co-champion, IRB approval for data collection, baseline audit of current imaging rates in NOD patients

---

### 🥈 Idea B — REDMOD AI Deployment on Existing Routine CT Queue (60–90 day pilot)

**What:** Deploy REDMOD (or a locally trained equivalent) as a background AI layer on all abdominal/chest-abdomen-pelvis CTs already ordered for non-pancreatic indications. Any CT flagged as high-risk by REDMOD triggers a structured radiologist second-read protocol.

**How to run:**
- Partner with Mayo Clinic Platform or license REDMOD pipeline (open-access methodology published in *Gut* 2026; code available on request per paper's data availability statement)
- Run retrospectively first: pull 2–3 years of abdominal CTs from patients who subsequently developed PDAC; validate local sensitivity before prospective deployment
- Prospective phase: REDMOD runs in background; flags generate a "Pancreatic Incidentaloma Protocol" — dedicated radiologist review + structured report + automatic 6-month follow-up CT scheduling
- Metrics: sensitivity vs radiologist alone, false positive rate (downstream imaging burden), lead time gain vs historical PDAC cases, cost per case detected
- **Expected impact:** Based on REDMOD data — nearly doubles sensitivity (73% vs 39%) at a median 475-day lead time. In a hospital reading 50,000 abdominal CTs/year, this could intercept 2–5 additional stage I/II PDACs annually vs current standard.

**Key collaborators to approach:** Ajit Goenka (Mayo Clinic, REDMOD PI — goenka.ajit@mayo.edu), NHS England (NICE already recommends urgent imaging in NOD + weight loss — REDMOD slots directly into this pathway)

---

### 🥉 Idea C — Multi-Analyte Liquid Biopsy Panel for NOD Cohort Stratification (Research/Product, Highest Upside)

**What:** Design a prospective biomarker study combining ENDPAC-flagged NOD patients with a multi-analyte blood test (ExoVita 7-protein EV panel + Avantect 5hmC cfDNA + CA 19-9 with Lewis antigen genotyping) to build a composite risk score that triages who needs immediate EUS vs 6-month CT vs routine follow-up.

**Why this is the highest-upside play:** The NOD cohort is the only validated, scalable, risk-enriched population for sporadic PDAC screening. A blood test that can stratify within this cohort (3.6% base risk → identify the 20–30% with >15% 3-year risk) would be the first commercially viable PDAC screening product.

**Tests needed:**
- Prospective cohort: 500–1,000 ENDPAC ≥3 patients with serial blood draws at 0, 6, 12, 24 months
- Endpoints: PDAC diagnosis, stage at diagnosis, imaging findings
- Biomarkers: CA 19-9 + Lewis antigen genotype + ExoVita EV panel + 5hmC cfDNA (Avantect) + plasma THBS2/ALPPL2

**Collaborators to approach:**
- PRECEDE Consortium (precedestudy.org) — already biobanking HRI samples; partner for biomarker sub-study
- ClearNote Health (EpiDetect NCT05188573) — already doing exactly this; approach for data-sharing or co-enrollment
- PanCAN Early Detection Initiative (NCT04662879, 8,800+ enrolled, now in follow-up) — approach for biomarker sub-study access

**Startup angle:** A company that owns the NOD-stratification liquid biopsy IP and validates it in PRECEDE data has a clear regulatory path (LDT → PMA) and a captive buyer market (endocrinologists, gastroenterologists, primary care). Comparable to Exact Sciences' Cologuard model — a single-indication, risk-enriched screening test.

---

## 7) First-Principles Signal Hunt (What We Should Measure Earlier)

**Hidden signal candidates:**

1. **Pancreatic CT radiomic texture change (REDMOD-class features):** 90% of REDMOD's predictive power comes from multi-scale wavelet-filtered textural features — not visible masses. These reflect subvisual fibrotic/inflammatory architectural disruption in the pancreatic parenchyma. This signal is present at median 475 days pre-diagnosis and is longitudinally stable (90–92% test-retest concordance). *This is the most underutilized signal in oncology today* — it exists in millions of already-acquired CTs and is being discarded.

2. **Plasma THBS2 + ALPPL2 (exosome surface proteins):** THBS2 (thrombospondin-2) and ALPPL2 (alkaline phosphatase placental-like 2) are shed on cancer-derived exosome surfaces and can differentiate PDAC from benign pancreatic cysts with high specificity — a critical clinical gap where CA 19-9 fails completely.

3. **5-Hydroxymethylcytosine (5hmC) in cfDNA:** An epigenetic mark on cell-free DNA that reflects tissue-of-origin gene regulation. PDAC-specific 5hmC patterns are detectable in blood before morphological changes — the basis of Avantect. Unlike mutation-based ctDNA, 5hmC is not confounded by CHIP.

4. **ENDPAC score as a triage gate (not a biomarker but a risk signal):** Fasting glucose delta + weight loss % + age — calculable from EHR data alone, no new test needed. Currently ignored in 95%+ of primary care settings.

**Minimal sampling change needed:** Standard venous blood draw (5–10 mL) for liquid biopsy; no new collection protocol required. For REDMOD, no new imaging — it runs on existing routine abdominal CTs already in PACS.

---

## 8) Strategic Value & Next Immediate Actions (CEO Lens)

**Public health impact:**
- ~500,000 new PDAC cases globally per year; ~470,000 deaths annually (near 1:1 incidence-to-mortality ratio)
- 5-year survival: 13% overall (US, PanCAN 2025); <7% globally; <3% at Stage IV
- Stage I 5-year survival: ~40%; Stage II: ~20% — the stage-shift imperative is enormous
- PDAC is projected to become the 2nd leading cause of cancer death in the US by 2030
- Economic burden: $5.3B annually in US direct costs; immense indirect burden from working-age mortality

**3 Immediate Actions for Ayan:**

> **Today (July 4, 2026):**
> Read the REDMOD full paper (*Gut*, April 2026, DOI: 10.1136/gutjnl-2025-337266 — open access). Specifically study the Methods section on automated nnU-Net segmentation and the SMOTE ensemble architecture. Assess feasibility of replicating this pipeline on your institution's PACS/CT archive as a retrospective validation study. Email: goenka.ajit@mayo.edu to inquire about collaboration or data access.

> **7 Days:**
> Pull your institution's last 3 years of PDAC diagnoses. For each case, identify: (a) were there any abdominal CTs in the 6–36 months prior to diagnosis? (b) what was the presenting symptom? (c) was new-onset diabetes documented? This retrospective audit will quantify your local diagnostic gap and build the IRB case for a REDMOD pilot.

> **30 Days:**
> Draft a 90-day pilot protocol for the EHR-based ENDPAC auto-flag (Idea A). Identify your Epic analyst, gastroenterology champion, and IRB pathway. Simultaneously, contact PRECEDE Consortium (precedestudy.org) and PanCAN (pancan.org) to explore biomarker sub-study co-enrollment. Define your primary metric: *number of stage I/II PDACs detected per 1,000 ENDPAC-flagged patients* vs your current baseline (likely near zero).

---

## 9) One-Minute Mental Model

> *"PDAC hides in plain sight: the cancer rewires pancreatic tissue texture for 13–24 months before forming a visible mass, while the healthcare system is wired only to look for masses — so the entire curable window is spent looking at the wrong signal with the wrong tool in the wrong patient. The single leverage point: deploy radiomic AI (REDMOD) on routine CTs already in the system, and an EHR alert on new-onset diabetes already in the chart — both signals exist today, require no new tests, and are being systematically ignored."*

**2–3 search keywords / exact paper/device names for immediate literature lookup:**
1. `"REDMOD" gutjnl-2025-337266` — *Gut* 2026, Mukherjee et al. (full open-access paper)
2. `"ExoVita Pancreas" PMC10587093` — Nature Communications 2023, EV-based 7-protein classifier
3. `"ENDPAC score pancreatic cancer new onset diabetes" NCT04662879` — PanCAN Early Detection Initiative trial

---

## 10) Pattern Insight (Meta-Learning)

**What recurring diagnostic failure pattern is this reinforcing?**

This is the **"Signal Exists, System Ignores It"** pattern — the most dangerous and most fixable failure mode in early diagnosis. The PDAC case is its purest expression:

- The radiomic signal is present on existing CTs **13–24 months before diagnosis** → ignored because radiologists read for masses, not texture
- The clinical risk signal (new-onset diabetes) is documented in the EHR **8 months before diagnosis** → ignored because no alert fires
- The liquid biopsy signal (5hmC, exosome proteins) is detectable in blood **at Stage I** → ignored because no reflex test is ordered
- CA 19-9 is ordered → fails in 10–20% of patients due to Lewis-negative biology → no one checks Lewis antigen status first

**Is this reinforcing or breaking a prior pattern?**
This reinforces a pattern seen across multiple disease areas: **the bottleneck is not the absence of a detectable signal — it is the absence of a system designed to act on that signal.** We saw this with:
- HCV in blood banks (signal detectable; window period known; NAT not universally deployed for decades)
- Alzheimer's (p-tau217 detectable years before symptoms; no primary care pathway to order it)
- Endometriosis (clinical pattern recognizable; no non-surgical diagnostic pathway existed)

**Generalizable opportunity forming:**
The cross-disease pattern points to a single class of high-value intervention: **"Retrospective Signal Archaeology"** — systematically mining existing clinical data (CT archives, EHR labs, historical blood draws) with AI to identify patients who were in a curable window and were missed. This is simultaneously a research method (to validate new tools), a quality improvement lever (to quantify institutional diagnostic gaps), and a product category (AI that runs continuously on existing data streams to generate prospective early-detection alerts). The founder who builds a disease-agnostic "Signal Archaeology" platform — plugging into PACS, EHR, and lab systems — and licenses disease-specific AI models (REDMOD for PDAC, p-tau217 algorithms for AD, etc.) onto that infrastructure may be building the most important diagnostic company of the decade.

---

*Brief compiled: Saturday, July 4, 2026 | Sources: Mukherjee et al., Gut 2026 (REDMOD, DOI:10.1136/gutjnl-2025-337266); de Leon Pisani et al., Dig Liver Dis 2025 (PMID:40175166); ExoVita Pancreas Assay, PMC10587093; ClearNote Health Avantect ASCO 2026 data; PanCAN EDI NCT04662879; PRECEDE Consortium (precedestudy.org); ctDNA review PMC12973717*