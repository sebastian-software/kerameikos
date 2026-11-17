"""Build the asset overview page for GitHub Pages, with one brand package per product.

usage: python3 tools/build-site.py [outdir]   (default: _site)

Writes one static index.html that shows every product's marks, small versions, and lockups with
download links, the palette, the typeface, the theme, and the frame, and copies the files it links
to. Each product also gets a zip file with everything a site or document needs. The
products and their motifs come from the members table in README.md, so a new member appears here
once it is listed there. Needs only the Python standard library.
"""
import html
import re
import shutil
import sys
import zipfile
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


# Rendered by tools/build-icons.mjs; offered as plain downloads beside the tiles.
RASTERS = [
    ("icons/favicon.ico", "favicon.ico"),
    ("icons/apple-touch-icon.png", "apple-touch-icon.png"),
    ("icons/icon-192.png", "icon-192.png"),
    ("icons/icon-512.png", "icon-512.png"),
    ("png/mark.png", "mark.png"),
    ("png/mark-on-dark.png", "mark-on-dark.png"),
    ("png/lockup.png", "lockup.png"),
    ("png/lockup-on-dark.png", "lockup-on-dark.png"),
]


def rasters(product):
    links = [
        f'<a href="marks/{product}/{path}" download>{e(label)}</a>'
        for path, label in RASTERS
        if (ROOT / "marks" / product / path).exists()
    ]
    return f'<p class="files">{"".join(links)}</p>' if links else ""


PACKAGE_README = """{name} brand package
{rule}

From Kerameikos, the brand of Sebastian Software's products with ancient-Greek names:
{site}

Files
-----

mark.svg, mark-on-dark.svg, mark-mono.svg
    The full mark, from 192 pixels up. "On dark" has a paper disc under the mark for dark
    surfaces; "mono" is for one-color print.
mark-small.svg, mark-small-on-dark.svg, mark-small-mono.svg
    The small version, below 192 pixels and beside the name.
lockup.svg, lockup-on-dark.svg, png/lockup*.png
    Mark and name, for emails, slides, and documents. On websites set the name as live text.
png/mark.png, png/mark-on-dark.png
    The full mark at 1024 pixels, for tools that do not take SVG.
icons/
    favicon.ico (16, 32, 48), apple-touch-icon.png (180), icon-192.png and icon-512.png for a
    web app manifest.
fonts/
    Cinzel Hellenic, for the product name as live text. SIL Open Font License, see OFL.txt.

In the <head> of a website
--------------------------

<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/mark-small-on-dark.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">

In a web app manifest
---------------------

"icons": [
  {{ "src": "/icon-192.png", "sizes": "192x192", "type": "image/png" }},
  {{ "src": "/icon-512.png", "sizes": "512x512", "type": "image/png" }}
]

Rules
-----

Clear space of half the mark's height on every side. Never recolor, stretch, rotate, crop,
or outline the mark, and put it on photographs only with its paper disc. The full style guide:
{repo}/blob/main/DESIGN.md

The marks, lockups, and icons are the brand of Sebastian Software and are not licensed for use
outside its products. The typeface is licensed under the SIL Open Font License (OFL.txt).
"""


