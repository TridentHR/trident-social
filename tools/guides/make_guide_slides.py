"""Employer Guide social template.

Builds a 6-slide carousel (1080x1350) for one guide from its employer_guides
record: cover, quick answer, at a glance, steps, mistakes, back page.
Writes Design canvas artboards (.dc.html). Usage: python3 make_guide_slides.py guide.json outdir
"""
import json, sys, html, os
from datetime import date

CINZEL = "/_blob/e379234a05bdab88089145d033e707c7"
LOGO = "/_blob/97ba543a5756c987d30b4f376f3b9a28"

BG = "#0A0C18"
PANEL = "#14161F"
GOLD = "#D4AF37"
INK = "#FFFFFF"
SOFT = "rgba(255,255,255,0.72)"
MUTED = "rgba(255,255,255,0.5)"

def e(s):
    return html.escape(str(s), quote=True)

def keep_hyphens(s):
    import re
    return re.sub(r"(\S+-\S+)", r'<span style="white-space: nowrap">\1</span>', e(s))

def page(title, inner, n, total):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{e(title)}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;600;700&display=swap">
<style>
@font-face{{font-family:"Cinzel TH";src:url({CINZEL}) format("truetype");font-weight:400 900}}
body{{margin:0}}
a{{color:{GOLD}}}a:hover{{color:#F0D27A}}
</style>
</helmet>
<div style="width: 1080px; height: 1350px; box-sizing: border-box; padding: 84px 96px 72px; background: {BG}; color: {INK}; font-family: Raleway, sans-serif; display: flex; flex-direction: column; font-variant-numeric: lining-nums">
<div style="display: flex; align-items: center; justify-content: space-between">
<div style="display: flex; align-items: center; gap: 16px"><img src="{LOGO}" alt="Trident HR" style="width: 34px; height: auto"><div style="display: flex; flex-direction: column; align-items: center; color: {GOLD}; font-family: 'Cinzel TH', serif"><span style="font-size: 26px; letter-spacing: 6px; line-height: 1">TRIDENT</span><span style="font-size: 12px; letter-spacing: 5px; margin-top: 5px">HR</span></div></div>
<div style="font-size: 20px; font-weight: 600; letter-spacing: 5px; color: {GOLD}">EMPLOYER GUIDE</div>
</div>
{inner}
<div style="display: flex; justify-content: space-between; align-items: center; font-size: 22px; font-weight: 500; color: {MUTED}">
<span>tridenthr.co.uk/guides</span><span>{n} / {total}</span>
</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1080,"height":1350}}}}'>
class Component extends DCLogic {{
  renderVals() {{
    return {{}};
  }}
}}
</script>
</body>
</html>
'''

def sentences(t):
    import re
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+(?=[A-Z])", t.strip()) if x.strip()]

def pack_name(t):
    t = t.strip()
    if t.lower().startswith("free "):
        t = t[5:]
    return t[:1].upper() + t[1:]

def heading(text):
    return f'<h2 style="margin: 0 0 44px; font-family: \'Cinzel TH\', serif; font-weight: 400; font-size: 72px; line-height: 1.1; letter-spacing: 1.5px">{e(text)}</h2>'

def numbered(items, size=36):
    rows = "".join(
        f'<div style="display: flex; gap: 32px; align-items: baseline"><span style="flex: 0 0 48px; font-family: \'Cinzel TH\', serif; font-size: {size+6}px; color: {GOLD}">{i}</span><span style="font-size: {size}px; line-height: 1.35; font-weight: 500">{e(t)}</span></div>'
        for i, t in enumerate(items, 1))
    return f'<div style="display: flex; flex-direction: column; gap: 34px">{rows}</div>'

def build(g, outdir):
    total = 6
    reviewed = date.fromisoformat(g["last_reviewed_at"][:10]).strftime("%-d %B %Y")
    files = []

    # 1 cover
    inner = f'''<div style="margin-top: auto; display: flex; flex-direction: column">
<h1 style="margin: 0; font-family: 'Cinzel TH', serif; font-weight: 400; font-size: 96px; line-height: 1.12; letter-spacing: 2px">{keep_hyphens(g["title"])}</h1>
<div style="margin-top: 56px; display: flex; flex-direction: column; gap: 14px; font-size: 28px; color: {SOFT}">
<span>Applies in <b style="color: {INK}; font-weight: 600">{e(g["applies"])}</b></span>
<span><b style="color: {INK}; font-weight: 600">{e(g["read_minutes"])} min</b> read · Last reviewed <b style="color: {INK}; font-weight: 600">{reviewed}</b></span>
</div>
</div>
<div style="margin: 96px 0 56px; font-size: 26px; font-weight: 600; letter-spacing: 4px; color: {GOLD}">SWIPE FOR THE QUICK ANSWER</div>'''
    files.append(("Guide1.dc.html", "Cover", page(g["title"], inner, 1, total)))

    # 2 quick answer
    inner = f'''<div style="margin: auto 0; background: {PANEL}; border-left: 4px solid {GOLD}; padding: 56px 56px 60px">
