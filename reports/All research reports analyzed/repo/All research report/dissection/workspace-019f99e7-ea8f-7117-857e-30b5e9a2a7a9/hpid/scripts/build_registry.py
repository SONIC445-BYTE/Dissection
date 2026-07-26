# -*- coding: utf-8 -*-
"""HPDA Phase 0/1 : build master Healthcare Platform Registry for JARVIS/Ovexis.
Sources: ABDM partner API (primary, govt), ABDM integrator API (govt ratings), curated augment set."""
import json, csv, sqlite3, re, sys, datetime, os
sys.path.insert(0, os.path.dirname(__file__))
from augment import AUGMENT

BASE = "/home/user/hpid"
TODAY = "2026-07-25"
ABDM_SRC = "https://abdm.gov.in/strapicms/api/our-partners  (ABDM official partner registry API)"

abdm  = json.load(open(f"{BASE}/sources/abdm_norm.json"))
integ = json.load(open(f"{BASE}/sources/abdm_integrators_clean.json"))

# ---- government product ratings keyed by fuzzy name/domain ----
def dom(u):
    if not u: return ""
    m = re.sub(r"^https?://(www\.)?", "", u).split("/")[0].lower()
    return m
rating_by_dom, rating_by_name = {}, {}
for i in integ:
    if i.get("rating"):
        if i.get("url"): rating_by_dom[dom(i["url"])] = float(i["rating"])
        if i.get("title"): rating_by_name[i["title"].lower().strip()] = float(i["rating"])

CAT_WEIGHT = {  # strategic weight of the category for JARVIS
 "HMIS":1.00,"EMR":0.95,"LMIS":0.80,"RIS/PACS":0.80,"Health Tech":0.55,"PHR App":0.50,
 "Insurance":0.65,"NHCX":0.70,"Government Programs":0.85,"Health Locker":0.45,
 "Connectors":0.75,"Pharmacy":0.60,"Others":0.35,"Imaging AI":0.55,
 "Teleradiology/AI":0.55,"National Infra":1.00,"Insurance Exchange":0.70,
 "Pharmacy/SCM":0.60,"Blood Bank":0.55}

def slug(n):
    s = re.sub(r"[^a-z0-9]+","-", n.lower()).strip("-")
    return re.sub(r"-(pvt|private|ltd|limited|llp|inc|technologies|technology|solutions|systems)$","",s)[:60]

def clean_company(n):
    return re.sub(r"\s+"," ", n).strip()

records = {}

# ---------- 1. ABDM-certified partners (PRIMARY GOVERNMENT SOURCE) ----------
for r in abdm:
    name = clean_company(r["name"])
    if not name: continue
    pid = "IN-" + slug(name)
    cats = r["categories"] or ["Others"]
    d = dom(r["url"])
    rating = rating_by_dom.get(d) or rating_by_name.get(name.lower())
    if pid in records:                      # merge duplicate listings
        rec = records[pid]
        rec["categories"] = sorted(set(rec["categories"]) | set(cats))
        rec["abdm_listings"] += 1
        if r["integrated"] and (not rec["abdm_integrated_date"] or r["integrated"] < rec["abdm_integrated_date"]):
            rec["abdm_integrated_date"] = r["integrated"]
        rec["security_audit_cert"] = rec["security_audit_cert"] or bool(r["wasa_pdf"])
        rec["demo_video"] = rec["demo_video"] or r["demo"]
        continue
    records[pid] = dict(
        platform_id=pid, name=name, company=name, website=r["url"],
        categories=sorted(set(cats)), sector=r["sector"] or "unknown",
        country="India", source_type="ABDM_REGISTRY", abdm_certified=True,
        abdm_id=r["abdm_id"], abdm_integrated_date=r["integrated"],
        abdm_expiry=r["expiry"], abdm_mvp_compliant=bool(r["mvp"]),
        abdm_listings=1, nhcx_type=r["nhcx"],
        cert_pdf=("https://abdm.gov.in/strapicms"+r["cert_pdf"]) if r["cert_pdf"] else None,
        security_audit_cert=bool(r["wasa_pdf"]), demo_video=r["demo"],
        govt_product_rating=rating, notes=None,
        evidence=ABDM_SRC, confidence="VERIFIED")

