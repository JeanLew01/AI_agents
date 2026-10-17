#!/usr/bin/env python3
"""Compile every $...$ and $$...$$ of a built paper.md with pdflatex, in small batches, to catch LaTeX syntax errors.
Markdown table rows (Unicode cells) are skipped. usage: mathcheck.py paper.md"""
import re, subprocess, sys
from pathlib import Path
md = Path(sys.argv[1]).read_text(encoding="utf-8")
md = "\n".join(l for l in md.split("\n") if not l.startswith("|"))
out = Path(__file__).parent / "texcheck"
displays = re.findall(r"\$\$(.+?)\$\$", md, flags=re.S)
rest = re.sub(r"\$\$(.+?)\$\$", " ", md, flags=re.S)
inlines = re.findall(r"\$([^$\n]+?)\$", rest)
assert rest.count("$") == 2 * len(inlines), ("unbalanced inline $", rest.count("$"), len(inlines))
uniq = list(dict.fromkeys(inlines))
items = [("D%d" % i, "\\[\n%s\n\\]" % d.strip()) for i, d in enumerate(displays, 1)] + [("I%d" % i, "$%s$\\par" % m) for i, m in enumerate(uniq, 1)]
print(f"displays={len(displays)} inline={len(inlines)} unique_inline={len(uniq)}")
N = 120; allok = True
for k in range(0, len(items), N):
    tex = [r"\documentclass[10pt]{article}\usepackage[margin=1.5cm]{geometry}\usepackage{amsmath,amssymb}\begin{document}\raggedright"]
    for lab, body in items[k:k+N]:
        tex.append(f"\\noindent {lab}: {body}")
    tex.append(r"\end{document}")
    (out / "math.tex").write_text("\n".join(tex), encoding="utf-8")
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "math.tex"], cwd=out, capture_output=True, text=True, errors="replace")
    errs = [l for l in r.stdout.splitlines() if l.startswith("!")]
    print(f"batch {k//N+1}: items {k+1}-{min(k+N,len(items))} rc={r.returncode} errors={len(errs)}")
    if errs:
        allok = False
        lines = r.stdout.splitlines()
        for i, l in enumerate(lines):
            if l.startswith("!"): print("   ", l, "|", " ".join(lines[i+1:i+4])[:200])
print("no LaTeX errors" if allok else "ERRORS")
