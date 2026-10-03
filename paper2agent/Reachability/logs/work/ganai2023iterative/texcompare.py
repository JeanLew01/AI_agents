#!/usr/bin/env python3
"""Check that every math snippet of the reviewed pages occurs (after macro expansion and whitespace removal) in the
authors' TeX source. Strict pass keeps braces; snippets that fail strictly are retried with all braces removed and are
listed as 'loose only'; snippets that fail both are listed as NOT IN TEX."""
import json, re, os, glob
R = os.path.expanduser("~/AI_agents/paper2agent/Reachability")
D = f"{R}/paper-review/ganai2023iterative-paper/documents/s001-ganai2023iterative"
tex = open(f"{R}/tex-source/ganai2023iterative/main.tex", encoding="utf-8").read()
tex = tex[tex.index(r"\begin{abstract}"):]
tex = "\n".join(re.sub(r"(?<!\\)%.*$", "", l) for l in tex.split("\n"))
tex = re.sub(r"\\E(?![a-zA-Z])", r"\\mathbb{E}", tex).replace(r"\mathbbm", r"\mathbb")
def norm(s, loose=False):
    s = re.sub(r"\\label\{[^}]*\}", "", s)
    s = re.sub(r"\\tag\{[^}]*\}", "", s)
    s = re.sub(r"\\vspace\*?\{[^}]*\}", "", s)
    s = re.sub(r"\\hspace\{[^}]*\}", r"\\quad", s)
    s = re.sub(r"\\color\{[^}]*\}", "", s)
    for e in ("aligned", "align*", "align", "equation*", "equation", "split"):
        s = s.replace(r"\begin{%s}" % e, "").replace(r"\end{%s}" % e, "")
    s = s.replace(r"\[", "").replace(r"\]", "")
    s = re.sub(r"\\(mathcal|mathbb|mathfrak) ([A-Za-z0-9])", r"\\\1{\2}", s)
    s = s.replace(r"^{\ast}", "^*").replace(r"\nonumber", "")
    s = s.replace("\\\\", "").replace("&", "").replace(r"\,", "")
    s = re.sub(r"\s+", "", s)
    if loose:
        s = s.replace("{", "").replace("}", "")
    return s
T, TL = norm(tex), norm(tex, True)
bad = loose = n = 0
for f in sorted(glob.glob(f"{D}/pages/page-*.json")):
    pg = json.load(open(f))
    for it in pg["items"]:
        if it["kind"] not in ("text", "caption", "heading"): continue
        md = it.get("markdown", "")
        if md.startswith("Conversion note"): continue
        sn = re.findall(r"\$\$(.+?)\$\$", md, flags=re.S)
        rest = re.sub(r"\$\$(.+?)\$\$", " ", md, flags=re.S)
        sn += re.findall(r"\$([^$]+?)\$", rest)
        for s in sn:
            n += 1
            if s.strip() == r"\square": continue
            if norm(s) in T: continue
            if norm(s, True) in TL:
                loose += 1; print(pg["page"], it["id"], "loose only:", s.strip()[:110].replace("\n", " "))
            else:
                bad += 1; print(pg["page"], it["id"], "NOT IN TEX:", s.strip()[:200].replace("\n", " "))
print("snippets", n, "loose-only", loose, "not found", bad)
