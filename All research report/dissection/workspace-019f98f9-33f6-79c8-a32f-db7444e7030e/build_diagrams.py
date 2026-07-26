#!/usr/bin/env python3
"""Generate clean SVG diagrams for the Practo dossier (guaranteed preview)."""
import html

NAVY="#1F3864"; BLUE="#2E5C9E"; LBLUE="#D9E1F2"; GREEN="#C6EFCE"; YEL="#FFEB9C"
RED="#FFC7CE"; GREY="#808080"; LGREY="#F2F2F2"; WHITE="#FFFFFF"; DKG="#404040"
FONTSIZE=12

def esc(s): return html.escape(str(s))

def svg_doc(title, w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" font-family="Helvetica, Arial, sans-serif">\n'
            f'<rect x="0" y="0" width="{w}" height="{h}" fill="{WHITE}"/>\n'
            f'<text x="20" y="28" font-size="16" font-weight="bold" fill="{NAVY}">{esc(title)}</text>\n'
            f'<line x1="20" y1="36" x2="{w-20}" y2="36" stroke="{NAVY}" stroke-width="1.5"/>\n'
            + body + '</svg>')

def node(x,y,w,h,label,fill=LBLUE,textcolor=DKG,fs=FONTSIZE):
    # wrap label into up to 3 lines
    words=str(label).split()
    lines=[]; cur=""
    for word in words:
        if len(cur)+len(word)+1<=int(w/6.5):
            cur=(cur+" "+word).strip()
        else:
            lines.append(cur); cur=word
    if cur: lines.append(cur)
    lines=lines[:4]
    txt=""
    lh=fs+3
    starty=y+h/2-(len(lines)-1)*lh/2
    for i,ln in enumerate(lines):
        txt+=f'<text x="{x+w/2}" y="{starty+i*lh}" font-size="{fs}" text-anchor="middle" fill="{textcolor}">{esc(ln)}</text>\n'
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" ry="8" fill="{fill}" stroke="{NAVY}" stroke-width="1.2"/>\n'+txt)

def arrow(x1,y1,x2,y2,label="",color=GREY):
    # draw line with arrowhead
    ax2=x2; ay2=y2
    # shorten to box edge
    import math
    dx=x2-x1; dy=y2-y1; d=math.hypot(dx,dy) or 1
    ux,uy=dx/d,dy/d
    sx=x1+ux*6; sy=y1+uy*6; ex=x2-ux*8; ey=y2-uy*8
    arr=(f'<line x1="{sx:.0f}" y1="{sy:.0f}" x2="{ex:.0f}" y2="{ey:.0f}" stroke="{color}" stroke-width="1.6"/>\n'
         f'<polygon points="{ex:.0f},{ey:.0f} {ex-10*ux-4*uy:.0f},{ey-10*uy+4*ux:.0f} {ex-10*ux+4*uy:.0f},{ey-10*uy-4*ux:.0f}" fill="{color}"/>\n')
    if label:
        mx=(sx+ex)/2; my=(sy+ey)/2
        arr+=f'<rect x="{mx-26}" y="{my-9}" width="52" height="16" rx="3" fill="{WHITE}" stroke="{color}" stroke-width="0.8"/>\n'
        arr+=f'<text x="{mx}" y="{my+3}" font-size="10" text-anchor="middle" fill="{DKG}">{esc(label)}</text>\n'
    return arr

def build(title, nodes, edges, w=1100, h=720):
    body=""
    # edges first (under nodes)
    for e in edges:
        n1=nodes[e[0]]; n2=nodes[e[1]]
        x1=n1[0]+n1[2]/2; y1=n1[1]+n1[3]/2
        x2=n2[0]+n2[2]/2; y2=n2[1]+n2[3]/2
        lbl=e[2] if len(e)>2 else ""
        col=e[3] if len(e)>3 else GREY
        body+=arrow(x1,y1,x2,y2,lbl,col)
    for k,n in nodes.items():
        fill=BLUE if len(n)<5 else n[4]
        body+=node(n[0],n[1],n[2],n[3],n[4] if len(n)>4 else "", fill=fill)
    return svg_doc(title,w,h,body)

