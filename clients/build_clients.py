import json,re,os
os.chdir('/workspace/clayworks/client-flow/clients')
fh=open('../client_flow.html').read()
FLOW=json.loads(re.search(r'const FLOW = (.*?);\n</script>',fh,re.S).group(1))
FLOW=json.loads(re.sub(r"\bJack\b","Theo",json.dumps(FLOW,ensure_ascii=False)));flow={"phases":[x for x in FLOW["phases"] if x["id"]!="find"],"steps":[{k:s[k] for k in("phase","title","owner","client","us","tool","timing","bots","gates","proposed_bots") if k in s} for s in FLOW["steps"] if s["phase"]!="find"]}
assert len(flow["steps"])==53
AFTER={'c1':11,'c2':11,'c3':12,'c4':12,'c5':8,'c6':12,'c7':12,'c8':13,'c9':13,'c10':14,'c11':14,'c12':17,'c13':17,'c14':16,'c15':15,'c16':15,'c17':16,'c18':15,'c19':16,'c20':35,'c21':20,'c22':18,'c23':19,'c24':21,'c25':25,'c26':28,'c27':30,'c28':34,'c29':32,'c30':31}
CKO={'c1':'Joy','c2':'Joy','c5':'Client, Callum','c6':'Client, Joy','c7':'Joy','c25':'Joy','c12':'Joy','c13':'Theo, Joy','c22':'Callum','c23':'Callum','c26':'Client','c28':'Callum','c30':'Joy'}
meta=json.load(open('page_meta.json'));T=open('_page_template.html').read()
ORDER=["kmc","prime-marketing","variolytics","servicefirst","odd-latent"]
cards=[]
def page(slug,client,m,out):
    data=json.dumps({"slug":slug,"client":client,"meta":m,"flow":flow,"after":AFTER,"ckowner":CKO},ensure_ascii=False)
    html=T.replace('/*DATA*/',data).replace('/*TITLE*/',client["client"]["name"])
    bad=re.findall(r'(?i)(api[_-]?key=|password\s*[:=]\s*\S|sk-[a-z0-9]{10})',html)
    assert not bad,(slug,bad); assert '\u2014' not in html and '\u2013' not in html,slug
    if slug=='kmc': assert not re.search(r'(?i)offshor|outsourc|\bbpo\b|manila|jack page',html),'kmc words'
    open(out,'w').write(html)
for slug in ORDER:
    c=json.load(open(f'{slug}.status.json'));m=meta[slug]
    page(slug,c,m,f'{slug}.html')
    st=list(c["steps"].values())+list(c["checklist"].values())
    cnt={k:sum(1 for x in st if x["status"]==k) for k in("done","not_done","unclear","n_a")}
    miss=len(m["urgent"])+cnt["not_done"]+cnt["unclear"]
    cards.append(dict(slug=slug,name=c["client"]["name"],status=m["status"],tone=m["tone"],health=m["health"],steps=c["steps_counts"],check=c["checklist_counts"],cnt=cnt,missing=miss,bl=m["blacklist"]))
# template
D,X=[],[]
blank={"client":{"name":"New client","tenant":"","state":"","raw_date":""},"status_values":"done | not_done | unclear | n_a","source_default":"clients/raw/<slug>.md",
 "steps":{f"step{i}":{"title":s["title"],"status":"unclear","evidence":"","source":""} for i,s in enumerate(flow["steps"])},
 "checklist":{},"spot_checks":[]}
exec(open('gen_status.py').read().split('D,N,U,X')[0])
CL=CHECK.split('|') if isinstance(CHECK,str) else CHECK
blank["checklist"]={f"c{i+1}":{"title":t,"status":"unclear","evidence":"","source":""} for i,t in enumerate(CL)}
bmeta={"status":"Onboarding","tone":"grey","health":"Not set","dates":[["Signed",""],["First send",""],["Pilot ends",""]],"blacklist":{"loaded":"unclear","checked":"unclear","gate":"unclear","entries":"","issues":[]},"urgent":[],"security":""}
json.dump(blank,open('_template.status.json','w'),indent=1,ensure_ascii=False)
json.dump(bmeta,open('_template.meta.json','w'),indent=1,ensure_ascii=False)
page('_template',blank,bmeta,'_template.html')
# index
def bar(c,t):
    return '<div class="pb">'+''.join(f'<i style="width:{100*c.get(k,0)/t:.1f}%;background:{col}"></i>' for k,col in (("done","var(--ok)"),("not_done","var(--no)"),("unclear","var(--un)"),("n_a","#cbd5e1")))+'</div>'
SL={"done":"&#10004; Done","not_done":"&#10008; Not done","unclear":"? Unclear"}
cardh=''.join(f'''<a class="cc" href="{c["slug"]}.html"><div class="row"><h2>{c["name"]}</h2><span class="pill {c["tone"]}">{c["status"]}</span></div>
<small>Health: {c["health"]}</small>
<div class="pr"><b><span>Full checklist (from proof)</span><span>{c["cnt"]["done"]} of {83-c["cnt"]["n_a"]} done</span></b>{bar({"done":c["cnt"]["done"]},83-c["cnt"]["n_a"])}</div><small>83 items: 53 journey steps + 30 onboarding items. {c["cnt"]["not_done"]} not done, {c["cnt"]["unclear"]} unclear, {c["cnt"]["n_a"]} N/A.</small>
<div class="row"><span><b>{c["missing"]}</b> items missing or to confirm</span></div>
<div class="row bl"><span>Blacklist:</span><span class="st {c["bl"]["loaded"]}">Loaded {SL[c["bl"]["loaded"]]}</span><span class="st {c["bl"]["checked"]}">Checked {SL[c["bl"]["checked"]]}</span><span class="st {c["bl"]["gate"]}">Gate {SL[c["bl"]["gate"]]}</span></div></a>''' for c in cards)
css=re.search(r'<style>(.*?)</style>',T,re.S).group(1)
idx=f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Client checklists | Clayworks</title>
<script>const INDEX={json.dumps(cards,ensure_ascii=False)};</script><style>{css}
.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:12px}}.cc{{display:block;background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;color:inherit;text-decoration:none}}.cc:hover{{border-color:var(--acc)}}
.cc h2{{margin:0;font-size:19px}}.row{{display:flex;justify-content:space-between;align-items:center;gap:6px;flex-wrap:wrap;margin:6px 0;font-size:14px}}.bl .st{{font-size:12px}}</style></head><body>
<header><div class="crumb"><a href="../client_flow.html">&larr; Client journey</a> &middot; <a href="_template.html">Blank template</a></div><h1>Client checklists</h1><p>One page per client. Each shows every journey step and the 30-item onboarding checklist, with proof for each. Green = done, red = not done, amber = unclear, grey = N/A.</p></header>
<main><div class="cards">{cardh}</div>
<p class="src">Built 4 Nov 2026 from the client files plus read-only checks in Client Hub and SmartLead. Not published. One client tracker holds plain-text passwords; values are never shown here.</p></main></body></html>'''
assert '\u2014' not in idx and '\u2013' not in idx
open('index.html','w').write(idx)
for c in cards: print(c["name"],c["steps"],c["check"],c["missing"])
