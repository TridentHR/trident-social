import base64, os
from playwright.sync_api import sync_playwright

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = R + "/tools/.fonts/gf/ofl"
OUT = R + "/2026-11-25-unfair-dismissal"
IMG = base64.b64encode(open(R + "/assets/contractor-bg/bg-3.jpg", "rb").read()).decode()
DATE_L, DATE_S, TOTAL = "Wednesday 25 November 2026", "25 Nov 2026", 3

def ff(name, path, style="normal", w="100 900"):
    b = base64.b64encode(open(D + path, "rb").read()).decode()
    return f"@font-face{{font-family:'{name}';font-style:{style};font-weight:{w};src:url(data:font/ttf;base64,{b})}}"
FONTS = "".join([ff("Inter", "/inter/Inter[opsz,wght].ttf"), ff("Fraktur", "/unifrakturmaguntia/UnifrakturMaguntia-Book.ttf"),
    ff("Caslon", "/librecaslontext/LibreCaslonText[wght].ttf"), ff("Caslon", "/librecaslontext/LibreCaslonText-Italic[wght].ttf", "italic")])

FCSS = """*{margin:0;padding:0;box-sizing:border-box;font-variant-numeric:lining-nums;font-variant-ligatures:none;font-feature-settings:'dlig' 0,'hlig' 0,'hist' 0}.up{text-transform:uppercase}
.pg{width:1080px;height:1350px;overflow:hidden;display:flex;flex-direction:column;background:#FFFFFF;padding:52px 60px 44px;color:#111}
.name{text-align:center;font-family:Fraktur;font-size:84px;color:#0B1235;line-height:1;white-space:nowrap;padding-bottom:14px}
.dl{display:flex;justify-content:space-between;border-top:3px solid #111;border-bottom:1px solid #111;padding:9px 0;font-family:Inter;font-size:15px;font-weight:600;letter-spacing:.14em}
h1{font-family:Caslon;font-weight:700;font-size:80px;line-height:.98;letter-spacing:-.025em;margin-top:30px;color:#0B1235;white-space:nowrap}
.deck{font-family:Caslon;font-style:italic;font-size:34px;line-height:1.3;margin-top:18px;color:#333}
.grid{display:flex;gap:30px;margin-top:28px;border-top:1px solid #111;padding-top:24px;flex:1}
.vr{width:1px;background:#111}
.lead2{flex:2;display:flex;flex-direction:column}
.lead2 img{width:100%;height:290px;object-fit:cover;object-position:50% 55%;display:block}
.cap{font-family:Caslon;font-style:italic;font-size:17px;color:#555;margin-top:8px;padding-bottom:14px;border-bottom:1px solid #111}
.lc{column-count:2;column-gap:26px;column-fill:balance;margin-top:16px}
.lc p{font-family:Caslon;font-size:21px;line-height:1.45;color:#222}
.lc p:first-child::first-letter{font-family:Caslon;font-weight:700;font-size:66px;float:left;line-height:.8;margin:5px 9px 0 0;color:#0B1235}
.side{flex:1;display:flex;flex-direction:column}
.st+.st{border-top:1px solid #111;margin-top:20px;padding-top:20px}
.st h3{font-family:Caslon;font-weight:700;font-size:36px;line-height:1.08}
.st p{font-family:Caslon;font-size:22px;line-height:1.45;margin-top:10px;color:#333}
.ft{display:flex;justify-content:space-between;border-top:3px solid #111;padding-top:12px;margin-top:22px;font-family:Inter;font-size:15px;font-weight:700;letter-spacing:.16em}
"""
LEAD = ("The Employment Rights Act 2025 cuts the qualifying period for unfair dismissal from two years to six months on 1 January 2027. "
        "It is not only about new hires. Existing staff with six months' service can claim if they are dismissed on or after that date, "
        "and some dismissals, such as for whistleblowing or pregnancy, are already unfair from day one. "
        "The date that counts is when employment ends, including statutory notice. Someone dismissed just short of six months can still be pushed over the line, so check service dates before you act.")
SIDE = [("Probation won't protect you", "Protection depends on service, not probation. Anyone who started by early July 2026 will be past six months on 1 January."),
        ("No cap on awards", "The cap on the compensatory award is removed for dismissals on or after 1 January 2027."),
        ("Day one still applies", "Whistleblowing, pregnancy and discrimination claims never needed qualifying service.")]
front = f"""<div class="pg">
<div class="name">Trident HR Newsdesk</div>
<div class="dl up"><span>{DATE_L}</span><span>UK employment news</span><span>Employer guide</span></div>
<h1>Two years to six months</h1>
<div class="deck">From 1 January 2027, most staff can claim unfair dismissal after six months' service.</div>
<div class="grid"><div class="lead2"><img src="data:image/jpeg;base64,{IMG}"><div class="cap">Staff with six months' service on 1 January are protected straight away.</div><div class="lc"><p>{LEAD}</p></div></div><div class="vr"></div>
<div class="side">{''.join(f'<div class="st"><h3>{h}</h3><p>{t}</p></div>' for h, t in SIDE)}</div></div>
<div class="ft up"><span>tridenthr.co.uk</span><span>Page 1 of {TOTAL}</span></div></div>"""

