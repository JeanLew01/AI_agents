# Independent verification: andrieu-pmcmc-2010-paper, PDF pages 56-74

Package: `staging/andrieu-pmcmc-2010-paper-s1` (paper.md lines ~1349-1860). Reference: `source.pdf` pages 56-74 (printed 324-342).
Result: **0 errors, 5 minors.**

## Coverage (what was actually done)
- Every page 56-74 rendered at 170 dpi and read in full next to the package text; all display equations and dense inline maths additionally compared with 260-400 dpi crops (p.56 model, p.59 (55) and acceptance ratio, p.62 both ABC displays, p.65 RMSE and (56), p.67 mixture display, p.68 all three displays, steps (a)/(b) and inline maths).
- Prose completeness: automated word-sequence diff (words >= 4 letters, maths stripped) of package text against the PDF text layer for pages 56-71; the only differences are running headers, figure axis text and the relocated figure captions. No sentence lost or duplicated.
- References in the discussion: all 112 entries, not a sample. Read against page images for pp. 71-74 (incl. the whole of p.74) and compared character by character (alphanumerics, accents folded, l/1 folded) with the text layer: identical, order identical. Digits versus letter l then checked on the images and by pattern search in the package (no "l" standing for a digit remains in pages 56-74).
- Figures d17-d23: every JPEG opened and compared with the page; captions compared with the PDF.
- Headings of all 9 contributions on these pages, the reply heading and its 10 italic topic titles.
- SKILL.md, index.md (all indexed headings exist verbatim in paper.md), conversion notes.
- LaTeX: `$` count even and braces balanced over the range; no `<sup>`, ligature glyphs, or stray markup.

## Findings
| # | severity | PDF page | item | package says | PDF shows | suggested fix |
|---|---|---|---|---|---|---|
| 1 | minor | 60 (59-61) | figure-d19 block (p0060) / index.md | Fig. 19 link + caption sit inside the **Simon Maskell** section (after its 2nd paragraph), and index.md lists figure-d19 under Maskell | Fig. 19 belongs to the Lee and Holmes contribution (cited there: "Fig. 19 shows the differences ..."); printed as a full page inside Maskell's text | Move the figure block to the end of the Lee and Holmes contribution (before the Maskell heading) and list it under Lee and Holmes in index.md. Text continuity itself is correct. |
| 2 | minor | 63 | figure-d20 block (p0063) / index.md | Fig. 20 sits inside the **Toivanen and Lampinen** section; index.md lists it under that heading | Printed at the bottom of p.63 (within Toivanen text) but it is Yun and Chen's figure (cited on p.65) | Move after the first paragraph of Yun and Chen (next to Fig. 21) and fix the index row. |
| 3 | minor | 66 | first list item on p0066 | "In broad terms PMCMC algorithms are valid (a) when unbiasedness ... and" run into the preceding paragraph; (b) is a separate paragraph | (a) and (b) are both printed as separate list items | Start a new paragraph at "(a)". |
| 4 | minor | 59, 61, 62 | text items | "et al." not italic in: "Lee et al. (2009)" (p.59); "Jones et al., 2009", "Peters et al., 2010", "Nevat et al., 2010", "Hayes et al., 2010", "Doucet et al., 2000" (p.61); "Peters et al. (2010)", "Peters et al., 2008", "Silva et al. (2009)" (p.62) | italic *et al.* (as rendered elsewhere in the package) | Italicise for consistency. |
| 5 | minor | 69, 70 | captions of Fig. 22, 23 | "**Fig. 22.**", "**Fig. 23.**" bold | Figs 17-21 captions in the package use plain "Fig. N." | Make uniform. |

No error-level finding (no wrong symbol, number, missing content, or wrong reference detail) was found.

