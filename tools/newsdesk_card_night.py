import base64
from playwright.sync_api import sync_playwright
D='/home/claude/trident-social/tools/.fonts/gf/ofl'
b=lambda p: base64.b64encode(open(D+p,'rb').read()).decode()
F=f"""@font-face{{font-family:'Playfair Display';src:url(data:font/ttf;base64,{b('/playfairdisplay/PlayfairDisplay[wght].ttf')});font-weight:400 900}}
@font-face{{font-family:'Newsreader';src:url(data:font/ttf;base64,{b('/newsreader/Newsreader[opsz,wght].ttf')});font-weight:200 800}}
@font-face{{font-family:'Newsreader';font-style:italic;src:url(data:font/ttf;base64,{b('/newsreader/Newsreader-Italic[opsz,wght].ttf')});font-weight:200 800}}
@font-face{{font-family:'Inter';src:url(data:font/ttf;base64,{b('/inter/Inter[opsz,wght].ttf')});font-weight:100 900}}"""
CSS="""*{margin:0;padding:0;box-sizing:border-box}body{margin:0}
.b{width:1080px;height:1350px;background:#0B1235;padding:76px 80px 64px;display:flex;flex-direction:column;position:relative;overflow:hidden;font-family:'Inter'}
.mark{position:absolute;right:-150px;top:-40px;height:1000px;opacity:.06}
.top{display:flex;justify-content:space-between;align-items:center;position:relative;padding-bottom:26px;border-bottom:1px solid rgba(212,175,55,.35)}
.top .m{font-size:19px;font-weight:900;letter-spacing:.3em;text-transform:uppercase;color:#D4AF37}
.top .d{font-size:17px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.5)}
.body{margin-top:auto;position:relative}
.cat{font-size:20px;font-weight:800;letter-spacing:.28em;text-transform:uppercase;color:#D4AF37}
h2{font-family:'Playfair Display';font-size:156px;font-weight:800;line-height:.9;letter-spacing:-.032em;color:#F7F4EC;margin-top:34px}
h2 em{font-style:italic;font-weight:500;color:#E8C44A}
.deck{font-family:'Newsreader';font-style:italic;font-weight:300;font-size:44px;line-height:1.3;color:rgba(255,255,255,.72);margin-top:38px;max-width:860px}
.foot{display:flex;justify-content:space-between;align-items:flex-end;margin-top:70px;padding-top:30px;border-top:1px solid rgba(212,175,55,.35);position:relative}
.foot .big{font-family:'Playfair Display';font-size:54px;font-weight:700;color:#D4AF37;line-height:1;font-variant-numeric:lining-nums}
.foot .l{font-size:15px;font-weight:800;letter-spacing:.22em;text-transform:uppercase;color:rgba(212,175,55,.75);margin-top:12px}
.foot .url{font-size:17px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:rgba(255,255,255,.5)}"""
HTML="""<div class="b">
<svg class="mark" viewBox="0 0 215 295"><path fill="#D4AF37" d="M107 0 97 31 80 61 97 61 96 199 58 199 53 196 50 189 31 87 35 85 51 84 0 50 13 96 37 216 97 218 97 280 107 294 117 278 117 218 164 217 178 215 201 99 214 50 195 64 163 85 182 85 184 87 163 194 155 199 117 199 116 62 118 60 134 61 129 55 118 34Z"/></svg>
<div class="top"><span class="m">Trident HR Newsdesk</span><span class="d">28 October 2026</span></div>
<div class="body">
<div class="cat">Trade Unions</div>
<h2>New Union<br>Rules <em>Friday</em></h2>
<div class="deck">The rules now start the moment a union's application is accepted.</div>
</div>
<div class="foot"><div><div class="big">30 October 2026</div><div class="l">In force</div></div><span class="url">tridenthr.co.uk</span></div>
</div>"""
with sync_playwright() as p:
    br=p.chromium.launch();pg=br.new_page(viewport={'width':1080,'height':1350})
    pg.set_content(f"<html><head><style>{F}{CSS}</style></head><body>{HTML}</body></html>");pg.wait_for_timeout(500)
    pg.screenshot(path='/mnt/user-data/outputs/newsdesk-night-v2.png');br.close()
