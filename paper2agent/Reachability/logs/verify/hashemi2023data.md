VERDICT: clean

Package: skills/hashemi2023data-paper (SKILL.md, references/index.md, references/paper.md, references/supplement.md, 3 figure JPEGs, 3 table CSVs).
Ground truth: papers/hashemi2023data.pdf (arXiv:2309.09187v1, 15 pages). All 15 pages rendered one at a time at 170 dpi and read next to paper.md; every theorem-like block, numbered display, table and figure re-checked on crops at 260-500 dpi. The TeX source was not consulted.

## Findings

None (0 A, 0 B, 0 C).

## Points the task asked to confirm (all confirmed, no finding)

- Calibration-size condition, PDF p.8 (500 dpi crop): the PDF prints "ceil((L+1)delta) <= L which gives us the explicit lower bound L >= ceil((1+delta)/(1-delta))". paper.md has `L \geq \lceil \frac{1+\delta}{1-\delta} \rceil`: identical. The conversion note describes it correctly as printed. (The note's added remark that the preceding condition alone is equivalent to L >= delta/(1-delta) is the reviewer's own commentary, arithmetically correct, and is marked as such; it is not paper content.)
- Theorem 1, split by the page break 6/7 (300 dpi crops of both halves): statement joined correctly without loss or duplication at "...from the stochastic system M with | initial state s_0 ~ I. Define the inflated surrogate flowpipe,"; display X = X-bar (+) Zonotope(0, diag([0_{1xn}, R*])), R* = [R^{1*},...,R^{nK*}] (no transpose inside the theorem, transpose in the sentence before it: both as printed); Delta = 1 - nK(1-delta).
- Proof of Theorem 1 (300 dpi): Pr[R^j > R^{j*}] < 1-delta and Pr[OR ...] < nK(1-delta) are printed with strict "<"; (3) ">= 1-nK(1-delta)."; unnumbered displays with |e_{j+n}^T sigma - F^j| <= R^{j*} and e_{j+n}^T sigma in C_j(s_0); (4) and (5) as in the package, subset sign and "= X" in (5), tags on the right equations.
- Equation (7), uncaptioned float at the top of PDF p.12 (400 dpi crops, rows 1-5 and 6-12; 300 dpi crop of the initial set): all 12 rows agree symbol by symbol, including the two continuation lines of x1-dot and x2-dot, the signs (- cos(x7) sin(x9) in row 1; + cos(x7) cos(x9) and - sin(x7) cos(x9) in row 2), 9.81 terms, "- 9.81 - u_1/1.4" in row 6, the nested (sin(x8)/cos(x8)) in row 7, -0.9259 / 0.9259 / 18.5185 and u_2, u_3 in rows 10-11, x12-dot = v_12; noise index v_1..v_12 on every row; initial set lower [-0.2 x6, 0 x6], upper [0.2 x6, 0 x6]; tag (7).
- Equations (6) and (8) (300 dpi): all matrix rows and both bound vectors agree (6: 90,32,0,10,30,0 / 110,32.2,0,11,30.2,0; 8: 1.05,0.9,1.35,2.25,0.85,-0.05,0.3 / 1.35,1.2,1.65,2.55,1.15,0.25,0.6).
- Case-study quantities: ACC n=6, 50-step, L=40000, dt=0.1 sec, layers [6,32,32,32,6], mu=10^-4, d=diag([1,0.1,0.05,1,0.1,0.05]), eps=0.01, 100000 extra trajectories; Quadcopter n=12, 50-step, L=40000, dt=0.1 sec, layers [12,20,20,20,12], d=diag([0.05 x 1_{1x6}, 0.01 x 1_{1x6}]); Laubloomis n=7, 200-step, L=160000, dt=0.01 (no unit printed), layers [7,20,20,20,7], approx-star. All as printed. The paper gives no numeric delta for the case studies and the package adds none.
- Footnotes 1-3 (foot of PDF pp. 2 and 6): text verbatim, marks at the printed positions ("i . k + n" in footnote 2 and inf{z in R | Pr[R^j <= z] >= delta} in footnote 3 as printed).
- Conversion-note "kept as printed" claims, each checked on the PDF and true: 'non-parameteric'; subset sign with R^{(K+1)n} in Sec. 2 vs element sign with R^{n(K+1)} later; D_test = {s_{0,i}, sigma_{s_0,i}} with i outside the sub-subscript in Sec. 2 vs sigma_{s_{0,i}} in Def. 4; R^j in R_{>0}; "e_j ... j^{th} base vector" in Def. 3; strict inequalities in the proof; N(0, d^2) with d a diagonal "standard deviation"; 'Fig.3' twice without a space; float positions (Fig. 1 p.8, Table 1 p.9, Fig. 2 p.10, Tables 2-3 p.11, eq. (7) p.12, Fig. 3 p.13 inside the reference list).

