#!/usr/bin/env python3
"""Per-page counts of relation/operator/decoration symbols: PDF text layer (evidence lines) vs reviewed markdown."""
import json, os, re, collections
R = os.path.expanduser("~/AI_agents/paper2agent/Reachability")
D = f"{R}/paper-review/sartipizadeh2019voronoi-paper/documents/s001-sartipizadeh2019voronoi"
def cnt(pat, s): return len(re.findall(pat, s))
tot = 0
for pn in range(1, 16):
    ev = json.load(open(f"{D}/evidence/page-{pn:04d}.json"))
    raw = "\n".join(l["text"] for l in ev["lines"])
    a = collections.OrderedDict()
    a["le"] = raw.count("≤"); a["ge"] = raw.count("≥"); a["subseteq"] = raw.count("⊆"); a["subset"] = raw.count("⊂")
    a["notin"] = raw.count("̸∈") + raw.count("/∈") + raw.count("∉"); a["in"] = raw.count("∈") - raw.count("̸∈") - raw.count("/∈")
    a["neq"] = raw.count("̸=") + raw.count("≠"); a["="] = raw.count("=") - raw.count("̸=")
    a["<"] = raw.count("<"); a[">"] = raw.count(">"); a["to"] = raw.count("→"); a["infty"] = raw.count("∞")
    a["+"] = raw.count("+"); a["minus"] = raw.count("−"); a["norm"] = raw.count("∥"); a["bar"] = raw.count("|")
    a["forall"] = raw.count("∀"); a["wedge"] = raw.count("∧"); a["times"] = raw.count("×"); a["triangleq"] = raw.count("≜")
    a["hat"] = raw.count("ˆ"); a["top"] = raw.count("⊤"); a["sum"] = raw.count("∑") + raw.count("P\n") * 0; a["prod"] = raw.count("∏")
    a["cdots"] = raw.count("· · ·") + raw.count("···"); a["ast"] = raw.count("∗")
    for g, n in (("δ", "delta"), ("β", "beta"), ("α", "alpha"), ("ε", "varepsilon"), ("ϵ", "epsilon"), ("ψ", "psi"), ("Ψ", "Psi"), ("ϕ", "phi"),
                 ("φ", "varphi"), ("Φ", "Phi"), ("ω", "omega"), ("ζ", "zeta"), ("µ", "mu"), ("η", "eta"), ("ℓ", "ell")):
        a[n] = raw.count(g)
    page = json.load(open(f"{D}/pages/page-{pn:04d}.json"))
    md = "\n".join(i.get("markdown", "") for i in page["items"] if i["kind"] in ("text", "caption", "heading"))
    math = " ".join(re.findall(r"\$\$.*?\$\$|\$[^$]+\$", md, flags=re.S))
    b = collections.OrderedDict()
    b["le"] = cnt(r"\\leq?(?![a-z])", math); b["ge"] = cnt(r"\\geq?(?![a-z])", math)
    b["subseteq"] = cnt(r"\\subseteq", math); b["subset"] = cnt(r"\\subset(?![a-z])", math)
    b["notin"] = cnt(r"\\not\\in|\\notin", math); b["in"] = cnt(r"\\in(?![a-z])", math) - b["notin"] + cnt(r"\\notin", math)
    b["neq"] = cnt(r"\\neq?(?![a-z])", math); b["="] = math.count("=")
    b["<"] = math.count("<"); b[">"] = math.count(">"); b["to"] = cnt(r"\\(to|rightarrow)(?![a-z])", math); b["infty"] = cnt(r"\\infty", math)
    b["+"] = math.count("+"); b["minus"] = math.count("-"); b["norm"] = math.count(r"\|")
    b["bar"] = math.replace(r"\|", "").count("|") + cnt(r"\\mid", math) + cnt(r"\\vert", math)
    b["forall"] = cnt(r"\\forall", math); b["wedge"] = cnt(r"\\wedge", math); b["times"] = cnt(r"\\times", math); b["triangleq"] = cnt(r"\\triangleq", math)
    b["hat"] = cnt(r"\\hat", math); b["top"] = cnt(r"\\top", math); b["sum"] = cnt(r"\\sum", math); b["prod"] = cnt(r"\\prod", math)
    b["cdots"] = cnt(r"\\cdots", math); b["ast"] = cnt(r"\\ast", math)
    for n in ("delta", "beta", "alpha", "varepsilon", "epsilon", "psi", "Psi", "phi", "varphi", "Phi", "omega", "zeta", "mu", "eta", "ell"):
        b[n] = cnt("\\\\" + n + r"(?![a-zA-Z])", math)
    diff = {k: (a[k], b[k]) for k in a if a[k] != b[k]}
    tot += len(diff)
    print(f"page {pn}: symbols_pdf={sum(a.values())} symbols_md={sum(b.values())} DIFF(pdf,md)={diff}")
print("differing counters:", tot)
