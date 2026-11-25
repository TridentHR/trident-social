"""Render an Employer Guide social set to PNGs and a LinkedIn PDF.

Usage: python3 render_guide.py guide.json outdir [chrome_path]
guide.json fields: title, applies, read_minutes, last_reviewed_at, quick_answer,
glance [{label, value}] (4 rows), steps [{title}], mistakes [str], back_line,
pack_title, pack_desc.
Fonts: tools/.fonts/ofl/raleway and tools/.fonts/ofl/cinzel (Google Fonts, gitignored).
Outputs: 1-cover.png ... 6-read-the-full-guide.png, facebook.png, linkedin.pdf
"""
import base64, json, os, re, sys, tempfile
from playwright.sync_api import sync_playwright
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import make_guide_slides as mgs

FONTS = os.path.join(ROOT, "tools", ".fonts", "ofl")
NAMES = ["1-cover", "2-quick-answer", "3-at-a-glance", "4-steps", "5-mistakes", "6-read-the-full-guide"]


def b64(p):
    return base64.b64encode(open(p, "rb").read()).decode()


def main(src, out, chrome=None):
    g = json.load(open(src))
    os.makedirs(out, exist_ok=True)
    tmp = tempfile.mkdtemp()
    mgs.build(g, tmp)
    rale = b64(os.path.join(FONTS, "raleway", "Raleway[wght].ttf"))
    cin = b64(os.path.join(FONTS, "cinzel", "Cinzel[wght].ttf"))
    logo = b64(os.path.join(ROOT, "assets", "trident-logo-gold.png"))
    files = [(f"Guide{i}.dc.html", NAMES[i - 1]) for i in range(1, 7)] + [("GuideFB.dc.html", "facebook")]
    pngs = []
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=chrome) if chrome else pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for f, name in files:
            s = open(os.path.join(tmp, f)).read()
            body = re.search(r"<x-dc>(.*)</x-dc>", s, re.S).group(1)
            style = re.search(r"<style>(.*?)</style>", body, re.S).group(1)
            body = re.sub(r"<helmet>.*?</helmet>", "", body, flags=re.S)
            style = (f"@font-face{{font-family:Raleway;src:url(data:font/ttf;base64,{rale});font-weight:100 900}}"
                     + style.replace(f"url({mgs.CINZEL})", f"url(data:font/ttf;base64,{cin})"))
            body = body.replace(mgs.LOGO, f"data:image/png;base64,{logo}")
            pg.set_content(f"<html><head><style>{style}</style></head><body style='margin:0'>{body}</body></html>")
            pg.wait_for_timeout(300)
            p = os.path.join(out, f"{name}.png")
            pg.screenshot(path=p)
            pngs.append(p)
        b.close()
    slides = [Image.open(p).convert("RGB") for p in pngs[:6]]
    slides[0].save(os.path.join(out, "linkedin.pdf"), save_all=True, append_images=slides[1:], resolution=72)
    print("\n".join(pngs + [os.path.join(out, "linkedin.pdf")]))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
