#!/usr/bin/env python3
"""Compile every $...$ and $$...$$ of a built paper.md with pdflatex to catch LaTeX syntax errors
and to allow a visual comparison of the display formulas with the PDF. usage: mathcheck.py paper.md"""
import re, subprocess, sys
from pathlib import Path
md = Path(sys.argv[1]).read_text(encoding="utf-8")
out = Path(__file__).parent / "texcheck"
displays = re.findall(r"\$\$(.+?)\$\$", md, flags=re.S)
rest = re.sub(r"\$\$(.+?)\$\$", " ", md, flags=re.S)
inlines = re.findall(r"\$([^$\n]+?)\$", rest)
assert rest.count("$") == 2 * len(inlines), "unbalanced inline $"
uniq = list(dict.fromkeys(inlines))
tex = [r"\documentclass[10pt]{article}\usepackage[margin=2cm]{geometry}\usepackage{amsmath,amssymb,mathrsfs}\begin{document}",
       r"\section*{Displays}"]
for i, d in enumerate(displays, 1):
    tex.append(f"\\noindent D{i}:\n\\[\n{d.strip()}\n\\]")
tex.append(r"\section*{Inline}\raggedright")
for i, m in enumerate(uniq, 1):
    tex.append(f"\\noindent I{i}: ${m}$\\par")
tex.append(r"\end{document}")
(out / "math.tex").write_text("\n".join(tex), encoding="utf-8")
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "math.tex"], cwd=out, capture_output=True, text=True)
errs = [l for l in r.stdout.splitlines() if l.startswith("!") or "Undefined" in l or "Missing" in l]
print(f"displays={len(displays)} inline={len(inlines)} unique_inline={len(uniq)} pdflatex_rc={r.returncode}")
print("\n".join(errs) if errs else "no LaTeX errors")
if r.returncode: print(r.stdout[-1500:])
