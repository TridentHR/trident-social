import base64, os, sys
from playwright.sync_api import sync_playwright

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = R + "/tools/.fonts/gf/ofl"
OUT = R + "/2026-11-18-newsdesk-24"
IMG = base64.b64encode(open(OUT + "/lead.jpg", "rb").read()).decode()
DATE_L, DATE_S, NO = "Wednesday 18 November 2026", "18 Nov 2026", 24
TOTAL = 5

def ff(name, path, style="normal", w="100 900"):
    b = base64.b64encode(open(D + path, "rb").read()).decode()
    return f"@font-face{{font-family:'{name}';font-style:{style};font-weight:{w};src:url(data:font/ttf;base64,{b})}}"
FONTS = "".join([ff("Inter", "/inter/Inter[opsz,wght].ttf"), ff("Fraktur", "/unifrakturmaguntia/UnifrakturMaguntia-Book.ttf"),
    ff("Caslon", "/librecaslontext/LibreCaslonText[wght].ttf"), ff("Caslon", "/librecaslontext/LibreCaslonText-Italic[wght].ttf", "italic")])

# ---------- front page (as No. 23, no poppy) ----------
FCSS = """*{margin:0;padding:0;box-sizing:border-box;font-feature-settings:'dlig' 0,'hlig' 0,'hist' 0}body{margin:0;font-variant-numeric:lining-nums}.pg{width:1080px;height:1350px;overflow:hidden;display:flex;flex-direction:column}.up{text-transform:uppercase}
.pg{background:#FFFFFF;padding:52px 60px 44px;color:#111}
.np{display:flex;align-items:center;gap:24px;padding-bottom:14px}
.name{flex:1;text-align:center;font-family:Fraktur;font-size:84px;color:#0B1235;line-height:1;white-space:nowrap}
.dl{display:flex;justify-content:space-between;border-top:3px solid #111;border-bottom:1px solid #111;padding:9px 0;font-family:Inter;font-size:15px;font-weight:600;letter-spacing:.14em}
h1{font-family:Caslon;font-weight:700;font-size:88px;line-height:.98;letter-spacing:-.02em;margin-top:30px;color:#0B1235}
.deck{font-variant-ligatures:none;font-family:Caslon;font-style:italic;font-size:34px;line-height:1.3;margin-top:18px;color:#333}
.grid{display:flex;gap:30px;margin-top:28px;border-top:1px solid #111;padding-top:24px;flex:1}
.vr{width:1px;background:#111}
.lead2{flex:2;display:flex;flex-direction:column}
.lead2 img{width:100%;height:290px;object-fit:cover;object-position:50% 50%;display:block}
.cap{font-variant-ligatures:none;font-feature-settings:'liga' 0,'dlig' 0;font-family:Caslon;font-style:italic;font-size:17px;color:#555;margin-top:8px;padding-bottom:14px;border-bottom:1px solid #111}
.lc{column-count:2;column-gap:26px;column-fill:balance;margin-top:16px}
.scot{margin-top:auto;display:flex;align-items:center;gap:16px;border-top:3px solid #0B1235;padding:12px 0 0;font-family:Caslon;font-weight:700;font-size:23px;color:#111}
.scot b{font-family:Inter;font-size:14px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:#fff;background:#0B1235;padding:6px 10px}
.lc p{font-family:Caslon;font-size:21px;line-height:1.45;color:#222}
.lc p:first-child::first-letter{font-family:Caslon;font-weight:700;font-size:66px;float:left;line-height:.8;margin:5px 9px 0 0;color:#0B1235}
.side{flex:1;display:flex;flex-direction:column}
.st+.st{border-top:1px solid #111;margin-top:20px;padding-top:20px}
.st .k{font-family:Inter;font-size:13px;font-weight:800;letter-spacing:.2em;color:#0B1235}
.st h3{font-family:Caslon;font-weight:700;font-size:36px;line-height:1.08;margin-top:8px}
.st p{font-family:Caslon;font-size:22px;line-height:1.45;margin-top:10px;color:#333}
.ft{display:flex;justify-content:space-between;border-top:3px solid #111;padding-top:12px;margin-top:22px;font-family:Inter;font-size:15px;font-weight:700;letter-spacing:.16em}
"""
S2 = ("Tribunals", "Acas may not call you first", "From 26 November, Acas does not have to contact you if it decides settlement is not possible. The claim could be your first warning.")
S3 = ("Dismissal", "Six weeks to six months", "From 1 January, staff with six months' service can claim unfair dismissal. Make probation decisions well before then.")
LEAD = ("New regulations made on 12 November mean every employer in England, Wales and Scotland must give workers a written statement of their right to join a trade union. "
        "New starters get it with their written terms from 1 January 2027. Existing staff must have it by 5 April 2027, then once a year. "
        "The government has published the form. You cannot add to it or change it.")
