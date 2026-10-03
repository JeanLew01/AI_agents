# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | Abstract; the author line, affiliations, e-mail addresses and funding note are just above it |
| I. Introduction | Motivation (inductive bias, sample complexity of linear vs nonlinear data-driven control), chain policies and recurrence, outline of the paper, Notation paragraph (norm, ball, diameter, closure, boundary, interior, distance to a set, ceiling/floor) |
| II. Preliminaries and Problem Formulations | Section opener only; content is in subsections A-D |
| A. Hamiltonian System | Section II-A: Definition 1 with system (1), Assumption 1 (bounded gradient, L_H), Assumption 2 (Lipschitz dynamics, L), Remark 1 with bound (2) (C_f), Definition 2 (energy layer) |
| B. Target Reachability Problem | Section II-B: admissible control signals, flow notation, sets S_0 and S_tgt, Problem 1 |
| C. Recurrence on Energy Layers | Section II-C: Definition 3 (invariant measure), Definition 4 (ergodic measure), Theorem 1 (ergodic decomposition), supports K_alpha^E, Proposition 1 (density of typical trajectories) |
| D. Chain Policies | Section II-D: demonstrations, Definition 5 (control alphabet), Definition 6 (assignment set, Supp), index map and selection rule, Definition 7 (nonparametric chain policy), Remark 2 (execution) |
| III. Reachability in Hamiltonian Systems | Section opener: overview of the two ingredients (energy decrease and recurrence) |
| A. Target Reachability via Chain Policies | Section III-A: H_min/H_max, Assumption 3, Remark 3, Definition 8 (energy distance Delta H), sets H_tgt and H_tgt^epsilon, Assumption 4, hitting time and rates (3)-(4), Assumption 5, Theorem 2 with its three conditions, proof (Steps 1-3, (5)-(7)), Remark 4 |
| B. Existence of the Chain Policy | Section III-B: Lemma 1 with proof, Assumption 6 (ergodic layers), Assumption 7 (strong convexity, mu_H), Remarks 5-6, Theorem 3 (radius r_i and sample-complexity bound on N), proof Steps 1-6 with (8)-(11) |
| C. Finite Time Reachability | Section III-C: Assumption 8 (return time T_1, reaching time T_2), Theorem 4 (bound on T_max), proof with (12)-(14) |
| D. From Expert Demonstrations to NCPs | Section III-D: construction of the assignment set from demonstrations, certified radius r_i(t), Figure 1, Algorithm 1 (image and transcription) |
| IV. Numerical Simulation | Experimental setup: baseline (behavior cloning) and its hyperparameters, expert generation, test protocol, horizons, hardware |
| 1) Spring-Mass | Section IV: spring-mass dynamics and parameters, Figure 2, reported success rates and reach times |
| 2) Single Pendulum | Section IV: pendulum dynamics and parameters, Figure 3, reported success rates and reach times |
| V. Conclusions and Future Work | Summary and directions left open |
| References | Bibliography [1]-[29] |
| Conversion notes | Source version, how the mathematics was transcribed, list of printed equation numbers, placement of floats and footnotes, source slips kept as printed (at the end of the file) |

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
