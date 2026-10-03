from pagelib import *
P = 1
items = [
    omit("p0001-b000", [11.0, 185.0, 38.0, 550.0],
         "Vertical arXiv stamp in the left margin ('arXiv:2309.09187v1 [eess.SY] 17 Sep 2023'); page furniture, the version is recorded in the conversion notes.",
         "arXiv:2309.09187v1 [eess.SY] 17 Sep 2023"),
    heading("p0001-b001", B(P, "p0001-b001"),
            "# Data-Driven Reachability Analysis of Stochastic Dynamical Systems with Conformal Inference"),
    text("p0001-b002", B(P, "p0001-b002"),
         r"Navid Hashemi$^{1}$, Xin Qin$^{1}$, Lars Lindemann$^{1}$, and Jyotirmoy V. Deshmukh$^{1}$"),
    text("p0001-b003", B(P, "p0001-b003"),
         r"$^{1}$Thomas Lord Department of Computer Science, University of Southern California"),
    text("p0001-b004", B(P, "p0001-b004"), "September 19, 2023"),
    heading("p0001-b005", B(P, "p0001-b005"), "## Abstract"),
    text("p0001-b006", B(P, "p0001-b006"),
         r"We consider data-driven reachability analysis of discrete-time stochastic dynamical systems using conformal inference. We assume that we are not provided with a symbolic representation of the stochastic system, but instead have access to a dataset of $\mathrm{K}$-step trajectories. The reachability problem is to construct a probabilistic flowpipe such that the probability that a $\mathrm{K}$-step trajectory can violate the bounds of the flowpipe does not exceed a user-specified failure probability threshold. The key ideas in this paper are: (1) to learn a surrogate predictor model from data, (2) to perform reachability analysis using the surrogate model, and (3) to quantify the surrogate model’s incurred error using conformal inference in order to give probabilistic reachability guarantees. We focus on learning-enabled control systems with complex closed-loop dynamics that are difficult to model symbolically, but where state transition pairs can be queried, e.g., using a simulator. We demonstrate the applicability of our method on examples from the domain of learning-enabled cyber-physical systems."),
    heading("p0001-b007", B(P, "p0001-b007"), "## 1 Introduction"),
    text("p0001-b008", B(P, "p0001-b008"),
         "Reachability analysis of stochastic nonlinear dynamical systems is a challenging problem that has been extensively studied in the literature [1–13]. Most of the prior work is *model-based*, i.e., it requires a symbolic model of the dynamical system which can then be over-approximated to obtain *flowpipes* or the set of reachable states of the system over a given time horizon. In this paper, we explore the notion of *model-free reachability analysis*, *i.e.*, to compute reachable sets of the stochastic dynamical system even when we *do not have the symbolic system dynamics*, but have access to a numeric simulator or actual behaviors sampled from the system. A significant advantage of such a data-driven technique is that we obtain not only (probabilistic) reachable sets for the system or the simulation model from which the trajectories are sampled, but we can get results over the possibly *infinite* set of models/systems consistent with the set of sampled trajectories. This provides us the opportunity for an analysis technique that is robust to model uncertainty."),
    text("p0001-b009", B(P, "p0001-b009"),
         "There is growing literature on computing probabilistically approximate reachable sets directly from data. The authors in [14] utilize level sets of Christoffel functions and provide a technique to compute a high accuracy probabilistic reach-set for general nonlinear systems. On the other hand, as a comparison, we only have access to sampled trajectories. The authors in [15] propose specific parametric models (linear or polynomial), to identify the Markovian stochastic dynamics of the system from data, and then perform reachability analysis on the identified models. In contrast, we"),
    pageno(P),
]
save(P, items, r"""
Compared with the 130 dpi render of PDF page 1 and with the authors' TeX source (main.tex, sections/abstract.tex,
sections/intro.tex). The vertical arXiv stamp in the left margin (an empty extractor text item) is set to omit, as is the
page number. Title kept as the single level-1 heading. Author line: the extractor's sup tags replaced by the printed
affiliation superscript written as $^{1}$; affiliation line and the printed date 'September 19, 2023' kept as separate
items. The centred bold word 'Abstract' is a level-2 heading; '1 Introduction' is a level-2 heading with its printed
number. The two occurrences of the horizon symbol in the abstract are written $\mathrm{K}$ (authors' macro \horizon =
\mathrm{K}, printed as an upright K). Line-wrap hyphen removed in 'closed-loop' (real compound hyphen, confirmed in the
TeX source). Italics kept: model-based, flowpipes, model-free reachability analysis, i.e., 'do not have the symbolic
system dynamics', infinite. Citations [1–13], [14], [15] resolved from the .bbl order and checked on the page. The last
paragraph ends in the middle of a sentence ('In contrast, we'); it continues on page 2 (join_previous 'space' there).
""")
