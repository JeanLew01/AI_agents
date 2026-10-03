#!/usr/bin/env python3
"""Per-page counts of relation/operator symbols: PDF text layer (evidence lines outside figure/omit boxes) vs reviewed markdown math."""
import json, os, re, collections
R = os.path.expanduser("~/AI_agents/paper2agent/Reachability")
D = f"{R}/paper-review/lew2022simple-paper/documents/s001-lew2022simple"
def cnt(pat, s): return len(re.findall(pat, s))
tot = 0
for pn in range(1, 26):
    ev = json.load(open(f"{D}/evidence/page-{pn:04d}.json"))
    page = json.load(open(f"{D}/pages/page-{pn:04d}.json"))
    excl = [i["bbox"] for i in page["items"] if i["kind"] in ("figure", "omit")]
    def inside(l):
        b = l["bbox"]; cx, cy = (b[0]+b[2])/2, (b[1]+b[3])/2
        return any(e[0] <= cx <= e[2] and e[1] <= cy <= e[3] for e in excl)
    raw = "\n".join(l["text"] for l in ev["lines"] if not inside(l))
    a = collections.OrderedDict()
    a["le"] = raw.count("≤"); a["ge"] = raw.count("≥")
    a["subset"] = raw.count("⊂"); a["subseteq"] = raw.count("⊆"); a["nsubseteq"] = raw.count("⊈")
    a["notin"] = raw.count("/∈") + raw.count("∉"); a["in"] = raw.count("∈") - raw.count("/∈")
    a["neq"] = raw.count("̸=") + raw.count("≠"); a["="] = raw.count("=") - raw.count("̸=")
    a["<"] = raw.count("<"); a[">"] = raw.count(">")
    a["to"] = raw.count("→"); a["gets"] = raw.count("←"); a["implies"] = raw.count("=⇒") + raw.count("⟹")
    a["infty"] = raw.count("∞"); a["+"] = raw.count("+"); a["minus"] = raw.count("−")
    a["norm"] = raw.count("∥")
    a["cup"] = raw.count("∪") + raw.count("S\n"); a["cap"] = raw.count("∩")
    a["forall"] = raw.count("∀"); a["exists"] = raw.count("∃")
    a["partial"] = raw.count("∂"); a["emptyset"] = raw.count("∅")
    a["oplus"] = raw.count("⊕"); a["ominus"] = raw.count("⊖"); a["approx"] = raw.count("≈"); a["times"] = raw.count("×")
    a["hat"] = raw.count("ˆ"); a["bar"] = raw.count("¯"); a["tilde"] = raw.count("˜")
    for g, n in (("λ", "lambda"), ("δ", "delta"), ("ϵ", "epsilon"), ("α", "alpha"), ("Λ", "Lambda"), ("π", "pi"), ("Γ", "Gamma"), ("ω", "omega"), ("Ω", "Omega"), ("µ", "mu"), ("ν", "nu"), ("β", "beta")):
        a[n] = raw.count(g)
    md = "\n".join(i.get("markdown", "") for i in page["items"] if i["kind"] in ("text", "caption", "heading"))
    math = " ".join(re.findall(r"\$\$.*?\$\$|\$[^$]+\$", md, flags=re.S))
    b = collections.OrderedDict()
    b["le"] = cnt(r"\\leq?(?![a-z])", math); b["ge"] = cnt(r"\\geq?(?![a-z])", math)
    b["subset"] = cnt(r"\\subset(?![a-z])", math); b["subseteq"] = cnt(r"\\subseteq", math); b["nsubseteq"] = cnt(r"\\nsubseteq", math)
    b["notin"] = cnt(r"\\notin", math); b["in"] = cnt(r"\\in(?![a-z])", math)
    b["neq"] = cnt(r"\\neq?(?![a-z])", math); b["="] = math.count("=")
    b["<"] = math.count("<"); b[">"] = math.count(">")
    b["to"] = cnt(r"\\(to|rightarrow|longrightarrow)(?![a-z])", math); b["gets"] = cnt(r"\\gets", math); b["implies"] = cnt(r"\\implies", math)
    b["infty"] = cnt(r"\\infty", math); b["+"] = math.count("+"); b["minus"] = math.count("-")
    b["norm"] = math.count(r"\|")
    b["cup"] = cnt(r"\\(big)?cup(?![a-z])", math); b["cap"] = cnt(r"\\(big)?cap(?![a-z])", math)
    b["forall"] = cnt(r"\\forall", math); b["exists"] = cnt(r"\\exists", math)
    b["partial"] = cnt(r"\\partial", math); b["emptyset"] = cnt(r"\\emptyset", math)
    b["oplus"] = cnt(r"\\oplus", math); b["ominus"] = cnt(r"\\ominus", math); b["approx"] = cnt(r"\\approx", math); b["times"] = cnt(r"\\times", math)
    b["hat"] = cnt(r"\\hat", math); b["bar"] = cnt(r"\\bar", math); b["tilde"] = cnt(r"\\tilde", math)
    for n, pat in (("lambda", r"\\lambda"), ("delta", r"\\delta"), ("epsilon", r"\\epsilon"), ("alpha", r"\\alpha"), ("Lambda", r"\\Lambda"), ("pi", r"\\pi"), ("Gamma", r"\\Gamma"), ("omega", r"\\omega"), ("Omega", r"\\Omega"), ("mu", r"\\mu"), ("nu", r"\\nu"), ("beta", r"\\beta")):
        b[n] = cnt(pat + r"(?![a-zA-Z])", math)
    diff = {k: (a[k], b[k]) for k in a if a[k] != b[k]}
    tot += len(diff)
    print(f"page {pn}: pdf={sum(a.values())} md={sum(b.values())} DIFF(pdf,md)={diff}")
print("differing counters:", tot)
