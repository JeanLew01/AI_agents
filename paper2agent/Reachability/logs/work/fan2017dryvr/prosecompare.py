#!/usr/bin/env python3
"""Check that every run of prose words (between math / numbers) of pages 1-17, 23-24 occurs contiguously in the authors' TeX prose."""
import json, re, os, glob
R = os.path.expanduser("~/AI_agents/paper2agent/Reachability")
D = f"{R}/paper-review/fan2017dryvr-paper/documents/s001-fan2017dryvr"
T_ = f"{R}/tex-source/fan2017dryvr"
tex = open(f"{T_}/main2.tex").read(); tex = tex[tex.index(r"\title"):tex.index(r"\input{intro}")]
for f in "intro overview examples algo experiments theory substitutivity_exp casestudies appendix".split():
    tex += open(f"{T_}/{f}.tex", encoding="utf-8").read() + "\n"
tex = re.sub(r"(?m)(?<!\\)%.*$", "", tex)
tex = tex.replace("\\toolname", "DryVR").replace("\\Simulink", "Simulink").replace("\\Mathworks", "Mathworks").replace("\\%", " ")
B = " @ "
tex = re.sub(r"\\begin\{(align\*?|algorithm)\}.*?\\end\{\1\}", B, tex, flags=re.S)
tex = re.sub(r"\\\[.*?\\\]", B, tex, flags=re.S)
tex = re.sub(r"\\Lmode\{([a-z]+)\\_([a-z]+)\}", B, tex); tex = re.sub(r"\\Lmode\{[^}]*\}", B, tex)
tex = re.sub(r"\$[^$]*\$", B, tex, flags=re.S)
tex = re.sub(r"\\(cite|ref|eqref|label|lnref|propref|proplabel|includegraphics|vspace|lnsref)(\[[^\]]*\])?\{[^}]*\}(\{[^}]*\})?", B, tex)
tex = re.sub(r"\\(begin|end)\{[^}]*\}(\[[^\]]*\])?", B, tex)
tex = re.sub(r"\\(textbf|textit|emph|section|subsection|subsubsection|paragraph|title|author|em|small|bf|caption|item|and|sc)\b", " ", tex)
tex = re.sub(r"\\[a-zA-Z]+\*?", B, tex)
tex = tex.replace("~", " ").replace("’", "'").replace("{", " ").replace("}", " ").replace("\\&", " ").replace("``", " ").replace("''", " ").replace("---", " — ").replace("\\/", "").replace("\\ ", " ")
def toks(s):
    s = s.replace("’", "'").replace("—", " — ").replace("–", " ").replace("“", " ").replace("”", " ").replace("®", " ")
    return re.findall(r"[A-Za-zö]+(?:['-][A-Za-zö]+)*|@|\d+|[\[\]]", s)
TT = [t.lower() for t in toks(tex)]
TJ = " " + " ".join(TT) + " "
bad = n = 0
for f in sorted(glob.glob(f"{D}/pages/page-*.json")):
    pg = json.load(open(f))
    if 18 <= pg["page"] <= 22: continue
    for it in pg["items"]:
        if it["kind"] not in ("text", "caption", "heading"): continue
        if "-alg" in it["id"] or "tnote" in it["id"]: continue
        md = it.get("markdown", "")
        md = re.sub(r"\$\$.*?\$\$", B, md, flags=re.S); md = re.sub(r"\$[^$]*\$", B, md)
        md = md.replace("**", " ").replace("*", " ").replace("#", " ").replace("&emsp;", " ")
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
