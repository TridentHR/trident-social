#!/usr/bin/env python3
"""Render Trident HR carousel slides (1080x1350) in the house style.

Usage:
  python3 tools/render.py spec.json OUTPUT_DIR

spec.json:
{
  "slides": [
    {"type": "cover", "kicker": "Employment Rights Act 2025", "big": "4", "unit": "days to go",
     "hook": "Your customers are now your problem."},
    {"type": "cover_text", "kicker": "...", "marker": "In force from today",
     "headline_html": "The rules changed <span style='color:#D4AF37'>this morning.</span>", "sub": "..."},
    {"type": "point", "kicker": "Third-party harassment",
     "title_html": "Clients. Contractors. <span style='color:#b8923a'>The public.</span>",
     "para": "optional paragraph", "bullets": ["optional", "list"]},
    {"type": "cta", "kicker": "Free for employers", "title_html": "Harassment<br>Checklist <span style='color:#D4AF37'>&amp;</span> Policy",
     "body": "One or two sentences.", "button": "Link in bio", "url": "tridenthr.co.uk/harassment-duty"}
  ]
}
Rules: 3 slides is the norm. Navy cover, cream middle, navy CTA. Gold #D4AF37 on navy,
#b8923a on cream. Plain UK English, no emoji. Page numbers are added automatically.

Needs: playwright (Chromium) and git (fonts are fetched once from github.com/google/fonts).
"""
import base64, json, os, subprocess, sys
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, ".fonts")

def ensure_fonts():
    ofl = os.path.join(FONT_DIR, "ofl")
    if os.path.exists(os.path.join(ofl, "cinzel")):
        return ofl
    os.makedirs(FONT_DIR, exist_ok=True)
    subprocess.run(["git", "clone", "--depth", "1", "--filter=blob:none", "--sparse",
                    "https://github.com/google/fonts.git", FONT_DIR + "/gf"], check=True)
    subprocess.run(["git", "-C", FONT_DIR + "/gf", "sparse-checkout", "set",
                    "ofl/cinzel", "ofl/raleway", "ofl/cormorantgaramond"], check=True)
    os.replace(FONT_DIR + "/gf/ofl", ofl)
    return ofl

D = ensure_fonts()
def b64(p): return base64.b64encode(open(p, "rb").read()).decode()
FONTS = f"""
@font-face{{font-family:'Cinzel';src:url(data:font/ttf;base64,{b64(D+'/cinzel/Cinzel[wght].ttf')}) format('truetype');font-weight:400 900}}
@font-face{{font-family:'Cormorant Garamond';src:url(data:font/ttf;base64,{b64(D+'/cormorantgaramond/CormorantGaramond[wght].ttf')}) format('truetype');font-weight:300 700}}
@font-face{{font-family:'Raleway';src:url(data:font/ttf;base64,{b64(D+'/raleway/Raleway[wght].ttf')}) format('truetype');font-weight:100 900}}
"""

TRIDENT = "M107 0 97 31 80 61 97 61 96 199 58 199 53 196 50 189 31 87 35 85 51 84 0 50 13 96 37 216 97 218 97 280 107 294 117 278 117 218 164 217 178 215 201 99 214 50 195 64 163 85 182 85 184 87 163 194 155 199 117 199 116 62 118 60 134 61 129 55 118 34Z"

CSS = FONTS + """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;overflow:hidden}
.s{position:relative;width:1080px;height:1350px;overflow:hidden;padding:110px 100px}
.navy{background:radial-gradient(ellipse 80% 70% at 80% 20%,rgba(212,175,55,.08) 0%,transparent 60%),linear-gradient(180deg,#0a0f1e,#060c1f);color:#fff}
.cream{background:#f4ede0;color:#060c1f}
.label{font-family:'Raleway';font-weight:600;font-size:22px;letter-spacing:.32em;text-transform:uppercase}
.cin{font-family:'Cinzel';font-weight:400;letter-spacing:.03em}
.cor{font-family:'Cormorant Garamond'}
.ral{font-family:'Raleway'}
.mark{position:absolute;pointer-events:none}
.foot{position:absolute;left:100px;right:100px;bottom:80px;display:flex;justify-content:space-between;align-items:center}
.brand{display:flex;align-items:center;gap:16px;font-family:'Raleway';font-weight:700;font-size:20px;letter-spacing:.32em}
.pg{font-family:'Raleway';font-weight:600;font-size:20px;letter-spacing:.2em}
.rule{height:2px;width:200px;background:linear-gradient(90deg,#D4AF37,rgba(212,175,55,0))}
.thr{position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,rgba(212,175,55,.5),transparent)}
.dash{display:flex;align-items:flex-start;gap:28px;font-family:'Raleway';font-weight:400;font-size:38px;line-height:1.4;margin-bottom:30px}
.dash::before{content:'';width:44px;height:2px;background:#b8923a;flex-shrink:0;margin-top:26px}
"""

