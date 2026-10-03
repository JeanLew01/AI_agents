# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | One-paragraph statement of the framework and its three parts |
| 1 Introduction | Motivation, model assumptions (white-box transition graph, black-box simulator), overview of the verification algorithm and of the reasoning principles, applications, related work |
| 2 Modeling/semantic framework | Opening of Section 2; running example announced |
| 2.1 Powertrain control system | Running example: state variables, modes, requirement |
| 2.2 Transition graphs | Definition 2.1 (transition graph), paths, traces; Figure 1 |
| 2.2.1 Trace containment | Mode maps, trace containment, Definition 2.2 (forward simulation), Proposition 2.3 |
| 2.2.2 Sequential composition of graphs | Definition 2.4 (sequential composition), Proposition 2.5 |
| 2.3 Trajectories | Labeled trajectories, prefix-closed and deterministic sets, standing assumptions on trajectories, Definition 2.6 (simulator), trajectory containment |
| 2.4 Hybrid systems | Definition 2.7 (hybrid system), executions, reachable states and reach tube, bounded safety verification problem, Remark 2.8, Proposition 2.9 |
| 2.5 ADAS and autonomous vehicle benchmarks | Vehicle modes, variables and the scenarios Merge, AutoPassing, Merge3, AEB |
| 3 Invariant verification | Opening of Section 3: reach tube computation as the subproblem |
| 3.1 Discrepancy functions | Definition of a discrepancy function, conditions (a) with inequality (1) and (b); pointers to model-based methods |
| 3.1.1 Learning linear separators. | Linear separator (2), error under a distribution, two-step sampling algorithm, Footnote 1, Proposition 3.1 (PAC statement and sample count) with proof |
| 3.1.2 Learning discrepancy functions | Global exponential discrepancy (GED) and piece-wise exponential discrepancy (PED): forms, reduction to linear separators, objective, choice of time points |
| 3.1.3 Experiments on learning discrepancy | Numbers of training and test traces and observed accuracy of learned discrepancies |
| 3.2 Verification algorithm | GraphReach (Algorithm 1: image and transcription), LearnDiscrepancy and ReachComp, VerifySafety in words, temporal properties, paragraph 'Correctness', Theorem 3.2 (soundness) |
| 3.3 Experiments on safety verification | Implementation, Figure 2, Table 1 (benchmarks, initial sets, refinements, run times), remarks on GED versus PED and on random counter-example search |
| 4 Reasoning principles for trace containment | Propositions 4.1, 4.2, 4.3 and Theorem 4.4 (sequential composition with itself); proofs are printed for Proposition 4.1 and Theorem 4.4 only |
| 4.1 Experiments on trace containment reasoning | Graph simulation on the AEB example (Figure 3) and sequential composition on the powertrain example |
| 5 Conclusions | Authors' summary and one direction for further work |
| References | Bibliography [1]-[56] |
| A Appendix | Start of Appendix A (after the references); its content is in the subsections A.1, A.2, A.3 |
| A.1 ADAS and autonomous vehicle venchmarks | Appendix A: detailed scenario descriptions (MergeBehind, MergeAhead, AutoPassing, AEB, MergeBetween); heading spelled as printed |
| A.2 Automatic transmission control | Appendix A: the ATS benchmark, its modes, variables and unsafe set |
| A.3 Safety verification algorithm | Appendix A: VerifySafety (Algorithm 2: image and transcription) |
| Conversion notes | Source version, numbering, notation and TeX/PDF differences, where the guarantees are, layout decisions, source errors kept as printed (at the end of the file) |

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
