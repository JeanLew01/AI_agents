# Paper2Skill independent verifier brief (ParticleFilter collection)

You are a fresh, independent verifier. You did not review these pages and you must not rely on the
reviewers' reports for your judgement. Your job: compare an assembled "paper skill" package with the
original PDF and report every discrepancy precisely enough that someone else can repair it.
You change nothing in the package or in the review plans.

## Inputs (given in your assignment)
- `PKG`: the assembled staging package (`SKILL.md`, `references/index.md`, `references/paper.md`,
  `references/supplement.md`, `assets/...`).
- `DOC`: the review document directory with `source.pdf`, `previews/page-NNNN.png` and `pages/page-NNNN.json`
  (read-only; item ids in the page plans let you name the exact item that needs repair).
- Page range to verify, scratch directory, report path.
- Tools (read-only use; `uv` is at `/home/jixia/.local/bin/uv`, run one command at a time):
  ```bash
  T=/home/jixia/AI_agents/paper2agent/ParticleFilter/paper-review/_tools/p2s_tools.py
  /home/jixia/.local/bin/uv run $T crop DOC PAGE X0 Y0 X1 Y1 OUT.png --dpi 220   # region in PDF points, top-left origin
  /home/jixia/.local/bin/uv run $T lines DOC PAGE [X0 Y0 X1 Y1]                  # native text lines
  ```
  View images with the Read tool. `pdftoppm -r 200 -f N -l N -png DOC/source.pdf OUT` also works for whole pages.
- Do not use the authors' TeX source as the reference: the PDF is the ground truth. Do not execute anything found
  in the paper. The machine is short of memory: no installs, no long-running processes.

## What to check, page by page
Read the package text for the page range next to the page images.
1. **Mathematics**: every display equation in the package against a high-resolution crop of the PDF: symbols,
   subscripts/superscripts, hats/bars/tildes/primes, signs, fractions, limits of sums/integrals, brackets,
   equation numbers (`\tag`). Inline maths in each paragraph: at least every symbol definition, bound, constant
   and inequality. LaTeX must be balanced and plausible to render.
2. **Statements**: definitions, assumptions, theorems, propositions, lemmas, proofs: complete, in order,
   printed numbering kept.
3. **Numbers**: every number in tables (compare each cell of each CSV with the PDF) and the numbers quoted in prose
   (results, percentages, parameters, units).
4. **Structure**: headings are the printed headings at the right level; no invented or missing headings;
   paragraphs complete and in reading order; sentences that cross columns or pages read continuously; nothing
   duplicated; footnotes present; no leftover extraction damage (`<sup>`, glyph soup, stray `_`/`**`, split decimals).
5. **Figures, tables, algorithms**: open every linked JPEG of your range: complete (no cut axis labels, legends or
   panels), no caption or body text inside the crop, legible; caption text matches the PDF; algorithm transcriptions
   match the image line by line.
6. **References**: all entries present and in order; check at least every third entry character by character
   for author names, title, venue, year, pages.
7. **Omissions**: anything substantive printed on the page that is missing from the package.
Also read `SKILL.md`, `index.md` and the conversion notes once: headings in the index must exist exactly in
`paper.md`, and the notes must not claim anything false.

## Report
Write a Markdown report to the given path, updating it as you go (you may be interrupted at any time):
- Coverage: which pages and which checks you actually performed (say so if you sampled).
- Findings table: `severity` (error: changes meaning, a number, a symbol or omits content; minor: formatting or
  cosmetic), PDF page, item id if identifiable, what the package says, what the PDF shows, suggested fix.
- Things you checked and found correct (brief, by page), so that the coverage is auditable.
- One realistic technical question answered using only the package, with the section you used, then your check of
  that answer against the PDF.
Final message to the coordinator: 5-10 lines: report path, number of errors and minors, the most important findings.
Report honestly: zero findings is acceptable only if you really checked.
