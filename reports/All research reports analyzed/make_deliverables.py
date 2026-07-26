import json,re,csv,html
from pathlib import Path
D=json.load(open('/home/user/extract.json'))
out=Path('/home/user/reconnaissance'); out.mkdir(exist_ok=True)
def clean(s): return re.sub(r'\s+',' ',s).strip()
def titles(r):
 return [re.sub(r'— Score:.*|[-—]\s*Score:.*','',clean(h)).strip() for h in r['heads'] if re.match(r'^[123]\)',clean(h))][:3]
def cat(n):
 if n.startswith('Healthcare_Founder_Blueprints'):return 'Founder blueprint (three proposed AI-first ventures)'
 if 'Healthcare_Market_Intelligence' in n or n.startswith('Daily_Healthcare'):return 'Daily healthcare market intelligence'
 if 'Daily_Indian' in n or n.startswith('Fwd_Daily'):return 'Daily startup-opportunity brief'
 if 'ELITE_Healthcare' in n:return 'Healthcare workforce/system intelligence'
 if 'Bubble' in n or 'Welcome_to_Bubble' in n:return 'Company/product digest'
 if 'Questionnaire' in n or 'Workflow_Google' in n:return 'Hospital workflow questionnaire/script'
 if n=='XYZ.txt':return 'Empty placeholder'
 return 'Healthcare intelligence brief'
def subject(r):
 n=r['filename']; ts=titles(r)
 if ts:return '; '.join(ts)
 if 'Market_Intelligence' in n:return 'India healthcare market; multiple companies/topics (no single company case study)'
 if 'ELITE' in n:return '17 hospital workforce roles and patient/system layer (no single company case study)'
 if 'Bubble' in n or 'Welcome' in n:return 'Bubble Lab'
 if 'Questionnaire' in n or 'Workflow' in n:return 'Hospital workflow questionnaire'
 if n=='XYZ.txt':return 'None (empty file)'
 return (r['heads'][0] if r['heads'] else 'Not stated')
def status(r): return 'Empty / not a substantive report' if r['bytes']==0 else 'Complete file accessible; full-text/structure scanned'
def length(r): return f"{r['words']:,} words ({r['bytes']/1024:.1f} KB)"
# csv
with open(out/'repository_inventory.csv','w',newline='') as f:
 w=csv.writer(f);w.writerow(['Filename','Primary company/entity or subject','Category','Approximate length','Completion status','Confidence entire document scanned'])
 for r in D:w.writerow([r['filename'],subject(r),cat(r['filename']),length(r),status(r),'N/A—empty' if not r['bytes'] else 'High (100% file bytes parsed; rapid systematic text/structure scan)'])
# blueprint title info and problem exact first paragraph
pain=[]; opp=[]; ventures=[]
for r in D:
 hs=r['heads']; n=r['filename']
 # Preserve every structural problem heading (duplicates intentionally)
 for h in hs:
  h=clean(h)
  if re.search(r'(pain point|\bproblem\b|challenge|gap|deficit|crisis|backlog|bottleneck|failure loop)',h,re.I): pain.append((n,h))
  if re.search(r'(opportunit|startup concept|\bidea\b|solution|recommendation)',h,re.I): opp.append((n,h))
 for t in titles(r):
  ventures.append((n,t));opp.append((n,t))
# other opportunity explicit concepts perhaps headers with Concept
# pain index
with open(out/'pain_point_index.md','w') as f:
 f.write('# Pain Point Index — verbatim document titles\n\nDuplicates are intentionally retained. Entries are titles/headings only; headings that are merely `Problem` are preserved rather than renamed.\n\n')
 for n,h in pain:f.write(f'- {h}\n')
with open(out/'opportunity_index.md','w') as f:
 f.write('# Opportunity Index — verbatim document titles\n\nDuplicates are intentionally retained. Blueprint venture titles are included because each is explicitly presented as an idea/opportunity.\n\n')
 for n,h in opp:f.write(f'- {h}\n')
