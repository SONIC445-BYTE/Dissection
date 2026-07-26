import asyncio,json,re
from pathlib import Path
from urllib.parse import urlparse
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
OUT=Path('/home/user/humanapi_research'); (OUT/'screenshots').mkdir(parents=True,exist_ok=True); (OUT/'dom').mkdir(exist_ok=True)
PAGES=[
('humanapi_redirect','https://www.humanapi.co/'),
('lexis_humanapi','https://risk.lexisnexis.com/products/humanapi'),
('health_intelligence_ehr','https://risk.lexisnexis.com/products/health-intelligence-ehr'),
('acquisition_press','https://risk.lexisnexis.com/about-us/press-room/press-release/20230425-humanapi-acquisition'),
('health_intelligence_2025','https://risk.lexisnexis.com/about-us/press-room/press-release/20250220-health-intelligence'),
('docs_getting_started','https://reference.humanapi.co/reference'),
('docs_overview','https://reference.humanapi.co/docs/overview'),
('docs_order_types','https://reference.humanapi.co/docs/configuring-order-types'),
('docs_submitting_orders','https://reference.humanapi.co/docs/submitting-orders'),
('docs_lifecycle','https://reference.humanapi.co/docs/order-fulfillment-lifecycle'),
('docs_reports','https://reference.humanapi.co/docs/reports'),
('docs_epic','https://reference.humanapi.co/page/epic-documentation'),
]
async def capture(ctx,name,url,suffix):
 page=await ctx.new_page(); rec={'name':name,'url':url,'requests':[],'responses':[],'hosts':[],'viewport':page.viewport_size}
 hosts=set()
 def on_req(r):
  try:
   hosts.add(urlparse(r.url).netloc)
   if len(rec['requests'])<300: rec['requests'].append({'method':r.method,'url':r.url,'type':r.resource_type})
  except Exception: pass
 def on_resp(r):
  try:
   hosts.add(urlparse(r.url).netloc)
   if len(rec['responses'])<300: rec['responses'].append({'status':r.status,'url':r.url,'headers':{k:v for k,v in r.headers.items() if k.lower() in ['server','content-type','cache-control','cf-cache-status','strict-transport-security','x-content-type-options','x-frame-options','content-security-policy']}})
  except Exception: pass
 page.on('request',on_req); page.on('response',on_resp)
 try:
  await page.goto(url,wait_until='domcontentloaded',timeout=60000)
  try: await page.wait_for_load_state('networkidle',timeout=10000)
  except PlaywrightTimeoutError: pass
  # close cookie banners if obvious buttons; don't submit forms
  for txt in ['Reject All','Reject all','Accept All','Accept all','Close']:
   try:
    await page.locator(f'button:has-text("{txt}")').first.click(timeout=1000)
    await page.wait_for_timeout(500)
    break
   except Exception: pass
  height=await page.evaluate('document.documentElement.scrollHeight')
  for i in range(min(8,max(2,int(height/1000)+1))+1):
   await page.evaluate('(y)=>window.scrollTo(0,y)', int(height*i/(min(8,max(2,int(height/1000)+1)))))
   await page.wait_for_timeout(250)
  await page.evaluate('window.scrollTo(0,0)'); await page.wait_for_timeout(500)
  rec['title']=await page.title(); rec['final_url']=page.url
  text=await page.locator('body').inner_text(timeout=5000)
  rec['body_text_sample']=text[:5000]; rec['body_text_length']=len(text)
  rec['links']=await page.evaluate('''()=>Array.from(document.querySelectorAll('a')).slice(0,300).map(a=>({text:(a.innerText||a.title||a.getAttribute('aria-label')||'').trim(),href:a.href}))''')
  rec['buttons']=await page.evaluate('''()=>Array.from(document.querySelectorAll('button,input[type=submit]')).slice(0,200).map(b=>({text:(b.innerText||b.value||b.getAttribute('aria-label')||'').trim(),type:b.type,disabled:b.disabled}))''')
  rec['inputs']=await page.evaluate('''()=>Array.from(document.querySelectorAll('input,textarea,select')).slice(0,200).map(i=>({tag:i.tagName,type:i.getAttribute('type'),name:i.getAttribute('name'),placeholder:i.getAttribute('placeholder'),required:i.required,value:i.value}))''')
  rec['images']=await page.evaluate('''()=>Array.from(document.images).slice(0,300).map(img=>({src:img.currentSrc||img.src,alt:img.alt,width:img.naturalWidth,height:img.naturalHeight}))''')
  rec['hosts']=sorted(hosts)
  (OUT/'dom'/f'{name}_{suffix}.txt').write_text(text,encoding='utf-8')
  path=OUT/'screenshots'/f'{name}_{suffix}.jpg'
  await page.screenshot(path=str(path),full_page=True,type='jpeg',quality=70)
  rec['screenshot']=str(path)
 except Exception as e: rec['error']=repr(e)
 await page.close(); return rec
async def main():
 async with async_playwright() as p:
  browser=await p.chromium.launch(headless=True,args=['--no-sandbox'])
  ctx=await browser.new_context(viewport={'width':1440,'height':1000})
  recs=[]
  for name,url in PAGES:
   print('desktop',name,flush=True); recs.append(await capture(ctx,name,url,'desktop'))
  await ctx.close()
  mctx=await browser.new_context(viewport={'width':390,'height':844},is_mobile=True,has_touch=True,device_scale_factor=2)
  for name,url in [('lexis_humanapi','https://risk.lexisnexis.com/products/humanapi'),('health_intelligence_ehr','https://risk.lexisnexis.com/products/health-intelligence-ehr'),('docs_getting_started','https://reference.humanapi.co/reference')]:
   print('mobile',name,flush=True); recs.append(await capture(mctx,name,url,'mobile'))
  await mctx.close(); await browser.close()
  (OUT/'capture_inventory.json').write_text(json.dumps(recs,indent=2),encoding='utf-8')
  print('done',len(recs))
asyncio.run(main())
