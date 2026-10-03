VERDICT: 1 finding (0 A, 0 B, 1 C)

# Verification of devonport2023data-paper against papers/devonport2023data.pdf

Independent check of `skills/devonport2023data-paper` (paper.md 572 lines, index.md, SKILL.md,
table-1.csv, 6 image assets) against the 20-page PDF (arXiv:2112.09995v1). No error of
mathematical or factual content, no wrong label, number, cross-reference, caption, heading or
order was found. Every "kept as printed" claim in the conversion notes is what the PDF prints.

## Findings

### C1 (cosmetic) - subscript "ber" upright where the PDF prints it in italics
- Location: paper.md, "3.2. Bayesian PAC Analysis", Lemma 3.8, equation (3.8), snippet
  `\overline{r}=\sup \left\{ \beta : D_{\text{ber}}(\hat{r}_Q || \beta)`; and
  "3.3. Bayesian PAC Analysis: the Polynomial Case", Lemma 3.10, equation (3.11), snippet
  `\overline{r} = \sup \left\{ \beta : D_{\text{ber}}(\hat{r}_Q || \beta)`. PDF pages 10 and 12.
- Package: `D_{\text{ber}}` (upright "ber") in both displays.
- PDF: italic subscript, D_{ber}, in both displays (they sit inside italic lemma bodies).
- Confirmed: (3.8) on a 300-dpi crop of page 10; (3.11) on a 260-dpi crop of page 12.
- Not an error elsewhere: the upright forms in the sentence after (3.8) on page 11, in (B.2) and
  in "the inner inequality D_ber(...) <= gamma" on page 19 are upright in the PDF too, and the
  package matches them. No change of meaning; fix only if typographic fidelity is wanted.

No other C items worth listing.

## Conversion notes: every "kept as printed" claim confirmed on the PDF (260-dpi crops)

(a) Theorem 3.6 (p. 9): the PAC bound is an unnumbered two-line display; the text reads
    "Thus, with confidence delta, upon the termination condition of Algorithm 3.2". Confirmed.
(b) Corollary 3.11 (p. 12): "constructed in Algorithms 3.3 satisfies the PAC bound (3.6)";
    its proof begins "The argument to verify Algorithm 3.1". Confirmed. The TeX explanation
    is also true: `\label{eq:pac_epsi}` is inside `equation*` (cfun.tex line 879), cited at 1131.
(c) Algorithms 3.2 and 3.3 (pp. 9, 11; 300/400-dpi crops): while-test uses epsilon^i
    (superscript), the update assigns epsilon_i (subscript). Algorithm 3.3 lists no threshold
    eta among its inputs (Algorithm 3.2 does) and has no step computing M-hat. Confirmed.
(d) Three printed forms of the polynomial-case Gaussian parameters: W_Q ~ N(0, M-hat^{-1})
    after (3.9) on p. 11; N(0, (sigma_0^{2} I + M-hat)^{-1}) in (3.11) on p. 12 and in the
    definition of gamma on p. 19; N(0, (sigma_0^{-2} I + M-hat)^{-1}) in the first lines of the
    proof of Lemma 3.10 on p. 19. All three confirmed.
(e) Proof of Theorem 3.6 (p. 11): "By Lemma 3.7" and "by Lemma 3.8" printed as plain black
    text (not links); variance printed as k(x,x) - k_{D^i}(x)^T (sigma_0^2 I + K^i) k_{D^i}(x)
    with no inverse. Confirmed.
(f) Lemma 3.9 (p. 11): r(c-bar_eta) in the first clause, r(c-bar_Q) in the bound. Confirmed.

Further slips, all confirmed as printed: "Algorithm 3.4" (p. 7) and "Algorithm 3.6" (p. 11);
(2.4) with M-hat_{m,sigma} (no inverse) on the left (p. 6); Z = [z_m(x_i) ... z_m(x_N)] (p. 5);
empirical risk without 1/N and the unbalanced "{x_1,...,x_N} : 1 - P_X(...) <= eps})" in the
proof of Theorem 3.4 (p. 8); "degree 2k" (p. 8), "order k = 10" (pp. 14, 16 and captions),
"b = z_k" and "order k" (p. 19); sigma_0^{-1} I in the termination remark (p. 10); sigma^2 I_N
in (3.4), (3.5) (p. 10); D_KL(W_P||W_Q) in the sentence after (3.2) (p. 9); unclosed "(I -"
in (3.13) and K_{Nr} as last factor of (3.12) (pp. 12-13); exp(||x-y||^2/(2 l^2)) in Section
4.1 (p. 14) against exp(-||x-y||^2/(2l)^2) elsewhere; "initial sample size of 20,000 and a
batch size of 5,000" for Algorithm 3.1 (p. 13); r = 2000 in the text against "1,000 samples"
(Fig. 1) and "m = 10,000" (Fig. 2, Fig. 3); captions of Fig. 2 and Fig. 3 naming three contours
of "order k = 10" while Table 1 has m = 4 for the quadrotor; "Figure 2" in Section 4.3 (p. 16);
(4.1) with an extra ")" in the last line, an undefined beta, no value for c, and "The input u"
in the text; no value for K in the quadrotor dynamics; (A.3) with sigma^2 B B^T and "By",
(A.4) ending in b(x), "R m x N", "z_m(x_i) T" (p. 19); 1{x in C_Q} in (B.1); the unmatched
"(" in every "(g(x)^2" term, r(c-hat_eta) in (B.11) and r_{Q_eta} in the last line (p. 20).

