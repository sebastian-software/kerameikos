"""Build the asset overview page for GitHub Pages.

usage: python3 tools/build-site.py [outdir]   (default: _site)

Writes one static index.html that shows every product's marks, small versions, and lockups with
download links, the palette, the typeface, and the frame, and copies the files it links to. The
products and their motifs come from the members table in README.md, so a new member appears here
once it is listed there. Needs only the Python standard library.
"""
import html
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "_site"
REPO = "https://github.com/sebastian-software/kerameikos"

readme = (ROOT / "README.md").read_text()
members = re.findall(
    r"^\| \[(\w+)\]\(marks/(\w+)/README\.md\)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|$", readme, re.M
)
if not members:
    sys.exit("no members found in README.md")

# Each file is shown on the background it is made for.
FILES = [
    ("mark.svg", "Mark", "light"),
    ("mark-on-dark.svg", "On dark", "dark"),
    ("mark-mono.svg", "One color", "light"),
    ("mark-small.svg", "Small", "light"),
    ("mark-small-on-dark.svg", "Small on dark", "dark"),
    ("mark-small-mono.svg", "Small one color", "light"),
]
LOCKUPS = [("lockup.svg", "Lockup", "light"), ("lockup-on-dark.svg", "Lockup on dark", "dark")]

PALETTE = [
    ("Navy", "#0E2A4D", "Ink and the mass of every motif"),
    ("Mark bronze", "#BC8A45", "The ring and accents in the marks; not for text"),
    ("Accent bronze", "#866026", "Links, actions, focus"),
    ("Paper", "#FAF9F4", "The ground of every page"),
    ("Parchment", "#F3EFE3", "Alternate bands"),
    ("Mist", "#E8EDF2", "Cool bands"),
    ("Night", "#0C1724", "The ground in dark mode"),
]

e = html.escape


def tile(product, file, label, bg, cls="tile"):
    path = f"marks/{product}/{file}"
    if not (ROOT / path).exists():
        return ""
    # Small versions are shown at the size they are made for, so their purpose is visible.
    if "small" in file:
        cls += " small"
    return (
        f'<figure class="{cls} {bg}"><a href="{path}" download>'
        f'<img src="{path}" alt="{e(label)}" loading="lazy"></a>'
        f'<figcaption><a href="{path}" download>{e(label)}</a></figcaption></figure>'
    )


def sizes(product):
    full, small = f"marks/{product}/mark.svg", f"marks/{product}/mark-small.svg"
    cells = []
    for px in (192, 64, 48, 32):
        src = full if px >= 192 or not (ROOT / small).exists() else small
        cells.append(f'<span><img src="{src}" width="{px}" height="{px}" alt=""><em>{px}</em></span>')
    return '<div class="sizes">' + "".join(cells) + "</div>"


def description(slug):
    """The product line of a mark's page: what the product is, without notes about the mark."""
    text = (ROOT / "marks" / slug / "README.md").read_text()
    m = re.search(r"\*\*Product:\*\*\s*(.+?)\n\n", text, re.S)
    if not m:
        return ""
    line = " ".join(m.group(1).split())
    sentences = [x for x in re.split(r"(?<=\.)\s+", line) if not re.search(r"\bmark\b", x, re.I)]
    line = " ".join(sentences)
    line = e(line[0].upper() + line[1:])
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", line)


sections = []
for name, slug, motif, stands in members:
    sections.append(
        f"""
<section class="product" id="{slug}">
  <header>
    <img class="lead" src="marks/{slug}/mark.svg" alt="">
    <div>
      <h2>{e(name)}</h2>
      <p class="what">{description(slug)}</p>
      <p class="motif"><span class="label">Mark</span> {e(motif)}: {e(stands[0].lower() + stands[1:])}.</p>
      <p class="links"><a href="{REPO}/blob/main/marks/{slug}/README.md">Idea and history</a></p>
    </div>
  </header>
  <div class="grid">{''.join(tile(slug, *f) for f in FILES)}</div>
  <div class="grid lockups">{''.join(tile(slug, *f, cls="tile wide") for f in LOCKUPS)}</div>
  {sizes(slug)}
</section>"""
    )

swatches = "".join(
    f'<li><span class="chip" style="background:{hexv}"></span><strong>{e(n)}</strong>'
    f"<code>{hexv}</code><small>{e(use)}</small></li>"
    for n, hexv, use in PALETTE
)
nav = "".join(f'<a href="#{slug}">{e(name)}</a>' for name, slug, _, _ in members)

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kerameikos</title>
<meta name="description" content="Marks, small versions, lockups, palette, and typeface of the products with ancient-Greek names.">
<link rel="icon" href="marks/palamedes/mark-small.svg">
<style>
@font-face {{ font-family: "Cinzel Hellenic"; src: url("CinzelHellenic-Regular.woff2") format("woff2"); font-display: swap; }}
:root {{
  --paper: #faf9f4; --parchment: #f3efe3; --mist: #e8edf2; --ink: #0e2a4d; --ink-2: #3f5471;
  --ink-3: #526176; --hair: #ddd6c6; --accent: #866026; --night: #0c1724;
  --display: "Cinzel Hellenic", "Times New Roman", serif;
  --mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--paper); color: var(--ink);
  font: 16px/1.6 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; }}
