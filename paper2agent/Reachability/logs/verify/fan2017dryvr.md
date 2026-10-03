VERDICT: 3 findings (0 A, 1 B, 2 C)

Package: skills/fan2017dryvr-paper (paper.md 515 lines, index.md, SKILL.md, 5 image assets, 1 CSV).
Ground truth: papers/fan2017dryvr.pdf (arXiv:1702.06902v1, 25 pages), rendered with pdftoppm.

## Findings

### B1 - Figure 3 asset: panel (c) does not look like the page; the conversion note explaining it is not supported by the PDF
- Location: `assets/figure/figure-3.jpg` (linked from "4.1 Experiments on trace containment reasoning", `[Figure 3](../assets/figure/figure-3.jpg)`), PDF p. 17; and Conversion notes, "Layout decisions": "The reach tubes of Figure 3(c) are drawn with transparency and appear as semi-transparent overlapping bands in the crop; other PDF renderers show an opaque gray band."
- Package asset shows: "cruise" panel = blue band with vertical purple/blue stripes, then a striped red band; "em_brake" panel = translucent layers: pale red (about 0.1 to -0.5), blue-purple (-0.5 to -2), purple-gray (-2 to about -7.6), brown-gray (-7.6 to -9), pale red (-9 to -10). No band is plain gray.
- PDF page (pdftoppm, 260 dpi crop of the figure and 400 dpi crop of panel (c)): solid, opaque colours with no stripes. "cruise" = solid blue for x in [0, 3.5], solid red for x in [3.5, 4.5]; "em_brake" = solid red (0.1 to -0.5), solid blue (-0.5 to -2), solid gray (-2 to -9), solid red (-9 to -10.1). This is what the text on p. 17 describes ("reachtubes for $G_1$ in red ... contain the reachtubes for $G_2$ (in blue and gray)").
- Why I think the asset, not pdftoppm, is the outlier: I scanned the PDF with python3 (raw bytes plus all 150 Flate streams, object streams included) for alpha settings. The only ExtGState dictionaries are `<< /Type /ExtGState /OPM 1 >>`; there is no `/CA` or `/ca` entry anywhere. The only two soft masks (`/SMask 558 0 R`, `/SMask 559 0 R`) belong to the two raster images 848x249 and 840x461, i.e. the graph drawings (a) and (b), not the plot (c). So the plot has no transparency in the file; the translucent, striped look is an artefact of the renderer used for the crop (anti-aliasing of many thin filled shapes).
- Suggested fix for the reviewer: re-crop Figure 3 from a pdftoppm render and correct or drop the "drawn with transparency" sentence. Parts (a), (b), the sub-captions and all four edges of the asset are fine.
- Confidence: high for what pdftoppm prints (400 dpi) and for the absence of alpha in the file; "unsure" only in the sense that I did not view the PDF in a third renderer.

### C1 - index.md: "with proofs" overstated for Section 4
- Location: `references/index.md`, row "4 Reasoning principles for trace containment": "Propositions 4.1-4.3 and Theorem 4.4 (sequential composition with itself) with proofs".
- PDF pp. 15-16 (260 dpi): proofs are printed only for Proposition 4.1 and Theorem 4.4. Propositions 4.2 and 4.3 have no proof (paper.md is correct here; only the index wording is loose).

### C2 - index.md: no row for the heading "A Appendix"
- paper.md has `## A Appendix` (line 447, PDF p. 23 prints "A Appendix"); index.md lists A.1, A.2, A.3 but not the parent heading. Harmless for navigation.

## Points the task asked me to confirm
- Mode-set symbol: the PDF prints the upright text letter "Ł" (L with stroke) everywhere (checked at 260 dpi on pp. 2, 4, 5, 6, 7, 10, 11, 14, 15, 16, 17). The package's `$\text{Ł}$` and its note are correct. (pdftotext extracts it as "L".)
- Relative completeness: confirmed. This version prints no relative-completeness theorem. Pp. 12-13 have only the run-in paragraph "Correctness" ("we can prove the soundness and relative completeness of Algorithm 2. This analysis closely follows the proof of Theorem 19 and Theorem 21 in [20].") followed by Theorem 3.2 (soundness only).
- PED condition split across pp. 10/11: the package's single piece `$|\tau_1(t) = \tau_2(t)| \leq |\tau_1(t_{i-1}) - \tau_2(t_{i-1})| Ke^{\gamma_i t}$` matches the two halves exactly, including the printed "=" inside the norm and the exponent $\gamma_i t$.
- Proposition 3.1: "$k \geq \frac{1}{\epsilon}\ln\frac{1}{\delta}$", "probability $\geq 1-\delta$", "$\mathsf{err}_{\mathcal{D}}(a,b) < \epsilon$" all match p. 10.
- Table 1 "9 x 7": 9 CSV rows (header + 8) x 7 columns; Model cells repeated in both rows as the note says.

