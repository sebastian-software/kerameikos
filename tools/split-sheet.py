"""Cut a sheet of eight emblems, as returned by an image model, into one image per product.

usage: python3 tools/split-sheet.py sheet.png outdir
The emblems are found by their bronze rings, sorted into rows and columns, and saved as
<product>.png in the order of tools/sheet.mjs (palamedes, tereon, stentaro, terminaro, gramano,
curano, agoros, naos), each with a margin of paper around it. Trace each one afterwards, for
example: CLEAN_SMALL=1 python3 tools/trace-mark.py outdir/naos.png marks/naos Naos 1.02 0 2
"""
import sys
from pathlib import Path
import numpy as np
from PIL import Image
from scipy import ndimage

ORDER = ["palamedes", "tereon", "stentaro", "terminaro", "gramano", "curano", "agoros", "naos"]
src, out = Path(sys.argv[1]), Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)
im = Image.open(src).convert("RGB")
a = np.asarray(im).astype(int)
r, g, b = a[..., 0], a[..., 1], a[..., 2]
bronze = (r - b > 55) & (r > 140) & (g < 200)
lab, n = ndimage.label(ndimage.binary_closing(bronze, iterations=2))
boxes = ndimage.find_objects(lab)
sizes = ndimage.sum(bronze, lab, range(1, n + 1))
# A ring's box is nearly square and large; keep the eight largest such components.
cands = []
for i, (sl, sz) in enumerate(zip(boxes, sizes)):
    h, w = sl[0].stop - sl[0].start, sl[1].stop - sl[1].start
    if min(h, w) > 0.1 * min(im.size) and 0.8 < h / w < 1.25:
        cands.append((sz, sl))
cands = sorted(cands, key=lambda c: -c[0])[:len(ORDER)]
if len(cands) != len(ORDER):
    sys.exit(f"found {len(cands)} rings, expected {len(ORDER)}")
rings = [c[1] for c in cands]
rings.sort(key=lambda s: s[0].start)
rows = [sorted(rings[:4], key=lambda s: s[1].start), sorted(rings[4:], key=lambda s: s[1].start)]
for product, sl in zip(ORDER, rows[0] + rows[1]):
    y0, y1, x0, x1 = sl[0].start, sl[0].stop, sl[1].start, sl[1].stop
    m = int(0.06 * (x1 - x0))
    crop = im.crop((max(0, x0 - m), max(0, y0 - m), min(im.width, x1 + m), min(im.height, y1 + m)))
    crop.save(out / f"{product}.png")
    print(product, crop.size)
