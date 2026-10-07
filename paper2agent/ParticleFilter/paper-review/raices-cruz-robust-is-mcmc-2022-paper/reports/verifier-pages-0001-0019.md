# Independent verifier report: raices-cruz-robust-is-mcmc-2022-paper, pages 1-19

Package: `staging/raices-cruz-robust-is-mcmc-2022-paper-s1`. Reference: `source.pdf` (arXiv:2206.08728v1), rendered at 130 dpi (pp. 1-15) and 170 dpi (pp. 16-19). The TeX source and reviewer reports were not consulted.

## Coverage

- All 19 pages read in full against `references/paper.md` (820 lines read completely), plus `SKILL.md`, `references/index.md`, `references/supplement.md` and the conversion notes.
- Mathematics: every display equation (1)-(62) and the unnumbered displays (ESS_MCMC definition, the two prior sets M and M', the Appendix A recall/expectation displays, the posterior density in Appendix C) compared symbol by symbol with the page images. Tag sequence checked mechanically: `\tag{1}`..`\tag{62}`, each once, in order. `$`/`$$` delimiters balanced.
- Prose: besides reading, a mechanical word-level diff of the prose (maths stripped) against `pdftotext` output for all pages; every non-maths difference was inspected.
- Tables 1-4: every cell of the four CSVs and of the four inline markdown tables compared with the PDF (p. 11, p. 12).
- Figures 1-3: all three JPEGs opened and compared with pp. 8, 9, 10; captions compared.
- References: all 47 entries compared with pp. 13-16 (read in full, not sampled; the word diff covers every entry, accented names inspected by eye).
- Index: all 20 indexed headings exist verbatim in `paper.md`.
- Not checked: the statement in the conversion notes about the published journal version (CSDA 176, 107558) cannot be verified from this PDF.

## Findings

| # | Severity | PDF page | Item id | Package says | PDF shows | Suggested fix |
|---|---|---|---|---|---|---|
| 1 | minor (inserted word) | 6 -> 7 (page break) | `p0006-r18` (joined with `p0007-r01`) | "...uses the effective sample size for importance sampling sampling with correlated samples eq. (24)..." (`paper.md` line 242) | p. 6 ends "...effective sample size for importance"; p. 7 continues "sampling with correlated samples eq. (24)". The word "sampling" occurs once. | Delete the trailing " sampling" from the markdown of `p0006-r18` (it must end "...for importance"). |
| 2 | minor (cosmetic crop) | 8 | Figure 1 crop (`assets/figure/figure-1.jpg`) | The outer frame of the figure is visible on the left and top only; the right and bottom frame lines are cut off. | Figure 1 is enclosed in a complete rectangular frame. | Optional: enlarge the crop by a few points right and bottom (or crop inside the frame on all sides). All nodes, arrows, the plate and "i = 1, ..., N" are complete and legible. |
| 3 | minor (cosmetic) | - | `references/index.md` | "equations (1)" for Section 1 (plural for a single equation). | - | Optional: "equation (1)". |

Errors: 0. Minors: 3.

No rendering problems found: no doubled backslashes in markdown tables (headers are plain Unicode; the LaTeX header symbols are in a separate transcription note), no `<sup>` or glyph debris, no footnote swallowing a paragraph (the first-page affiliation/e-mail/keyword footnotes sit in the title block and the paragraph crossing pp. 1-2 reads continuously), no unbalanced LaTeX.

## Checked and found correct

- p. 1: title, authors with affiliation marks, three affiliations, four e-mail addresses, key words, abstract ("rely on" kept as printed), Introduction paragraphs 1-3.
- p. 2: eq. (1) (inf over p in M), all citations lists ([3, 34, 46], [14, 41, 42, 43], [1, 7, 37], [6, 15], [44], [26], [29]).
- p. 3: eqs. (2)-(6), w_p := p_u/q, "(i.i.d)" as printed, bars vs tildes on mu.
- p. 4: eqs. (7)-(14); squared sum in numerator and w_p^2 in denominator of (7); (8) with (E_q(Z-bar))^2; sum over i<j in (14).
- p. 5: eqs. (15)-(23) and unnumbered ESS_MCMC; upper limit N-k in (15) as printed, infinity in (16), ell in (17)/(19), rho-hat subscripts g vs g-tilde, the condition rho-hat_g(ell+1) < 0, "[12][p. 5-6] (see A for details)" as printed, N^2 Var_p(mu-bar)/(ESS_IS . ESS_MCMC) in (23).
- p. 6: eq. (24), (25) (min over t in M), (26), w_t := c p_t/q, Steps 1-5 (arg min in Step 3, "ESS > ESS_target" in Step 4), "10 000" maximum iterations, 20%.
- p. 7: thinning paragraph and citations; data description numbers (75 studies, -24.17, 332.50, 28.46, -11.10, 76.29 ug/l); eqs. (27)-(32); tau_l = 1, k_l = 1, k_u = 5.
- p. 8: Figure 1 and caption; Section 5.2 text, list items (1)-(4), "(eq. 30 and eq. 31)" as printed.
- p. 9: Figure 2 and caption; item (5); R = [-20, 80], 90%, 200 x 200 grid, ranges; set M (-8..68, 5..16, r - 0.9 >= 0); r = tau_0 - (-0.01 mu_0^2 + 0.46 mu_0 + 9.56); eq. (33).
- p. 10: Figure 3 (three panels, titles, colour bars, axes complete) and caption (mu_0 = 5, tau_0 = 7, 5 000); eq. (34) (primes in the denominator); 5 000 / 10 000, 6 000 / 12 000; initial values (-7, 6) and (10, 10); 11 640 and 14 305; 12.1, 12.07-12.24, 19.9, tau_0 = 1 000, corner (-8, 5), 4 773, 12.09.
- p. 11: "over 10 hours", "15 to 25 minutes", 12.13, "over 20 hours"; Tables 1-3 captions and every cell (CSV and inline).
- p. 12: Section 5.5: R = [30, 100], median 14.6, set M' (42..88, 5..11, r' - 0.90 >= 0), r' coefficients (-0.011, 1.427, -35.104), 12.1 -> 26.8, tau_0 = 10.5, 1 649, 26.7, 4 hours, 13 minutes; Table 4 caption and every cell; Conclusions.
- p. 13: end of Conclusions, Supplementary material (URL), Acknowledgement(s), Disclosure statement, Funding (219-2013-1271), refs [1]-[9] (printed oddities "Stuart Stuart", "Gårdmark A.", "doi:doi:" kept).
- pp. 14-16: refs [10]-[47], all present and in order; names, titles, venues, volumes, pages, years, ISSN/ISBN/DOI agree.
- p. 16: Appendix A displays, eq. (35)-(39).
- p. 17: eqs. (40)-(46); 1/2 factor on the mixed partial in (43)/(44) as printed; g(u,v) := v^2 u; U = w_p(X), V = h(X).
- p. 18: eqs. (47)-(53); integration limits (1..tau_0, 1..5, -inf..+inf), order d mu dk d tau_mu; posterior density; a, b, c definitions; exponent -1/2 in (53); "Lemma D.1 in (48)" as printed.
- p. 19: eq. (54) (exponent -3/2, factor b); Lemma D.1 and D.2 statements, eqs. (55)-(62), both proofs with end-of-proof marks.
- Conversion notes: statements about kept typos (N-k, "see A", "see C"), headings, steps, tables and figures are accurate.

## Question answered from the package only

Question: With ESS_target = 10 000 and initial values (10; 10), why did the iterative importance sampling not stop after iteration 2, and what did it finally report?

Answer from the package (Section 4 Steps 2-5; Section 3 eq. (24); Section 5.4 Table 3 / `assets/table/table-3.csv`): Step 4 stops only when the combined ESS = (ESS_MCMC/N) . ESS_IS exceeds ESS_target. At iteration 2 the combined ESS was 3 995 (ESS_MCMC 13 907, ESS_IS 5 746, 20 000 samples), below 10 000, so the MCMC was re-run at the new hyperparameters. At iteration 3 ESS = 14 305 (ESS_MCMC 14 305, ESS_IS 20 000), so it stopped at (mu_0*, tau_0*) = (-7.995, 5.221) with estimated lower bound 12.103 after 23.72 minutes, against the grid-search value 12.091 (11.45 h). Consistency check: 13 907/20 000 x 5 746 = 3 995 and 14 305/20 000 x 20 000 = 14 305.

Check against the PDF (p. 6 Steps, p. 6 eq. (24), p. 11 Table 3): all values and the stopping rule agree.
