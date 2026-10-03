#!/usr/bin/env python3
"""Number-token comparison with the tool's own tokenizer, split by region:
 (a) PDF lines outside figure/omit regions vs markdown without the algorithm transcriptions (what the tool compares,
     minus the transcription), and (b) PDF lines inside each algorithm crop vs that algorithm's transcription."""
import json, re, collections
from pagelib import D
TOK = re.compile(r"[+−-]?(?:\d{1,3}(?:,\d{3})+(?!\d)|\d+)(?:\.\d+)*(?:[eE][+−-]?\d+)?%?")
def toks(t): return collections.Counter(TOK.findall(t.replace("*", "").replace("_", "")))
def diff(a, b): return {"pdf_only": dict(a - b), "md_only": dict(b - a)}
for pn in range(1, 15):
    ev = json.load(open(D / f"evidence/page-{pn:04d}.json"))
    page = json.load(open(D / f"pages/page-{pn:04d}.json"))
    excl = [i for i in page["items"] if i["kind"] in ("figure", "omit")]
    def inside(b, e):
        cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
        return e[0] <= cx <= e[2] and e[1] <= cy <= e[3]
    outside = "\n".join(l["text"] for l in ev["lines"] if not any(inside(l["bbox"], e["bbox"]) for e in excl))
    md = "\n".join(i.get("markdown", "") + " " + " ".join(" ".join(r) for r in (i.get("rows") or []))
                   for i in page["items"] if i["kind"] not in ("omit", "figure") and not i["id"].endswith("-text"))
    d = diff(toks(outside), toks(md))
    if d["pdf_only"] or d["md_only"]: print(f"page {pn} main text: {d}")
    for i in page["items"]:
        if i["id"].endswith("-text"):
            box = "\n".join(l["text"] for l in ev["lines"] if inside(l["bbox"], i["bbox"]))
            print(f"page {pn} {i['id']}: box tokens {sum(toks(box).values())}, transcription tokens {sum(toks(i['markdown']).values())}, diff {diff(toks(box), toks(i['markdown']))}")
