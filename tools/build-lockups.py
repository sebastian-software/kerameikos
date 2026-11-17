"""Build the horizontal lockups: each product's mark beside its name in Cinzel Hellenic.

usage: python3 tools/build-lockups.py
Writes marks/<product>/lockup.svg (on paper) and lockup-on-dark.svg for every product listed
below. The name is converted to outlines, so the files need no font. Proportions follow the
Tereon and Palamedes headers: the name's font size is 0.625 of the mark's height, letters are
spaced 0.16 em apart, and the gap between mark and name is 0.35 of the mark's height.
"""
import re
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

ROOT = Path(__file__).resolve().parent.parent
PRODUCTS = ["Palamedes", "Tereon", "Stentaro", "Terminaro", "Gramano", "Curano", "Agoros", "Naos"]
MARK = 240                 # the mark's height in lockup units
SIZE = 0.625 * MARK        # font size of the name
TRACKING = 0.16            # letter spacing in em
GAP = 0.35 * MARK          # space between mark and name
NAVY, PAPER = "#0E2A4D", "#FAF9F4"

font = TTFont(ROOT / "CinzelHellenic-Regular.ttf")
upm = font["head"].unitsPerEm
cap = font["OS/2"].sCapHeight or 0.7 * upm
glyphs, cmap, hmtx = font.getGlyphSet(), font.getBestCmap(), font["hmtx"]
scale = SIZE / upm


def name_path(text: str) -> tuple[str, float]:
    """Outlines of the text, set on a baseline at y = 0, and its advance width."""
    pen = SVGPathPen(glyphs)
    x = 0.0
    for i, ch in enumerate(text):
        g = cmap[ord(ch)]
        tp = TransformPen(pen, (scale, 0, 0, -scale, x, 0))
        glyphs[g].draw(tp)
        x += hmtx[g][0] * scale
        if i < len(text) - 1:
            x += TRACKING * SIZE
    return pen.getCommands(), x


def inner(svg: str) -> str:
    """The mark's content without its outer <svg> element."""
    return re.sub(r"^.*?<svg[^>]*>", "", svg, count=1, flags=re.S).rsplit("</svg>", 1)[0]


for product in PRODUCTS:
    d, width = name_path(product.upper())
    total = MARK + GAP + width
    baseline = MARK / 2 + cap * scale / 2      # cap height centered on the mark
    for variant, mark_file, ink in (("lockup", "mark.svg", NAVY), ("lockup-on-dark", "mark-on-dark.svg", PAPER)):
        mark = (ROOT / "marks" / product.lower() / mark_file).read_text()
        svg = (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total:.1f} {MARK}" role="img" '
            f'aria-label="{product}">'
            f'<svg x="0" y="0" width="{MARK}" height="{MARK}" viewBox="0 0 240 240">{inner(mark)}</svg>'
            f'<path fill="{ink}" transform="translate({MARK + GAP:.2f} {baseline:.2f})" d="{d}"/>'
            "</svg>\n"
        )
        (ROOT / "marks" / product.lower() / f"{variant}.svg").write_text(svg)
    print(f"{product}: {total:.0f} x {MARK}")
