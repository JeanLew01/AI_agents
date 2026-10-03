#!/usr/bin/env python3
"""lines.py N [y0 y1] : evidence lines of page N (bbox + text) within a y-range."""
import json,sys,os
D=os.path.expanduser("~/AI_agents/paper2agent/Reachability/paper-review/ganai2023iterative-paper/documents/s001-ganai2023iterative")
n=int(sys.argv[1]); y0=float(sys.argv[2]) if len(sys.argv)>2 else 0; y1=float(sys.argv[3]) if len(sys.argv)>3 else 1e9
d=json.load(open(f"{D}/evidence/page-{n:04d}.json"))
for l in sorted(d['lines'], key=lambda l:(l['bbox'][1],l['bbox'][0])):
    b=l['bbox']
    if y0<=b[1]<=y1: print(f"{b[0]:6.1f} {b[1]:6.1f} {b[2]:6.1f} {b[3]:6.1f}  {l['text'][:90]}")
