#!/usr/bin/env python3
"""Compare every text/caption/heading item without math against the PDF text layer inside its bbox,
character by character after removing Markdown markers and whitespace (punctuation and dashes kept)."""
import json, re, sys, unicodedata
from pagelib import D
pages = [int(a) for a in sys.argv[1:]] or range(1, 16)
LIG = {"ﬁ": "fi", "ﬂ": "fl", "ﬀ": "ff", "ﬃ": "ffi", "ﬄ": "ffl"}
def norm(t):
    for k, v in LIG.items(): t = t.replace(k, v)
    return re.sub(r"\s+", "", t)
bad = 0
for pn in pages:
    st = json.loads((D / f"pages/page-{pn:04d}.json").read_text())
    ev = json.loads((D / f"evidence/page-{pn:04d}.json").read_text())
    for it in st["items"]:
        if it["kind"] not in ("text", "caption", "heading") or "$" in it["markdown"]:
            continue
        b = it["bbox"]
        ls = [l for l in ev["lines"] if b[0]-2 <= (l["bbox"][0]+l["bbox"][2])/2 <= b[2]+2 and b[1]-1 <= (l["bbox"][1]+l["bbox"][3])/2 <= b[3]+1]
        ls.sort(key=lambda l: (round(l["bbox"][1]/4), l["bbox"][0]))
        md = it["markdown"]
        md = re.sub(r"^#+ ", "", md).replace("\\*", "\x00").replace("*", "").replace("\x00", "*")
        md = re.sub(r"^Footnote (\d+): ", r"\1", md)
        mine = norm(md)
        src = ""
        for l in ls:
            t = l["text"].strip()
            src += t + "\n"
        # resolve line-end hyphens: drop the hyphen when my text has the closed form
        out = ""
        parts = src.split("\n")
        for k, t in enumerate(parts):
            t = norm(t)
            if t.endswith("-") and not mine.startswith(out + t):
                t = t[:-1]
            out += t
        if out != mine:
            bad += 1
            # locate first difference
            i = next((k for k in range(min(len(out), len(mine))) if out[k] != mine[k]), min(len(out), len(mine)))
            print(f"page {pn} {it['id']}: DIFF at {i}: pdf='{out[max(0,i-25):i+30]}' mine='{mine[max(0,i-25):i+30]}'")
print("items differing:", bad)
