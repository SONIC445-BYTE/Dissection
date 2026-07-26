Subject: Daily Early-Diagnosis Brief — Pancreatic Ductal Adenocarcinoma (PDAC) — 2026-05-07

**1) Snapshot (one line)**
Pancreatic Ductal Adenocarcinoma (PDAC) — why early diagnosis fails in practice: Vague symptoms mimic benign GI/metabolic issues, early tumors shed minimal ctDNA, and visually occult architectural changes are routinely missed by human radiologists on standard CTs.

**2) Why early diagnosis fails (3–5 bullets)**
*   **Biological barrier:** Deep anatomical location combined with exceptionally low circulating tumor DNA (ctDNA) shedding at Stage I/II limits standard liquid biopsies.
*   **Test limitation:** The standard CA19-9 blood test suffers from high false positives (confounded by pancreatitis) and entirely misses genetic non-secretors (Lewis-negative phenotype).
*   **System failure:** EHR silos prevent the synthesis of longitudinal prodromes (e.g., new-onset diabetes + weight loss), and incidentally found pancreatic cysts suffer from severe surveillance protocol fatigue.
*   **Perceptual ceiling:** Up to 35% of missed cases on prior imaging are potentially avoidable; early architectural changes simply fall below human visual thresholds.

**3) Detection window & gap (concise)**
*   **Earliest detectable signal (research / ideal):** 475 days pre-diagnosis via AI radiomics on routine CTs; 6–12 months via LLM-EHR symptom clustering.
*   **Typical clinical detection:** Stage III/IV (unresectable), driven by late-stage jaundice, severe abdominal/back pain, or cachexia.
*   **Gap to close:** ~12–18 months. Shifting detection into this window flips the 5-year survival rate from ~13% to >44%.

**4) What’s being used today (gold standard + emergent)**
*   **Gold standard(s):** CA19-9 blood test, followed by multiphasic CT and Endoscopic Ultrasound (EUS) with fine-needle aspiration.
*   **Emerging research / tools:** 4-marker plasma panel (ANPEP + PIGR + CA19-9 + THBS2) hitting 87.5% Stage I/II sensitivity; REDMOD AI for visually occult CT detection; 5hmC epigenomics (Bluestar Genomics); Harbinger Health’s RESOLVE™ multi-cancer platform.
*   **Main limitations:** Current blood tests lack isolated Stage I sensitivity; EUS is invasive, operator-dependent, and bottlenecked by specialist capacity; standard CTs miss pre-diagnostic texture changes.

**5) Where healthcare is failing (operational insight)**
*   **Screening point that drops the ball:** Post-Imaging Pancreatic Cancer (PIPC). Roughly 7.7% of PDAC patients had a prior "clean" CT 3–18 months earlier where subtle signs, focal lesions, or incidental cysts were either misread or documented but not acted upon.
*   **Bottleneck most fixable in 90 days:** Triage of Glycaemically-defined New-Onset Diabetes (gNOD). Patients >50 with gNOD and mild weight loss are overwhelmingly managed in primary care as routine metabolic cases rather than triggered for urgent oncology/GI screening.
*   **High-risk population missed:** Sporadic cases with no traditional familial/genetic risk factors. They make up >90% of all PDAC cases but are completely excluded from current systematic surveillance guidelines.

**6) 3 High-leverage solution ideas (practical, ranked)**
*   **[Idea A — quick pilotable] — Retrospective EHR "Missed Signal" Audit:** Run a 30-day pilot on the last 100 PDAC diagnoses at a partner hospital. Apply a simple NLP script to flag preceding new-onset diabetes, back pain, or incidental cysts in the 24 months prior. *Metrics to collect:* % of cases with a documented missed trigger >6 months prior, and the average latency from first symptom to EUS referral.
*   **[Idea B — scalable tech / workflow change] — Automated Radiomic Triage Pipeline:** Deploy a background radiomics model (like Mayo Clinic's REDMOD) on *all* routine abdominal CTs for patients >60, regardless of the primary indication. *Resource checklist:* PACS integration, GPU compute, automated GI referral protocol. *Expected impact:* Catching visually occult tumors up to 475 days earlier without ordering net-new scans, doubling detection sensitivity over human reads.
*   **[Idea C — research / product] — Multi-Omic + EHR Fusion Diagnostic:** Develop an integrated product combining continuous LLM-based EHR risk scoring (flagging metabolic/GI clusters) with a reflex multi-protein blood draw (ANPEP/PIGR). *Tests needed:* Prospective validation in a general primary care cohort. *Collaborators to approach:* Harbinger Health or Bluestar Genomics to embed their assays into this EHR-triggered pathway.

**7) First-principles signal hunt (what we should measure earlier)**
*   **Hidden signal candidate:** Exosome-derived miRNA signatures or blood-based epigenomic 5-hydroxymethylcytosine (5hmC) markers, which reflect cancer-specific gene regulation and epigenetic shifts *before* overt mutational burden (ctDNA) reaches detectable thresholds.
*   **Minimal sampling change needed:** Standard peripheral blood draw, but routed for exosome isolation or epigenetic sequencing rather than standard cfDNA mutational profiling.

**8) Strategic value & next immediate actions (CEO lens)**
*   **Public health impact:** 3rd leading cause of cancer death globally. High mortality is almost entirely an artifact of late detection; the asymmetric upside of shifting diagnosis left by just one year is massive.
*   **Today:** Review the Mayo Clinic REDMOD paper to understand the specific wavelet-filtered radiomic features that beat human perception on CT scans.
*   **7 days:** Draft a workflow protocol for a primary care "gNOD (new-onset diabetes) + weight loss" reflex testing pathway to pitch to a progressive ACO.
*   **30 days:** Pitch a regional hospital system on a 90-day retrospective EHR analysis using LLM embeddings to identify their specific PIPC (Post-Imaging Pancreatic Cancer) failure rate and map the lost revenue from delayed EUS procedures.

**9) One-minute mental model**
"PDAC hides by mimicking benign aging (diabetes, back pain, cysts) and shedding too little DNA for early liquid biopsies; the leverage point is treating the EHR and routine CTs as continuous, passive surveillance sensors rather than isolated diagnostic events."
*Attach:* 
*   Krusen et al. (2026) ANPEP/PIGR 4-marker panel: [DOI: 10.1158/1078-0432.CCR-25-3297](https://doi.org/10.1158/1078-0432.CCR-25-3297)
*   Mukherjee et al. (2026) REDMOD AI on occult CT: [DOI: 10.1136/gutjnl-2025-337266](https://doi.org/10.1136/gutjnl-2025-337266)
*   Harbinger Health RESOLVE™ platform / PROCARES Trial: [NCT07046260](https://clinicaltrials.gov/study/NCT07046260)

**10) Pattern Insight (Meta-Learning)**
*   **What recurring diagnostic failure pattern is emerging?** The "Vague Symptom + Incidental Finding Dismissal" loop. Providers logically attribute non-specific symptoms to common benign causes. When incidental abnormalities (like cysts) are found, surveillance fatigue sets in, and patients fall through the cracks.
*   **Is today’s disease reinforcing or breaking that pattern?** Strongly reinforcing. PDAC is the ultimate "needle in a haystack" problem where fatal early signals are drowned out by primary care noise. 
*   **What generalizable opportunity is forming across diseases?** Opportunistic AI screening. Using routine, already-collected data (LLM embeddings on EHRs, background radiomics on standard CTs) to automatically flag high-risk patients *without* requiring the clinician to suspect the rare disease first.