# ---------- 2. Curated augment (non-ABDM segments) ----------
for a in AUGMENT:
    pid = "IN-" + slug(a["name"])
    if pid in records:
        rec = records[pid]
        rec["notes"] = a["note"]; rec["evidence"] += " ; " + a["src"]
        rec["categories"] = sorted(set(rec["categories"]) | {a["category"]})
        continue
    records[pid] = dict(
        platform_id=pid, name=a["name"], company=a["company"], website=a["url"],
        categories=[a["category"]], sector=a["sector"], country=a["country"],
        source_type="CURATED", abdm_certified=False, abdm_id=None,
        abdm_integrated_date=None, abdm_expiry=None, abdm_mvp_compliant=False,
        abdm_listings=0, nhcx_type=None, cert_pdf=None,
        security_audit_cert=False, demo_video=None,
        govt_product_rating=rating_by_name.get(a["name"].lower()),
        notes=a["note"], evidence=a["src"], confidence=a["conf"])

# ---------- 3. Enrichment: known deployment scale / integration surface ----------
# footprint tiers derived from cited evidence; NATIONAL/LARGE/MID/SMB/NICHE
FOOTPRINT = {
 "IN-e-sushrut":"NATIONAL","IN-e-hospital-nextgen-e-hmis":"NATIONAL","IN-nic":"NATIONAL",
 "IN-cdac":"NATIONAL","IN-abha-abdm-core-hfr-hpr-hie-cm":"NATIONAL","IN-nhcx":"NATIONAL",
 "IN-e-aushadhi":"NATIONAL","IN-eaushadhi":"NATIONAL","IN-e-raktkosh-bbms":"NATIONAL",
 "IN-e-sushrut-clinic":"LARGE","IN-karexpert":"LARGE","IN-practo":"LARGE",
 "IN-insta-hms":"LARGE","IN-bahmni":"LARGE","IN-openmrs":"LARGE","IN-attune-his-lis":"LARGE",
 "IN-creliohealth":"LARGE","IN-eka-care":"LARGE","IN-healthplix":"LARGE","IN-mocdoc":"LARGE",
 "IN-yro-systems":"LARGE","IN-suvarna-technosoft":"LARGE","IN-plus91":"LARGE",
 "IN-medixcel-emr-his":"LARGE","IN-healthray":"MID","IN-dcm4chee":"LARGE",
 "IN-qure-ai":"MID","IN-radspa-ris-pacs":"MID","IN-napier-his":"MID","IN-softclinic-genx":"MID",
 "IN-caresoft-his":"MID","IN-halemind":"MID","IN-ezovion-hims":"MID","IN-drlogy":"MID",
 "IN-epic":"NICHE","IN-oracle-health-cerner":"NICHE","IN-meditech-expanse":"NICHE",
 "IN-intersystems-trakcare":"NICHE","IN-dedalus":"NICHE",
}
FOOT_SCORE = {"NATIONAL":10,"LARGE":8,"MID":6,"SMB":4,"NICHE":3,"UNKNOWN":3}

OPEN_API = {  # documented/known programmatic surface beyond ABDM
 "IN-bahmni":9,"IN-openmrs":9,"IN-dcm4chee":9,"IN-creliohealth":7,"IN-eka-care":7,
 "IN-epic":8,"IN-oracle-health-cerner":8,"IN-intersystems-trakcare":8,"IN-karexpert":6,
 "IN-abha-abdm-core-hfr-hpr-hie-cm":10,"IN-nhcx":9,"IN-practo":6,"IN-medixcel-emr-his":6,
 "IN-e-sushrut":4,"IN-e-hospital-nextgen-e-hmis":4,"IN-nic":4,"IN-cdac":4,
}

