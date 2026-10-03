#!/usr/bin/env python3
"""Per-page counts of relation/operator/decoration symbols: PDF text layer (evidence lines) vs reviewed markdown.
Extended version for liebenwein2018sampling (separates subset/subseteq, in/notin, =/neq, norm bars/single bars; adds
quantifiers, cup, partial, primes, arrows, emptyset, hats, lambda/mu/delta/epsilon counts)."""
import json, os, re, collections, unicodedata
R = os.path.expanduser("~/AI_agents/paper2agent/Reachability")
D = f"{R}/paper-review/hashemi2023data-paper/documents/s001-hashemi2023data"
def cnt(pat, s): return len(re.findall(pat, s))
tot = 0
for pn in range(1, 17):
    ev = json.load(open(f"{D}/evidence/page-{pn:04d}.json"))
    raw = "\n".join(l["text"] for l in ev["lines"])
    a = collections.OrderedDict()
    a["le"] = raw.count("≤"); a["ge"] = raw.count("≥")
    a["subset"] = raw.count("⊂"); a["subseteq"] = raw.count("⊆")
    a["notin"] = raw.count("/∈"); a["in"] = raw.count("∈") - a["notin"]
    a["neq"] = raw.count("̸="); a["="] = raw.count("=") - a["neq"]
    a["<"] = raw.count("<"); a[">"] = raw.count(">")
    a["to"] = raw.count("→"); a["leftarrow"] = raw.count("←")
    a["infty"] = raw.count("∞"); a["+"] = raw.count("+"); a["minus"] = raw.count("−")
    a["norm"] = raw.count("∥"); a["bar"] = raw.count("|")
    a["cup"] = raw.count("∪"); a["forall"] = raw.count("∀"); a["exists"] = raw.count("∃")
    a["partial"] = raw.count("∂"); a["prime"] = raw.count("′"); a["emptyset"] = raw.count("∅")
    a["hat"] = raw.count("ˆ"); a["approx"] = raw.count("≈"); a["cdot"] = raw.count("·")
    for g, n in (("λ", "lambda"), ("µ", "mu"), ("δ", "delta"), ("ϵ", "epsilon"), ("α", "alpha"), ("∆", "Delta"), ("ξ", "xi"), ("ρ", "rho"), ("θ", "theta"), ("Γ", "Gamma"), ("π", "pi")):
        a[n] = raw.count(g)
    page = json.load(open(f"{D}/pages/page-{pn:04d}.json"))
    md = "\n".join(i.get("markdown", "") for i in page["items"] if i["kind"] in ("text", "caption", "heading"))
    math = " ".join(re.findall(r"\$\$.*?\$\$|\$[^$]+\$", md, flags=re.S))
    b = collections.OrderedDict()
    b["le"] = cnt(r"\\leq?(?![a-z])", math); b["ge"] = cnt(r"\\geq?(?![a-z])", math)
    b["subset"] = cnt(r"\\subset(?![a-z])", math); b["subseteq"] = cnt(r"\\subseteq", math)
    b["notin"] = cnt(r"\\notin", math); b["in"] = cnt(r"\\in(?![a-z])", math)
    b["neq"] = cnt(r"\\neq?(?![a-z])", math); b["="] = math.count("=")
    b["<"] = math.count("<"); b[">"] = math.count(">")
    b["to"] = cnt(r"\\(to|rightarrow)(?![a-z])", math); b["leftarrow"] = cnt(r"\\(leftarrow|gets)(?![a-z])", math)
    b["infty"] = cnt(r"\\infty", math); b["+"] = math.count("+"); b["minus"] = math.count("-")
    b["norm"] = math.count(r"\|"); b["bar"] = math.replace(r"\|", "").count("|") + cnt(r"\\mid", math)
    b["cup"] = cnt(r"\\(big)?cup", math); b["forall"] = cnt(r"\\forall", math); b["exists"] = cnt(r"\\exists", math)
    b["partial"] = cnt(r"\\partial", math); b["prime"] = math.count("'"); b["emptyset"] = cnt(r"\\emptyset", math)
    b["hat"] = cnt(r"\\hat", math); b["approx"] = cnt(r"\\approx", math); b["cdot"] = cnt(r"\\cdot(?![a-z])", math)
    for n, pat in (("lambda", r"\\lambda"), ("mu", r"\\mu"), ("delta", r"\\delta"), ("epsilon", r"\\epsilon"), ("alpha", r"\\alpha"), ("Delta", r"\\Delta"), ("xi", r"\\xi"), ("rho", r"\\rho"), ("theta", r"\\theta"), ("Gamma", r"\\Gamma"), ("pi", r"\\pi")):
        b[n] = cnt(pat + r"(?![a-zA-Z])", math)
    diff = {k: (a[k], b[k]) for k in a if a[k] != b[k]}
    tot += len(diff)
    print(f"page {pn}: symbols_pdf={sum(a.values())} symbols_md={sum(b.values())} DIFF(pdf,md)={diff}")
print("differing counters:", tot)
