Subject: Daily Early-Diagnosis Brief — Pancreatic Ductal Adenocarcinoma (PDAC) — 2026-05-24

**1) Snapshot (one line)**
Pancreatic Ductal Adenocarcinoma (PDAC) — why early diagnosis fails in practice: Deep anatomical location masks symptoms until metastasis, while visually occult pre-diagnostic tissue changes are missed on routine imaging and ignored by standard blood work.

**2) Why early diagnosis fails (3–5 bullets)**
*   **Biological barrier:** Tumors develop in the retroperitoneum, causing vague, non-specific symptoms (back pain, mild weight loss) until late-stage biliary obstruction or metastasis occurs.
*   **Test limitation:** The standard biomarker (CA 19-9) has low sensitivity and specificity for early-stage disease and frequently elevates in benign conditions.
*   **System failure:** Routine abdominal CT scans fail to visually capture early micro-architectural changes, and there is no automated reflex screening for the highest-risk early clinical indicator: new-onset atypical diabetes in patients over 50.

**3) Detection window & gap (concise)**
*   **Earliest detectable signal (research / ideal):** 16 to 36 months pre-diagnosis (radiomic changes via AI on CT) or epigenetic shifts (cfDNA methylation).
*   **Typical clinical detection:** Stage III/IV (locally advanced or metastatic).
*   **Gap to close:** 1.5 to 3 years (shifting detection from unresectable to surgical candidates, potentially raising 5-year survival from 13% to >50%).

**4) What’s being used today (gold standard + emergent)**
*   **Gold standard(s):** High-resolution Pancreatic Protocol CT/MRI, Endoscopic Ultrasound (EUS) with Fine-Needle Aspiration (FNA), CA 19-9 blood test.
*   **Emerging research / tools:** REDMOD AI model (analyzing pre-diagnostic CTs), cfDNA methylation assays (ZFP30 & ZNF781 / EG-Pancreatic Blood Test-E1), exosome multi-omics, Craif's "Bio-AI" (miSignal).
*   **Main limitations:** Pancreatic protocol CTs are expensive and not used for broad screening; EUS is highly invasive and operator-dependent; novel liquid biopsies still face false-positive hurdles when differentiating PDAC from chronic pancreatitis.

**5) Where healthcare is failing (operational insight)**
*   **Screening point that drops the ball:** Incidental abdominal CTs ordered for unrelated GI complaints, where human eyes routinely miss "visually occult" pre-diagnostic changes.
*   **Bottleneck most fixable in 90 days:** Lack of centralized reflex testing/imaging for patients >50 presenting in primary care with new-onset diabetes and unexplained weight loss.
*   **High-risk population missed:** Patients with familial risk (BRCA1/2, PALB2) or new-onset atypical diabetes who are managed entirely in primary care without oncology/GI referral until jaundice appears.

**6) 3 High-leverage solution ideas (practical, ranked)**
*   **[Idea A — quick pilotable] Centralized "New-Onset Diabetes" Alert Protocol:** Run a 90-day pilot in a mid-sized health system's EHR. Flag all patients >50 with new-onset diabetes + weight loss. Auto-trigger a reflex CA 19-9 and a fast-track Pancreatic Protocol MRI. *(Metrics to collect: % of flagged patients imaged, early-stage yield rate, time-to-scan).*
*   **[Idea B — scalable tech / workflow change] Retrospective AI Imaging Overlay:** Deploy an FDA-breakthrough-designated AI model (like REDMOD) as a background processing layer on all routine abdominal CTs across a hospital network. *(Resource checklist: PACS integration, AI vendor API, radiology sign-off; Expected impact: Catching visually occult PDAC 1-3 years earlier).*
*   **[Idea C — research / product] Point-of-Care Epigenetic Triage:** Develop a low-cost, primary-care-friendly blood test focusing exclusively on ZFP30/ZNF781 cfDNA methylation and exosome profiles to triage high-risk patients before expensive imaging. *(Highest upside; needs clinical validation against chronic pancreatitis cohorts; approach PRECEDE Consortium for trial collaboration).*

**7) First-principles signal hunt (what we should measure earlier)**
*   **Hidden signal candidate:** Visually occult micro-architectural tissue changes (radiomics) and early host transcriptomic/epigenetic shifts (5mC/5hmC methylation profiles).
*   **Minimal sampling change needed:** Routing existing, routine abdominal CT scans through an AI radiomic filter before radiologist review, and adding a 10mL blood draw for cfDNA methylation to standard A1C checks in new-onset diabetics.

**8) Strategic value & next immediate actions (CEO lens)**
*   **Public health impact:** ~64,000 new cases/year (US) with a dismal ~13% 5-year survival rate; currently the 3rd leading cause of cancer death, projected to become the 2nd.
*   **3 immediate actions for you (today → 7 days → 30 days):**
    *   **Today:** Review the Mayo Clinic REDMOD AI model validation studies and the recent ASCO data on the EG-Pancreatic Blood Test-E1.
    *   **7 days:** Identify 1-2 regional health systems with large primary care networks to discuss a retrospective EHR data pilot on new-onset diabetes patients.
    *   **30 days:** Draft a pilot spec for integrating an AI radiomics tool into a partner hospital's PACS system to analyze historical CTs of known PDAC patients to definitively prove the 16-36 month local detection gap.

**9) One-minute mental model**
"PDAC hides in plain sight by mimicking aging (back pain, diabetes) and staying invisible to the human eye on standard scans; the leverage point is turning routine, unrelated CTs and A1C tests into opportunistic, AI-filtered screening events."

**Attach:**
*   "REDMOD AI model CT scan" (Mayo Clinic visually occult PDAC detection)
*   "EG-Pancreatic Blood Test-E1" (ZFP30 cfDNA methylation)
*   "Cell-free DNA testing for the detection and prognosis prediction of pancreatic cancer" (Nature Communications)
*   PRECEDE Consortium / CAPS5 Study

**10) Pattern Insight (Meta-Learning)**
*   **What recurring diagnostic failure pattern is emerging?** The "Siloed Incidental Data" pattern — valuable early-warning data (routine CTs, primary care A1C labs) is collected for other clinical reasons but never cross-referenced or analyzed with high-sensitivity, disease-specific AI.
*   **Is today’s disease reinforcing or breaking that pattern?** Strongly reinforcing. The data to detect PDAC 1-3 years earlier already exists in hospital PACS systems and primary care EHRs; it just isn't being looked at through the right lens.
*   **What generalizable opportunity is forming across diseases?** Opportunistic Screening Platforms. The biggest asymmetric startup upside lies not in creating net-new, expensive screening pathways, but in building software layers that passively mine existing, routine primary-care touchpoints (standard blood panels, routine imaging) for secondary, high-impact diagnoses.