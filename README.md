# Greek family brand assets

The shared identity of our products with ancient-Greek names: one typeface, one palette, and
marks that share one frame, a motif in a bronze ring. This repository is the single source for
them; product repositories copy what they need from here.

## Contents

| Path                                                       | What it is                                             |
| ---------------------------------------------------------- | ------------------------------------------------------ |
| [`CinzelHellenic-Regular.ttf`](CinzelHellenic-Regular.ttf) | The wordmark typeface                                  |
| [`frame/ring-template.svg`](frame/ring-template.svg)       | The frame with its guides                              |
| [`frame/ring-blank.svg`](frame/ring-blank.svg)             | The empty frame to draw a motif into                   |
| [`marks/<product>/mark.svg`](marks)                        | A mark on paper, transparent background                |
| [`marks/<product>/mark-on-dark.svg`](marks)                | The same with a paper disc under it, for dark surfaces |
| [`marks/<product>/mark-mono.svg`](marks)                   | The same in one color                                  |

## Members

| Product   | Motif                                   | Why                                                                                |
| --------- | --------------------------------------- | ---------------------------------------------------------------------------------- |
| Palamedes | A laureled head                         | Palamedes, to whom the Greeks ascribed letters and numbers                         |
| Tereon    | A signal tower with a flame, on a coast | The watchman's beacon in Aeschylus' "Agamemnon"; τηρέων, "the one who keeps watch" |
| Stentaro  | A herald sounding a salpinx             | Stentor, the herald of the Iliad whose voice carries like fifty men's              |
| Terminaro | Two people shaking hands                | The dexiosis of Attic reliefs: an appointment is an agreement between two people   |

Marks for Gramano and Curano are in preparation and will be added here.

## Palette

| Name   | Value     | Use                                        |
| ------ | --------- | ------------------------------------------ |
| Navy   | `#0E2A4D` | The mass of every motif, text              |
| Bronze | `#BC8A45` | The ring and the one accent inside a motif |
| Paper  | `#FAF9F4` | The ground, and lines cut into the navy    |

## The frame

Everything is measured on a 240-unit square with its center at 120/120. One number sets the
rest: the ring width **W = 10**.

| Part       | Measure                                 | Rule                                                      |
| ---------- | --------------------------------------- | --------------------------------------------------------- |
| Gold ring  | center line radius 112, width W         | bronze `#BC8A45`; drawn last, on top of everything        |
| Paper ring | radius 97 to 107, width W               | stays empty; navy never touches gold                      |
| Window     | radius 97                               | the motif lives inside it                                 |
| Top limit  | y = 38, which is 1.5 W below the window | the motif's highest point                                 |
| Side limit | radius 92, which is W/2 inside          | parts of the motif that are not its base stay inside this |
| Base zone  | below y = 170                           | here the motif may run to the window's edge and is cut    |

## Placing a motif

1. **Stand it on its base.** A bust, a ground, a coastline: the base runs past the window's
   lower edge and is cut on it, as a figure stands on the ground line of an ancient coin.
2. **Size it from the base upward** until its highest point reaches the top limit or its widest
   free part reaches the side limit, whichever comes first.
3. **Keep the rest free.** Head, flame, tower, or whatever the motif is about touches nothing
   and stays inside the side limit.
4. **Cut or clear, never almost.** A part either runs past the window and is cut, or keeps
   its distance. A part that nearly touches the window's edge is moved or redrawn.

## Drawing

- Navy `#0E2A4D` carries the mass. Paper `#FAF9F4` appears as lines cut out of it, never as
  an outline drawn around it.
- Bronze marks the one element the motif is about, such as a laurel or a flame, and nothing
  else inside the window.
- Flat shapes only: no gradients, shading, or texture.
- Cut-out lines are at least 2.5 units wide, so they stay open at 32 pixels.
- One main motif and at most one supporting plane such as ground or water.

## Versions

- **On paper:** as drawn.
- **On dark:** a paper disc of radius 117 lies under the mark; the motif is not inverted.
- **One color:** ring and motif in the same color; the paper ring keeps them apart.

## History

The frame was worked out in November 2026 on the Palamedes head and the Tereon beacon. With the
motif standing on the window and its top 1.5 W below the window's edge, both marks carry about
the same weight at the same size.

- The Palamedes mark here is the earlier one, moved onto the frame: wider ring, paper ring, the
  bust cut on the window. Its inner lines are painted in paper color, not cut out, so on a
  surface that is not paper-colored use `mark-on-dark.svg`.
- Earlier assets for Agoros, Relanto, Stellara, and Terminaro predate the frame and were
  removed. Agoros continues as Vorort under its own identity; Relanto and Stellara are not
  developed further; Terminaro has a new mark. They remain in the git history.
