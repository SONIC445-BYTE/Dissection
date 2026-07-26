All research data is rich and verified. I now have everything needed to compose the complete brief. Given the depth of 2024–2026 data, I'm selecting **Pulmonary Arterial Hypertension (PAH)** as today's disease — it has a 2–3 year diagnostic delay, a freshly FDA-cleared AI-ECG tool (Anumana, March 2026), rich operational failure data, and high asymmetric startup + hospital improvement potential. Here is the full report:

---

## Subject: Daily Early-Diagnosis Brief — Pulmonary Arterial Hypertension (PAH) — 2026-07-24

---

### 1) Snapshot (one line)

**Pulmonary Arterial Hypertension (PAH)** — why early diagnosis fails in practice: *Non-specific dyspnea is misattributed to asthma/COPD for 2–3 years while irreversible pulmonary vascular remodeling progresses silently, and the definitive test (right heart catheterization) is invasive, specialist-gated, and rarely triggered early.*

---

### 2) Why Early Diagnosis Fails (3–5 bullets)

- **Biological barrier:** PAH's cardinal symptom — exertional dyspnea — is shared by >40 common conditions. The disease remodels pulmonary arterioles silently for months to years before hemodynamic thresholds cross into clinical detection range (mPAP >20 mmHg). By the time patients are symptomatic enough to trigger specialist referral, most are already WHO Functional Class III–IV.
- **Test limitation:** The gold standard (right heart catheterization, RHC) is invasive, requires catheterization lab access, and is only ordered after echocardiographic suspicion. Standard echo TRV thresholds (>3.4 m/s = high probability) miss borderline cases (2.8–3.4 m/s = intermediate) that are not escalated. NT-proBNP and BNP elevate late, not early.
- **System failure — referral pathway collapse:** Primary care and general cardiology consistently under-refer patients with borderline echo findings. EMR systems have no automated flags to triage patients with intermediate TRV + dyspnea toward PH centers. A Temple Health 2025 study documented that an EMR-integrated tool identified PAH candidates who were entirely missed by standard referral pathways.
- **System failure — siloed specialties:** PAH frequently presents first to pulmonologists (asthma/COPD workup) or rheumatologists (in scleroderma patients) who don't own the cardiac workup pathway. Fragmented care between rheumatology, pulmonology, and cardiology creates a "three-door problem" with no one coordinating the diagnostic thread.
- **Screening policy gap:** High-risk populations (scleroderma/SSc, HIV, portal hypertension) have evidence-based screening algorithms (DETECT for SSc), but a 2024 PMC study found that rheumatologist adherence to annual PAH screening in SSc patients is poor — the majority wait for symptomatic presentation rather than proactively screen.

---

### 3) Detection Window & Gap

| Stage | Marker / Signal | Timing |
|---|---|---|
| **Earliest detectable (research)** | AI-ECG signature (PH-EDA algorithm) | **Up to 5 years before clinical diagnosis** (AUC 0.79 at Mayo; AUC 0.73 at Vanderbilt) |
| **Sub-clinical detectable** | AI-ECG at 6–18 months pre-diagnosis | AUC 0.86 (Mayo) / 0.81 (Vanderbilt) |
| **Borderline echo** | TRV 2.8–3.4 m/s on echocardiogram | 1–2 years before diagnosis — rarely acted upon |
| **Typical clinical detection** | Symptomatic + TRV >3.4 m/s + RHC confirmation | **2–3 years after symptom onset** |
| **Gap to close** | **~2–5 years** — clinically devastating: each year of delay correlates with worse RV function, lower 6MWD, higher mortality, and reduced treatment response |

**Practical impact of closing the gap:** Tafamidis-class stabilizers and prostacyclin/ERA combination therapy are dramatically more effective when initiated in WHO FC I–II vs. FC III–IV. Earlier diagnosis = measurable survival benefit and reduced hospitalization burden.

---

