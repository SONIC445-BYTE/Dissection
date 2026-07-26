from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT=Path('diagrams'); OUT.mkdir(exist_ok=True)
W,H=1800,1050
NAVY='#153B5B'; BLUE='#2E75B6'; LIGHT='#D9EAF7'; GREEN='#D9EAD3'; YELLOW='#FFF2CC'; RED='#F4CCCC'; GREY='#F3F6F8'; TEXT='#172B3A'; LINE='#5B7083'
font_path='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
bold_path='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def F(n,b=False): return ImageFont.truetype(bold_path if b else font_path,n)

def text_box(d, xy, text, fill=LIGHT, outline=BLUE, title=False, fs=24):
    x1,y1,x2,y2=xy
    d.rounded_rectangle(xy, radius=16, fill=fill, outline=outline, width=3)
    lines=[]
    maxw=x2-x1-30
    words=text.split()
    cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if d.textbbox((0,0),t,font=F(fs,title))[2] <= maxw: cur=t
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    total=len(lines)*(fs+8)
    yy=y1+(y2-y1-total)/2
    for line in lines:
        bb=d.textbbox((0,0),line,font=F(fs,title)); tw=bb[2]
        d.text((x1+(x2-x1-tw)/2,yy),line,fill=TEXT,font=F(fs,title))
        yy+=fs+8

def arrow(d,a,b,label=None):
    x1,y1=a; x2,y2=b
    d.line((x1,y1,x2,y2),fill=LINE,width=5)
    # basic arrow head
    import math
    ang=math.atan2(y2-y1,x2-x1); L=16
    p1=(x2-L*math.cos(ang-0.55),y2-L*math.sin(ang-0.55)); p2=(x2-L*math.cos(ang+0.55),y2-L*math.sin(ang+0.55))
    d.polygon([(x2,y2),p1,p2],fill=LINE)
    if label:
        mx,my=(x1+x2)/2,(y1+y2)/2
        d.rounded_rectangle((mx-100,my-18,mx+100,my+18),radius=6,fill='white')
        d.text((mx-90,my-12),label,fill=TEXT,font=F(18))

def title(d, t, sub):
    d.rectangle((0,0,W,95),fill=NAVY)
    d.text((45,22),t,fill='white',font=F(37,True))
    d.text((48,65),sub,fill='#D9EAF7',font=F(17))

def footer(d, txt='Public-source map — CONFIRMED: confirmed nodes; INFERRED: inferred/recommended nodes — 25 Jul 2026'):
    d.text((45,H-40),txt,fill=LINE,font=F(16))

# Product architecture
im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im); title(d,'OpenEvidence Product Architecture','Publicly evidenced features and explicitly inferred platform layers')
text_box(d,(70,155,390,290),'CONFIRMED: Verified clinician identity & consent',GREEN,fs=25)
text_box(d,(70,400,390,535),'CONFIRMED: Questions, Visits documents & optional EHR context',GREEN,fs=23)
text_box(d,(570,120,950,255),'CONFIRMED: Licensed journals, guidelines & society content',GREEN,fs=23)
text_box(d,(570,345,950,490),'INFERRED: Rights-aware ingestion, versioning, indexes & retrieval',YELLOW,fs=23)
text_box(d,(570,615,950,760),'CONFIRMED: Specialty models / CONFIRMED: DeepConsult / INFERRED: orchestration',GREEN,fs=23)
text_box(d,(1150,205,1530,350),'CONFIRMED: Cited answer + CONFIRMED: EvidenceGrade',GREEN,fs=26)
text_box(d,(1150,470,1530,620),'CONFIRMED: Note, trial match, Dialer documentation, EHR workflow',GREEN,fs=22)
text_box(d,(1150,735,1530,880),'INFERRED: Clinician review, accountable action & outcome loop',YELLOW,fs=22)
arrow(d,(390,222),(570,222)); arrow(d,(760,255),(760,345)); arrow(d,(760,490),(760,615)); arrow(d,(390,467),(570,467)); arrow(d,(950,687),(1150,310)); arrow(d,(1340,350),(1340,470)); arrow(d,(1340,620),(1340,735))
footer(d); im.save(OUT/'01_product_architecture.png')

