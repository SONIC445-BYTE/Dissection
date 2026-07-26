import json,re,csv
D=json.load(open('/home/user/extract.json'))
clusters={
'Claims denial, rejection & appeal backlog':r'claim.{0,25}(deni|reject)|denial|appeal|remittance|eob',
'Prior authorisation friction':r'prior.?auth|pre.?auth|authorization',
'Billing opacity, overcharging & medical debt':r'medical debt|opaque bill|bill audit|overcharg|out.of.pocket|price transparency|itemized bill',
'Coding/charge-capture & documentation defects':r'medical cod|icd|cpt|charge capture|upcod|coding error',
'Cash-flow delay & revenue leakage':r'cash.?flow|revenue leak|revenue cycle|write.down|reimbursement delay',
'Workforce shortage, retention & brain drain':r'understaff|staff shortage|brain drain|migration|retention|workforce shortage',
'Clinician burnout, mental health & administrative burden':r'burnout|administrative burden|mental health|suicide|logbook',
'Workplace violence & staff security':r'workplace violence|mob attack|assault.*doctor|violence against|hospital security',
'Patient wait, queues & access delays':r'wait time|waiting time|long queue|queue|waitlist',
'ED triage, crowding & routing':r'\btriage\b|emergency department|\bed\b|\ber\b|crowding|diversion',
'Bed, ICU & capacity management':r'bed allocation|bed management|icu bed|capacity optim|load balanc',
'Documentation, notes & medical-records burden':r'clinical documentation|medical record|clinical note|ambient scrib|voice.to.log|record retrieval',
'Diagnostic delay/error & clinical decision support':r'diagnostic error|missed diagnos|diagnostic delay|clinical decision|diagnostic discovery',
'Lab/pathology quality & workflow':r'lab technician|patholog|\blims\b|laboratory',
'Radiology/imaging workflow':r'radiolog|\bpacs\b|imaging',
'Medication safety, pharmacy & access':r'medication error|pharmacy|prescription safety|medicin',
'Medicine/consumable stock-out & procurement':r'stock.?out|procurement|inventory|consumable|supply chain',
'Equipment maintenance & biomedical readiness':r'equipment maintenance|biomedical|preventive maintenance|equipment failure|ventilator',
'Ambulance/transport & emergency readiness':r'ambulance|oxygen cylinder|golden hour|transport',
'Referral, transfer & care navigation':r'\breferral\b|interfacility|public.to.private|care navigation|second opinion',
'Discharge, post-discharge & home-care gap':r'post.discharge|discharge planning|home.?care|hospital.at.home|readmission',
'Chronic care, population health & follow-up':r'chronic care|\bncd\b|population health|care plan|follow.up',
'Surgical consent, audit trail & clinical governance':r'surgical consent|consent form|surgical audit|operating surgeon|audit trail',
'Patient trust, communication & grievances':r'trust deficit|patient communication|grievance|complaint|credibility crisis',
'Credentialing, scope-of-practice & quackery':r'quack|credential|unqualified|scope.of.practice|bogus',
'Hygiene, infection control & housekeeping':r'hygiene|infection control|housekeeping|sanitation',
'HIS/EHR fragmentation & interoperability':r'\bhis\b|\behr\b|\bemr\b|interoperab|\bfhir\b|\bhl7\b|fragmented.*system',
'Unstructured documents/OCR & data quality':r'\bocr\b|unstructured|pdf bill|scanned|data quality|incomplete documentation',
'Privacy, consent, data localisation & security':r'privacy|\bphi\b|data local|\bpdpl\b|consent workflow|cybersecurity',
'AI reliability, validation & governance':r'hallucination|clinical validation|ai.*accuracy|model.*bias|human.in.the.loop|\bsamd\b',
'Rural/primary-care access & offline delivery':r'\bphc\b|rural|offline.first|tier.?.?[23]|global south',
'Government scheme/admin friction':r'ayushman|government scheme|empanelment|nphies|government.*claim',
'Salary, payroll & workforce exploitation':r'delayed wage|unpaid salar|salary stagnation|low wage|pay disparity',
'Scheduling, handover & task coordination':r'schedul|handover|shift allocation|task allocation',
'Security/crowd control incident response':r'cctv|crowd control|quick response|panic.to.police|spatial control',
'Reputation/medico-legal defence':r'medico.legal|legal defence|defamation|reputation|litigation',
'Public health surveillance & reporting':r'surveillance|public health|reporting requirement|disease report',
'Medical education/training workflow':r'medical education|medical college|resident training|\bintern\b|\btrainee\b',
}
rows=[]
for name,pat in clusters.items():
 per=[r for r in D if re.search(pat,r['text'],re.I)]
 fam={}
 for r in per:
  n=r['filename'];k='Blueprint' if n.startswith('Healthcare_Founder') else 'Market intelligence' if 'Market_Intelligence' in n or n.startswith('Daily_Healthcare') else 'ELITE/workforce' if 'ELITE' in n else 'Other'
  fam[k]=fam.get(k,0)+1
 rows.append([name,len(per),'; '.join(f'{a}: {b}' for a,b in fam.items())])
with open('/home/user/reconnaissance/problem_frequency.csv','w') as f:
 w=csv.writer(f);w.writerow(['Normalized problem','Documents mentioning (keyword-based)','Family distribution']);w.writerows(rows)
for x in sorted(rows,key=lambda x:-x[1]):print(x)