def score(rec):
    cw = max((CAT_WEIGHT.get(c,0.4) for c in rec["categories"]), default=0.4)
    foot = FOOTPRINT.get(rec["platform_id"],"UNKNOWN")
    fs   = FOOT_SCORE[foot]
    # market importance
    market = round(min(10, fs*cw + (1.0 if rec["abdm_certified"] else 0)), 1)
    # api quality: ABDM cert implies at least FHIR M1-M3 surface
    api = OPEN_API.get(rec["platform_id"], 5 if rec["abdm_certified"] else 2)
    fhir = 8 if rec["abdm_certified"] else OPEN_API.get(rec["platform_id"],2)
    if rec["platform_id"] in ("IN-abha-abdm-core-hfr-hpr-hie-cm","IN-nhcx"): fhir = 10
    # ui automation feasibility: cloud/web = easier
    web = 8 if (rec["sector"] in ("private","open-source") or rec["abdm_certified"]) else 6
    sec = 7 if rec["security_audit_cert"] else (5 if rec["abdm_certified"] else 4)
    integ_diff = round(max(1, 11 - (api*0.6 + fhir*0.4)),1)
    maint = round(min(10, 3 + (0.4 if rec["abdm_certified"] else 0) + (2 if foot in("NATIONAL","LARGE") else 0)),1)
    autom = round(min(10, (api*0.45 + web*0.35 + fhir*0.20)),1)
    strat = round(min(10, market*0.55 + autom*0.30 + (rec["govt_product_rating"] or 0)*0.25),1)
    prio  = round(min(10, strat*0.6 + market*0.3 + (10-integ_diff)*0.1),1)
    rec.update(deployment_footprint=foot, score_market_importance=market,
        score_api_quality=api, score_fhir_readiness=fhir, score_ui_automation=web,
        score_security=sec, score_automation_potential=autom,
        score_integration_difficulty=integ_diff, score_maintenance_burden=maint,
        score_strategic_importance=strat, recommended_priority=prio,
        last_verified=TODAY)
    return rec

recs = [score(r) for r in records.values()]
recs.sort(key=lambda r: (-r["recommended_priority"], -r["score_market_importance"], r["name"]))
for i,r in enumerate(recs,1):
    r["rank"] = i
    r["tier"] = "P0" if i<=15 else "P1" if i<=50 else "P2" if i<=150 else "P3"

os.makedirs(f"{BASE}/registry", exist_ok=True)
json.dump(recs, open(f"{BASE}/registry/platform_registry.json","w"), indent=1)

# ---- CSV ----
cols = ["rank","tier","platform_id","name","company","website","categories","sector","country",
 "deployment_footprint","source_type","abdm_certified","abdm_integrated_date","abdm_expiry",
 "abdm_listings","security_audit_cert","govt_product_rating","score_market_importance",
 "score_automation_potential","score_api_quality","score_ui_automation","score_fhir_readiness",
 "score_security","score_integration_difficulty","score_maintenance_burden",
 "score_strategic_importance","recommended_priority","confidence","last_verified","evidence","notes"]
