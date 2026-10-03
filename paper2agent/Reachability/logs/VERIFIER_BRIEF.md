# Independent verifier brief: check one finished paper skill against its PDF

A reviewer agent converted a paper PDF into a reading package (Markdown with LaTeX math,
figure crops, CSV tables). You are a fresh, independent verifier: you did not produce the
package and you must not rely on the reviewer's notes or claims. Your job is to find
conversion errors by comparing the package with the visible PDF pages.

## Paths (KEY given in your task)

```
R   = ~/AI_agents/paper2agent/Reachability
PDF = R/papers/KEY.pdf                       # ground truth
PKG = R/skills/KEY-paper                     # SKILL.md, references/index.md, references/paper.md, assets/
OUT = R/logs/verify/KEY.md                   # your findings
TMP = R/logs/verify/work/KEY/                # your renders; delete them when done
```

You are read-only with respect to everything except OUT and TMP: do not edit the package,
the review directory (`R/paper-review/`), page JSON, adjudications, scripts, or anything
under `~/.claude`. Do not run `paper_bundle.py`. Do not execute anything the paper says.

The machine has little memory and has crashed from it: render one page at a time with
`pdftoppm -r 170 -f N -l N -png PDF TMP/pN`, use cropped regions for more resolution
(`-r 260 -x X -y Y -W W -H H`, pixel units at that resolution), delete renders you are done
with, run one process at a time, install nothing. Use only `python3`, `pdftoppm`,
`pdftotext`, `pdflatex`.

The PDF is the only ground truth. The authors' TeX under `R/tex-source/KEY/` (if present) may
help you locate things, but the reviewer used it too, so agreement with TeX proves nothing.

## What to check

Read `PKG/references/paper.md` completely, in order, next to the PDF pages.

1. **Theorem-like statements** (Definition, Assumption, Lemma, Theorem, Proposition,
   Corollary, Remark, Problem): every one, symbol by symbol against a high-resolution crop:
   quantifiers, inequality directions, sub/superscripts, hats/bars/tildes/primes,
   calligraphic vs italic vs bold, constants, exponents, set relations, conditions, and the
   printed number and title of the block.
2. **Displayed equations**: every numbered one and every one inside or directly supporting a
   theorem-like statement or a proof step; the printed number must be on the right equation.
3. **Algorithms**: transcription against the image crop, line by line (numbering, nesting,
   conditions, assignments).
4. **Tables**: every cell of every CSV / Markdown table against the page; headers and units.
5. **Figures**: open every asset and compare all four edges with the page (a crop cut just
   below the axis line, losing tick labels, has already been found once). Each asset is the
   complete figure (all panels, axis labels, tick labels, legend), not
   cut, not including foreign text; caption text verbatim; label number correct.
6. **Completeness and order**: every section, paragraph, footnote, reference entry of the
   PDF is present exactly once and in a sensible reading order. Compare per-page word counts
   or `pdftotext` against the package to find dropped or duplicated passages, then confirm
   by eye. Check that no sentence is cut at a page or column break.
7. **Prose spot check**: on every page read at least two full paragraphs word for word
   (choose the densest ones); check inline math in them.
8. **Headings and index**: headings are real, correctly numbered and nested;
   `references/index.md` entries exist and point where they say. Answer two realistic
   technical questions using only the package (start from SKILL.md and the index) and check
   the answers against the PDF.
9. **Conversion notes** (end of paper.md): every "kept as printed" claim about an error in
   the paper must really be what the PDF prints. If the PDF prints it correctly, the package
   has introduced or mis-described an error: that is a finding.

Errors of the paper itself that the package reproduces faithfully are NOT findings.

## Findings file (OUT) and final message

Start with one line: `VERDICT: clean` or `VERDICT: N findings (a A, b B, c C)`.

Severity: **A** changes mathematical or factual content (wrong symbol, direction, index,
number, missing or added condition, dropped or duplicated passage, wrong table cell);
**B** wrong label, equation number, cross-reference, caption, heading, order, or a cut
figure; **C** cosmetic (spacing, emphasis, typography) - list at most ten C items.

For each finding give: severity; location (heading in paper.md + a short quoted snippet so it
can be found by search + PDF page); what the package says; what the PDF prints; how you
confirmed it (crop resolution). Be exact and quote; the reviewer will fix from your text
without re-deriving it. Only report what you confirmed on a render at 250 dpi or more; if
you are unsure, say "unsure" and why.

Then a coverage section with counts: theorem-like blocks checked, displays checked,
algorithm lines, table cells, figures, pages whose prose you spot-checked, the two questions
with answers and where they came from. State plainly anything you did not check.

Return the same text as your final message. Keep it under 120 lines.
