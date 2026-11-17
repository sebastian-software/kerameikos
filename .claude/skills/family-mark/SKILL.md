---
name: family-mark
description: >-
  Design, redraw, or review a mark (logo emblem) for a product of the Greek
  product family: Palamedes, Tereon, Stentaro, Terminaro, Gramano, Curano,
  Agoros, Naos, and any new member. Use whenever someone wants a logo, mark, icon,
  or emblem for one of these products or for a new product with a Greek or
  Latin name, asks for a motif or metaphor for such a mark, wants a prompt for
  an image model in the family's style, sends a generated emblem to be judged
  or set into the ring frame, or wants an existing mark traced, cleaned,
  resized, or repositioned. Covers finding the metaphor, writing and revising
  the image prompt, judging results against the family, tracing to clean SVG,
  placement in the frame, and recording the decision.
---

# Family mark

How a mark for the Greek product family is made, from the first idea to the files in this
repository. The frame rule and the reasons behind each existing mark are in the repository
itself: read [`README.md`](../../../README.md) and the page of the mark closest to the new one
under `marks/<product>/README.md` before you start. This skill holds what those pages do not:
how to get there.

The work is a conversation with the owner. They generate the images with an image model and
send them back; you propose metaphors, write the prompts, judge what comes back, and turn the
chosen drawing into files. Most marks took five to ten rounds. Expect that, and keep each round
short.

## The steps

1. **Understand the product and its name.** Read the product's README. Find out what the name
   comes from, and say so if the repository does not; do not present a guessed etymology as
   fact.
2. **Find the metaphor** and agree on it before writing a prompt. See below.
3. **Write the prompt** from the template in
   [`references/prompts.md`](references/prompts.md).
4. **Judge each result in the frame, beside the family**, not on its own. See below.
5. **Revise:** a targeted edit if the idea holds, a new metaphor if it does not.
6. **Trace and place** the chosen drawing with `tools/trace-mark.py`.
7. **Record** the mark, its page, and the member row, and open a pull request.

## Finding the metaphor

The family's idea: each product is named after a figure or word from the ancient Greek world,
and its mark shows that figure or a scene from its story, something that stands for what the
product does in a picture older than software.

Offer two or three candidates, name the risk of each, and recommend one. What the rounds so far
have shown:

- **A figure using an object carries a mark; the object alone does not.** A trumpet, a scroll, a
  bowl, a sundial each stayed a prop. The herald sounding the trumpet and the muse reading the
  scroll worked on the first try. When an object motif fails, ask who would hold it.
- **Single pieces of architecture fail.** Two columns and a doorway from the front are a bank
  portal, however close the crop. One column on a mound with a bronze piece on top is a lighthouse,
  the silhouette of the first Tereon mark. A building works only as a small thing in someone's hand.
- **A mark need not explain itself, but it must not point the wrong way.** Nobody reads
  "translation" from the Palamedes head, and that is fine. But a winged runner reads as
  delivery, a ship under sail as shipping, scales as justice, a bowl with a snake as a
  pharmacy, a forge as a build tool. Check every candidate for the reading it already has
  today, especially in software.
- **Show what the product gives its user, at the right end of the chain.** A component library
  gives building blocks, not the finished temple. A website for a small business gives the shop
  sign, not the goods on the table.
- **Do not make it more literal than the product.** A fruit seller behind heaps of fruit became
  a food label, and the product is not for fruit sellers. Mixed wares say "any trade".
- **If the product is about people meeting, show people.** Terminaro went through a water clock and
  a sundial before the handshake of two people; the owner's sentence "every appointment is an
  agreement between two people" was the metaphor.
- **Check against the family before proposing.** Two marks must not share a silhouette. Keep heads,
  figures, and scenes mixed, and vary the figures in age, gender, and hair: the family has a
  laureled youth, a curly-haired herald, a helmeted watchman, a man with long tied hair, a bearded
  elder, and women with a knot and with open hair. A second craftsman with a tool needs a clearly
  different object and pose.
- **When three correction rounds have not fixed a picture, the metaphor is wrong.** Say so and
  step back. Ask whether the owner dislikes the execution or the idea; they usually know.

## Writing the prompt

The template and worked examples are in [`references/prompts.md`](references/prompts.md). The
reasons behind its parts:

- **Attach the style reference.** `frame/style-reference.png` shows three finished figure marks. It
  fixes line quality and detail better than any description. Regenerate it with
  `tools/preview-marks.mjs --reference` when better examples exist.
- **One emblem per run.** A sheet of four gives each a quarter of the resolution, and the
  model makes them alike: it once gave all four the same stone pedestal.
- **Figures in profile, as half-figures cut at the waist.** This is the coin convention the
  family follows. A frontal face was tried: its expression tips over at small sizes, and the
  result looked like a product label.
- **Say little about hands.** Detailed instructions about which arm comes from where, thumbs,
  and forearms made the hands worse in every run. "Holds the tablet in his left hand and writes
  with his right" was enough. If one hand still goes wrong, hide it while tracing.
- **Say that skin is paper-colored with navy contours.** Hair, garments, and objects are navy.
  It keeps hands and faces readable and sets the figure marks apart from the dark Palamedes
  head.
- **The object is in the hand and apart from where it goes.** A spoke already in the wheel
  showed a man holding a wheel. The same spoke held in front of a visible gap showed him
  fitting it.
- **Name the bronze parts and close with "nothing else is bronze".** Bronze marks what the
  picture is about. Where a figure has no such object, give it small fittings: a shoulder
  clasp, a hair ribbon.
