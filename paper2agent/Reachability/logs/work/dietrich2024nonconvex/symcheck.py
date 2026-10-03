#!/usr/bin/env python3
"""Per-page counts of relation/operator/Greek symbols: PDF text layer (evidence lines, whole page incl. the
algorithm boxes) vs reviewed markdown (all non-omitted text items incl. the algorithm transcriptions, plus table cells).
Adapted from liebenwein2018sampling/symbol_check2.py."""
import json, re, collections
from pagelib import D
def cnt(pat, s): return len(re.findall(pat, s))
PDF = [("le", "≤"), ("ge", "≥"), ("subseteq", "⊆"), ("to", "→"), ("infty", "∞"), ("times", "×"), ("cdot", "·"),
       ("sim", "∼"), ("forall", "∀"), ("cup", "∪"), ("cap", "∩"), ("emptyset", "∅"), ("star", "∗"), ("ddot", "¨"), ("dot", "˙"),
       ("theta", "θ"), ("epsilon", "ϵ"), ("delta", "δ"), ("sigma", "σ"), ("mu", "µ"), ("beta", "β"), ("gamma", "γ"),
       ("Sigma", "Σ"), ("pi", "π"), ("Phi", "Φ"), ("phi", "ϕ"), ("alpha", "α"), ("omega", "ω"), ("Delta", "∆"), ("Gamma", "Γ")]
MD = {"le": r"\\le(?![a-z])", "ge": r"\\ge(?![a-z])", "subseteq": r"\\subseteq", "to": r"\\to(?![a-z])", "infty": r"\\infty",
      "times": r"\\times", "cdot": r"\\cdot(?![a-z])", "sim": r"\\sim(?![a-z])", "forall": r"\\forall", "cup": r"\\cup(?![a-z])",
      "cap": r"\\cap(?![a-z])", "emptyset": r"\\emptyset", "star": r"\^\*", "ddot": r"\\ddot", "dot": r"\\dot(?![a-z])",
      "theta": r"\\theta", "epsilon": r"\\epsilon|ϵ", "delta": r"\\delta", "sigma": r"\\sigma", "mu": r"\\mu(?![a-z])",
      "beta": r"\\beta", "gamma": r"\\gamma", "Sigma": r"\\Sigma", "pi": r"\\pi(?![a-z])", "Phi": r"\\Phi", "phi": r"\\phi",
      "alpha": r"\\alpha", "omega": r"\\omega", "Delta": r"\\Delta", "Gamma": r"\\Gamma"}
tot = 0
for pn in range(1, 15):
    ev = json.load(open(D / f"evidence/page-{pn:04d}.json"))
    page = json.load(open(D / f"pages/page-{pn:04d}.json"))
    omit = [i["bbox"] for i in page["items"] if i["kind"] == "omit"]
    def inside(b):
        cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
        return any(e[0] <= cx <= e[2] and e[1] <= cy <= e[3] for e in omit)
    raw = "\n".join(l["text"] for l in ev["lines"] if not inside(l["bbox"]))
    a = collections.OrderedDict((n, raw.count(g)) for n, g in PDF)
    a["notin"] = raw.count("/∈"); a["in"] = raw.count("∈") - a["notin"]
    a["="] = raw.count("="); a["+"] = raw.count("+"); a["<"] = raw.count("<"); a[">"] = raw.count(">")
    a["minus"] = raw.count("−"); a["bar"] = raw.count("|"); a["setminus"] = raw.count("\\")
    md = "\n".join(i.get("markdown", "") + " " + " ".join(" ".join(r) for r in (i.get("rows") or []))
                   for i in page["items"] if i["kind"] != "omit")
    math = " ".join(re.findall(r"\$\$.*?\$\$|\$[^$]+\$", md, flags=re.S))
    b = collections.OrderedDict((n, cnt(MD[n], md)) for n, _ in PDF)
    b["notin"] = cnt(r"\\notin", md); b["in"] = cnt(r"\\in(?![a-z])", md)
    b["="] = md.count("="); b["+"] = math.count("+"); b["<"] = math.count("<"); b[">"] = math.count(">")
    b["minus"] = math.count("-"); b["bar"] = math.count("|"); b["setminus"] = cnt(r"\\setminus", md)
    diff = {k: (a[k], b[k]) for k in a if a[k] != b[k]}
    tot += len(diff)
    print(f"page {pn}: symbols_pdf={sum(a.values())} symbols_md={sum(b.values())} DIFF(pdf,md)={diff}")
print("differing counters:", tot)
