Excellent research gathered. Now I have deep, current intelligence on pancreatic cancer (PDAC) as today's disease — it checks every box: catastrophic late-detection rate, long preclinical window, multiple operational failures, strong startup asymmetry, and rich emerging biomarker science. Let me now compose the full brief.

---

## Subject: Daily Early-Diagnosis Brief — Pancreatic Ductal Adenocarcinoma (PDAC) — 2026-05-30

---

### 1) Snapshot (one line)

**Pancreatic Ductal Adenocarcinoma (PDAC)** — why early diagnosis fails in practice: a long, symptom-silent preclinical window (3–5 years) combined with a biomarker (CA19-9) that is blind to early-stage disease and a hospital workflow that only triggers investigation after jaundice or weight loss — by which point 80–85% of patients are already Stage III/IV.

---

### 2) Why Early Diagnosis Fails (3–5 bullets)

- **Biological barrier:** PDAC is anatomically retroperitoneal and biochemically "quiet" — precursor lesions (PanIN-1/2, small IPMNs) shed negligible ctDNA and cause no luminal obstruction until late; the pancreas has no pain-sensitive peritoneal lining at early stages, so symptoms are absent or indistinguishable from IBS/dyspepsia for years.
- **Test limitation:** CA19-9 — the only FDA-approved serum biomarker — has **~37.5% sensitivity for Stage I/IIA disease** and is completely uninformative in 5–10% of the population (Lewis antigen-negative genotype, Lea⁻b⁻). ctDNA is detectable in <50% of localized PDAC due to low tumor-shed fraction. No single biomarker clears a clinical utility threshold alone.
- **Imaging limitation:** EUS and MRI/MRCP are highly operator-dependent and cost-prohibitive for population screening; they detect macroscopic IPMNs well (sensitivity 90–94%) but **cannot visualize microscopic PanINs** — the dominant precursor pathway — until they are already high-grade.
- **System failure — workflow:** Vague abdominal symptoms route patients through GI investigations first. Studies document a **mean 64-day delay** between first symptom presentation and PDAC-specific workup. No primary care algorithm reliably flags the "new-onset diabetes + weight loss + age >50" triad as a pancreatic cancer red flag in time.
- **System failure — screening policy:** Unlike colon, breast, or lung cancer, **no population-level PDAC screening program exists** anywhere in the world. High-risk surveillance (CAPS consortium guidelines) covers only ~1.5% of eventual PDAC patients — those with hereditary syndromes (BRCA2, PALB2, ATM, Lynch) or familial pancreatic cancer. The remaining 98.5% have no systematic safety net.

---

### 3) Detection Window & Gap

| Stage | Earliest Detectable Signal (Research/Ideal) | Typical Clinical Detection | Gap |
|---|---|---|---|
| PanIN-1/2 (precursor) | Epigenetic cfDNA methylation panels, novel MRI diffusion kurtosis imaging | **Never detected** in routine practice | **3–5 years** of missed window |
| IPMN (branch-duct, <1 cm) | MRI/MRCP in high-risk surveillance programs | Incidental finding only; rarely acted on | **12–24 months** of under-surveillance |
| Stage I PDAC | Multi-omic liquid biopsy (miRNA + ctDNA + protein panel) at ~85% accuracy (OHSU 2025) | Typically Stage III/IV at diagnosis (80–85% of cases) | **6–18 months** of actionable clinical window lost |
| Symptomatic presentation | CA19-9 + CT | This is the current "detection" point | **0 days — but 5-year survival <5%** |

**Gap to close:** Minimum **12–18 months** of actionable lead time exists between a detectable multi-omic signal and current clinical diagnosis. Closing even 6 months of this gap in resectable patients would shift surgical eligibility from ~20% to a theoretically achievable ~40–50%, transforming median survival from 11 months to 24–36 months.

---

### 4) What's Being Used Today (Gold Standard + Emergent)

**Gold Standards:**
- **CT Abdomen/Pelvis with contrast** — primary staging tool; cannot detect <1 cm lesions reliably
- **EUS (Endoscopic Ultrasound)** — best spatial resolution for pancreatic parenchyma; operator-dependent, invasive, not scalable
- **MRI/MRCP** — preferred for IPMN surveillance in high-risk cohorts (CAPS5 guidelines)
- **CA19-9 serum** — FDA-approved, used for monitoring not screening; clinically misleading at early stage
- **ERCP + brushings** — for biliary stricture workup; low sensitivity for malignancy (~40%)

