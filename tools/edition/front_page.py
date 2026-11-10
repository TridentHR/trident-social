import base64, os
from playwright.sync_api import sync_playwright

D = "/home/claude/tridenthr/trident-social/tools/.fonts/gf/ofl"
OUT = "/tmp/claude-0/-home-claude/1d4e6e69-d7be-54bc-81c0-1f17dec24709/scratchpad/fronts"
IMG = base64.b64encode(open("/tmp/claude-0/-home-claude/1d4e6e69-d7be-54bc-81c0-1f17dec24709/scratchpad/till.jpg","rb").read()).decode()
os.makedirs(OUT, exist_ok=True)
def ff(name, path, style="normal", w="100 900"):
    b = base64.b64encode(open(D + path, "rb").read()).decode()
    return f"@font-face{{font-family:'{name}';font-style:{style};font-weight:{w};src:url(data:font/ttf;base64,{b})}}"
FONTS = "".join([
    ff("Playfair", "/playfairdisplay/PlayfairDisplay[wght].ttf"),
    ff("Newsreader", "/newsreader/Newsreader[opsz,wght].ttf"),
    ff("Newsreader", "/newsreader/Newsreader-Italic[opsz,wght].ttf", "italic"),
    ff("Inter", "/inter/Inter[opsz,wght].ttf"),
    ff("Oswald", "/oswald/Oswald[wght].ttf"),
    ff("Anton", "/anton/Anton-Regular.ttf"),
    ff("Fraktur", "/unifrakturmaguntia/UnifrakturMaguntia-Book.ttf"),
    ff("Jacq", "/jacquard24/Jacquard24-Regular.ttf"),
    ff("Eagle", "/eaglelake/EagleLake-Regular.ttf"),
    ff("Caslon", "/librecaslontext/LibreCaslonText[wght].ttf"),
    ff("Caslon", "/librecaslontext/LibreCaslonText-Italic[wght].ttf", "italic"),
    ff("DMSerif", "/dmserifdisplay/DMSerifDisplay-Regular.ttf"),
    ff("DMSerif", "/dmserifdisplay/DMSerifDisplay-Italic.ttf", "italic"),
    ff("SSerif", "/sourceserif4/SourceSerif4[opsz,wght].ttf"),
    ff("SSerif", "/sourceserif4/SourceSerif4-Italic[opsz,wght].ttf", "italic"),
])
BASE = "*{margin:0;padding:0;box-sizing:border-box;font-feature-settings:'dlig' 0,'hlig' 0,'hist' 0}body{margin:0;font-variant-numeric:lining-nums}.pg{width:1080px;height:1350px;overflow:hidden;display:flex;flex-direction:column}.up{text-transform:uppercase}"

L_K = "Pay &amp; Payroll"
L_D = "Every minimum wage rate rises 3.9% on 1 April 2027. Employers have five months to budget."
L_B1 = "The government has accepted the Low Pay Commission's recommendations in full. From 1 April 2027 the National Living Wage for workers aged 21 and over rises by 50p to £13.21 an hour."
L_B2 = "The 18 to 20 rate goes to £11.27. The 16 to 17 and apprentice rates go to £8.31. Salaried staff count too, so check pay against hours actually worked."
S2 = ("Harassment", "Harassment guidance refreshed", "The EHRC has updated its guidance for the duties in force since 30 October. You can now be liable when customers or contractors harass your staff.", "1 Dec", "Brief staff before party season")
S3 = ("Fire &amp; Rehire", "Shift changes to be restricted", "Moving staff onto nights or days without agreement may soon be automatically unfair. The rules are due in March 2027.", "17 Dec", "Code consultation closes")
DIARY = [("1 Apr", "New minimum wage rates in force"), ("1 Dec", "Brief staff before party season"), ("17 Dec", "Fire and rehire Code consultation closes")]

