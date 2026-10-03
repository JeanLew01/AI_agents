import json, os
W = os.path.expanduser('~/AI_agents/paper2agent/Reachability/paper-review/dietrich2025data-paper')
D = W + '/documents/s001-dietrich2025data'
TITLE = 'Data-Driven Reachability with Scenario Optimization and the Holdout Method'

plan = json.load(open(D + '/plan.json'))
plan['title'] = TITLE
plan['notes'] = [
    'Source version: arXiv:2504.06541v2 [eess.SY], dated 11 Sep 2025 (7 pages, IEEE two-column conference format; arXiv version of the CDC 2025 paper by E. Dietrich, R. Devonport, S. Tu and M. Arcak; the first page carries a ©2025 IEEE notice).',
    'Mathematics was transcribed to LaTeX from the authors\' arXiv TeX source (root.tex, reachable_fig.tex, root.bbl) and checked against the PDF pages; cross-references, equation numbers and citations are given as printed. No formula is kept as an image. Printed equation numbers are (1)-(14); several displays are unnumbered in print and carry no tag here.',
    'Notation of the transcription: the indicator printed with a double-struck 1 (TeX `\\mathds{1}`) is written `\\mathbb{1}`; the starred parameter is written `\\theta^{\\ast}`; the violation level is one printed glyph throughout, written `\\epsilon` in Sections II to V-A and `\\varepsilon` in Section V-B as in the authors\' source; displays (3) and (4), two lines of one aligned display in print, are given as two consecutive displays. Authors\' inconsistencies and typos are kept as printed (for example `k` without a hat in Section II-E and in the Computation paragraph, the subscript of the indicator in (5), `R(\\theta)` without a hat in Section II-C, "futher", "critize", "Alburquerque").',
    'Reading order: the unnumbered first-page author note and the IEEE copyright notice follow the author line; Figure 1 (printed at the top of page 3) follows Theorem 1 and the paragraph after it; Figures 2 and 3 follow the paragraphs that cite them; Footnote 1 follows the paragraph that carries its mark. The text and formulas printed inside Figure 1 are also transcribed after its caption. Tables I and II are CSV files (11 rows x 5 columns each, cells as printed) with a conversion note on the row-group label.',
    'Scope of this version: no appendix or supplementary material. Theorem 1 is stated with a citation to [28, Thm. 3.3] and has no proof in the paper; Lemma 1 has a proof. The vertical arXiv stamp on page 1 is omitted as page furniture.',
]
json.dump(plan, open(D + '/plan.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

b = json.load(open(W + '/bundle.json'))
b['title'] = TITLE
s = b['sources'][0]
s['title'] = TITLE
s['reviewed'] = True
s['review_notes'] = ('All 7 pages compared with 220 dpi renders (four quadrants per page). Prose, inline and display mathematics were taken from the authors\' arXiv TeX source (arXiv:2504.06541v2) and checked against the page images; no formula is kept as an image. '
    'Three figures are image crops checked at 200 dpi (Figure 1 full-width schematic, Figure 2 epsilon/e-hat plot, Figure 3 reachable tube); Tables I and II are CSVs checked cell by cell. One region is omitted (arXiv margin stamp, page 1). '
    'Definition 1 (binomial tail inversion, (7)-(8)), Theorem 1 ((9)), the order-wise bounds ((10) and the k-hat = 0 bound), the tower-property display and Lemma 1 with its proof were checked symbol by symbol. '
    'Remaining verifier diagnostics are LaTeX-versus-glyph differences and are adjudicated per page.')
P = 'references/paper.md'
b['navigation'] = [
    {'file': P, 'heading': 'Abstract', 'purpose': 'Summary of the claims: holdout method for data-driven reachability, and the de-randomization discussion'},
    {'file': P, 'heading': 'I. Introduction', 'purpose': 'Motivation, related work on data-driven reachability, positioning against wait-and-judge scenario bounds'},
    {'file': P, 'heading': 'II. Problem Statement', 'purpose': 'Start of the setup section (subsections A to E below)'},
    {'file': P, 'heading': 'A. Forward Reachable Sets.', 'purpose': 'Reachable set definition, sampling distributions on X_0 and D, i.i.d. samples, sublevel-set estimator (1)'},
    {'file': P, 'heading': 'B. Violation Probability.', 'purpose': 'Violation probability / true error (2), empirical error (3)-(5), the target guarantee P{V > epsilon} <= beta'},
    {'file': P, 'heading': 'C. Nonconvex Scenario Reachability Analysis', 'purpose': 'Scenario program (6) with the volume proxy'},
    {'file': P, 'heading': 'D. Wait-and-Judge', 'purpose': 'The a-posteriori support-scenario baseline and its computational cost'},
    {'file': P, 'heading': 'E. Binomial Tail Inversion.', 'purpose': 'Definition 1: binomial tail inversion, equations (7)-(8)'},
    {'file': P, 'heading': 'III. The Holdout Method', 'purpose': 'Holdout sampling, Theorem 1 (bound (9)) and what the probability is taken over, computation, order-wise scaling in M and beta ((10)), zero-violation remark, marginal bound over training and holdout data, Figure 1'},
    {'file': P, 'heading': 'IV. Applications', 'purpose': 'Start of the numerical section; comparison protocol against wait-and-judge'},
    {'file': P, 'heading': 'A. Reachable Sets', 'purpose': 'RBF scenario program (11)-(12), solver, experimental settings (gamma, 3000 samples, beta), runtime accounting'},
    {'file': P, 'heading': '1) Duffing Oscillator:', 'purpose': 'Duffing example: system, Table I (N, M, volume proxy, epsilon), Figure 2, runtimes'},
    {'file': P, 'heading': '2) Quadrotor:', 'purpose': 'Quadrotor example: dynamics (13), parameters, Table II, runtimes, and the "Sample Complexity" paragraph'},
    {'file': P, 'heading': 'B. Reachable Tubes', 'purpose': 'Reachable tube definition, time-varying RBF program, linear example (14), Figure 3'},
    {'file': P, 'heading': 'V. De-randomization', 'purpose': 'The two layers of probability in PAC bounds and the case against de-randomizing them'},
    {'file': P, 'heading': 'A. De-randomization Methods', 'purpose': 'Enlargement-based de-randomization, level-set bound function, Lipschitz assumption, sample-and-cover'},
    {'file': P, 'heading': 'B. Lower Bounds from Zeroth-Order Optimization', 'purpose': 'Conditions (a)-(b), Lemma 1 and its proof, the (L/gamma)^d sample and query counts, Footnote 1, the three takeaways'},
    {'file': P, 'heading': 'VI. Conclusion', 'purpose': 'Closing summary'},
    {'file': P, 'heading': 'VII. Acknowledgments', 'purpose': 'Funding'},
    {'file': P, 'heading': 'References', 'purpose': 'Bibliography [1]-[36]; [28] is the source of Theorem 1, [19] the wait-and-judge baseline'},
    {'file': P, 'heading': 'Conversion notes', 'purpose': 'Source version, how the mathematics was transcribed, relocated items and limitations'},
]
json.dump(b, open(W + '/bundle.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('ok')