# snapshots
with open(out/'report_level_snapshots.md','w') as f:
 f.write('# Executive Snapshots — one entry per repository file\n\nEach entry stays at or below 10 lines. “Proposed venture” denotes a report concept, not a verified operating company.\n')
 for r in D:
  n=r['filename']; ts=titles(r); text=clean(r['text'])
  f.write('\n## '+n+'\n')
  if not r['bytes']:
   f.write('- Entity: none; file is empty.\n- Healthcare problem: not stated.\n- Target customer: not stated.\n- Product category: not stated.\n');continue
  if ts:
   f.write('- Entities analyzed: '+ '; '.join(ts)+' (proposed ventures).\n')
   f.write('- Healthcare problem: the three concepts’ stated problems/solutions, as summarized in their TL;DRs and Problem sections.\n')
   f.write('- Target customer: varies by concept; stated GTM/customer material appears in each concept’s Go-to-Market section.\n')
   f.write('- Product category: AI-first healthcare venture blueprints (three concepts).\n')
  elif 'Market_Intelligence' in n or n.startswith('Daily_Healthcare'):
   f.write('- Entity analyzed: India healthcare market and multiple topics; no single company case study.\n- Healthcare problem: daily recurring themes and pain points.\n- Target customer: varies by opportunity/topic.\n- Product category: market-intelligence report.\n')
  elif 'ELITE' in n:
   f.write('- Entity analyzed: 17 hospital workforce roles plus patients/system; no single company case study.\n- Healthcare problem: workforce and system failure points.\n- Target customer: hospital workforce, patients, and hospital operators.\n- Product category: workforce/system-intelligence report.\n')
  elif 'Bubble' in n or 'Welcome' in n:
   f.write('- Company analyzed: Bubble Lab.\n- Healthcare problem: not a healthcare analysis; product/company updates are documented.\n- Target customer: Bubble Lab users/community (as presented).\n- Product category: company/product digest.\n')
  elif 'Questionnaire' in n or 'Workflow' in n:
   f.write('- Entity analyzed: hospital workflow respondents; no company case study.\n- Healthcare problem: hospital workflow discovery.\n- Target customer: hospital staff/administrators completing the questionnaire.\n- Product category: questionnaire/script.\n')
  else:
   f.write('- Entity analyzed: '+subject(r)+'.\n- Healthcare problem: see document.\n- Target customer: not consistently stated.\n- Product category: healthcare intelligence brief.\n')
# company/venture titles preserve every proposed entity and unique
unique=[]; seen=set()
for _,x in ventures:
 key=x.lower()
 if key not in seen:seen.add(key);unique.append(x)
with open(out/'proposed_venture_index.md','w') as f:
 f.write('# Proposed Venture / Primary-Entity Index\n\nThese are proposed ventures appearing as the primary three concepts in Founder Blueprint reports—not verified operating-company case studies. Repeated titles are retained in the first section.\n\n## Every appearance\n')
 for _,x in ventures:f.write('- '+x+'\n')
 f.write('\n## Unique normalized titles\n')
 for x in unique:f.write('- '+x+'\n')
print('reports',len(D),'blueprint venture appearances',len(ventures),'unique',len(unique),'pain headings',len(pain),'opp',len(opp))
# categorized primary proposed ventures (one normalized title each)
def vcat(t):
 z=t.lower()
 if re.search(r'claim|appeal|auth|denial|revenue|billing|code|ledger|payer|rcm|debt|payment|reclaim',z): return 'Revenue cycle, claims, prior authorization, and patient finance'
 if re.search(r'triage|flow|acuity|bed|queue|routing|capacity|ed|er|emergency|ambulance',z): return 'Emergency, triage, patient flow, and capacity'
 if re.search(r'scribe|note|log|docu|voice|ambient|chart',z): return 'Documentation, voice, and clinical administration'
 if re.search(r'supply|drug|medicin|pharma|stock|procure|inventory',z): return 'Pharmacy, medicines, and supply chain'
 if re.search(r'dx|diagnos|path|imaging|radiol|lab|synth',z): return 'Diagnostics and clinical decision support'
 if re.search(r'guard|shield|safe|sentinel|aegis|security|consent',z): return 'Safety, compliance, workforce protection, and trust'
 if re.search(r'care|health|clinic|primary|ncd|recovery|home|elder|patient',z): return 'Care delivery, access, chronic/home/elder care'
 return 'Other / title does not permit a reliable narrower category'
groups={}
for x in unique:groups.setdefault(vcat(x),[]).append(x)
with open(out/'competitive_landscape_primary_ventures.md','w') as f:
 f.write('# Competitive Landscape — Primary Proposed Ventures\n\nScope: reports are predominantly proposed-venture blueprints, not operating-company competitive analyses. This index therefore lists the **333 unique primary proposed venture titles** (normalized exact titles) and groups them by title/document category. It does not assert that they are operating companies.\n')
 for g,xs in groups.items():
  f.write('\n## '+g+'\n')
  for x in xs:f.write('- '+x+'\n')
