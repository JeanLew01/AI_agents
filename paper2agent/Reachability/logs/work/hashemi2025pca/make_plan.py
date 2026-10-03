#!/usr/bin/env python3
"""Set title/notes/reading_order in plan.json and title/review/navigation in bundle.json (idempotent)."""
import json
from pathlib import Path
R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/hashemi2025pca-paper"
D = W / "documents/s001-hashemi2025pca"
TITLE = "PCA-DDReach: Efficient Statistical Reachability Analysis of Stochastic Dynamical Systems via Principal Component Analysis"

plan = json.loads((D / "plan.json").read_text(encoding="utf-8"))
plan["title"] = TITLE

# ---- reading order: page order, with footnote 2 and the appendix floats moved ----
order = []
for pg in plan["pages"]:
    st = json.loads((D / pg["file"]).read_text(encoding="utf-8"))
    order += [i["id"] for i in st["items"] if i["kind"] != "omit"]
MOVES = [  # (items to move, in order) -> placed directly after this item
    (["p0002-b005"], "p0003-b000"),                                           # Footnote 2 after the end of the 'Related Work' paragraph
    (["p0014-b000", "p0014-b001"], "p0016-b000"),                             # Figure 3 after the end of the A.1 paragraph
    (["p0015-b000", "p0015-b001"], "p0016-b004"),                             # Figure 4 after the end of Section A.2
    (["p0015-b003", "p0015-b005", "p0015-b002", "p0015-b004"], "p0016-b006"), # Figures 5 and 6 after Section A.3
]
for ids, after in MOVES:
    for i in ids:
        order.remove(i)
    k = order.index(after) + 1
    order[k:k] = ids
assert len(order) == len(set(order))
plan["reading_order"] = order

