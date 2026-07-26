Subject: Daily Early-Diagnosis Brief — Pancreatic Ductal Adenocarcinoma (PDAC) — 2026-05-13

1) Snapshot (one line)
Pancreatic Ductal Adenocarcinoma (PDAC) — why early diagnosis fails in practice: Deep anatomical seating combined with severe biological scarcity of early shedding biomarkers and missed opportunistic clinical signals (like new-onset diabetes).

2) Why early diagnosis fails (3–5 bullets)
*   **Biological barrier:** Intense stromal/desmoplastic reaction creates a fibrotic "fortress" around the tumor, causing an absolute scarcity of circulating tumor DNA (ctDNA) in the blood during highly curable Stages I/II.
*   **Test limitation:** The current blood marker, CA 19-9, lacks sensitivity (misses non-secretors) and specificity (elevated in benign biliary issues); baseline liquid biopsies fail due to the low-shedding nature of early PDAC.
*   **System failure:** Siloed EHRs fail to flag high-risk clinical "sentinel" events—specifically New-Onset Diabetes Mellitus (NODM) in adults over 50—treating it as a routine endocrine issue rather than a potential oncologic warning.

3) Detection window & gap (concise)
*   **Earliest detectable signal (research / ideal):** 10 years prior (Sequential Proteomic Relay in tissues) / 12–18 months prior (AI detecting visually occult signals on routine CTs).
*   **Typical clinical detection:** Stage III/IV upon onset of jaundice, severe back pain, or sudden weight loss.
*   **Gap to close:** 12 to 18 months (radiological). Closing this 475-day gap shifts detection to resectable Stage I/II, dramatically improving the 5-year survival rate from <13% to >50%.

4) What’s being used today (gold standard + emergent)
*   **Gold standard(s):** Multiphasic contrast-enhanced CT (pancreatic protocol) and Endoscopic Ultrasound (EUS) with fine-needle aspiration (used reactively, post-symptoms).
*   **Emerging research / tools:** AI models (e.g., REDMOD) running opportunistically on non-pancreatic CTs; Exosome profiling (differentiates early PDAC from benign disease better than ctDNA); EndPAC clinical risk score for EHRs.
*   **Main limitations:** Liquid biopsy struggles with low early-stage ctDNA volume; EUS is too invasive, operator-dependent, and costly for general population screening.

5) Where healthcare is failing (operational insight)
*   **Screening point that drops the ball:** Primary care and endocrinology treating New-Onset Diabetes Mellitus (NODM) in patients >50 without reflexively ordering a pancreatic MRI or EUS.
*   **Bottleneck most fixable in 90 days:** Automating the EndPAC risk score calculation in Epic/Cerner to trigger a hard-stop alert for a pancreatic workup when an older patient presents with NODM and weight loss.
*   **High-risk population missed:** Patients with incidental pancreatic cysts (IPMNs) noted on routine abdominal scans who are lost to follow-up due to complex surveillance guidelines and the lack of automated tracking or dedicated "cyst clinics."

6) 3 High-leverage solution ideas (practical, ranked)
*   **[Idea A — quick pilotable] EHR-Triggered NODM Triage:** Run a 90-day pilot in a mid-sized health system computing the EndPAC score in the background for all patients >50 diagnosed with diabetes. Metrics to collect: Number of flags generated, percentage of resulting MRIs/EUS ordered, and early lesions found.
*   **[Idea B — scalable tech / workflow change] Opportunistic AI CT Screening:** Partner with a radiology department to run an AI model retroactively on the last 10,000 routine abdominal CTs (done for kidney stones, GI pain) to flag visually occult morphological changes. Resource checklist: De-identified PACS access, AI vendor API (e.g., REDMOD), 1 radiologist for validation. Expected impact: Catching Stage I tumors up to 475 days earlier with zero new patient scans.
*   **[Idea C — research / product] Exosome-First Liquid Biopsy:** Highest upside startup play. Since ctDNA is scarce, build a diagnostic isolating pancreatic-derived exosomes (extracellular vesicles) from standard blood draws. Tests needed: Validation against benign chronic pancreatitis. Collaborators to approach: PRECEDE Consortium researchers.

7) First-principles signal hunt (what we should measure earlier)
*   **Hidden signal candidate:** Exosomes (extracellular vesicles). Unlike necrotic tumor DNA (ctDNA) which passively leaks, exosomes actively cross the dense desmoplastic stroma into the bloodstream long before the tumor breaks down.
*   **Minimal sampling change needed:** Standard peripheral blood draw, but utilizing advanced microfluidics/ultracentrifugation to isolate exosomes rather than cell-free DNA.

8) Strategic value & next immediate actions (CEO lens)
*   **Public health impact:** ~64,000 cases/year in the US; 3rd leading cause of cancer death with a dismal 13% 5-year survival rate. Shifting stage at diagnosis is the *only* proven way to alter mortality.
*   **Today:** Contact the authors of the May 2026 *Gut* paper on "Next-generation AI for visually occult pancreatic cancer detection" or the REDMOD AI team to discuss commercialization/licensing.
*   **7 days:** Map out the exact Epic/Cerner logic required to calculate the EndPAC score and draft a pilot proposal for a local hospital's IT steering committee.
*   **30 days:** Finalize a pilot spec for a "Retroactive Opportunistic CT Scan" AI run, securing IRB exemption for a de-identified retrospective data pull.

9) One-minute mental model
“Pancreatic cancer builds a fibrotic fortress (desmoplasia) that traps early DNA signals, but it leaks metabolic changes (new-onset diabetes) and microscopic structural shifts (detectable by AI on routine CTs) 18 months before symptoms.”
*Attach: "A Sequential Proteomic Relay Defines a Decade-long Pre-Diagnostic Window for Pancreatic Cancer" (Feb 2026); REDMOD AI; EndPAC risk score; PANDOME study.*

10) Pattern Insight (Meta-Learning)
*   **What recurring diagnostic failure pattern is emerging?** The "Siloed Sentinel Event" — a systemic disease presents its first symptom in a completely different specialty (e.g., cancer presenting as endocrine failure/diabetes), and the EHR fails to connect the dots.
*   **Is today’s disease reinforcing or breaking that pattern?** Strongly reinforcing. NODM is treated purely as an endocrine issue rather than a potential oncologic warning sign.
*   **What generalizable opportunity is forming across diseases?** "Reflex AI Triage." Building middleware that sits on top of EHRs and PACS to passively monitor routine data (blood work, opportunistic imaging, new chronic diagnoses) and automatically trigger specialized screening pathways without relying on primary care intuition.