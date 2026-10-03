#!/usr/bin/env python3
"""For every PDF text-layer line outside the stamp/figure crops: is its alphanumeric skeleton a substring of the
page markdown after de-LaTeXing (same mapping as charcheck.py)? Lines that fail are printed (they are the stacked /
reordered math fragments, or real errors)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util, unicodedata, io, contextlib
spec = importlib.util.spec_from_file_location("cc", os.path.join(os.path.dirname(os.path.abspath(__file__)), "charcheck.py"))
cc = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(cc)
def canon(t):
    return "".join(c for c in unicodedata.normalize("NFKD", t).casefold() if c.isalnum())
pages = [int(a) for a in sys.argv[1:]] or range(1, 9)
fail = total = 0
for pn in pages:
    ev = json.load(open(f"{cc.D}/evidence/page-{pn:04d}.json"))
    page = json.load(open(f"{cc.D}/pages/page-{pn:04d}.json"))
    excl = [i["bbox"] for i in page["items"] if i["kind"] == "omit" or (i["kind"] == "figure" and i["asset_name"].startswith("figure-"))]
    def inside(b):
        cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
        return any(e[0] <= cx <= e[2] and e[1] <= cy <= e[3] for e in excl)
    md = "\n".join(i.get("markdown", "") + " " + " ".join(" ".join(r) for r in (i.get("rows") or [])) for i in page["items"] if i["kind"] in ("text", "caption", "heading", "table"))
    text = canon(cc.delatex(md))
    for l in ev["lines"]:
        if inside(l["bbox"]):
            continue
        c = canon(l["text"])
        if len(c) < 2:
            continue
        total += 1
        if c not in text:
            fail += 1
            print(f"page {pn}: UNMATCHED {l['text']!r} y={l['bbox'][1]:.0f} x={l['bbox'][0]:.0f}")
print(f"{total} lines checked, {fail} unmatched after de-LaTeX")
