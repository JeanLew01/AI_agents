VERDICT: 1 findings (0 A, 0 B, 1 C)

Package: skills/ganai2023iterative-paper (paper.md 1045 lines, index.md, 15 image assets, 2 CSV tables)
PDF: papers/ganai2023iterative.pdf, 33 pages. Package files were not modified (mtime unchanged).

## Findings

### C1 (cosmetic) - Table 1 cells: 'max' / 'min' subscripts are italic in the table, upright in print
- Location: paper.md, heading "A Notation", Markdown table rows `| $H_{max}$ | upper bound of function $h$ |`,
  `| $H_{min}$ | ...`, `| $λ_{max}$ | ...`, `| $R_{max}$ | ...`; same four cells in
  assets/supp_table/supplementary-table-1.csv. PDF p. 14.
- Package: `$H_{max}$`, `$H_{min}$`, `$λ_{max}$`, `$R_{max}$` (plain letters in the subscript, so a
  renderer shows italic m-a-x / m-i-n).
- PDF: H_max, H_min, lambda_max, R_max with upright (operator) 'max' / 'min', as everywhere else in the paper.
- The "Conversion note for Table 1" directly below gives the correct forms (`$H_{\max}$` etc.), so no
  information is lost; only the table cells / CSV differ typographically.
- Confirmed on a 260 dpi crop of the table (p. 14).

No A or B finding. Everything else I compared matches the PDF.

## Coverage

Method: paper.md read completely, in order; every page rendered one crop at a time (text 240-260 dpi,
two inline formulas on p. 20 at 700 dpi; figure regions 170-230 dpi next to the asset) and compared with the package text. Text-layer cross-checks by script (pdftotext, word 4-grams).

- Theorem-like blocks checked symbol by symbol: 21 = Definitions 1-5, Theorem 1, Propositions 1-2,
  Theorem 2, assumptions A1-A3 (p. 4-7); appendix restatements Theorem 3, Propositions 3-4, Theorem 4
  (p. 15-16; printed numbers and the 'Main paper' wording correct); informal Lemmas 1-5 (p. 19-22).
  Numbers, titles, quantifiers, inequality directions, italic vs calligraphic S all as printed.
- Displays checked: all 49 display blocks of paper.md, including the 14 tagged ones: (CMDP), (RCRL),
  (RESPO), (1)-(11); every tag sits on the right display. Proof displays compared line by line:
  theta_{k+1} (4 lines), delta theta_{k+1} (4), delta theta_eps (5), Lemma 1 bound (5) + six bounds,
  Lemma 2 chain (6), contraction chain (5), omega_{k+1} (3), delta omega_{k+1} (11), lambda_max
  derivation (5), proof of Theorem 3 (5).
- `[Q] (s,a)` / `[Q_c] (s,a)` / `[p] (s)`: apart from the inserted space the three operator formulas
  are exactly as printed (second Bellman operator is printed as B without subscript c, as the note says).
- Equations (10)-(11) colour note: checked against the page (230 dpi crop and a 600 dpi zoom). Red -V^pi(s); blue
  lambda_sc.(V_sc^pi(s) - chi); brown lambda_hc2.V_hc2^pi(s)].(1 - p_hc2(s)) + V_hc2^pi(s).p_hc2(s);
  teal lambda_hc1.V_hc1^pi(s)].(1 - p_hc1(s)) + V_hc1^pi(s).p_hc1(s); in (11) red / blue / brown / teal on
  the four terms. The note is correct.
- Algorithm 1: 14 printed lines (title, 2 Require lines, lines 1-11) vs transcription and vs asset:
  numbering, nesting, conditions, assignments match. Asset algorithm-1.jpg is the whole float (three
  rules, all lines); right edge is tight (3 px after 'zeta_1(k),') but nothing is cut.
- Tables: 90 cells. Table 1: 19 rows x 2 (38 cells) vs CSV, Markdown table and LaTeX note (only C1).
  Table 2: header + 25 rows x 2 (52 cells) vs CSV and Markdown table: all match (three 'Linear Decay
  ... -> 0' schedules, REF rate '1e-4 -> 0' without 'Linear Decay', two-line last value, four bold group
  titles); the conversion note under the table is accurate.