# ---------- 1. Product Architecture ----------
prod_nodes={
 "U":(20,60,200,50,"Users: Patients/Doctors/Hospitals/Payors",LBLUE),
 "W":(300,60,220,50,"Web + Mobile App",LBLUE),
 "GW":(580,60,200,50,"API Gateway / Services",LBLUE),
 "DIS":(300,160,150,50,"Discovery + Booking",GREEN),
 "CON":(470,160,150,50,"Teleconsult + Rx",GREEN),
 "COM":(640,160,150,50,"Commerce: Meds/Labs/Surg",GREEN),
 "SAS":(810,160,150,50,"Enterprise: Ray/Insta",GREEN),
 "AI":(580,260,200,60,"AI Brain: Clinical+Consult+Care",YEL),
 "HL7":(810,260,150,50,"HL7 / API Integration",LBLUE),
 "DATA":(300,300,200,50,"40M structured data points",YEL),
 "MKT":(300,400,220,50,"Marketplace Liquidity",LBLUE),
}
prod_edges=[("U","W","",GREY),("W","GW","",GREY),("GW","DIS"),("GW","CON"),("GW","COM"),("GW","SAS"),
 ("GW","AI"),("SAS","HL7"),("AI","DATA","",GREY),("DIS","MKT"),("CON","MKT"),("COM","MKT"),("SAS","MKT")]
svg1=build("Practo — Product Architecture",prod_nodes,prod_edges)

# ---------- 2. AI Architecture ----------
ai_nodes={
 "IN":(20,60,200,50,"Ingest: Records/Labs/Wearables/Consults",LBLUE),
 "NORM":(300,60,220,60,"Normalisation + Vector Store (FHIR-style)",LBLUE),
 "CI":(600,60,200,60,"Clinical Intelligence (layer 1)",YEL),
 "COI":(600,170,200,60,"Consultation Intelligence (layer 2)",YEL),
 "CC":(600,280,200,60,"Care Companion (layer 3)",YEL),
 "EVAL":(330,280,220,60,"Evaluation / Guardrails / HITL ?",RED),
 "U":(870,170,200,60,"Patient + Doctor",GREEN),
}
ai_edges=[("IN","NORM"),("NORM","CI"),("CI","COI"),("COI","CC"),("CI","EVAL"),("COI","U"),("CC","U"),("EVAL","U","",GREY)]
svg2=build("Practo — AI Architecture (stated + inferred)",ai_nodes,ai_edges,w=1100,h=420)

# ---------- 3. Healthcare Data Flow ----------
df_nodes={
 "PAT":(20,60,170,50,"Patient",GREEN),
 "BOOK":(250,60,170,50,"Booking / Consult",LBLUE),
 "DOC":(20,160,170,50,"Doctor / Clinic",LBLUE),
 "EMR":(250,160,170,50,"Ray / Insta EMR",LBLUE),
 "HL7":(480,160,170,50,"HL7 / API",LBLUE),
 "LAB":(480,60,170,50,"Labs / Imaging",LBLUE),
 "REC":(710,160,180,50,"Provider-scoped Records",LBLUE),
 "AI":(710,260,180,50,"AI Insights",YEL),
 "REC2":(710,360,180,50,"Recommendations",YEL),
 "FUL":(480,360,170,50,"Meds/Labs/Surgery",GREEN),
 "LON":(250,360,170,60,"Longitudinal PHR = OVEXIS GAP",RED),
}
df_edges=[("PAT","BOOK"),("DOC","EMR"),("EMR","HL7"),("LAB","HL7"),("BOOK","REC"),("HL7","REC"),
 ("REC","AI"),("AI","REC2"),("REC2","FUL"),("FUL","PAT"),
 ("REC","LON","GAP",RED),("LON","PAT","",GREY)]
svg3=build("Practo — Healthcare Data Flow (gap highlighted)",df_nodes,df_edges,w=920,h=460)

# ---------- 4. User Journey ----------
uj_nodes={
 "A":(20,60,180,45,"Anonymous Visitor",LBLUE),
 "M":(20,120,180,45,"Marketing (SEO/App)",LBLUE),
 "S":(20,180,180,45,"Signup (OTP)",LBLUE),
 "V":(20,240,180,45,"Verification",LBLUE),
 "C":(20,300,180,45,"Consent",LBLUE),
 "P":(20,360,180,45,"Permissions",LBLUE),
 "DI":(20,420,180,45,"Data Import (history)",LBLUE),
 "AI":(280,420,180,45,"AI (triage)",YEL),
 "R":(280,360,180,45,"Recommendations",YEL),
 "B":(280,300,180,45,"Booking / Payment",GREEN),
 "CO":(280,240,180,45,"Consultation",GREEN),
 "PR":(280,180,180,45,"Prescription + Records",GREEN),
 "F":(280,120,180,45,"Fulfilment (meds/labs)",GREEN),
 "RE":(540,420,180,45,"Retention (reminders)",LBLUE),
 "SU":(540,360,180,45,"Subscription (Plus)",LBLUE),
 "SP":(540,300,180,45,"Support",LBLUE),
 "RN":(540,240,180,45,"Renewal",LBLUE),
 "RF":(540,180,180,45,"Referral (weak)",RED),
}
uj_edges=[("A","M"),("M","S"),("S","V"),("V","C"),("C","P"),("P","DI"),("DI","AI"),("AI","R"),("R","B"),
 ("B","CO"),("CO","PR"),("PR","F"),("F","RE"),("RE","SU"),("SU","SP"),("SP","RN"),("RN","RF"),("RF","RE","",GREY),("DI","RE","",GREY)]
