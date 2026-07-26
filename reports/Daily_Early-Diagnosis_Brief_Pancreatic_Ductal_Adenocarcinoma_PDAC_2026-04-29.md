Subject: Daily Early-Diagnosis Brief — Pancreatic Ductal Adenocarcinoma (PDAC) — 2026-04-29

1) Snapshot (one line)
Pancreatic Ductal Adenocarcinoma (PDAC) — why early diagnosis fails in practice: Deep anatomical location hides early symptoms, while healthcare systems completely miss the critical 8–36 month pre-diagnostic window signaled by new-onset diabetes and subtle CT anomalies.

2) Why early diagnosis fails (3–5 bullets)
*   **Biological barrier:** Deep retroperitoneal location means tumors grow silently; systemic metabolic changes (diabetes) occur long before localized pain or jaundice.
*   **Test limitation:** Standard CA19-9 biomarker has dismal sensitivity for Stage I disease; Endoscopic Ultrasound (EUS) is invasive, operator-dependent, and unscalable for population screening.
*   **System failure:** Vague GI complaints (indigestion, back pain) trigger generic workups that add a median of 5 months of delay.
*   **Missed imaging:** Retrospective data shows up to 8% of tumors were visible but missed by human radiologists on routine scans taken up to 18 months prior to clinical diagnosis.

3) Detection window & gap (concise)
*   **Earliest detectable signal (research / ideal):** 8 to 36 months prior to mass visualization (via metabolic shadow/New-Onset Diabetes or AI opportunistic CT screening).
*   **Typical clinical detection:** Stage III/IV (when biliary obstruction or severe pain forces acute imaging).
*   **Gap to close:** 8 to 18 months. Catching the tumor in this window shifts 5-year survival from ~3% to >50% (Stage IA).

4) What’s being used today (gold standard + emergent)
*   **Gold standard(s):** Contrast abdominal CT/MRI, followed by EUS-FNA (Endoscopic Ultrasound with Fine Needle Aspiration) for tissue confirmation.
*   **Emerging research / tools:** ClearNote *Avantect* (epigenomics/cfDNA liquid biopsy), Immunovia *PancreaSure* (serum-based biomarker signature), and *FELIX Project* AI (opportunistic pre-diagnostic screening on routine CTs).
*   **Main limitations:** Liquid biopsies require high-risk stratification (like genetic cohorts) to be cost-effective; AI tools face massive PACS integration hurdles and resistance from radiology departments.

5) Where healthcare is failing (operational insight)
*   **Screening point that drops the ball:** Primary care diagnosing New-Onset Diabetes (NOD) in patients >50 without recognizing it as a potential paraneoplastic syndrome. 
*   **Bottleneck most fixable in 90 days:** Lack of automated EMR risk stratification. The ENDPAC (Enriching New-Onset Diabetes for Pancreatic Cancer) score should be auto-calculated for every older adult with a new diabetes diagnosis.
*   **High-risk population missed:** Patients with incidental intraductal papillary mucinous neoplasms (IPMNs/cysts). Because they don't require immediate surgery under Fukuoka/AGA guidelines, patients are told to "return in a year"—with no automated tracking, attrition is massive, and cysts silently turn malignant.

6) 3 High-leverage solution ideas (practical, ranked)
*   **[Idea A — quick pilotable] EMR "NOD-to-Scan" Trigger:** Run a 90-day pilot auto-calculating the ENDPAC score for all patients >50 receiving a new diabetes diagnosis. Trigger an automated reflex protocol (EUS or Avantect test) for scores ≥3. Metrics to collect: % of eligible NOD patients screened, time-to-imaging, and false-positive burden on GI.
*   **[Idea B — scalable tech / workflow change] Incidentaloma Safety Net:** Deploy NLP software over historical radiology reports to flag "pancreatic cyst" or "IPMN." Resource checklist: NLP parser, EMR write-access, and one dedicated care navigator. Expected impact: Close the loop on 100% of incidental findings, automate EUS scheduling, and eliminate the "return in a year" patient drop-off.
*   **[Idea C — research / product] Opportunistic AI CT Screening:** Partner with the FELIX Project (Johns Hopkins) or deploy proprietary AI on historical non-contrast CTs (e.g., kidney stone workups) to flag pre-diagnostic neoplastic lesions. Highest upside, requires PACS integration and collaboration with a forward-thinking radiology chair.

7) First-principles signal hunt (what we should measure earlier)
*   **Hidden signal candidate:** Exosome-based transcriptomic shifts coupled with peripheral insulin resistance that precedes the actual tumor mass formation. 
*   **Minimal sampling change needed:** A simple serum reflex draw at the exact time of the initial HbA1c spike in older adults.

8) Strategic value & next immediate actions (CEO lens)
*   **Public health impact:** ~500,000 global cases/year with ~90% mortality; the 3rd leading cause of cancer death, soon to be 2nd. 
*   **3 immediate actions for you (today → 7 days → 30 days):**
    *   **Today:** Pull sample EMR data on patients >50 diagnosed with diabetes in your system over the last 24 months—how many had abdominal imaging within 90 days of that diagnosis?
    *   **7 days:** Map the current hospital workflow for incidental pancreatic cysts to identify the exact tracking drop-off rate between discovery and the 1-year follow-up.
    *   **30 days:** Draft a pilot protocol for an automated ENDPAC score alert in primary care clinics to catch the NOD-to-PDAC window.

9) One-minute mental model
"PDAC isn't just a localized mass; it's a systemic metabolic disruptor that signals its presence via new-onset diabetes 8–36 months before the tumor is clinically visible—leverage the metabolic shadow, not just the scan."

Attach: *ENDPAC Score validation*; *ClearNote Avantect*; *FELIX Project AI (Johns Hopkins)*; *PANORAMA Study*.

10) Pattern Insight (Meta-Learning)
*   **What recurring diagnostic failure pattern is emerging?** The "Siloed Symptom" failure. Systemic early-warning signs (like metabolic changes/diabetes) are treated by one specialty (primary care/endocrinology), while the root cause (cancer) belongs to another (oncology/GI). The data exists but never crosses specialty lines.
*   **Is today’s disease reinforcing or breaking that pattern?** Strongly reinforcing. Just as early cardiac warnings hide in GI charts (indigestion), PDAC hides in the endocrinology chart.
*   **What generalizable opportunity is forming across diseases?** Cross-specialty EMR reflex triggers. If Disease A (diabetes) in Cohort B (age >50) suddenly appears, software must automatically calculate the risk for hidden Disease C (cancer) before a standard referral is made. Diagnostic startups should focus on bridging these specialty data silos rather than just building novel assays.