- **Say where the motif ends:** cut by the circle at the bottom, where the garment or ground
  forms a broad base; free everywhere else; ending a ring's width inside the bronze ring. Tell
  the model that a body runs straight down to the cut, or garments flare and make a waist.
- **List what must not appear.** No pedestal, no floor, no background objects, and the objects
  of the other marks (no trumpet, no scroll, no laurel). The model otherwise borrows them from
  the reference.
- **No dark wall surfaces and no thin frames.** Every mark stands free on paper. A filled wall
  made the mark a dark disc; a door drawn as a thin frame looked flimsy beside the others.
- **Scenes in strict side view.** For a scene with several things, ask for flat profile on one
  ground line, no perspective, no view from above. Otherwise it is unclear where a figure
  stands.
- **No letters.** A sign carries two or three strokes instead of an inscription.
- **Give sizes in relation:** "about as wide as his head", "two thirds of the medallion's
  height". The model otherwise shrinks the thing that matters.

For a correction, send the last image back with an edit prompt: "Keep X, Y, Z exactly as in
the attached image. Change only these things:" and a numbered list. This holds faces and hands
well. Change few things per round, and expect that an edit can make things worse; keep the
earlier image.

The images so far were made with **Codex Sol 6.1 High**, at 1254 by 1254 pixels. Note the model
on a mark's page if a different one is used, because prompts may need adjusting.

## Judging a result

Trace it roughly and look at it in the frame beside the family before saying anything:

```sh
python3 tools/trace-mark.py drawing.png /tmp/try <Name> 1.0
NODE_PATH=$(npm root -g) node tools/preview-marks.mjs /tmp/try.png /tmp/try/mark.svg marks/*/mark.svg
```

Then look at the picture, and ask:

- **Would someone who does not know the idea see it?** You know what it is meant to show, and
  that makes you read it kindly. A hull seen close was "obviously a ship" to the one who wrote
  the prompt and a curved brick wall to the owner. Describe what is drawn, not what was asked
  for.
- **Is something happening?** A figure that only holds a thing is weaker than one doing
  something with it.
- **Does it share a silhouette with another mark?** Compare them side by side.
- **How large is the figure?** Two figures or a scene make each part small. Say so; it may be
  worth it.
- **Which size matters?** The marks are used mostly large, on websites and in marketing, where
  their details count. At favicon size the figure only has to remain recognizable; do not judge
  or reject a mark by what disappears at 32 pixels.
- **Where is the bronze, and is it the right thing?**
- **Is it heavy or light beside the others?** A slim figure can be the lightest mark; a filled
  background the heaviest.

Report strengths and weaknesses plainly, including the ones the owner did not ask about, and
say which you would fix and how. The owner's eye has been right each time it disagreed.

## Tracing and placing

`tools/trace-mark.py` turns a drawing into `mark.svg`, `mark-on-dark.svg`, and `mark-mono.svg`:

```sh
python3 tools/trace-mark.py drawing.png marks/<product> <Name> <factor> [dx] [dy]
```

`factor` is the size relative to the drawn ring, `dx` and `dy` move the motif right and down
in frame units. It prints where the top and the outermost parts end up. It needs Python with
numpy, scipy, and Pillow, and the `potrace` and `npx` commands.

- **Take the drawing over as drawn.** Do not rescale a motif to a rule if that cuts into hair
  or hands; scale the whole motif a few percent instead, or move it.
- **The paper ring stays empty.** If free parts reach past radius 97, reduce the factor until
  they are clear, or move the motif so that they are either clear or plainly cut.
- **The top is judged by eye.** The mass of the motif, a head or a crown of hair, ends at about
  y = 38. A narrow element may rise above it. A wide motif that reaches the side first ends
  lower; note that on its page.
- **A cut stays open.** Where the window cuts a paper-colored arm, the arm simply ends. Do not
  close it with a contour.
- **Change colors on the tracing masks, never in the image.** Recoloring pixels leaves ragged
  edges that trace into rough lines. Put the change into a small file and pass it as
  `CLEAN_EDIT`; `marks/gramano/trace-edit.py` is the example.
- **Two drawings of the same figure can be combined** when head and body are congruent, for
  instance the composition of one with the bronze details of the other.
- **Look at the result enlarged, beside the drawing.** The owner checks line ends and joins at
  high magnification. Compare fine details such as hands, fingernails, and faces with the same
  crop of the drawing: the default smoothing can erase them. If lines are rough, raise
  `CLEAN_SIGMA`; if fine lines vanish, lower it (Palamedes uses 0.8).
- **Check what the window cuts.** A motif scaled up a few percent can lose a hand or the edge of
  a garment at the window. Describe the traced mark, not the drawing you remember.

## Recording the mark

A mark is done when the repository holds:

- `marks/<product>/mark.svg`, `mark-on-dark.svg`, `mark-mono.svg`, and `drawing.webp`, the
  drawing it was traced from;
- `marks/<product>/README.md` with the product in one line, the idea, what navy, paper, and
  bronze are in this mark, the decisions that a redrawing must keep, what was tried and
  dropped and why, and the placement. The pages of Terminaro, Curano, and Agoros are the
  fullest examples;
- a row in the members table of the main README.

Write the "tried and dropped" list while the rounds are fresh. It is the part that saves the
next mark from repeating them. Ask before adding a mark the owner has not approved in so many
words, and open the pull request as a draft.
