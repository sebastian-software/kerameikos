# Kerameikos

The shared identity of Sebastian Software's products with ancient-Greek names: Palamedes,
Tereon, Stentaro, Terminaro, Gramano, Curano, Agoros, and Naos. Each has a mark that shows a
figure from the Greek world at work, drawn like the painting on a Greek vase, in navy and bronze
on paper inside one shared ring. This repository is the single source for those marks, their
small versions and lockups, the typeface, the palette, and the style guide; the products take
what they need from here.

The Kerameikos was the potters' quarter of ancient Athens, where the painted vases were made
whose style these marks follow.

- **Overview with downloads:** https://sebastian-software.github.io/kerameikos/, published from
  `main` by `.github/workflows/pages.yml`.
- **Style guide:** [`DESIGN.md`](DESIGN.md): lockups, typography, colors, layout, and voice.
- **Brand package per product:** a zip with every file of the product (marks, lockups, favicon,
  app icons, PNG files, and the typeface) on the overview page.
- **Theme for websites:** `theme/theme.css` (custom properties, light and dark, the typeface,
  the lockup as live text) and `theme/ardo.js` (the Ardo theme). The repository is an npm
  package; see [Using the theme](#using-the-theme).
- **Making a new mark:** the skill in [`.claude/skills/family-mark/`](.claude/skills/family-mark/SKILL.md).

The marks, lockups, style guide, and tools are the brand of Sebastian Software and are not
licensed for use outside its products. The typeface Cinzel Hellenic is free software under the
[SIL Open Font License](OFL.txt).

## Contents

| Path                                                                                                 | What it is                                                                              |
| ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| [`DESIGN.md`](DESIGN.md)                                                                             | The style guide: lockups, type, colors, layout, voice                                   |
| [`CinzelHellenic-Regular.ttf`](CinzelHellenic-Regular.ttf), [`.woff2`](CinzelHellenic-Regular.woff2) | The typeface for product names, under the [SIL OFL](OFL.txt)                            |
| [`frame/ring-template.svg`](frame/ring-template.svg)                                                 | The frame with its guides                                                               |
| [`frame/ring-blank.svg`](frame/ring-blank.svg)                                                       | The empty frame to draw a motif into                                                    |
| [`marks/<product>/mark.svg`](marks)                                                                  | A mark on paper, transparent background                                                 |
| [`marks/<product>/mark-on-dark.svg`](marks)                                                          | The same with a paper disc under it, for dark surfaces                                  |
| [`marks/<product>/mark-mono.svg`](marks)                                                             | The same in one color                                                                   |
| [`marks/<product>/mark-small.svg`](marks)                                                            | The small version, below 192 pixels; also `-on-dark` and `-mono`                        |
| [`marks/<product>/lockup.svg`](marks)                                                                | Mark and name, on light surfaces; `lockup-on-dark.svg` for dark                         |
| [`marks/<product>/icons/`](marks)                                                                    | `favicon.ico`, `apple-touch-icon.png`, `icon-192.png`, `icon-512.png`                   |
| [`marks/<product>/png/`](marks)                                                                      | The mark and lockups as PNG, for tools that do not take SVG                             |
| [`marks/<product>/README.md`](marks)                                                                 | The idea behind the mark and its history                                                |
| [`tools/trace-mark.py`](tools/trace-mark.py)                                                         | Turns a drawn emblem into a clean mark in the frame                                     |
| [`tools/preview-marks.mjs`](tools/preview-marks.mjs)                                                 | Shows marks side by side, to judge a new one                                            |
| [`tools/build-lockups.py`](tools/build-lockups.py)                                                   | Builds the lockups from the marks and the font                                          |
| [`products.json`](products.json)                                                                     | Each product's homepage, repository, open source or commercial, and its oss-metrics key |
| [`brands/`](brands)                                                                                  | The Sebastian Software and Sebastian Consulting logos for the page's foot               |
| [`theme/`](theme)                                                                                    | `theme.css`, `ardo.js`, `tokens.json`, generated from `DESIGN.md`                       |
| [`tools/build-theme.py`](tools/build-theme.py)                                                       | Writes `theme/` from the tokens in `DESIGN.md`; `--check` runs in CI                    |
| [`tools/build-icons.mjs`](tools/build-icons.mjs)                                                     | Renders `icons/` and `png/` of every mark                                               |
| [`tools/build-site.py`](tools/build-site.py)                                                         | Builds the overview page and the brand packages that GitHub Pages publishes             |
| [`tools/sheet.mjs`](tools/sheet.mjs), [`tools/split-sheet.py`](tools/split-sheet.py)                 | Put all marks on one sheet for an image model, and cut its answer apart                 |
| [`frame/style-reference.png`](frame/style-reference.png)                                             | Three finished marks, to attach to an image prompt                                      |
| [`frame/sheet.png`](frame/sheet.png)                                                                 | All marks on one sheet, to send to an image model; rebuilt by `tools/sheet.mjs`         |
| [`.claude/skills/family-mark/`](.claude/skills/family-mark/SKILL.md)                                 | How a new mark is found, prompted, judged, and placed                                   |

## Using the theme

The repository is the npm package `kerameikos`, installed from GitHub until it is published:

```sh
pnpm add github:sebastian-software/kerameikos
```

```ts
import "kerameikos/theme.css"; // --kr-* colors, light and dark, Cinzel Hellenic, .kr-lockup
import { KERAMEIKOS_ARDO_THEME } from "kerameikos/ardo"; // <ArdoRoot theme={KERAMEIKOS_ARDO_THEME}>
import mark from "kerameikos/marks/tereon/mark-small.svg";
```

`theme.css` follows the system's dark mode unless the page sets `class="light"` or
`data-theme="light"`, and `class="dark"` (as Ardo sets it) or `data-theme="dark"` forces dark.
The lockup as live text:

```html
<a class="kr-lockup" href="/">
  <img class="kr-lockup-mark" src="mark-small.svg" alt="" />
  <span class="kr-lockup-name">Tereon</span>
</a>
```

The colors live in the front matter of [`DESIGN.md`](DESIGN.md). After changing one, run
`python3 tools/build-theme.py`; CI fails while `theme/` is out of date. After changing a mark,
run `NODE_PATH=$(npm root -g) node tools/build-icons.mjs <product>` to render its icons again.

## Products and live numbers

[`products.json`](products.json) lists for every member its homepage, its public repository,
whether it is open source (with its license) or commercial, and the repository name under which
[oss-metrics](https://github.com/sebastian-software/oss-metrics) reports it. The overview page
shows a badge and the links from it, and for open-source products it fetches the latest
release, stars, and downloads from `metrics.sebastian-software.com` in the browser. If that
fails, only the numbers are missing. oss-metrics lists public repositories with the
`oss-project` topic; a commercial product has `"metrics": null`. The file is also exported as
`kerameikos/products.json`. A new member needs an entry here, or the page build fails.

## The idea

Each product is named after a figure or a word from the ancient Greek world, and its mark shows
that figure or a scene from its story: something that stands for what the product does, in a
picture older than software. The marks are drawn like figures on Greek coins and vases, in navy
on paper with one bronze accent, and they share one ring.

What the marks so far have taught:

- **A figure or a scene carries a mark; a bare object does not.** A trumpet, a bowl, a scroll on
  its own stayed a prop. The herald sounding the trumpet worked at once.
- **A mark need not explain itself, but it must not point the wrong way.** Nobody reads
  "translation" from a youth writing on a tablet, and that is fine. A winged runner for a booking
  tool reads as delivery, and that is not.
- **Bronze marks the one thing the picture is about:** the flame, the trumpet, the new spoke. Where
  there is no such thing, it sits in a few small fittings.
- **Marks are made for large uses.** Website, marketing, and documents show them large, and
  their details count there. At favicon size the figure only has to remain recognizable.
- **A person doing something carries the family.** All marks show a figure in action, and the
  figures differ in age, gender, hair, and headgear so that the marks can be told apart at a glance.

## Members

| Product                                | Motif                                              | Stands for                                         |
| -------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| [Palamedes](marks/palamedes/README.md) | A youth writing the first letters, watching cranes | The inventor of letters                            |
| [Tereon](marks/tereon/README.md)       | A watchman on a roof who sees a beacon fire        | The one who keeps watch for a signal               |
| [Stentaro](marks/stentaro/README.md)   | A herald sounding a salpinx                        | The voice that carries what others say             |
| [Terminaro](marks/terminaro/README.md) | Two people shaking hands                           | An appointment as an agreement between two         |
| [Gramano](marks/gramano/README.md)     | Clio reading a scroll                              | The keeper of records who reads what is written    |
| [Curano](marks/curano/README.md)       | A wheelwright fitting a new spoke                  | Replacing one part so that the whole keeps running |
| [Agoros](marks/agoros/README.md)       | A woman at her market stall, with a shop sign      | The place where customers find a small business    |
| [Naos](marks/naos/README.md)           | A master builder setting a block into a wall       | Uniform building blocks that fit together          |

Each product's page records the idea behind its mark, what the colors mean, and what was tried
and dropped.

## Palette

The marks use three colors. The full palette for pages, including the darker interface bronze
for text and the dark variant, is in [`DESIGN.md`](DESIGN.md#colors).

| Name   | Value     | Use in the marks                              |
| ------ | --------- | --------------------------------------------- |
| Navy   | `#0E2A4D` | The mass of every motif                       |
| Bronze | `#BC8A45` | The ring and the accents inside a motif       |
| Paper  | `#FAF9F4` | The ground, skin, and lines cut into the navy |

## The frame

Everything is measured on a 240-unit square with its center at 120/120. One number sets the
rest: the ring width **W = 10**.

| Part       | Measure                                       | Rule                                                      |
| ---------- | --------------------------------------------- | --------------------------------------------------------- |
| Gold ring  | center line radius 112, width W               | bronze `#BC8A45`; drawn last, on top of everything        |
| Paper ring | radius 97 to 107, width W                     | stays empty; navy never touches gold                      |
| Window     | radius 97                                     | the motif lives inside it                                 |
| Top limit  | about y = 38, which is 1.5 W below the window | where the motif's mass ends at the top; see below         |
| Side limit | radius 92, which is W/2 inside                | parts of the motif that are not its base stay inside this |
| Base zone  | below y = 170                                 | here the motif may run to the window's edge and is cut    |

### The small version

Below 192 pixels a mark is shown in its small version, `mark-small.svg`: the same figure, pose,
and colors, redrawn with less detail. Hair is a few large shapes, garments lose their fold lines,
outlines are bolder, and the bronze parts are a little larger. The frame changes in one point:
**there is no paper ring.** The window reaches the gold ring (radius 107), and the motif fills it,
with its mass ending at about y = 28. At small sizes the empty ring would only make the motif
smaller.

## Placing a motif

1. **Stand it on its base.** A bust, a ground, a coastline: the base runs past the window's
   lower edge and is cut on it, as a figure stands on the ground line of an ancient coin.
2. **Size it from the base upward** until its mass reaches the top limit or its widest free
   part reaches the side limit, whichever comes first.
3. **Keep the rest free.** Head, flame, hand, or whatever the motif is about touches nothing
   and stays inside the side limit.
4. **Cut or clear, never almost.** A part either runs past the window and is cut, or keeps
   its distance. A part that nearly touches the window's edge is moved or redrawn.
5. **A cut stays open.** Where the window cuts a part, the part simply ends there, also when
   it is paper-colored like an arm. No contour is drawn along the window to close it.

### The top limit is judged by eye

The marks should end at the same height to the eye, not to the unit. What counts is where the
mass of a motif ends: a head, a crown of hair, a broad shape. That edge sits at about y = 38 and
does not rise above it as an area. A single narrow element, such as the tip of a flame, a curl,
or a trumpet, may rise above the limit, as long as it stays clear of the window's edge. A wide
motif that reaches the side limit first ends lower; Stentaro does, at y = 48.

## Drawing

- Navy `#0E2A4D` carries the mass. Paper `#FAF9F4` appears as lines cut out of it, never as
  an outline drawn around it.
- Bronze marks the one element the motif is about, such as a laurel, a flame, or a trumpet. A
  motif without such an element, like Terminaro's two figures, carries bronze in a few small
  fittings instead (clasps, a ribbon, bracelets).
- Flat shapes only: no gradients, shading, or texture.
- Cut-out lines are at least 2.5 units wide, so they stay open at 32 pixels.
- One main motif and at most one supporting plane such as ground or water.

## Versions

- **On paper:** as drawn.
- **On dark:** a paper disc of radius 117 lies under the mark; the motif is not inverted.
- **One color:** ring and motif in the same color; the paper ring keeps them apart.

## Making a mark from a drawing

The marks start as a drawn emblem (a raster image with its own ring).
[`tools/trace-mark.py`](tools/trace-mark.py) turns such an image into the three SVG versions:

1. It separates navy, bronze, and paper, fits the drawn ring, and drops it.
2. It smooths both shapes, removes specks and pinholes, and lets bronze run under the navy that
   borders it, so no paper shows between the two.
3. It traces the shapes with potrace into few, smooth curves and sets them into the frame,
   scaled relative to the drawn ring.

```sh
python3 tools/trace-mark.py drawing.png marks/<product> <Name> 0.96
```

The last number is the size relative to the drawing; a fifth and sixth move the motif right and
down in frame units. It needs Python with numpy, scipy, and Pillow, and the `potrace` and `npx`
commands. The drawing a mark was traced from lies beside it as `drawing.webp`. A file given in
`CLEAN_EDIT` can change the color areas before tracing; Gramano uses one.

## History

The frame was worked out in November 2026 on the Palamedes head and the first Tereon mark, a
signal tower on a coast. With the
motif standing on the window and its top 1.5 W below the window's edge, both marks carry about
the same weight at the same size.

- The first Palamedes mark, a laureled head, predates the frame. It was moved onto the frame
  and later replaced by the writing youth, so that it follows the same grammar as the others.
- Earlier assets for Agoros and Terminaro predate the frame and were replaced by new marks.
  Agoros runs as Vorort in the German market. The earlier files remain in the git history.
