Now I have comprehensive, deeply researched data on both the landscape of diagnostic delays and pancreatic cancer specifically. Pancreatic cancer (PDAC) is clearly the strongest candidate for today's brief — it has the most compelling combination of: massive public health impact, a 3-year AI-detectable window vs. 80% Stage 3/4 clinical detection, multiple recent 2025-2026 breakthroughs, and enormous startup + hospital improvement potential. Let me now compile the full decision-grade brief.

---

## Subject: Daily Early-Diagnosis Brief — Pancreatic Ductal Adenocarcinoma (PDAC) — 2026-06-25

---

### 1) Snapshot (one line)

**Pancreatic Ductal Adenocarcinoma (PDAC)** — why early diagnosis fails in practice: *The tumor sits silent in the retroperitoneal cavity for 1–3 years with detectable AI/molecular signals, yet 80% of patients reach Stage 3/4 before diagnosis because no population-level screening exists, CA 19-9 is blind at early stage, and GPs misattribute vague symptoms for months.*

---

### 2) Why Early Diagnosis Fails (5 bullets)

- **Biological barrier:** Deep retroperitoneal location means no palpable mass; early symptoms (mild back pain, weight loss, new-onset diabetes, indigestion) are non-specific and shared with a dozen benign GI conditions. Tumors can metastasize when still <2 cm.
- **Test limitation — CA 19-9:** The only FDA-approved PDAC biomarker has near-zero sensitivity at Stage 1–2; ~5% of patients lack the Lewis antigen entirely and never produce it; false positives from pancreatitis and biliary obstruction erode clinical trust. It is a monitoring tool masquerading as a screening tool.
- **Test limitation — imaging:** Multiphasic CT (gold standard) is not deployed until red-flag symptoms appear. Routine abdominal CTs ordered for other reasons routinely miss early PDAC because radiologists are not primed to look, and subtle pre-diagnostic parenchymal changes are dismissed.
- **System failure — screening policy:** High-risk surveillance (annual MRI/EUS) is restricted to <5% of eventual PDAC patients — those with familial history or known germline mutations (BRCA1/2, PALB2, ATM, CDKN2A). The >80% of sporadic cases receive zero proactive surveillance.
- **System failure — referral pathway:** Patients with vague GI symptoms are subjected to prolonged GI workups (H. pylori, colonoscopy, gallbladder ultrasound) before pancreatic imaging is ordered. Median delay from first symptom to diagnosis: **1.4–4.2 months** with accurate initial suspicion; **up to 104+ days** when initial misdiagnosis occurs — and >104 days independently increases mortality.

---

### 3) Detection Window & Gap

| Stage | Signal | Timepoint |
|---|---|---|
| **Earliest detectable (AI/research)** | Subtle CT parenchymal changes detectable by AI model (Mayo Clinic AUROC 0.92) | **Up to 3 years pre-diagnosis** |
| **Molecular signal** | CA 19-9 + novel panel (THBS2, ANPEP, PIGR) rising; exosome miRNA signatures | **~2 years pre-diagnosis** |
| **Typical clinical detection** | Stage 3 (locally advanced) or Stage 4 (metastatic) | **At or after symptom onset** |
| **Gap to close** | **2–3 years** | 5-year survival jumps from ~13% (Stage 3/4) → ~44% (Stage 1) → >80% (resectable Stage 1A) |

**Practical impact of closing the gap:** Even shifting 20% of diagnoses from Stage 3/4 to Stage 1/2 would prevent tens of thousands of deaths annually (PDAC kills ~57,000/year in the US alone).

---

### 4) What's Being Used Today (Gold Standard + Emergent)

