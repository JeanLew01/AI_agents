#!/usr/bin/env python3
"""Per-page counts of relation/operator symbols and Greek letters: PDF text layer (evidence lines outside figure/table/omit
bboxes) vs reviewed markdown (math only)."""
import json, os, re, collections
D = os.path.expanduser("~/AI_agents/paper2agent/Reachability/paper-review/hashemi2025pca-paper/documents/s001-hashemi2025pca")
def cnt(pat, s): return len(re.findall(pat, s))
PDF = [("le", "≤"), ("ge", "≥"), ("subset", "⊂"), ("subseteq", "⊆"), ("in", "∈"), ("sim", "∼"), ("to", "→"), ("times", "×"),
       ("oplus", "⊕"), ("top", "⊤"), ("bot", "⊥"), ("langle", "⟨"), ("rangle", "⟩"), ("lceil", "⌈"), ("rceil", "⌉"), ("ast", "∗"),
       ("succeq", "⪰"), ("minus", "−"), ("+", "+"), ("<", "<"), (">", ">"), ("=", "="),
       ("rho", "ρ"), ("omega", "ω"), ("delta", "δ"), ("tau", "τ"), ("sigma", "σ"), ("ell", "ℓ"), ("alpha", "α"), ("mu", "µ"),
       ("theta", "θ"), ("Theta", "Θ"), ("Sigma", "Σ")]
MD = {"le": r"\\le(q)?(?![a-z])", "ge": r"\\ge(q)?(?![a-z])", "subset": r"\\subset(?![a-z])", "subseteq": r"\\subseteq", "in": r"\\in(?![a-z])",
      "sim": r"\\sim(?![a-z])", "to": r"\\(to|rightarrow)(?![a-z])", "times": r"\\times", "oplus": r"\\oplus", "top": r"\\top(?![a-z])", "bot": r"\\bot(?![a-z])",
      "langle": r"\\langle", "rangle": r"\\rangle", "lceil": r"\\lceil", "rceil": r"\\rceil", "ast": r"\\ast", "succeq": r"\\succeq",
      "minus": r"-", "+": r"\+", "<": r"<", ">": r">", "=": r"=",
      "rho": r"\\rho(?![a-z])", "omega": r"\\omega(?![a-z])", "delta": r"\\delta(?![a-z])", "tau": r"\\tau(?![a-z])", "sigma": r"\\sigma(?![a-z])",
      "ell": r"\\ell(?![a-z])", "alpha": r"\\alpha(?![a-z])", "mu": r"\\mu(?![a-z])", "theta": r"\\theta(?![a-z])", "Theta": r"\\Theta", "Sigma": r"\\Sigma"}
tot = 0
for pn in range(1, 17):
    ev = json.load(open(f"{D}/evidence/page-{pn:04d}.json"))
    page = json.load(open(f"{D}/pages/page-{pn:04d}.json"))
    excl = [i["bbox"] for i in page["items"] if i["kind"] in ("figure", "omit", "table")]
    def inside(l):
        b = l["bbox"]; cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
        return any(e[0] <= cx <= e[2] and e[1] <= cy <= e[3] for e in excl)
    raw = "\n".join(l["text"] for l in ev["lines"] if not inside(l))
    a = collections.OrderedDict((k, raw.count(g)) for k, g in PDF)
    a["notin"] = raw.count("/∈") + raw.count("∈/"); a["in"] -= a["notin"]
    a["iff"] = raw.count("⇐"); a["="] -= 0
    md = "\n".join(i.get("markdown", "") for i in page["items"] if i["kind"] in ("text", "caption", "heading") and not i["id"].endswith("-note"))
    math = " ".join(re.findall(r"\$\$.*?\$\$|\$[^$]+\$", md, flags=re.S))
    math = re.sub(r"\\tag\{[^}]*\}", "", math)
    b = collections.OrderedDict((k, cnt(MD[k], math)) for k, _ in PDF)
    b["notin"] = cnt(r"\\notin", math); b["iff"] = cnt(r"\\iff", math)
    b["="] += 0
    b["+"] += 0
    # ':=' contains '=', '\succeq' etc. do not; \geq/\leq counted once
    diff = {k: (a[k], b[k]) for k in a if a[k] != b[k]}
    tot += len(diff)
    print(f"page {pn}: symbols_pdf={sum(a.values())} symbols_md={sum(b.values())} DIFF(pdf,md)={diff}")
print("differing counters:", tot)