<div style="font-size: 22px; font-weight: 700; letter-spacing: 6px; color: {GOLD}">QUICK ANSWER</div>
{"".join(f'<p style="margin: 30px 0 0; font-size: 38px; line-height: 1.45; color: rgba(255,255,255,0.92)">{e(x)}</p>' for x in sentences(g["quick_answer"]))}
</div>'''
    files.append(("Guide2.dc.html", "Quick answer", page("Quick answer", inner, 2, total)))

    # 3 at a glance
    rows = "".join(
        f'<div style="display: flex; flex-direction: column; gap: 10px"><span style="font-size: 26px; font-weight: 600; color: {GOLD}">{e(r["label"])}</span><span style="font-size: 34px; line-height: 1.4">{e(r["value"])}</span></div>'
        for r in g["glance"])
    inner = f'<div style="margin: auto 0">{heading("At a glance")}<div style="display: flex; flex-direction: column; gap: 46px">{rows}</div></div>'
    files.append(("Guide3.dc.html", "At a glance", page("At a glance", inner, 3, total)))

    # 4 steps
    inner = f'<div style="margin: auto 0">{heading("Steps")}{numbered([s["title"] for s in g["steps"]], 38)}</div>'
    files.append(("Guide4.dc.html", "Steps", page("Steps", inner, 4, total)))

    # 5 mistakes
    inner = f'<div style="margin: auto 0">{heading("Mistakes to avoid")}{numbered(g["mistakes"], 34)}</div>'
    files.append(("Guide5.dc.html", "Mistakes to avoid", page("Mistakes to avoid", inner, 5, total)))

    # 6 back page
    inner = f'''<div style="margin: auto 0; display: flex; flex-direction: column">
{heading("Read the full guide")}
<p style="margin: 0; font-size: 36px; line-height: 1.5; color: {SOFT}">{e(g["back_line"])}</p>
<div style="margin-top: 64px; background: {PANEL}; border-left: 4px solid {GOLD}; padding: 44px 48px">
<div style="font-size: 22px; font-weight: 700; letter-spacing: 6px; color: {GOLD}">PLUS, FREE TO DOWNLOAD</div>
<div style="margin-top: 20px; font-size: 38px; font-weight: 600">{e(pack_name(g["pack_title"]))}</div>
<div style="margin-top: 12px; font-size: 30px; line-height: 1.45; color: {SOFT}">{e(g["pack_desc"])}</div>
</div>
<div style="margin-top: 64px; font-family: 'Cinzel TH', serif; font-size: 50px; letter-spacing: 1px; color: {GOLD}">tridenthr.co.uk/guides</div>
</div>'''
    files.append(("Guide6.dc.html", "Read the full guide", page("Read the full guide", inner, 6, total)))


    # Facebook single card
    qa = "".join(f'<p style="margin: 22px 0 0; font-size: 31px; line-height: 1.45; color: rgba(255,255,255,0.92)">{e(x)}</p>' for x in sentences(g["quick_answer"]))
    inner = f'''<div style="margin: auto 0; display: flex; flex-direction: column">
<h1 style="margin: 0; font-family: 'Cinzel TH', serif; font-weight: 400; font-size: 70px; line-height: 1.14; letter-spacing: 1.5px">{keep_hyphens(g["title"])}</h1>
<div style="margin-top: 52px; background: {PANEL}; border-left: 4px solid {GOLD}; padding: 40px 46px 46px">
<div style="font-size: 20px; font-weight: 700; letter-spacing: 6px; color: {GOLD}">QUICK ANSWER</div>{qa}
</div>
<div style="margin-top: 46px; font-size: 28px; color: {SOFT}">Read the full guide, plus a free checklist</div>
<div style="margin-top: 12px; font-family: 'Cinzel TH', serif; font-size: 44px; letter-spacing: 1px; color: {GOLD}">tridenthr.co.uk/guides</div>
</div>'''
    fbsrc = page(g["title"], inner, 1, 1).replace('<span>tridenthr.co.uk/guides</span><span>1 / 1</span>', '<span></span><span></span>')
    files.append(("GuideFB.dc.html", "Facebook card", fbsrc))
    os.makedirs(outdir, exist_ok=True)
    for name, _, src in files:
        open(os.path.join(outdir, name), "w").write(src)
    return [(n, t) for n, t, _ in files]

if __name__ == "__main__":
    g = json.load(open(sys.argv[1]))
    for n, t in build(g, sys.argv[2]):
        print(n, t)
