#!/usr/bin/env python3
"""Stricter look at the verifier's missing lines.
For each missing source line: take its alphabetic words (>=3 letters). A word is 'found' when it occurs in the
built page text (LaTeX commands removed) in order after the previous found word; the first/last word of a line may be
a line-wrap fragment (suffix/prefix of a page word). Words that are not found are printed, so that every line that
loses a real prose word is visible. Math glyph-soup words (dber, dkl, vargq, ...) are expected to remain."""
import json, re, sys, unicodedata
from pathlib import Path
R = Path.home() / "AI_agents/paper2agent/Reachability"
D = R / "paper-review/devonport2023data-paper/documents/s001-devonport2023data"
v = json.loads((D / "verification.json").read_text())
b = json.loads((D / "build.json").read_text())
md = (Path(b["output"]) / b["paper"]).read_text(encoding="utf-8")
chunks = re.split(r"<!-- PDF page (\d+) -->", md)
pages = {int(chunks[i]): chunks[i + 1] for i in range(1, len(chunks), 2)}
def words(t, strip_tex=False):
    t = unicodedata.normalize("NFKD", t)
    if strip_tex:
        t = re.sub(r"\\[A-Za-z]+", " ", t)
    return [w.lower() for w in re.findall(r"[A-Za-z]{3,}", t)]
tot = 0
for p in v["pages"]:
    n = p["page"]
    pw = words(pages.get(n - 1, "")[-700:] + pages[n] + pages.get(n + 1, "")[:400], strip_tex=True)
    for l in p["missing_lines"]:
        lw = words(l["text"])
        pos, miss = 0, []
        for k, w in enumerate(lw):
            hit = None
            for j in range(pos, len(pw)):
                x = pw[j]
                if x == w or (k == 0 and x.endswith(w)) or (k == len(lw) - 1 and x.startswith(w)):
                    hit = j; break
            if hit is None:
                # retry anywhere on page (order broken)
                any_ = any(x == w or (k == 0 and x.endswith(w)) or (k == len(lw) - 1 and x.startswith(w)) for x in pw)
                miss.append(w + ("?order" if any_ else ""))
            else:
                pos = hit + 1
        if miss:
            tot += 1
            print(f"p{n}: {l['text']!r}\n      unmatched: {miss}")
print("lines with unmatched words:", tot)