**Gold Standards:**
- **Multiphasic pancreatic protocol CT scan** — primary imaging workhorse; misses lesions <1 cm
- **Endoscopic Ultrasound (EUS) + Fine Needle Aspiration (FNA)** — most sensitive for small lesions (<2 cm), but invasive, operator-dependent, and not scalable for screening
- **MRI/MRCP** — evaluates ductal anatomy non-invasively; used in high-risk surveillance programs
- **CA 19-9 serum assay** — FDA-approved but used almost exclusively for monitoring, not detection

**Emerging Research & Tools (2024–2026):**
- **Exosome-based liquid biopsy + CA 19-9 (combined):** Detected **97% of Stage 1–2 PDAC** in breakthrough study (AACR 2025) — the most exciting near-term clinical tool
- **Four-biomarker blood panel (CA19-9 + THBS2 + ANPEP + PIGR):** Significantly outperforms CA 19-9 alone for early-stage detection (ASCO Post, Feb 2026)
- **ClearNote Health — Avantect Test:** Cell-free DNA epigenomic blood test; 82% sensitivity / 97% specificity in high-risk populations (2026 data)
- **Craif (urine-based miRNA test):** Raised $22M in 2025; non-invasive, early-stage signal; pre-clinical validation ongoing
- **Mayo Clinic AI CT model:** AUROC 0.92 on routine abdominal CT, outperforms average radiologist (0.88); detects pre-diagnostic signals up to 3 years before clinical diagnosis — *validated in landmark Lancet Oncology 2025 study*
- **PRECEDE Consortium:** International prospective cohort study aiming to validate early detection models to raise 5-year survival from 13% → 50%
- **NCT06388967:** Prospective trial validating exosome miRNA signatures for noninvasive PDAC detection

**Main Limitations:**
- Liquid biopsies: Not yet approved for screening; validation cohorts still maturing; cost ~$500–$1,500/test
- AI CT model: Requires large institutional CT archive infrastructure; not yet deployed in community hospitals
- Urine/exosome tests: Analytical sensitivity varies by stage; no head-to-head RCT data yet

---

### 5) Where Healthcare Is Failing (Operational Insight)

**Screening point that drops the ball:**
> **Primary care / GP triage.** The first 1–3 clinical encounters for vague abdominal pain, unexplained weight loss, or new-onset diabetes (especially in adults >50) are where the diagnostic clock starts — and where it stalls. GPs default to common diagnoses; pancreatic imaging is rarely reflexively ordered. New-onset diabetes in a patient >50 with no family history is a known PDAC early signal that is almost universally missed in practice.

**Bottleneck most fixable in 90 days:**
> **EHR-based reflex alert for new-onset diabetes + weight loss co-occurrence in adults >50.** This is a software change, not a new test. A rule-based or ML-based EHR flag triggering pancreatic imaging referral at first presentation of this combination could be deployed at a hospital network in 60–90 days with minimal cost.

**High-risk population being missed:**
> **Sporadic PDAC patients (>80% of all cases)** — no genetic flag, no family history, no current screening pathway. Also critically missed: **patients with new-onset diabetes (NOD) over age 50** — PanCAN's Early Detection Initiative has identified this as a trigger population, but clinical uptake of NOD-based screening protocols is near zero outside of academic centers.

---

### 6) 3 High-Leverage Solution Ideas (Practical, Ranked)

**🥇 Idea A — EHR Reflex Alert for New-Onset Diabetes + Weight Loss (30–60 day pilot)**

*How to run it:*
- Partner with a hospital network (500+ bed academic center or regional health system with Epic/Cerner)
- Build a rule-based alert: Patient age >50 + new T2DM diagnosis (or HbA1c crossing threshold) + ≥5% unintentional weight loss within 6 months → auto-trigger gastroenterology/radiology referral order for pancreatic protocol CT or MRI
- Run for 90 days; track: (a) alert trigger rate, (b) referral completion rate, (c) imaging yield (PDAC found / total imaged), (d) stage at detection vs. historical baseline
- *Why now:* PanCAN's Early Detection Initiative has published the epidemiological basis; this is a protocol translation, not research
- *Measurable metrics:* # alerts fired, # imaging orders completed, # PDAC detected, stage distribution, time-to-diagnosis vs. control cohort

