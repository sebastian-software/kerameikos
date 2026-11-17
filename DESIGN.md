---
name: Greek product family
description: >-
  The shared visual identity of the products with ancient-Greek names: marks, lockups,
  typeface, palette, and the page style their websites share. Taken from palamedes.dev and the
  Tereon homepage, which both implement it.
colors:
  paper: "#faf9f4"
  parchment: "#f3efe3"
  mist: "#e8edf2"
  ink: "#0e2a4d"
  ink-2: "#3f5471"
  ink-3: "#526176"
  hair: "#ddd6c6"
  hair-2: "#e8e2d3"
  listing: "#fdfcf8"
  accent: "#866026"
  accent-2: "#6f4f1e"
  accent-wash: "#f4ecda"
  on-accent: "#ffffff"
  mark-navy: "#0e2a4d"
  mark-bronze: "#bc8a45"
  mark-paper: "#faf9f4"
colors-dark:
  paper: "#0c1724"
  parchment: "#111e2e"
  mist: "#15263a"
  ink: "#ece6d6"
  ink-2: "#bcc4cf"
  ink-3: "#a3afbe"
  hair: "#2a3d55"
  hair-2: "#223349"
  listing: "#0f1c2b"
  accent: "#d2a660"
  accent-2: "#e2bd80"
  accent-wash: "#2a2416"
  on-accent: "#0c1724"
typography:
  wordmark:
    fontFamily: "Cinzel Hellenic, Times New Roman, serif"
    fontWeight: 400
    textTransform: uppercase
    letterSpacing: "0.16em"
    lineHeight: 1
  display:
    fontFamily: "Cinzel Hellenic, Times New Roman, serif"
    fontSize: "clamp(2.45rem, 6.2vw, 4.75rem)"
    fontWeight: 400
    lineHeight: 1.15
  headline:
    fontFamily: "Cinzel Hellenic, Times New Roman, serif"
    fontSize: "clamp(1.9rem, 3.7vw, 3.1rem)"
    fontWeight: 400
    lineHeight: 1.15
  lede:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "clamp(1.0625rem, 0.95rem + 0.4vw, 1.3125rem)"
    lineHeight: 1.65
  body:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "1rem"
    lineHeight: 1.6
  eyebrow:
    fontFamily: "ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "0.6875rem"
    textTransform: uppercase
    letterSpacing: "0.22em"
  code:
    fontFamily: "ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontVariantNumeric: tabular-nums
lockup:
  markHeight: "1em of the lockup"
  nameSize: "0.625 x mark height"
  gap: "0.35 x mark height"
  webHeader: "mark 2rem, name 1.25rem, gap 0.7rem"
layout:
  lede: "42rem"
  band-header: "54rem"
  rules: "1px hairlines"
  corners: "0 for marketing actions; the documentation framework keeps its own"
---

# Design system: the Greek product family

This is the shared identity of our products with ancient-Greek names: Palamedes, Tereon,
Stentaro, Terminaro, Gramano, Curano, Agoros, and Naos. It covers what makes them recognizable
as one family: the marks, the lockups, the typeface for their names, the palette, and the page
style of their websites. Each product's own content, artwork, and product UI stay with the
product.

