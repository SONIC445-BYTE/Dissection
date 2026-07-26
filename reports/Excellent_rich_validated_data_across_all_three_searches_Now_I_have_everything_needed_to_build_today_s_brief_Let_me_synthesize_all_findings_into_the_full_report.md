Excellent — rich, validated data across all three searches. Now I have everything needed to build today's brief. Let me synthesize all findings into the full report.

---

**Subject: Daily Early-Diagnosis Brief — Pancreatic Ductal Adenocarcinoma (PDAC) — 2026-06-20**

---

## 1) Snapshot (one line)

**Pancreatic Ductal Adenocarcinoma (PDAC)** — why early diagnosis fails in practice: The pancreas is anatomically silent and symptomatically invisible until late-stage disease; no population-level screening protocol exists, and the only approved blood marker (CA 19-9) is functionally blind at the one stage where surgery can save lives.

---

## 2) Why Early Diagnosis Fails (3–5 bullets)

- **Biological barrier:** The pancreas sits deep in the retroperitoneum; early tumors cause no jaundice, no mass effect, no organ dysfunction — symptoms (mild back pain, bloating, weight loss) are indistinguishable from GERD, IBS, or musculoskeletal pain for 12–18 months. Preclinical tumour biology progresses through PanIN lesions for years before imaging visibility.
- **Test limitation:** CA 19-9 sensitivity at Stage I/II is ~50–70% and is falsely elevated in pancreatitis, biliary obstruction, and diabetes — conditions that are common in the exact population at risk. It is not approved or recommended for population screening. No single validated early-detection blood test exists at scale.
- **Imaging blind spot:** Standard CT and MRI miss sub-centimetre lesions; endoscopic ultrasound (EUS) is invasive and operator-dependent. Routine abdominal imaging is not performed in asymptomatic individuals, so there is no incidental detection pathway.
- **System failure — risk stratification:** New-onset diabetes (a 5× elevated PDAC risk signal) is managed by primary care as a metabolic condition, with no reflex pancreatic imaging protocol. BRCA2/PALB2 carriers without dense family history fall outside surveillance guidelines entirely.
- **Surgical attrition:** Even when early-stage disease is identified, 71.4% of clinical Stage I patients never receive surgery — driven by care coordination failure, clinical pessimism, and lack of high-volume surgical centres in community settings (only ~26% of patients reach academic centres).

---

## 3) Detection Window & Gap (concise)

| Milestone | Time / Marker |
|---|---|
| **Earliest detectable signal (research/ideal)** | PanIN-2/3 lesions detectable via REDMOD AI on CT: median 475 days (~16 months) before clinical diagnosis |
| **Liquid biopsy (PAC-MANN + CA 19-9)** | Early-stage blood detection with 85% accuracy (Science Translational Medicine, Feb 2025) |
| **New-onset diabetes as prodrome** | Occurs avg. 8 months before PDAC diagnosis; 40% of cases diagnosed ≥1 year after diabetes onset |
| **Typical clinical detection** | Stage III/IV in ~80% of patients; median survival ~12 months post-diagnosis |
| **Gap to close** | **16–24 months of actionable lead time is being lost.** Closing even 50% of this gap would shift 10–15% of diagnoses to resectable stages — translating to a ~30% improvement in 5-year survival for those patients |

---

## 4) What's Being Used Today (Gold Standard + Emergent)

**Gold Standards:**
- **CT abdomen/pelvis (contrast-enhanced):** Primary imaging — misses sub-centimetre lesions; sensitivity ~70–80% at Stage III+, far lower at Stage I
- **Endoscopic Ultrasound (EUS) ± biopsy:** Best spatial resolution for pancreatic head lesions; invasive, operator-dependent, not scalable for screening
- **CA 19-9 serum:** Elevated in ~80% of advanced PDAC, but only 50–70% at early stage; 10% of patients are Lewis antigen-negative and never produce it
- **ERCP:** For biliary/ductal evaluation; therapeutic more than diagnostic