front = f"""<div class="pg">
<div class="np"><div class="name">Trident HR Newsdesk</div></div>
<div class="dl up"><span>{DATE_L}</span><span>UK employment news</span><span>Edition No. {NO}</span></div>
<h1>Every worker gets a union statement</h1>
<div class="deck">From 1 January every employer must hand out a set form. Existing staff need it by 5 April.</div>
<div class="grid"><div class="lead2"><img src="data:image/jpeg;base64,{IMG}"><div class="cap">New starters get the statement with their written terms from 1 January.</div><div class="lc"><p>{LEAD}</p></div><div class="scot"><b>Trident</b>Now members of Dundee &amp; Angus and Glasgow Chambers</div></div><div class="vr"></div>
<div class="side">{''.join(f'<div class="st"><div class="k up">{s[0]}</div><h3>{s[1]}</h3><p>{s[2]}</p></div>' for s in (S2, S3))}</div></div>
<div class="ft up"><span>tridenthr.co.uk</span><span>Full stories: link in bio</span></div></div>"""

# ---------- inside pages (as No. 23) ----------
CSS = """*{margin:0;padding:0;box-sizing:border-box;font-variant-numeric:lining-nums;font-variant-ligatures:none;font-feature-settings:'dlig' 0,'hlig' 0,'hist' 0}
.pg{width:1080px;height:1350px;background:#FFFFFF;padding:44px 60px 44px;color:#111;display:flex;flex-direction:column}
.up{text-transform:uppercase}
.run{display:flex;justify-content:space-between;align-items:center;padding-bottom:12px;border-bottom:3px solid #111}
.run .n{font-family:Caslon;font-weight:700;font-size:34px;color:#0B1235;width:160px}
.run .m{font-family:Fraktur;font-size:38px;color:#0B1235;white-space:nowrap}
.run .d{font-family:Inter;font-size:14px;font-weight:700;letter-spacing:.14em;width:160px;text-align:right}
.rule2{height:1px;background:#111;margin-top:4px}
.sec{display:inline-block;margin-top:30px;font-family:Inter;font-size:15px;font-weight:800;letter-spacing:.22em;color:#FFFFFF;background:#0B1235;padding:7px 14px}
h1{font-family:Caslon;font-weight:700;font-size:80px;line-height:1;letter-spacing:-.02em;color:#0B1235;margin-top:20px}
.deck{font-family:Caslon;font-style:italic;font-size:31px;line-height:1.32;color:#333;margin-top:16px;padding-bottom:22px;border-bottom:1px solid #111}
.body{display:flex;gap:28px;margin-top:24px;flex:1}
.col{flex:1;font-family:Caslon;font-size:22px;line-height:1.5;color:#222}
.col p+p{margin-top:14px}
.col h4{font-family:Inter;font-size:14px;font-weight:800;letter-spacing:.16em;color:#0B1235;text-transform:uppercase;margin:18px 0 6px}
.dc::first-letter{font-family:Caslon;font-weight:700;font-size:72px;float:left;line-height:.8;margin:6px 10px 0 0;color:#0B1235}
.vr{width:1px;background:#111}
.pull{border-top:3px solid #0B1235;border-bottom:1px solid #0B1235;padding:18px 0 20px;margin:4px 0 18px}
.pull q{display:block;font-family:Caslon;font-style:italic;font-size:34px;line-height:1.22;color:#0B1235;quotes:"\\201C" "\\201D"}
.pull q::before{content:open-quote;font-size:70px;line-height:0;vertical-align:-.38em;margin-right:4px;color:#0B1235}
.pull span{display:block;font-family:Inter;font-size:13px;font-weight:800;letter-spacing:.16em;color:#666;margin-top:12px}
.box{border:2px solid #0B1235;padding:16px 18px}
.box .h{font-family:Inter;font-size:14px;font-weight:800;letter-spacing:.18em;color:#0B1235}
.box ol{list-style:none;counter-reset:x;margin-top:6px}
.box li{counter-increment:x;display:flex;gap:12px;font-family:Caslon;font-size:21px;line-height:1.35;padding:10px 0;border-bottom:1px solid #ccc}
.box li:last-child{border-bottom:0}
.box li::before{content:counter(x);font-weight:700;color:#0B1235}
.ft{display:flex;justify-content:space-between;border-top:3px solid #111;padding-top:12px;margin-top:20px;font-family:Inter;font-size:15px;font-weight:700;letter-spacing:.16em}
.dr{display:flex;gap:34px;padding:26px 0;border-bottom:1px solid #111;align-items:flex-start}
.dr .dt{width:250px;flex-shrink:0}
.dr .dt b{display:block;white-space:nowrap;font-family:Caslon;font-weight:700;font-size:72px;line-height:.95;color:#0B1235}
.dr .dt span{display:block;text-transform:uppercase;font-family:Inter;font-size:14px;font-weight:800;letter-spacing:.16em;color:#666;margin-top:8px}
.dr .tx .k{font-family:Inter;font-size:13px;font-weight:800;letter-spacing:.18em;color:#666}
.dr .tx h3{font-family:Caslon;font-weight:700;font-size:40px;line-height:1.1;color:#111;margin-top:6px}
.dr .tx p{font-family:Caslon;font-size:25px;line-height:1.45;color:#333;margin-top:8px}
"""
def head(n):
    return f'<div class="run"><span class="n">{n}</span><span class="m">Trident HR Newsdesk</span><span class="d up">{DATE_S}</span></div><div class="rule2"></div>'
