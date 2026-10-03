# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | One-paragraph statement of the approach and of the two estimators; keywords |
| 1. Introduction | Related model-based and data-driven reachability work, prior convex scenario approach of Devonport and Arcak (2020b), what is generalized here |
| 2. Nonconvex Scenario Optimization | Scenario program (1), violation probability $V(x)$, support scenarios and $s_N^*$, Theorem 1 (Campi et al., 2018) with $\epsilon(s_N^*)$ in (2) and the probability bound (3), convex refinement (4) |
| 3. Nonconvex Scenario-Based Reachability | Forward reachable set, sampling model, sublevel-set estimate $\mathcal{R}(\theta)$ (5), minimum-volume scenario programs (6)-(7) and the guarantee they aim at |
| 3.1. Tiling with Basis Functions | Basis-function form (8), partition cells and indicator functions, program (9), support scenarios for the tiling, use of (4); Algorithm 1 (image and transcription) |
| 3.2. Radial Basis Functions (RBFs) | Gaussian RBF (10), sublevel function (11), parameter vector $\theta$, Figure 1, program (12), support scenarios for RBFs, use of (2); Algorithm 2 (image and transcription) |
| 4. Examples | Hardware, threads, and the a-posteriori Chernoff-bound validation with its sample count and confidence |
| 4.1. Duffing Oscillator | Dynamics, parameter values, initial set and time range of the first example |
| 4.1.1. Tiling with Basis Functions | Duffing, Algorithm 1: grid, $N$, $\beta$, run time, support-scenario count, $\epsilon$, 100-trial statistics; Figure 2 |
| 4.1.2. Radial Basis Functions | Duffing, Algorithm 2: number of RBFs, threshold, $N$, $\beta$, run time, support-scenario count, $\epsilon$; Table 1 |
| 4.2. Quadrotor Model | Dynamics (13), parameter values, initial intervals (14), input set and time range; Figure 3 |
| 4.2.1. Tiling with Basis Functions | Quadrotor, Algorithm 1: grid, $N$, $\beta$, run time, support-scenario count, $\epsilon$; Table 2 |
| 4.2.2. Radial Basis Functions | Quadrotor, Algorithm 2: number of RBFs, threshold, $N$, $\beta$, run time, support-scenario count, $\epsilon$ |
| 5. Conclusion | Authors' summary of the two estimators |
| Acknowledgments | Funding grants |
| References | Complete bibliography, 39 entries, author-year style without numbers |
| Conversion notes | Source version, how the mathematics was transcribed, moved floats, table and algorithm conventions, misprints of the paper kept as printed, reviewer's numerical check of (2) and (4) (at the end of the file) |

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
