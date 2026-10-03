# Report: devonport2023data

**Paper.** Devonport, Yang, El Ghaoui, Arcak, "Data-Driven Reachability Analysis and Support Set Estimation with Christoffel Functions" (printed arXiv title; published in IEEE TAC 68(9), 2023 as "Data-Driven Reachability and Support Estimation with Christoffel Functions" - stated in the conversion notes).
**Source.** arXiv:2112.09995v1, 20 pages, single column, SIAM style. Authors' TeX (cfun.tex, cfun_shared.tex, cfun.bbl) used for all mathematics and the bibliography; PDF checked page by page.
**Result.** `verify --strict` exit 0, status `reviewed_with_limitations` (the limitations are the 46 adjudicated parser differences; no image-only content).
**Package.** `~/AI_agents/paper2agent/Reachability/skills/devonport2023data-paper` (staging builds s1-s3 kept; scripts, crops, saved review queues and `verify-strict.out` in `logs/work/devonport2023data/`).

**Counts.** Figures 3; tables 1 (Table 1 as CSV, 3 data rows x 10 columns) plus the unnumbered symbol list of Section 1.1 as a text list (40 rows); algorithms 3 (image crop + transcription each); displays 40 as LaTeX (39 with printed tags (2.1)-(2.7), (3.1)-(3.16), (4.1), (A.1)-(A.4), (B.1)-(B.11); the Theorem 3.6 display is unnumbered); formulas kept as images 0; omitted regions 21 (arXiv stamp and page number on p.1, running header on pp.2-20); adjudications 46 (18 missing_lines, 14 + 14 number checks); references 34.

**IMPORTANT for the reader (numbering).** This version numbers by section. The polynomial PAC-Bayes estimator the reader calls "Algorithm 3" is **Algorithm 3.3** here; its guarantee is **Corollary 3.11** (via Lemma 3.10 / bound (3.11), Lemma 3.7 / (3.6)-(3.7), Lemma 3.9, Theorem 3.6). Algorithm 3.1 = polynomial, classical PAC (Theorem 3.4, Lemma 3.2 / (3.1)); Algorithm 3.2 = kernelized (Theorem 3.6, Lemma 3.8 / (3.8)). The TAC version was not compared.

**What I corrected.**
- Every page rewritten from the TeX source (macros expanded), not patched: 28 extractor formula images -> LaTeX; glyph-soup inline math -> `$...$`.
- SIAM run-in bold titles -> real `##`/`###` headings; theorem-like blocks and 7 proofs with bold printed labels; QED boxes as `$\square$`.
- Wrapped floats (3 algorithm boxes, 3 figures) untangled from the narrow body column; line-wrap hyphens removed; 10 cross-page joins (two inside a word, one inside an inline formula, p.11/12).
- Footnotes moved off the page foot (p.1 after the author line, p.6 after (2.7)) so the joins work.
- Table 1: extractor grid was wrong; cells re-read on a 250 dpi crop; two header rows combined (noted in the caption).
- Bibliography from the .bbl, each entry compared with the page (accents `Açikmeşe`, `Nyström`, `Géza`, broken URL in [3] repaired).

**Source errors kept as printed and listed in the conversion notes (pp. in brackets).** These matter for citing the guarantees:
- Corollary 3.11 says "satisfies the PAC bound (3.6)" [12]. In the TeX this is a label inside the *unnumbered* display of Theorem 3.6, so the theorem number is printed; the bound meant is P(for all i>=1, P_X({x: C^i(x) <= eta}) >= 1-eps^i) >= 1-delta, not equation (3.6). Its proof says "Algorithm 3.1" for 3.3.
- Theorem 3.6 says "with confidence delta" (not 1-delta) [9].
- Algorithms 3.2/3.3 test eps^i but assign eps_i; Algorithm 3.3 lists no threshold eta among its inputs and has no step computing M-hat [9, 11].
- The posterior covariance of the polynomial case is printed three ways: M-hat^{-1} after (3.9) [11]; (sigma_0^{2} I + M-hat)^{-1} in (3.11) and in gamma [12, 19]; (sigma_0^{-2} I + M-hat)^{-1} in the proof of Lemma 3.10 [19]. All three read on 220 dpi crops.
- Proof of Theorem 3.6 cites "Lemma 3.7/3.8" (hard-coded; by content 3.8/3.9) and prints (sigma_0^2 I + K^i) without inverse [11]; "Algorithm 3.4" [7] and "Algorithm 3.6" [11] are mis-resolved references.
- Others: (2.4) left side, missing 1/N in the proof of Theorem 3.4, kernel without minus sign in Section 4.1, r = 2000 vs "1,000" / "m = 10,000" in captions, "Figure 2" for Figure 3, (4.1) extra parenthesis and undefined beta, (A.3)/(A.4), (B.1), unmatched "(" in Appendix B.

