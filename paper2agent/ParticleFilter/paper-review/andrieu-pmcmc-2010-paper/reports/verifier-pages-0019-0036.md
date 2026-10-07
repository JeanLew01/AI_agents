# Independent verification: andrieu-pmcmc-2010-paper, PDF pages 19-36

Package: `staging/andrieu-pmcmc-2010-paper-s1` (paper.md lines ~362-868). Ground truth: `source.pdf` page renders (130 dpi full pages for all 18 pages, 220-260 dpi crops for dense mathematics) and the native text layer.

## Coverage
- Pages 19-36, all read in full against page images (no sampling of pages).
- Mathematics: every numbered display (20)-(43) and every unnumbered display in Sections 4-5, Appendices A-B and the Fearnhead contribution compared with the image; high-resolution crops used for (21)-(22), (30)-(31), (33), conditional SMC steps, the PG sweep (a)-(c), Appendix A displays, (41), the B.4 display, (42)-(43) and the two displays after (43). Equations (23)-(29), (32), (34)-(40) and the Section 5.1 acceptance-ratio display were checked on full-page renders (legible at that size).
- Statements: Assumptions 1-7, Theorems 1-6, proofs B.1-B.5: presence, order, numbering, wording.
- Prose: automated word-level diff (all alphabetic words of length >= 4, running heads excluded) between the PDF text layer of pages 20-36 and the package with maths stripped: no word differences other than text-layer artefacts (glued words, maths fragments). Short words and inline maths were checked by reading.
- References: all 40 entries compared character by character (automated, normalised whitespace/ligatures) with the text layer of pages 33-34: identical, in order (printed spellings 'Berthelesen', 'Unhlenbeck', 'Shephard N. and Pitt M. K.' kept). Journal italics are not marked.
- Figures: figure-7.jpg and figure-d8-p0035.jpg opened; captions compared.
- Structure: headings 4, 4.1-4.6, 5, 5.1, 5.2, Acknowledgements, Appendix A, Appendix B, B.1-B.5, References, discussion title, Fearnhead / Godsill / Chopin headings; page-boundary continuity at every page turn 19->36; LaTeX balance check ($, $$, braces, \left/\right) on the range: clean; no `<sup>`, glyph soup or stray markup.
- SKILL.md, index.md, conversion notes read once; all index headings exist verbatim in paper.md.

## Findings
| severity | PDF page | item id | package says | PDF shows | suggested fix |
| --- | --- | --- | --- | --- | --- |
| minor | n/a (conversion notes) | - | 'Theorems 1-6, Assumptions 1-6, Propositions and Lemmas carry bold printed labels' | The paper has Assumptions 1-7 (Assumption 7 on p. 28; it is present and correctly labelled in paper.md) | Change to 'Assumptions 1-7' in the conversion notes |
| minor | 33-34 | - | Reference entries carry no italics for journal/book titles | Titles of journals/books are italic in print | Cosmetic; optional |

Errors: 0. Minors: 2.

## Checked and found correct
- p19: Fig. 7 crop complete (panels (a), (b), axis labels; sideways as printed, no caption text inside); caption matches. Placement after the paragraph ending on p20 agrees with the conversion notes.
- p20: Section 4 intro, 4.1 first paragraph (gamma_n, Z_n, M_n, r(.|w), A_n definitions).
- p21: generic SMC steps 1(a)-(b), 2(a)-(c), one paragraph per step; (20), (21); O_n^k, s(.|W_n), ancestral lineage B_{1:P}^k, B_n^k := A_n^{B_{n+1}^k}; (22).
- p22: S_n, Q_n definitions (both 'for n >= 1' as printed), Assumptions 1-2, (23), (24), allocation indices A_n^{O_n^1+1}, Assumption 3, (25).
- p23: Assumption 4 (underlined/barred w, epsilon), Theorem 1, (26)-(28), 4.2, (29).
- p24: (30), X = X^{PN} x {1..N}^{(P-1)N+1}, (31) incl. denominator M_1(x_1^{b_1^k}) prod_{n=2}^P r(b_{n-1}^k|w_{n-1}) M_n(x_n^{b_n^k}|x_{1:n-1}^{b_{n-1}^k}), Theorem 2, Theorem 3(a).
- p25: Theorem 3(b), (32), L_*^N display, 4.3, (33), conditional SMC steps (q_1(.) as printed).
- p26: A_{n-1}^{-B_n^K} notation, marginal pi(x^k_{1:P})/N^P, sub-block update (a)-(c), 4.4, (34), (35).
- p27: S_n^theta / Q_n^theta (printed duplicate 'in X^n in X^n' kept and disclosed), Assumptions 5-6, Theorem 4, (36), (37), proposal density, 4.5 ('equation (8)', 'unormalized' as printed), sweep (a).
- p28: sweep (b)-(c) superscripts, Assumption 7, Theorem 5 (N >= 2), 4.6, Theorem 6, (38) (X_{1:T} as printed), (39).
- p29-30: (40), 5.1 incl. acceptance-ratio display, 5.2.
- p31: Acknowledgements, Appendix A (three displays, multinomial procedure), B.1, (41) all four lines.
- p32: B.2 display and rate 1 - Z/prod C_n, B.3, B.4 (sets, exponents (N-1)P, (N-1)(P-1), P-1, P; display with {K} as printed), B.5, F(k,v), (42).
- p33: (43), rewritten Q(F), final expectation display, closing remark; references start.
- p34: references end; discussion title; Fearnhead heading and text.
- p35: Fig. 8 crop (both panels, axes) and caption; Pr(O_n = x | A_n^1 = 1) display; toy model display; remaining text.
- p36: end of Fearnhead (Kingman (1982) digit restored, disclosed), Godsill, 'The vote of thanks was passed by acclamation.', Chopin heading and text to the page end.

## Test question
Q: In the PIMH sampler, what is the ratio of the extended target to the extended proposal, and what convergence rate follows under Assumption 3?
A (from 'B.1. Proof of theorem 2' and 'B.2. Proof of theorem 3'): tilde-pi^N / q^N = hat-Z^N / Z (eq. (41), using Assumption 2 on the second line); under Assumption 3 this is < Z^{-1} prod_{n=1}^P C_n < infinity, giving uniform geometric ergodicity with rate at least 1 - Z / prod_{n=1}^P C_n (Mengersen and Tweedie (1996), theorem 2.1).
Check against PDF pp. 31-32 (crops of (41) and the B.2 display): agrees exactly.
