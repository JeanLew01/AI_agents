#!/usr/bin/env python3
"""Check that every run of prose words (between math / numbers) in the reviewed pages 1-9 occurs contiguously in the authors' TeX source prose."""
import json, re, os, glob
R = os.path.expanduser("~/AI_agents/paper2agent/Reachability")
D = f"{R}/paper-review/ouyang2026symplectic-paper/documents/s001-ouyang2026symplectic"
tex = open(f"{R}/tex-source/ouyang2026symplectic/CDC2026_sample.tex", encoding="utf-8").read()
tex = tex[tex.index(r"\title"):]
tex = re.sub(r"(?m)(?<!\\)%.*$", "", tex)
B = " @ "
tex = re.sub(r"\\begin\{(align\*?|algorithmic|figure|algorithm)\}.*?\\end\{\1\}", B, tex, flags=re.S)
tex = re.sub(r"\\\[.*?\\\]", B, tex, flags=re.S)
tex = re.sub(r"\$[^$]*\$", B, tex, flags=re.S)
tex = re.sub(r"\\(cite|ref|eqref|label)(\[[^\]]*\])?\{[^}]*\}", B, tex)
tex = re.sub(r"\\(begin|end)\{[^}]*\}(\[[^\]]*\])?", B, tex)
tex = re.sub(r"\\(textbf|textit|emph|section|subsection|subsubsection|title|author|thanks|tt|small|LARGE|bf)\b", " ", tex)
tex = re.sub(r"\\[a-zA-Z]+\*?", B, tex)
tex = tex.replace("~", " ").replace("’", "'").replace("{", " ").replace("}", " ").replace("\\&", " ")
def toks(s):
    s = s.replace("’", "'").replace("—", " — ").replace("–", " ")
    return re.findall(r"[A-Za-zö]+(?:['-][A-Za-zö]+)*|@|\d+|[\[\]]", s)
TT = [t.lower() for t in toks(tex)]
TJ = " " + " ".join(TT) + " "
bad = n = 0
for f in sorted(glob.glob(f"{D}/pages/page-*.json"))[:9]:
    pg = json.load(open(f))
    for it in pg["items"]:
        if it["kind"] not in ("text", "caption", "heading"): continue
        md = it.get("markdown", "")
        md = re.sub(r"\$\$.*?\$\$", B, md, flags=re.S); md = re.sub(r"\$[^$]*\$", B, md)
        md = md.replace("*", " ").replace("#", " ").replace("&emsp;", " ")
        run = []
        seq = [t.lower() for t in toks(md)] + ["@"]
        for t in seq:
            if t == "@" or t.isdigit() or t in "[]":
                if len(run) >= 2:
                    n += 1
                    if " " + " ".join(run) + " " not in TJ:
                        bad += 1; print(pg["page"], it["id"], "NOT IN TEX:", " ".join(run)[:150])
                run = []
            else:
                run.append(t)
print("runs checked", n, "not found", bad)
