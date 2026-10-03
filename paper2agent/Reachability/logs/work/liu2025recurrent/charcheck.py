#!/usr/bin/env python3
r"""Character-multiset check per page (liu2025recurrent): every letter/digit/Greek letter of the PDF text layer
(outside the omitted stamp and the three figure crops) against the reviewed markdown after mapping LaTeX back to
the glyphs of the text layer (\tau -> τ, \hat x -> ˆx, \mathrm{sd} -> sd, \max -> max, \tag{5} -> 5, ...).
A wrong, missing or extra variable, subscript, digit or Greek letter shows up as a non-empty difference."""
import json, os, re, unicodedata, collections, html
R = os.path.expanduser("~/AI_agents/paper2agent/Reachability")
D = f"{R}/paper-review/liu2025recurrent-paper/documents/s001-liu2025recurrent"
GREEK = {"tau": "τ", "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "kappa": "κ", "phi": "ϕ", "lambda": "λ", "pi": "π"}
WORDOPS = ["max", "min", "sup", "inf", "lim", "arg", "log", "cos", "sin"]
KEEPARG = ["mathrm", "text", "mathcal", "mathbb", "dot", "overline", "underline", "boldsymbol", "sqrt", "frac", "big"]
def delatex(s):
    s = html.unescape(s)
    s = re.sub(r"\\tag\{(\d+)\}", r" \1 ", s)
    s = re.sub(r"\\(begin|end)\{[a-z]+\}", " ", s)
    s = re.sub(r"\\hat(?![a-z])", "ˆ", s)
    for k, g in GREEK.items():
        s = re.sub(r"\\" + k + r"(?![A-Za-z])", g, s)
    for k in WORDOPS:
        s = re.sub(r"\\" + k + r"(?![A-Za-z])", " " + k + " ", s)
    for k in KEEPARG:
        s = re.sub(r"\\" + k + r"(?![A-Za-z])", " ", s)
    s = re.sub(r"\\[A-Za-z]+", " ", s)          # every other command prints no letter or digit
    return s
def chars(t):
    t = unicodedata.normalize("NFKD", t)
    return collections.Counter(c for c in t.casefold() if c.isalnum())
tot = 0
for pn in range(1, 9):
    ev = json.load(open(f"{D}/evidence/page-{pn:04d}.json"))
    page = json.load(open(f"{D}/pages/page-{pn:04d}.json"))
    excl = [i["bbox"] for i in page["items"] if i["kind"] == "omit" or (i["kind"] == "figure" and i["asset_name"].startswith("figure-"))]
    def inside(b):
        cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
        return any(e[0] <= cx <= e[2] and e[1] <= cy <= e[3] for e in excl)
    raw = "\n".join(l["text"] for l in ev["lines"] if not inside(l["bbox"]))
    md = "\n".join(i.get("markdown", "") + " " + " ".join(" ".join(r) for r in (i.get("rows") or [])) for i in page["items"] if i["kind"] in ("text", "caption", "heading", "table"))
    a, b = chars(raw), chars(delatex(md))
    miss, extra = dict(a - b), dict(b - a)
    tot += sum(miss.values()) + sum(extra.values())
    print(f"page {pn}: pdf chars {sum(a.values())}, md chars {sum(b.values())}; in PDF not in md: {miss}; in md not in PDF: {extra}")
print("total differing characters:", tot)