### 4) What's Being Used Today (Gold Standard + Emergent)

**Gold Standards:**
- **Right Heart Catheterization (RHC):** Definitive. mPAP >20 mmHg + PVR ≥2 WU + PAWP ≤15 mmHg = PAH diagnosis. Invasive, specialist-gated, not scalable as a screen.
- **Echocardiography (TTE):** TRV >3.4 m/s = high PH probability. First-line triage. Misses borderline cases.
- **NT-proBNP / BNP:** Standard risk stratification; not early-detection biomarkers — elevate with established RV strain.
- **DETECT Algorithm (SSc patients):** Two-step, 8-variable decision tree (FVC%, DLCO%, telangiectasias, anticentromere antibodies, NT-proBNP, serum urate → echo → RHC). Validated, underused. A 2025 Italian observational study (Stano et al., *JMDPI*) reconfirmed its predictive value.

**Emerging Research / Tools (2024–2026):**
- **Anumana ECG-AI (PH-EDA algorithm):** FDA 510(k) cleared **March 28, 2026** (K252360). Detects PH from standard 12-lead ECG. Sensitivity 73%, specificity 74.4% in dyspnea patients. Developed with Mayo Clinic + nference. First FDA-cleared AI tool for PH detection.
- **Tempus ECG-AI (MOMENTOUS Study):** FDA-cleared ECG-AI device; active multicenter study assessing clinical impact on PAH diagnosis rates. Watch this space for Q3 2026 readout.
- **DuBrock et al. AI-ECG (European Respiratory Journal, July 2024):** The foundational study — AUC 0.92 at diagnosis, 0.86 at 6–18 months pre-diagnosis, 0.79 up to 5 years pre-diagnosis. Validated at Mayo + Vanderbilt. This is the paper underpinning Anumana's FDA clearance.
- **Us2.ai:** Automated AI right-heart echocardiography analysis — first validated AI for fully automated RV function + TRV measurement. Reduces dependency on expert sonographers for PAH screening echo reads.
- **miRNA Panels (Errington et al., *Circulation: Genomic and Precision Medicine*, 2025):** Machine-learning-derived whole-blood miRNA signatures that classify PAH and differentiate from disease controls. AUC promising; not yet clinical-grade. Collaborators: University of Leeds, King's College London.
- **Protein Biomarker Panels (Niu et al., *Journal of Translational Medicine*, 2025):** Novel proteomics-based biomarkers detecting pulmonary vascular remodeling before severe pressure elevation — pre-competitive research phase.
- **BMPR2 mRNA therapy (preclinical 2025–2026):** Targeted BMPR2 mRNA delivery to reverse pulmonary vascular remodeling — opens a window for genetic pre-symptomatic screening in heritable PAH.
- **NCT07079592 (Active Clinical Trial):** Deep-learning ECG model to identify PH in high-risk patients, prompting RHC evaluation — ongoing enrollment.

**Main Limitations:**
- Anumana's cleared algorithm: 73% sensitivity means 27% false negatives — not sufficient as a standalone rule-out; best used as a triage layer.
- miRNA panels: Not yet standardized, no clinical-grade assay, require prospective multicenter validation.
- Us2.ai: Dependent on echo acquisition quality; not a screening tool in non-echo settings.
- RHC: Remains the unavoidable confirmatory test — no non-invasive alternative yet.

---

### 5) Where Healthcare Is Failing (Operational Insight)

**Screening point that drops the ball:**
> **The borderline echo report.** When TRV reads 2.8–3.4 m/s (intermediate probability), the report is filed, the clinician notes "borderline" — and nothing happens. No reflex order for NT-proBNP, no DETECT algorithm trigger, no PH center referral. This is the single highest-yield failure point. In scleroderma clinics, the DETECT algorithm is available but not systematically applied — most rheumatologists wait for overt symptoms.

