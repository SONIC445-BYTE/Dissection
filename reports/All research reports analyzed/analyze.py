from pathlib import Path
from bs4 import BeautifulSoup
import re, json, html
root=Path('/home/user/repo/reports')
rows=[]
for p in sorted(root.iterdir()):
 if not p.is_file():continue
 raw=p.read_text(errors='replace')
 if p.suffix.lower()=='.html':
  s=BeautifulSoup(raw,'html.parser')
  for x in s(['script','style']): x.decompose()
  text=s.get_text('\n',strip=True)
  heads=[x.get_text(' ',strip=True) for x in s.find_all(['h1','h2','h3','h4'])]
 else:
  text=raw
  heads=[]
  for line in raw.splitlines():
   m=re.match(r'^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$',line)
   if m: heads.append(m.group(1))
   elif re.match(r'^[A-Z][A-Z0-9 /&,:—–\-()]{5,}$', line.strip()): heads.append(line.strip())
 words=re.findall(r"\b[\w'-]+\b", text)
 rows.append({'filename':p.name,'ext':p.suffix,'bytes':p.stat().st_size,'chars':len(text),'words':len(words),'heads':heads,'text':text})
Path('/home/user/extract.json').write_text(json.dumps(rows))
# human summaries headings
with open('/home/user/heads.txt','w') as f:
 for r in rows:
  f.write('\n### '+r['filename']+f" [{r['words']}w]\n")
  f.write(' | '.join(r['heads'][:30])+'\n')
