#!/usr/bin/env python3
"""figbox.py N y0 y1 : union of evidence-line boxes on page N with top in [y0,y1] (text inside a figure), plus the first caption line below."""
import json,sys,os
D=os.path.expanduser("~/AI_agents/paper2agent/Reachability/paper-review/ganai2023iterative-paper/documents/s001-ganai2023iterative")
n=int(sys.argv[1]); y0=float(sys.argv[2]); y1=float(sys.argv[3])
d=json.load(open(f"{D}/evidence/page-{n:04d}.json"))
L=[l for l in d['lines'] if y0<=l['bbox'][1]<=y1 and not l['text'].startswith('Figure')]
print("lines",len(L),"union",[min(l['bbox'][0] for l in L),min(l['bbox'][1] for l in L),max(l['bbox'][2] for l in L),max(l['bbox'][3] for l in L)])
for l in d['lines']:
    if l['text'].startswith('Figure'): print("caption line",l['bbox'],l['text'][:40])
