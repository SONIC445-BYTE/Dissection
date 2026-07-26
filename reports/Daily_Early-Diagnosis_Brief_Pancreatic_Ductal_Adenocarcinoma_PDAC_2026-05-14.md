Subject: Daily Early-Diagnosis Brief — Pancreatic Ductal Adenocarcinoma (PDAC) — 2026-05-14

1) Snapshot (one line)
Pancreatic Ductal Adenocarcinoma (PDAC) — why early diagnosis fails in practice: The earliest physiological warning sign (new-onset diabetes) is routinely miscategorized by primary care as a common metabolic condition rather than an urgent oncological alarm.

2) Why early diagnosis fails (3–5 bullets)
*   **Biological barrier:** Deep anatomical location prevents physical detection; classic symptoms (jaundice, back pain) only manifest when the tumor physically obstructs bile ducts or invades nerves (Stage III/IV).
*   **Test limitation:** The sole FDA-approved biomarker (CA 19-9) is blind to the 5–10% of the population who are Lewis-antigen negative, and frequently spikes falsely during benign biliary inflammation.
*   **System failure:** EHRs lack automated triage to connect New-Onset Diabetes (NOD) in patients over 50 with rapid weight loss to pancreatic screening protocols.
*   **System failure:** Incidental pancreatic cysts (IPMNs) found on routine CTs for unrelated issues are frequently lost to follow-up due to fragmented care coordination between radiology and gastroenterology.

3) Detection window & gap (concise)
*   **Earliest detectable signal (research / ideal):** Exosome transcriptomic signatures or paraneoplastic metabolic shifts (e.g., new-onset diabetes) 18–36 months prior to tumor mass visualization.
*   **Typical clinical detection:** Stage IV metastasis via CT scan after the onset of jaundice or severe abdominal pain.
*   **Gap to close:** 12 to 24 months. Shifting detection from symptomatic presentation to the asymptomatic paraneoplastic/metabolic window is the difference between a 13% and a 50% 5-year survival rate.

4) What’s being used today (gold standard + emergent)
*   **Gold standard(s):** CA 19-9 blood test; Endoscopic Ultrasound (EUS) and MRCP for high-risk surveillance.
*   **Emerging research / tools:** AI EHR-mining models (e.g., MIT's PRISM); ExoVita™ Pancreas Assay (exosome-based); MIR129-2 promoter methylation (ctDNA); i-Metabolic plasma multimetabolite signatures.
*   **Main limitations:** EUS is highly invasive, expensive, requires deep sedation, and is operator-dependent. Current liquid biopsies are still too expensive for general population screening and pending broad clinical utility validation.

5) Where healthcare is failing (operational insight)
*   **Screening point that drops the ball:** Primary care and endocrinology clinics. A 55-year-old presenting with new-onset type 2 diabetes and dropping weight is prescribed Metformin, not an MRCP.
*   **Bottleneck most fixable in 90 days:** The lack of automated EHR reflex alerts for the "NOD + Age >50 + Weight Loss" triad.
*   **High-risk population missed:** Patients with incidentally discovered cysts (IPMNs) on scans done for unrelated reasons (e.g., kidney stones) who never receive their 6-month follow-up EUS due to poor care navigation.

6) 3 High-leverage solution ideas (practical, ranked)
*   **[Idea A — quick pilotable] EHR "NOD-Oncology" Reflex Protocol:** Run a 90-day pilot in a single health system. Create a strict EHR alert: Any patient >50 diagnosed with New-Onset Diabetes + a >5% BMI drop triggers an automatic navigator referral for a CA 19-9 draw and a baseline MRCP. *Metrics to collect:* Number of alerts fired, % compliant with imaging, early neoplasms found, false-positive rate.
*   **[Idea B — scalable tech / workflow change] NLP-Driven Incidentaloma Net:** Deploy an NLP algorithm over historical and incoming radiology reports to flag mentions of "incidental pancreatic cyst" or "IPMN". *Resource checklist:* NLP software (e.g., Nuance or an open-source clinical LLM), one dedicated care navigator. *Expected impact:* Close the loop on 100% of incidental findings, converting lost patients into a highly structured surveillance cohort.
*   **[Idea C — research / product] Multi-Omic NOD Triage Panel:** Highest upside startup play. Build a low-cost, reflex blood test combining CA 19-9, i-Metabolic signatures, and MIR129-2 methylation specifically for the NOD cohort. *Tests needed:* Retrospective analysis of banked blood from NOD patients who later developed PDAC. *Collaborators to approach:* The PRECEDE Consortium, PanCAN Early Detection Initiative, and OHSU.

7) First-principles signal hunt (what we should measure earlier)
*   **Hidden signal candidate:** Tumor-derived exosomes (T-Exos) and high-throughput protease activity. The tumor microenvironment secretes specific proteases and extracellular vesicles long before a solid mass forms.
*   **Minimal sampling change needed:** Standard peripheral blood draw, but processed specifically for extracellular vesicle isolation rather than standard serum/plasma separation.

8) Strategic value & next immediate actions (CEO lens)
*   **Public health impact:** Low population prevalence but massive mortality (5-year survival ~13%), projected to become the second leading cause of cancer-related death. Moving the needle here creates massive asymmetric value.
*   **Today:** Forward this brief to your CMIO or lead clinical operational officer to ask: "Do we have a centralized tracking mechanism for incidental IPMNs found on routine imaging?"
*   **7 days:** Pull a blinded, retrospective EHR report of patients >50 diagnosed with Type 2 Diabetes in the last 12 months who also had a recorded weight loss of >5%. See how many received any pancreatic imaging.
*   **30 days:** Draft a pilot specification for the NLP Radiology "Incidentaloma Net" to pitch to the hospital's innovation steering committee.

9) One-minute mental model
"PDAC hides in plain sight by disguising its earliest warning sign as routine adult-onset diabetes; the leverage point is treating new-onset diabetes in older, thinning patients as an oncology alert, not an endocrinology routine."

Attach: 
*   MIT PRISM (Predicting Risk of Incidence of Malignancy) AI model.
*   PRECEDE Consortium / PANORAMA study (The Lancet, 2026).
*   ExoVita Pancreas Assay / MIR129-2 promoter methylation.

10) Pattern Insight (Meta-Learning)
*   **What recurring diagnostic failure pattern is emerging?** The "Siloed Specialty Trap." Lethal signals present as non-lethal routine conditions (diabetes, indigestion, anemia) managed by primary care or generalists, never triggering an oncology/specialty reflex until it's too late.
*   **Is today’s disease reinforcing or breaking that pattern?** Strongly reinforcing. Endocrinology handles the diabetes; Gastroenterology handles the indigestion; Oncology is only called when the CT finally shows a mass.
*   **What generalizable opportunity is forming across diseases?** Cross-disciplinary EHR trigger systems. There is a massive startup opportunity in building "diagnostic bridges"—middleware that automatically connects a cluster of primary care symptoms to specialized screening protocols without requiring the primary care physician to play master diagnostician.