def foot(n, last=False):
    return f'<div class="ft up"><span>tridenthr.co.uk</span><span>{"Full stories: link in bio" if last else f"Page {n} of {TOTAL}"}</span></div>'
def story(n, sec, h, deck, c1, pull, src, c2, acts):
    return f'''<div class="pg">{head(n)}
<div><span class="sec up">{sec}</span></div>
<h1>{h}</h1><div class="deck">{deck}</div>
<div class="body"><div class="col dc">{c1}</div><div class="vr"></div>
<div class="col"><div class="pull"><q>{pull}</q><span class="up">{src}</span></div>{c2}</div><div class="vr"></div>
<div class="col"><div class="box"><div class="h up">Do this now</div><ol>{"".join(f"<li>{a}</li>" for a in acts)}</ol></div></div></div>
{foot(n)}</div>'''

p2 = story(2, "Trade Unions", "Union rights statement from 1 January",
 "A set form for every worker, every year. There is no exemption for small businesses.",
 "<p>The Statement of Trade Union Rights Regulations 2026 were made on 12 November. They bring in a new duty from the Employment Rights Act 2025.</p><p>Every employer must give each worker a written statement that they have the right to join a trade union.</p><h4>When</h4><p>New starters from 1 January 2027 get it with their written statement of particulars. Existing staff need it by 5 April 2027.</p>",
 "You cannot add to the statement or change its wording.", "The rule",
 "<h4>Every year</h4><p>It then goes out again by 5 April each year. Hand it over, post it, email it, or put it on your intranet and tell staff in writing where it is.</p><h4>If you forget</h4><p>If a worker wins another tribunal claim, the award can rise by two or four weeks' pay.</p>",
 ["Download the standardised statement from GOV.UK.", "Add it to your new starter pack.", "Plan how existing staff get it by 5 April.", "Keep a record of who got it and when."])