**🥈 Idea B — AI-Assisted Radiology Re-Read Program for Retrospective CT Archive (60–90 days)**

*How to run it:*
- License or pilot the Mayo Clinic AI model (or equivalent: Pancreatlas, Google Health CT models) on existing institutional CT archive
- Retrospectively flag patients who had routine abdominal CTs in the past 3 years and now have a PDAC diagnosis — validate the model's pre-diagnostic sensitivity on your own population
- Prospectively deploy on all new abdominal CTs: auto-flag subtle pancreatic parenchymal changes for radiologist second-read
- *Resource checklist:* PACS integration, IRB approval for retrospective review, radiology champion, AI vendor contract or research partnership
- *Expected impact:* Detection of PDAC 12–36 months earlier in flagged patients; quantifiable shift in stage at diagnosis within 12–18 months of deployment
- *Collaborators:* Mayo Clinic (model validation), Frontiers in Medicine (2025 AI+EUS paper), academic radiology departments

**🥉 Idea C — Liquid Biopsy Reflex Testing Embedded in High-Risk GI Clinic (90-day research pilot)**

*How to run it:*
- Identify patients already in GI clinic for unexplained weight loss, new-onset diabetes, or indeterminate pancreatic cysts (IPMNs)
- Add a reflex blood draw for exosome-based liquid biopsy (partner with ClearNote Health Avantect or NCT06388967 trial enrollment) alongside standard CA 19-9
- Track: sensitivity vs. CA 19-9 alone, turnaround time, false positive rate, patient acceptance
- *Highest upside:* If exosome + CA 19-9 combo (97% Stage 1–2 sensitivity) validates in a prospective institutional cohort, this becomes the basis for a new screening protocol for at-risk adults
- *Collaborators to approach:* ClearNote Health, Craif, PRECEDE Consortium, PanCAN Early Detection Initiative, NCI EDRN (Early Detection Research Network)

---

### 7) First-Principles Signal Hunt (What We Should Measure Earlier)

**Hidden signal candidate:**
> **New-onset diabetes (NOD) as a metabolic proxy for early PDAC.** PDAC frequently *causes* diabetes via destruction of islet cells before the tumor is radiologically visible. An adult >50 with no obesity/family history who develops T2DM within 12–24 months has a ~1% PDAC risk — 8× the background rate. This is a population-level, EHR-accessible signal requiring zero new tests.

**Secondary signal candidate:**
> **Exosome-derived miRNA signatures in urine or plasma** — measurable with next-gen sequencing panels at ~$200–$400/test at scale; non-invasive; detectable at Stage 1–2 in current validation data.

**Minimal sampling change needed:**
> **Blood (plasma) draw at annual physical** — no new visit, no invasive procedure. Adding a reflex liquid biopsy panel to a standard annual blood draw for adults >50 with any 2 of: unexplained weight loss, NOD, new back pain, elevated liver enzymes is operationally feasible today.

---

### 8) Strategic Value & Next Immediate Actions (CEO Lens)

**Public health impact:**
- PDAC is the **3rd leading cause of cancer death** in the US; projected to become **2nd by 2030**
- ~57,000 US deaths/year; ~500,000 globally
- 5-year survival: **13% overall** vs. **44% Stage 1** vs. **>80% Stage 1A resectable**
- Closing even 30% of the 2–3 year detection window gap could prevent 15,000–20,000 deaths/year in the US alone
- Global liquid biopsy market: ~$25B projected; PDAC-specific early detection is a high-value, underserved segment

**3 Immediate Actions for Ayan:**