## Coverage

- Theorem-like blocks: 5 of 5 (Definitions 1-4, Theorem 1) plus the proof, on 260-300 dpi crops; numbers and titles (Delta-confident flowpipe / Surrogate flowpipe / Residual Error / Calibration Dataset) correct.
- Displays: 8 numbered, (1)-(8), and 12 unnumbered (two conformal-inference displays in Sec. 2, surrogate output vector, partition of I, Def. 3 residual, Def. 4 set, Pr[R^j <= R^{j*}] >= delta, Theorem 1 display, four unnumbered proof displays): 20 of 20 checked at 260-400 dpi.
- Inline math checked on the same crops: Sec. 2 (all five run-in paragraphs), Sec. 3 intro, 3.1.1, 3.2 including ell = ceil((L+1)delta), the paragraph after the proof, Sec. 4 setup paragraphs.
- Algorithms: none in the paper.
- Tables: 3 tables, 90 data cells + 18 header cells checked at 300 dpi against both the CSV files and the Markdown tables; all agree, including printed precision (3.096, 2.475, 2.364, 7.5, 71.3700, 49.7770). Three captions verbatim (2 hours / 122 seconds; 273 sec / 2 hours and 25 minutes; 19 minutes / 2 hours and 30 minutes).
- Figures: 3 of 3 assets opened and compared with 260 dpi page crops on all four edges. figure-1.jpg: 6 panels, all y tick labels (250...90, 32.5...21, 0.2...-2.2, 160...0, 31...21, 1...-3), x tick labels 0-50 under both rows, "Time steps" labels, x1-x6. figure-2.jpg: 12 panels, tick labels on left and bottom of every panel, x1-x12. figure-3.jpg: 7 panels, bottom tick labels 0-200 of both rows and the right-most "200" under x4 present, x1-x7. Nothing cut, no foreign text. Captions verbatim, numbers correct.
- Completeness and order: word-level diff of pdftotext (all 15 pages) against paper.md prose: the only differences are math tokens, page numbers, the arXiv stamp, moved floats/footnotes and line-end hyphenation; no dropped or duplicated passage. All eight page-break joins read by eye (1/2, 3/4, 5/6, 6/7, 7/8, 8/9, 9/10, 11/12). 37 of 37 reference entries compared with the PDF (pp. 12-15), authors, titles, venues, volumes, pages, years.
- Prose spot check: pages 1-12 read in full against the renders (every paragraph), pages 13-15 are references and the Figure 3 caption, read in full.
- Headings and index: 12 headings of paper.md are real and correctly numbered/nested (1, 2, 3, 3.1, 3.1.1, 3.2, 4, 5, Acknowledgments, References); all 12 index.md entries exist as exact headings and describe their content correctly; 6 asset links resolve; tags (1)-(8) each occur once.
- Question 1: "What confidence does the inflated flowpipe have, and how is it built?" From index -> "3.2 Computation of a guaranteed Delta-confident flowpipe" -> Theorem 1: X = X-bar (+) Zonotope(0, diag([0_{1xn}, R*])), with R^{j*} the ceil((L+1)delta)-th smallest calibration residual of component j; X is Delta-confident with Delta = 1 - nK(1-delta), i.e. delta = 1 - (1-Delta)/(nK). Agrees with PDF pp. 6-8.
- Question 2: "Laubloomis setup and run time at failure probability 0.01?" From index -> "4 Experimental Results" -> Laubloomis paragraph + Table 3: 7-dimensional, no noise, L = 160000 test trajectories of 200 steps, dt = 0.01, ReLU network [7,20,20,20,7], approx-star, CORA [37] as comparison; at 0.01 conformal inference 91.9276 sec, reachability 92.9743 sec; test-data generation 19 minutes, training 2 hours 30 minutes. Agrees with PDF pp. 10-11.

## Not checked

- Italic/roman rendering inside definition and theorem bodies (the package states that it does not reproduce it).
- The curves inside the figure JPEGs were compared visually only (panel content, labels, edges), not pixel by pixel.
- The TeX source and the unused sections/appendix.tex mentioned in the conversion notes were not opened; the claim that the appendix file is absent from the PDF is consistent with the PDF (no appendix on pp. 1-15).
- supplement.md states that no supplementary material was supplied; nothing to compare.

Work directory logs/verify/work/hashemi2023data/ emptied and removed.
