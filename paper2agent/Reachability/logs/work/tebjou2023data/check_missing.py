#!/usr/bin/env python3
"""For every 'missing line' of verification.json, check that its prose words (>=3 letters) occur,
in order and close together, in the built page text. Lines that fail are printed for manual review."""
import json, re, sys, unicodedata
from pathlib import Path
R = Path.home() / "AI_agents/paper2agent/Reachability"
D = R / "paper-review/tebjou2023data-paper/documents/s001-tebjou2023data"
v = json.loads((D / "verification.json").read_text())
b = json.loads((D / "build.json").read_text())
md = (Path(b["output"]) / b["paper"]).read_text(encoding="utf-8")
chunks = re.split(r"<!-- PDF page (\d+) -->", md)
pages = {int(chunks[i]): chunks[i + 1] for i in range(1, len(chunks), 2)}
def words(t):
    t = unicodedata.normalize("NFKD", t)
    return [w.lower() for w in re.findall(r"[A-Za-z]{3,}", t)]
bad = 0
for p in v["pages"]:
    # neighbouring pages included because joins/moved glyphs cross page boundaries
    pw = words(pages.get(p["page"] - 1, "")[-600:] + pages[p["page"]] + pages.get(p["page"] + 1, "")[:300])
    for l in p["missing_lines"]:
        lw = words(l["text"])
        if not lw:
            continue
        ok = False
        for s in [i for i, w in enumerate(pw) if w == lw[0]]:
            j, k = s, 0
            while j < len(pw) and j < s + 6 * len(lw) + 25 and k < len(lw):
                if pw[j] == lw[k]:
                    k += 1
                j += 1
            if k == len(lw):
                ok = True; break
        if not ok:
            bad += 1
            print(f"page {p['page']}: NOT FOUND IN ORDER: {l['text']!r}  words={lw}")
print("lines failing word-order check:", bad)
