Excellent research. Now I have everything I need to produce today's decision-grade brief. Let me synthesize all findings into the exact template format.

---

**Subject: Daily Early-Diagnosis Brief — Pancreatic Ductal Adenocarcinoma (PDAC) — 2026-05-27**

---

## 1) Snapshot (one line)

**Pancreatic Ductal Adenocarcinoma (PDAC)** — early diagnosis fails because the tumor grows silently in a retroperitoneal organ with no reliable early biomarker, no population-level screening protocol, and a clinical presentation that mimics benign GI conditions until the disease is surgically incurable.

---

## 2) Why Early Diagnosis Fails (3–5 bullets)

- **Biological barrier:** PDAC is anatomically hidden (retroperitoneal), produces no early pain signal, and sheds minimal ctDNA/cfDNA at Stage I–II; CA19-9 is falsely negative in ~20% of patients (Lewis antigen-negative genotype) and non-specific in early disease. Precursor lesions (PanIN-1/2) are sub-5mm — invisible to any current clinical imaging.
- **Test limitation:** CA19-9 has only ~79% sensitivity and ~82% specificity at clinical diagnosis — far worse in Stage I (~50%). CT scan misses Stage 0 lesions 90% of the time. EUS, the most sensitive early tool, is invasive, expensive, operator-dependent, and not deployed at scale. No FDA-approved blood test exists for PDAC-specific early screening.
- **System failure (screening policy):** There is no population-level pancreatic cancer screening program anywhere in the world. High-risk groups (BRCA2, PALB2, ATM mutation carriers; familial pancreatic cancer; Peutz-Jeghers; chronic pancreatitis; new-onset diabetes >50 years) are chronically under-enrolled in surveillance programs due to fragmented genetics referral pipelines.
- **System failure (workflow):** New-onset diabetes in adults over 50 — a known PDAC prodrome — is managed exclusively by primary care/endocrinology with zero oncology reflex. The median window from new-onset diabetes to PDAC diagnosis is 6–36 months — a missed interception point.
- **Diagnostic odyssey:** 64% of patients experience a diagnostic interval >3 months from symptom onset. The median symptom-to-treatment time is 4.9 months. By presentation, ~80% are Stage III–IV — beyond curative resection.

---

## 3) Detection Window & Gap

| Marker / Stage | Earliest Detectable Signal | Typical Clinical Detection | Gap |
|---|---|---|---|
| PanIN precursor lesion | Experimental (pancreatic juice cytology, cfDNA methylation) | Not detected clinically | Years |
| Stage I PDAC (≤2 cm, node-negative) | ctDNA + methylation panels (research) | Rarely detected; ~10% of diagnoses | 12–24 months |
| Stage II PDAC | EUS in high-risk surveillance | Symptomatic CT presentation | 6–12 months |
| Visually occult on CT | Mayo Clinic AI model: **475 days (15+ months)** before clinical diagnosis | Radiologist misses; CT reads as normal | **~15 months gap** |
| Clinical diagnosis (all-comers) | Symptom onset → diagnosis: 4.9 months median | Stage III–IV at presentation in 80% | Curative window already closed |

**Gap to close:** The highest-leverage gap is the **12–18 month window** between when an AI model can detect pre-diagnostic signal on routine CT and when a radiologist calls it. Additionally, the **new-onset diabetes → PDAC interception window** of 6–36 months is entirely unused in clinical practice.

---

## 4) What's Being Used Today

**Gold Standards:**
- **CA19-9 serum assay** — standard of care, but poor early sensitivity (~50% Stage I); fails in Lewis-antigen-negative patients
- **CT Abdomen/Pelvis (contrast-enhanced)** — primary imaging; misses Stage 0 (90% miss rate) and small tumors <1 cm
- **EUS ± FNA/FNB** — highest sensitivity for early lesions (80–95%); specificity 92–100%; Stage 0 sensitivity 24.4% vs CT's 10% — but invasive, resource-intensive, not scalable

