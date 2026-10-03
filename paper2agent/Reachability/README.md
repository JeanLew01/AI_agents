# Sampling-based reachability: paper skills

Twenty paper skills, one per paper, built with the Paper2Agent `paper2skill` workflow. Each
skill is a reading package that lets Claude answer detailed questions about one paper
(assumptions, theorem statements, bounds, algorithms, experiments) from the paper's own text.

The papers are the ones cited as sampling-based or data-driven reachable-set methods in
"On the Limits of Sampling-Based Reachability" (CoRL 2026); skill names are the bib keys of
`~/overleaf_project/CoRL_2026/CoRL_2026/example.bib` plus `-paper`.

## Using a skill

The skills are linked into `~/.claude/skills/`, so they work in Claude Code from any folder:

- call one directly: `/lew2022simple-paper`, then ask your question, or
- just ask ("What does Theorem 2 of Lew 2022 assume?") and Claude picks the matching skill.

Answers should be cited by section, theorem number or equation tag. The packages carry no PDF
page numbers.

## The skills

| Skill | Paper | PDF version used | Authors' TeX used |
| --- | --- | --- | --- |
| `liebenwein2018sampling-paper` | Sampling-Based Approximation Algorithms for Reachability Analysis with Provable Guarantees | RSS 2018 proceedings | no |
| `devonport2021data-paper` | Data-Driven Reachability Analysis with Christoffel Functions | arXiv:2104.13902v1 | yes |
| `devonport2023data-paper` | Data-Driven Reachability Analysis and Support Set Estimation with Christoffel Functions | arXiv:2112.09995v1 | yes |
| `lew2021sampling-paper` | Sampling-based Reachability Analysis: A Random Set Theory Approach with Adversarial Sampling | arXiv:2008.10180v2 | yes |
| `lew2022simple-paper` | A Simple and Efficient Sampling-based Algorithm for General Reachability Analysis | arXiv:2112.05745v3 | yes |
| `devonport2020estimating-paper` | Estimating Reachable Sets with Scenario Optimization | PMLR v120 (L4DC 2020) | no |
| `dietrich2025data-paper` | Data-Driven Reachability with Scenario Optimization and the Holdout Method | arXiv:2504.06541v2 | yes |
| `dietrich2024nonconvex-paper` | Nonconvex Scenario Optimization for Data-Driven Reachability | PMLR v242 (L4DC 2024) | no |
| `sartipizadeh2019voronoi-paper` | Voronoi Partition-based Scenario Reduction for Fast Sampling-based Stochastic Reachability Computation of LTI Systems | arXiv:1811.03643v1 | yes |
| `hewing2019scenario-paper` | Scenario-based Probabilistic Reachable Sets for Recursively Feasible Stochastic Model Predictive Control | accepted version, ETH Research Collection | no |
| `fan2017dryvr-paper` | DryVR: Data-driven verification and compositional reasoning for automotive systems | arXiv:1702.06902v1 | yes |
| `gruenbacher2022gotube-paper` | GoTube: Scalable Stochastic Verification of Continuous-Depth Models | arXiv:2107.08467v2 | yes |
| `tebjou2023data-paper` | Data-driven Reachability using Christoffel Functions and Conformal Prediction | PMLR v204 (COPA 2023) | yes (arXiv source, PDF is PMLR) |
| `lin2024verification-paper` | Verification of Neural Reachable Tubes via Scenario Optimization and Conformal Prediction | arXiv:2312.08604v2 | yes |
| `hashemi2023data-paper` | Data-Driven Reachability Analysis of Stochastic Dynamical Systems with Conformal Inference | arXiv:2309.09187v1 | yes |
| `hashemi2025pca-paper` | PCA-DDReach: Efficient Statistical Reachability Analysis of Stochastic Dynamical Systems via Principal Component Analysis | arXiv:2505.14935v1 | yes |
| `selim2022safe-paper` | Safe Reinforcement Learning Using Black-Box Reachability Analysis | arXiv:2204.07417v2 | yes |
| `ganai2023iterative-paper` | Iterative Reachability Estimation for Safe Reinforcement Learning | arXiv:2309.13528v1 | yes |
| `liu2025recurrent-paper` | Recurrent Control Barrier Functions: A Path Towards Nonparametric Safety Verification | arXiv:2510.02127v1 | yes |
| `ouyang2026symplectic-paper` | Symplectic Inductive Bias for Data-Driven Target Reachability in Hamiltonian Systems | arXiv:2604.17213v1 | yes |