p3 = story(3, "Tribunals", "Acas may not call you first",
 "From 26 November, the first sign of a claim could be the claim itself.",
 "<p>New rules for Acas early conciliation start on 26 November 2026. Early conciliation is still needed before most tribunal claims.</p><p>Anyone notifying Acas must now say whether they want to settle. If they do, they give more detail, including whether they raised it with you first.</p><h4>What changes</h4><p>Acas no longer has to contact you if it decides settlement is not possible.</p>",
 "If Acas does call, the employee is open to settling. Answer it quickly.", "The opportunity",
 "<h4>Why it matters</h4><p>A grievance that was logged and answered shows you took the concern seriously. One left without a reply will be visible from the start.</p><p>With a six-month time limit, a claim can arrive long after the event.</p>",
 ["Name one person to handle Acas contact.", "Check your phone and email details are current.", "Log and answer every grievance in writing.", "Keep records long enough to defend a late claim."])

p4 = story(4, "Dismissal", "Six weeks to six months",
 "From 1 January, unfair dismissal rights start after six months' service, not two years.",
 "<p>The Employment Rights Act 2025 cuts the qualifying period for unfair dismissal from two years to six months on 1 January 2027.</p><p>It is not only about new hires. Existing staff with six months' service can claim if dismissed on or after that date.</p><h4>Probation</h4><p>Probation does not stop the clock, and extending it does not either.</p>",
 "Make the probation decision by month five, not month six.", "Our advice",
 "<h4>The notice trap</h4><p>Statutory notice can count towards service. Someone dismissed just short of six months may be pushed over the line.</p><h4>Read more</h4><p>Our two-part series on the change is on the Newsdesk.</p>",
 ["List who will have six months' service on 1 January.", "Cap probation at five months.", "Update contracts that still mention two years.", "Brief managers on probation reviews."])

DIARY = [("26 Nov", "2026", "Tribunals", "Acas early conciliation changes", "Acas may issue a certificate without contacting you. Name who handles Acas contact."),
 ("1 Jan", "2027", "Dismissal", "Six-month qualifying period", "Unfair dismissal rights start after six months' service."),
 ("1 Jan", "2027", "Trade Unions", "Union rights statement starts", "New starters get it with their written terms."),
 ("5 Apr", "2027", "Trade Unions", "Existing staff deadline", "Every existing worker must have the statement. It then goes out by 5 April each year.")]
p5 = f'''<div class="pg">{head(5)}
<h1 style="margin-top:34px;padding-bottom:22px;border-bottom:3px solid #111">Dates for the diary</h1>
<div style="flex:1;display:flex;flex-direction:column;justify-content:space-evenly">{"".join(f'<div class="dr"><div class="dt"><b>{d}</b><span>{y}</span></div><div class="tx"><div class="k up">{k}</div><h3>{h}</h3><p>{t}</p></div></div>' for d,y,k,h,t in DIARY)}</div>
{foot(5, True)}</div>'''

with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page(viewport={"width": 1080, "height": 1350})
    pages = [(front, FCSS)] + [(h, CSS) for h in (p2, p3, p4, p5)]
    for i, (h, css) in enumerate(pages, 1):
        pg.set_content(f"<html><head><style>{FONTS}{css}</style></head><body style='margin:0'>{h}</body></html>"); pg.wait_for_timeout(500)
        pg.screenshot(path=f"{OUT}/page{i}.png"); print(f"{OUT}/page{i}.png")
    br.close()