with open(f"{BASE}/registry/platform_registry.csv","w",newline="",encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore"); w.writeheader()
    for r in recs:
        row = dict(r); row["categories"] = "|".join(r["categories"]); w.writerow(row)

# ---- YAML (no external dep) ----
def y(v, ind=0):
    p = "  "*ind
    if v is None: return "null"
    if isinstance(v,bool): return "true" if v else "false"
    if isinstance(v,(int,float)): return str(v)
    s = str(v).replace('"','\\"').replace("\n"," ")
    return '"'+s+'"'
with open(f"{BASE}/registry/platform_registry.yaml","w",encoding="utf-8") as f:
    f.write("# JARVIS/Ovexis Healthcare Platform Registry - India\n")
    f.write(f"# generated: {TODAY}  platforms: {len(recs)}\n")
    f.write("# primary source: ABDM official partner registry API (Govt of India)\nplatforms:\n")
    for r in recs:
        f.write(f"  - platform_id: {y(r['platform_id'])}\n")
        for k in cols[:-2]:
            if k=="platform_id": continue
            v = r.get(k)
            if k=="categories":
                f.write("    categories: ["+", ".join(y(c) for c in v)+"]\n")
            else: f.write(f"    {k}: {y(v)}\n")
        f.write(f"    evidence: {y(r.get('evidence'))}\n")
        f.write(f"    notes: {y(r.get('notes'))}\n")

# ---- SQLite ----
db = f"{BASE}/registry/platform_registry.sqlite"
if os.path.exists(db): os.remove(db)
con = sqlite3.connect(db); c = con.cursor()
c.executescript("""
PRAGMA journal_mode=WAL;
CREATE TABLE platform (
  platform_id TEXT PRIMARY KEY, rank INTEGER, tier TEXT, name TEXT NOT NULL, company TEXT,
  website TEXT, sector TEXT, country TEXT, deployment_footprint TEXT, source_type TEXT,
  abdm_certified INTEGER, abdm_id INTEGER, abdm_integrated_date TEXT, abdm_expiry TEXT,
  abdm_listings INTEGER, abdm_mvp_compliant INTEGER, nhcx_type TEXT, cert_pdf TEXT,
  security_audit_cert INTEGER, demo_video TEXT, govt_product_rating REAL,
  notes TEXT, evidence TEXT, confidence TEXT, last_verified TEXT);
CREATE TABLE category (platform_id TEXT, category TEXT,
  PRIMARY KEY(platform_id,category), FOREIGN KEY(platform_id) REFERENCES platform(platform_id));
CREATE TABLE score (platform_id TEXT PRIMARY KEY, market_importance REAL, automation_potential REAL,
  api_quality REAL, ui_automation REAL, fhir_readiness REAL, security REAL,
  integration_difficulty REAL, maintenance_burden REAL, strategic_importance REAL,
  recommended_priority REAL, FOREIGN KEY(platform_id) REFERENCES platform(platform_id));
-- forward-looking tables for Phase 2/3 (append-only pipeline)
CREATE TABLE dossier (platform_id TEXT PRIMARY KEY, status TEXT DEFAULT 'PENDING',
  path TEXT, completed_date TEXT, author TEXT, revision INTEGER DEFAULT 0);
CREATE TABLE automation_method (platform_id TEXT, method TEXT, feasible INTEGER,
  difficulty INTEGER, notes TEXT, PRIMARY KEY(platform_id,method));
CREATE TABLE adapter (platform_id TEXT PRIMARY KEY, priority TEXT, est_hours INTEGER,
  primary_strategy TEXT, fallback_strategy TEXT, repo_path TEXT, feature_flag TEXT);
CREATE TABLE module (platform_id TEXT, module TEXT, present INTEGER, PRIMARY KEY(platform_id,module));
CREATE TABLE source (platform_id TEXT, url TEXT, kind TEXT, retrieved TEXT);
CREATE VIEW v_priority AS
  SELECT p.rank,p.tier,p.platform_id,p.name,p.deployment_footprint,
         s.recommended_priority,s.strategic_importance,s.automation_potential,p.confidence
  FROM platform p JOIN score s USING(platform_id) ORDER BY p.rank;
""")
for r in recs:
    c.execute("""INSERT INTO platform VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
      (r["platform_id"],r["rank"],r["tier"],r["name"],r["company"],r["website"],r["sector"],
       r["country"],r["deployment_footprint"],r["source_type"],int(r["abdm_certified"]),r["abdm_id"],
       r["abdm_integrated_date"],r["abdm_expiry"],r["abdm_listings"],int(r["abdm_mvp_compliant"]),
       r["nhcx_type"],r["cert_pdf"],int(r["security_audit_cert"]),r["demo_video"],
       r["govt_product_rating"],r["notes"],r["evidence"],r["confidence"],r["last_verified"]))
    for cat in r["categories"]:
        c.execute("INSERT OR IGNORE INTO category VALUES (?,?)",(r["platform_id"],cat))
    c.execute("INSERT INTO score VALUES (?,?,?,?,?,?,?,?,?,?,?)",
      (r["platform_id"],r["score_market_importance"],r["score_automation_potential"],
       r["score_api_quality"],r["score_ui_automation"],r["score_fhir_readiness"],r["score_security"],
       r["score_integration_difficulty"],r["score_maintenance_burden"],
       r["score_strategic_importance"],r["recommended_priority"]))
    c.execute("INSERT INTO dossier(platform_id,status) VALUES (?,'PENDING')",(r["platform_id"],))
con.commit()
print("platforms:",len(recs))
print("sqlite rows:",c.execute("SELECT COUNT(*) FROM platform").fetchone()[0])
con.close()

print("\n=== TOP 25 (Phase 1 prioritisation) ===")
for r in recs[:25]:
    print(f"{r['rank']:>3} {r['tier']} {r['recommended_priority']:>4}  {r['name'][:44]:<44} {'/'.join(r['categories'])[:26]:<26} {r['deployment_footprint']:<9} {r['confidence']}")
