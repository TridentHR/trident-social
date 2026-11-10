import base64, os
from playwright.sync_api import sync_playwright

S = "/tmp/claude-0/-home-claude/1d4e6e69-d7be-54bc-81c0-1f17dec24709/scratchpad"
D = "/home/claude/tridenthr/trident-social/tools/.fonts/gf/ofl"
OUT = S + "/inside"; os.makedirs(OUT, exist_ok=True)
def ff(name, path, style="normal", w="100 900"):
    b = base64.b64encode(open(D + path, "rb").read()).decode()
    return f"@font-face{{font-family:'{name}';font-style:{style};font-weight:{w};src:url(data:font/ttf;base64,{b})}}"
FONTS = "".join([ff("Inter", "/inter/Inter[opsz,wght].ttf"), ff("Fraktur", "/unifrakturmaguntia/UnifrakturMaguntia-Book.ttf"),
    ff("Caslon", "/librecaslontext/LibreCaslonText[wght].ttf"), ff("Caslon", "/librecaslontext/LibreCaslonText-Italic[wght].ttf", "italic")])
POPPY = open(S + "/poppy.svg").read().replace("width:76px;height:70px;left:2px;top:-2px", "width:34px;height:31px;left:0px;top:-2px")

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
.dy{margin-top:18px;border:2px solid #0B1235}
.dy .hd{background:#0B1235;color:#fff;font-family:Inter;font-size:14px;font-weight:800;letter-spacing:.18em;padding:9px 16px}
.dy .bd{padding:14px 16px 16px}
.dy b{display:block;font-family:Caslon;font-weight:700;font-size:48px;line-height:1;color:#0B1235}
.dy .y{font-family:Inter;font-size:13px;font-weight:800;letter-spacing:.16em;color:#666;margin-top:6px}
.dy .t{font-family:Caslon;font-size:20px;line-height:1.35;color:#222;margin-top:8px}
.ft{display:flex;justify-content:space-between;border-top:3px solid #111;padding-top:12px;margin-top:20px;font-family:Inter;font-size:15px;font-weight:700;letter-spacing:.16em}
/* diary */
.dl{margin-top:0}
.dr{display:flex;gap:34px;padding:26px 0;border-bottom:1px solid #111;align-items:flex-start}
.dr .dt{width:250px;flex-shrink:0}
.dr .dt b{display:block;font-family:Caslon;font-weight:700;font-size:72px;line-height:.95;color:#0B1235}
.dr .dt span{display:block;text-transform:uppercase;font-family:Inter;font-size:14px;font-weight:800;letter-spacing:.16em;color:#666;margin-top:8px}
.dr .tx .k{font-family:Inter;font-size:13px;font-weight:800;letter-spacing:.18em;color:#666}
.dr .tx h3{font-family:Caslon;font-weight:700;font-size:40px;line-height:1.1;color:#111;margin-top:6px}
.dr .tx p{font-family:Caslon;font-size:25px;line-height:1.45;color:#333;margin-top:8px}
"""

def head(n):
    return f'''<div class="run"><span class="n">{n}</span><span class="m">Trident HR Newsdes<span style="position:relative;display:inline-block">k{POPPY}</span></span><span class="d up">11 Nov 2026</span></div><div class="rule2"></div>'''

def foot(n, total, last=False):
    return f'<div class="ft up"><span>tridenthr.co.uk</span><span>{"Full stories: link in bio" if last else f"Page {n} of {total}"}</span></div>'

TOTAL = 6

def diary(d, y, t):
    return f'<div class="dy"><div class="hd up">Dates for the diary</div><div class="bd"><b>{d}</b><div class="y up">{y}</div><div class="t">{t}</div></div></div>'

def story(n, sec, h, deck, c1, pull, src, c2, acts, dy=''):
    return f'''<div class="pg">{head(n)}
<div><span class="sec up">{sec}</span></div>
<h1>{h}</h1><div class="deck">{deck}</div>
<div class="body"><div class="col dc">{c1}</div><div class="vr"></div>
<div class="col"><div class="pull"><q>{pull}</q><span class="up">{src}</span></div>{c2}</div><div class="vr"></div>
<div class="col"><div class="box"><div class="h up">Do this now</div><ol>{"".join(f"<li>{a}</li>" for a in acts)}</ol></div>{dy}</div></div>
{foot(n, TOTAL)}</div>'''

RATES = [("21 and over","£13.21","up 50p"),("18 to 20","£11.27","up 42p"),("16 to 17","£8.31","up 31p"),("Apprentice","£8.31","up 31p")]
pNLW = f'''<div class="pg">{head(2)}
<div><span class="sec up">Pay &amp; Payroll</span></div>
<h1>Living Wage rises to £13.21 from 1 April</h1><div class="deck">Every minimum wage rate rises 3.9%. You have five months to budget.</div>
<div class="body"><div class="col dc"><p>The government has accepted the Low Pay Commission's recommendations in full. They were announced at the Autumn Budget on 28 October.</p><p>From 1 April 2027 the National Living Wage for workers aged 21 and over rises by 50p to £13.21 an hour. Every other rate rises by the same 3.9%.</p><h4>Age bands</h4><p>The plan to bring the 18 to 20 rate up to the full rate is paused for 2027, so it rises by the same percentage.</p></div><div class="vr"></div>
<div class="col"><div class="pull"><q>You have five months to budget, check your pay structures and update contracts.</q><span class="up">The deadline</span></div><h4>Who it affects</h4><p>Any employer with staff paid at or near the minimum, especially hospitality, retail, care, cleaning, warehousing and childcare.</p><p>Salaried staff count too. Check their pay against hours actually worked.</p></div><div class="vr"></div>
<div class="col"><div class="box"><div class="h up">New hourly rates</div><table style="width:100%;border-collapse:collapse;margin-top:6px;font-family:Caslon;font-size:21px">{"".join(f'<tr style="border-bottom:1px solid #ccc"><td style="padding:9px 0">{a}</td><td style="padding:9px 0;text-align:right;font-weight:700;color:#0B1235">{b}</td></tr>' for a,b,c in RATES)}</table></div>
<div class="box" style="margin-top:18px"><div class="h up">Do this now</div><ol><li>Build the new rates into your 2027/28 budget.</li><li>Check salaried and apprentice pay against hours worked.</li><li>Confirm your payroll provider will apply them from 1 April.</li></ol></div></div></div>
{foot(2, TOTAL)}</div>'''

p2 = story(3, "Harassment", "EHRC refreshes its harassment guidance",
 "The guidance has caught up with the duties in force since 30 October. Christmas parties are weeks away.",
 "<p>The Equality and Human Rights Commission has refreshed its technical guidance on harassment at work and its shorter 8-step guide for employers. The update was announced on 2 November.</p><p>It reflects the stronger duties that came into force on 30 October under the Employment Rights Act 2025.</p><h4>All reasonable steps</h4><p>Employers must now take all reasonable steps to prevent sexual harassment of their staff, up from reasonable steps.</p>",
 "Missing one reasonable step can be enough to breach the duty.", "The new standard",
 "<h4>Third parties</h4><p>You are also liable if a customer, client, contractor or member of the public harasses one of your staff at work, unless you took all reasonable steps to prevent it.</p><p>The burden is on you to show what you did.</p>",
 ["Review your risk assessment against the new guidance.", "Update your policy to cover third parties.", "Brief staff before the Christmas party.", "Check training for customer-facing staff."])

p3 = story(4, "Fire &amp; Rehire", "Shift and expenses changes to be restricted",
 "Forcing new shift patterns or cutting expenses may soon be automatically unfair.",
 "<p>On 22 October the government published its response to the fire and rehire consultation. It confirms which changes to shifts, expenses and benefits will count as restricted variations.</p><h4>What changes</h4><p>Requiring an employee to work nights, 11pm to 6am, when they did not before, or days when they did not before, will be a restricted variation.</p>",
 "Dismissing someone for refusing one of these changes may be automatically unfair.", "The new protection",
 "<h4>When</h4><p>The government aims for the rules to start in March 2027, alongside the wider fire and rehire protections.</p><p>A revised Code of Practice on dismissal and re-engagement is out for consultation until 17 December.</p>",
 ["Check how contracts describe shifts and days.", "Confirm whether travel and mileage are contractual.", "Consult on 2027 rota changes before March."])

pSC = story(5, "Scotland", "Six months to bring a contract claim",
 "From 9 November, employees in Scotland have six months, not three, to bring a breach of contract claim.",
 "<p>The Employment Tribunals Extension of Jurisdiction (Amendment) (Scotland) Order 2026 doubles the time limit for contract claims in Scottish employment tribunals.</p><p>It brings Scotland back into line with England and Wales, where the same change took effect on 1 October.</p><h4>What it covers</h4><p>Claims for breach of contract, or sums due under it, outstanding when employment ends. For example notice pay, bonus or commission.</p>",
 "Scottish leavers now have six months to claim unpaid notice pay or bonus.", "The change",
 "<h4>Who it applies to</h4><p>Anyone whose employment ends on or after 9 November 2026.</p><p>If employment ended between 1 October and 8 November, Scottish contract claims still have three months.</p>",
 ["Check final pay, notice pay, bonus and commission for leavers.", "Keep leaver pay records for at least six months.", "Update guidance that still quotes three months."])

DIARY = [("Now", "", "Harassment", "Brief staff before party season", "Set out expected behaviour at work events and how to report concerns."),
 ("17 Dec", "2026", "Fire &amp; Rehire", "Code consultation closes", "Last day to comment on the revised Code of Practice on dismissal and re-engagement."),
 ("March", "2027 (expected)", "Fire &amp; Rehire", "New rules expected", "The government aims to bring in the shift, expenses and benefits rules in March 2027. Consult on any rota changes before then."),
 ("1 Apr", "2027", "Pay &amp; Payroll", "New minimum wage rates", "National Living Wage rises to £13.21. Update payroll from this pay period.")]
p5 = f'''<div class="pg">{head(6)}
<h1 style="margin-top:34px;padding-bottom:22px;border-bottom:3px solid #111">Dates for the diary</h1>
<div class="dl" style="flex:1;display:flex;flex-direction:column;justify-content:space-evenly">{"".join(f'<div class="dr"><div class="dt"><b>{d}</b><span>{y}</span></div><div class="tx"><div class="k up">{k}</div><h3>{h}</h3><p>{t}</p></div></div>' for d,y,k,h,t in DIARY)}</div>
{foot(6, TOTAL, True)}</div>'''

with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page(viewport={"width": 1080, "height": 1350})
    for i, h in enumerate([pNLW, p2, p3, pSC, p5], 2):
        pg.set_content(f"<html><head><style>{FONTS}{CSS}</style></head><body style='margin:0'>{h}</body></html>"); pg.wait_for_timeout(500)
        pg.screenshot(path=f"{OUT}/page{i}.png"); print(f"{OUT}/page{i}.png")
    br.close()