Exact source URLs and checksums are in `papers/SOURCES.tsv` and `papers/SHA256SUMS`.

## What is in a package

```
skills/<key>-paper/
├── SKILL.md                 # how to read the package
├── references/index.md      # section-level navigation
├── references/paper.md      # full text, mathematics as LaTeX, conversion notes at the end
└── assets/                  # figure and algorithm crops (JPEG), tables (CSV)
```

Things to know when relying on a package:

- **Version.** Each package reflects the PDF version in the table, usually the arXiv version.
  Numbering can differ from the published version (for example `devonport2023data` numbers
  algorithms by section: the journal's "Algorithm 3" is "Algorithm 3.3" there). Titles follow
  the PDF, so two differ from the bib entries (`gruenbacher2022gotube`, `sartipizadeh2019voronoi`).
- **Mathematics is LaTeX, not images.** It was taken from the authors' TeX where available and
  checked against the PDF; for the four papers without TeX it was transcribed from page
  images. Because of this, the tool's strict verification ends as `reviewed_with_limitations`:
  every page's parser differences were inspected and recorded, none is unresolved.
- **Errors in the papers are kept as printed.** Each package ends with "Conversion notes" that
  list the paper's own slips and inconsistencies found during review, so they are not mistaken
  for conversion errors and are not silently corrected.
- **Figures** are image crops; values that exist only inside plots are not transcribed.

## Verification

1. Every page of every paper was reviewed by an agent against the page image, and every
   package passes `paper_bundle.py verify --strict` (exit 0). Reports: `logs/reports/<key>.md`.
2. A second, independent agent then compared every finished package with the PDF (theorem
   statements, numbered equations, algorithms, table cells, figure crops, completeness).
   Findings: `logs/verify/<key>.md`; per-paper outcome: `logs/STATE.md`.

Outcome of the second pass (2026-10-02, all 20 packages):

- No error in the mathematics or the text of any package.
- Two figure issues. `lew2021sampling`: the Figure 6 crop was cut below the axis; repaired.
  `fan2017dryvr`: the packaging tool's renderer (MuPDF) draws Figure 3(c) as translucent
  striped bands where other PDF renderers show solid bands; the image could not be replaced,
  so the package's conversion notes describe the solid colours in words.
- Small slips in the packages' own conversion notes or index (`tebjou2023data`,
  `devonport2021data`, `lin2024verification`, `fan2017dryvr`); corrected.
- Typographic differences left as they are: italic "Proof"/"Remark" labels shown bold, a few
  upright-vs-italic or script-vs-calligraphic symbols, and theorem bodies not set in italics,
  so the end of a statement is sometimes only recorded in the conversion notes
  (`hashemi2025pca` Definition 4 and Proposition 5, `ouyang2026symplectic` Proposition 1).

## Folder layout

| Path | Content |
| --- | --- |
| `papers/` | The 20 PDFs, named by bib key |
| `tex-source/` | arXiv TeX sources (transcription aid only) |
| `paper-review/` | Review directories of `paper_bundle.py` (page plans, evidence, adjudications) |
| `skills/` | The finished packages (linked from `~/.claude/skills/`) |
| `staging/` | Intermediate builds; safe to delete |
| `logs/` | `REVIEWER_BRIEF.md`, `VERIFIER_BRIEF.md`, `STATE.md`, `accept.sh`, per-paper reports, findings and scripts |

To re-check a package and re-create its link: `logs/accept.sh <key>`.

The PDFs are copyrighted by their authors and publishers; keep `papers/` and `skills/` out of
public repositories.
