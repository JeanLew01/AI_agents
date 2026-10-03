#!/usr/bin/env python3
"""Check that every math snippet of the reviewed pages occurs (after macro expansion and whitespace removal) in the authors' TeX source."""
import json, re, os, glob
R = os.path.expanduser("~/AI_agents/paper2agent/Reachability")
D = f"{R}/paper-review/gruenbacher2022gotube-paper/documents/s001-gruenbacher2022gotube"
T = f"{R}/tex-source/gruenbacher2022gotube"
tex = open(f"{T}/GoTube.tex", encoding="utf-8").read()
tex = tex[tex.index(r"\begin{abstract}"):]
tex += open(f"{T}/supplements.tex", encoding="utf-8").read()
tex = re.sub(r"(?m)(?<!\\)%.*$", "", tex)
MAC = [("calB", r"\\mathcal{B}"), ("calV", r"\\mathcal{V}"), ("calS", r"\\mathcal{S}"), ("calP", r"\\bar{p}"), ("rd", r"\\delta"), ("R", r"\\mathbb{R}"),
       ("area", r"\\operatorname{Area}")]
for a, b in MAC:
    tex = re.sub(r"\\" + a + r"(?![a-zA-Z])", b, tex)
def norm(s):
    s = re.sub(r"\\label\{[^}]*\}", "", s)
    s = re.sub(r"\\tag\{[^}]*\}", "", s)
    s = re.sub(r"\\,\{(\\?[^{}\s]+)\}\\,", r"\1", s)      # \,{=}\,  -> =
    s = re.sub(r"\\,\{(\\?[^{}\s]+)\}", r"\1", s)          # \,{<}    -> <
    s = re.sub(r"\{(<|>|=|-|:|\\in|\\approx|\\rightarrow)\}\\,", r"\1", s)
    s = re.sub(r"\{(<|>|=|-|:|\\in|\\approx|\\rightarrow)\}", r"\1", s)
    s = s.replace(r"\nonumber", "").replace(r"\hspace*{-2ex}", "")
    for env in ("aligned", "align*", "align", "split"):
        s = s.replace(r"\begin{%s}" % env, "").replace(r"\end{%s}" % env, "")
    s = s.replace(r"\,", "").replace("\\\\", "").replace("&", "").replace("~", "").replace("\\ ", "")
    s = s.replace(r"\ldots", r"\dots").replace(r"\mathbbm", r"\mathbb")
    s = s.replace(r"\frac1{", r"\frac{1}{").replace(r"\ln2", r"\ln 2")
    s = s.replace(r"\operatorname{Area}{(\mathcal{B}_0})", r"\operatorname{Area}(\mathcal{B}_0)")
    s = re.sub(r"\\eqref\{app_eq:ks-statistic\}", r"\\text{(S1)}", s)
    s = re.sub(r"\\eqref\{app_eq:DKW inequality\}", r"\\text{(S6)}", s)
    return re.sub(r"\s+", "", s)
TN = norm(tex)
bad = 0; n = 0
for f in sorted(glob.glob(f"{D}/pages/page-*.json")):
    pg = json.load(open(f))
    for it in pg["items"]:
        md = it.get("markdown", "")
        if it["kind"] not in ("text", "caption", "heading"): continue
        if "Conversion note" in md: continue
        snippets = re.findall(r"\$\$(.+?)\$\$", md, flags=re.S)
        rest = re.sub(r"\$\$(.+?)\$\$", " ", md, flags=re.S)
        snippets += re.findall(r"\$([^$]+?)\$", rest)
        for sn in snippets:
            n += 1
            p = norm(sn)
            if p and p not in TN:
                bad += 1
                print(pg["page"], it["id"], "NOT IN TEX:", sn.strip()[:200])
print("snippets", n, "not found", bad)