# 1 Broadsheet: white paper, blackletter nameplate, Caslon
m1 = f"""<style>{BASE}
.pg{{background:#FFFFFF;padding:52px 60px 44px;color:#111}}
.np{{display:flex;align-items:center;gap:24px;padding-bottom:14px}}
.ear{{width:140px;border:1.5px solid #111;padding:10px 12px;font-family:Inter;font-size:14px;font-weight:700;letter-spacing:.12em;line-height:1.35;text-align:center}}
.ear b{{display:block;font-family:Caslon;font-size:22px;letter-spacing:0;font-weight:700;color:#0B1235}}
.name{{flex:1;text-align:center;font-family:Fraktur;font-size:84px;color:#0B1235;line-height:1;white-space:nowrap}}
.dl{{display:flex;justify-content:space-between;border-top:3px solid #111;border-bottom:1px solid #111;padding:9px 0;font-family:Inter;font-size:15px;font-weight:600;letter-spacing:.14em}}
h1{{font-family:Caslon;font-weight:700;font-size:88px;line-height:.98;letter-spacing:-.02em;margin-top:30px;color:#0B1235}}
.deck{{font-family:Caslon;font-style:italic;font-size:34px;line-height:1.3;margin-top:18px;color:#333}}
.grid{{display:flex;gap:30px;margin-top:28px;border-top:1px solid #111;padding-top:24px;flex:1}}
.lead{{flex:2;display:flex;gap:26px}}
.lead p{{flex:1;font-family:Caslon;font-size:24px;line-height:1.5;color:#222}}
.lead p:first-child::first-letter{{font-family:Caslon;font-weight:700;font-size:78px;float:left;line-height:.8;margin:6px 10px 0 0;color:#0B1235}}
.vr{{width:1px;background:#111}}
.lead2{{flex:2;display:flex;flex-direction:column}}
.lead2 img{{width:100%;height:290px;object-fit:cover;object-position:55% 35%;display:block}}
.cap{{font-variant-ligatures:none;font-feature-settings:'liga' 0,'dlig' 0;font-family:Caslon;font-style:italic;font-size:17px;color:#555;margin-top:8px;padding-bottom:14px;border-bottom:1px solid #111}}
.lc{{column-count:2;column-gap:26px;column-fill:balance;margin-top:16px}}
.scot{{margin-top:auto;display:flex;align-items:center;gap:16px;border-top:3px solid #0B1235;padding:12px 0 0;font-family:Caslon;font-weight:700;font-size:23px;color:#111}}
.scot b{{font-family:Inter;font-size:14px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:#fff;background:#0B1235;padding:6px 10px}}
.scot span{{margin-left:auto;white-space:nowrap;font-family:Inter;font-size:13px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:#666}}
.lc p{{font-family:Caslon;font-size:21px;line-height:1.45;color:#222}}
.lc p:first-child::first-letter{{font-family:Caslon;font-weight:700;font-size:66px;float:left;line-height:.8;margin:5px 9px 0 0;color:#0B1235}}
.side{{flex:1;display:flex;flex-direction:column}}
.st+.st{{border-top:1px solid #111;margin-top:20px;padding-top:20px}}
.st .k{{font-family:Inter;font-size:13px;font-weight:800;letter-spacing:.2em;color:#0B1235}}
.st h3{{font-family:Caslon;font-weight:700;font-size:36px;line-height:1.08;margin-top:8px}}
.st p{{font-family:Caslon;font-size:22px;line-height:1.45;margin-top:10px;color:#333}}
.st .dt{{font-family:Inter;font-size:14px;font-weight:800;letter-spacing:.12em;margin-top:12px;color:#0B1235}}
.ft{{display:flex;justify-content:space-between;border-top:3px solid #111;padding-top:12px;margin-top:22px;font-family:Inter;font-size:15px;font-weight:700;letter-spacing:.16em}}
</style><div class="pg">
<div class="np"><div class="name">Trident HR Newsdes<span style="position:relative;display:inline-block">k<svg viewBox="0 0 120 110" style="position:absolute;width:76px;height:70px;left:2px;top:-2px"><path d="M44 104 C14 100 0 76 6 50 C32 56 50 78 44 104Z" fill="#2F5D3A"/><path d="M44 104 C34 86 20 66 6 50" stroke="#1F4228" stroke-width="2.4" fill="none"/><circle cx="50" cy="38" r="22" fill="#C8102E"/><circle cx="82" cy="38" r="22" fill="#C8102E"/><circle cx="52" cy="62" r="21" fill="#B00D27"/><circle cx="80" cy="62" r="21" fill="#B00D27"/><circle cx="66" cy="50" r="10" fill="#111"/><circle cx="63" cy="47" r="1.6" fill="#555"/><circle cx="69" cy="48" r="1.6" fill="#555"/><circle cx="66" cy="53" r="1.6" fill="#555"/></svg></span></div></div>
<div class="dl up"><span>Wednesday 11 November 2026</span><span>UK employment news</span><span>Edition No. 23</span></div>
<h1>Living Wage hits £13.21 from April</h1>
<div class="deck">{L_D}</div>
<div class="grid"><div class="lead2"><img src="data:image/jpeg;base64,{IMG}"><div class="cap">Hospitality and retail staff are among those most affected by the April rise.</div><div class="lc"><p>{L_B1} {L_B2}</p></div><div class="scot"><b>Scotland</b>Six months to bring a contract claim<span>Page 5</span></div></div><div class="vr"></div>
<div class="side">{''.join(f'<div class="st"><div class="k up">{s[0]}</div><h3>{s[1]}</h3><p>{s[2]}</p></div>' for s in (S2,S3))}</div></div>
<div class="ft up"><span>tridenthr.co.uk</span><span>Full stories: link in bio</span></div></div>"""

