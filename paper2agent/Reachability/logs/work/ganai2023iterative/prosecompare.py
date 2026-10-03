#!/usr/bin/env python3
"""Check that every run of prose words (between math / citations / numbers) in the reviewed pages occurs contiguously in the authors' TeX source prose."""
import json, re, os, glob
R = os.path.expanduser("~/AI_agents/paper2agent/Reachability")
D = f"{R}/paper-review/ganai2023iterative-paper/documents/s001-ganai2023iterative"
tex = open(f"{R}/tex-source/ganai2023iterative/main.tex", encoding="utf-8").read()
tex = tex[tex.index(r"\title"):]
tex = "\n".join(re.sub(r"(?<!\\)%.*$", "", l) for l in tex.split("\n"))
B = " @ "
tex = re.sub(r"\\begin\{(align\*?|equation\*?|algorithmic|tabular)\}.*?\\end\{\1\}", B, tex, flags=re.S)
tex = re.sub(r"\\\[.*?\\\]", B, tex, flags=re.S)
tex = re.sub(r"\$[^$]*\$", B, tex, flags=re.S)
tex = re.sub(r"\\(cite|ref|eqref|label|includegraphics|vspace\*?|hspace|bibitem|url|usepackage)(\[[^\]]*\])?\{[^}]*\}", B, tex)
tex = re.sub(r"\\(begin|end)\{[^}]*\}(\[[^\]]*\])?(\{[^}]*\})?", B, tex)
tex = re.sub(r"\\(textbf|textit|emph|em|section|subsection|subsubsection|paragraph|title|author|texttt|small|caption|underline|newblock)\b", " ", tex)
tex = tex.replace(r"\&", " ").replace(r"\'", "").replace(r"\c", "")
tex = re.sub(r"\\[a-zA-Z]+\*?", B, tex)
tex = tex.replace("~", " ").replace("’", "'").replace("{", "").replace("}", "").replace("``", '"').replace("--", " ")
def toks(s):
    s = s.replace("’", "'").replace("–", " ").replace("“", '"')
    return re.findall(r"[A-Za-zíáéç]+(?:['-][A-Za-zíáéç]+)*|@|\d+|[\[\]]", s)
TT = [t.lower() for t in toks(tex)]
TJ = " " + " ".join(TT) + " "
bad = n = 0
for f in sorted(glob.glob(f"{D}/pages/page-*.json")):
    pg = json.load(open(f))
    for it in pg["items"]:
        if it["kind"] not in ("text", "caption", "heading"): continue
        md = it.get("markdown", "")
        if md.startswith("Conversion note"): continue
        md = re.sub(r"\$\$.*?\$\$", B, md, flags=re.S); md = re.sub(r"\$[^$]*\$", B, md)
        md = md.replace("*", "").replace("#", " ").replace("&emsp;", " ").replace("`", " ")
        run = []
        seq = [t.lower() for t in toks(md)] + ["@"]
        for t in seq:
            if t == "@" or t.isdigit() or t in "[]":
                if len(run) >= 2:
                    n += 1
                    if " " + " ".join(run) + " " not in TJ:
                        bad += 1; print(pg["page"], it["id"], "NOT IN TEX:", " ".join(run)[:170])
                run = []
            else:
                run.append(t)
print("runs checked", n, "not found", bad)
