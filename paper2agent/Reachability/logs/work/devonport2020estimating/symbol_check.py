#!/usr/bin/env python3
"""Count relation/operator symbols per page in the PDF text layer and in the reviewed markdown.
The tool's line check ignores non-alphanumeric characters, so this covers <=, >=, subset, in, ->, =, +, -."""
import json, os, re, collections
import subprocess
R = os.path.expanduser("~/AI_agents/paper2agent/Reachability")
D = f"{R}/paper-review/devonport2020estimating-paper/documents/s001-devonport2020estimating"
PDFSYM = {"≤": "le", "≥": "ge", "⊂": "subset", "∈": "in", "→": "to", "∞": "infty", "×": "times", "=": "=", "+": "+", "−": "minus",
          ">": ">", "∥": "norm", "|": "bar"}
for pn in range(1, 11):
    ev = json.load(open(f"{D}/evidence/page-{pn:04d}.json"))
    raw = "\n".join(l["text"] for l in ev["lines"])
    a = collections.Counter()
    for ch, name in PDFSYM.items():
        a[name] = raw.count(ch)
    a["norm"] = a["norm"] + a["bar"] // 2; del a["bar"]          # '||' or one double-bar glyph = one delimiter
    page = json.load(open(f"{D}/pages/page-{pn:04d}.json"))
    md = "\n".join(i.get("markdown", "") for i in page["items"] if i["kind"] in ("text", "caption", "heading"))
    if pn == 8:
        md += "\n" + "\n".join(" ".join(r) for i in page["items"] if i.get("rows") for r in i["rows"])
    math = " ".join(re.findall(r"\$\$.*?\$\$|\$[^$]+\$", md, flags=re.S))
    b = collections.Counter()
    b["le"] = len(re.findall(r"\\le(?![a-z])", math)); b["ge"] = len(re.findall(r"\\ge(?![a-z])", math))
    b["subset"] = math.count(r"\subset"); b["in"] = len(re.findall(r"\\in(?![a-z])", math))
    b["to"] = len(re.findall(r"\\to(?![a-z])", math)); b["infty"] = math.count(r"\infty"); b["times"] = math.count(r"\times")
    b["="] = math.count("="); b["+"] = math.count("+") ; b[">"] = math.count(">")
    b["minus"] = math.count("-") - math.count("-accurate")
    b["norm"] = math.count(r"\|")
    diff = {k: (a[k], b[k]) for k in sorted(set(a) | set(b)) if a[k] != b[k]}
    print(f"page {pn}: pdf={dict(a)}\n         md ={dict(b)}\n         DIFF(pdf,md)={diff}")