**Limitations / uncertainty.** None in the transcription that I know of. Full pages were read at 130 dpi (not 170) plus 200-300 dpi crops of every mathematical region, the algorithm boxes, Table 1 and the figures. Figure 2/3 captions do not match the pictures (four contours); kept as printed. One reviewer, no independent verifier.

**Checks run.** Word-level test of all 389 missing lines (only math glyph strings unmatched); word-multiset vs pdftotext (no prose word lost); symbol counts per page (all differences explained: \leq/\geq, \gets, \cdots, \mapsto); every number difference attributed (Unicode minus, math-mode thousands, algorithm transcriptions hidden by crops, repeated table headers, kerned digits in the second parser); all 40 displays and 790 inline formulas compile with pdflatex and the rendered displays were compared with the PDF; recomputed N = 70307 (m=10) and 14587 (m=4) from the transcribed Algorithm 3.1 line, and 1/(1-F_1(1)) = 3.151 (printed 3.15).

**Self-check question.** "What does Algorithm 3 (polynomial Christoffel estimator, Bayesian PAC) compute per iteration and what is guaranteed?" Answer from `references/paper.md`, Section 3.3 and 3.2: inputs X, order m, eps, delta in (0,1), sigma_0^2, N_0, N_b; start N <- N_0, eps^0 <- 1; while eps^i > eps: i <- i+1, append N_b iid samples, N <- N+N_b, C(x) = z_m(x)^T M-hat_{m,sigma_0}^{-1} z_m(x), evaluate r-bar by (3.11) [sup of beta with D_ber(r-hat_Q||beta) <= (D_KL(N(0,(sigma_0^2 I + M-hat)^{-1}) || N(0, sigma_0^{-2} I)) + log((N+1)/delta))/N, r-hat_Q from (3.6)], eps_i <- (r-bar + (2/N) log(pi^2 i^2/(6 delta)))/(1-F_1(1)); return 1{C(x) <= eta}. Guarantee (Corollary 3.11 -> Theorem 3.6): with probability >= 1-delta, for all i, P_X({x: C^i(x) <= eta}) >= 1-eps^i; heuristic eta = binom(n+2m,n)/eps (Remark 3.12). Compared with the 300 dpi crop of the box and the crops of pp. 9 and 12: identical.

**Tool pitfalls / suggestions for the brief.**
- A bare `$$` in a plan note ("one $$ block per line") breaks math parsing of the built file; write "display block".
- `\chi^2_1` is tokenised as the number 21 and `[100,200]` as one thousands token; `\chi_1^2` and `[100, 200]` avoid both diagnostics without changing the math.
- `check_missing.py` flags every line that starts with a line-wrap fragment; `check2.py` (fragment-aware) and `numcheck.py` (subtracts algorithm-transcription tokens and minus pairs, leaving only real residue) in my work folder are reusable.
- With TeX available, grep hard-coded numbers and labels inside starred environments: the PDF alone cannot show that "(3.6)" in Corollary 3.11 is not equation (3.6).
- In a shell chain, `grep -c` returning 0 matches exits 1 and silently skips the following steps; I lost one edit that way and caught it only by rechecking.
- Per-page generator scripts (`pNN.py` + `pagelib.py`) made the restart after the out-of-memory reboot a non-event.