## Coverage
- Theorem-like blocks checked symbol by symbol at 260 dpi: 15 of 15 (Definitions 2.1, 2.2, 2.4, 2.6, 2.7; Propositions 2.3, 2.5, 2.9, 3.1, 4.1, 4.2, 4.3; Remark 2.8; Theorems 3.2, 4.4), plus the unnumbered discrepancy-function definition (conditions (a), (b)). Numbers and titles of all blocks match. The three proofs (Prop. 3.1, Prop. 4.1, Thm. 4.4) checked step by step. No discrepancy.
- Displays checked: 9 of 9 (eq. (1), eq. (2), three ReachTube/Reach/Reach^v definitions, GED form, GED inequality, log form, PED form) plus the inline PED condition. The tags (1) and (2) are on the right equations.
- Algorithm lines: Algorithm 1 caption + 13 lines, Algorithm 2 caption + "initially" + 11 lines; numbering, nesting depth, conditions and assignments all match (including upright "Order" in line 3, $\mathcal{I}$ vs $I$, plain "(x,l,t)").
- Table cells: 63 of 63 (CSV) match p. 14; Markdown table in paper.md is identical to the CSV (script check); caption verbatim.
- Figures/assets: 5 of 5 opened and compared on all four edges with the page (figure-1, figure-2, figure-3, algorithm-1, algorithm-2). None is cut, none contains foreign text; tick labels, mode titles and sub-captions are inside the crops. Captions of Figures 1-3 verbatim. Only issue: B1.
- References: 56 of 56 entries present once, in order (script) and compared entry by entry with 200 dpi renders of pp. 18-22 plus a word/number diff; accents (Ivančić, Čerāns, Ábrahám, Joël, Donzé, Bjørner), URLs of [31], [46], [47], page ranges and years all match. No finding, so no 250 dpi re-crop was needed there.
- Completeness and order: word-level diff of pdftotext (all 25 pages, 8,666 tokens of 3+ letters and all numbers; second pass with every token) against paper.md: no dropped or duplicated passage, no number differing; the only differences are math tokenisation, hyphenation at line ends, page numbers and the moved floats. All 26 headings are real, correctly numbered and nested. Sentences across every page break (2/3, 8/9, 10/11, 11/12, 12/13, 13/14, 14/15, 15/16, 16/17, 23/24) read continuously.
- Prose read word for word against 260 dpi crops: pp. 4-17 and 23-25 completely; pp. 1-3 partly by crop (title block, p. 2 both halves, "Automotive applications" on p. 3) and fully by the text-layer diff.
- Index: 25 of 25 "Exact heading" entries exist exactly once in paper.md; all 6 asset links resolve.
- Conversion notes: every "printed like this" claim checked on the crops and is true ('=' in the two norms; $\gamma_i t$ vs $\gamma_i(t-t_{i-1})$; Def. 2.2(c)(i) "$(v,u_j) \in R$"; stray ")" in Def. 2.4(a) and math-italic "otherwise"; Def. 2.7 4-tuple without vlab; plain $U$ in Thm. 3.2; "the transition $G$", "$\gets$" in line 5; GraphReach($\mathcal{H}$) without $S$; "shown in 2"; Powertrn/Powertrain; "venchmarks"; "$x$-axis" twice in A.1; "seprator", "can used to", "“Safe” of “Unsafe”", "was been proved", "with the the", "$S_{\mathsf{test}}$ in and for"). The one note I could not confirm is the transparency sentence (B1).
- Two questions answered from the package only (SKILL.md -> index.md -> heading):
  1. "How many samples make the learned separator wrong on less than an $\epsilon$ fraction with probability at least $1-\delta$?" Index row "3.1.1 Learning linear separators." -> Proposition 3.1: $k \geq \frac{1}{\epsilon}\ln\frac{1}{\delta}$; proof bound $(1-\epsilon)^k \leq e^{-\epsilon k} \leq \delta$. PDF p. 10: same.
  2. "When does safety under $G$ carry over to $G$ composed with itself $i$ times?" Index row "4 Reasoning principles for trace containment" -> Theorem 4.4: if $\mathsf{Reach}^{v_{\mathsf{term}}}_{\mathcal{H}_1} \subseteq \Theta$ then $\mathsf{Reach}_{\mathcal{H}_i} \subseteq \mathsf{Reach}_{\mathcal{H}_1}$ for all $i$. PDF p. 16: same. (Also checked from the CSV: Merge3 safe row = 4 refinements, 197.6s; p. 14 agrees.)

## Not checked / caveats
- Italic emphasis was compared only where it fell inside a crop I was reading for content; I did not audit every emphasised word on pp. 1-3.
- "semi-group property" (p. 15) is broken at a line end in the PDF ("semi-" / "group"), so the hyphen in the package cannot be confirmed or refuted from the page.
- The statement in the notes that the paper appeared at CAV 2017 is outside the PDF and was not checked.
- The authors' TeX under tex-source/ was not used.
- Process note: I ran `pdffonts` once (read-only, not on the brief's tool list); nothing depends on its output. Everything else used python3, pdftoppm and pdftotext, one process at a time; all renders and scripts were deleted by literal path and my work folder removed. Nothing outside OUT and TMP was written.
