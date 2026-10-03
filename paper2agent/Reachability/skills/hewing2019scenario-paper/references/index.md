# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Repository cover sheet (ETH Research Collection) | Bibliographic record of this accepted version: authors, publication date, permanent link (DOI), rights/licence, journal reference and publisher DOI, funding entry |
| Abstract | Abstract and index terms |
| I. Introduction | Analytic-approximation versus randomized stochastic MPC, related work [1]-[14], what the paper contributes, outline |
| II. Preliminaries | Start of the preliminaries (subsections A-C follow) |
| A. Problem Formulation | Section II-A: system (1), disturbance model $W \sim \mathcal{Q}$, chance and input constraints (2a)/(2b), Remark 1, nominal/error split (3a)/(3b) |
| B. Probabilistic Reachable Sets | Section II-B: Definition 1 ($k$-step PRS), Definition 2 (PRS), what the probability level does and does not cover |
| C. Scenario Optimization | Section II-C: chance-constrained program (4), sampled program with discarded samples (5), Assumption 1, Theorem 1 with the binomial condition (6), sufficient condition (7) for the number of discarded samples $N_k$, sample-size bound (8) for $N_k = 0$ |
| III. Stochastic MPC using Probabilistic Reachable Sets | Predictive dynamics (9a)-(9c), conditional predictive disturbance sequence $W_k$ |
| A. Constraint Tightening | Section III-A: Assumption 2 (bounded tube controller), tightened constraints (10a)/(10b), Assumption 3 (tightening sets are PRS) |
| B. Stochastic MPC with Indirect Feedback | Section III-B: expected cost, sampled MPC problem (11a)-(11g), control law (12), Remark 2 |
| C. Recursive Feasibility and Constraint Satisfaction | Section III-C: Assumption 4 (terminal set), Remark 3, Theorem 2 (recursive feasibility) with proof, Theorem 3 (closed-loop constraint satisfaction) with proof |
| IV. Probabilistic Reachable Sets using Scenario Optimization | How disturbance scenarios and simulated error trajectories are used to build PRS; Remark 4 (confidence level $1-\beta$ and the MPC guarantees) |
| A. Scaling of Convex Set | Section IV-A: scaling problem (13a)/(13b), Corollary 1 ($d = 1$), Remark 5 (half-space PRS) |
| B. Polytopic PRS | Section IV-B: polytope level problem (14a)/(14b), greedy sample removal, Corollary 2 ($d = n_{hs}$) |
| C. Ellipsoidal PRS | Section IV-C: minimum-volume ellipsoid problem (15a)/(15b), Corollary 3 and Remark 6 (values of $d$), Remark 7 |
| V. Simulation Example: Overhead Crane | Crane example: states, disturbance, constraints (16), (17a)/(17b), reference; Figure 1 |
| A. Simulation Setup | Section V-A: cost weights, horizons, tube controller, number of scenarios, number of discarded samples, resulting probability/confidence levels, computation times; Figure 2 and Table I follow this paragraph |
| B. Results | Section V-B: closed-loop simulation outcome and empirical constraint satisfaction rates |
| VI. Conclusion | Closing summary |
| Acknowledgments | Thanks |
| Appendix | Crane (damped cart-pole) equations of motion, parameter values, sampling time, eigenvalues, disturbance covariance kernel |
| References | Bibliography [1]-[16] |
| Conversion notes | Source version, how the mathematics was transcribed, layout decisions, source slips kept as printed (at the end of the file) |

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