svg4=build("Practo — Complete User Journey (Patient)",uj_nodes,uj_edges,w=760,h=500)

# ---------- 5. Feature Dependency Graph ----------
fd_nodes={
 "C":(40,60,180,50,"Consent & Identity",LBLUE),
 "I":(40,150,180,50,"Patient/Doctor Identity (OTP+2FA)",LBLUE),
 "D":(40,240,180,50,"Data Collection",LBLUE),
 "N":(320,240,180,50,"Normalisation (HL7/EMR)",LBLUE),
 "A":(320,330,180,50,"AI Layer",YEL),
 "RE":(600,330,180,50,"Reports (PROMs)",YEL),
 "IN":(600,420,180,50,"Insights",YEL),
 "DOC":(600,510,180,50,"Doctor (Ray/Pro/Insta)",GREEN),
 "PAT":(320,510,180,50,"Patient (App/Web)",GREEN),
 "MKT":(320,600,180,50,"Marketplace Liquidity",LBLUE),
 "RET":(80,600,180,50,"Retention",LBLUE),
 "CC":(600,240,180,50,"Care Companion",YEL),
}
fd_edges=[("C","I"),("I","D"),("D","N"),("N","A"),("A","RE"),("RE","IN"),("IN","DOC"),("IN","PAT"),
 ("DOC","MKT"),("PAT","MKT"),("MKT","RET"),("RET","D","",GREY),("A","CC"),("CC","PAT"),("N","IN","",GREY)]
svg5=build("Practo — Feature Dependency Graph",fd_nodes,fd_edges,w=820,h=680)

# ---------- 6. Business Model Canvas (grid) ----------
def bmc_box(x,y,w,h,title,items,fill=LGREY):
    body=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{NAVY}" stroke-width="1"/>\n'
    body+=f'<text x="{x+8}" y="{y+18}" font-size="12" font-weight="bold" fill="{NAVY}">{esc(title)}</text>\n'
    yy=y+34
    for it in items:
        body+=f'<text x="{x+8}" y="{yy}" font-size="10.5" fill="{DKG}">• {esc(it)}</text>\n'
        yy+=15
    return body
w=1120;h=560
bmc=(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="Helvetica,Arial,sans-serif">\n'
     f'<rect width="{w}" height="{h}" fill="{WHITE}"/>\n'
     f'<text x="20" y="26" font-size="16" font-weight="bold" fill="{NAVY}">Practo — Business Model Canvas</text>\n')
bmc+=bmc_box(20,40,180,90,"Key Partners",["Doctors/Clinics/Hospitals","Insurers (Tata AIA)","Pharmacies / Labs","Acquired talent (Genii)"],LBLUE)
bmc+=bmc_box(20,140,180,120,"Key Activities",["Marketplace ops","SaaS Ray/Insta","Teleconsult + AI","Care navigation"],LBLUE)
bmc+=bmc_box(20,270,180,90,"Key Resources",["700k doctors","2,400 cities","40M data points","Brand + ISO27001"],LBLUE)
bmc+=bmc_box(20,370,180,90,"Value Prop",["Verified discovery","Booking + teleconsult","Records + AI nav","Outcomes (PROMs)"],YEL)
bmc+=bmc_box(20,470,180,70,"Customer Rel.",["Self-serve app","Field sales B2B"],LBLUE)
bmc+=bmc_box(210,40,180,90,"Cost Structure",["Eng / Sales","Support / Cloud","Compliance / Security","Acquisition (M&A)"],RED)
bmc+=bmc_box(210,140,180,530,"Channels",["App Store / Web","SEO / Health content","SMS app-link","Practo Reach (B2B)"],LBLUE)
bmc+=bmc_box(400,40,320,240,"Revenue Streams",["SaaS Ray (1.5-5k/mo)","Insta HMS ($25-40/u/mo)","Consult (per-visit)","Plus/Prime subscription","Practo Reach (sponsored)","Meds/Labs/Surgery GMV","Insurer/corporate tie-ups"],GREEN)
bmc+=bmc_box(400,290,320,140,"Customer Segments",["Patients (B2C India+UAE+US)","Doctors / Clinics","Hospitals","Insurers / Corporates"],LBLUE)
bmc+=bmc_box(730,40,370,520,"Key Differentiators / Moat",["Marketplace liquidity (Strong)","Enterprise SaaS lock-in (Strong)","Brand + 16M downloads (Strong)","Agentic AI narrative (Medium)","Regulatory posture (Medium)","Switching costs B2B (Med-Strong)","GAP: no patient-owned record","GAP: no open API","GAP: navigation-not-diagnosis AI","GAP: thin take-rate ~6-7%"],YEL)
bmc+='</svg>'
svg6=bmc