# 2 Tabloid: Anton, navy masthead band, huge number
m2 = f"""<style>{BASE}
.pg{{background:#FFFFFF;color:#0B1235}}
.band{{background:#0B1235;padding:30px 56px 26px;display:flex;justify-content:space-between;align-items:flex-end}}
.band .n{{font-family:Anton;font-size:118px;line-height:.85;color:#FFFFFF;letter-spacing:.01em}}
.band .s{{font-family:Oswald;font-weight:500;font-size:20px;letter-spacing:.18em;color:#D4AF37;text-align:right;line-height:1.5}}
.bar{{display:flex;justify-content:space-between;padding:12px 56px;border-bottom:4px solid #0B1235;font-family:Oswald;font-weight:600;font-size:19px;letter-spacing:.14em}}
.body{{padding:28px 56px 40px;flex:1;display:flex;flex-direction:column}}
.big{{font-family:Anton;font-size:340px;line-height:.86;letter-spacing:-.01em}}
h1{{font-family:Anton;font-size:84px;line-height:.98;margin-top:10px;text-transform:uppercase}}
.ld{{font-family:Newsreader;font-size:32px;line-height:1.4;margin-top:20px;color:#222;max-width:940px}}
.two{{display:flex;gap:0;margin-top:auto;border-top:4px solid #0B1235}}
.two .c{{flex:1;padding:22px 28px 0 0}}
.two .c+.c{{padding:22px 0 0 28px;border-left:2px solid #0B1235}}
.two .k{{font-family:Oswald;font-weight:700;font-size:18px;letter-spacing:.18em;color:#7A7770}}
.two h3{{font-family:Anton;font-size:46px;line-height:1;margin-top:8px;text-transform:uppercase}}
.two p{{font-family:Newsreader;font-size:23px;line-height:1.42;margin-top:12px;color:#222}}
.two .d{{font-family:Oswald;font-weight:700;font-size:19px;letter-spacing:.1em;margin-top:12px}}
.ft{{display:flex;justify-content:space-between;margin-top:26px;font-family:Oswald;font-weight:600;font-size:18px;letter-spacing:.16em;color:#7A7770}}
</style><div class="pg">
<div class="band"><div class="n up">Newsdesk</div><div class="s up">Trident HR<br>No. 23 &middot; 10 Nov 2026</div></div>
<div class="bar up"><span>Three changes every UK employer needs</span><span>Free</span></div>
<div class="body"><div class="kick" style="font-family:Oswald;font-weight:700;font-size:20px;letter-spacing:.2em;color:#7A7770" class="up">PAY &amp; PAYROLL</div>
<div class="big">£13.21</div><h1>Living Wage rise confirmed</h1>
<div class="ld">Every minimum wage rate rises 3.9% on 1 April 2027. The 18 to 20 rate goes to £11.27, and the 16 to 17 and apprentice rates to £8.31.</div><div style="font-family:Oswald;font-weight:700;font-size:24px;letter-spacing:.12em;margin-top:18px">DO THIS NOW: BUILD THE NEW RATES INTO YOUR 2027/28 BUDGET</div>
<div class="two">{''.join(f'<div class="c"><div class="k up">{s[0]}</div><h3>{s[1]}</h3><p>{s[2]}</p><div class="d up">{s[3]}: {s[4]}</div></div>' for s in (S2,S3))}</div>
<div class="ft up"><span>Trident HR</span><span>Full stories: link in bio</span></div></div></div>"""