**Emerging Research / Tools (2025–2026):**
| Tool | What It Does | Key Metric |
|---|---|---|
| **REDMOD (Mayo Clinic, *Gut BMJ* Apr 2026)** | AI radiomic analysis of routine CT for visually occult PDAC | Sensitivity 73% vs. radiologist 38.9%; AUC 0.82; lead time 475 days |
| **PAC-MANN (OHSU, *Sci Transl Med* Feb 2025)** | Blood protease-activity nanosensor + CA 19-9 | 85% accuracy early-stage; 98% PDAC vs. healthy controls |
| **4-Biomarker Panel — ANPEP+PIGR+CA19-9+THBS2 (Penn/Mayo, *Clin Cancer Res* Feb 2026)** | Plasma protein panel | 87.5% sensitivity Stage I-II; AUC 0.96–0.97 |
| **ctDNA liquid biopsy** | Circulating tumour DNA for MRD and early genomic profiling | Sensitivity low at Stage I (~30–40%), rising rapidly with tech improvement |
| **Exosome-based microRNA panels** | Cancer-derived vesicles carrying stable early-signal RNA | Pre-clinical / early validation phase |
| **UC San Diego rapid blood test** | Single-drop POC biomarker screen | Proof-of-concept; minutes turnaround |
| **Paper-based graphene oxide biosensors (PEAK1 kinase)** | POC immunosensor | Lab-stage; no clinical validation yet |

**Main Limitations:**
- REDMOD requires CT infrastructure and retrospective validation at community hospitals
- PAC-MANN and 4-biomarker panel need large prospective validation before clinical adoption
- ctDNA sensitivity remains low at Stage I — tumour-shed DNA is minimal
- All emerging tools currently lack FDA clearance for PDAC screening indication

---

## 5) Where Healthcare is Failing (Operational Insight)

**Screening point that drops the ball:**
> **Primary care and endocrinology clinics** — where new-onset diabetes is managed as a metabolic condition without any reflex pancreatic workup. The REGARD Study (*Gastroenterology*, Aug 2025) confirmed new-onset diabetes precedes PDAC diagnosis by an average of **8 months**, yet no standardised protocol triggers imaging or specialist referral. This is the single biggest missed window in the entire PDAC diagnostic pathway.

**Bottleneck most fixable in 90 days:**
> **Implementing a "New-Onset Diabetes + PDAC Risk" reflex protocol in EHR systems.** A simple rule-based alert — patient age >50, new HbA1c ≥6.5%, no prior diabetes history, BMI not consistent with obesity-driven T2DM, weight loss ≥5% — triggers CA 19-9 + abdominal CT referral. This requires no new technology; only EHR configuration and a clinical protocol.

**High-risk population missed:**
- **BRCA2/PALB2 germline carriers** without ≥2 affected first-degree relatives — fall outside CAPS (Cancer of the Pancreas Screening) consortium guidelines; estimated to represent 3–5% of all PDAC cases
- **New-onset diabetes patients over 50** — a 5× elevated risk cohort with no active surveillance
- **Chronic pancreatitis patients** — 5–10× elevated lifetime risk; often tracked by gastroenterology without structured PDAC surveillance intervals
- **Community hospital patients** — 74% of PDAC patients never reach a high-volume academic surgical centre

---

## 6) Three High-Leverage Solution Ideas (Practical, Ranked)

### 🥇 Idea A — EHR-Triggered "New-Onset Diabetes → PDAC Reflex Protocol" *(30-day pilot)*
**What:** Build a clinical decision support (CDS) rule in Epic/Cerner: patient aged 50–80, new HbA1c ≥6.5% or fasting glucose ≥126 mg/dL, no prior diabetes diagnosis, weight loss ≥5% in 6 months → auto-generate an order set: CA 19-9 serum + abdominal CT with contrast + gastroenterology referral.

**How to run the pilot:**
- Partner with 2–3 primary care or endocrinology practices at a single academic health system
- Configure EHR alert (Epic BestPractice Advisory or equivalent) — 2–3 weeks of IT work
- Run for 60 days; capture: alert trigger rate, physician override rate, CA 19-9 results distribution, CT findings, referral completion rate
- **Metrics to collect:** Number of alerts fired / accepted / overridden; time from diabetes diagnosis to CT completion; proportion with elevated CA 19-9; any incidental PDAC findings (even one early-stage detection validates the protocol)