def package(name, slug):
    """A zip with every file of one product, a short guide, and the typeface."""
    src = ROOT / "marks" / slug
    path = OUT / "packages" / f"{slug}.zip"
    path.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(src.glob("*.svg")):
            z.write(f, f"{slug}/{f.name}")
        for sub in ("icons", "png"):
            for f in sorted((src / sub).glob("*")):
                z.write(f, f"{slug}/{sub}/{f.name}")
        for font in ("CinzelHellenic-Regular.woff2", "CinzelHellenic-Regular.ttf"):
            z.write(ROOT / font, f"{slug}/fonts/{font}")
        z.write(ROOT / "OFL.txt", f"{slug}/fonts/OFL.txt")
        guide = PACKAGE_README.format(
            name=name, rule="=" * (len(name) + 14), site=f"https://sebastian-software.github.io/kerameikos/#{slug}", repo=REPO
        )
        z.writestr(f"{slug}/README.txt", guide)



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
      <p class="links"><a class="package" href="packages/{slug}.zip" download>Brand package (.zip)</a>
      <a href="{REPO}/blob/main/marks/{slug}/README.md">Idea and history</a></p>
    </div>
  </header>
  <div class="grid">{''.join(tile(slug, *f) for f in FILES)}</div>
  <div class="grid lockups">{''.join(tile(slug, *f, cls="tile wide") for f in LOCKUPS)}</div>
  {rasters(slug)}
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
.product {{ padding: 5rem 0; border-bottom: 1px solid var(--hair); }}
.product header {{ display: flex; gap: 1.5rem; align-items: center; margin-bottom: 1.75rem; }}
.product .lead {{ width: 6rem; height: 6rem; flex: none; }}
.what {{ margin: 0.4rem 0 0; font-size: 1.0625rem; max-width: 46rem; }}
.what code {{ font: 0.9em var(--mono); }}
.motif {{ margin: 0.45rem 0 0; color: var(--ink-2); max-width: 46rem; }}
.label {{ font: 0.6875rem/1 var(--mono); letter-spacing: 0.16em; text-transform: uppercase; color: var(--accent);
  margin-right: 0.35rem; }}
.links {{ margin: 0.5rem 0 0; font-size: 0.875rem; display: flex; flex-wrap: wrap; gap: 0.4rem 1.25rem; align-items: center; }}
.package {{ background: var(--accent); color: #fff; padding: 0.35rem 0.75rem; text-decoration: none; }}
.product .files {{ margin: 1rem 0 0; font: 0.75rem/1.4 var(--mono); }}
pre {{ font: 0.8125rem/1.6 var(--mono); background: #fdfcf8; border: 1px solid var(--hair); padding: 1rem; overflow-x: auto; }}
p code {{ font: 0.9em var(--mono); }}
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
  lockups, icons, palette, typeface, and theme, and a brand package per product. The Kerameikos was the potters' quarter of Athens, where the
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
  <h3>Theme</h3>
  <p>The palette as code, generated from the style guide, for websites of the family:</p>
  <p class="files"><a href="theme/theme.css" download>theme.css</a>
  <a href="theme/ardo.js" download>ardo.js</a>
  <a href="theme/tokens.json" download>tokens.json</a></p>
  <p><code>theme.css</code> sets the colors as <code>--kr-*</code> custom properties, light and
  dark, loads Cinzel Hellenic, and styles the lockup as live text (<code>.kr-lockup</code>).
  <code>ardo.js</code> is the theme for sites built with Ardo. Both come with the package:</p>
  <pre>pnpm add github:sebastian-software/kerameikos

import "kerameikos/theme.css"
import {{ KERAMEIKOS_ARDO_THEME }} from "kerameikos/ardo"</pre>
</div></div>

<div class="band parchment"><div class="wrap">
  <h3>Typeface</h3>
  <p class="type">ΑΒΓΔ PALAMEDES TEREON</p>
  <p>Cinzel Hellenic, for product names and headlines only, in capitals with 0.16 em spacing.
  Licensed under the SIL Open Font License.</p>
  <p class="files"><a href="CinzelHellenic-Regular.woff2" download>CinzelHellenic-Regular.woff2</a>
  <a href="CinzelHellenic-Regular.ttf" download>CinzelHellenic-Regular.ttf</a>
  <a href="OFL.txt">OFL.txt</a></p>
</div></div>

<div class="band"><div class="wrap">
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
shutil.copytree(ROOT / "theme", OUT / "theme")
for name, slug, _, _ in members:
    dst = OUT / "marks" / slug
    dst.mkdir(parents=True)
    for f in (ROOT / "marks" / slug).glob("*.svg"):
        shutil.copy2(f, dst / f.name)
    for sub in ("icons", "png"):
        if (ROOT / "marks" / slug / sub).exists():
            shutil.copytree(ROOT / "marks" / slug / sub, dst / sub)
    package(name, slug)
(OUT / ".nojekyll").write_text("")
print(f"{len(members)} products, written to {OUT}")
