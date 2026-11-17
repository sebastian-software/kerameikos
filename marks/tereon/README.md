# Tereon

**Product:** cookieless web analytics: what people read, not who they are.

## The idea

Tereon is Greek, τηρέων, "the one who keeps watch". Aeschylus' "Agamemnon" opens with a watchman
who has waited on the palace roof for a year for one signal: the beacon that announces the fall
of Troy, passed from mountain to mountain across the sea. He watches for a signal and reports
it; he does not follow anyone. That is the stance of the product. A browser's analytics message
is also called a beacon.

## The mark

The watchman on the palace roof, leaning on its stone edge and shading his eyes with one hand
as he looks across the sea at the beacon fire burning on a distant mountain.

- **Navy:** his helmet and cloak, the roof edge, the sea, and the mountain.
- **Paper color:** face, arms, and hands, and the waves and moulding lines.
- **Bronze:** the beacon fire, the signal itself, and his shoulder clasp.

Three decisions should survive any redrawing:

- **The fire is large,** about as tall as his head, and the brightest thing in the picture. As
  a small flame at the edge the story was lost.
- **He wears a helmet, without a headband or curls.** With curly hair and a headband he was a
  second Stentor.
- **The roof edge runs across the whole width in front of the sea.** In the drawing it stopped
  mid-picture and roof and sea merged into one dark area; `trace-edit.py` continues it.

## What was tried and dropped

- **A Greek tau drawn as a surveyor's rod:** the first proposal; abstract and without a story.
- **The watchman's head alone:** too close to the Palamedes head.
- **A chain of three beacons on three hills:** true to the story, but three small fires
  scatter; none of them carries the mark.
- **A stone signal tower with a flame, on a coast:** the mark from November 2026 until the
  family had grown. It read well at small sizes, but it was the only mark without a person in a
  family of figures, and a single tower with bronze on top is a lighthouse. The watchman keeps
  its sea, mountain, and fire.
- **The watchman with curly hair, a headband, a beard, and a small fire:** the herald of
  Stentaro once more, and the fire too small to carry the picture.

## Placement and tracing

Taken over as drawn, scaled to 97% and moved 1 unit down. The roof edge is continued to the
right edge by [`trace-edit.py`](trace-edit.py), which
[`tools/trace-mark.py`](../../tools/trace-mark.py) applies while tracing (`CLEAN_EDIT`).
