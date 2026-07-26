#!/usr/bin/env python3
"""HPID refresh — re-pull the ABDM registry and reconcile.
Idempotent. Run weekly:  python3 refresh.py
Closes the loop that makes HPID a living asset rather than a snapshot."""
import json,csv,urllib.request,urllib.parse,sqlite3,os,datetime
BASE=os.path.dirname(os.path.abspath(__file__))
API="https://abdm.gov.in/strapicms/api/our-partners"
def fetch(page):
    q=urllib.parse.urlencode({'locale':'en','populate':'*','pagination[pageSize]':100,'pagination[page]':page})
    with urllib.request.urlopen(f"{API}?{q}",timeout=60) as r: return json.load(r)
def main():
    all_recs=[];page=1
    while True:
        d=fetch(page); all_recs+=d['data']
        m=d['meta']['pagination']
        if page>=m['pageCount']: break
        page+=1
    ts=datetime.date.today().isoformat()
    out=f"{BASE}/sources/abdm_{ts}.json"; os.makedirs(f"{BASE}/sources",exist_ok=True)
    json.dump(all_recs,open(out,'w'),indent=1)
    prev=sorted(f for f in os.listdir(f"{BASE}/sources") if f.startswith('abdm_'))
    print(f"fetched {len(all_recs)} partners -> {out}")
    if len(prev)>1:
        old=json.load(open(f"{BASE}/sources/{prev[-2]}"))
        on={x['attributes'].get('website') for x in old}
        nn={x['attributes'].get('website') for x in all_recs}
        print(f"  NEW: {len(nn-on)}   REMOVED: {len(on-nn)}")
        for w in list(nn-on)[:10]: print("   +",w)
    return all_recs
if __name__=="__main__": main()