**Bottleneck most fixable in 90 days:**
> **EMR-integrated reflex alert for intermediate TRV + dyspnea ICD codes.** A simple rule-based CDS (Clinical Decision Support) trigger — if TRV 2.8–3.4 m/s AND ICD-10 code for dyspnea (R06.0x) AND age >40 → auto-generate "PAH risk flag: consider DETECT algorithm / PH center referral" — requires only IT configuration, no new equipment. Temple Health proved this works in 2025.

**High-risk population most missed:**
> **Systemic Sclerosis (SSc) patients in rheumatology clinics.** PAH develops in 8–12% of SSc patients and is the leading cause of SSc-related mortality. Annual echo screening is guideline-recommended. Yet a 2024 survey (Álvarez-Hernández et al., *PMC11188845*) found that most rheumatologists don't apply the DETECT algorithm and only 72% recommend any screening — creating a structured, knowable population that is systematically under-screened. **HIV patients with unexplained dyspnea** and **cirrhotic patients awaiting liver transplant** (portopulmonary hypertension) are secondary missed cohorts.

---

### 6) Three High-Leverage Solution Ideas (Practical, Ranked)

---

**🥇 Idea A — EMR-Reflex CDS Alert for Borderline Echo + Dyspnea [30-day pilot, hospital-level]**

*What:* Build a rule-based EMR alert that fires when: (1) echocardiography report contains TRV 2.8–3.4 m/s AND (2) patient has a dyspnea ICD-10 code within 90 days AND (3) no prior PH workup or RHC on record.

*How to run a 30-day pilot:*
- Partner with 1 academic cardiology + 1 rheumatology department
- Configure Epic/Cerner BPA (Best Practice Advisory) — IT lift: ~2 weeks
- Alert fires to ordering physician: "Intermediate PH probability — consider DETECT algorithm or PH center referral"
- Track: # alerts fired, # DETECT algorithms completed, # RHC orders placed, # new PAH diagnoses confirmed

*Metrics to collect:*
- Alert-to-action rate (target >40% of alerts result in next-step action)
- Time from alert to RHC (target: <60 days)
- New PAH diagnoses per 100 alerts fired (baseline: near-zero without alert)
- False positive burden (RHC negative rate)

*Collaborators:* Temple Health (already published proof-of-concept), any Epic-integrated academic center

---

**🥈 Idea B — Structured PAH Screening Program in SSc/Rheumatology Clinics [60-90 day pilot, scalable]**

*What:* Implement a standardized, nurse-led DETECT algorithm workflow at every SSc clinic visit. Embed DETECT score calculation into the rheumatology EMR visit template. Trigger automatic annual echo order if DETECT Step 1 score exceeds threshold.

*Resource checklist:*
- [ ] DETECT calculator embedded in EMR template (Epic SmartForm or equivalent) — 2 weeks
- [ ] Nurse/PA training on 6 non-echo variables (FVC%, DLCO%, telangiectasias, anticentromere Ab, NT-proBNP, urate) — 1 day
- [ ] Radiology/echo scheduling pathway for SSc patients flagged by DETECT
- [ ] Rheumatology-cardiology liaison for DETECT Step 2 review
- [ ] Patient registry for longitudinal tracking

*Expected impact:* In a scleroderma cohort of 200 patients, expect to identify 16–24 PAH cases (8–12% prevalence) vs. historical detection rate of ~50% of these being missed or late-stage. Estimated 2–3 year earlier diagnosis in flagged patients.

*Scale pathway:* Exportable as a rheumatology QI protocol; target ACR (American College of Rheumatology) quality measure adoption.

---

**🥉 Idea C — AI-ECG PAH Triage Layer Integrated into Primary Care / ED Dyspnea Workup [Startup / Research product, 90-day spec]**

*What:* Deploy Anumana's FDA-cleared PH algorithm (or license the DuBrock et al. model) as a background inference layer on all ECGs ordered in primary care and ED settings for dyspnea workup. Flag high-probability patients for expedited echo + PH center referral.

