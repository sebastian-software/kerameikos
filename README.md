# Greek family brand assets

The shared identity of our products with ancient-Greek names: one typeface, one palette, and
marks that share one frame, a motif in a bronze ring. [`DESIGN.md`](DESIGN.md) is the style
guide: lockups, typography, colors, layout, and voice. An overview page with every file to
download is published to GitHub Pages from `main` by `.github/workflows/pages.yml`. This repository is the single source for
them; product repositories copy what they need from here.

## Contents

| Path                                                                                                 | What it is                                                                      |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [`DESIGN.md`](DESIGN.md)                                                                             | The style guide: lockups, type, colors, layout, voice                           |
| [`CinzelHellenic-Regular.ttf`](CinzelHellenic-Regular.ttf), [`.woff2`](CinzelHellenic-Regular.woff2) | The typeface for product names, under the [SIL OFL](OFL.txt)                    |
| [`frame/ring-template.svg`](frame/ring-template.svg)                                                 | The frame with its guides                                                       |
| [`frame/ring-blank.svg`](frame/ring-blank.svg)                                                       | The empty frame to draw a motif into                                            |
| [`marks/<product>/mark.svg`](marks)                                                                  | A mark on paper, transparent background                                         |
| [`marks/<product>/mark-on-dark.svg`](marks)                                                          | The same with a paper disc under it, for dark surfaces                          |
| [`marks/<product>/mark-mono.svg`](marks)                                                             | The same in one color                                                           |
| [`marks/<product>/mark-small.svg`](marks)                                                            | The small version, below 128 pixels; also `-on-dark` and `-mono`                |
| [`marks/<product>/lockup.svg`](marks)                                                                | Mark and name, on light surfaces; `lockup-on-dark.svg` for dark                 |
| [`marks/<product>/README.md`](marks)                                                                 | The idea behind the mark and its history                                        |
| [`tools/trace-mark.py`](tools/trace-mark.py)                                                         | Turns a drawn emblem into a clean mark in the frame                             |
| [`tools/preview-marks.mjs`](tools/preview-marks.mjs)                                                 | Shows marks side by side, to judge a new one                                    |
| [`tools/build-lockups.py`](tools/build-lockups.py)                                                   | Builds the lockups from the marks and the font                                  |
| [`tools/build-site.py`](tools/build-site.py)                                                         | Builds the asset overview page that GitHub Pages publishes from `main`          |
| [`tools/sheet.mjs`](tools/sheet.mjs), [`tools/split-sheet.py`](tools/split-sheet.py)                 | Put all marks on one sheet for an image model, and cut its answer apart         |
| [`frame/style-reference.png`](frame/style-reference.png)                                             | Three finished marks, to attach to an image prompt                              |
| [`frame/sheet.png`](frame/sheet.png)                                                                 | All marks on one sheet, to send to an image model; rebuilt by `tools/sheet.mjs` |
| [`.claude/skills/family-mark/`](.claude/skills/family-mark/SKILL.md)                                 | How a new mark is found, prompted, judged, and placed                           |

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

Below 128 pixels a mark is shown in its small version, `mark-small.svg`: the same figure, pose,
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
- Earlier assets for Agoros, Relanto, Stellara, and Terminaro predate the frame and were
  removed. Agoros, which runs as Vorort in the German market, has a new mark; Relanto and
  Stellara are not developed further; Terminaro has a new mark. They remain in the git history.