# 3 Night broadsheet: navy ground, DM Serif, gold rules
m3 = f"""<style>{BASE}
.pg{{background:#0B1235;padding:56px 64px 46px;color:#F2EEE3}}
.tr{{height:2px;background:#D4AF37}}.tr2{{height:1px;background:#D4AF37;margin-top:5px}}
.name{{font-family:DMSerif;font-size:86px;text-align:center;line-height:1;padding:22px 0 16px;letter-spacing:-.01em}}
.dl{{display:flex;justify-content:space-between;border-top:1px solid rgba(212,175,55,.6);border-bottom:1px solid rgba(212,175,55,.6);padding:11px 0;font-family:Inter;font-size:15px;font-weight:700;letter-spacing:.18em;color:rgba(242,238,227,.6)}}
.k{{font-family:Inter;font-size:15px;font-weight:800;letter-spacing:.24em;color:#D4AF37}}
h1{{font-family:DMSerif;font-size:124px;line-height:.95;margin-top:14px;letter-spacing:-.015em}}
h1 em{{color:#D4AF37}}
.deck{{font-family:Newsreader;font-style:italic;font-weight:300;font-size:34px;line-height:1.32;margin-top:18px;color:rgba(242,238,227,.75)}}
.cols{{display:flex;gap:32px;margin-top:26px}}
.cols p{{flex:1;font-family:Newsreader;font-size:27px;line-height:1.5;color:rgba(242,238,227,.85)}}
.vr{{width:1px;background:rgba(212,175,55,.4)}}
.row{{display:flex;gap:32px;margin-top:auto;border-top:1px solid rgba(212,175,55,.6);padding-top:24px}}
.row .c{{flex:1}}
.row h3{{font-family:DMSerif;font-size:40px;line-height:1.05;margin-top:8px}}
.row p{{font-family:Newsreader;font-size:22px;line-height:1.45;margin-top:10px;color:rgba(242,238,227,.78)}}
.row .d{{font-family:Inter;font-size:14px;font-weight:800;letter-spacing:.14em;margin-top:12px;color:#D4AF37}}
.ft{{display:flex;justify-content:space-between;margin-top:24px;padding-top:14px;border-top:2px solid #D4AF37;font-family:Inter;font-size:15px;font-weight:700;letter-spacing:.18em}}
.ft span:last-child{{color:rgba(242,238,227,.5)}}
</style><div class="pg"><div class="tr"></div><div class="tr2"></div>
<div class="name">Trident HR Newsdesk</div>
<div class="dl up"><span>10 November 2026</span><span>UK employment news</span><span>No. 23</span></div>
<div style="margin-top:34px" class="k up">{L_K}</div>
<h1>Living Wage hits <em>£13.21</em></h1>
<div class="deck">{L_D}</div>
<div class="cols"><p>{L_B1}</p><div class="vr"></div><p>{L_B2} <span style="color:#D4AF37;font-weight:600">Do this now:</span> build the new rates into your 2027/28 budget.</p></div>
<div class="row">{''.join(f'<div class="c"><div class="k up">{s[0]}</div><h3>{s[1]}</h3><p>{s[2]}</p><div class="d up">{s[3]} &middot; {s[4]}</div></div>' for s in (S2,S3))}</div>
<div class="ft up"><span style="color:#D4AF37">Trident HR</span><span>Full stories: link in bio</span></div></div>"""