**Cost:** Near-zero marginal cost. Primarily EHR configuration + clinician education.

---

### 🥈 Idea B — Integrate REDMOD AI into Routine Abdominal CT Read Workflow *(60–90 day pilot)*
**What:** Deploy the Mayo Clinic REDMOD model (or equivalent radiomic AI) as a background secondary-read layer on all abdominal CT scans performed for *any* indication in patients aged 50+ — flagging cases with elevated PDAC radiomic risk scores for radiologist review.

**How to run:**
- Identify a radiology department willing to run a prospective shadow-mode pilot (AI flags cases but does not alter primary read)
- Resource checklist: DICOM pipeline access, GPU inference server or cloud API, IRB approval, radiologist education session (2 hrs)
- Run for 90 days on all abdominopelvic CTs in the 50+ cohort
- **Expected impact:** Based on REDMOD's 73% sensitivity vs. 38.9% for radiologists alone, the model should flag a meaningful proportion of "normal" scans that warrant follow-up EUS or repeat CT in 3 months
- **Metrics:** Number of scans processed; AI flag rate; radiologist concordance rate; downstream workup triggered; any new PDAC diagnoses within 6 months of flagged scans

**Collaborators to approach:** Mayo Clinic AI Lab (REDMOD authors), Gradient Health (de-identified DICOM data), Nuance/Microsoft (AI radiology integration)

---

### 🥉 Idea C — Multi-Biomarker Blood Panel Deployment as High-Risk Surveillance Tool *(Research/Product — 90 days to pilot spec)*
**What:** Build a structured surveillance program using the 4-biomarker plasma panel (ANPEP + PIGR + CA 19-9 + THBS2) for a defined high-risk cohort: BRCA2/PALB2 carriers, new-onset diabetes 50+, and chronic pancreatitis patients. Run annual or semi-annual blood draws with reflexive EUS if panel score exceeds threshold.

**Tests needed:**
- Prospective validation in a multi-site cohort (n=500 high-risk, n=500 age-matched controls) — 12–18 months
- Assay standardisation across clinical labs (ELISA vs. mass spec for ANPEP/PIGR)
- Cost modelling: target <$150/panel to be reimbursable

**Startup angle:** Build a CLIA-certified lab-developed test (LDT) around this panel. Partner with genetic testing companies (Invitae, Color) who already hold BRCA2/PALB2 data and have consent for longitudinal follow-up. This is a defensible data moat — the genetic + longitudinal biomarker dataset is the product.

