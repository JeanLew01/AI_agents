# Independent verification: greco-vasile-2022-paper, pages 23-44

Package: `staging/greco-vasile-2022-paper-s1` (paper.md lines 612-1106, tables 3-5, figures 3-7, algorithm-5).
Reference: `documents/s001-greco-vasile-2022/source.pdf` (page images and 200-dpi crops; native text only for prose and numbers).
Scratch: `paper-review/_scratch/verify-greco-23-44`.

## Result

**0 errors, 3 minors.** No symbol, number, statement or reference discrepancy was found in pages 23-44.

## Coverage (what was actually done)

- **Display mathematics, all checked against 200-dpi crops**: (36), (37), (38), (39), (40), (41), (42), (43a), (43b), (44), (45), (46), (47a), (47b), (48); all unnumbered displays: the seven PoC intervals (pp. 26, 28, 28, 29, 30, 31, 31), the two Lemma 2 displays, the two Lemma 3 diameter displays and K, the six Theorem 1 displays plus the final pair and conclusion, the plane parameterisation, the two-sphere system, the m/c expression, the brace system, the quadratic sum, and lb(S) = s_cap.
- **Inline mathematics**: read against crops on pp. 23, 24, 30, 33-40 (all appendix and proof text); on pp. 25-29, 31-32 against 110-dpi page images plus native text.
- **Prose**: full word-level diff of the package text (lines 612-992) against the PDF native text for pages 23-40; every difference was a mathematics or float artifact. No missing, duplicated or reordered sentence.
- **Tables**: every cell of Tables 3, 4, 5 (CSV and Markdown) against crops.
- **Figures**: figure-3 to figure-7 and algorithm-5 opened and compared with the pages; captions compared.
- **Algorithm 5**: transcription compared line by line with the crop.
- **References**: all 52 entries compared character by character by script (after Unicode normalisation, italics markers removed); the two differences were inspected by hand. Italic markup itself was not checked.
- **Structure**: headings, page joins 22/23 and 33/34 (and all other page joins in range), LaTeX delimiter/brace balance by script, damage patterns (doubled backslashes, `<sup>`, replacement characters), index headings against paper.md, conversion notes, SKILL.md.
- Not checked: pages 1-22 (other verifier); rendering in an actual Markdown/MathJax viewer.

## Findings

| Severity | PDF page | Item id | Package says | PDF shows | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| minor | 35 | p0035-r002 | Algorithm 5 steps 1-5 each written on one line with a semicolon joining the description and the formula line(s), e.g. `Branch most promising simplex lb(S_k*) = L_k; S_k* -> ...` | Two (step 3: three) separate printed lines per step, no semicolons | Optional: use a line break instead of `;`. Content is identical. |
| minor | 24 | (Table 3 item, page 24) | Table 3 and its caption placed after the paragraph following Eq. (39), i.e. after "...found in literature [48-50]." | Table 3 printed inside the paragraph before Eq. (39), between "The measurements y-bar_k are simulated" and "starting from the debris reference trajectory" | None needed: the sentence is joined correctly and the conversion notes state that floats sit at paragraph boundaries. Listed for auditability only (the float lands about one paragraph and one equation later than printed). |
| minor | - | index.md | "equations (22)", "equations (30)", "equations (31)", "equations (32)", "equations (40)", "equations (46)" (plural for a single equation); SKILL.md boilerplate mentions workbooks/supplement that do not exist for this paper | - | Cosmetic; generated text. |

## Checked and found correct (by page)