# 4 Modern editorial: cool grey paper, Source Serif, sidebar + diary strip
m4 = f"""<style>{BASE}
.pg{{background:#F3F4F6;padding:0 0 40px;color:#14161A}}
.top{{background:#0B1235;padding:26px 60px;display:flex;justify-content:space-between;align-items:center}}
.top .n{{font-family:SSerif;font-weight:700;font-size:46px;color:#FFFFFF;letter-spacing:-.01em}}
.top .n span{{color:#D4AF37}}
.top .e{{font-family:Inter;font-size:15px;font-weight:700;letter-spacing:.16em;color:rgba(255,255,255,.6);text-align:right;line-height:1.5}}
.in{{padding:0 60px;flex:1;display:flex;flex-direction:column}}
.main{{display:flex;gap:40px;margin-top:52px}}
.lead{{flex:1.7}}
.k{{font-family:Inter;font-size:15px;font-weight:800;letter-spacing:.2em;color:#0B1235;padding-bottom:10px;border-bottom:3px solid #0B1235;display:inline-block}}
h1{{font-family:SSerif;font-weight:800;font-size:116px;line-height:.98;letter-spacing:-.025em;margin-top:22px;color:#0B1235}}
.deck{{font-family:SSerif;font-style:italic;font-size:31px;line-height:1.32;margin-top:18px;color:#3A3D44}}
.lead p{{font-family:SSerif;font-size:23px;line-height:1.55;margin-top:18px;color:#2A2D33}}
.side{{flex:1;border-left:1px solid #C9CDD4;padding-left:34px}}
.side .h{{font-family:Inter;font-size:15px;font-weight:800;letter-spacing:.2em;color:#7A7F88}}
.st{{padding:20px 0;border-bottom:1px solid #C9CDD4;display:flex;gap:16px}}
.st .num{{font-family:SSerif;font-weight:800;font-size:54px;line-height:.85;color:#0B1235}}
.st .sk{{font-family:Inter;font-size:13px;font-weight:800;letter-spacing:.18em;color:#7A7F88}}
.st h3{{font-family:SSerif;font-weight:700;font-size:34px;line-height:1.1;margin-top:6px;color:#0B1235}}
.st p{{font-family:SSerif;font-size:22px;line-height:1.45;margin-top:8px;color:#3A3D44}}
.diary{{margin-top:auto;display:flex;background:#FFFFFF;border-top:4px solid #0B1235}}
.diary .h{{writing-mode:vertical-rl;transform:rotate(180deg);background:#0B1235;color:#FFFFFF;font-family:Inter;font-size:13px;font-weight:800;letter-spacing:.24em;padding:14px 10px;text-align:center}}
.diary .c{{flex:1;padding:20px 24px}}
.diary .c+.c{{border-left:1px solid #C9CDD4}}
.diary .v{{font-family:SSerif;font-weight:800;font-size:44px;color:#0B1235;line-height:1}}
.diary .t{{font-family:SSerif;font-size:19px;line-height:1.35;margin-top:8px;color:#3A3D44}}
.ft{{display:flex;justify-content:space-between;margin-top:22px;font-family:Inter;font-size:15px;font-weight:700;letter-spacing:.16em;color:#7A7F88}}
</style><div class="pg">
<div class="top"><div class="n">Trident HR <span>Newsdesk</span></div><div class="e up">No. 23<br>10 November 2026</div></div>
<div class="in"><div class="main"><div class="lead"><div class="k up">{L_K}</div>
<h1>Living Wage hits £13.21</h1><div class="deck">{L_D}</div><p>{L_B1}</p><p>{L_B2}</p><div style="margin-top:22px;border-left:4px solid #0B1235;padding:6px 0 6px 18px;font-family:SSerif;font-weight:700;font-size:25px;color:#0B1235">Do this now: build the new rates into your 2027/28 budget.</div></div>
<div class="side"><div class="h up">Also this week</div>
{''.join(f'<div class="st"><div class="num">{i}</div><div><div class="sk up">{s[0]}</div><h3>{s[1]}</h3><p>{s[2]}</p></div></div>' for i,s in ((2,S2),(3,S3)))}</div></div>
<div style="height:30px"></div>
<div class="diary"><div class="h up">Diary</div>{''.join(f'<div class="c"><div class="v">{d}</div><div class="t">{t}</div></div>' for d,t in DIARY)}</div>
<div class="ft up"><span>Trident HR &middot; tridenthr.co.uk</span><span>Full stories: link in bio</span></div></div></div>"""

