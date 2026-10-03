VERDICT: clean

Package: skills/selim2022safe-paper (SKILL.md, references/index.md, references/paper.md, 7 image assets, 2 CSV).
Ground truth: papers/selim2022safe.pdf (arXiv:2204.07417v2, 8 pages). Verified read-only; all renders and temp files removed.

## Findings

None. No A, B or C finding was confirmed on a render at 250 dpi or more.

## Points the task asked to confirm

- Algorithm 2, two statements under line number 1: CONFIRMED on a 300 dpi crop of p.4. The PDF prints
  `1  Z_eps <- Z(0, diag((L*)_1 (delta)_1 /2, ..., (L*)_n (delta)_n /2)) for` and, on the continuation line,
  `j = k : (k + n_plan) do`; the loop header has no number of its own, `M_j <- ...` is line 2, `return` is line 7.
  The transcription and the conversion note describe exactly this. The text references "Line 1 of Algorithm 2"
  (p.4) and "Algorithm 2, Line 2" (p.5) are printed as the package gives them.
- Linearization point x*_j (the item labelled "Not printed in the PDF"): CONFIRMED correctly handled. It is the last
  bullet of "Conversion notes", opens with "Not printed in the PDF, reported here only as background from the authors'
  TeX source", and does not appear anywhere in the paper text of paper.md. In the PDF the word "linearization" occurs
  once only (p.5, "(assuming a constant linearization point)"), and that sentence is transcribed as printed; x*_j is
  used in Algorithm 2 lines 2, 3, 6 without definition, as the notes say. The note's description also agrees with the
  commented-out line 132 of tex-source/.../Sections/5_solu.tex and with the commented-out appendix \input in main.tex.
- Sentences at float, column and page breaks: all 14 joins checked and intact, none cut or duplicated:
  p1 col1->col2 across footnotes and Fig. 1 ("...safety constraints during | both learning and deployment [3]");
  p1->p2 ("Others | utilize constrained MDPs [7]"); p2 col break ("addressing the above | challenges of lacking");
  p2->p3 ("generator matrix | G in R^{n x n_g}"); p3 col break ("future work. | We also note,");
  p3->p4 across Algorithm 1 ("collision checking to | enable safe trajectory optimization");
  p4 col break across Algorithm 2 ("the policy and environment | model. We consider q");
  p4->p5 across Fig. 2 ("checking the | intersection of the plan's"); p5 col break across Algorithm 3
  ("(assuming a | constant linearization point)"); p5->p6 across Fig. 3 ("when adjusting an | unsafe plan");
  p6 col break ("reaches the goal, | crashes, or exceeds"); p6->p7 across Fig. 4 and Tables I-II
  ("RTS' planning | time increases"); p7 col break inside ref [3] ("safe reinforce-|ment learning"); p7->p8 ([16] -> [17]).
- Float placement in paper.md is as the notes state and is sensible: Fig. 1 after the first paragraph of Section I;
  Algorithm 1 after "BRSL is summarized in Algorithm 1 ..."; Algorithm 2 after the first paragraph of III-A;
  Algorithm 3 then Fig. 2 after "We adjust unsafe actions using Algorithm 3 ..."; Fig. 3 after the first paragraph
  of IV; Fig. 4, Table I, Table II after "Results and Discussion"; then V. Conclusion.
- Four edges of every figure and algorithm asset compared with the page (260-300 dpi crops): figure-1 (green dotted
  frame complete on all sides, yellow "Offline Data Collection" box complete at right); figure-2 (both panels, (a)/(b)
  labels, X_obs hexagons complete, no caption text inside); figure-3 (three panels with window title bar at top and
  sub-captions at bottom); figure-4 (four panels with y-labels, tick labels, "1e6" offsets, legends, sub-captions);
  algorithm-1/2/3 (top and bottom rules, line numbers at left, full line width at right). None cut, none with
  foreign text.

## Coverage

- Theorem-like blocks checked symbol by symbol at 280-300 dpi: 4 of 4 (Assumption 1, Assumption 2, Definition 1,
  Theorem 1) plus the proof (start p.5, end with box p.6). Numbers, titles, block ends as printed.
- Numbered displays checked at 300 dpi: 11 of 11: (1), (2), (3), (4a), (4b), (4c), (5), (6), (7), (8a), (8b); each
  number sits on the right equation; closing punctuation matches. The paper has no unnumbered display. All 11 displays
  and 266 inline formulas of paper.md compile with pdflatex (amsmath, amssymb) without error.
- Algorithm lines checked at 300 dpi against transcription and asset: 37 numbered lines (Alg. 1: 16, Alg. 2: 7,
  Alg. 3: 14) plus the Input / Parameter headers of Alg. 2 and Alg. 3; numbering, nesting, conditions, assignments,
  comments all agree.
- Table cells checked at 300 dpi: Table I 50 data cells, Table II 50 data cells, both two-level headers, all row
  labels and units, both captions; CSV and Markdown copies are identical to each other and to the page. The
  bold-cell lists in the two "Note on Table" paragraphs agree with the printed bold face (including the whole bold
  entry 32.79 +/- 27.6 of Hexarotor Baseline and the half-bold speed cells).