- Figures: 14 figures + the algorithm = 15 assets, each opened and compared with the page on all four
  edges: figure-1..6, supplementary-figure-7..14. All complete (all panels, titles, tick labels with
  minus signs, 1e6 / x10^n offsets, legends, colour bars), no foreign text, side-by-side Figures 4 / 5
  correctly separated. A script check also shows white margin on every edge of every asset (min 3 px).
  All 14 captions verbatim, labels correct. figure-3.jpg is small (1006x143 px) but the embedded figure
  in the PDF is equally coarse (checked at 300 dpi), so not a finding.
- Float placement differs from the page only as declared in the notes (Figure 1 under '6 Experiments',
  Figures 3-6 after the paragraphs that discuss them, Figure 7 after the C.4.1 paragraph).
- Completeness / order: script comparison of all 33 pages found no dropped or altered prose (only math,
  figure-internal text, page numbers, line-break hyphens differ); a duplicate scan found only passages
  the paper itself repeats (multi-drone paragraph in 6.2 and D.2, restated theorem / propositions,
  repeated 'Vanilla PPO' sentences, Figure 3 / 12 captions). Sentences across page breaks (p2/3, p8/9,
  p9/10, p15/16) are joined correctly. No footnotes in the paper; first-page footer omitted as stated.
  References: 60 entries, each once and in order, every entry read against p. 11-13.
- Prose spot check: all 33 pages; in practice every paragraph was read against the crop (pages 26-32:
  the discussion paragraphs under each figure).
- Headings and index: 47 headings real, numbered and nested as printed; 46 index rows each point to an
  existing heading with the stated content; 17 asset links resolve.
- Two questions answered from the package only (SKILL.md -> index.md -> paper.md):
  1. "Which step-size conditions does A1 impose and which component runs on which time scale?" Index row
     '5.4 Convergence Analysis' -> sum zeta_i(k) = infinity, sum zeta_i(k)^2 < infinity for i = 1..4,
     zeta_j(k) = o(zeta_{j-1}(k)) for j = 2,3,4; critics zeta_1 (fastest), policy zeta_2, REF zeta_3,
     Lagrange multiplier zeta_4 (slowest). Same on PDF p. 7.
  2. "What output activation and learning rate does the REF network use?" Index row 'D.3
     Hyperparameters/Other Details' -> supplementary-table-2.csv: sigmoid; 1e-4 -> 0. Same on PDF p. 25.
- Conversion notes: every 'kept as printed' claim was checked on the page and is what the PDF prints:
  arg min over V_c (4.1) vs V_h (4.2); italic S in S^pi_f (Prop. 2), S_I (RESPO), S_v (REF update,
  appendix proofs); subscript eta on the REF gradient (App. B); 'h(s_t|s_0 = 0, pi) = 0'; second Bellman
  operator without subscript c; 'Q_h' in Lemma 1; one-argument 'Q^{pi_theta_k}(s_i)' in Lemma 2;
  unbalanced 'Upsilon_Theta[M(theta]'; 'nabla_Omega' after Eq. (9); 'gradient for Equation is:';
  surplus ']' ending the delta-omega display; 'Assumption 1' in 6.3; the listed misspellings (each
  found once in the PDF text layer; 'the the' and 'of of' at the stated places). No note mis-describes
  the PDF.

## Not checked / limits

- Curve data inside the training-curve figures were not digitised or compared numerically (the package
  keeps them as images only); I compared assets with the page visually.
- Page 32 (Figure 14) was compared on a 170 dpi full-page render; its caption was read on a 260 dpi
  strip. Reference pages 11-13 were read at 220-250 dpi (plus the text-layer comparison).
- The note's statement that a script found all 606 math snippets identical to the TeX source was not
  re-run (TeX is not ground truth; I used it only once, to locate two inline formulas on p. 20).
- Process note: my image viewer keeps only the most recent ~40 pictures, so I could not keep the whole
  paper in view at once; I worked page by page and re-viewed pages 3-8, 14-16 and 18-33 (definitions,
  theorems, proofs, both tables, appendix figures) a second time at the end. Both passes agree.