# AI architecture
im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im); title(d,'AI / RAG Architecture Assessment','Confirmed claims versus strongest functional inference')
text_box(d,(70,145,385,275),'CONFIRMED: Clinician question; optional patient/session context',GREEN,fs=24)
text_box(d,(470,145,785,275),'INFERRED: Intent, risk & specialty router',YELLOW,fs=25)
text_box(d,(870,145,1185,275),'CONFIRMED: “Conductor” routes specialised models',GREEN,fs=24)
text_box(d,(1270,145,1585,275),'CONFIRMED: DeepConsult for multi-study work',GREEN,fs=24)
text_box(d,(250,430,620,585),'INFERRED: Licensed corpus retrieval, metadata filtering & reranking',YELLOW,fs=24)
text_box(d,(720,430,1090,585),'INFERRED: Context selection, source diversity & evidence synthesis',YELLOW,fs=24)
text_box(d,(1190,430,1560,585),'CONFIRMED: Citations + CONFIRMED: EvidenceGrade where gradeable',GREEN,fs=24)
text_box(d,(460,750,780,900),'INFERRED: Claim–source verifier, contradiction and applicability checks',YELLOW,fs=23)
text_box(d,(1010,750,1330,900),'CONFIRMED: / INFERRED: Clinician review and documented decision',GREEN,fs=23)
arrow(d,(385,210),(470,210)); arrow(d,(785,210),(870,210)); arrow(d,(1185,210),(1270,210)); arrow(d,(1030,275),(905,430)); arrow(d,(620,507),(720,507)); arrow(d,(1090,507),(1190,507)); arrow(d,(1375,585),(1170,750)); arrow(d,(780,825),(1010,825));
footer(d,'Public-source map — evidence labels reflect the report; verifier layer is an Ovexis recommendation'); im.save(OUT/'02_ai_rag_architecture.png')

# data flow
im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im); title(d,'Healthcare Data Flow','Where data enters, how it should be controlled, and where public detail ends')
text_box(d,(55,150,385,310),'CONFIRMED: Evidence sources: journals, guidelines, society content',GREEN,fs=25)
text_box(d,(55,510,385,670),'CONFIRMED: Patient documents; CONFIRMED: named partner Epic context',GREEN,fs=25)
text_box(d,(535,130,925,285),'INFERRED: Rights / consent / BAA / identity / data minimisation',YELLOW,fs=25)
text_box(d,(535,390,925,545),'INFERRED: Parse, normalise, temporally reconcile, provenance',YELLOW,fs=25)
text_box(d,(535,650,925,805),'INFERRED: Query context + retrieval + speciality reasoning',YELLOW,fs=25)
text_box(d,(1080,255,1460,410),'CONFIRMED: Cited response, evidence grade, note/trial candidate',GREEN,fs=24)
text_box(d,(1080,590,1460,745),'INFERRED: Clinician review / sign-off / task & follow-up closure',YELLOW,fs=24)
arrow(d,(385,230),(535,207)); arrow(d,(385,590),(535,467)); arrow(d,(730,285),(730,390)); arrow(d,(730,545),(730,650)); arrow(d,(925,727),(1080,335)); arrow(d,(1270,410),(1270,590))
footer(d,'No public OpenEvidence FHIR schema, data retention table or write-back map was verified.'); im.save(OUT/'03_healthcare_data_flow.png')

# Journey
im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im); title(d,'Clinician Journey','Publicly evidenced path and unknown enterprise/patient controls')
steps=[('Discover','CONFIRMED: Web/app/peer','GREEN'),('Register','CONFIRMED: Account details','GREEN'),('Verify','CONFIRMED: NPI/licence','GREEN'),('Consent','CONFIRMED: Terms/BAA','GREEN'),('Ask','CONFIRMED: Clinical question','GREEN'),('Inspect','CONFIRMED: Citations/grade','GREEN'),('Act','INFERRED: Review/decision','YELLOW'),('Retain','CONFIRMED: Visit/Dialer/context','GREEN')]
colors={'GREEN':GREEN,'YELLOW':YELLOW}
x=55
for i,(h,t,c) in enumerate(steps):
    text_box(d,(x,330,x+185,540),h+'\n'+t,colors[c],fs=21,title=True)
    if i<len(steps)-1: arrow(d,(x+185,435),(x+220,435))
    x+=220