- **p. 23**: join with p. 22 ("...defined as a normal distribution" + (36)); (36); (37) including tilde on Sigma, bold-x subscripts, `[1/5^2, 5^2]` twice, trailing `},`; printed inconsistency lambda_{0-1}, lambda_{0-2} kept; italic-x subscripts in the "Note that" paragraph kept; "a new observations" kept; (38) arctan/arcsin entries and norm of x_k(1:3).
- **p. 24**: (39) with y-bar, Sigma-tilde, lambda_{y_Sigma-1/2}, ranges; Table 3 (10, 10 arcsec); wall-time paragraph numbers (M in {10+5i : i=1..8}, N = {5000j : j=1..10}, 50000, 1%, 100 calls, 30 repetitions, Matlab R2020b, 3.5GHz Dual-Core i7); models a), b).
- **p. 25**: model c); Table 4 all 18 cells (0.0578/0.928/<.001/0.928/<.001; 0.0360/0.972/<.001/0.045/<.001; 0.0357/0.973/<.001/0.001/.21); 92.8%, 97.2%, 37%, 1%; "C. Results" paragraph.
- **p. 26**: N = 50000, M = 0, delta_DCA = 50m, underlined/overlined lambda and PoC; Fig. 3 crop complete (axes, legend), caption; PoC_50m in [0, 4.97e-5].
- **p. 27**: Fig. 4 crop complete (both panels, x10^-4 multiplier, (a)/(b) labels), caption; approx 100 m, approx 20 km, PoC > 10^-4 at 300 m, upper PoC_300m > 5e-4, lower PoC_300m < 1e-5; M = 12, 24 h.
- **p. 28**: [0, 2.15e-4]; 75%; Fig. 5 crop and caption; 9 h; [0, 9.69e-3]; "almost 1%".
- **p. 29**: "less than 1000 iterations"; approx 1 m/s, 1 km, M = 12; [0, 2.82e-4]; 14 revolutions; Fig. 6 crop and caption.
- **p. 30**: [0, 0]; overlined PoC at the 24 h cut-off; (40) all five lines including the y_k vector with square roots, lambda_{y_mu_k-1/2} in [-5, 5], lambda_{y_Sigma-3/4} in [1/5^2, 5^2], k = M+1, M+2.
- **p. 31**: D1-D6 description (9 h, 6 h); [0, 2.94e-2]; "almost 3%"; Fig. 7 crop and caption; [1.20e-8, 9.94e-1]; "less than 4 revolutions".
- **p. 32**: Table 5 all 81 cells against the crop, including the group values printed once for D1-D3 (8, 7.83e-5, 154.27, 33.17) and D4-D6 (10, 2.57e-4, 159.58, 34.44) and the ".00" proposal time for A; the transcription note is accurate; "IV. Conclusions" text.
- **p. 33**: Conclusions continuation ("the the" kept as printed); "A. Estimator Derivatives"; the three nabla expressions.
- **p. 34**: join with p. 33; (41)-(45); hats on w distinguished from un-hatted w exactly as printed (lhs of (43a) un-hatted, (43b) hatted); initial condition vector; C_{partial psis}.
- **p. 35**: Algorithm 5 crop complete and transcription correct ("min" in both U_0 and U_{k+1} as printed); B&B paragraph joined across the float; (46).
- **p. 36**: Lemma 1 proof end; Lemma 2 proof with absolute-value bars, "L delta + L delta", 2L delta, 0 < delta <= epsilon/2L; Lemma 3 first display and (sqrt3/2)^floor(k/n_lambda).
- **p. 37**: Lemma 3 second display, floor/ceiling expressions, log base 2/sqrt3, K^(i), K = N_0 n_lambda ceil(log sigma_0/delta); Theorem 1 proof with printed K/k mixing kept; five displays.
- **p. 38**: remaining Theorem 1 displays including "not greater than" (ngtr); "D. Lower bound computation" first paragraph, tan^-1(1/L), CH = conv{...}, [52].
- **p. 39**: (47a), (47b); plane parameterisation; two-sphere system with theta-hat(lambda_1) as printed; m_0j/c_0j expression; (48) with plain n as printed.
- **p. 40**: brace system; m-tilde, c-tilde definitions; quadratic sum; lb(S) = lb(lambda_cap) = s_cap; Funding Sources (grant 722734).
- **pp. 40-44**: references [1]-[52] all present, in order, text identical to the PDF. The two script differences are line-break hyphens resolved correctly: [33] DOI `S0898-1221(02)00205-5`, [51] "B-plane". Diacritics (Žilinskas, Witczyński, Bäck, Sánchez, García, Tóth) correct.
- **Structure**: appendix headings A-D at section level as stated in the notes; no footnotes on pages 23-44; no doubled backslashes or extraction damage in tables or text; all `$` delimiters and braces balanced in lines 612-1106; every heading in index.md exists verbatim in paper.md; conversion notes checked for my range (Algorithm 5 "min", K/k mixing, theta-hat(lambda_1), plain n in (48), proofs ending with a square, Table 5 folding) and found true.

## Technical question answered from the package only

**Question**: For the measurement-simulation subcase D6, how many epistemic parameters are used, what PoC interval results, and what does the computation cost?

**Answer from the package** (sections "4. Measurements simulation instance" and Table 5 / `assets/table/table-5.csv`): D6 simulates measurements until 6 h before rTCA with n_lambda = 10 epistemic parameters and B&B threshold epsilon = 10^-6, Lipschitz constant L = 2.57e-4. The interval is PoC_50m in [1.20e-8, 9.94e-1]. Cost: surrogate 159.58 s, proposal 34.44 s, optimisation 1922.37 s, total 35.27 min, 13043 pSIS calls.

**Check against the PDF**: pages 31 (interval, 6 h) and 32 (Table 5 row D6 with the group values on the D5 line) confirm every value.