# ---------- 7. SWOT ----------
def quad(x,y,w,h,title,items,fill):
    body=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{NAVY}" stroke-width="1.2"/>\n'
    body+=f'<text x="{x+10}" y="{y+22}" font-size="14" font-weight="bold" fill="{NAVY}">{esc(title)}</text>\n'
    yy=y+42
    for it in items:
        body+=f'<text x="{x+10}" y="{yy}" font-size="11" fill="{DKG}">• {esc(it)}</text>\n'; yy+=18
    return body
w=1100;h=560
sw=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="Helvetica,Arial,sans-serif"><rect width="{w}" height="{h}" fill="{WHITE}"/>\n'
sw+=f'<text x="20" y="26" font-size="16" font-weight="bold" fill="{NAVY}">Practo — SWOT</text>\n'
sw+=quad(20,40,520,240,"Strengths",["Marketplace liquidity (India) 🟢","Brand + 16M downloads 🟢","Enterprise SaaS Ray/Insta 🟢","Profitability discipline FY25 🟢","AI narrative + 20k AI/day 🟢","Strong board / governance 🟢"],GREEN)
sw+=quad(560,40,520,240,"Weaknesses",["Thin take-rate (~6-7%) 🟡","'Scam'/pricing trust erosion 🟢","No patient-owned record 🟡","Tech debt from 5 acquisitions 🟡","No open API / dev moat 🟢","Navigation-not-diagnosis AI 🟡"],RED)
sw+=quad(20,300,520,240,"Opportunities",["US/UAE GMV arbitrage 🟡","Payor integration 🟡","Agentic AI moat 🟡","IPO uplift 🟡","Diaspora internationalization 🟢","PROMs credibility 🟢"],YEL)
sw+=quad(560,300,520,240,"Threats",["Apollo/1mg/MediBuddy rivalry 🟢","Longitudinal/AI entrants 🟡","OS health graphs (Apple/Google) 🟡","DPDP/HIPAA exposure 🟡","Clinical-harm incidents 🟢","Platform disintermediation 🟡"],LBLUE)
sw+='</svg>'
svg7=sw

# ---------- 8. Porter's Five Forces ----------
pf=f'<svg xmlns="http://www.w3.org/2000/svg" width="900" height="620" viewBox="0 0 900 620" font-family="Helvetica,Arial,sans-serif"><rect width="900" height="620" fill="{WHITE}"/><text x="20" y="26" font-size="16" font-weight="bold" fill="{NAVY}">Practo — Porter\'s Five Forces</text>\n'
pf+=node(330,250,240,60,"Rivalry: HIGH",RED)
pf+=node(330,60,240,55,"New Entrants: MEDIUM",YEL)
pf+=node(330,440,240,55,"Substitutes: HIGH",RED)
pf+=node(40,250,240,60,"Supplier Power (doctors): MED",YEL)
pf+=node(620,250,240,60,"Buyer Power (patients/payors): MED",YEL)
# center link lines
pf+='<line x1="450" y1="115" x2="450" y2="250" stroke="#888" stroke-width="1.4"/>'
pf+='<line x1="450" y1="310" x2="450" y2="440" stroke="#888" stroke-width="1.4"/>'
pf+='<line x1="280" y1="280" x2="330" y2="280" stroke="#888" stroke-width="1.4"/>'
pf+='<line x1="570" y1="280" x2="620" y2="280" stroke="#888" stroke-width="1.4"/>'
pf+=f'<text x="450" y="600" font-size="11" text-anchor="middle" fill="{DKG}">Apollo 24/7, Tata 1mg, MediBuddy, PharmEasy (rivalry) • OS health graphs + insurer apps (substitutes) • Ovexis-type longitudinal entrants (new entrants)</text>\n'
pf+='</svg>'
svg8=pf

# ---- write all ----
files={"product_architecture.svg":svg1,"ai_architecture.svg":svg2,"healthcare_data_flow.svg":svg3,
       "user_journey.svg":svg4,"feature_dependency.svg":svg5,"business_model_canvas.svg":svg6,
       "swot.svg":svg7,"porters_five_forces.svg":svg8}
for fn,content in files.items():
    with open("/home/user/"+fn,"w") as f: f.write(content)
    print("WROTE",fn, len(content),"bytes")