CSS = """*{margin:0;padding:0;box-sizing:border-box;font-variant-numeric:lining-nums;font-variant-ligatures:none;font-feature-settings:'dlig' 0,'hlig' 0,'hist' 0}.up{text-transform:uppercase}
.pg{width:1080px;height:1350px;background:#FFFFFF;padding:44px 60px 44px;color:#111;display:flex;flex-direction:column}
.run{display:flex;justify-content:space-between;align-items:center;padding-bottom:12px;border-bottom:3px solid #111}
.run .n{font-family:Caslon;font-weight:700;font-size:34px;color:#0B1235;width:160px}
.run .m{font-family:Fraktur;font-size:38px;color:#0B1235;white-space:nowrap}
.run .d{font-family:Inter;font-size:14px;font-weight:700;letter-spacing:.14em;width:160px;text-align:right}
.rule2{height:1px;background:#111;margin-top:4px}
h1{font-family:Caslon;font-weight:700;font-size:80px;line-height:1;letter-spacing:-.02em;color:#0B1235;margin-top:34px}
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
.box{border:2px solid #0B1235;padding:16px 18px}
.box .h{font-family:Inter;font-size:14px;font-weight:800;letter-spacing:.18em;color:#0B1235}
.box ol{list-style:none;counter-reset:x;margin-top:6px}
.box li{counter-increment:x;display:flex;gap:12px;font-family:Caslon;font-size:21px;line-height:1.35;padding:10px 0;border-bottom:1px solid #ccc}
.box li:last-child{border-bottom:0}
.box li::before{content:counter(x);font-weight:700;color:#0B1235}
.ft{display:flex;justify-content:space-between;border-top:3px solid #111;padding-top:12px;margin-top:20px;font-family:Inter;font-size:15px;font-weight:700;letter-spacing:.16em}
.dr{display:flex;gap:34px;padding:30px 0;border-bottom:1px solid #111;align-items:flex-start}
.dr .dt{width:250px;flex-shrink:0}
.dr .dt b{display:block;white-space:nowrap;font-family:Caslon;font-weight:700;font-size:72px;line-height:.95;color:#0B1235}
.dr .dt span{display:block;text-transform:uppercase;font-family:Inter;font-size:14px;font-weight:800;letter-spacing:.16em;color:#666;margin-top:22px}
.dr .tx h3{font-family:Caslon;font-weight:700;font-size:40px;line-height:1.1;color:#111}
.dr .tx p{font-family:Caslon;font-size:25px;line-height:1.45;color:#333;margin-top:8px}
"""
def head(n):
    return f'<div class="run"><span class="n">{n}</span><span class="m">Trident HR Newsdesk</span><span class="d up">{DATE_S}</span></div><div class="rule2"></div>'
def foot(n, last=False):
    return f'<div class="ft up"><span>tridenthr.co.uk</span><span>{"Free guide: link in bio" if last else f"Page {n} of {TOTAL}"}</span></div>'

p2 = f'''<div class="pg">{head(2)}
<h1>Before 1 January</h1><div class="deck">Just over five weeks to check who is protected, and how you will make fair decisions.</div>
<div class="body"><div class="col dc"><p>From 1 January 2027, most employees can claim ordinary unfair dismissal after six months' service instead of two years.</p><p>The date that counts is when employment ends, not when you make the decision.</p><h4>Probation</h4><p>Probation does not stop the clock, and extending it does not either. Someone still on probation after six months can claim.</p><p>Make the probation decision early, with a fair review behind it.</p><h4>Existing staff</h4><p>The change is not only for new starters. Anyone already employed who reaches six months' service is covered.</p></div><div class="vr"></div>
<div class="col"><div class="pull"><q>Make the probation decision by month five, not month six.</q></div><h4>The notice trap</h4><p>Statutory notice counts towards service. Dismiss someone just short of six months and their notice can still take them over the line.</p><h4>A fair process</h4><p>You need one of five fair reasons and a fair process, such as the Acas Code for conduct and performance.</p><p>Investigate, put concerns in writing, hold a meeting with the right to be accompanied, and offer an appeal.</p></div><div class="vr"></div>
<div class="col"><div class="box"><div class="h up">Do this now</div><ol>{"".join(f"<li>{a}</li>" for a in ["List who will have six months' service on 1 January.", "Check probation end dates against it.", "Update contracts that still mention two years.", "Brief managers on fair dismissal."])}</ol></div><h4>What does not change</h4><p>Automatically unfair reasons, such as whistleblowing or pregnancy, still need no qualifying service. Discrimination claims never needed any.</p><h4>Our guide</h4><p>The five fair reasons, the dates that count and a one-page checklist.</p></div></div>
{foot(2)}</div>'''

DIARY = [("Now", "", "Check service dates", "List who will pass six months' service by 1 January, including statutory notice."),
         ("1 Jan", "2027", "Six-month qualifying period", "Unfair dismissal rights start after six months' service, not two years."),
         ("1 Jan", "2027", "Compensation cap removed", "No cap on the compensatory award for dismissals on or after this date.")]
p3 = f'''<div class="pg">{head(3)}
<h1 style="margin-top:34px;padding-bottom:22px;border-bottom:3px solid #111">Dates for the diary</h1>
<div style="flex:1;display:flex;flex-direction:column;justify-content:space-evenly">{"".join(f'<div class="dr"><div class="dt"><b>{d}</b><span>{y}</span></div><div class="tx"><h3>{h}</h3><p>{t}</p></div></div>' for d,y,h,t in DIARY)}</div>
{foot(3, True)}</div>'''

with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page(viewport={"width": 1080, "height": 1350})
    for i, (h, css) in enumerate([(front, FCSS), (p2, CSS), (p3, CSS)], 1):
        pg.set_content(f"<html><head><style>{FONTS}{css}</style></head><body style='margin:0'>{h}</body></html>"); pg.wait_for_timeout(600)
        fn = f"{OUT}/paper-page{i}.png"; pg.screenshot(path=fn); print(fn)
    br.close()
