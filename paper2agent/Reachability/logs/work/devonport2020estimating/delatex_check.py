#!/usr/bin/env python3
"""Independent check of the LaTeX transcription.

For every source line that the tool's line check reports as missing, convert the reviewed page
markdown from LaTeX back to the glyph order of the PDF text layer (\\epsilon -> ϵ, \\hat{R} -> R, ...)
and test whether the line's alphanumeric skeleton now occurs in the page.  Lines that still fail are
printed; they are the stacked-fraction / display fragments that must be justified by eye.
Usage: delatex_check.py <staging-or-final package dir>
"""
import json, os, re, sys, unicodedata
R = os.path.expanduser("~/AI_agents/paper2agent/Reachability")
D = f"{R}/paper-review/devonport2020estimating-paper/documents/s001-devonport2020estimating"

GREEK = {r"\epsilon": "ϵ", r"\delta": "δ", r"\theta": "θ", r"\Theta": "Θ", r"\Phi": "Φ", r"\phi": "φ",
         r"\infty": "∞", r"\times": "×", r"\log": "log", r"\det": "det", r"\min": "min", r"\arg": "arg"}
DROP = [r"\left", r"\right", r"\lceil", r"\rceil", r"\quad", r"\dots", r"\blacksquare", r"\subset", r"\in",
        r"\le", r"\ge", r"\to", r"\|", r"\\", r"\begin{aligned}", r"\end{aligned}", "&emsp;", "&"]

def delatex(s):
    s = re.sub(r"\\tag\{(\d+)\}", r"(\1)", s)
    s = s.replace(r"\hat{R}", "\u02c6R")            # the text layer has a modifier circumflex before R
    s = s.replace(r"_{i=1}^{N}", "N i=1")            # text layer order: superscript line first
    s = re.sub(r"\\underset\{(.*?)\}\{\\text\{(.*?)\}\}", r"\2 \1", s)
    for _ in range(3):
        s = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"\1 \2", s)
        s = re.sub(r"\\(?:mathbb|mathcal|mathrm|hat|dot|text)\{([^{}]*)\}", r"\1", s)
    for k in sorted(GREEK, key=len, reverse=True):
        s = s.replace(k, GREEK[k])
    for k in sorted(DROP, key=len, reverse=True):
        s = s.replace(k, " ")
    return s

def canon(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s) if c.isalnum()).casefold()

pkg = sys.argv[1]
md = open(f"{pkg}/references/paper.md", encoding="utf-8").read()
# the published paper.md has no page markers; use the per-page intermediate render instead
ver = json.load(open(f"{D}/verification.json"))
build = json.load(open(f"{D}/build.json"))
inter = open(os.path.join(build["output"], build["paper"]), encoding="utf-8").read()
chunks = re.split(r"<!-- PDF page (\d+) -->", inter)
pages = {int(chunks[i]): chunks[i + 1] for i in range(1, len(chunks), 2)}
total = still = 0
for p in ver["pages"]:
    text = canon(delatex(pages[p["page"]]))
    for l in p["missing_lines"]:
        total += 1
        c = canon(l["text"])
        if c not in text:
            still += 1
            print(f"page {p['page']}: STILL UNMATCHED {l['text']!r}  y={l['bbox'][1]:.0f}")
print(f"{total} tool-missing lines; {total - still} match after de-LaTeX; {still} need visual justification")