text_box(d,(170,690,750,830),'CONFIRMED: Visits: transcription, templates, documents and post-visit query',GREEN,fs=25)
text_box(d,(1040,690,1620,830),'CONFIRMED: Dialer: call, SMS, fax, voicemail, Create Visit',GREEN,fs=25)
arrow(d,(870,540),(460,690)); arrow(d,(1100,540),(1330,690))
footer(d,'Exact screens, settings, permissions, support, renewal and enterprise admin flows are not publicly verified.'); im.save(OUT/'04_user_journey.png')

# dependency
im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im); title(d,'Feature Dependency Graph','The longitudinal platform capabilities required after an AI answer')
items=[('CONFIRMED: Identity & credential',GREEN),('CONFIRMED: Consent / BAA / authority',GREEN),('INFERRED: Data acquisition & reconciliation',YELLOW),('CONFIRMED: Retrieval + specialised reasoning',GREEN),('CONFIRMED: Citations + CONFIRMED: evidence grading',GREEN),('INFERRED: Review + accountable action',YELLOW),('INFERRED: Follow-up, outcomes & learning',YELLOW)]
y=125
for i,(t,c) in enumerate(items):
    text_box(d,(600,y,1200,y+95),t,c,fs=26)
    if i<len(items)-1: arrow(d,(900,y+95),(900,y+130))
    y+=130
text_box(d,(80,400,440,560),'Ovexis edge: patient-owned longitudinal provenance graph',YELLOW,fs=25)
text_box(d,(1360,400,1720,560),'Ovexis edge: local policy, safety case and outcome ledger',YELLOW,fs=25)
arrow(d,(440,480),(600,480)); arrow(d,(1200,610),(1360,480))
footer(d); im.save(OUT/'05_feature_dependency_graph.png')

# bmc
im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im); title(d,'OpenEvidence Business Model Canvas','Publicly evidenced components and strategic inference')
boxes=[
((50,130,400,380),'Key partners','CONFIRMED: Publishers/societies\nCONFIRMED: Health systems\nCONFIRMED: Microsoft/Veeva\nCONFIRMED: GCP/Vercel',GREEN),
((430,130,780,380),'Key activities','INFERRED: Content rights & ingestion\nINFERRED: Retrieval/evaluation\nINFERRED: Clinical workflow\nINFERRED: Advertiser ops',YELLOW),
((810,130,1160,380),'Value proposition','CONFIRMED: Fast cited evidence\nCONFIRMED: Free verified access\nCONFIRMED: Workflow expansion',GREEN),
((1190,130,1540,380),'Customer segments','INFERRED: Clinicians\nINFERRED: Health systems\nINFERRED: Advertisers\nINFERRED: Publishers',YELLOW),
((50,450,540,730),'Key resources','INFERRED: Content rights\nINFERRED: Verified audience\nINFERRED: Specialised models\nINFERRED: Trust brand',YELLOW),
((570,450,1060,730),'Channels & relationships','CONFIRMED: Web/iOS/Android\nINFERRED: Product-led word of mouth\nCONFIRMED: EHR/platform integrations',GREEN),
((1090,450,1540,730),'Revenue / cost','CONFIRMED: Ads & partnerships\nINFERRED: Enterprise route\nINFERRED: Content + compute + staff + security costs',YELLOW),
]
for xy,h,t,c in boxes:
    text_box(d,xy,h+'\n'+t,c,fs=23,title=True)
footer(d); im.save(OUT/'06_business_model_canvas.png')
print('Wrote diagrams to',OUT)
