#!/usr/bin/env python3
"""inkbox.py page x0 y0 x1 y1 : tight bounding box (PDF points) of non-white pixels of the 150-dpi render inside the region."""
import sys
from PIL import Image
n=int(sys.argv[1]); x0,y0,x1,y1=[float(v) for v in sys.argv[2:6]]
im=Image.open(f"/home/jixia/AI_agents/paper2agent/Reachability/logs/work/sartipizadeh2019voronoi/p-{n:02d}.png").convert("L")
s=150/72
reg=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
bb=reg.point(lambda v:255 if v<235 else 0).getbbox()
print("ink bbox pt:", [round(x0+bb[0]/s,1), round(y0+bb[1]/s,1), round(x0+bb[2]/s,1), round(y0+bb[3]/s,1)])
# row profile: list blank bands
px=reg.load(); W,H=reg.size
rows=[any(px[x,y]<235 for x in range(0,W)) for y in range(H)]
bands=[];start=None
for y,r in enumerate(rows+[False]):
    if r and start is None: start=y
    if not r and start is not None: bands.append((round(y0+start/s,1),round(y0+y/s,1))); start=None
print("ink bands (y pt):", bands)