a {{ color: var(--accent); }}
.wrap {{ max-width: 80rem; margin: 0 auto; padding: 0 1.25rem; }}
.top {{ border-bottom: 1px solid var(--hair); padding: 3.5rem 0 2rem; }}
.eyebrow {{ font: 0.6875rem/1 var(--mono); letter-spacing: 0.22em; text-transform: uppercase; color: var(--ink-3); }}
h1, h2 {{ font-family: var(--display); font-weight: 400; letter-spacing: 0.08em; text-transform: uppercase; margin: 0; }}
h1 {{ font-size: clamp(1.9rem, 4.5vw, 3.1rem); line-height: 1.15; margin-top: 0.75rem; }}
h2 {{ font-size: 1.6rem; letter-spacing: 0.16em; }}
h3 {{ font: 0.75rem/1 var(--mono); letter-spacing: 0.16em; text-transform: uppercase; color: var(--ink-3); margin: 0 0 1rem; }}
.lede {{ max-width: 42rem; color: var(--ink-2); font-size: 1.125rem; }}
nav {{ display: flex; flex-wrap: wrap; gap: 0.25rem 1.25rem; margin-top: 1.5rem; font-size: 0.9375rem; }}
.family {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(7.5rem, 1fr)); gap: 1rem; margin-top: 2rem; }}
.family a {{ text-decoration: none; color: var(--ink); text-align: center; font-size: 0.8125rem;
  letter-spacing: 0.12em; text-transform: uppercase; }}
.family img {{ width: 100%; display: block; margin-bottom: 0.4rem; }}
.band {{ padding: 3rem 0; border-bottom: 1px solid var(--hair); }}
.band.parchment {{ background: var(--parchment); }}
.product {{ padding: 3rem 0; border-bottom: 1px solid var(--hair); }}
.product header {{ display: flex; gap: 1.5rem; align-items: center; margin-bottom: 1.75rem; }}
.product .lead {{ width: 6rem; height: 6rem; flex: none; }}
.what {{ margin: 0.4rem 0 0; font-size: 1.0625rem; max-width: 46rem; }}
.what code {{ font: 0.9em var(--mono); }}
.motif {{ margin: 0.45rem 0 0; color: var(--ink-2); max-width: 46rem; }}
.label {{ font: 0.6875rem/1 var(--mono); letter-spacing: 0.16em; text-transform: uppercase; color: var(--accent);
  margin-right: 0.35rem; }}
.links {{ margin: 0.4rem 0 0; font-size: 0.875rem; }}
.grid {{ display: grid; grid-template-columns: repeat(6, 1fr); gap: 1px;
  background: var(--hair); border: 1px solid var(--hair); }}