TOTAL = 3

def logo(color, h=44):
    return f'<svg viewBox="0 0 215 295" height="{h}"><path fill-rule="evenodd" fill="{color}" d="{TRIDENT}"/></svg>'

def foot(dark, n):
    c = "#D4AF37" if dark else "#b8923a"
    t = "rgba(255,255,255,.55)" if dark else "rgba(6,12,31,.5)"
    return f'<div class="foot"><div class="brand" style="color:{c}">{logo(c)}TRIDENT HR</div><div class="pg" style="color:{t}">{n} / {TOTAL}</div></div>'

def slide1(big, unit, hook):
    small = len(big) > 2
    size = "230px" if small else "420px"
    return f'''<div class="s navy">
<svg class="mark" viewBox="0 0 215 295" style="right:-120px;top:120px;height:1250px;opacity:.05"><path fill-rule="evenodd" fill="#D4AF37" d="{TRIDENT}"/></svg>
<div class="label" style="color:#D4AF37">Employment Rights Act 2025</div>
<div class="cin" style="font-size:{size};line-height:1;color:#D4AF37;margin-top:{'90px' if small else '40px'}">{big}</div>
<div class="cor" style="font-size:56px;font-weight:400;color:rgba(255,255,255,.85);margin-top:{'20px' if small else '0'}">{unit}</div>
<div class="rule" style="margin:56px 0 52px"></div>
<div class="cin" style="font-size:66px;line-height:1.18;max-width:860px">{hook}</div>
{foot(True,1)}</div>'''

def slide2(kicker, title, body_html):
    return f'''<div class="s cream">
<div class="thr"></div>
<svg class="mark" viewBox="0 0 215 295" style="right:-160px;bottom:-140px;height:900px"><path fill-rule="evenodd" fill="#e8dfcd" d="{TRIDENT}"/></svg>
<div style="position:relative">
<div class="label" style="color:#b8923a">{kicker}</div>
<div class="cin" style="font-size:64px;line-height:1.18;margin:44px 0 40px;max-width:860px">{title}</div>
<div style="width:60px;height:2px;background:#b8923a;margin-bottom:52px"></div>
{body_html}
</div>
{foot(False,2)}</div>'''

def slide3(extra=""):
    return f'''<div class="s navy" style="display:flex;flex-direction:column;justify-content:center">
<svg class="mark" viewBox="0 0 215 295" style="left:50%;top:50%;transform:translate(-50%,-55%);height:1000px;opacity:.045"><path fill-rule="evenodd" fill="#D4AF37" d="{TRIDENT}"/></svg>
<div style="position:relative;text-align:center">
<div class="label" style="color:#D4AF37">Free for employers</div>
<div class="cin" style="font-size:78px;line-height:1.15;margin:50px 0 46px">Harassment<br>Checklist <span style="color:#D4AF37">&amp;</span> Policy</div>
<div class="ral" style="font-size:34px;font-weight:300;line-height:1.6;color:rgba(255,255,255,.72);max-width:780px;margin:0 auto">A two-page employer checklist and an editable anti-harassment policy, updated for 30 October 2026.{extra}</div>
<div style="display:inline-block;margin-top:70px;padding:30px 64px;border:2px solid #D4AF37;color:#D4AF37" class="label">Link in bio</div>
<div class="ral" style="margin-top:34px;font-size:26px;letter-spacing:.06em;color:rgba(255,255,255,.5)">tridenthr.co.uk/harassment-duty</div>
</div>
{foot(True,3)}</div>'''

