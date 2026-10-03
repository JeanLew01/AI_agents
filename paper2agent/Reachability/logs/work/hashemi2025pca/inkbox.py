#!/usr/bin/env python3
"""inkbox.py PAGE X0 Y0 X1 Y1 : ink bounding box (PDF points) inside the region, and the horizontal ink bands (rows) in it.
Uses the 170 dpi page render p-NN.png."""
import sys
from PIL import Image
p = int(sys.argv[1]); x0, y0, x1, y1 = map(float, sys.argv[2:6])
im = Image.open(f"/home/jixia/AI_agents/paper2agent/Reachability/logs/work/hashemi2025pca/p-{p:02d}.png").convert("L")
s = im.width / 612.0
box = (int(x0 * s), int(y0 * s), int(x1 * s), int(y1 * s))
c = im.crop(box)
bw = c.point(lambda v: 255 if v < 235 else 0)
bb = bw.getbbox()
print("ink bbox pt:", [round(box[0] / s + bb[0] / s, 1), round(box[1] / s + bb[1] / s, 1), round(box[0] / s + bb[2] / s, 1), round(box[1] / s + bb[3] / s, 1)])
# row bands
W, H = bw.size
px = bw.load()
rows = [any(px[x, y] for x in range(0, W, 2)) for y in range(H)]
bands, start = [], None
for y, r in enumerate(rows + [False]):
    if r and start is None:
        start = y
    if not r and start is not None:
        bands.append((round(y0 + start / s, 1), round(y0 + y / s, 1)))
        start = None
print("bands:", bands)
