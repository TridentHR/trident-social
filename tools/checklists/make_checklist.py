import base64, json, os, sys, html
from datetime import date
from playwright.sync_api import sync_playwright

FONT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".fonts", "ofl")
TRIDENT = "M107 0 97 31 80 61 97 61 96 199 58 199 53 196 50 189 31 87 35 85 51 84 0 50 13 96 37 216 97 218 97 280 107 294 117 278 117 218 164 217 178 215 201 99 214 50 195 64 163 85 182 85 184 87 163 194 155 199 117 199 116 62 118 60 134 61 129 55 118 34Z"


def b64(p):
    return base64.b64encode(open(p, "rb").read()).decode()


FONTS = f"""
@font-face{{font-family:'Cormorant';src:url(data:font/ttf;base64,{b64(FONT_DIR + '/cormorantgaramond/CormorantGaramond[wght].ttf')});font-weight:300 700}}
@font-face{{font-family:'Cormorant';font-style:italic;src:url(data:font/ttf;base64,{b64(FONT_DIR + '/cormorantgaramond/CormorantGaramond-Italic[wght].ttf')});font-weight:300 700}}
@font-face{{font-family:'Raleway';src:url(data:font/ttf;base64,{b64(FONT_DIR + '/raleway/Raleway[wght].ttf')});font-weight:100 900}}
"""

CSS = FONTS + """
@page{size:A4;margin:0}
*{margin:0;padding:0;box-sizing:border-box}
body{font-variant-numeric:lining-nums;font-feature-settings:'lnum' 1;font-family:Raleway;color:#1a2236;font-size:10.5pt;line-height:1.5}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;display:flex;flex-direction:column}
.page:last-child{page-break-after:auto}
.band{background:#060c1f;color:#fff;padding:13mm 16mm 11mm;position:relative;overflow:hidden}
.band .mark{position:absolute;right:-8mm;top:-6mm;height:62mm;opacity:.09}
.brand{display:flex;align-items:center;gap:3mm;font-family:Cormorant;font-size:13pt;letter-spacing:.12em;color:#D4AF37}
.band h1{font-family:Cormorant;font-weight:600;font-size:27pt;line-height:1.08;margin-top:7mm;max-width:150mm}
.band .sub{font-family:Cormorant;font-style:italic;font-size:14pt;color:rgba(255,255,255,.72);margin-top:2.5mm}
.gold{height:1.2mm;background:linear-gradient(90deg,#b8923a,#D4AF37,#b8923a)}
.body{padding:9mm 16mm 0;flex:1}
h2{font-family:Cormorant;font-weight:600;font-size:16pt;color:#060c1f;margin:0 0 3mm}
.qa{background:#f6f1e6;border-left:1.2mm solid #D4AF37;padding:5mm 6mm;font-size:10.5pt;line-height:1.6}
.facts{width:100%;border-collapse:collapse;margin-top:2mm}
.facts td{padding:2.6mm 3mm;border-bottom:.3mm solid #e4dccb;vertical-align:top;font-size:9.8pt}
.facts td:first-child{width:48mm;font-weight:700;color:#060c1f}
.sheet{display:grid;grid-template-columns:1fr 1fr;gap:3mm 6mm;margin-top:2mm}
.sheet div{border-bottom:.3mm solid #8a8f9c;padding:6mm 0 1.2mm;font-size:8.5pt;color:#5a6070}
.steps{margin-top:1mm}
.step{display:flex;gap:4mm;padding:3.4mm 0;border-bottom:.3mm solid #e4dccb}
.box{width:5.5mm;height:5.5mm;border:.45mm solid #060c1f;border-radius:.6mm;flex-shrink:0;margin-top:.6mm}
.step .n{font-family:Cormorant;font-weight:700;font-size:13pt;color:#b8923a;width:5mm;flex-shrink:0;line-height:1.2}
.step .t{flex:1}
.step b{display:block;font-size:10.5pt;color:#060c1f}
.step p{font-size:9.6pt;color:#3a4152;margin-top:.8mm}
.step .d{width:30mm;flex-shrink:0;border-bottom:.3mm solid #8a8f9c;align-self:flex-end;font-size:7.5pt;color:#8a8f9c;padding-bottom:.6mm}
.mist{display:grid;grid-template-columns:1fr 1fr;gap:2mm 6mm;margin-top:1mm}
.mist div{display:flex;gap:2.5mm;font-size:9.5pt;line-height:1.45}
.mist div:before{content:"";width:2mm;height:2mm;background:#b8923a;transform:rotate(45deg);flex-shrink:0;margin-top:1.6mm}
.help{margin:7mm 16mm 0;background:#060c1f;color:#fff;padding:6mm 7mm;display:flex;justify-content:space-between;align-items:center;gap:6mm}
.help h3{font-family:Cormorant;font-weight:600;font-size:16pt;color:#D4AF37}
.help p{font-size:9.5pt;color:rgba(255,255,255,.78);margin-top:1mm;max-width:105mm}
.help .c{text-align:right;font-size:10pt;line-height:1.7;white-space:nowrap}
.help .c b{color:#D4AF37;font-weight:600}
.foot{margin-top:auto;padding:5mm 16mm 8mm;display:flex;justify-content:space-between;font-size:7.5pt;color:#7a8090;border-top:.3mm solid #e4dccb}
.sec{margin-top:7mm}
.t1 .step{padding:2.6mm 0}.t1 .step p{font-size:9.1pt;margin-top:.5mm}.t1 .help{margin-top:5mm;padding:5mm 6mm}.t1 .body{padding-top:9mm}
.t2 .step{padding:2mm 0}.t2 .step p{font-size:8.7pt;line-height:1.4}.t2 .step b{font-size:10pt}.t2 .mist div{font-size:9pt}.t2 .sec{margin-top:5mm}.t2 .help p{font-size:9pt}
"""


