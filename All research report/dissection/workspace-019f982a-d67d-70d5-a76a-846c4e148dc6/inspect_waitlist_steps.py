import asyncio,json
from pathlib import Path
from playwright.async_api import async_playwright
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(headless=True,args=['--no-sandbox'])
  ctx=await b.new_context(viewport={'width':1200,'height':800})
  page=await ctx.new_page(); reqs=[]; page.on('request',lambda r:reqs.append((r.method,r.url)))
  await page.goto('https://www.regacore.com/waitlist', wait_until='domcontentloaded'); await page.wait_for_timeout(1000)
  out=[]
  async def snap(label):
   text=await page.locator('body').inner_text()
   inputs=await page.evaluate('''()=>Array.from(document.querySelectorAll('input,textarea,select')).map(i=>({tag:i.tagName,type:i.type,name:i.name,placeholder:i.placeholder,value:i.value,required:i.required}))''')
   buttons=await page.evaluate('''()=>Array.from(document.querySelectorAll('button')).map(b=>b.innerText.trim())''')
   out.append({'label':label,'text':text[:1500], 'inputs':inputs, 'buttons':buttons, 'reqs':reqs[-10:]})
  await snap('step1')
  for n in range(8):
   inputs=await page.query_selector_all('input,textarea,select')
   if not inputs: break
   meta=await page.evaluate('''el=>({type:el.type,name:el.name,placeholder:el.placeholder})''', inputs[0])
   typ=(meta.get('type') or '').lower(); name=(meta.get('name') or '').lower(); ph=(meta.get('placeholder') or '').lower()
   if typ=='email' or 'email' in name: val='research@example.com'
   elif typ in ['tel','number'] or 'phone' in name or 'mobile' in name: val='9000000000'
   elif 'age' in name or 'age' in ph: val='34'
   else: val='Research Test'
   try:
    await inputs[0].fill(val)
   except Exception as e:
    out.append({'label':f'fill_error_{n}','meta':meta,'error':repr(e)}); break
   await page.click('button[type="submit"]')
   await page.wait_for_timeout(1000)
   await snap(f'after_submit_{n+1}_{typ}_{name}')
   if any('script.google.com' in u for _,u in reqs):
    break
  await b.close()
  Path('/home/user/regacore_research/interactions/waitlist_steps.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
asyncio.run(main())
