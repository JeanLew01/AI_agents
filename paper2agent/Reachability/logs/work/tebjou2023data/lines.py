#!/usr/bin/env python3
import json, sys
from lib import D
n = int(sys.argv[1])
e = json.loads((D / f"evidence/page-{n:04d}.json").read_text())
for l in e["lines"]:
    print([round(v, 1) for v in l["bbox"]], l["text"])
