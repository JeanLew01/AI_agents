#!/usr/bin/env python3
"""Count relation/operator symbols per page in the PDF text layer (evidence lines, figure/table regions excluded)
and in the reviewed markdown math. Adapted from logs/work/devonport2020estimating/symbol_check.py."""
import json, os, re, collections
R = os.path.expanduser("~/AI_agents/paper2agent/Reachability")
D = f"{R}/paper-review/hewing2019scenario-paper/documents/s001-hewing2019scenario"
PDFSYM = {"≤": "le", "≥": "ge", "⊆": "subseteq", "⊂": "subset", "∈": "in", "→": "to", "⇒": "Rightarrow", "∞": "infty",
          "×": "times", "=": "=", "+": "+", "−": "minus", ">": ">", "≪": "ll", "∥": "norm", "⊖": "ominus", "∀": "forall",
          "∼": "sim", "≈": "approx", "±": "pm", "∗": "star", "˜": "tilde", "¯": "bar", "δ": "delta", "β": "beta", "α": "alpha",
          "θ": "theta", "π": "pi", "˙": "dot", "%": "percent"}
for pn in range(2, 8):
    ev = json.load(open(f"{D}/evidence/page-{pn:04d}.json"))
    page = json.load(open(f"{D}/pages/page-{pn:04d}.json"))
    excl = [i["bbox"] for i in page["items"] if i["kind"] in ("figure", "table")]
    def inside(l):
        x = (l["bbox"][0] + l["bbox"][2]) / 2; y = (l["bbox"][1] + l["bbox"][3]) / 2
        return any(b[0] <= x <= b[2] and b[1] <= y <= b[3] for b in excl)
    raw = "\n".join(l["text"] for l in ev["lines"] if not inside(l))
    a = collections.Counter({name: raw.count(ch) for ch, name in PDFSYM.items()})
    md = "\n".join(i.get("markdown", "") for i in page["items"] if i["kind"] in ("text", "caption", "heading") and "conversion note" not in i.get("markdown", ""))
    math = " ".join(re.findall(r"\$\$.*?\$\$|\$[^$]+\$", md, flags=re.S))
    math_notag = re.sub(r"\\tag\{[^}]*\}", "", math)
    c = lambda pat, s=math_notag: len(re.findall(pat, s))
    b = collections.Counter()
    b["le"] = c(r"\\le(?![a-z])"); b["ge"] = c(r"\\ge(?![a-z])"); b["subseteq"] = c(r"\\subseteq"); b["subset"] = c(r"\\subset(?!eq)")
    b["in"] = c(r"\\in(?![a-z])"); b["to"] = c(r"\\to(?![a-z])"); b["Rightarrow"] = c(r"\\Rightarrow"); b["infty"] = c(r"\\infty")
    b["times"] = c(r"\\times"); b["="] = math_notag.count("="); b["+"] = math_notag.count("+"); b[">"] = math_notag.count(">")
    b["ll"] = c(r"\\ll(?![a-z])"); b["norm"] = c(r"\\\|"); b["ominus"] = c(r"\\ominus"); b["forall"] = c(r"\\forall")
    b["sim"] = c(r"\\sim(?![a-z])"); b["approx"] = c(r"\\approx"); b["pm"] = c(r"\\pm(?![a-z])")
    b["minus"] = math_notag.count("-") + md.count("−")
    b["star"] = math_notag.count("*"); b["tilde"] = c(r"\\tilde"); b["bar"] = c(r"\\bar")
    b["delta"] = c(r"\\delta"); b["beta"] = c(r"\\beta"); b["alpha"] = c(r"\\alpha"); b["theta"] = c(r"\\theta"); b["pi"] = c(r"\\pi(?![a-z])")
    b["dot"] = c(r"\\dot\{") + 2 * c(r"\\ddot\{")
    b["percent"] = md.count("%")
    diff = {k: (a[k], b[k]) for k in sorted(set(a) | set(b)) if a[k] != b[k]}
    print(f"page {pn}: pdf={ {k: v for k, v in a.items() if v} }\n   DIFF(pdf,md)={diff}")