**Emerging Research / Tools (2025–2026):**
- **Multi-omic liquid biopsy (miRNA + ctDNA + protein):** OHSU 2025 study reports **85% accuracy** distinguishing early PDAC from healthy controls in a blood draw
- **CancerSEEK → Cancerguard (Exact Sciences):** Multi-cancer early detection panel; **~68% sensitivity for lethal cancers** including PDAC; specificity >99%; not yet PDAC-stage-specific enough
- **Methylated cfDNA panels:** Grail Galleri, Nucleix — epigenetic tissue-of-origin signal; promising but early-stage PDAC sensitivity still limited (~50–60%)
- **Mayo Clinic REDMOD AI model:** Runs passively on routine abdominal CT scans; demonstrated ability to flag pre-clinical PDAC **up to 3 years before clinical diagnosis** — highest near-term translational value
- **Diffusion Kurtosis Imaging / advanced MRI techniques:** Early 2025/2026 data showing detection of PanIN-associated tissue microstructure changes invisible on standard MRI
- **CA19-9 + ctDNA combinatorial scoring:** AACR Cancer Discovery 2026 — cell-free DNA methylation combined with CA19-9 significantly improves early-stage sensitivity vs. either alone
- **New-onset diabetes (NOD) as a trigger:** "Enrichment strategy" — PDAC-associated diabetes (PA-DM) precedes diagnosis by 6–36 months in ~25% of patients; algorithms to flag high-risk NOD in EHRs are in active validation (ENDPAC score)

**Main Limitations:**
- Multi-omic panels: not yet CE-marked or FDA-cleared for PDAC screening; sample prep complexity; cost ($300–$1,200/test); no prospective RCT evidence yet
- Galleri/Cancerguard: Stage I PDAC sensitivity remains ~30–40% — insufficient for standalone screening
- Mayo AI model: requires retrospective CT data; not yet deployed in real-time prospective workflows
- ENDPAC/NOD algorithms: EHR integration and alert fatigue are major barriers

---

### 5) Where Healthcare Is Failing (Operational Insight)

**Screening point that drops the ball:**
The **primary care encounter for new-onset diabetes in patients >50 years old** is the single most catastrophically missed opportunity. Approximately 25% of PDAC patients develop PA-DM 6–36 months before diagnosis. Every primary care physician manages new-onset T2DM routinely — without any structured reflex to consider pancreatic malignancy. This is a **zero-cost protocol gap** hiding in plain sight.

**Bottleneck most fixable in 90 days:**
**EHR-based ENDPAC score auto-calculation and alert** for all new-onset diabetes patients aged 50+ presenting to primary care or endocrinology. The ENDPAC algorithm (age + BMI change + glucose trajectory) is validated, free, and can be embedded as a passive EHR rule. Implementation requires only clinical informatics work — no new devices, no new labs. This is a **90-day hospital QI project**, not a research study.

**High-risk population missed:**
- **Non-hereditary sporadic PDAC patients (98.5% of cases):** Completely outside CAPS surveillance; no safety net whatsoever
- **Lewis antigen-negative patients (~7% of population):** CA19-9 will always be falsely negative; never flagged for alternative biomarker workup
- **Patients with new-onset diabetes + weight loss in resource-limited settings:** Routed to diabetes management; pancreatic imaging never ordered
- **Incidentally found branch-duct IPMNs <1 cm:** Often under-followed due to "low-risk" radiological classification despite being precursor lesions

---

### 6) 3 High-Leverage Solution Ideas (Practical, Ranked)

---

**🥇 Idea A — EHR ENDPAC Alert System (30–60 day pilot, hospital QI)**

*What:* Embed a passive, automated ENDPAC score calculator into the EHR (Epic/Cerner) that fires a **soft alert** to the ordering provider whenever a patient aged 50+ receives a new diabetes diagnosis AND has lost ≥5% body weight in the prior 6 months.

*How to run the pilot:*
- Partner with 1–2 primary care or endocrinology departments at an academic medical center
- Clinical informatics team builds the EHR rule (Epic BPA or equivalent) — estimated 2–4 weeks build time
- Pilot duration: 60 days across ~500–1,000 new diabetes diagnoses
- Alert fires → provider chooses: (a) order abdominal CT/MRI, (b) refer to GI, (c) dismiss with reason code

*Metrics to collect:*
- Alert fire rate (expected: 8–12% of new DM patients)
- Provider acceptance rate (click-through vs. dismiss)
- Imaging ordered within 30 days of alert (conversion rate)
- PDAC or IPMN detection yield per 1,000 alerts
- Time-to-diagnosis vs. historical baseline (64-day gap target)