**Emerging Research / Tools (2025–2026):**
- **Mayo Clinic AI CT model** *(Gut BMJ, April 2026)*: Detects visually occult PDAC on routine CT at a median lead time of **475 days** before clinical diagnosis — the single most actionable near-term tool
- **Exosome-based liquid biopsy + CA19-9 combo**: 97% sensitivity for Stage I–II PDAC (AACR 2025 data) — not yet commercially available
- **cfDNA methylation assays**: Epi-TOP Pancreatic Assay (7 differentially methylated genes + KRAS), PDACatch (Singlera Technologies) — sensitivity ~83.7%; specificity high
- **Multi-Cancer Early Detection (MCED) tests**: Galleri (GRAIL), CancerGuard™ (Exact Sciences) — 68% sensitivity for high-mortality cancers including PDAC; FDA review pathway underway
- **5-hydroxymethylcytosine (5hmC) profiling** in cfDNA — emerging epigenetic signal detectable in early-stage PDAC
- **AI-assisted EUS** — deep learning models improving lesion characterization; reducing operator dependency

**Main Limitations:**
- Exosome assay: not yet FDA-cleared, no commercial rollout
- cfDNA methylation: low tumor DNA shedding at Stage I limits sensitivity; needs large validation cohorts
- MCED tests: PDAC-specific sensitivity still suboptimal at 40–68% for Stage I; high cost (~$900–$1,200/test); no reimbursement
- Mayo AI model: requires prospective validation; needs integration into PACS/radiology workflow

---

## 5) Where Healthcare Is Failing (Operational Insight)

**Screening point that drops the ball:**
- **Primary care / endocrinology:** New-onset diabetes in patients >50 years is a validated PDAC prodrome (3–4× elevated risk), yet zero oncology reflex exists. This is the single most underutilized interception point in real-world medicine.
- **Radiology read pipeline:** Routine CT scans (ordered for GI complaints, renal stones, abdominal pain) contain pre-diagnostic PDAC signal that radiologists miss — now demonstrably detectable by AI 15 months earlier. There is no AI second-read deployed in standard radiology workflow for pancreatic risk.
- **Genetics/familial risk:** BRCA2, PALB2, ATM, CDKN2A carriers — who have 3–10× elevated PDAC risk — are not systematically enrolled in pancreatic surveillance. Genetic counseling pipelines rarely trigger GI/pancreatic surveillance referrals.

**Bottleneck most fixable in 90 days:**
- **Deploy the Mayo Clinic AI model (or equivalent) as a reflex read on all abdominal CTs** in a single academic hospital — flag pre-diagnostic pancreatic findings for structured radiologist review. This requires PACS integration, not new equipment.
- **Create a "new-onset diabetes + age >50" EHR alert** that auto-triggers a CA19-9 + pancreatic protocol CT order — a workflow rule changeable within 30–60 days in any Epic/Cerner system.

**High-risk population missed:**
- **New-onset diabetics >50** — managed entirely in primary care/endocrinology with no oncology crossover
- **BRCA2/PALB2/ATM carriers** — known from cancer genetics but not enrolled in pancreatic surveillance (unlike BRCA → breast/ovarian pipelines which are mature)
- **Chronic pancreatitis patients** — 5-year cumulative PDAC risk ~1.8%, 20-year risk ~4%; followed by GI but rarely with structured PDAC screening intervals

---

## 6) 3 High-Leverage Solution Ideas (Practical, Ranked)

### 🥇 Idea A — EHR Alert: New-Onset Diabetes → PDAC Reflex Screen *(30-day pilot, highest ROI)*
**Concept:** Build an Epic/Cerner BPA (Best Practice Advisory) that fires when a patient: (a) is ≥50 years old, (b) receives a new ICD-10 code for Type 2 diabetes or "diabetes unspecified," and (c) has no prior diabetes diagnosis in the last 5 years. Alert recommends: CA19-9 + pancreatic protocol CT within 60 days.

**30-day pilot spec:**
- Site: 1 academic medical center with Epic access
- Partners: Primary care chief, endocrinology, GI/oncology
- Metrics: # alerts fired, # CA19-9 ordered, # CT ordered, # incidental PDAC findings, alert acceptance rate, time-to-imaging from alert
- Cost: ~$5–10K (IT build); near-zero incremental cost per alert
- Expected impact: If 1 in 200 new-onset diabetics >50 has occult PDAC (literature estimate), a 500-patient pilot should surface 2–3 early-stage diagnoses

