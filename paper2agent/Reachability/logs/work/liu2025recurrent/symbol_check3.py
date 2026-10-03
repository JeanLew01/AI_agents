#!/usr/bin/env python3
r"""Per-page symbol counts, PDF text layer vs reviewed markdown (liu2025recurrent).
Differences from symbol_check2.py: \leq/\geq/\rightarrow/\gets/\neq/\mid variants are counted, PDF lines inside
figure crops named figure-* are excluded (algorithm crops are kept because they are transcribed), and the whole
markdown (plus table cells) is scanned, not only the math."""
import json, os, re, collections
R = os.path.expanduser("~/AI_agents/paper2agent/Reachability")
D = f"{R}/paper-review/liu2025recurrent-paper/documents/s001-liu2025recurrent"
def cnt(pat, s): return len(re.findall(pat, s))
tot = 0
for pn in range(1, 9):
    ev = json.load(open(f"{D}/evidence/page-{pn:04d}.json"))
    page = json.load(open(f"{D}/pages/page-{pn:04d}.json"))
    excl = [i["bbox"] for i in page["items"] if i["kind"] == "omit" or (i["kind"] == "figure" and i["asset_name"].startswith("figure-"))]
    def inside(b):
        cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
        return any(e[0] <= cx <= e[2] and e[1] <= cy <= e[3] for e in excl)
    raw = "\n".join(l["text"] for l in ev["lines"] if not inside(l["bbox"]))
    a = collections.OrderedDict()
    a["le"] = raw.count("≤"); a["ge"] = raw.count("≥")
    a["subset"] = raw.count("⊂"); a["subseteq"] = raw.count("⊆")
    a["notin"] = raw.count("/∈") + raw.count("∈/") + raw.count("∉"); a["in"] = raw.count("∈") - raw.count("/∈") - raw.count("∈/")
    a["neq"] = raw.count("̸=") + raw.count("≠"); a["="] = raw.count("=") - raw.count("̸=")
    a["<"] = raw.count("<"); a[">"] = raw.count(">")
    a["to"] = raw.count("→"); a["leftarrow"] = raw.count("←")
    a["infty"] = raw.count("∞"); a["+"] = raw.count("+"); a["minus"] = raw.count("−")
    a["norm"] = raw.count("∥"); a["bar"] = raw.count("|")
    a["cup"] = raw.count("∪"); a["cap"] = raw.count("∩"); a["forall"] = raw.count("∀"); a["exists"] = raw.count("∃")
    a["partial"] = raw.count("∂"); a["prime"] = raw.count("′"); a["emptyset"] = raw.count("∅")
    a["hat"] = raw.count("ˆ"); a["star"] = raw.count("∗"); a["nabla"] = raw.count("∇")
    for g, n in (("λ", "lambda"), ("δ", "delta"), ("α", "alpha"), ("β", "beta"), ("γ", "gamma"), ("τ", "tau"), ("κ", "kappa"), ("ϕ", "phi"), ("π", "pi")):
        a[n] = raw.count(g)
    md = "\n".join(i.get("markdown", "") + " " + " ".join(" ".join(r) for r in (i.get("rows") or [])) for i in page["items"] if i["kind"] in ("text", "caption", "heading", "table"))
    b = collections.OrderedDict()
    b["le"] = cnt(r"\\leq?(?![a-z])", md); b["ge"] = cnt(r"\\geq?(?![a-z])", md)
    b["subset"] = cnt(r"\\subset(?![a-z])", md); b["subseteq"] = cnt(r"\\subseteq", md)
    b["notin"] = cnt(r"\\notin", md); b["in"] = cnt(r"\\in(?![a-z])", md)
    b["neq"] = cnt(r"\\neq?(?![a-z])", md); b["="] = md.count("=")
    b["<"] = md.count("<"); b[">"] = md.count(">")
    b["to"] = cnt(r"\\(to|rightarrow)(?![a-z])", md); b["leftarrow"] = cnt(r"\\(leftarrow|gets)", md)
    b["infty"] = cnt(r"\\infty", md); b["+"] = md.count("+"); b["minus"] = " ".join(re.findall(r"\$\$.*?\$\$|\$[^$]+\$", md, flags=re.S)).count("-")
    b["norm"] = md.count(r"\|"); b["bar"] = md.replace(r"\|", "").count("|") + cnt(r"\\mid", md)
    b["cup"] = cnt(r"\\cup", md); b["cap"] = cnt(r"\\cap", md); b["forall"] = cnt(r"\\forall", md); b["exists"] = cnt(r"\\exists", md)
    b["partial"] = cnt(r"\\partial", md); b["prime"] = md.count("'"); b["emptyset"] = cnt(r"\\emptyset", md)
    b["hat"] = cnt(r"\\hat", md); b["star"] = cnt(r"\\ast", md); b["nabla"] = cnt(r"\\nabla", md)
    for n, pat in (("lambda", r"\\lambda"), ("delta", r"\\delta"), ("alpha", r"\\alpha"), ("beta", r"\\beta"), ("gamma", r"\\gamma"), ("tau", r"\\tau"), ("kappa", r"\\kappa"), ("phi", r"\\phi"), ("pi", r"\\pi")):
        b[n] = cnt(pat + r"(?![a-zA-Z])", md)
    diff = {k: (a[k], b[k]) for k in a if a[k] != b[k]}
    tot += len(diff)
    print(f"page {pn}: symbols_pdf={sum(a.values())} symbols_md={sum(b.values())} DIFF(pdf,md)={diff}")
print("differing counters:", tot)
