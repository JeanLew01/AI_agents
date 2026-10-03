#!/usr/bin/env python3
"""Make main.resolved.tex: comments stripped, \cite resolved to printed numbers (order of \bibitem), \E and \mathbbm expanded.
\ref's are left for manual resolution against the page."""
import re, os
T=os.path.expanduser("~/AI_agents/paper2agent/Reachability/tex-source/ganai2023iterative/main.tex")
s=open(T,encoding="utf-8").read()
keys=re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]*)\}",s)
num={k:i+1 for i,k in enumerate(keys)}
out=[]
for ln in s.split("\n"):
    ln=re.sub(r"(?<!\\)%.*$","",ln)
    out.append(ln)
s="\n".join(out)
def cite(m):
    ks=[k.strip() for k in m.group(1).split(",")]
    return "["+", ".join(str(num[k]) for k in ks)+"]"
s=re.sub(r"~?\\cite\{([^}]*)\}",lambda m:(" " if m.group(0).startswith("~") else "")+cite(m),s)
s=re.sub(r"\\E(?![a-zA-Z])",r"\\mathbb{E}",s)
s=s.replace(r"\mathbbm",r"\mathbb")
s=re.sub(r"\\vspace\*?\{[^}]*\}","",s)
s=re.sub(r"\n{3,}","\n\n",s)
open("main.resolved.tex","w",encoding="utf-8").write(s)
print(len(keys),"bibitems;", len(s.split(chr(10))),"lines")
import json; json.dump(num,open("bibnum.json","w"),indent=0)
