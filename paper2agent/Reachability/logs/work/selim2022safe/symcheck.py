#!/usr/bin/env python3
"""Per-page counts of relation/operator/decoration symbols: PDF text layer vs reviewed markdown (selim2022safe).
PDF lines inside pure figure crops (Figures 1-4) are excluded; lines inside algorithm crops are kept because the
algorithms are transcribed. LaTeX spellings used in this paper: \leq/\le, \geq, \lVert/\rVert, \cdots (three dots),
\mapsto (shown as '7→' in the text layer), \neq (shown as '̸ =')."""
import json, os, re, collections
D = os.path.expanduser("~/AI_agents/paper2agent/Reachability/paper-review/selim2022safe-paper/documents/s001-selim2022safe")
def cnt(pat, s): return len(re.findall(pat, s))
tot = 0
for pn in range(1, 9):
    page = json.load(open(f"{D}/pages/page-{pn:04d}.json"))
    ev = json.load(open(f"{D}/evidence/page-{pn:04d}.json"))
    figs = [i["bbox"] for i in page["items"] if i["kind"] == "figure" and i["asset_name"].startswith("figure")]
    def inside(b):
        cx, cy = (b[0]+b[2])/2, (b[1]+b[3])/2
        return any(e[0] <= cx <= e[2] and e[1] <= cy <= e[3] for e in figs)
    raw = "\n".join(l["text"] for l in ev["lines"] if not inside(l["bbox"]))
    a = collections.OrderedDict()
    a["le"] = raw.count("≤"); a["ge"] = raw.count("≥")
    a["subset"] = raw.count("⊂"); a["subseteq"] = raw.count("⊆"); a["supseteq"] = raw.count("⊇")
    a["in"] = raw.count("∈"); a["neq"] = cnt(r"̸\s*=", raw); a["="] = raw.count("=") - a["neq"]
    a["<"] = raw.count("<"); a[">"] = raw.count(">")
    a["to+mapsto"] = raw.count("→"); a["leftarrow"] = raw.count("←")
    a["infty"] = raw.count("∞"); a["+"] = raw.count("+"); a["minus"] = raw.count("−")
    a["norm"] = raw.count("∥"); a["cap"] = raw.count("∩"); a["times"] = raw.count("×")
    a["forall"] = raw.count("∀"); a["emptyset"] = raw.count("∅"); a["nabla"] = raw.count("∇")
    a["hat"] = raw.count("ˆ"); a["cdot"] = raw.count("·"); a["star"] = raw.count("⋆"); a["dagger"] = raw.count("†")
    a["dot-accent"] = raw.count("˙")
    for g, n in (("δ", "delta"), ("ϵ", "epsilon"), ("ρ", "rho"), ("θ", "theta"), ("π", "pi"), ("γ", "gamma"), ("µ", "mu"), ("φ", "phi")):
        a[n] = raw.count(g)
    md = "\n".join(i.get("markdown", "") for i in page["items"] if i["kind"] in ("text", "caption", "heading"))
    math = " ".join(re.findall(r"\$\$.*?\$\$|\$[^$]+\$", md, flags=re.S))
    b = collections.OrderedDict()
    b["le"] = cnt(r"\\leq?(?![a-z])", math); b["ge"] = cnt(r"\\geq?(?![a-z])", math)
    b["subset"] = cnt(r"\\subset(?![a-z])", math); b["subseteq"] = cnt(r"\\subseteq", math); b["supseteq"] = cnt(r"\\supseteq", math)
    b["in"] = cnt(r"\\in(?![a-z])", math); b["neq"] = cnt(r"\\neq?(?![a-z])", math); b["="] = math.count("=")
    b["<"] = math.count("<"); b[">"] = math.count(">")
    b["to+mapsto"] = cnt(r"\\to(?![a-z])", math) + cnt(r"\\mapsto", math); b["leftarrow"] = cnt(r"\\leftarrow", math)
    b["infty"] = cnt(r"\\infty", math); b["+"] = math.count("+"); b["minus"] = math.count("-")
    b["norm"] = cnt(r"\\[lr]Vert", math); b["cap"] = cnt(r"\\cap(?![a-z])", math); b["times"] = cnt(r"\\times", math)
    b["forall"] = cnt(r"\\forall", math); b["emptyset"] = cnt(r"\\emptyset", math); b["nabla"] = cnt(r"\\nabla", math)
    b["hat"] = cnt(r"\\hat", math); b["cdot"] = 3 * cnt(r"\\cdots", math) + cnt(r"\\cdot(?![a-z])", math)
    b["star"] = cnt(r"\\star", math); b["dagger"] = cnt(r"\\dagger", math); b["dot-accent"] = cnt(r"\\dot(?![a-z])", math)
    for n, pat in (("delta", r"\\delta"), ("epsilon", r"\\epsilon"), ("rho", r"\\rho"), ("theta", r"\\theta"), ("pi", r"\\pi"), ("gamma", r"\\gamma"), ("mu", r"\\mu"), ("phi", r"\\phi")):
        b[n] = cnt(pat + r"(?![a-zA-Z])", math)
    diff = {k: (a[k], b[k]) for k in a if a[k] != b[k]}
    tot += len(diff)
    print(f"page {pn}: symbols_pdf={sum(a.values())} symbols_md={sum(b.values())} DIFF(pdf,md)={diff}")
print("differing counters:", tot)