Consistency check of the notes recomputed: n = 2, eps = 0.1, delta = 1e-9, natural log gives
N = 70307 for m = 10 and N = 14587 for m = 4, as in Table 1; 1/(1 - F_1(1)) = 3.151.

## Coverage

- Pages: 3-20 read in full on 260-dpi crops (three per page) side by side with paper.md;
  pages 1-2 read in full at 170 dpi (prose, no displayed mathematics), end of page 2 at 260 dpi.
- Completeness and order: word-level diff of pdftotext (20 pages) against paper.md (all words
  of two or more letters and all digit strings, math stripped). No dropped, duplicated or
  reordered passage; differences are only line-break hyphenation, running heads, and the
  floats and footnotes moved to paragraph boundaries. No sentence cut at a page break
  (checked at every page transition).
- Theorem-like blocks, symbol by symbol: Problem 1, Remark 3.1, Lemma 3.2, Lemma 3.3,
  Theorem 3.4 with proof, Theorem 3.5, Theorem 3.6 with proof, Lemmas 3.7, 3.8, 3.9, 3.10,
  Corollary 3.11 with proof, Remark 3.12 = 13 blocks; numbers, titles and source citations
  ("[1], Corollary 4", "[13], Theorem 7.2", "PAC-Bayes Theorem, adapted from [29, 17]") match.
- Displays: 39 numbered ((2.1)-(2.7), (3.1)-(3.16), (4.1), (A.1)-(A.4), (B.1)-(B.11)) and the
  unnumbered display of Theorem 3.6; each number is on the right equation. Inline mathematics
  of every paragraph on pages 3-20 was read against the crops.
- Algorithms: 3.1 (9 lines), 3.2 (15 lines), 3.3 (14 lines) - inputs, assignments, loop
  nesting, conditions and return lines match; the last lines of 3.2 at 400 dpi.
- Table 1: 27 data cells and both header rows, CSV and Markdown table; caption verbatim.
- Figures: figure-1/2/3.jpg and algorithm-3-1/2/3.jpg are complete (axes, labels, all
  contours, full boxes), no foreign text; captions verbatim with the right numbers.
- Symbol list of Section 1.1: all 40 rows in four groups (both kappa-hat^{-1} rows are printed
  with a hat, as in the package).
- References: all 34 entries read against the page crops (authors, initials, titles, venues,
  volumes, years, pages, URLs).
- Front matter: title, authors, both footnotes, grant numbers, key words, "93E10," match.
- Headings and index: the 19 section headings of paper.md are real and correctly numbered and nested;
  every "Exact heading" of index.md exists verbatim in paper.md and holds what the row says
  ("2. Preliminaries" has no row of its own; its content is covered by the 2.1 row).

Two questions answered from the package only (SKILL.md -> index.md -> section):
1. "How does Algorithm 3.3 update the accuracy level and when does it stop?" Index row
   "3.3. Bayesian PAC Analysis: the Polynomial Case": after each batch of N_b samples,
   eps_i <- (r-bar + (2/N) log(pi^2 i^2 / (6 delta))) / (1 - F_1(1)) with r-bar from (3.11)
   and F_1 from (3.7); loop while eps^i > eps; return 1{C(x) <= eta}. PDF page 11: same.
2. "How many samples did the classical and the Bayesian polynomial estimators need on the
   Duffing example, and at what cost?" Index row "4. Examples", Table 1: Algorithm 3.1
   N = 70307 in 39 s, Algorithm 3.3 N = 11000 in 13 s (both m = 10); kernel Algorithm 3.2
   N = 30000 in 506 s with l = 1/4. PDF page 14: same.

## Not checked

- The published IEEE TAC version: not available here. The note's journal title and
  "68(9), 2023" cannot be confirmed from this PDF (the PDF metadata title does read
  "Data-Driven Reachability and Support Estimation with Christoffel Functions").
- Pages 1-2 were not rendered at 250 dpi or more (170 dpi, plus the machine word diff).
- Single-letter words and punctuation are outside the machine diff; they were read by eye only.
- Figure assets were compared visually, not pixel by pixel. Hyperlink targets were not tested.
- supplement.md states that no supplementary material was supplied; nothing to compare.
- The external review directory and its page-level notes were not read (by design).
- The TeX source was used only to confirm the one statement about `eq:pac_epsi`.
