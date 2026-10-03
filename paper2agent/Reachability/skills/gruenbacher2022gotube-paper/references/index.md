# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | Abstract; the author line, the first-page footnote (affiliations, correspondence, code URL) and the copyright line are just above it |
| Introduction | Motivation, deterministic vs stochastic reachability, the SLR predecessor and its three scalability problems, overview of GoTube, contribution list; Figure 1 (CartPole reachtubes) and Figure 2 (GoTube in a nutshell, with the notation of the initial ball, Lipschitz caps and bounding ball) |
| Related Work | Paragraphs 'Global Optimization.', 'Verification of Neural Networks.', 'Verification of Continuous-time Systems.'; Table 1 (comparison of reachability tools: deterministic, parallel, wrapping effect, arbitrary time-horizon) |
| Setup | Problem setting and standing assumptions: the ODE with initial ball, display (1); numerical integration of the centre and of surface samples; Definition 1 (Bounding Ball), Definition 2 (Bounding Tube); the maximum-perturbation optimisation problem, display (2), and the argument for restricting it to the surface of the initial ball |
| Main Results | How the tube is built and what is guaranteed: Algorithm 1 (image and line-by-line transcription) with its prose walk-through (inputs, sampling loop, stopping test, radius mu times sample maximum); Definition 3 (Lipschitz Cap); Theorem 1 (cap radius from the stretching factors and the quantile of the difference quotient, displays (3)-(5)) with proof sketch; Theorem 2 (probabilistic guarantee, display (6)) with proof sketch |
| Experimental Evaluation | Hardware and time-out; the three experiments are in the subsections below |
| On the volume of the bounding balls with GoTube | First experiment: benchmarks, baselines, confidence levels and tightness factor used; Table 2 (tube volumes per tool) and Figure 3 (Dubins car reachtubes; its caption gives the sample count and runtime of that run) |
| GoTube provides safety bounds up an arbitrary time horizon | Second experiment: longer time horizons on the CartPole benchmarks; Table 3 |
| GoTube can trade runtime for reachtube tightness | Third experiment: three new CT-RNN benchmarks, runtime vs volume as a function of the tightness factor; Figure 4 |
| Discussions, Scope and Conclusions | Summary and the paragraphs 'SLR versus GoTube?', 'Sample blow up in GoTube?' (dependence of the number of samples on the parameters and the dimension), 'What about Gaussian Processes?', 'Limitations of GoTube.', 'Future of GoTube.' |
| References | Bibliography, 64 unnumbered author-year entries in alphabetical order |
| Appendix | Start of the appendix (pages 11-13 of the PDF); its content is under the next heading |
| Proofs of the Theorems | Lemma 1 (stochastic lower bound of a distribution function from a fitted extreme-value distribution, Kolmogorov-Smirnov statistic and the DKW inequality, (S1)-(S4)) with proof (S5)-(S13) and Figure S1; restated Theorem 1 ((S14)-(S16)) with full proof ((S17)-(S30)); restated Theorem 2 ((S31)) with full proof ((S32)-(S40), including the cap-coverage probability and the lower bound on the cap radius) |
| Conversion notes | Source version and the two titles, how the mathematics was transcribed, list of printed equation numbers, numbering of theorem-like statements, treatment of the algorithm, figures and tables, placement of floats, source slips kept as printed (at the end of the file) |

For long sections, search a narrower subsection or prompt. Headings inside fenced quotations are source content, not document section boundaries.

## Supplementary information — [supplement.md](supplement.md)

| Exact heading | Look here for |
| --- | --- |
| Document beginning | Source text or supplied-material notes |

For long sections, search a narrower subsection or prompt. Headings inside fenced quotations are source content, not document section boundaries.

## Assets

Figure and table captions in the documents link to the files below. Open only the needed image; for a table, read its header and relevant rows first.

- `assets/figure/`: main figures (JPEG).
- `assets/supp_figs/`: supplementary and extended-data figures (JPEG).
- `assets/table/`: main tables (CSV, or JPEG when transcription is unreliable).
- `assets/supp_table/`: supplementary tables (CSV, or JPEG fallback).

Asset paths are relative to the skill root. CSVs retain internal blank rows; captions and merged headers may also occupy rows. Consult the document notes before treating every row as data.