*Highest upside scenario:* PAH is diagnosed at WHO FC I–II instead of III–IV in flagged patients → measurable survival benefit + reduced hospitalization cost (PAH hospitalization costs ~$50K–$100K per episode).

*Tests needed:*
- Prospective real-world validation of Anumana algorithm in primary care setting (not just tertiary PH centers)
- Head-to-head: AI-ECG flag vs. standard of care — time-to-diagnosis as primary endpoint
- Cost-effectiveness model: cost per QALY gained from earlier PAH diagnosis

*Collaborators to approach:*
- **Anumana** (FDA-cleared algorithm, seeking deployment partners)
- **Tempus** (MOMENTOUS study — could expand enrollment to primary care sites)
- **Pulmonary Hypertension Association (PHA)** — 2026 conference abstracts show active interest in AI triage tools
- **Mayo Clinic / Vanderbilt** — original DuBrock et al. study teams; open to multicenter expansion

*30-day pilot spec:* Identify 1 health system with Anumana integration capability → define dyspnea-presenting patient cohort → run 90-day prospective observational study → measure: PAH detection rate vs. historical baseline, time-to-RHC, false positive rate.

---

### 7) First-Principles Signal Hunt (What We Should Measure Earlier)

**Hidden signal candidate:**
> **The ECG's right ventricular strain pattern — invisible to human readers, detectable by AI up to 5 years early.** The DuBrock/Anumana model exploits subtle convolutional features in the 12-lead ECG waveform (likely: rightward QRS axis shift, P-wave changes in V1, R/S ratio changes in right precordial leads, subtle ST-T changes) that precede any clinical hemodynamic threshold. This is a "latent signal" hiding in a test that costs $15 and is ordered routinely for dyspnea worldwide.

**Secondary early signal candidate:**
> **Whole-blood miRNA panels** (Errington et al., 2025): A machine-learning-derived miRNA signature that classifies PAH from whole blood — non-invasive, potentially detectable before echo changes. miRNA-7110, miR-21, miR-204, miR-let-7f are candidate markers. Could serve as a blood-based pre-echo triage test.

**Minimal sampling change needed:**
> **No new sample type required.** The AI-ECG approach requires only a standard 12-lead ECG — already collected in virtually every dyspnea workup. The miRNA approach requires a standard blood draw (EDTA tube), no specialized collection. The barrier is purely software/algorithm deployment, not new specimen logistics.

---

### 8) Strategic Value & Next Immediate Actions (CEO Lens)

**Public health impact:**
- ~40,000 diagnosed PAH cases in the US (2025); globally estimated 15–50 cases per million (rare but highly morbid). Broader pulmonary hypertension (all 5 WHO groups) affects millions.
- 5-year survival without treatment: ~34%. With early treatment (FC I–II): >70%.
- Median time from symptom onset to diagnosis: **2–3 years** — during which irreversible RV remodeling occurs.
- US PAH treatment market: **$2.61B (2024)**, growing to $3.95B by 2032 — driven by new therapies that only work if patients are diagnosed early enough to receive them.
- **The asymmetry:** Closing the diagnostic gap by 18 months for 10,000 patients/year = thousands of life-years saved + billions in reduced hospitalization costs.

**3 Immediate Actions:**

| Timeline | Action |
|---|---|
| **Today** | Read: DuBrock HM et al., *European Respiratory Journal* 2024;64:2400192 (the foundational AI-ECG PAH paper). Read the Anumana FDA 510(k) clearance summary (K252360, March 28, 2026). These two documents define the current state of the art and the regulatory pathway. |
| **7 days** | Map your institution's echo reporting workflow: Does your radiology/cardiology system flag borderline TRV (2.8–3.4 m/s) reports to ordering physicians? If not, draft a 1-page CDS alert specification for your IT/Epic team. Simultaneously, identify your rheumatology department's SSc patient volume and current PAH screening adherence rate. |
| **30 days** | Design and submit a 90-day QI pilot protocol: EMR-triggered reflex alert for borderline echo + dyspnea ICD codes → DETECT algorithm completion → PH center referral. Primary endpoint: time-to-RHC in flagged vs. historical control patients. Secondary: new PAH diagnoses per quarter. Approach Anumana for an academic deployment partnership for AI-ECG integration. |