def p(t): return f'<div class="ral" style="font-size:40px;font-weight:300;line-height:1.6;color:rgba(6,12,31,.82);max-width:880px">{t}</div>'
def dashes(items): return "".join(f'<div class="dash">{i}</div>' for i in items)


def cover_text(kicker, marker, headline_html, sub):
    return f'''<div class="s navy">
<svg class="mark" viewBox="0 0 215 295" style="right:-120px;top:120px;height:1250px;opacity:.05"><path fill-rule="evenodd" fill="#D4AF37" d="{TRIDENT}"/></svg>
<div class="label" style="color:#D4AF37">{kicker}</div>
<div style="display:flex;align-items:center;gap:22px;margin-top:150px">
  <span style="width:14px;height:14px;border-radius:50%;background:#D4AF37;display:inline-block"></span>
  <span class="label" style="color:rgba(255,255,255,.75)">{marker}</span>
</div>
<div class="cin" style="font-size:96px;line-height:1.12;margin-top:44px;max-width:880px">{headline_html}</div>
<div class="rule" style="margin:60px 0 44px"></div>
<div class="cor" style="font-size:46px;line-height:1.4;color:rgba(255,255,255,.78);max-width:820px">{sub}</div>
{foot(True,1)}</div>'''

def cta(kicker, title_html, body, button, url, n):
    return f'''<div class="s navy" style="display:flex;flex-direction:column;justify-content:center">
<svg class="mark" viewBox="0 0 215 295" style="left:50%;top:50%;transform:translate(-50%,-55%);height:1000px;opacity:.045"><path fill-rule="evenodd" fill="#D4AF37" d="{TRIDENT}"/></svg>
<div style="position:relative;text-align:center">
<div class="label" style="color:#D4AF37">{kicker}</div>
<div class="cin" style="font-size:78px;line-height:1.15;margin:50px 0 46px">{title_html}</div>
<div class="ral" style="font-size:34px;font-weight:300;line-height:1.6;color:rgba(255,255,255,.72);max-width:780px;margin:0 auto">{body}</div>
<div style="display:inline-block;margin-top:70px;padding:30px 64px;border:2px solid #D4AF37;color:#D4AF37" class="label">{button}</div>
<div class="ral" style="margin-top:34px;font-size:26px;letter-spacing:.06em;color:rgba(255,255,255,.5)">{url}</div>
</div>
{foot(True,n)}</div>'''

def build(spec):
    global TOTAL
    slides = spec["slides"]
    TOTAL = len(slides)
    html = []
    for i, s in enumerate(slides, 1):
        t = s["type"]
        if t == "cover":
            h = slide1(s["big"], s["unit"], s["hook"]).replace("Employment Rights Act 2025", s.get("kicker", "Employment Rights Act 2025"))
        elif t == "cover_text":
            h = cover_text(s["kicker"], s["marker"], s["headline_html"], s["sub"])
        elif t == "point":
            body = (p(s["para"]) if s.get("para") else "")
            if s.get("para") and s.get("bullets"):
                body += '<div style="height:36px"></div>'
            body += dashes(s.get("bullets", []))
            h = slide2(s["kicker"], s["title_html"], body).replace(f"{2} / {TOTAL}", f"{i} / {TOTAL}")
        elif t == "cta":
            h = cta(s["kicker"], s["title_html"], s["body"], s.get("button", "Link in bio"), s.get("url", "tridenthr.co.uk"), i)
        else:
            raise SystemExit(f"Unknown slide type: {t}")
        html.append(h)
    return html

def main():
    spec = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    os.makedirs(out, exist_ok=True)
    pages = build(spec)
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for i, h in enumerate(pages, 1):
            pg.set_content(f"<html><head><style>{CSS}</style></head><body>{h}</body></html>")
            pg.wait_for_timeout(300)
            pg.screenshot(path=os.path.join(out, f"slide{i}.png"))
        b.close()
    print("\n".join(os.path.join(out, f"slide{i}.png") for i in range(1, len(pages) + 1)))

if __name__ == "__main__":
    main()