plan["notes"] = [
    "Source version: arXiv:2505.14935v1 [cs.RO], 20 May 2025 (16 pages, single column, JMLR-style preprint layout); authors Navid Hashemi, Lars Lindemann, Jyotirmoy Deshmukh (University of Southern California). The paper was published in the proceedings of the International Conference on Neuro-symbolic Systems (NeuS) 2025, PMLR vol. 288, pp. 693-707. This package was made from the arXiv v1 PDF only; the proceedings version was not compared, so its numbering and any corrections made there are not reflected here. In this arXiv version the Acknowledgements are the numbered Section 5 and the Conclusion is Section 6; Appendix A (details of the three experiments) follows the references.",
    "Mathematics was transcribed to LaTeX from the authors' arXiv TeX source (neus2025-arxiv.tex, sections/*.tex, sections/macros.tex, neus2025-arxiv.bbl), with the authors' private macros expanded to standard LaTeX, and every formula was checked against the PDF pages (170 dpi page renders plus 220-500 dpi crops of all mathematical regions). TeX source and PDF agree everywhere; no formula is kept as an image only. Equation numbers (1)-(18) are the printed ones and are given as `\\tag{n}`. Manual spacing commands of the source (runs of negative thin spaces used to squeeze displays (6) and (15) into the line) were dropped; no symbol was changed. Asterisk superscripts are written `^{\\ast}`.",
    "Notation as printed: the horizon is an upright $\\mathrm{K}$ and the time index an italic $k$; $\\sigma^{\\mathsf{sim}}_{s_0}$, $\\sigma^{\\mathsf{real}}_{s_0}$ are simulated / real trajectories with distributions $\\mathcal{D}^{\\mathsf{sim}}_{S,\\mathrm{K}}$, $\\mathcal{D}^{\\mathsf{real}}_{S,\\mathrm{K}}$; $\\mathcal{J}^{\\mathsf{sim}}_{S,\\mathrm{K}}$, $\\mathcal{J}^{\\mathsf{real}}_{S,\\mathrm{K}}$ are the residual distributions; $\\mathsf{PE}$ is the vector of prediction errors $R^j$ (capital $R$), $r^j$ (lower case) are the errors mapped to the principal axes, $\\mathsf{V}^q$ the eigenvector matrix of segment $q$, $\\omega_j$ the scaling factors, $\\mathcal{T}^{\\mathsf{trn}}$ the training dataset and $\\mathcal{R}^{\\mathsf{calib}}$ the calibration dataset. The single letter $\\rho$ denotes the residual under both distributions (the authors' two macros print the same symbol); which one is meant is told only by '$\\rho\\sim\\mathcal{J}^{\\mathsf{sim}}_{S,\\mathrm{K}}$' or '$\\rho\\sim\\mathcal{J}^{\\mathsf{real}}_{S,\\mathrm{K}}$'. In this paper $\\delta\\in(0,1)$ is the confidence (coverage) level, e.g. 99.99%, not a failure probability, and $\\delta X$ is the name of the inflating hypercube (one symbol). Citations are natbib author-year without parentheses around the group, exactly as printed; 'Hashemi et al. (2024b)' is the method the paper extends and 'Cauchois et al. (2024)' the robust conformal inference reference.",
    "Theorem-like blocks share one counter: Definition 1 (residual distributions), Definition 2 (star set), Lemma 3 (inflated reachset is a $\\delta$-confident flowpipe; stated without proof, 'See Hashemi et al. (2024b) for the proof'), Definition 4 (calibration dataset), Proposition 5 (the PCA-based probabilistic guarantee, with its proof), Remark 6. Their bodies are italic in the print and are written upright here; each block ends where the TeX environment ends (recorded in the page review notes). 'Related Work', 'Notation', 'Training and Deployment Environments', 'Surrogate Flowpipe and Star-Set', 'Inflating Hypercube' and '$\\delta$-Confident Flowpipe & Probabilistic Reachability' are bold run-in paragraph titles, not numbered headings; they are kept as bold text at the start of their paragraphs. The paper contains no algorithm box.",
    "Floats and footnotes: Figures 1 and 2 are image crops with verbatim captions at their printed places (Figure 1 is placed after the paragraph of Section 3.1 that it interrupts in the print). Table 1 is a CSV (assets/table/table-1.csv) whose two printed header rows are combined into single column names; a line marked 'Conversion note on Table 1 (not part of the paper)' follows its caption. Figures 3-6 are numbered in the main sequence but printed in the appendix area (Figure 3 on the page of the last references, Figures 4-6 on a float page inside Section A.1); in this file Figure 3 follows Section A.1, Figure 4 follows Section A.2 and Figures 5 and 6 follow Section A.3, i.e. each follows the text that cites it (Figure 6 is cited in Section 4.2). Their tick labels and legends are inside the image crops only. The six footnotes are placed after the paragraph (or theorem-like block, or display) that carries the mark, as 'Footnote n: ...'; the marks are written as a superscript number with a space in front.",
    "IMPORTANT for citing the guarantee (all of this is printed so in the source PDF and in the authors' TeX; these are not conversion errors). (a) Inequality signs are not uniform: Section 2.3 has $\\Pr[\\rho<\\rho_\\ell]\\ge\\delta$ for ordinary conformal inference and $\\Pr[\\rho<\\rho_{\\ell^{\\ast}}]>\\delta$ for robust conformal inference under $\\mathsf{TV}(\\mathcal{J}^{\\mathsf{real}}_{S,\\mathrm{K}},\\mathcal{J}^{\\mathsf{sim}}_{S,\\mathrm{K}})\\le\\tau$ with $\\tau>0$; Section 2.4, Section 3.2 and Proposition 5 require the total variation to be 'less than' $\\tau$ (strict); the $\\delta$-confident flowpipe is defined with $\\Pr[\\sigma^{\\mathsf{real}}_{s_0}\\in X]\\ge\\delta$, Lemma 3 assumes $\\Pr[\\mathsf{PE}\\in\\delta X]>\\delta$, Proposition 5 concludes $\\Pr[P(r^1,\\ldots,r^{n\\mathrm{K}})=\\top]>\\delta$, and its proof works with $\\Pr[\\rho\\le\\rho^{\\ast}_{\\delta,\\tau}]\\ge\\delta$ and ends with '$\\ge\\delta$'. (b) Proposition 5 says 'Assume $\\rho^{\\ast}_{\\delta,\\tau}$ is the $\\delta$-quantile of $\\rho\\sim\\mathcal{J}^{\\mathsf{real}}_{S,\\mathrm{K}}$', while the paragraph before it defines $\\rho^{\\ast}_{\\delta,\\tau}:=\\rho_{\\ell^{\\ast}}$ as 'an upper bound for the residual's $\\delta$-quantile'. (c) The paper writes $\\Pr[\\cdot]$ throughout without stating the probability space (for instance whether the calibration samples are included in the randomness); its statements are those of Section 2.3 and Proposition 5, and the robust-conformal step is attributed to Cauchois et al. (2024) without proof. (d) The theory asks for a threshold $\\tau>0$; Experiments 1 and 2 use $\\tau=0$ (Table 1, Section 4). (e) The principal axes, the centre $\\overline{\\mathsf{PE}}^q$ and the scaling factors $\\omega_j$ are computed from the training dataset, and the quantile from a separate calibration dataset (Definition 4); the paper states that reusing the training dataset for the conformal step 'violates CI rules'.",
    "Further source slips kept as printed: in (8) the last state of segment $q$ is written $s_{t_q+T_i}$ (index $T_i$; the segment length is $T_q$ elsewhere); in (10) the second factor of the covariance, $(\\mathsf{PE}^{q}-\\overline{\\mathsf{PE}}^{q})$, has no sample index $i$ and the transpose sits on the first factor although (9) writes $\\mathsf{PE}^q_i$ as a row; '$i\\in|\\mathcal{T}^{\\mathsf{trn}}|$', '$i\\in|\\mathcal{R}^{\\mathsf{calib}}|$' and '$j\\in n\\mathrm{K}$' without square brackets; the global inflating hypercube after (17) is written $\\langle\\overline{\\mathsf{PE}},V,P\\rangle$ with an italic $V=\\mathbf{diag}(V^1,\\ldots,V^N)$ instead of the sans-serif $\\mathsf{V}^q$; in Section 4.1 the noise covariance is printed with a stray ']' inside a subscript; the two arguments of $\\mathsf{TV}$ appear in both orders; the realization of the process and the joint distribution start at index 1 ($s_1,\\ldots,s_\\mathrm{K}$) while the random vectors are $S_0,\\ldots,S_\\mathrm{K}$; the heading of Section 3.1 is spelled 'Scalabilty'; wording such as 'caligraphic', 'In other word', 'this results', 'restricted to utilized approx star' is the authors'. The page-level review notes in the external review directory list these page by page.",
    "Consistency checks done during conversion (computed by the converter, not printed in the paper): with the transcribed rank formula (4), $\\ell^{\\ast}=\\lceil(L+1)(1+1/L)(\\delta+\\tau)\\rceil$, the calibration sizes of Table 1 give $\\ell^{\\ast}=20000=L$ for $L=20000$, $\\delta=0.9999$, $\\tau=0$ (Experiments 1 and 2; the condition $\\ell^{\\ast}\\le L$ holds with equality) and $\\ell^{\\ast}=9902\\le L$ for $L=10000$, $\\delta=0.95$, $\\tau=0.04$ (Experiment 3). In Table 1 the counts 451 and 4501 of Experiment 2 equal the number of indices $i\\in 50,\\ldots,500$ and of time steps 500 through 5000 given in Section A.2.",
]
(D / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

b = json.loads((W / "bundle.json").read_text(encoding="utf-8"))
b["title"] = TITLE
src = b["sources"][0]
src["title"] = TITLE
src["reviewed"] = True
src["review_notes"] = (
    "All 16 PDF pages (arXiv:2505.14935v1) were compared item by item with 170 dpi page renders and 220-500 dpi crops of every "
    "mathematical region, of Table 1 and of the six figures, and with the authors' TeX source (main file, sections/*.tex, macros, "
    ".bbl). Every page with mathematics was rewritten: all inline and display mathematics is LaTeX taken from the TeX source with the "
    "private macros expanded; all 18 extractor 'formula' image items were replaced by $$ blocks with \\tag for the printed equation "
    "numbers (1)-(18); Definitions 1, 2, 4, Lemma 3, Proposition 5 with its proof and Remark 6 carry their printed labels in bold. "
    "Figures 1-6 are image crops (bboxes measured with ink profiles and checked on crops) with verbatim captions; Table 1 is a CSV read "
    "on a 300 dpi crop and compared with the TeX tabular. The 28 bibliography entries were generated from the .bbl, compared "
    "automatically with the PDF text layer and read on the page renders. The six footnotes follow the paragraphs that carry their "
    "marks. Omitted regions: the vertical arXiv stamp on page 1 and the page numbers 1-16. plan.json reading_order moves Footnote 2 "
    "after the end of its paragraph and Figures 3-6 after the appendix sections that cite them. Authors' typos and inconsistencies are "
    "kept and listed in the page review notes and in the conversion notes. Review was done by one agent; no independent second "
    "verifier was used."
)
P = "references/paper.md"
b["navigation"] = [
    {"file": P, "heading": "Abstract", "purpose": "One-paragraph statement of the problem, the PCA + conformal inference idea and the case studies; keywords"},
    {"file": P, "heading": "1 Introduction", "purpose": "Motivation, the three-step method of Hashemi et al. (2024b) being extended, the two contributions, Related Work paragraph, Notation paragraph, Footnotes 1-2"},
    {"file": P, "heading": "2 Preliminaries", "purpose": "Section heading only; Sections 2.1-2.4 follow (setting, surrogate model, conformal inference and the earlier method, problem definition)"},
    {"file": P, "heading": "2.1 Stochastic Dynamical Systems", "purpose": "Trajectory and initial-state distributions, training vs deployment environment, distribution shift"},
    {"file": P, "heading": "2.2 Surrogate Model: Reachability & Error Analysis", "purpose": "Surrogate model (1), prediction errors (2), Definition 1 (residual distributions), total-variation shift, surrogate flowpipe, Definition 2 (star set, (3))"},
    {"file": P, "heading": "2.3 Conformal Inference & Probabilistic Reachability", "purpose": "Conformal and robust conformal quantile statements, rank formula (4), max-residual (5) and inflating hypercube (6)-(7) of the earlier method, definition of a delta-confident flowpipe, Lemma 3"},
    {"file": P, "heading": "2.4 Problem Definition", "purpose": "Problem statement (flowpipe valid under a total-variation bound) and the two sources of conservatism addressed"},
    {"file": P, "heading": "3 Scalable and Accurate Data Driven Reachability Analysis", "purpose": "One-sentence overview of Section 3"},
    {"file": P, "heading": "3.1 Improved Scalabilty and Accuracy for Training Surrogate Models", "purpose": "Trajectory segmentation (8), one small surrogate model per segment, concatenated star-set flowpipe, Figure 1, Footnote 4"},
    {"file": P, "heading": "3.2 Accurate Inflating Hypercubes via Principal Component Analysis", "purpose": "PCA background, Figure 2, limitations of the earlier hypercube, PCA construction (9)-(11), new residual (12)-(13), Definition 4 (calibration dataset, (14)), Proposition 5 with (15) and proof (16), star-set form of the hypercube (17), Remark 6"},
    {"file": P, "heading": "4 Numerical Evaluation", "purpose": "Experimental setup overview, thresholds used, Table 1 (specification, training, reachability and hypercube runtimes, dataset sizes)"},
    {"file": P, "heading": "4.1 12-Dimensional Quadcopter", "purpose": "Quadcopter states, process noise covariance, initial-state distribution"},
    {"file": P, "heading": "4.2 27-Dimensional Powertrain", "purpose": "Powertrain simulator, noise, sampling time, horizon, division setting, network structure, Footnote 6"},
    {"file": P, "heading": "5 Acknowledgements", "purpose": "Funding and grant numbers"},
    {"file": P, "heading": "6 Conclusion", "purpose": "Authors' three-sentence summary"},
    {"file": P, "heading": "References", "purpose": "Bibliography, 28 author-year entries in alphabetical order"},
    {"file": P, "heading": "Appendix A. Detail of the Experiments", "purpose": "Appendix heading only; Sections A.1-A.3 give the details of Experiments 1-3 and Figures 3-6"},
    {"file": P, "heading": "A.1 Experiment 1:[Comparison with Hashemi et al. (2024b)]", "purpose": "Hovering quadcopter, horizon, division setting, network structure; Figure 3"},
    {"file": P, "heading": "A.2 Experiment 2: [Sequential Goal Reaching Task]", "purpose": "Long-horizon quadcopter task, model interpolation formula (18); Figure 4"},
    {"file": P, "heading": "A.3 Experiment 3: [Reachability with Distribution shift]", "purpose": "Powertrain under distribution shift, threshold and confidence used; Figures 5 and 6"},
    {"file": P, "heading": "Conversion notes", "purpose": "Source version, notation, numbering of theorem-like blocks, placement of floats and footnotes, source inconsistencies in the guarantee (inequality signs, assumptions), source typos kept, consistency checks (at the end of the file)"},
]
(W / "bundle.json").write_text(json.dumps(b, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("plan.json and bundle.json updated;", len(order), "items in reading_order")