# 5 Classic big-number: white, Playfair, giant figure
m5 = f"""<style>{BASE}
.pg{{background:#FFFFFF;padding:56px 64px 46px;color:#0B1235}}
.r1{{height:8px;background:#0B1235}}.r2{{height:2px;background:#0B1235;margin-top:5px}}
.name{{font-family:Playfair;font-weight:900;font-size:76px;text-align:center;line-height:1;padding:22px 0 18px;letter-spacing:-.015em}}
.dl{{display:flex;justify-content:space-between;border-top:2px solid #0B1235;border-bottom:2px solid #0B1235;padding:11px 0;font-family:Inter;font-size:15px;font-weight:700;letter-spacing:.18em;color:#6B6F78}}
.hero{{display:flex;align-items:flex-end;gap:34px;margin-top:30px}}
.fig{{font-family:Playfair;font-weight:900;font-size:230px;line-height:.8;letter-spacing:-.04em}}
.hero .t{{padding-bottom:14px}}
.hero .k{{font-family:Inter;font-size:15px;font-weight:800;letter-spacing:.22em;color:#C9A227}}
.hero h1{{font-family:Playfair;font-weight:800;font-size:44px;line-height:1.05;margin-top:10px;color:#14161A}}
.deck{{font-family:Newsreader;font-size:30px;line-height:1.5;margin-top:34px;color:#33363D;columns:2;column-gap:40px;column-rule:1px solid #D5D7DC}}
.row{{display:flex;margin-top:auto;border-top:2px solid #0B1235}}
.row .c{{flex:1;padding:22px 28px 0 0}}
.row .c+.c{{padding-left:28px;border-left:1px solid #D5D7DC}}
.row .k{{font-family:Inter;font-size:14px;font-weight:800;letter-spacing:.2em;color:#C9A227}}
.row h3{{font-family:Playfair;font-weight:800;font-size:38px;line-height:1.05;margin-top:8px;color:#14161A}}
.row p{{font-family:Newsreader;font-size:22px;line-height:1.45;margin-top:10px;color:#33363D}}
.row .d{{display:inline-block;margin-top:14px;border:2px solid #0B1235;padding:6px 12px;font-family:Inter;font-size:14px;font-weight:800;letter-spacing:.12em}}
.ft{{display:flex;justify-content:space-between;margin-top:26px;padding-top:14px;border-top:6px solid #0B1235;font-family:Inter;font-size:15px;font-weight:800;letter-spacing:.18em}}
.ft span:last-child{{color:#6B6F78;font-weight:600}}
</style><div class="pg"><div class="r1"></div><div class="r2"></div>
<div class="name">Trident HR Newsdesk</div>
<div class="dl up"><span>10 November 2026</span><span>Three stories this edition</span><span>No. 23</span></div>
<div class="hero"><div class="fig">£13.21</div><div class="t"><div class="k up">{L_K}</div><h1>New Living Wage from April</h1></div></div>
<div class="deck">{L_B1} {L_B2} <b style="color:#0B1235">Do this now:</b> build the new rates into your 2027/28 budget.</div>
<div class="row">{''.join(f'<div class="c"><div class="k up">{s[0]}</div><h3>{s[1]}</h3><p>{s[2]}</p><div class="d up">Diary &middot; {s[3]}</div></div>' for s in (S2,S3))}</div>
<div class="ft up"><span>Trident HR</span><span>Full stories: link in bio</span></div></div>"""

with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page(viewport={"width": 1080, "height": 1350})
    for i, h in enumerate([m1, m2, m3, m4, m5], 1):
        pg.set_content(f"<html><head><style>{FONTS}</style></head><body>{h}</body></html>"); pg.wait_for_timeout(500)
        pg.screenshot(path=f"{OUT}/front{i}.png"); print(f"{OUT}/front{i}.png")
    br.close()
