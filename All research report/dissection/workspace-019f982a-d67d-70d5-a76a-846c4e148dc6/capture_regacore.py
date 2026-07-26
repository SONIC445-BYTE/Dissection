import asyncio, json, os, re, time
from pathlib import Path
from urllib.parse import urlparse
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

BASE='https://www.regacore.com'
PAGES=[
 ('landing', '/'),
 ('whatwetest', '/whatwetest'),
 ('how-it-works', '/how-it-works'),
 ('checkout', '/checkout'),
 ('login', '/login'),
 ('waitlist', '/waitlist'),
 ('privacy', '/privacy'),
 ('termsandconditions', '/termsandconditions'),
 ('blog', '/blog'),
 ('blog_science_of_biological_aging', '/blog/science-of-biological-aging'),
 ('blog_understanding_apob', '/blog/understanding-apob'),
 ('blog_hormonal_optimization', '/blog/hormonal-optimization'),
 ('blog_longevity_protocol', '/blog/the-longevity-protocol'),
 ('blog_quest_labs_vs_home', '/blog/quest-labs-vs-at-home-draws'),
 ('blog_metabolic_health', '/blog/optimizing-metabolic-health'),
 ('blog_digital_twin', '/blog/the-digital-twin-architecture'),
 ('app_home', '/home'),
 ('app_data', '/data'),
 ('app_protocol', '/protocol'),
 ('app_concierge', '/concierge'),
 ('app_marketplace', '/marketplace'),
 ('notfound_terms', '/terms'),
]
OUT=Path('/home/user/regacore_research')
(OUT/'screenshots').mkdir(parents=True, exist_ok=True)
(OUT/'dom').mkdir(exist_ok=True)

async def capture_page(context, browser, name, path, viewport, suffix):
    page=await context.new_page()
    rec={'name':name,'path':path,'url':BASE+path,'viewport':viewport,'requests':[], 'responses':[], 'console':[], 'errors':[]}
    hosts=set()
    def on_req(req):
        try:
            u=req.url; hosts.add(urlparse(u).netloc)
            if len(rec['requests'])<200:
                rec['requests'].append({'method':req.method,'url':u,'resource_type':req.resource_type})
        except Exception: pass
    def on_resp(resp):
        try:
            u=resp.url; hosts.add(urlparse(u).netloc)
            if len(rec['responses'])<200:
                rec['responses'].append({'status':resp.status,'url':u,'headers':{k:v for k,v in resp.headers.items() if k.lower() in ['server','content-type','cache-control','cf-cache-status','x-matched-path','x-nextjs-prerender','x-next-cache-tags','access-control-allow-origin','strict-transport-security','x-content-type-options','referrer-policy']}})
        except Exception: pass
    page.on('request', on_req)
    page.on('response', on_resp)
    page.on('console', lambda msg: rec['console'].append({'type':msg.type,'text':msg.text[:500]}))
    page.on('pageerror', lambda err: rec['errors'].append(str(err)[:500]))
    try:
        await page.goto(BASE+path, wait_until='domcontentloaded', timeout=45000)
        try:
            await page.wait_for_load_state('networkidle', timeout=7000)
        except PlaywrightTimeoutError:
            pass
        # scroll through page to lazy-load assets and trigger reveal animations
        height = await page.evaluate('document.documentElement.scrollHeight')
        steps = max(1, min(8, int(height/800)+1))
        for i in range(steps+1):
            await page.evaluate('(y)=>window.scrollTo(0,y)', int(height*i/steps))
            await page.wait_for_timeout(300)
        await page.evaluate('window.scrollTo(0,0)')
        await page.wait_for_timeout(600)
        title=await page.title()
        rec['title']=title
        rec['final_url']=page.url
        rec['html_length']=len(await page.content())
        # DOM inventory
        bodytext=''
        try: bodytext=await page.locator('body').inner_text(timeout=5000)
        except Exception: pass
        rec['body_text_length']=len(bodytext)
        rec['body_text_sample']=bodytext[:4000]
        rec['links']=await page.evaluate('''() => Array.from(document.querySelectorAll('a')).slice(0,200).map(a=>({text:(a.innerText||a.getAttribute('aria-label')||a.title||'').trim(), href:a.href, target:a.target||''}))''')
        rec['buttons']=await page.evaluate('''() => Array.from(document.querySelectorAll('button')).slice(0,200).map(b=>({text:(b.innerText||b.getAttribute('aria-label')||'').trim(), type:b.type, disabled:b.disabled}))''')
        rec['inputs']=await page.evaluate('''() => Array.from(document.querySelectorAll('input,textarea,select')).slice(0,200).map(i=>({tag:i.tagName, type:i.getAttribute('type'), name:i.getAttribute('name'), placeholder:i.getAttribute('placeholder'), aria:i.getAttribute('aria-label'), required:i.required, value:i.value}))''')
        rec['images']=await page.evaluate('''() => Array.from(document.images).slice(0,200).map(img=>({src:img.currentSrc||img.src, alt:img.alt, width:img.naturalWidth, height:img.naturalHeight, class:img.className}))''')
        rec['head_meta']=await page.evaluate('''() => Array.from(document.querySelectorAll('meta,link[rel="icon"],link[rel="canonical"]')).map(el=>({tag:el.tagName, name:el.getAttribute('name'), property:el.getAttribute('property'), rel:el.getAttribute('rel'), href:el.getAttribute('href'), content:el.getAttribute('content')}))''')
        rec['hosts']=sorted(hosts)
        shot_path=OUT/'screenshots'/f'{name}_{suffix}.jpg'
        await page.screenshot(path=str(shot_path), full_page=True, type='jpeg', quality=70)
        rec['screenshot']=str(shot_path)
        (OUT/'dom'/f'{name}_{suffix}.txt').write_text(bodytext, encoding='utf-8')
    except Exception as e:
        rec['capture_error']=repr(e)
    finally:
        await page.close()
    return rec

async def main():
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True, args=['--disable-gpu','--no-sandbox'])
        records=[]
        # Desktop all pages
        desktop={'width':1440,'height':1000,'device_scale_factor':1}
        context=await browser.new_context(viewport={'width':1440,'height':1000}, device_scale_factor=1, user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149 Safari/537.36')
        for name,path in PAGES:
            print('desktop', name, flush=True)
            records.append(await capture_page(context,browser,name,path,desktop,'desktop'))
        await context.close()
        # Mobile key pages
        mobile={'width':390,'height':844,'device_scale_factor':2, 'is_mobile':True}
        mctx=await browser.new_context(viewport={'width':390,'height':844}, device_scale_factor=2, is_mobile=True, has_touch=True, user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1')
        for name,path in [('landing','/'),('checkout','/checkout'),('app_home','/home'),('app_data','/data'),('app_concierge','/concierge'),('marketplace','/marketplace')]:
            print('mobile', name, flush=True)
            records.append(await capture_page(mctx,browser,name,path,mobile,'mobile'))
        await mctx.close()
        await browser.close()
        (OUT/'capture_inventory.json').write_text(json.dumps(records, indent=2), encoding='utf-8')
        print('done', len(records))

if __name__=='__main__': asyncio.run(main())
