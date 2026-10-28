import base64
from playwright.sync_api import sync_playwright
D='/home/claude/trident-social/tools/.fonts/gf/ofl'
b=lambda p: base64.b64encode(open(D+p,'rb').read()).decode()
F=f"""@font-face{{font-family:'Playfair Display';src:url(data:font/ttf;base64,{b('/playfairdisplay/PlayfairDisplay[wght].ttf')});font-weight:400 900}}
@font-face{{font-family:'Newsreader';src:url(data:font/ttf;base64,{b('/newsreader/Newsreader[opsz,wght].ttf')});font-weight:200 800}}
@font-face{{font-family:'Newsreader';font-style:italic;src:url(data:font/ttf;base64,{b('/newsreader/Newsreader-Italic[opsz,wght].ttf')});font-weight:200 800}}
@font-face{{font-family:'Inter';src:url(data:font/ttf;base64,{b('/inter/Inter[opsz,wght].ttf')});font-weight:100 900}}"""
CSS="""*{margin:0;padding:0;box-sizing:border-box}body{margin:0}
.a{width:1080px;height:1350px;background:#F7F4EC;padding:64px 72px 56px;display:flex;flex-direction:column;font-family:'Inter'}
.rule-heavy{height:9px;background:#0B1235}.rule-thin{height:2px;background:#0B1235;margin-top:5px}
.masthead{font-family:'Playfair Display';font-size:62px;font-weight:900;color:#0B1235;text-align:center;letter-spacing:-.015em;padding:26px 0 20px;line-height:1}
.edition{display:flex;justify-content:space-between;font-size:16px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:#7A7770;padding:14px 0 16px;border-top:2px solid #0B1235;border-bottom:2px solid #0B1235}
.kicker{font-size:22px;font-weight:800;letter-spacing:.26em;text-transform:uppercase;color:#9C7C18;margin:64px 0 30px;display:flex;align-items:center;gap:20px}
.kicker i{flex:1;height:2px;background:#9C7C18;opacity:.4;display:block}
h2{font-family:'Playfair Display';font-size:158px;font-weight:900;line-height:.9;letter-spacing:-.03em;color:#14161A}
h2 em{font-style:normal;color:#9C7C18}
.deck{font-family:'Newsreader';font-style:italic;font-weight:300;font-size:50px;line-height:1.25;color:#3D3D3A;margin-top:40px;max-width:900px}
.bottom{margin-top:auto;display:flex;align-items:stretch;border-top:2px solid rgba(20,22,26,.22);padding-top:40px}
.date{padding-right:44px;border-right:1px solid rgba(20,22,26,.2)}
.date .v{white-space:nowrap;font-variant-numeric:lining-nums;font-family:'Playfair Display';font-size:96px;font-weight:900;color:#0B1235;line-height:.95}
.date .l{font-size:17px;font-weight:800;letter-spacing:.22em;text-transform:uppercase;color:#9C7C18;margin-top:14px}
.act{padding-left:44px;display:flex;flex-direction:column;justify-content:center}
.act .l{font-size:17px;font-weight:800;letter-spacing:.22em;text-transform:uppercase;color:#7A7770}
.act .v{font-family:'Newsreader';font-size:36px;line-height:1.3;color:#14161A;margin-top:10px}
.folio{display:flex;justify-content:space-between;margin-top:44px;padding-top:20px;border-top:6px solid #0B1235;font-size:16px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:#0B1235}
.folio span:last-child{color:#7A7770;font-weight:600}"""
HTML="""<div class="a"><div class="rule-heavy"></div><div class="rule-thin"></div>
<div class="masthead">Trident HR Newsdesk</div>
<div class="edition"><span>28 October 2026</span><span>Employment Rights Act 2025</span><span>No. 22</span></div>
<div class="kicker">Trade Unions <i></i></div>
<h2>New Union<br>Rules <em>Friday</em></h2>
<div class="deck">The rules now apply from the moment a union's application is accepted.</div>
<div class="bottom"><div class="date"><div class="v">30 Oct</div><div class="l">In force</div></div>
<div class="act"><div class="l">Do this now</div><div class="v">Brief your managers before a bid arrives.</div></div></div>
<div class="folio"><span>Trident HR</span><span>tridenthr.co.uk</span></div></div>"""
with sync_playwright() as p:
    br=p.chromium.launch();pg=br.new_page(viewport={'width':1080,'height':1350})
    pg.set_content(f"<html><head><style>{F}{CSS}</style></head><body>{HTML}</body></html>");pg.wait_for_timeout(500)
    pg.screenshot(path='/mnt/user-data/outputs/newsdesk-card-mock.png');br.close()