**Success threshold:** >40% alert acceptance rate; ≥1 PDAC or IPMN finding per 200 alerts

---

### 🥈 Idea B — AI CT Second-Read for Pancreatic Risk *(60–90 day pilot, scalable)*
**Concept:** Integrate the Mayo Clinic AI PDAC detection model (or equivalent — Pancreasense, Enlitic, or academic collaboration) into the radiology PACS workflow as a background read on all contrast-enhanced abdominal CTs. Radiologist receives a structured flag: "AI: Pancreatic risk signal detected — recommend dedicated pancreatic protocol CT."

**Resource checklist:**
- PACS/AI integration vendor agreement (60 days)
- IRB approval for retrospective validation on local CT archive (30 days)
- Radiology department buy-in + structured reporting template
- Radiologist education: 1-hour CME on AI flag interpretation
- IT: DICOM routing rule to AI inference server

**Expected impact:** Based on Mayo data (475-day lead time), a hospital reading 50,000 abdominal CTs/year with ~0.05% PDAC incidence could flag 20–25 pre-diagnostic cases annually — vs. ~0 currently detected at Stage I in that same pool.

**Metrics:** AI flag rate, false positive rate (unnecessary follow-up CT), radiologist override rate, downstream PDAC diagnoses within 18 months of flagged scan

---

### 🥉 Idea C — cfDNA Methylation + CA19-9 Combo Panel for High-Risk Surveillance *(Research / Product, 90-day design phase)*
**Concept:** Partner with Singlera Technologies (PDACatch), or build a CLIA-lab validated panel combining: (1) cfDNA methylation (5–7 gene panel), (2) CA19-9, (3) CEA, (4) KRAS mutation in cfDNA — as a quarterly surveillance blood test for defined high-risk cohorts (BRCA2/PALB2/ATM carriers, familial PDAC, chronic pancreatitis, IPMN surveillance).

**90-day design phase actions:**
- Identify existing PDAC high-risk cohort registry (CAPS consortium, EUROPAC, or institutional)
- Negotiate sample access with biobank (residual serum from enrolled patients)
- Run retrospective case-control: 50 Stage I PDAC cases vs. 100 matched high-risk controls
- Primary endpoint: sensitivity/specificity of combo panel vs. CA19-9 alone
- Collaborators: Singlera Technologies, MD Anderson PDAC program, CAPS Study Group

**Highest upside:** If combo panel achieves >80% sensitivity at >90% specificity in Stage I, this becomes a reimbursable surveillance tool for a defined 2–3 million high-risk US population — a clear FDA Breakthrough Device pathway.

---

## 7) First-Principles Signal Hunt

**Hidden signal candidate:**
- **New-onset diabetes as a metabolic prodrome** — PDAC causes insulin resistance and beta-cell destruction 6–36 months before imaging-detectable tumor. The signal is already captured in EHR (HbA1c trajectory, fasting glucose, C-peptide) but never cross-referenced with cancer risk algorithms.
- **cfDNA fragment size distribution (fragmentomics)** — PDAC-derived cfDNA shows distinct fragment length profiles (shorter fragments, nucleosome positioning shifts) detectable before methylation or mutation signals. Fragmentomics + methylation = higher early sensitivity than either alone.
- **5-hydroxymethylcytosine (5hmC) in cfDNA** — tissue-specific 5hmC signatures are detectable in plasma at early PDAC stages; distinct from methylation and additive in multi-marker panels.

**Minimal sampling change needed:**
- **Blood (EDTA plasma, 10 mL)** — sufficient for cfDNA methylation + fragmentomics + CA19-9 in a single draw. No new sample type needed. The change is purely **algorithmic and assay** — not procedural.
- For new-onset diabetes interception: **no new blood draw** — CA19-9 can be added as a reflex to existing HbA1c/metabolic panel orders at zero additional patient inconvenience.

---

## 8) Strategic Value & Next Immediate Actions (CEO Lens)

