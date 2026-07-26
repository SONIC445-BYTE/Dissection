import re,html,sys
t=open(sys.argv[1],encoding='utf-8',errors='ignore').read()
t=re.sub(r'(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>',' ',t)
t=re.sub(r'(?s)<[^>]+>','\n',t); t=html.unescape(t)
lines=[l.strip() for l in t.split('\n') if l.strip()]
seen=set(); out=[]
for l in lines:
    if l not in seen and 1<len(l)<200: seen.add(l); out.append(l)
n=int(sys.argv[2]) if len(sys.argv)>2 else 200
print('\n'.join(out[:n]))
