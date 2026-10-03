#!/usr/bin/env python3
"""Check that every math snippet of the reviewed pages occurs (after macro expansion and whitespace removal) in the authors' TeX source."""
import json, re, os, glob
R = os.path.expanduser("~/AI_agents/paper2agent/Reachability")
D = f"{R}/paper-review/ouyang2026symplectic-paper/documents/s001-ouyang2026symplectic"
tex = open(f"{R}/tex-source/ouyang2026symplectic/CDC2026_sample.tex", encoding="utf-8").read()
tex = tex[tex.index(r"\begin{abstract}"):]
tex = re.sub(r"(?m)^\s*%.*$", "", tex)
MAC = [(r"\\X(?![a-zA-Z])", r"\\mathcal{X}"), (r"\\R(?![a-zA-Z])", r"\\mathbb{R}"), (r"\\cB(?![a-zA-Z])", r"\\mathcal{B}"),
       (r"\\tgt(?![a-zA-Z])", r"\\mathrm{tgt}"), (r"\\supp(?![a-zA-Z])", r"\\mathrm{supp}"), (r"\\Supp(?![a-zA-Z])", r"\\mathrm{Supp}"),
       (r"\\K(?![a-zA-Z])", r"\\mathcal{K}"), (r"\\cA(?![a-zA-Z])", r"\\mathcal{A}"), (r"\\cD(?![a-zA-Z])", r"\\mathcal{D}")]
for a, b in MAC:
    tex = re.sub(a, b, tex)
def norm(s):
    s = re.sub(r"\\label\{[^}]*\}", "", s)
    s = re.sub(r"\\tag\{[^}]*\}", "", s)
    s = s.replace(r"\notag", "").replace(r"\begin{aligned}", "").replace(r"\end{aligned}", "")
    s = s.replace(r"\begin{align*}", "").replace(r"\end{align*}", "").replace(r"\begin{align}", "").replace(r"\end{align}", "")
    s = s.replace(r"\!", "").replace("\\\\", "").replace("&", "")
    s = s.replace(r"S_\mathrm{\mathrm{tgt}}", r"S_{\mathrm{tgt}}").replace(r"H_\mathrm{\mathrm{tgt}}", r"H_{\mathrm{tgt}}").replace(r"S_\mathrm{tgt}", r"S_{\mathrm{tgt}}")
    s = s.replace(r"\textgreater", ">").replace(r"\underline v_\epsilon", r"\underline{v}_\epsilon")
    s = s.replace(r"^{\ast}", "^*").replace(r"_{\ast}", "_*")
    s = re.sub(r"\[1ex\]", "", s)
    return re.sub(r"\s+", "", s)
T = norm(tex)
bad = 0; n = 0
for f in sorted(glob.glob(f"{D}/pages/page-*.json")):
    pg = json.load(open(f))
    for it in pg["items"]:
        md = it.get("markdown", "")
        if it["kind"] not in ("text", "caption", "heading"): continue
        snippets = re.findall(r"\$\$(.+?)\$\$", md, flags=re.S)
        rest = re.sub(r"\$\$(.+?)\$\$", " ", md, flags=re.S)
        snippets += re.findall(r"\$([^$]+?)\$", rest)
        for sn in snippets:
            n += 1
            for part in re.split(r"\$\$", sn):
                p = norm(part)
                if p and p not in T:
                    bad += 1
                    print(pg["page"], it["id"], "NOT IN TEX:", part.strip()[:160])
print("snippets", n, "not found", bad)
