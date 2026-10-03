#!/usr/bin/env python3
"""Per-page counts of relation/operator/Greek symbols: PDF text layer (evidence lines outside figure crops, but
including the algorithm boxes) vs reviewed markdown (LaTeX commands in math + Unicode symbols anywhere, incl. table
cells). Sub-caption lines repeated in captions are compared too (PDF lines inside figure crops whose text starts
with '(a)'..'(d)' are kept)."""
import json, re, collections
from lib import D
def cnt(pat, s): return len(re.findall(pat, s))
tot = 0
for pn in range(1, 21):
    ev = json.load(open(D / f"evidence/page-{pn:04d}.json"))
    page = json.load(open(D / f"pages/page-{pn:04d}.json"))
    excl = [i["bbox"] for i in page["items"] if i["kind"] == "figure" and not i["asset_name"].startswith("algorithm")]
    omit = [i["bbox"] for i in page["items"] if i["kind"] == "omit"]
    def inside(l, boxes):
        cx = (l["bbox"][0] + l["bbox"][2]) / 2; cy = (l["bbox"][1] + l["bbox"][3]) / 2
        return any(b[0] <= cx <= b[2] and b[1] <= cy <= b[3] for b in boxes)
    lines = [l["text"] for l in ev["lines"] if not inside(l, omit) and (not inside(l, excl) or re.match(r"\([a-d]\)", l["text"]))]
    raw = "\n".join(lines)
    a = collections.OrderedDict()
    a["le"] = raw.count("≤"); a["ge"] = raw.count("≥")
    a["subset"] = raw.count("⊂"); a["subseteq"] = raw.count("⊆"); a["in"] = raw.count("∈")
    a["="] = raw.count("="); a["<"] = raw.count("<"); a[">"] = raw.count(">")
    a["arrow"] = raw.count("→"); a["infty"] = raw.count("∞"); a["+"] = raw.count("+"); a["minus"] = raw.count("−")
    a["norm"] = raw.count("∥"); a["cup"] = raw.count("∪"); a["forall"] = raw.count("∀"); a["times"] = raw.count("×")
    a["cdot"] = raw.count("·"); a["hat"] = raw.count("ˆ"); a["sim"] = raw.count("∼"); a["top"] = raw.count("⊤")
    a["setminus"] = raw.count("\\")
    for g, n in (("µ", "mu"), ("δ", "delta"), ("ϵ", "epsilon"), ("ε", "varepsilon"), ("α", "alpha"), ("β", "beta"), ("γ", "gamma"), ("ω", "omega"), ("Λ", "Lambda"), ("Π", "Pi")):
        a[n] = raw.count(g)
    md = "\n".join(i.get("markdown", "") + " " + " ".join(" ".join(r) for r in (i.get("rows") or [])) for i in page["items"] if i["kind"] != "omit")
    math = " ".join(re.findall(r"\$\$.*?\$\$|\$[^$]+\$", md, flags=re.S))
    math = re.sub(r"\\tag\{\d+\}", "", math)
    b = collections.OrderedDict()
    b["le"] = cnt(r"\\leq?(?![a-z])", math); b["ge"] = cnt(r"\\geq?(?![a-z])", math)
    b["subset"] = cnt(r"\\subset(?![a-z])", math); b["subseteq"] = cnt(r"\\subseteq", math); b["in"] = cnt(r"\\in(?![a-z])", math)
    b["="] = md.count("=") ; b["<"] = math.count("<"); b[">"] = math.count(">")
    b["arrow"] = cnt(r"\\rightarrow|\\to(?![a-z])|\\mapsto", math); b["infty"] = cnt(r"\\infty", math)
    b["+"] = math.count("+"); b["minus"] = math.count("-")
    b["norm"] = math.count(r"\|"); b["cup"] = cnt(r"\\cup", math); b["forall"] = cnt(r"\\forall", math); b["times"] = cnt(r"\\times", math)
    b["cdot"] = cnt(r"\\cdot(?![a-z])", math); b["hat"] = cnt(r"\\hat(?![a-z])", math); b["sim"] = cnt(r"\\sim", math); b["top"] = cnt(r"\\top", math)
    b["setminus"] = cnt(r"\\setminus", math)
    for n, pat, uni in (("mu", r"\\mu", "µ"), ("delta", r"\\delta", "δ"), ("epsilon", r"\\epsilon", "ϵ"), ("varepsilon", r"\\varepsilon", "ε"), ("alpha", r"\\alpha", "α"), ("beta", r"\\beta", "β"), ("gamma", r"\\gamma", "γ"), ("omega", r"\\omega", "ω"), ("Lambda", r"\\Lambda", "Λ"), ("Pi", r"\\Pi", "Π")):
        b[n] = cnt(pat + r"(?![a-zA-Z])", math) + md.count(uni)
    diff = {k: (a[k], b[k]) for k in a if a[k] != b[k]}
    tot += len(diff)
    print(f"page {pn}: symbols_pdf={sum(a.values())} symbols_md={sum(b.values())} DIFF(pdf,md)={diff}")
print("differing counters:", tot)