def esc(s):
    return html.escape(s or "")


def mark(color, cls="", h=None):
    style = f' style="height:{h}"' if h else ""
    return f'<svg class="{cls}" viewBox="0 0 215 295"{style}><path fill-rule="evenodd" fill="{color}" d="{TRIDENT}"/></svg>'


def long_date(iso):
    d = date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%B %Y')}"


def build(g, tight=0):
    title = g["title"]
    sub = g.get("subtitle", "Employer checklist")
    reviewed = long_date(g["last_reviewed_at"]) if g.get("last_reviewed_at") else ""
    url = f"tridenthr.co.uk/guides/{g['slug']}"
    foot = lambda n: f'<div class="foot"><span>{esc(g.get("jurisdiction", ""))} · Checked {reviewed} · Not legal advice</span><span>{url} · {n} of 2</span></div>'
    band = f'<div class="band">{mark("#D4AF37", "mark")}<div class="brand">{mark("#D4AF37", h="7mm")}TRIDENT HR</div><h1>{esc(title)}</h1><div class="sub">{esc(sub)}</div></div><div class="gold"></div>'
    facts = "".join(f'<tr><td>{esc(f["label"])}</td><td>{esc(f["value"])}</td></tr>' for f in g["at_a_glance"])
    sheet = "".join(f"<div>{esc(x)}</div>" for x in g.get("worksheet", []))
    p1 = f'''<div class="page">{band}<div class="body">
<h2>The short answer</h2><div class="qa">{esc(g["quick_answer"])}</div>
<div class="sec"><h2>Key facts</h2><table class="facts">{facts}</table></div>
{f'<div class="sec"><h2>Your case</h2><div class="sheet">{sheet}</div></div>' if sheet else ""}
</div>{foot(1)}</div>'''
    steps = "".join(f'<div class="step"><div class="box"></div><div class="n">{i}</div><div class="t"><b>{esc(s["title"])}</b><p>{esc(s["body"])}</p></div><div class="d">Done on</div></div>' for i, s in enumerate(g["steps"], 1))
    mist = "".join(f"<div>{esc(m)}</div>" for m in g["mistakes"])
    p2 = f'''<div class="page"><div class="body" style="padding-top:12mm">
<h2>Step by step</h2><div class="steps">{steps}</div>
<div class="sec"><h2>Common mistakes</h2><div class="mist">{mist}</div></div>
</div>
<div class="help"><div><h3>{esc(g.get("help_title") or "Need a hand?")}</h3><p>{esc(g.get("help_body") or "")}</p></div><div class="c"><b>0330 133 6933</b><br>tridenthr.co.uk/contact</div></div>
{foot(2)}</div>'''
    cls = " ".join(f"t{i}" for i in range(1, tight + 1))
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body class='{cls}'>{p1}{p2}</body></html>"


WORKSHEET = ["Employee or matter", "Manager handling it", "Date started", "Next deadline"]


def render_all(src, outdir):
    import os
    os.makedirs(outdir, exist_ok=True)
    guides = json.load(open(src))
    report = []
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={"width": 794, "height": 1123})
        for g in guides:
            g.setdefault("subtitle", "Employer checklist")
            if g["slug"] == "unfair-dismissal-qualifying-period":
                g["worksheet"] = ["Employee", "Start date", "Date employment would end (incl. notice)", "Fair reason"]
            elif g.get("topic_group") != "hr_software":
                g["worksheet"] = WORKSHEET
            for tight in range(3):
                pg.set_content(build(g, tight))
                pg.wait_for_timeout(300)
                over = pg.evaluate("[...document.querySelectorAll('.page')].map(p=>p.scrollHeight)")
                if max(over) <= 1123:
                    break
            pg.pdf(path=f"{outdir}/{g['slug']}-checklist.pdf", format="A4", print_background=True, prefer_css_page_size=True)
            report.append((g["slug"], over))
        br.close()
    for r in report:
        print(r[0], r[1], "OVERFLOW" if max(r[1]) > 1123 else "")


if __name__ == "__main__" and sys.argv[1] == "--all":
    render_all(sys.argv[2], sys.argv[3])
    sys.exit()

if __name__ == "__main__":
    g = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page()
        pg.set_content(build(g))
        pg.wait_for_timeout(500)
        pg.pdf(path=out, format="A4", print_background=True, prefer_css_page_size=True)
        if len(sys.argv) > 3:
            pg.set_viewport_size({"width": 794, "height": 1123})
            pg.screenshot(path=sys.argv[3], full_page=True)
        br.close()
    print(out)
