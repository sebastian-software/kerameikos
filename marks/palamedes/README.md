# Palamedes

**Product:** translation and localization tooling for web applications.

## The idea

Palamedes is the hero to whom the Greeks ascribed the invention of letters, numbers, and
counting. A product that carries text from one language into another is named after the man
who, in the story, gave the Greeks writing in the first place.

A later tradition says he found the letters by watching the flight of cranes, whose formations
draw shapes in the sky; the Roman poet Martial calls the crane "the bird of Palamedes". The mark
shows that moment: he looks up at the cranes and writes the first letters on a wax tablet.

## The mark

A young man in profile with a laurel wreath, looking up at three cranes flying in a loose V
while he writes with a stylus on an open wooden tablet held against his body.

- **Navy:** his hair and cloak, the tablet's frame, and the stylus.
- **Paper color:** face, neck, arm, and hand, and the wax of the tablet.
- **Bronze:** the laurel, the cranes, and the marks on the wax: the honor, the cause, and the
  letters.

Three decisions should survive any redrawing:

- **He writes, and the marks are visible on the tablet**, slanted, as one sees a notebook that
  someone holds while writing. The letters are what the mark is about at large sizes; at small
  sizes the figure, the tablet, and the cranes carry it.
- **The cranes are a small detail at different distances,** not a main motif. As large birds
  they turned the picture into bird-watching.
- **The tablet is an ancient wax tablet,** not a dark rectangle with rounded corners, which reads
  as a tablet computer.

## What was tried and dropped

- **The laureled head alone:** the first mark of the family, drawn before the ring frame. It
  was the only mark in which nobody does anything.
- **Six large cranes as the main motif, with the writer below:** the birds took over, and the
  picture read as nature or migration.
- **A single framed tablet held upright:** a person with a tablet computer and a pen.
- **Long prompts that described his hands in detail:** each run drew the holding hand worse,
  with an arm that came out of his belly or a third hand under the tablet. A short prompt that
  only said "holds the tablet in his left hand and writes with his right" produced plausible
  hands.
- **A frontal torso holding a closed, dark book:** he no longer wrote, and the book read as a
  leather folder.

## Placement and tracing

Taken over as drawn, scaled to 96% and moved 4 units down. The drawing showed a supporting hand
poking out under the tablet with no room for its forearm; [`trace-edit.py`](trace-edit.py)
removes it, which [`tools/trace-mark.py`](../../tools/trace-mark.py) applies while tracing
(`CLEAN_EDIT`). The tablet now rests against his cloak, held by a hand hidden behind it.