**Public health impact:**
- PDAC: ~64,000 new US cases/year (2026 estimate); ~51,000 deaths/year — #3 cancer killer in the US, projected to become #2 by 2030
- 5-year survival: ~13% overall; **80%+ if caught at Stage IA** — the survival delta is among the largest of any cancer
- Global burden: ~500,000 new cases/year worldwide; rising incidence linked to obesity, T2DM, and aging populations
- Economic burden: Average cost of late-stage PDAC treatment ($150,000–$300,000/patient) vs. early curative resection — early detection is cost-dominant

**3 Immediate Actions for Ayan:**

| Timeline | Action |
|---|---|
| **Today** | Read the Mayo Clinic AI PDAC paper: *"Next-generation AI for visually occult pancreatic cancer detection in routine CT"* — Gut BMJ, April 22, 2026 (gutjnl-2025-337266). Assess whether this model is available for academic collaboration or licensing. |
| **7 days** | Map your institution's Epic/Cerner environment: identify whether a "new-onset diabetes + age >50" BPA alert is technically feasible. Schedule a 30-min call with your informatics/IT team and the endocrinology chief to scope the pilot. |
| **30 days** | Design the 90-day AI CT second-read pilot: draft a 1-page concept note for radiology leadership, identify PACS vendor compatibility, and submit an IRB pre-submission for retrospective CT validation. Simultaneously, identify your institution's BRCA2/PALB2 carrier registry and assess whether a pancreatic surveillance protocol exists — if not, propose one. |

---

## 9) One-Minute Mental Model

> *"PDAC hides behind three masks — a silent organ, a benign metabolic signal (new-onset diabetes), and a normal-looking CT — and the single leverage point is deploying AI to read what radiologists biologically cannot see, 15 months before the tumor declares itself."*

**2–3 search keywords / citations for immediate lookup:**
1. **"Next-generation AI for visually occult pancreatic cancer detection in routine CT"** — *Gut BMJ, April 2026* — DOI: gutjnl-2025-337266
2. **"PDACatch cfDNA methylation Singlera Technologies pancreatic cancer"** — search PubMed + company pipeline
3. **"CAPS Study Group pancreatic cancer surveillance high-risk"** — ongoing multicenter surveillance consortium; key collaborator network

---

## 10) Pattern Insight (Meta-Learning)

**Recurring diagnostic failure pattern — "The Silent Prodrome Problem":**

This is now the **third major pattern** emerging across high-impact diseases with diagnostic delay:

> **The disease announces itself early — but in a language that belongs to a different specialty.**

- In **PDAC**: new-onset diabetes is an oncology signal managed by endocrinology. The CT finding is a radiology signal missed without AI.
- In **ovarian cancer** (prior brief pattern): vague GI symptoms are a GI signal managed by gastroenterology, not gynecology.
- In **ALS / neurodegenerative disease**: subtle motor signs are a neurology signal, but patients first present to orthopedics or sports medicine.

**The generalizable opportunity forming:**
The gap is not just biological — it is **specialty siloing**. The early signal exists in a different clinical department than where the disease will ultimately be diagnosed and treated. The startup/hospital opportunity is **cross-specialty signal routing**: EHR algorithms, AI models, and reflex testing protocols that translate a signal from specialty A into an action in specialty B.

**This is the meta-pattern:** Build **cross-specialty diagnostic bridges** — not better tests within a single specialty. The new-onset diabetes → oncology alert is a perfect prototype. The AI CT flag → GI/oncology referral is another. The BRCA2 genetics result → pancreatic surveillance enrollment is a third.

**Is today's disease reinforcing or breaking the pattern?** Strongly **reinforcing** — PDAC is the canonical example of the silent prodrome + specialty silo failure. It also adds a new dimension: **AI as the cross-specialty translator** — the model that reads a radiologist's CT and speaks oncology.

---

*Brief generated: Wednesday, May 27, 2026 | UTC 09:00 | Research + Hospital Improvement focus | Sources: Gut BMJ 2026, AACR 2025, Frontiers in Oncology 2024, Exact Sciences, GRAIL, Singlera Technologies, CAPS Consortium*