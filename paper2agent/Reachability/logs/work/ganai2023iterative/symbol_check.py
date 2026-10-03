#!/usr/bin/env python3
"""Per-page counts of relation/operator/Greek symbols: PDF text layer (evidence lines outside figure/table/omit boxes) vs reviewed markdown math."""
import json, os, re, collections
D = os.path.expanduser("~/AI_agents/paper2agent/Reachability/paper-review/ganai2023iterative-paper/documents/s001-ganai2023iterative")
def cnt(pat, s): return len(re.findall(pat, s))
tot = 0
for pn in range(1, 34):
    ev = json.load(open(f"{D}/evidence/page-{pn:04d}.json"))
    page = json.load(open(f"{D}/pages/page-{pn:04d}.json"))
    boxes = [i["bbox"] for i in page["items"] if i["kind"] in ("figure", "omit", "table")]
    def inside(b):
        cx, cy = (b[0]+b[2])/2, (b[1]+b[3])/2
        return any(x0 <= cx <= x1 and y0 <= cy <= y1 for x0, y0, x1, y1 in boxes)
    raw = "\n".join(l["text"] for l in ev["lines"] if not inside(l["bbox"]))
    a = collections.OrderedDict()
    a["le"] = raw.count("≤"); a["ge"] = raw.count("≥"); a["subseteq"] = raw.count("⊆")
    a["notin"] = raw.count("/∈"); a["in"] = raw.count("∈") - a["notin"]
    a["neq"] = raw.count("̸="); a["="] = raw.count("=") - a["neq"]
    a["<"] = raw.count("<"); a[">"] = raw.count(">"); a["ll"] = raw.count("≪")
    a["to"] = raw.count("→"); a["mapsto"] = raw.count("7→"); a["infty"] = raw.count("∞"); a["+"] = raw.count("+"); a["minus"] = raw.count("−")
    a["cap"] = raw.count("∩"); a["forall"] = raw.count("∀"); a["exists"] = raw.count("∃"); a["nabla"] = raw.count("∇")
    a["prime"] = raw.count("′"); a["hat"] = raw.count("ˆ"); a["cdot"] = raw.count("·"); a["sim"] = raw.count("∼"); a["times"] = raw.count("×")
    G = (("λ","lambda"),("γ","gamma"),("δ","delta"),("ϵ","epsilon"),("θ","theta"),("ξ","xi"),("ω","omega"),("η","eta"),("κ","kappa"),("π","pi"),("ϕ","phi"),("ζ","zeta"),("χ","chi"),("τ","tau"),("ρ","rho"),("ψ","psi"),("υ","upsilon"),("ν","nu"),("Γ","Gamma"),("Θ","Theta"),("Ω","Omega"),("Υ","Upsilon"),("∆","Delta"),("⋄","diamond"))
    for g, nme in G: a[nme] = raw.count(g)
    md = "\n".join(i.get("markdown", "") for i in page["items"] if i["kind"] in ("text", "caption", "heading") and not i.get("markdown","").startswith("Conversion note") and not i["id"].endswith("alg1-text"))
    math = " ".join(re.findall(r"\$\$.*?\$\$|\$[^$]+\$", md, flags=re.S))
    b = collections.OrderedDict()
    b["le"] = cnt(r"\\leq?(?![a-z])", math); b["ge"] = cnt(r"\\geq?(?![a-z])", math); b["subseteq"] = cnt(r"\\subseteq", math)
    b["notin"] = cnt(r"\\notin", math); b["in"] = cnt(r"\\in(?![a-z])", math)
    b["neq"] = cnt(r"\\neq?(?![a-z])", math); b["="] = math.count("=")
    b["<"] = math.count("<"); b[">"] = math.count(">"); b["ll"] = cnt(r"\\ll(?![a-z])", math)
    b["mapsto"] = cnt(r"\\mapsto", math); b["to"] = cnt(r"\\to(?![a-z])|\\rightarrow", math) + b["mapsto"]; b["infty"] = cnt(r"\\infty", math); b["+"] = math.count("+"); b["minus"] = math.count("-")
    b["cap"] = cnt(r"\\cap(?![a-z])", math); b["forall"] = cnt(r"\\forall", math); b["exists"] = cnt(r"\\exists", math); b["nabla"] = cnt(r"\\nabla", math)
    b["prime"] = math.count("'"); b["hat"] = cnt(r"\\hat", math); b["cdot"] = cnt(r"\\cdot(?![a-z])", math); b["sim"] = cnt(r"\\sim(?![a-z])", math); b["times"] = cnt(r"\\times", math)
    for g, nme in G:
        b[nme] = cnt("\\\\" + nme + r"(?![a-zA-Z])", math)
    diff = {k: (a[k], b[k]) for k in a if a[k] != b[k]}
    tot += len(diff)
    if diff: print(f"page {pn}: DIFF(pdf,md)={diff}")
print("differing counters:", tot)