## Checked and found correct
- p.56: Jacob et al. tail (O(T^2), T=945, N=O(T), 1 day, 1 h, 1 s); heading "Michael Johannes (Columbia University, New York) and Nick Polson and Seung M.-Yae (University of Chicago)"; model display (|x_t|^alpha/20, printed "beta_1" twice kept, cos(1.2t)); alpha=2, beta_1=0.5, beta_2=25, beta_3=8; lists (a)-(b), (a)-(d); 60000, 5000, 300000, "1/1000th" (PDF glyph "l" -> digit, correct).
- p.56->58 across Fig. 17: "...whether assumption 4 is satisfied in the | examples that are considered..." continuous, nothing lost/duplicated. Fig. 17 crop complete (6 rows, both columns, panel labels), caption exact.
- p.58-59: Johansen and Aston heading/text, f_theta, g_theta as printed (N(y_n|x_n,1)), 100-filter/100 particles/10000, 30 s, 1000 steps, 1.33-GHz, norm expression; Fig. 18 crop complete, caption matches (line samples approximated, as declared in notes).
- p.59: Lee and Holmes: eq (55) incl. integral over calligraphic Z and bold y, z; F-hat(j) sum; acceptance ratio display; 50000, 13065, 2333; Maskell heading and q(theta*|theta) q(x*_{1:T}|theta*) forms.
- p.59->61 across Fig. 19: "...a sampler of the form q(.)q(.) | and the particle Gibbs sampler considers ..." continuous. Fig. 19 crop complete, caption exact.
- p.61: Murray et al. heading (5 names, CSIRO Canberra), text incl. "ecosytem" as printed, p_theta(x_n|x_{n-1}), p_theta(x_n|y_n,x_{n-1}), p_theta(x_1|y_1); Peters and Cornebise heading.
- p.62: items (a)-(d); both p-hat^ABC displays symbol by symbol (round vs square outer brackets, y_n vs y_{n-1} in the second denominator, A^k_{n-1} superscripts, epsilon^2, "y_n^k(S)" capital S as printed); "chapter 1"; Silva et al. heading; integral display; items (a)-(e) (p.62-63).
- p.63-65: Toivanen and Lampinen heading/text ("test image, Owing" as printed; 2009a,b; 2009c); Yun and Chen heading ("Urbana—Champaign"); sigma_V^2=10, sigma_W^2=1, N*=1000000, y_{1:300}; RMSE display; eq (56) incl. printed W_T^{*K}, z-tilde, z-hat^{N,*}, Z-hat^{N,*}; "PIMH-Reuse1" (PDF glyph "Reusel"). Figs 20, 21 crops complete; captions exact (N/L values 25/40000, 100/10000, 250/4000, 1000/1000).
- p.65-71: reply heading; all 10 italic topic titles present and in order (What the users say; Correctness and sequential Monte Carlo implementations; Valid sequential Monte Carlo implementations; Large state spaces; General proposals for particle Metropolis-Hastings algorithms; Smoothing; Performance and the choice of N: from theory to practice; Unbiasedness versus sampling; Using sequential Monte Carlo methods with Markov chain Monte Carlo moves; Some past and future work). All displays on pp. 67-68 match (check accent on pi^{KN}, product j=1, j != k, delta_{x^i}, q(k,x^{1:N}) relations, 1<=a<=b<=P, pi{x_{1:P}(l)|x_{1:P}(1:m\{l})}). "Andrieu amd Thoms" printed typo kept; 0.234; numbers on pp. 69-70 (500; T=100; 300000; 1000 times; N=5000; T=500, sigma=1, sigma_x=sqrt(10); 150; (N-1)T; NT; 12000; 7 min; 10 runs; N=100000). Figs 22, 23 crops complete, captions exact.
- pp. 71-74: 112 reference entries, all compared (see coverage). Printed oddities kept correctly: "Berthelesen"/"Berthelsen", "alogrithms", "Bethelehem", "Rubio-Ramírez" (2005) vs "Rubio-Ramirez" (2007), "probabilites", "Hamze F.", "Proc IEEE ICASSP", "Bernoulli, 7, no. 2", "Molec. Phys., 75, 59".
- Conversion notes: statements concerning this range (W_T^{*K} in (56), Figs 17/19 moved, l -> 1) are true. The printed repeated "beta_1" (p.56 model) and "y_n^k(S)" (p.62) are kept but not listed among the oddities (optional addition).

## Test question
Q: In their reply, what PG configuration do the authors use for the Johannes-Polson-Yae scenario, and how do they justify it against the claimed 1000-fold cost?
A (package, section "The authors replied later, in writing, as follows", topic "Using sequential Monte Carlo methods with Markov chain Monte Carlo moves"): T=100 simulated points, informative priors; PG sampler with a conditional SMC of 150 particles for 12000 iterations (1000 burn-in, Fig. 22), 7 min in MATLAB on a desktop; this has the computational complexity of the bootstrap filter with Gibbs moves at N=300000 because PG samples only (N-1)T variables X_n plus one parameter set per iteration versus NT (X_n, parameters). N=5000 in Section 3.1 was for a harder case (T=500, sigma=1, sigma_x=sqrt(10)), whereas here sigma=sqrt(10), sigma_x=1.
Check against PDF pp. 69-70: all values and the argument agree.