.grid.lockups {{ grid-template-columns: repeat(2, 1fr); margin-top: 1rem; }}
.tile {{ margin: 0; padding: 1rem; display: flex; flex-direction: column; align-items: center; gap: 0.6rem; }}
.tile.light {{ background: var(--paper); }}
.tile.dark {{ background: var(--night); }}
.tile img {{ width: 100%; max-width: 12rem; aspect-ratio: 1; display: block; }}
.tile.small {{ justify-content: flex-end; }}
.tile.small img {{ width: 4rem; height: 4rem; margin-block: auto; }}
.tile.wide img {{ max-width: 100%; aspect-ratio: auto; height: 3.5rem; width: auto; }}
.tile figcaption {{ font: 0.6875rem/1 var(--mono); letter-spacing: 0.14em; text-transform: uppercase; }}
.tile.dark figcaption a {{ color: #d2a660; }}
.sizes {{ display: flex; align-items: flex-end; gap: 1.5rem; margin-top: 1rem; flex-wrap: wrap; }}
.sizes span {{ display: flex; flex-direction: column; align-items: center; gap: 0.35rem; }}
.sizes em {{ font: normal 0.6875rem/1 var(--mono); color: var(--ink-3); }}
.palette {{ list-style: none; padding: 0; margin: 0; display: grid;
  grid-template-columns: repeat(auto-fill, minmax(13rem, 1fr)); gap: 1rem; }}
.palette li {{ display: grid; grid-template-columns: 3rem 1fr; column-gap: 0.75rem; align-items: center; }}
.chip {{ grid-row: span 3; width: 3rem; height: 3rem; border: 1px solid var(--hair); }}
.palette code {{ font: 0.8125rem var(--mono); color: var(--ink-2); }}
.palette small {{ color: var(--ink-3); line-height: 1.35; }}
.type {{ font-family: var(--display); font-size: clamp(1.75rem, 5vw, 3rem); letter-spacing: 0.16em; margin: 0.5rem 0; }}
.files {{ display: flex; flex-wrap: wrap; gap: 0.5rem 1.5rem; }}
.frame {{ display: flex; gap: 2rem; align-items: center; flex-wrap: wrap; }}
.frame img {{ width: 12rem; height: 12rem; }}
.usage {{ display: grid; grid-template-columns: 9rem 1fr; gap: 0.75rem 1.5rem; margin: 0; max-width: 56rem; }}
.usage dt {{ font: 0.75rem/1.9 var(--mono); letter-spacing: 0.14em; text-transform: uppercase; color: var(--accent); }}
.usage dd {{ margin: 0; color: var(--ink-2); }}
@media (max-width: 40rem) {{ .usage {{ grid-template-columns: 1fr; gap: 0.2rem; }} .usage dd {{ margin-bottom: 0.75rem; }} }}
footer {{ padding: 2rem 0 3rem; color: var(--ink-3); font-size: 0.875rem; }}
@media (max-width: 64rem) {{ .grid {{ grid-template-columns: repeat(3, 1fr); }} }}
@media (max-width: 40rem) {{ .grid {{ grid-template-columns: repeat(2, 1fr); }} .grid.lockups {{ grid-template-columns: 1fr; }} .tile.wide img {{ height: 2.75rem; }} .product header {{ align-items: flex-start; }} .product .lead {{ width: 4rem; height: 4rem; }} }}
</style>
</head>
<body>
<div class="top"><div class="wrap">
  <div class="eyebrow">Sebastian Software · Brand assets</div>
  <h1>Kerameikos</h1>
  <p class="lede">The brand assets of our products with ancient-Greek names: marks, small versions,
  lockups, palette, and typeface. The Kerameikos was the potters' quarter of Athens, where the
  painted vases were made whose style the marks follow. Click any file to download it. The rules are in the
  <a href="{REPO}/blob/main/DESIGN.md">style guide</a> and the
  <a href="{REPO}/blob/main/README.md">frame rule</a>.</p>
  <div class="family">{''.join(f'<a href="#{slug}"><img src="marks/{slug}/mark.svg" alt="">{e(name)}</a>' for name, slug, _, _ in members)}</div>
</div></div>

<div class="band parchment"><div class="wrap">
  <h3>Which file to use</h3>
  <dl class="usage">
    <dt>Mark</dt>
    <dd>For 192 pixels and more, on paper or another light surface. Inside the ring the file is
    transparent: sky, skin, and the paper ring are not drawn, the page shows through.</dd>
    <dt>On dark</dt>
    <dd>For dark surfaces. It looks the same as the mark but has a paper disc under it. Without
    the disc the dark page would show through those transparent parts, and the navy figure
    would vanish into it.</dd>
    <dt>One color</dt>
    <dd>Where only one color can be printed or embossed.</dd>
    <dt>Small</dt>
    <dd>Below 192 pixels: favicons, app icons, avatars. The same figure redrawn with less detail
    and without the paper ring, so it stays readable at 32 to 64 pixels. Also on dark and in
    one color.</dd>
    <dt>Lockup</dt>
    <dd>The small mark beside the name in Cinzel Hellenic, for headers, emails, and slides. On
    websites set the name as live text instead and use the small mark beside it.</dd>
  </dl>
</div></div>

<div class="wrap">{''.join(sections)}</div>

<div class="band parchment"><div class="wrap">
  <h3>Palette</h3>
  <ul class="palette">{swatches}</ul>
</div></div>

<div class="band"><div class="wrap">
  <h3>Typeface</h3>
  <p class="type">ΑΒΓΔ PALAMEDES TEREON</p>
  <p>Cinzel Hellenic, for product names and headlines only, in capitals with 0.16 em spacing.
  Licensed under the SIL Open Font License.</p>
  <p class="files"><a href="CinzelHellenic-Regular.woff2" download>CinzelHellenic-Regular.woff2</a>
  <a href="CinzelHellenic-Regular.ttf" download>CinzelHellenic-Regular.ttf</a>
  <a href="OFL.txt">OFL.txt</a></p>
</div></div>

<div class="band parchment"><div class="wrap">
  <h3>Frame</h3>
  <div class="frame">
    <a href="frame/ring-template.svg" download><img src="frame/ring-template.svg" alt="Ring frame with guides"></a>
    <a href="frame/ring-blank.svg" download><img src="frame/ring-blank.svg" alt="Empty ring frame"></a>
    <p>The frame with its guides and empty, to draw a new mark into. A mark is made from a drawn
    emblem as described in the <a href="{REPO}/blob/main/README.md#making-a-mark-from-a-drawing">README</a>.</p>
  </div>
</div></div>

<footer><div class="wrap">Generated from <a href="{REPO}">sebastian-software/kerameikos</a>.</div></footer>
</body>
</html>
"""

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)
(OUT / "index.html").write_text(page)
for name in ("CinzelHellenic-Regular.woff2", "CinzelHellenic-Regular.ttf", "OFL.txt"):
    shutil.copy2(ROOT / name, OUT / name)
shutil.copytree(ROOT / "frame", OUT / "frame", ignore=shutil.ignore_patterns("*.png"))
for _, slug, _, _ in members:
    dst = OUT / "marks" / slug
    dst.mkdir(parents=True)
    for f in (ROOT / "marks" / slug).glob("*.svg"):
        shutil.copy2(f, dst / f.name)
(OUT / ".nojekyll").write_text("")
print(f"{len(members)} products, written to {OUT}")
