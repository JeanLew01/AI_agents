# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | Abstract and keywords; the author block, affiliation line and copyright line are just above it, Figure 1 just below |
| 1. Introduction | Motivation (limits of nonlinear, data-driven and Koopman reachability), the name ScaRe-Kro, and the four contributions |
| 2. Related Work | Run-in paragraphs on reachability via linear relaxation (NNV, CROWN), Koopman/Carleman reachability, and data-driven reachability |
| 3. Preliminaries | System model (1a)/(1b), interval, ball and sequence notation; Koopman operators and the autoencoder lifting; NNV with Proposition 1 (CG Robustness); exact reachable set and RSOA; split conformal prediction |
| 4. Problem Statement | Planner, initial-state perturbation, the high-probability RSOA target; Problem 1 (model learning and controller design) and Problem 2 ((1 - delta)-confident RSOA) |
| 5. Methodology | One-paragraph roadmap of Sections 5.1-5.4 (Fig. 2, Alg. 1) |
| 5.1. Koopman Operator Training | Composite training loss (reconstruction, latent consistency, multi-step prediction), initialisation and activations |
| 5.2. Koopman Tracking LQR Design | Feedforward control (2), lifted error dynamics, finite-horizon LQR and the tracking laws (3)-(4) |
| 5.3. Reachability Analysis for Closed-Loop Koopman Dynamics | TKFL computational graph, decoded closed-loop rollout (5)-(6), construction of the CG, the KRS optimisation (7), Lemma 1; Figure 2 (block diagram) at the end |
| 5.4. Conformalizing Koopman Reachable Sets | Calibration data and rollouts (8)-(9), normalised SNSA score, quantile and error bounds, CP coverage display, Theorem 1 with the CKRS (10), Offline Calibration paragraph and runtime use |
| 6. Experiments | Metrics, Baselines, the four baseline comparisons (learned reachability, pure CP with Figure 3, hybrid CP+NNV, pure NNV), Table 1, and per-system paragraphs (unicycle, planar and 3D quadcopter with Figure 4, MuJoCo hopper and swimmer) |
| 7. Conclusion | Summary and two directions of future work |
| References | Bibliography, 40 entries in author-year style |
| 8. Appendix | Appendix roadmap (proofs, algorithm, experiment details) |
| 8.1. Proofs | Lemma 1 restated with its proof, Theorem 1 restated (CKRS display numbered (11)) with its three-step proof |
| 8.2. Algorithm | Prose description of the CKRS procedure followed by Algorithm 1 (image and line-by-line transcription) |
| 8.3. Experiment Details and Additional Experiments | Roadmap of 8.3.1-8.3.9 |
| 8.3.1. Dynamics. | Unicycle (12), planar quadcopter (13) and 3D quadcopter (14) dynamics with parameters and time steps |
| 8.3.2. Comparison between neural Koopman liftings and polynomial liftings | Polynomial (PyKoopman, degree-3) vs neural lifting on the hopper; Table 2 (RMSE per state) |
| 8.3.3. Baseline comparison with Bansal and Tomlin (2021). | DeepReach comparison on the unicycle; Figure 5 |
| 8.3.4. Baseline comparison with Hashemi et al. (2024). | CP-NNV comparison on the 3D quadcopter; Figure 6 |
| 8.3.5. Additional results on unicycle system. | Unicycle CKRS; Figure 7 |
| 8.3.6. Additional results on planar quadcopter system. | Planar quadcopter, offline CP bounds over four references; Figure 8 (panels a-d) |
| 8.3.7. Additional results on 3D quadrotor system. | 3D quadrotor with alternative references and the obstacle view; Figures 9 (panels a-d) and 10 |
| 8.3.8. Additional results on MuJoCo hopper system. | Full 11-state hopper results; Figure 11 |
| 8.3.9. Additional results on MuJoCo swimmer system. | Full 28-state swimmer results; Figure 12 |
| Conversion notes | Source version, conversion method, equation-number and float-placement remarks, source slips kept as printed |

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