---

### 9) One-Minute Mental Model

> *"PAH hides behind the world's most common symptom (breathlessness) and is confirmed only by the world's most invasive cardiology test (right heart catheterization) — but its fingerprint has been sitting unread in every routine ECG for up to 5 years. The single leverage point: deploy FDA-cleared AI inference on existing ECG streams to convert a $15 test into a PAH pre-screen, triggering the echo → DETECT → RHC cascade years earlier than current practice."*

**2–3 literature lookup keywords / paper names:**
1. **"DuBrock HM et al. ECG AI pulmonary hypertension European Respiratory Journal 2024"** — foundational AI-ECG study; AUC 0.92 at diagnosis, 0.79 at 5 years pre-diagnosis
2. **"Anumana PH algorithm FDA 510(k) K252360 March 2026"** — regulatory clearance document + clinical performance data
3. **"Errington N miRNA PAH Circulation Genomic Precision Medicine 2025"** — whole-blood miRNA diagnostic signature for PAH classification

---

### 10) Pattern Insight (Meta-Learning)

**Recurring diagnostic failure pattern emerging:**

> **The "Latent Signal in Ubiquitous Data" pattern** — PAH joins a growing list of diseases (ATTR-CM, HFpEF, early AF, diabetic cardiomyopathy) where the diagnostic signal has been present in routinely collected, low-cost data (ECGs, routine labs, standard imaging) for years before clinical detection — but human pattern recognition cannot extract it. The disease is not hiding from *data*, it is hiding from *human cognition applied to that data*.

**Is today's disease reinforcing or breaking the pattern?**
> **Strongly reinforcing.** PAH is almost a perfect archetype of this pattern: 12-lead ECG costs $15, is ordered for every dyspnea presentation, and contains a detectable signal up to 5 years before diagnosis — yet the average patient waits 2–3 years. The FDA clearance of Anumana's algorithm in March 2026 is the regulatory proof-of-concept that this pattern is now actionable at scale.

**Generalizable opportunity forming across diseases:**
> The meta-opportunity is a **"Latent Signal Infrastructure" layer** — a software platform that runs validated AI inference models in the background on all routine clinical data streams (ECGs, chest X-rays, routine blood panels, EHR time-series) and generates probabilistic disease-risk flags for rare but treatable conditions. PAH, ATTR-CM, early HFpEF, and pulmonary fibrosis are all candidates for this architecture. The business model: a SaaS layer on top of existing hospital data infrastructure, FDA-cleared algorithm by algorithm, condition by condition. **The moat is regulatory clearance + clinical validation, not the AI itself.**

> **Pattern to watch:** As more AI-ECG algorithms achieve FDA clearance (Anumana for PH, separate clearances for ATTR-CM, AF, HFpEF), the question shifts from "can AI detect this?" to "who owns the infrastructure layer that runs all these algorithms simultaneously?" — that is the platform play forming right now.

---

*Brief prepared: 2026-07-24 | Sources: DuBrock et al. ERJ 2024, Anumana FDA K252360 (March 2026), Errington et al. Circulation Genomic Precision Medicine 2025, Temple Health EMR-PAH study 2025, Álvarez-Hernández et al. PMC11188845 (2024), Niu et al. J Translational Medicine 2025, Stano et al. JMDPI 2025, DETECT algorithm (Coghlan et al. ARD 2014, validated 2025), Tempus MOMENTOUS Study, NCT07079592.*