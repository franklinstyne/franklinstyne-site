"""Builds the Monogram Seal logo as outlined SVGs (no font dependency) plus PNG exports."""
import os, subprocess
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

D = os.path.dirname(os.path.abspath(__file__))
OUT = D
os.makedirs(OUT, exist_ok=True)
FONTS = {k: TTFont(os.path.join(D, "..", "fonts", f)) for k, f in
         {"b800": "b800.ttf", "b700": "b700.ttf", "mono": "mono600.ttf"}.items()}


def text_path(font_key, text, x, y, size, spacing=0.0):
    """Return (svg path d, advance width) for text with baseline at (x, y)."""
    f = FONTS[font_key]
    gs = f.getGlyphSet()
    cmap = f.getBestCmap()
    upm = f["head"].unitsPerEm
    s = size / upm
    pen = SVGPathPen(gs)
    cx = x
    for ch in text:
        g = cmap[ord(ch)]
        tp = TransformPen(pen, (s, 0, 0, -s, cx, y))
        gs[g].draw(tp)
        cx += f["hmtx"][g][0] * s + spacing
    return pen.getCommands(), cx - x - spacing


def text_bounds(font_key, text, size, spacing=0.0):
    f = FONTS[font_key]
    gs = f.getGlyphSet()
    cmap = f.getBestCmap()
    s = size / f["head"].unitsPerEm
    xmin, xmax, cx = None, None, 0
    for ch in text:
        g = cmap[ord(ch)]
        bp = BoundsPen(gs)
        gs[g].draw(bp)
        if bp.bounds:
            a, _, b, _ = bp.bounds
            xmin = cx + a * s if xmin is None else min(xmin, cx + a * s)
            xmax = cx + b * s if xmax is None else max(xmax, cx + b * s)
        cx += f["hmtx"][g][0] * s + spacing
    return xmin, xmax


def tile(c_tile, c_chev, c_cur, ox=0, oy=0):
    return (f'<rect x="{ox}" y="{oy}" width="94" height="94" rx="20" fill="{c_tile}"/>'
            f'<path d="M{ox+24} {oy+29} L{ox+45} {oy+47} L{ox+24} {oy+65}" fill="none" stroke="{c_chev}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<rect x="{ox+51}" y="{oy+60}" width="24" height="8" rx="1.5" fill="{c_cur}"/>')


def lockup(c_chev, c_name, c_cur, c_tag):
    name_d, name_w = text_path("b800", "Franklin Styne", 44, 54, 48, -1.4)
    cur_x = 44 + name_w + 7
    tag = "AI, AGENTIC AI & AUTOMATION TRAINER"
    _, unit_w = text_path("mono", tag, 0, 0, 10, 0)
    sp = 1.0
    size = (name_w - sp * (len(tag) - 1)) / unit_w * 10
    tag_d, tag_w = text_path("mono", tag, 46, 84, size, sp)
    w = round(cur_x + 24 + 3)
    body = (f'<path d="M6 17 L30 38 L6 59" fill="none" stroke="{c_chev}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{name_d}" fill="{c_name}"/>'
            f'<rect x="{cur_x:.1f}" y="48" width="22" height="7" rx="1.2" fill="{c_cur}"/>'
            f'<path d="{tag_d}" fill="{c_tag}"/>')
    return w, 94, body


def svg(w, h, body, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{label}">{body}</svg>\n')


INK, PAPER, GOLD, GOLD_DEEP, GOLD_TEXT = "#13302E", "#EEF3F1", "#F0B54A", "#D9901A", "#93590A"
files = {
    "franklinstyne-logo-for-light-backgrounds.svg": svg(*lockup(GOLD_DEEP, INK, GOLD_DEEP, GOLD_TEXT), "Franklin Styne, AI, Agentic AI and Automation Trainer"),
    "franklinstyne-logo-for-dark-backgrounds.svg": svg(*lockup(GOLD, PAPER, GOLD, GOLD), "Franklin Styne, AI, Agentic AI and Automation Trainer"),
    "franklinstyne-icon.svg": svg(94, 94, tile(INK, GOLD, PAPER), "Franklin Styne"),
    "franklinstyne-icon-light.svg": svg(94, 94, tile(PAPER, GOLD_DEEP, INK), "Franklin Styne"),
}
for n, s in files.items():
    open(os.path.join(OUT, n), "w").write(s)

# PNG exports with transparent backgrounds via headless Chromium
CH = "/opt/pw-browsers/chromium"
def png(svgname, pngname, width):
    s = files[svgname]
    vw, vh = [float(v) for v in s.split('viewBox="')[1].split('"')[0].split()[2:]]
    h = round(width * vh / vw)
    html = os.path.join(OUT, "_tmp.html")
    open(html, "w").write(f'<!doctype html><style>html,body{{margin:0;background:transparent}}svg{{display:block;width:{width}px;height:{h}px}}</style>{s}')
    subprocess.run([CH, "--headless", "--no-sandbox", "--hide-scrollbars", "--default-background-color=00000000",
                    f"--window-size={width},{h + 300}", f"--screenshot={os.path.join(OUT, pngname)}", "file://" + html],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
    os.remove(html)
    from PIL import Image
    im = Image.open(os.path.join(OUT, pngname)); im.crop((0, 0, width, h)).save(os.path.join(OUT, pngname))

png("franklinstyne-logo-for-light-backgrounds.svg", "franklinstyne-logo-for-light-backgrounds.png", 1600)
png("franklinstyne-logo-for-dark-backgrounds.svg", "franklinstyne-logo-for-dark-backgrounds.png", 1600)
png("franklinstyne-icon.svg", "franklinstyne-icon-512.png", 512)
png("franklinstyne-icon-light.svg", "franklinstyne-icon-light-512.png", 512)
print(sorted(os.listdir(OUT)))
