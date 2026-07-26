import asyncio, json
from pathlib import Path
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
BASE='https://www.regacore.com'
OUT=Path('/home/user/regacore_research/interactions'); OUT.mkdir(parents=True,exist_ok=True)

async def snapshot(page,label):
    text=await page.locator('body').inner_text(timeout=5000)
    buttons=await page.evaluate('''() => Array.from(document.querySelectorAll('button')).map((b,i)=>({i,text:(b.innerText||b.getAttribute('aria-label')||'').trim(),type:b.type,disabled:b.disabled}))''')
    inputs=await page.evaluate('''() => Array.from(document.querySelectorAll('input,textarea,select')).map((x,i)=>({i,tag:x.tagName,type:x.getAttribute('type'),name:x.getAttribute('name'),placeholder:x.getAttribute('placeholder'),value:x.value, required:x.required}))''')
    await page.screenshot(path=str(OUT/f'{label}.jpg'), full_page=True, type='jpeg', quality=70)
    return {'label':label,'text':text,'buttons':buttons,'inputs':inputs,'url':page.url}

async def main():
    async with async_playwright() as p:
      browser=await p.chromium.launch(headless=True,args=['--no-sandbox'])
      ctx=await browser.new_context(viewport={'width':1200,'height':900})
      results=[]
      # Waitlist wizard
      page=await ctx.new_page()
      await page.goto(BASE+'/waitlist', wait_until='domcontentloaded')
      await page.wait_for_timeout(1500)
      results.append(await snapshot(page,'waitlist_step1_name'))
      await page.fill('input[name="name"]','Research Test')
      await page.click('button[type="submit"]')
      await page.wait_for_timeout(800)
      results.append(await snapshot(page,'waitlist_step2_after_name'))
      # Fill next input if exists but do not submit final if obvious
      # Checkout step one validation and transition if any no submit? click empty then fake? capture before payment, no payment attempt
      page2=await ctx.new_page()
      await page2.goto(BASE+'/checkout', wait_until='domcontentloaded')
      await page2.wait_for_timeout(1500)
      results.append(await snapshot(page2,'checkout_initial'))
      # Try invalid/empty validation only
      await page2.click('button:has-text("Continue")')
      await page2.wait_for_timeout(1000)
      results.append(await snapshot(page2,'checkout_after_empty_continue'))
      # Try a synthetic local-invalid email not final? It may create account; avoid external? Use invalid email to trigger HTML validation
      await page2.fill('input[type="email"]','invalid')
      await page2.click('button:has-text("Continue")')
      await page2.wait_for_timeout(1000)
      results.append(await snapshot(page2,'checkout_after_invalid_email'))
      # Concierge: click New AI Chat, specialist, sample review
      page3=await ctx.new_page(); await page3.goto(BASE+'/concierge', wait_until='domcontentloaded'); await page3.wait_for_timeout(2500)
      results.append(await snapshot(page3,'concierge_initial'))
      for sel,label in [('text=New AI Chat','concierge_after_new_chat'),('text=Specialist Directory','concierge_after_specialist'),('text=Review ApoB & LDL ratio','concierge_after_review_apob')]:
          try:
              await page3.click(sel, timeout=3000); await page3.wait_for_timeout(1000); results.append(await snapshot(page3,label))
          except Exception as e: results.append({'label':label,'error':repr(e)})
      # Data filters
      page4=await ctx.new_page(); await page4.goto(BASE+'/data', wait_until='domcontentloaded'); await page4.wait_for_timeout(2500)
      results.append(await snapshot(page4,'data_initial'))
      try:
          await page4.fill('input[placeholder="Search biomarkers..."]','cortisol'); await page4.wait_for_timeout(800); results.append(await snapshot(page4,'data_search_cortisol'))
      except Exception as e: results.append({'label':'data_search_cortisol','error':repr(e)})
      # Marketplace filters/search
      page5=await ctx.new_page(); await page5.goto(BASE+'/marketplace', wait_until='domcontentloaded'); await page5.wait_for_timeout(1500)
      results.append(await snapshot(page5,'marketplace_initial'))
      try:
          await page5.fill('input[placeholder="Search anything"]','NAD'); await page5.wait_for_timeout(800); results.append(await snapshot(page5,'marketplace_search_nad'))
      except Exception as e: results.append({'label':'marketplace_search_nad','error':repr(e)})
      await browser.close()
      (OUT/'interaction_inventory.json').write_text(json.dumps(results,indent=2), encoding='utf-8')
      print('done',len(results))

asyncio.run(main())
