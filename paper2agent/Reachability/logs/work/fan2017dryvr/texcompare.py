#!/usr/bin/env python3
"""Check that every math snippet of the reviewed pages occurs (after macro expansion and whitespace removal) in the authors' TeX source."""
import json, re, os, glob
R = os.path.expanduser("~/AI_agents/paper2agent/Reachability")
D = f"{R}/paper-review/fan2017dryvr-paper/documents/s001-fan2017dryvr"
T_ = f"{R}/tex-source/fan2017dryvr"
tex = ""
for f in "intro overview examples algo experiments theory substitutivity_exp casestudies appendix".split():
    tex += open(f"{T_}/{f}.tex", encoding="utf-8").read() + "\n"
tex = re.sub(r"(?<!\\)%.*", "", tex)
def braced(name, repl):
    global tex
    tex = re.sub(r"\\" + name + r"\{((?:[^{}]|\{[^{}]*\})*)\}", repl, tex)
for _ in range(2):
    braced("reachtube", r"\\mathsf{ReachTube}_{\1}"); braced("reach", r"\\mathsf{Reach}_{\1}"); braced("Reach", r"\\mathsf{Reach}_{\1}")
    braced("paths", r"\\mathsf{Paths}_{\1}"); braced("traces", r"\\mathsf{Trace}_{\1}"); braced("execs", r"\\mathsf{Execs}_{\1}")
    braced("pathof", r"\\mathsf{path}(\1)"); braced("auto", r"\\mathsf{\1}"); braced("Lmode", r"\\mathsf{\1}")
MAC = [("TL", r"\\mathcal{TL}"), ("L", r"\\text{Ł}"), ("V", r"\\mathcal{V}"), ("E", r"\\mathcal{E}"), ("H", r"\\mathcal{H}"), ("U", r"\\mathcal{U}"), ("I", r"\\mathcal{I}"),
       ("reals", r"\\mathbb{R}"), ("nnreals", r"\\mathbb{R}_{\\geq 0}"), ("plreals", r"\\mathbb{R}_{+}"),
       ("vertlab", r"\\mathit{vlab}"), ("edgelab", r"\\mathit{elab}"), ("modemap", r"\\mathit{lmap}"), ("simulator", r"\\mathit{sim}"),
       ("dom", r"\\mathit{dom}"), ("seqcomp", r"\\circ"), ("GraphReach", r"\\mathit{GraphReach}"), ("VerInit", r"\\mathit{VerInit}"), ("computeRT", r"\\mathit{ReachComp}")]
for a, b in MAC:
    tex = re.sub(r"\\" + a + r"(?![a-zA-Z])", b, tex)
for m_ in "fstate lstate ltime fmode lmode".split():
    tex = re.sub(r"\\" + m_ + r"(?![a-zA-Z])", r"\\mathit{" + m_ + "}", tex)
tex = re.sub(r"_\{\\sf ([a-z]+)\}", r"_{\\mathsf{\1}}", tex)
tex = re.sub(r"_\{\\sf init,\s*\\ell\}", r"_{\\mathsf{init},\\ell}", tex)
tex = re.sub(r"\$\s*\$", " ", tex)
tex = re.sub(r"\{\\sf ([^{}]*)\}", r"\\mathsf{\1}", tex)
tex = re.sub(r"\{\\cal ([^{}]*)\}", r"\\mathcal{\1}", tex)
tex = re.sub(r"\{\\sf\s+([a-z]+)\}", r"\\mathsf{\1}", tex)
def norm(s):
    s = re.sub(r"\\label\{[^}]*\}", "", s)
    s = re.sub(r"\\tag\{[^}]*\}", "", s)
    s = s.replace(r"_{\ast}", "_*").replace("{\\mathsf{id}}", "\\mathsf{id}").replace("{\\mathsf{init}}", "\\mathsf{init}").replace("{\\mathsf{term}}", "\\mathsf{term}")
    s = s.replace("{\\mathcal{D}}", "\\mathcal{D}").replace("~", "\\ ")
    s = s.replace("\\mbox", "\\text").replace("\\textrm{max}", "\\mathrm{max}")
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
            p = norm(sn)
            if p and p not in T:
                bad += 1
                print(pg["page"], it["id"], "NOT IN TEX:", sn.strip()[:200])
print("snippets", n, "not found", bad)