- Figures: 4 figure assets and 3 algorithm assets opened; captions of Fig. 1-4 and sub-captions of Fig. 3-4 verbatim.
- Completeness and order: pdftotext of all 8 pages compared with paper.md by token diff, (a) lower-case words and
  numbers for the whole document, (b) case-sensitive with single letters and punctuation for body and references
  separately. The only non-math differences are line-break hyphens resolved to hyphenated compounds (data-driven,
  collision-checking, objective-based, learning-based, receding-horizon, first-order, Risk-constrained,
  non-communicating, Off-policy; all agree with the authors' TeX/bbl), small-caps headings, and omitted page furniture
  (running heads, page numbers, arXiv stamp). No dropped, duplicated or reordered prose. References [1]-[55] all
  present once, in order, with matching authors' initials, volumes, pages and years.
- Hyperlinks: the six URI annotations in the PDF (video playlist, GitHub repository, four reference URLs) equal the
  URLs in paper.md.
- Prose read word for word on crops of 260 dpi or more: p1 (abstract, index terms, Section I paragraph, Fig. 1
  caption), p2 (I-B paragraph, Limitations, Contributions, II-A notation paragraph), p3 (whole left column, II-B
  obstacle paragraphs, II-C, II-D), p4 (III overview paragraph, III-A opening, data paragraph, both Lipschitz
  paragraphs), p5 (both III-B prose paragraphs, collision-check and gradient paragraphs, text around (7)-(8b)),
  p6 (proof end, remark, Setup, data and ensemble paragraphs, Goal-Based, Turtlebot, quadrotor, point-robot
  paragraph with X_safe and the reward formula), p7 (end of Results and Discussion, Conclusion). p8 (references
  [17]-[55]) and the p1 footnotes were read at 170 dpi and by the exact token diff only.
- Headings: 17 headings of paper.md are real, correctly numbered (I-V, A-D) and nested; run-in heads of Section IV
  (Setup., Goal-Based Environments., Path Following Environments., Results and Discussion.) keep the printed
  bold / italic. All 17 "Exact heading" entries of index.md for paper.md exist exactly once; all 9 asset links resolve.
- Conversion notes: every "kept as printed" item was looked up on the page and is really printed that way:
  f: X x U x W -> X with two arguments in (2); Lipschitz bound with only ||x_1 - x_2|| and unsubscripted norms;
  "X_0 in R^n" in Definition 1; upper index n_plan in text / Alg. 3 Input and line 12 versus k + n_plan in Alg. 1
  line 8, Alg. 2 and Alg. 3 line 5; R-hat_0 in Alg. 2 Input; min_j on Alg. 2 line 3; unhatted x_k on Alg. 1 line 7;
  Alg. 3 line 3 to k + n_plan + n_brk, line 8 with "+ gamma grad", line 11 "x_n is stopped"; non-bold u_{k-1} in
  (8b); "j =" in both limits of the product in (7); "iff v <= 1" without star; SECAS (and TD3) in the Fig. 4
  legends; "such loiter circles", "at safe state", "manuever", "as in fig 2", "conservativeness is by placing",
  "a low-dimensional parameterized plans", "[3] J. Garcıa".

## Two questions answered from the package only (SKILL.md -> index.md -> section)

1. "Which optimisation problem decides whether a reachable set collides with an obstacle, and which value means
   collision?" Index -> "B. Adjusting Unsafe Actions": the linear program (6),
   v* = min_{z,v} { v | A_cap z = b_cap and |z| <= v }, on the intersection constrained zonotope (5); Z_cap is nonempty
   iff v <= 1; Algorithm 3 line 7 treats v* <= 1 as "in collision", and collision avoidance requires v* > 1
   [43, Prop. 2]. PDF p.5: identical.
2. "For the Turtlebot, what are n_brk and n_plan, and what collision rate and compute time does BRSL reach?"
   Index -> "IV. Evaluation": n_brk = 6, n_plan = 8 (Goal-Based Environments); Table I, column Turtlebot BRSL:
   Collision Rate 0.0 %, compute time 50.41 +/- 20.5 ms, Goal Rate 57 %, Mean Reward 86. PDF p.6 and p.7: identical.

## Observations that are not findings

- index.md, supplement table: the "Exact heading" cell reads "Document beginning", which is not a heading of
  supplement.md (its only heading is "# Supplementary information", followed by "No corresponding materials were
  supplied."). It is a pointer to the start of a three-line file and looks like generator boilerplate; not counted.
- Conversion notes, first bullet: "published in IEEE Robotics and Automation Letters 7(4), 2022" is not printed in
  this PDF (the running head only says "Preprint Version. Accepted June, 2022"), so it cannot be checked against the
  ground truth; the bullet does say the package was made from the arXiv v2 preprint.

## Not checked

- Pixel-level content of the plots (curve shapes, colours) beyond completeness of the crops and legibility of labels.
- External facts not in the PDF (journal volume/issue, validity of the URLs; nothing was fetched or executed).
- Italic versus upright runs inside reference entries were not compared entry by entry (words, numbers, initials and
  punctuation were).