*Expected impact:* Even a 15% conversion rate on a 10% alert fire rate in a 10,000-patient primary care panel = ~150 additional imaging referrals/year, with estimated 2–4 early-stage PDAC detections annually per hospital site.

---

**🥈 Idea B — Opportunistic AI Radiology Overlay (60–90 day pilot, scalable tech)**

*What:* Deploy the Mayo Clinic REDMOD-style AI model (or equivalent from Sycamore/Enlitic/Rad AI ecosystem) as a **passive background reader on all routine abdominal CT scans** regardless of indication — reading for pancreatic texture changes, ductal dilation, and parenchymal atrophy patterns associated with pre-clinical PDAC.

*How to run the pilot:*
- Identify a radiology department performing >200 abdominal CTs/month
- Integrate AI model as a secondary read (non-blocking, additive to radiologist workflow)
- Flag cases meeting threshold → route to a dedicated pancreatic multidisciplinary team (MDT) review slot

*Resource checklist:*
- [ ] AI vendor contract / IRB approval for retrospective validation first
- [ ] PACS integration (HL7/DICOM routing)
- [ ] Dedicated MDT slot (1 hour/week minimum)
- [ ] Radiologist training on AI output interpretation
- [ ] Patient consent framework for incidental finding disclosure

*Metrics:*
- Number of AI-flagged scans per 100 routine CTs
- False positive rate (unnecessary workup per flag)
- Lead time to diagnosis vs. control group
- Resectability rate of AI-detected vs. clinically detected PDAC

*Expected impact:* Mayo retrospective data suggests 3-year lead time. Even 12-month lead time improvement would shift resectability from ~20% to ~35% in flagged cohort.

---

**🥉 Idea C — Multi-Omic Liquid Biopsy Validation Consortium (30–90 day setup, research/product)**

*What:* Launch a prospective biobank and validation study for a **combinatorial blood test** (miRNA signature + methylated cfDNA + CA19-9 + THBS2 protein) in a high-risk enriched population (new-onset diabetes + family history + IPMN surveillance patients).

*Why now:* The OHSU 2025 85%-accuracy multi-omic panel is a discovery cohort result — it needs a prospective, multi-site validation in a clinically realistic population before regulatory submission. This is the exact gap between "promising research" and "FDA Breakthrough Device."

*How to set up in 90 days:*
- Identify 3 academic pancreatic centers with active IPMN surveillance programs (e.g., Johns Hopkins, UCSF, MD Anderson)
- Design a prospective case-control biobank protocol: collect blood at IPMN surveillance visits + new-onset DM clinics
- Target N=500 (200 PDAC/high-grade dysplasia, 300 controls) for 18-month accrual
- Partner with a CLIA-certified lab for sample processing (Quest Diagnostics Research or equivalent)

*Collaborators to approach:*
- Lustgarten Foundation (PDAC-specific research funding)
- NCI EDRN (Early Detection Research Network) — existing infrastructure
- Exact Sciences / Grail — commercial partnership potential post-validation
- OHSU liquid biopsy team (Dr. Brett Sheppard group)

*Metrics:* AUC for Stage I/II PDAC vs. controls; sensitivity at 95% specificity; time-to-result from blood draw; cost-per-test at scale

---

### 7) First-Principles Signal Hunt (What We Should Measure Earlier)

**Hidden signal candidate:**
**Pancreatic stellate cell (PSC) activation markers in plasma** — specifically **periostin, SPARC, and TGF-β1 isoforms** released during desmoplastic stroma formation. The PDAC tumor microenvironment is characterized by extreme desmoplasia (up to 80% stroma by volume) that begins forming at PanIN-2/3 stage — *before* malignant transformation is complete. These stromal remodeling proteins are detectable in plasma at concentrations measurable by Simoa (single-molecule array) or proximity ligation assay well before tumor-shed ctDNA reaches detectable levels. This is a fundamentally different signal class — **host response, not tumor shed** — and therefore not subject to the low ctDNA shedding problem.

**Secondary candidate:** Fecal microbiome signature — Fusobacterium nucleatum enrichment and Bifidobacterium depletion have been associated with PDAC in multiple cohorts; a stool-based test could serve as a low-cost, non-invasive first-pass triage tool.

**Minimal sampling change needed:**
- Primary: **2 mL EDTA plasma** (existing blood draw infrastructure; add to routine metabolic panel in high-risk patients) — zero new patient touchpoints required
- Secondary: **Single stool collection** (self-administered, mail-in) — scalable for population-level risk stratification

---

### 8) Strategic Value & Next Immediate Actions (CEO Lens)