| Timeframe | Action |
|---|---|
| **Today** | Read: *"Artificial intelligence and radiologists in pancreatic cancer detection on CT"* — Lancet Oncology 2025 (PIIS1470-2045(25)00567-4). This is the foundational validation paper for AI-CT deployment. Also pull the ClearNote Health Avantect 2026 data sheet. |
| **7 Days** | Contact PanCAN's Early Detection Initiative (pancan.org/research/early-detection-initiative) and the PRECEDE Consortium (precedestudy.org) to understand open collaboration/enrollment opportunities. Map your institution's EHR (Epic/Cerner) capability to deploy a NOD + weight loss reflex alert — identify the clinical informatics lead. |
| **30 Days** | Draft a 90-day pilot protocol: EHR-based reflex alert for NOD + weight loss in adults >50 → pancreatic imaging referral. Define IRB pathway, identify GI/radiology champion, set baseline metrics (current time-to-diagnosis, stage distribution). Submit pilot proposal to hospital quality improvement committee or research office. |

---

### 9) One-Minute Mental Model

> *"PDAC hides in plain sight: it causes metabolic disruption (new diabetes, weight loss) that is visible in the EHR years before it causes pain — but clinicians are trained to treat the symptom, not hunt the cause. The single leverage point is converting the EHR from a passive record into an active surveillance system that reflexively links metabolic red flags to pancreatic imaging before the tumor announces itself."*

**2–3 Search Keywords / Paper Citations for Immediate Lookup:**
1. **"Artificial intelligence and radiologists in pancreatic cancer detection on CT"** — *Lancet Oncology*, 2025 (PIIS1470-2045(25)00567-4) — Mayo Clinic AI validation, AUROC 0.92
2. **"New-onset diabetes as early indicator pancreatic cancer PanCAN Early Detection Initiative"** — PanCAN.org research pages + ASCO/AACR 2025 abstracts
3. **"Exosome liquid biopsy CA19-9 pancreatic cancer stage 1 detection AACR 2025"** — AACR newsroom + NCT06388967 on ClinicalTrials.gov

---

### 10) Pattern Insight (Meta-Learning)

**Recurring diagnostic failure pattern observed:**

> **The "Metabolic Proxy Blindness" pattern** — diseases that cause measurable, EHR-visible metabolic or physiological changes *years before* tissue-level pathology is sought, but clinical systems are not designed to reverse-engineer causation from these upstream signals.

This pattern has now appeared across multiple disease categories:
- **PDAC today:** New-onset diabetes + weight loss = early PDAC signal, missed because GPs treat the diabetes, not the cause
- **Alzheimer's (prior pattern):** Subtle speech/sleep/metabolic changes precede clinical cognitive decline by 10–15 years; only now being captured by digital biomarkers
- **Chagas disease (prior pattern):** Cardiac remodeling begins in the latent phase; EKG changes are visible but not connected to the parasitic cause without specific suspicion

**The generalizable opportunity forming:**

> **EHR-as-Surveillance-Engine:** Across diseases, the data to trigger earlier diagnosis already exists inside hospital EHR systems — it is simply not being queried with the right clinical logic. The highest-leverage, lowest-cost intervention class across all these diseases is **rule-based or ML-based EHR alert systems that connect upstream metabolic/physiological signals to the correct downstream diagnostic pathway.** This is a $0-infrastructure, 60–90 day deployable intervention that does not require new biomarkers, new devices, or new clinical visits. It requires only clinical informatics will and a champion clinician.

**Breaking or reinforcing?** → **Strongly reinforcing.** PDAC is the clearest, highest-stakes example yet of this pattern. The opportunity is not just PDAC-specific — a startup or hospital program that builds a modular "metabolic red flag → reflex imaging/testing" EHR layer could apply the same architecture to 5–10 other diseases with identical upstream-signal blindness.

---

*Brief compiled: June 25, 2026 | Sources: Lancet Oncology 2025, AACR 2025, Mayo Clinic News Network, ClearNote Health, PanCAN Early Detection Initiative, PRECEDE Consortium, NCT06388967, ASCO Post Feb 2026*