**Collaborators:** Penn Medicine (Dr. Erica Carpenter's lab), Mayo Clinic GI oncology, PanCAN's Precision Promise trial network, Tempus AI for multi-omic integration.

---

## 7) First-Principles Signal Hunt (What We Should Measure Earlier)

**Hidden signal candidate:**
> **New-onset diabetes glycemic trajectory + protease activity in blood** — the combination of (a) rapid HbA1c escalation without classical obesity risk factors and (b) elevated blood protease activity (PAC-MANN signal) creates a two-hit early-warning fingerprint that precedes imaging visibility by 12–18 months. Neither signal alone is sufficient; together they could form a ~90% specific screening rule.

**Secondary candidate:** Exosome-derived microRNA panels (miR-196a, miR-217) in plasma — these are shed by PanIN lesions before invasive cancer forms and are detectable in peripheral blood, though still in early validation.

**Minimal sampling change needed:**
- **Blood only** — no invasive procedure required for the first-line screen
- Add-on to routine HbA1c draw at diabetes diagnosis: 1 extra EDTA tube for CA 19-9 + protease activity panel
- No fasting required; no specialist visit needed at initial screen
- Reflexive EUS only if blood panel is positive → dramatically reduces unnecessary invasive workup

---

## 8) Strategic Value & Next Immediate Actions (CEO Lens)

**Public health impact:**
- ~67,000 new PDAC diagnoses/year in the US (2026); 3rd leading cause of cancer death
- Overall 5-year survival: **13%** — unchanged for a decade
- If 20% more patients were diagnosed at Stage I/II (from ~20% to ~40%), the math yields ~8,000–10,000 additional patients/year entering the resectable surgical window — at a Stage I survival rate of ~44%, this is thousands of lives annually
- Economic burden: PDAC costs the US healthcare system ~$4.9B/year in direct costs; late-stage care is 3–4× more expensive than early resection

**3 Immediate Actions:**

| Timeline | Action |
|---|---|
| **Today** | Read: REGARD Study (*Gastroenterology*, Aug 2025) on new-onset diabetes as PDAC prodrome + REDMOD paper (*Gut BMJ*, Apr 2026). Map your institution's EHR CDS capability — find the Epic/Cerner analyst who owns BestPractice Advisory rules. |
| **7 Days** | Identify 2 clinical champions: (1) a primary care/endocrinology physician willing to co-design the new-onset diabetes reflex protocol, (2) a GI oncologist or radiologist interested in AI-augmented CT reads. Draft a 1-page pilot proposal for IRB pre-submission. |
| **30 Days** | Submit IRB protocol for the EHR-triggered new-onset diabetes → PDAC workup pilot. Simultaneously, contact Penn Medicine (ANPEP/PIGR panel team) and Mayo Clinic AI Lab (REDMOD) to explore co-investigation or licensing. Define your primary metric: *time from diabetes diagnosis to PDAC imaging* — this is your north-star KPI. |

---

## 9) One-Minute Mental Model

> *"Pancreatic cancer hides inside two Trojan horses — new-onset diabetes and a 'normal' CT scan — and the healthcare system treats both as benign. The leverage point is building a reflex bridge: every new diabetes diagnosis in a 50+ patient without classical obesity triggers a one-tube blood screen, and every 'normal' abdominal CT in a high-risk patient gets a 10-second AI radiomic re-read. Neither intervention requires a new device or a new clinic visit — just a protocol and an algorithm."*

**2–3 Search Keywords / Papers for Immediate Literature Lookup:**
1. `"REGARD study new-onset diabetes pancreatic cancer Gastroenterology 2025"` — validates diabetes as prodrome
2. `"REDMOD gutjnl-2025-337266 Gut BMJ 2026"` — Mayo Clinic AI radiomic model full paper
3. `"PAC-MANN protease activity pancreatic cancer Science Translational Medicine 2025 OHSU"` — blood-based protease nanosensor

---

## 10) Pattern Insight (Meta-Learning)

**What recurring diagnostic failure pattern is emerging?**

Across the diseases reviewed in this series, a **"signal-in-plain-sight" pattern** is crystallising: the earliest detectable signal for many high-mortality diseases is *already present* in routine clinical data — it is simply never connected to the disease it predicts. In PDAC, new-onset diabetes is documented in the EHR months before the cancer diagnosis. In Alzheimer's, subtle cognitive scores exist in routine notes years before dementia. In sepsis, vital sign trends precede clinical recognition by hours. In every case, the data exists; the **reflex logic does not.**

**Is today's disease reinforcing or breaking the pattern?**
> **Strongly reinforcing.** PDAC is the canonical example: a 5× elevated risk signal (new-onset diabetes) sits dormant in the primary care record while the tumour progresses to Stage IV. The system treats the signal as a separate disease rather than a red flag for a third condition.

**What generalizable opportunity is forming across diseases?**
> The **cross-disease opportunity** is a **"risk-signal reflex engine"** — a disease-agnostic EHR layer that maps known prodromal signals (metabolic, genomic, imaging-textural) to downstream cancer/disease risk, and automatically triggers a lightweight, non-invasive first-line screen. This is not a single-disease startup; it is a **platform play** — one that could be applied to PDAC (diabetes → CA19-9), ovarian cancer (bloating + CA-125 trajectory), Alzheimer's (MCI notation → p-tau217 blood draw), and ALS (fasciculation complaints → EMG referral). The underlying architecture — EHR signal → risk score → reflex order set — is identical across all four. **The founder who builds the disease-agnostic reflex engine, not the disease-specific biomarker, captures the largest long-term value.**

---
*Brief compiled: Saturday, 20 June 2026 | Sources: OHSU News, Gut BMJ (Apr 2026), Clinical Cancer Research (Feb 2026), Gastroenterology REGARD Study (Aug 2025), PanCAN, SEER/ACS Cancer Facts & Figures 2026, Penn Medicine, Mayo Clinic News Network*