**Public health impact:**
- ~60,000 new PDAC diagnoses/year in the US; ~495,000 globally (2022, GLOBOCAN)
- 5-year survival: **13% overall; <5% for Stage IV** (the stage at which 52% are diagnosed)
- If Stage I detection rate doubled (from current ~10% to ~20%), modeling suggests **~6,000–8,000 additional lives saved per year in the US alone**
- Economic burden: $5.4B direct medical costs/year in the US; indirect productivity loss ~$19B
- Startup asymmetry: PDAC liquid biopsy is a **$2–4B addressable market** with no dominant player; Grail/Galleri's PDAC sensitivity is insufficient — the space is open

**3 Immediate Actions:**

| Timeline | Action |
|---|---|
| **Today** | Download and read the ENDPAC score validation paper (Sharma et al., *Gastroenterology* 2018) and the OHSU 2025 liquid biopsy paper — map the exact biomarker panel used and identify the validation gap |
| **7 days** | Contact your hospital's clinical informatics / Epic team to scope the ENDPAC BPA (Best Practice Advisory) alert build — get a time and cost estimate; simultaneously identify which departments see the most new-onset diabetes patients (internal medicine, endocrinology, family medicine) |
| **30 days** | Submit a QI protocol or IRB-exempt pilot proposal for the ENDPAC EHR alert system; in parallel, draft a one-page concept note for a Lustgarten Foundation Pilot Award or NCI EDRN Letter of Intent for the multi-omic biobank study |

---

### 9) One-Minute Mental Model

> *"PDAC hides because it remodels its neighborhood before it moves in — the desmoplastic stroma forms years before invasion, the tumor sheds almost no DNA into blood at early stage, and the only approved biomarker (CA19-9) is blind to the very stage where surgery can cure. The single leverage point: intercept the 25% of patients who develop new-onset diabetes 6–36 months before diagnosis — they are already in the healthcare system, already getting labs drawn, and we are simply failing to ask the right question of the data we already have."*

**2–3 search keywords / paper lookups:**
1. **"ENDPAC score new-onset diabetes pancreatic cancer" — Sharma et al., *Gastroenterology* 2018** (PMID: 29360515)
2. **"OHSU multi-omic liquid biopsy pancreatic cancer 85% accuracy 2025"** — search OHSU News Feb 2025 + *BJC Reports* 2026 (Nature)
3. **"Mayo Clinic REDMOD AI CT pancreatic cancer pre-clinical detection"** — search *Radiology* or *Gastroenterology* 2024–2025; also keyword: **"opportunistic CT screening PDAC artificial intelligence"**

---

### 10) Pattern Insight (Meta-Learning)

**Recurring diagnostic failure pattern emerging:**

Today's PDAC brief reinforces a pattern that is crystallizing across multiple disease briefs: **"The Symptom-Silence Trap + Biomarker Threshold Mismatch."**

The pattern has three consistent components:
1. **A long preclinical window where biology is detectable but sub-threshold for current assays** (PDAC: 3–5 year PanIN stage; analogous to: HIV eclipse phase, prion disease, early Alzheimer's tau accumulation)
2. **A single approved biomarker that is calibrated for late-stage monitoring, not early detection** (CA19-9 for PDAC; PSA for prostate; AFP for HCC) — creating a false sense of clinical coverage
3. **A missed behavioral/metabolic signal already present in routine healthcare data** (new-onset diabetes for PDAC; cognitive complaints in GP notes for dementia; recurrent UTIs for bladder cancer) that could trigger earlier investigation with zero new technology — only a protocol change

**What's generalizable:**
The highest-leverage, lowest-cost interventions consistently lie at the intersection of **existing EHR data + validated risk algorithms + zero-new-technology workflow triggers.** The research community keeps building better tests; the operational community keeps failing to use the signals it already has. The asymmetric opportunity — for both hospital QI and startups — is building the **"reflex layer"**: the intelligent middleware that sits between existing data and existing clinicians and asks the question nobody is currently asking.

**Is today's disease reinforcing or breaking the pattern?**
Strongly **reinforcing** — PDAC is perhaps the purest expression of this pattern. The ENDPAC score has been validated since 2018. Eight years later, it is embedded in essentially zero EHR systems at scale. The gap is not scientific. It is operational, economic, and organizational. That is where the next wave of diagnostic value will be created.

---
*Brief generated: 2026-05-30 | Focus: Research + Hospital Improvement (partial Startup) | Disease: PDAC | Next brief: recommend rotating to a neurodegenerative or infectious disease to avoid oncology clustering*