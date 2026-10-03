# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | One-paragraph statement of the problem, the PCA + conformal inference idea and the case studies; keywords |
| 1 Introduction | Motivation, the three-step method of Hashemi et al. (2024b) being extended, the two contributions, Related Work paragraph, Notation paragraph, Footnotes 1-2 |
| 2 Preliminaries | Section heading only; Sections 2.1-2.4 follow (setting, surrogate model, conformal inference and the earlier method, problem definition) |
| 2.1 Stochastic Dynamical Systems | Trajectory and initial-state distributions, training vs deployment environment, distribution shift |
| 2.2 Surrogate Model: Reachability & Error Analysis | Surrogate model (1), prediction errors (2), Definition 1 (residual distributions), total-variation shift, surrogate flowpipe, Definition 2 (star set, (3)) |
| 2.3 Conformal Inference & Probabilistic Reachability | Conformal and robust conformal quantile statements, rank formula (4), max-residual (5) and inflating hypercube (6)-(7) of the earlier method, definition of a delta-confident flowpipe, Lemma 3 |
| 2.4 Problem Definition | Problem statement (flowpipe valid under a total-variation bound) and the two sources of conservatism addressed |
| 3 Scalable and Accurate Data Driven Reachability Analysis | One-sentence overview of Section 3 |
| 3.1 Improved Scalabilty and Accuracy for Training Surrogate Models | Trajectory segmentation (8), one small surrogate model per segment, concatenated star-set flowpipe, Figure 1, Footnote 4 |
| 3.2 Accurate Inflating Hypercubes via Principal Component Analysis | PCA background, Figure 2, limitations of the earlier hypercube, PCA construction (9)-(11), new residual (12)-(13), Definition 4 (calibration dataset, (14)), Proposition 5 with (15) and proof (16), star-set form of the hypercube (17), Remark 6 |
| 4 Numerical Evaluation | Experimental setup overview, thresholds used, Table 1 (specification, training, reachability and hypercube runtimes, dataset sizes) |
| 4.1 12-Dimensional Quadcopter | Quadcopter states, process noise covariance, initial-state distribution |
| 4.2 27-Dimensional Powertrain | Powertrain simulator, noise, sampling time, horizon, division setting, network structure, Footnote 6 |
| 5 Acknowledgements | Funding and grant numbers |
| 6 Conclusion | Authors' three-sentence summary |
| References | Bibliography, 28 author-year entries in alphabetical order |
| Appendix A. Detail of the Experiments | Appendix heading only; Sections A.1-A.3 give the details of Experiments 1-3 and Figures 3-6 |
| A.1 Experiment 1:[Comparison with Hashemi et al. (2024b)] | Hovering quadcopter, horizon, division setting, network structure; Figure 3 |
| A.2 Experiment 2: [Sequential Goal Reaching Task] | Long-horizon quadcopter task, model interpolation formula (18); Figure 4 |
| A.3 Experiment 3: [Reachability with Distribution shift] | Powertrain under distribution shift, threshold and confidence used; Figures 5 and 6 |
| Conversion notes | Source version, notation, numbering of theorem-like blocks, placement of floats and footnotes, source inconsistencies in the guarantee (inequality signs, assumptions), source typos kept, consistency checks (at the end of the file) |

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