Ground truth is the shipped work: [palamedes.dev](https://palamedes.dev) (its
[ADR-011](https://github.com/sebastian-software/palamedes/blob/main/adr/011-editorial-visual-brand-system.md)
and `site/app/ardo-theme.ts`) and the Tereon homepage (`site/app/theme.ts`), which adds the dark
variant. The front matter copies their tokens; the prose says where each goes. The marks and
their frame are described in the [README](README.md).

## Overview

**North star: "Inscription and ledger, opened up."** A page reads like a well-set inscription
above an editorial page that explains before it proves. Warm paper, navy ink, one bronze
accent, inscription-scale capitals for names and headlines, readable body text, hairline rules,
and tabular numbers. Confidence comes from clear explanation and real evidence, not from visual
loudness.

- One palette for marks, pages, and documentation; light first, with a dark "night watch"
  variant.
- Cinzel Hellenic for product names and marketing headlines only; the reader's system face for
  everything that is read.
- Structure from hairlines and bands, not from boxes and shadows.
- Bronze is spent deliberately: on the one thing that matters, never as decoration.

## The marks

Every product has a mark: a figure from the Greek world doing something that stands for what
the product does, drawn like a figure on a coin or vase, in navy on paper with bronze accents,
inside one shared ring. The frame rule, the members, and the reasons behind each mark are in
the [README](README.md); each product's page under `marks/<product>/` records its idea and its
history.

| File                 | Use                                                                                |
| -------------------- | ---------------------------------------------------------------------------------- |
| `mark.svg`           | On paper or any light surface, transparent background                              |
| `mark-on-dark.svg`   | On dark surfaces, with a paper disc under the mark; the motif is never inverted    |
| `mark-mono.svg`      | Where only one color is possible: embossing, stamps, single-color print            |
| `mark-small.svg`     | Below 192 pixels: favicons, app icons, avatars; also `-on-dark` and `-mono`        |
| `lockup.svg`         | Mark and name side by side, on light surfaces                                      |
| `lockup-on-dark.svg` | Mark and name side by side, on dark surfaces                                       |
| `icons/`             | `favicon.ico`, `apple-touch-icon.png`, and the manifest icons, from the small mark |
| `png/`               | The full mark and the lockups as PNG, for tools that do not take SVG               |

Every product has a brand package on the
[overview page](https://sebastian-software.github.io/kerameikos/): a zip with all of these
files, the typeface, and a short guide with the HTML for a site's head.

**Icons** use the small mark at every file size, because they are seen at icon size: the
favicon and the manifest icons with the paper disc, since tabs and launchers can be light or
dark; the touch icon as the small mark on an opaque paper square with room around it, since the
system rounds its corners.

- **Clear space:** at least half the mark's height on every side, free of text and edges.
- **Which version at which size:** the full mark from 192 pixels up; below that the small
  version, which keeps the figure and pose with less detail and without the paper ring inside
  the gold ring. The small version works down to 32 pixels; favicons at 16 pixels use it too.
- **Minimum size:** 24 pixels for a mark alone, 20 pixels mark height in a lockup, except for
  favicons.
- **Never** recolor a mark, put it on a photograph without the paper disc, stretch it, rotate
  it, add an outline or shadow, or crop the ring.

## Lockup and product name

The product name is always set in **Cinzel Hellenic**, uppercase, letter-spaced at 0.16 em, at
regular weight. Cinzel Hellenic is Cinzel with a restrained Greek tint (an A without crossbar,
among others); it ships here as `CinzelHellenic-Regular.ttf` and `.woff2` under the SIL Open
Font License (`OFL.txt`).

The lockup sets the mark to the left of the name. **The mark in a lockup is always the small
version** (`mark-small.svg`): beside a name the mark is shown at header or button size, where
the full mark's detail blurs.

- The name's font size is 0.625 of the mark's height, so the capitals sit centered on the mark.
- The gap between mark and name is 0.35 of the mark's height.
- In a web header that is a 2 rem mark, a 1.25 rem name, and a 0.7 rem gap.
- On dark surfaces the mark uses its paper disc (`mark-small-on-dark.svg`) and the name is set
  in paper color.

`tools/build-lockups.py` builds both lockups for every product from the small mark and the font, with
the name converted to outlines. Use these files wherever the font cannot be loaded, such as in
emails, slides, and documents; on websites, set the name as live text in the font so that it
stays accessible.

A product name inside running text is written normally ("Palamedes"), never in capitals and
never in the display face.

## Colors

The palette has two bronzes, and the difference matters:

- **Mark bronze `#bc8a45`** is the bronze of the marks and of large graphic elements. On paper it
  reaches only 2.9:1 contrast, so it never carries text or thin lines on its own.
- **Accent bronze `#866026`** is the bronze of interfaces: links, primary actions, focus rings,
  the kicker above a headline. It holds 5.4:1 on paper and 5.7:1 under white text.

| Token                | Light                | Dark                 | Use                                                       |
| -------------------- | -------------------- | -------------------- | --------------------------------------------------------- |
| `paper`              | `#faf9f4`            | `#0c1724`            | The ground of every page                                  |
| `parchment`          | `#f3efe3`            | `#111e2e`            | Alternate bands, sidebars, the footer                     |
| `mist`               | `#e8edf2`            | `#15263a`            | A cool band for contrast with parchment; tracks of charts |
| `ink`                | `#0e2a4d`            | `#ece6d6`            | Text and headings (13.7:1 on paper)                       |
| `ink-2`              | `#3f5471`            | `#bcc4cf`            | Ledes and secondary text (7.3:1)                          |
| `ink-3`              | `#526176`            | `#a3afbe`            | Captions, labels, metadata (5.5:1 on parchment)           |
| `hair`, `hair-2`     | `#ddd6c6`, `#e8e2d3` | `#2a3d55`, `#223349` | Rules and borders; they divide, they never box            |
| `listing`            | `#fdfcf8`            | `#0f1c2b`            | The ground of code listings: printed, not a dark editor   |
| `accent`, `accent-2` | `#866026`, `#6f4f1e` | `#d2a660`, `#e2bd80` | Interaction and emphasis, and its hover state             |
| `accent-wash`        | `#f4ecda`            | `#2a2416`            | A selected row, a highlighted line                        |
| `on-accent`          | `#ffffff`            | `#0c1724`            | Text on a bronze action                                   |

These tokens exist as code in `theme/`: `theme.css` as `--kr-*` custom properties, `ardo.js` as
the Ardo theme with the names Ardo uses (`paper` is `bg`, `accent` is `brand`, `listing` is
`codeBg`), and `tokens.json`. They are generated from this file's front matter by
`tools/build-theme.py`; change a color here, never there.

Terminal green and amber are reserved for real CLI output. No gradients, no glow, no purple.

## Typography

- **Cinzel Hellenic** for product names, page titles, and section headlines, at weight 400.
  It is a display face: never for body text, buttons, navigation, or anything below about
  1.25 rem.
- **The system UI face** for everything that is read: ledes, body text, navigation, labels.
- **The system monospace face** for code, numbers in tables and specimens (tabular figures),
  eyebrows, and file names.
- No third-party font service is contacted; Cinzel Hellenic is self-hosted with
  `font-display: swap`.

The front matter gives the sizes. Headlines wrap balanced (`text-wrap: balance`); ledes keep a
measure of 42 rem.

## Layout

- Pages are built from full-width **bands** that alternate paper, parchment, and mist,
  separated by one-pixel rules. Content inside a band is centered at a readable measure.
- **Hairlines, not boxes:** structure comes from rules and a framed grid with one-pixel gaps.
  Cards with shadows are not part of the style.
- The documentation framework (Ardo) owns the shell: header, sidebar, outline, gutters,
  breakpoints, and focus. Products theme it through its public options and do not restyle its
  internals.
- A site links to the family once, in its header, rather than listing sibling products.

## Shape, elevation, and motion

- Marketing actions are square, bronze, and flat: no radius, no shadow.
- Elevation is reserved for small badges, such as integration logos, with a fine border and a
  subtle shadow.
- Motion is optional and small; under `prefers-reduced-motion` it is off. Scroll reveals and
  ornamental meanders are not part of the style.

## Imagery

- **Product specimens are the imagery:** real code, real output, real screenshots of the
  product, produced by the site's own scripts.
- **The mark is the only illustration of the brand.** Additional artwork must explain content,
  not fill space. A product may use one licensed icon family consistently (Palamedes uses
  Streamline Sharp Duo, colored with ink and accent); families are not mixed.
- Third-party logos identify integrations, keep their own geometry, and are not shown as
  customers.

## Voice

Precise, calm, verifiable. Name the reader's situation and the benefit in plain words first,
then show the work. Every number on a page is backed by a checked-in measurement and shows its
scope. No "seamless", no "blazingly fast" without a measurement beside it. Copy is written in US
English.

## Do and don't

### Do

- Use one bronze accent per view, on the thing that matters.
- Set product names in Cinzel Hellenic capitals, everything read in the system face.
- Use the mark's dark version with its paper disc on dark surfaces.
- Show real product output and say where numbers come from.
- Keep contrast at WCAG AA or better; check every new color pair.

### Don't

- Generic SaaS looks: gradient heroes, glassmorphism, rounded cards with drop shadows,
  dark mode with glow.
- The unthemed look of the documentation framework bleeding into the brand surface.
- Mark bronze for text or thin lines on paper.
- Cinzel Hellenic for body text, buttons, or long headlines in small sizes.
- A second palette in a product's stylesheet; new colors become tokens first.

## Accessibility

- Text meets at least 4.5:1, large display text at least 3:1; the token table lists the
  measured ratios.
- Focus is always visible, in the accent color.
- Color is never the only carrier of meaning.
- Navigation and search are reachable by keyboard.
- Content reads without JavaScript where prerendering allows, and pages reflow on narrow
  screens without horizontal scrolling.
