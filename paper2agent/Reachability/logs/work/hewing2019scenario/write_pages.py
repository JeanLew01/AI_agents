#!/usr/bin/env python3
"""Write the reviewed page JSON files for hewing2019scenario (pages given on argv, default all)."""
import json
import os
import sys

D = os.path.expanduser(
    "~/AI_agents/paper2agent/Reachability/paper-review/hewing2019scenario-paper/documents/s001-hewing2019scenario"
)


def T(i, bbox, md, **kw):
    return {"id": i, "kind": "text", "bbox": bbox, "markdown": md, **kw}


def H(i, bbox, md):
    return {"id": i, "kind": "heading", "bbox": bbox, "markdown": md}


def C(i, bbox, md, **kw):
    return {"id": i, "kind": "caption", "bbox": bbox, "markdown": md, **kw}


def save(n, items, notes):
    path = f"{D}/pages/page-{n:04d}.json"
    page = json.load(open(path))
    page["items"] = items
    page["reviewed"] = True
    page["review_notes"] = notes
    ids = [it["id"] for it in items]
    assert len(ids) == len(set(ids)), "duplicate ids"
    for it in items:
        md = it.get("markdown", "")
        assert md.count("$") % 2 == 0, (it["id"], "unbalanced $")
    with open(path, "w") as f:
        json.dump(page, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("wrote", path, len(items), "items")


# --------------------------------------------------------------------------- page 1
def page1():
    items = [
        H("p0001-cover-heading", [34.0, 120.0, 509.0, 160.0], "## Repository cover sheet (ETH Research Collection)"),
        {
            "id": "p0001-b001",
            "kind": "omit",
            "bbox": [29.0, 34.0, 163.0, 65.0],
            "markdown": "",
            "reason": "ETH Zürich logo (wordmark image 'ETH zürich') at the top left of the repository cover sheet; decorative, no bibliographic content.",
        },
        T("p0001-b000", [507.0, 52.0, 562.0, 62.0], "ETH Library"),
        T(
            "p0001-b002",
            [34.0, 165.0, 509.0, 313.0],
            "Scenario-Based Probabilistic Reachable Sets for Recursively Feasible Stochastic Model Predictive Control",
        ),
        T("p0001-b003", [56.0, 409.0, 127.0, 417.0], "**Journal Article**"),
        T("p0001-b004", [56.0, 438.0, 210.0, 460.0], "**Author(s):** Hewing, Lukas; Zeilinger, Melanie N."),
        T("p0001-b005", [56.0, 476.0, 130.0, 495.0], "**Publication date:** 2020-04"),
        T(
            "p0001-b006",
            [56.0, 512.0, 272.0, 533.0],
            "**Permanent link:** https://doi.org/https://doi.org/10.3929/ethz-b-000389523",
        ),
        T(
            "p0001-b007",
            [56.0, 548.0, 235.0, 569.0],
            "**Rights / license:** In Copyright - Non-Commercial Use Permitted",
        ),
        T(
            "p0001-b009",
            [56.0, 585.0, 360.0, 606.0],
            "**Originally published in:** IEEE Control Systems Letters 4(2), https://doi.org/10.1109/lcsys.2019.2949194",
        ),
        T(
            "p0001-b011",
            [56.0, 621.0, 286.0, 642.0],
            "**Funding acknowledgement:** - Safety and Performance for Human in the Loop Control ()",
        ),
        T(
            "p0001-b013",
            [56.0, 776.0, 433.0, 795.0],
            "This page was generated automatically upon download from the ETH Zurich Research Collection. For more information, please consult the Terms of use.",
        ),
        T(
            "p0001-links",
            [56.0, 700.0, 433.0, 760.0],
            "Conversion note (not printed text): hyperlink targets of the underlined cover-sheet entries, read from the PDF link annotations: "
            "\"Hewing, Lukas\" → https://orcid.org/0000-0002-2770-4687 ; "
            "\"In Copyright - Non-Commercial Use Permitted\" → http://rightsstatements.org/page/InC-NC/1.0/ ; "
            "\"ETH Zurich Research Collection\" → https://www.research-collection.ethz.ch ; "
            "\"Terms of use\" → https://www.research-collection.ethz.ch/terms-of-use",
        ),
    ]
    notes = (
        "ETH Research Collection cover sheet, compared with a 200 dpi render. Every printed text field is kept as plain text under the added "
        "heading '## Repository cover sheet (ETH Research Collection)' (the heading itself is not printed; it was requested for this conversion). "
        "The large blue title on the cover sheet is kept as plain text (it prints 'Scenario-Based', whereas the paper's own title on PDF page 2 "
        "prints 'Scenario-based'); the '#' title of the package is the page-2 title. Each bold field label printed on its own line "
        "(Author(s), Publication date, Permanent link, Rights / license, Originally published in, Funding acknowledgement) was merged with its "
        "value into one line; the extractor had turned 'Journal Article', 'Rights / license', 'Originally published in' and 'Funding "
        "acknowledgement' into headings and wrapped link text in <u> tags, both removed. The permanent link is printed with a doubled prefix "
        "'https://doi.org/https://doi.org/10.3929/ethz-b-000389523' and the funding entry ends with empty parentheses '()'; both kept as printed. "
        "Omitted: the ETH Zürich logo (top left). The small green ORCID icon after 'Hewing, Lukas' is a decoration inside the author line and has "
        "no text. Added one clearly labelled conversion-note item listing the four hyperlink targets that are not visible as text (ORCID, rights "
        "statement, Research Collection, Terms of use), read from the PDF link annotations with PyMuPDF. In the reading order (plan.json) this "
        "whole block is placed after the page-2 title, author line and first-page footnote, before the abstract."
    )
    save(1, items, notes)


# --------------------------------------------------------------------------- page 2
def page2():
    L = [48.0, 301.0]
    R = [311.0, 564.0]
    items = [
        H(
            "p0002-b000",
            [51.0, 60.0, 561.0, 96.0],
            "# Scenario-based Probabilistic Reachable Sets for Recursively Feasible Stochastic Model Predictive Control",
        ),
        T("p0002-b001", [222.0, 107.0, 390.0, 118.0], "Lukas Hewing, Melanie N. Zeilinger"),
        T(
            "p0002-b007",
            [48.0, 713.0, 301.0, 730.0],
            "Footnote (unnumbered, first page): This work was supported by the Swiss National Science Foundation under grant no. PP00P2 157601 / 1.",
        ),
        T(
            "p0002-b008",
            [48.0, 731.0, 301.0, 748.0],
            "Footnote (unnumbered, first page): The authors are members of the Institute for Dynamic Systems and Control, ETH Zurich. `[lhewing|mzeilinger]@ethz.ch`",
        ),
        H("p0002-abstract-heading", [48.0, 153.0, 301.0, 164.0], "## Abstract"),
        T(
            "p0002-b002",
            [48.0, 153.0, 301.0, 282.0],
            "*Abstract*—This paper presents a stochastic model predictive control approach (MPC) for linear discrete-time systems subject to "
            "unbounded and correlated additive disturbance sequences, which makes use of the *scenario approach* for offline computation of "
            "probabilistic reachable sets. These sets are used in a tube-based MPC formulation, resulting in low computational requirements. "
            "Using a recently proposed MPC initialization scheme and nonlinear tube controllers, we provide recursive feasibility and "
            "closed-loop chance constraint satisfaction, as well as *hard* input constraint guarantees, which are typically challenging in "
            "tube-based formulations with unbounded noise. The approach is demonstrated in simulation for the control of an overhead crane system.",
        ),
        T(
            "p0002-b003",
            [48.0, 289.0, 301.0, 308.0],
            "*Index Terms*—Predictive control for linear systems; Constrained control; Stochastic optimal control",
        ),
        H("p0002-b004", [135.0, 328.0, 214.0, 336.0], "## I. Introduction"),
        T(
            "p0002-b005",
            [48.0, 344.0, 301.0, 665.0],
            "Stochastic MPC techniques can be broadly classified into *analytic approximation*, and *randomized* formulations [1]. "
            "*Analytic approximation* formulations rely on distributional information, e.g. disturbance mean and variance, to formulate a "
            "(conservative) approximation of the chance constrained optimal control problem. Many closed-loop properties such as convergence, "
            "recursive feasibility and closed-loop chance constraint satisfaction can be established with these approaches for linear systems, "
            "both for bounded (e.g. [2], [3], [4]) and unbounded additive disturbances (e.g. [5], [6], [7]). They typically rely on specific "
            "disturbance distributions, in particular the Gaussian distribution, or are subject to considerable conservatism, e.g. by making use "
            "of Chebyshev-type bounds. The treatment of *hard* input constraints presents a challenge under unbounded noise, since the methods "
            "usually rely on linear tube controllers to reduce uncertainty in the prediction. *Randomized* approaches, on the other hand, rely on "
            "disturbance samples or *scenarios* and make use of guarantees from scenario optimization [8], [9]. This offers great flexibility and "
            "applicability to a wide class of problems, with the additional benefit that no disturbance distribution has to be known, provided "
            "that samples can be obtained. The approaches are, however, typically computationally intensive and closed-loop properties are not "
            "well-established. In particular, recursive feasibility guarantees are often not provided [10], [11], [12], or established for soft "
            "constraints [13], compromising closed-loop chance constraint satisfaction guarantees.",
        ),
        T(
            "p0002-b006",
            [48.0, 667.0, 301.0, 701.0],
            "This paper presents a stochastic MPC scheme that combines properties of both *analytic approximation* and *randomized* approaches, "
            "by using scenarios for offline computation of probabilistic reachable sets (PRS). These take a similar role to error tubes in "
            "tube-based MPC, keeping the online computational complexity of the approach comparable to nominal MPC. For the case of bounded "
            "independent and identically distributed (i.i.d.) multiplicative uncertainty, a related approach was presented in [14], which "
            "similarly samples scenarios offline and guarantees feasibility through a first step constraint and computation of a control "
            "invariant set. In contrast, we guarantee recursive feasibility and closed-loop chance constraint satisfaction based on an MPC "
            "initialization introduced in [7], enabling the treatment of unbounded non-i.i.d. additive disturbances. Compared to *analytic "
            "approximation* methods, the proposed approach facilitates handling a wide variety of disturbance classes by requiring only access "
            "to samples of the disturbance sequence. In addition, the scenario-based tube computation allows for the use of nonlinear tube "
            "controllers, in particular controllers with limited control authority, enabling the treatment of hard input constraints also under "
            "unbounded disturbances.",
        ),
        T(
            "p0002-b010",
            [311.0, 380.0, 564.0, 484.0],
            "The paper is organized as follows: In Section II we present the problem formulation and state definitions for PRS, as well as "
            "results from scenario optimization. Using the PRS definitions, we present the resulting recursively feasible stochastic MPC approach "
            "in Section III. The specific scenario-based computation of PRS is shown in Section IV, enabling the treatment of hard input "
            "constraints. We demonstrate the approach in simulation on an overhead crane in Section V and conclude in Section VI.",
        ),
        H("p0002-b011", [396.0, 506.0, 480.0, 514.0], "## II. Preliminaries"),
        H("p0002-b012", [311.0, 524.0, 413.0, 532.0], "### A. Problem Formulation"),
        T("p0002-b013", [321.0, 541.0, 497.0, 551.0], "We consider a linear time-invariant system"),
        T(
            "p0002-b014",
            [343.0, 556.0, 569.0, 577.0],
            r"$$x(k+1) = Ax(k) + Bu(k) + \bar{w}(k) + w(k) \tag{1}$$",
        ),
        T(
            "p0002-b015",
            [311.0, 582.0, 564.0, 653.0],
            r"with state $x(k) \in \mathbb{R}^n$ and input $u(k) \in \mathbb{R}^{n_u}$. The system is subject to additive disturbances taking "
            r"values in $\mathbb{R}^n$, which we split into a known part in a compact set $\bar{w}(k) \in \bar{\mathcal{W}}$ (e.g. a known mean) "
            r"and a stochastic component $w(k)$. Introducing this distinction facilitates the design of tube controllers, which can be carried "
            r"out with respect to $w(k)$.",
        ),
        T(
            "p0002-b016",
            [311.0, 655.0, 564.0, 749.0],
            r"The goal is to control this system for large, but finite, run times $\bar{N}$, where we assume the stochastic disturbance sequence "
            r"to be distributed according to $W = [w(0)^{\mathsf{T}}, \ldots, w(\bar{N})^{\mathsf{T}}]^{\mathsf{T}} \sim \mathcal{Q}$. We consider "
            r"general non-i.i.d. disturbance sequences with potentially unbounded support, such that at each time step $w(k)$ can take values in "
            r"all of $\mathbb{R}^n$. While the distribution does not need to be known, we assume access to samples of the (conditional) "
            r"disturbance sequence. The system is subject to",
        ),
    ]
    notes = (
        "First page of the paper itself (IEEE two-column), compared with 200 dpi and 300 dpi renders. The printed title is the single '#' "
        "heading (extractor's bold markers removed). Reading order fixed: left column, then right column; the paragraph 'This paper presents a "
        "stochastic MPC scheme ...' is split by the column break after 'offline computation of' and was merged with its right-column "
        "continuation 'probabilistic reachable sets (PRS). ...' into one item (p0002-b006; former item p0002-b009 merged into it). The "
        "unnumbered first-page footnote (funding: Swiss National Science Foundation grant no. 'PP00P2 157601 / 1', printed with a space inside "
        "the grant number; affiliation and e-mail pattern '[lhewing|mzeilinger]@ethz.ch', printed in typewriter type) is printed at the bottom "
        "of the left column; it is placed directly after the author line so that it does not interrupt the sentence that runs across the "
        "column break, and each of its two paragraphs is prefixed 'Footnote (unnumbered, first page):'. Added a '## Abstract' heading (the page "
        "prints 'Abstract—'); the abstract and index terms are printed in bold, bold dropped, italic emphasis (*scenario approach*, *hard*) "
        "kept. Line-wrap hyphens repaired: 'tube-based' (real compound, restored from extractor's 'tubebased'), 'closed-loop' (real compound, "
        "restored from 'closedloop'), 'requirements', 'constraint', 'particular', 'disturbance', 'computational', 'definitions', 'treatment'. "
        "Section headings: small caps written in title case ('I. Introduction', 'II. Preliminaries'), subsection 'A. Problem Formulation' as "
        "'###'. Equation (1) and all inline math transcribed to LaTeX from the render (no TeX source available): \\bar{w}, \\bar{\\mathcal{W}}, "
        "\\bar{N}, \\mathbb{R}^{n_u}, sans-serif transpose written \\mathsf{T}, W ~ \\mathcal{Q}. The last sentence ('The system is subject "
        "to') continues on PDF page 3."
    )
    save(2, items, notes)


# --------------------------------------------------------------------------- page 3
def page3():
    items = [
        T(
            "p0003-b000",
            [48.0, 57.0, 301.0, 79.0],
            r"a collection of $n_c$ chance constraints on the states and hard constraints on the inputs",
            join_previous="space",
        ),
        T(
            "p0003-b001",
            [78.0, 81.0, 306.0, 118.0],
            r"$$\Pr(x(k) \in \mathcal{X}^j \mid x(0)) \ge p_j\,,\ \ j \in \{1, \ldots n_c\}, \tag{2a}$$" "\n\n" r"$$u(k) \in \mathcal{U}, \tag{2b}$$",
        ),
        T(
            "p0003-b003",
            [48.0, 120.0, 301.0, 179.0],
            r"where $\mathcal{X}^j \subseteq \mathbb{R}^n$ and $\mathcal{U} \subseteq \mathbb{R}^{n_u}$ and the probabilities are with respect to "
            r"a known initial state $x(0)$. We consider the objective of minimizing the expected value of a general time-varying cost function "
            r"$l_k(x(k), u(k))$ resulting in a finite-time stochastic optimal control problem.",
        ),
        T(
            "p0003-b004",
            [48.0, 183.0, 301.0, 266.0],
            r"**Remark 1.** The assumption of finite $\bar{N}$ is particularly relevant for open-loop unstable systems in the context of "
            r"constraint (2a), which cannot be satisfied under unbounded disturbances with *any* bounded control law as $\bar{N} \to \infty$ "
            r"[15]. In practice, $\mathcal{U}$ is often large w.r.t. likely disturbance realizations, and the problem is well defined with finite "
            r"$\bar{N}$ also for unstable systems.",
        ),
        T(
            "p0003-b005",
            [48.0, 271.0, 301.0, 376.0],
            r"In this paper, we present an MPC approach to approximate the solution of the optimal control problem by repeatedly solving a "
            r"simplified problem over a smaller horizon $N \ll \bar{N}$ in such a way that the closed-loop system satisfies constraints (2). To "
            r"this end, we split the system dynamics (1) into a nominal part $z(k)$ and error $e(k)$ such that $x(k) = z(k) + e(k)$. "
            r"Correspondingly, the input is divided into a nominal input $v(k)$ and a tube controller $\pi_{\text{tube}}$ with "
            r"$u(k) = v(k) + \pi_{\text{tube}}(e(k))$, resulting in the decoupled dynamics",
        ),
        T(
            "p0003-b006",
            [85.0, 379.0, 306.0, 415.0],
            r"$$z(k+1) = Az(k) + Bv(k) + \bar{w}(k), \tag{3a}$$" "\n\n" r"$$e(k+1) = Ae(k) + B\pi_{\text{tube}}(e(k)) + w(k) \tag{3b}$$",
        ),
        T(
            "p0003-b008",
            [48.0, 418.0, 301.0, 500.0],
            r"with initial condition $z(0) = x(0)$, $e(0) = 0$. Differently to many other tube-based methods, we formulate the MPC problem such "
            r"that (3) remains valid also in closed-loop under the MPC control law, as detailed in Section III. For constraint tightening, we "
            r"therefore make use of the concept of probabilistic reachable sets (PRS) for the error system (3b), as outlined in the following.",
        ),
        H("p0003-b009", [48.0, 518.0, 180.0, 526.0], "### B. Probabilistic Reachable Sets"),
        T("p0003-b010", [58.0, 533.0, 258.0, 543.0], "We recall the definitions of PRS as given in [7]."),
        T(
            "p0003-b011",
            [48.0, 549.0, 301.0, 585.0],
            r"**Definition 1 ($k$-step PRS).** A set $\mathcal{R}_k$ with $0 \le k \le \bar{N}$ is a $k$-step probabilistic reachable set "
            r"($k$-step PRS) of probability level $p$ for system (3b) initialized at $e(0)$ if",
        ),
        T("p0003-b012", [116.0, 588.0, 233.0, 609.0], r"$$\Pr(e(k) \in \mathcal{R}_k \mid e(0)) \ge p.$$"),
        T(
            "p0003-b013",
            [48.0, 612.0, 301.0, 644.0],
            r"**Definition 2 (PRS).** A set $\mathcal{R}$ is a probabilistic reachable set (PRS) of probability level $p$ for system (3b) "
            r"initialized at $e(0)$ if",
        ),
        T(
            "p0003-b014",
            [88.0, 642.0, 261.0, 663.0],
            r"$$\Pr(e(k) \in \mathcal{R} \mid e(0)) \ge p \quad \forall\, 0 \le k \le \bar{N}.$$",
        ),
        T(
            "p0003-b015",
            [48.0, 667.0, 301.0, 749.0],
            r"Note that the probability bound in the definition of a PRS holds at all time steps individually, i.e. it guarantees $e(k)$ to lie "
            r"in $\mathcal{R}$ with probability $p$ at each time step $k$, but makes no statement about the probability of being contained in "
            r"$\mathcal{R}$ for all time steps jointly, which would require much more restrictive sets. Assuming knowledge of the distribution of "
            r"the disturbance sequence $W$, or at least the first two moments, techniques for analytically computing PRS for (3b) have been "
            r"presented in [6], [7]. In this paper, we instead compute PRS relying on samples of $W$ and simulation of the error system (see "
            r"Section IV), by making use of results from scenario optimization, which are outlined in the following section.",
        ),
        H("p0003-b017", [311.0, 130.0, 418.0, 140.0], "### C. Scenario Optimization"),
        T(
            "p0003-b018",
            [311.0, 145.0, 564.0, 167.0],
            "Scenario optimization [8], [9] considers chance constrained optimization problems of the form",
        ),
        T(
            "p0003-b019",
            [375.0, 168.0, 569.0, 211.0],
            r"$$\min_{x \in \mathcal{X} \subseteq \mathbb{R}^d} \quad c^{\mathsf{T}} x \tag{4a}$$" "\n\n" r"$$\text{s.t.} \quad \Pr(x \in \mathcal{X}_\delta) \ge p, \tag{4b}$$",
        ),
        T(
            "p0003-b021",
            [311.0, 214.0, 564.0, 283.0],
            r"where $\mathcal{X}_\delta$ are convex and closed sets for each realization of a random variable $\delta$, and $d$ is the dimension "
            r"of the decision variable $x$. Problem (4) is approximated by considering $N_s$ samples of the random variable $\delta$, and "
            r"enforcing the constraint for a selection of these samples $i \in \mathcal{I}_s$. The sampled optimization problem results in",
        ),
        T(
            "p0003-b022",
            [375.0, 284.0, 569.0, 327.0],
            r"$$\min_{x \in \mathcal{X} \subseteq \mathbb{R}^d} \quad c^{\mathsf{T}} x \tag{5a}$$" "\n\n" r"$$\text{s.t.} \quad x \in \mathcal{X}_{\delta^{(i)}},\ i \in \mathcal{I}_s, \tag{5b}$$",
        ),
        T(
            "p0003-b024",
            [311.0, 329.0, 564.0, 365.0],
            r"in which $\delta^{(i)}$ denotes a sample of $\delta$, and the considered subset of samples has cardinality "
            r"$|\mathcal{I}_s| = N_s - N_k$, which is found by discarding $N_k$ samples from the original set.",
        ),
        T(
            "p0003-b025",
            [311.0, 372.0, 564.0, 407.0],
            r"**Assumption 1 ([9]).** Constraints are discarded such that the optimal solution $x^*$ of (5) violates all the discarded "
            r"constraints $\mathcal{X}_{\delta^{(j)}}$ with $j \in \{1, \ldots, N_s\} \setminus \mathcal{I}_s$.",
        ),
        T(
            "p0003-b026",
            [311.0, 414.0, 564.0, 508.0],
            "This technical assumption is required to make use of established results from scenario optimization and can in general be "
            "satisfied, e.g. by successive optimization while greedily removing samples [9]. By discarding samples it is therefore possible to "
            "improve the objective function in (5), while maintaining probabilistic guarantees of the solution with regard to the chance "
            "constraint optimization problem (4), which is formalized in the following theorem.",
        ),
        T("p0003-b027", [311.0, 515.0, 481.0, 525.0], r"**Theorem 1 ([9]).** Let $N_s$ and $N_k$ satisfy"),
        T(
            "p0003-b028",
            [324.0, 526.0, 569.0, 567.0],
            r"$$\binom{N_k + d - 1}{N_k} \sum_{i=0}^{N_k + d - 1} \binom{N_s}{i} (1 - p)^i p^{N_s - i} \le \beta. \tag{6}$$",
        ),
        T(
            "p0003-b029",
            [311.0, 568.0, 564.0, 590.0],
            r"The optimal solution $x^*$ of (5) is a feasible solution for optimization problem (4) with probability $1 - \beta$.",
        ),
        T(
            "p0003-b030",
            [311.0, 597.0, 564.0, 631.0],
            "The bound in Theorem 1 is often unwieldy for practical computations and can be approximated. For instance, a sufficient condition "
            "for (6) is given by",
        ),
        T(
            "p0003-b031",
            [306.0, 632.0, 569.0, 681.0],
            r"$$N_k \le (1-p) N_s - d + 1 - \sqrt{2 (1-p) N_s \ln\left( \frac{((1-p) N_s)^{d-1}}{\beta} \right)} \tag{7}$$",
        ),
        T(
            "p0003-b032",
            [311.0, 679.0, 564.0, 724.0],
            r"and provides a practical way of assessing how many samples $N_k$ to discard while providing guarantees with respect to $p$ and "
            r"$\beta$ given a number of sampled scenarios $N_s$ (see [9]. Without removing constraint samples, i.e. for $N_k = 0$, one can obtain",
        ),
        T(
            "p0003-b033",
            [356.0, 724.0, 569.0, 757.0],
            r"$$N_s \ge \frac{2}{1-p} \left( (d-1) \ln(2) - \ln(\beta) \right), \tag{8}$$",
        ),
    ]
    notes = (
        "Compared with 200 dpi page render and 300 dpi column crops (all sub/superscripts legible). All 13 extractor 'formula' image items "
        "replaced by LaTeX text items: (2a)/(2b), (3a)/(3b), the two unnumbered displays in Definitions 1 and 2, (4a)/(4b), (5a)/(5b), (6), "
        "(7), (8); each printed equation number has its own $$ block with \\tag, and the lines of one multi-line display stay together in one item. Inline math rewritten from glyph soup to "
        "LaTeX (\\mathcal{X}^j, \\mathcal{U}, \\mathbb{R}^{n_u}, \\pi_{\\text{tube}}, \\mathcal{R}_k, \\mathcal{X}_\\delta, \\mathcal{I}_s, "
        "\\delta^{(i)}, x^*, \\bar{N}). Reading order: left column then right column; the paragraph 'Note that the probability bound ...' is "
        "split by the column break after 'the first two moments,' and was merged with its right-column continuation (former item p0003-b016). "
        "First item continues the last sentence of PDF page 2 (join_previous=space). Extractor errors fixed: subsection titles 'B. "
        "Probabilistic Reachable Sets' and 'C. Scenario Optimization' were '#' headings (now '###'); the sentence 'We recall the definitions "
        "of PRS as given in [7].' was wrongly a heading (now text). Theorem-like labels set in bold as first words: Remark 1 (printed italic), "
        "Definition 1 (k-step PRS), Definition 2 (PRS), Assumption 1 ([9]), Theorem 1 ([9]); the statement of Theorem 1 is printed in italics "
        "and consists of the items 'Let N_s and N_k satisfy', display (6), and 'The optimal solution x^* of (5) is a feasible solution for "
        "optimization problem (4) with probability 1 - beta.' (italic markers not reproduced). Printed peculiarities kept verbatim: in (2a) "
        "the index set is printed '{1, . . . n_c}' without a comma after the dots; before (8) the parenthesis in '(see [9].' is never closed; "
        "(3b) and (7) have no terminal punctuation. Line-wrap hyphens repaired: 'time-varying' (real compound), 'relevant', 'constraint', "
        "'disturbances', 'probabilistic', 'optimization', 'sufficient'. Sentence continues after (8) on PDF page 4."
    )
    save(3, items, notes)


# --------------------------------------------------------------------------- page 4
def page4():
    items = [
        T(
            "p0004-b000",
            [48.0, 57.0, 301.0, 79.0],
            r"to estimate the required number of samples to guarantee probability level $p$ with probability $1 - \beta$ (see [8]).",
        ),
        H("p0004-b001", [75.0, 97.0, 274.0, 117.0], "## III. Stochastic MPC using Probabilistic Reachable Sets"),
        T(
            "p0004-b002",
            [48.0, 126.0, 301.0, 208.0],
            r"In the following, we recount a recursively feasible stochastic MPC approach recently proposed in [7] and show how it can be "
            r"modified to be wholly reliant on samples, before discussing the scenario-based computation of PRS in Section IV. In order to "
            r"differentiate quantities in prediction from the closed-loop system (1), we make use of the index $i$ for an $i$-step ahead "
            r"prediction. The predictive dynamics are",
        ),
        T(
            "p0004-b003",
            [105.0, 213.0, 306.0, 264.0],
            r"$$x_{i+1} = A x_i + B u_i + \bar{w}_i + w_i, \tag{9a}$$" "\n\n" r"$$z_{i+1} = A z_i + B v_i + \bar{w}_i, \tag{9b}$$" "\n\n" r"$$e_{i+1} = A e_i + B \pi_{\text{tube}}(e_i) + w_i, \tag{9c}$$",
        ),
        T(
            "p0004-b006",
            [48.0, 269.0, 301.0, 437.0],
            r"which are initialized at every time step at the currently measured state $x_0 = x(k)$, $z_0 = z(k)$, $e_0 = e(k)$, and the known "
            r"disturbance part is $\bar{w}_i = \bar{w}(k+i)$. The *predictive* disturbance sequence $W_k$, i.e. $w_i$ and resulting *predictive* "
            r"error $e_i$ are exclusively used to optimize the MPC cost, making use of all information about the disturbance sequence available "
            r"at that time. The sequence $W_k = [w_0, \ldots, w_N]$ is therefore obtained by conditioning $W$ on all past disturbances, such that "
            r"$p(W_k) = p\Big( [w(k)^{\mathsf{T}}, \ldots, w(k+N)^{\mathsf{T}}]^{\mathsf{T}} \,\Big|\, [w(0)^{\mathsf{T}}, \ldots, w(k-1)^{\mathsf{T}}]^{\mathsf{T}} \Big)$, "
            r"where we assume for notational convenience that the distributions allow a density, as well as access to samples of $W_k$. "
            r"Closed-loop constraint satisfaction, on the other hand, is established with regard to the *closed-loop* error $e(k)$ and "
            r"disturbance sequence $W$.",
        ),
        H("p0004-b007", [48.0, 458.0, 152.0, 468.0], "### A. Constraint Tightening"),
        T(
            "p0004-b008",
            [48.0, 474.0, 301.0, 520.0],
            r"In order to guarantee satisfaction of constraints (2) on state $x$ and input $u$ we consider tightened constraints on the nominal "
            r"state $z$ and input $v$. Hard input constraints are realized by imposing a limited control authority on $\pi_{\text{tube}}$.",
        ),
        T(
            "p0004-b009",
            [48.0, 528.0, 267.0, 538.0],
            r"**Assumption 2.** The tube controller $\pi_{\text{tube}}$ is such that",
        ),
        T(
            "p0004-b010",
            [110.0, 543.0, 239.0, 564.0],
            r"$$\pi_{\text{tube}}(e) \in \mathcal{E}_u \subset \mathcal{U}\,,\ \forall e \in \mathbb{R}^n.$$",
        ),
        T(
            "p0004-b011",
            [48.0, 569.0, 301.0, 651.0],
            r"This can be ensured by designing $\pi_{\text{tube}}$ e.g. as an input constrained (explicit) MPC, or a saturated linear controller "
            r"[16]. Each chance constraint $j$ in (2a) is treated based on the idea of keeping the error $e(k)$ within a respective time-varying "
            r"PRS $\mathcal{R}^j_k$, the scenario-based computation of which we discuss in Section IV. This results in the following tightened "
            r"constraints on the nominal system (9b)",
        ),
        T(
            "p0004-b012",
            [108.0, 654.0, 306.0, 708.0],
            r"$$z_i \in \mathcal{Z}_i = \bigcap_{j=1}^{n_c} \left( \mathcal{X}^j \ominus \mathcal{R}^j_{k+i} \right), \tag{10a}$$" "\n\n" r"$$v_i \in \mathcal{V} = \mathcal{U} \ominus \mathcal{E}_u. \tag{10b}$$",
        ),
        T(
            "p0004-b014",
            [48.0, 712.0, 301.0, 749.0],
            r"**Assumption 3.** The tightening set $\mathcal{R}^j_{k+i}$ in (10a) is chosen as a $k+i$-step PRS of probability $p_j$ for system "
            r"(3b) initialized at $e(0) = 0$.",
        ),
        H("p0004-b015", [311.0, 57.0, 488.0, 65.0], "### B. Stochastic MPC with Indirect Feedback"),
        T(
            "p0004-b016",
            [311.0, 73.0, 564.0, 107.0],
            r"In the MPC problem, we introduce a terminal constraint $\mathcal{Z}_f$ and terminal cost $l_f$ to approximate the remainder of the "
            r"horizon, resulting in the cost function",
        ),
        T(
            "p0004-b017",
            [358.0, 110.0, 517.0, 151.0],
            r"$$\mathbb{E}_{W_k} \left( l_f(x_N) + \sum_{i=0}^{N-1} l_{k+i}(x_i, u_i) \right).$$",
        ),
        T(
            "p0004-b018",
            [311.0, 153.0, 564.0, 187.0],
            r"We follow a sampling-based approach to approximate this cost based on $N_s^{\text{MPC}}$ samples of the predicted disturbance "
            r"sequence $W_k$ and formulate the MPC problem as",
        ),
        T(
            "p0004-b019",
            [329.0, 189.0, 569.0, 330.0],
            r"$$\min_{\{v_i\}} \quad \sum_{l=1}^{N_s^{\text{MPC}}} \left( l_f(x_N^{(l)}) + \sum_{i=0}^{N-1} l_{k+i}(x_i^{(l)}, u_i^{(l)}) \right) \tag{11a}$$" "\n\n" r"$$\text{s.t.} \quad x_{i+1}^{(l)} = z_{i+1} + e_{i+1}^{(l)} \tag{11b}$$" "\n\n" r"$$u_i^{(l)} = v_i + \pi_{\text{tube}}(e_i^{(l)}) \tag{11c}$$" "\n\n" r"$$e_{i+1}^{(l)} = A e_i^{(l)} + B \pi_{\text{tube}}(e_i^{(l)}) + w_i^{(l)} \tag{11d}$$" "\n\n" r"$$z_{i+1} = A z_i + B v_i + \bar{w}_i \tag{11e}$$" "\n\n" r"$$v_i \in \mathcal{V},\ z_i \in \mathcal{Z}_i,\ z_N \in \mathcal{Z}_f \tag{11f}$$" "\n\n" r"$$z_0 = z(k),\ x_0^{(l)} = x(k),\ e_0^{(l)} = e(k), \tag{11g}$$",
        ),
        T(
            "p0004-b023",
            [311.0, 333.0, 564.0, 394.0],
            r"for all $i \in \{0, \ldots, N-1\}$. Note that $e_i^{(l)}$, $\pi_{\text{tube}}(e_i^{(l)})$ are not affected by the decision "
            r"variables $\{v_i\}$ and can therefore be precomputed. The resulting control input applied to system (1) is obtained by setting "
            r"$v(k) = v_0^*$, where $v_0^*$ is the first element of the minimizer in (11), i.e.",
        ),
        T(
            "p0004-b024",
            [382.0, 399.0, 569.0, 420.0],
            r"$$u(k) = v_0^* + \pi_{\text{tube}}(e(k)). \tag{12}$$",
        ),
        T(
            "p0004-b025",
            [311.0, 424.0, 564.0, 470.0],
            r"**Remark 2.** Since $z_0 = z(k)$ at each time-step, the closed-loop error $e(k)$ evolves autonomously according to (3b). Feedback "
            r"from $x(k)$ on the nominal trajectory $z(k)$ is nevertheless introduced through the cost in (11), see also [7].",
        ),
        H("p0004-b026", [311.0, 490.0, 526.0, 500.0], "### C. Recursive Feasibility and Constraint Satisfaction"),
        T(
            "p0004-b027",
            [311.0, 506.0, 564.0, 538.0],
            r"In order to ensure recursive feasibility, we require an invariance assumption on the terminal set $\mathcal{Z}_f$, taking into "
            r"account the known disturbance $\bar{w} \in \bar{\mathcal{W}}$.",
        ),
        T(
            "p0004-b028",
            [311.0, 548.0, 564.0, 583.0],
            r"**Assumption 4.** The terminal set $\mathcal{Z}_f$ is robust invariant with respect to $\bar{w} \in \bar{\mathcal{W}}$ under the "
            r"local controller $\pi_f(z) \in \mathcal{V}\ \forall z \in \mathcal{Z}_f$, i.e.",
        ),
        T(
            "p0004-b029",
            [340.0, 584.0, 540.0, 602.0],
            r"$$z \in \mathcal{Z}_f \Rightarrow Az + B\pi_f(z) + \bar{w} \in \mathcal{Z}_f$$",
        ),
        T(
            "p0004-b029b",
            [311.0, 604.0, 564.0, 622.0],
            r"and $\mathcal{Z}_f \subseteq \mathcal{Z}_\infty$, where $\mathcal{Z}_\infty = \bigcap_{k=1}^{\bar{N}} \mathcal{Z}_k$.",
        ),
        T(
            "p0004-b030",
            [311.0, 623.0, 564.0, 718.0],
            r"**Remark 3.** For the choice of $\bar{\mathcal{W}} = \{0\}$ and time-invariant $\mathcal{R}_k = \mathcal{R}$, for "
            r"$0 \le k \le \bar{N}$, Assumption 4 requires a nominal invariant set within the tightened constraints, which is a standard "
            r"assumption in robust tube MPC. Here we allow more flexibility to deal with correlated time-varying disturbances, requiring that in "
            r"the terminal set a control input exists which keeps the nominal state within *every* tightened constraint set $\mathcal{Z}_k$ from "
            r"$k = 0, \ldots, \bar{N}$.",
        ),
        T(
            "p0004-b031",
            [311.0, 727.0, 564.0, 748.0],
            "**Theorem 2.** Consider system (1) under control law (12) resulting from (11) satisfying Assumptions 2 & 4. If optimization",
        ),
    ]
    notes = (
        "Compared with 200 dpi page render and 300 dpi column crops. All 13 extractor 'formula' image items replaced by LaTeX text items: "
        "(9a)-(9c), the unnumbered display of Assumption 2, (10a)/(10b), the unnumbered expected-cost display, the MPC problem (11a)-(11g) as "
        "one item with seven $$ blocks carrying the printed tags, (12), and the unnumbered invariance implication of Assumption 4. The extractor had "
        "fused the implication display and the following text line 'and Z_f ⊆ Z_∞, where Z_∞ = ∩_{k=1}^{N̄} Z_k.' into one formula image; "
        "they are now two items (p0004-b029, p0004-b029b). Heavily damaged inline math rebuilt from the render, in particular the conditional "
        "density p(W_k) = p([w(k)^T,...,w(k+N)^T]^T | [w(0)^T,...,w(k-1)^T]^T) (extractor had scattered the big delimiters and replacement "
        "characters), R^j_k / R^j_{k+i} (extractor had glued the following words into a <sup> tag), e_i^{(l)}, v_0^*, N_s^{MPC}, "
        "\\bar{\\mathcal{W}}. The first item finishes the sentence that runs through display (8) on PDF page 3; it follows a display "
        "equation, so no join_previous is set. Headings: 'III. Stochastic MPC using Probabilistic Reachable Sets' (two printed lines, small "
        "caps) as '##'; subsections A, B, C as '###' (extractor had '#'). Theorem-like labels in bold: Assumption 2, Assumption 3, Remark 2 "
        "(printed italic), Assumption 4, Remark 3 (printed italic), Theorem 2 (statement printed in italics; italic markers not reproduced; "
        "it continues on PDF page 5). Printed details kept: (11b)-(11f) carry no punctuation, (11g) ends with a comma; Remark 3 prints "
        "'R_k = R, for 0 ≤ k ≤ N̄'; Z_∞ is an intersection from k=1 while Remark 3 says 'from k = 0, ..., N̄' (as printed). Line-wrap "
        "hyphens repaired: 'measured', 'Closed-loop' (real compound), 'constrained', 'invariance', 'resulting'."
    )
    save(4, items, notes)


# --------------------------------------------------------------------------- page 5
def page5():
    items = [
        T(
            "p0005-b000",
            [48.0, 56.0, 301.0, 79.0],
            r"problem (11) is feasible for $x(0) = z(0)$, then it is feasible for all times $0 \le k \le \bar{N} - N$, i.e. it is recursively "
            r"feasible.",
            join_previous="space",
        ),
        T(
            "p0005-b001",
            [48.0, 87.0, 301.0, 253.0],
            r"**Proof.** The proof follows from standard arguments in MPC by showing feasibility of a candidate solution. Let "
            r"$V^* = \{v_0^*, \ldots v_{N-1}^*\}$ be the minimizer of (11) at time step $k$ with resulting $Z^* = \{z_0^*, \ldots, z_N^*\}$. "
            r"Applying control input (12) results in state $x(k+1)$ and $z(k+1) = z_1^*$, for which we consider the candidate solution "
            r"$\bar{V} = \{v_1^*, \ldots, v_{N-1}^*, \pi_f(z_N^*)\}$ resulting in "
            r"$\bar{Z} = \{z_1^*, \ldots, z_N^*, A z_N^* + B\pi_f(z_N^*) + \bar{w}(k+N+1)\}$. Since $v_i^* \in \mathcal{V}$ for all "
            r"$1 \le i \le N$ and $\pi_f(z_N^*) \in \mathcal{V}$ we have that $\bar{V}$ satisfies input constraints (11f). Similarly, we have "
            r"that $z_i^* \in \mathcal{Z}_i(k) = \mathcal{Z}_{i-1}(k+1)$ defined in (10a) for all $1 \le i \le N$, where we use notation "
            r"$\mathcal{Z}_i(k)$ to indicate the state constraint at $i$-th prediction step for optimization problem (11) at time step $k$. We "
            r"finally have $A z_N^* + B\pi_f(z_N^*) + \bar{w}(k+N+1) \in \mathcal{Z}_f$ due to Assumption 4. $\square$",
        ),
        T(
            "p0005-b002",
            [48.0, 264.0, 301.0, 310.0],
            "Recursive feasibility and Definition 1 of the PRS used in constraint tightening (10a) can directly be used to establish "
            "satisfaction of hard constraints on the inputs (2b) and chance constraints on the state (2a) for the closed-loop system.",
        ),
        T(
            "p0005-b003",
            [48.0, 318.0, 301.0, 364.0],
            r"**Theorem 3.** Consider system (1) under control law (12) resulting from (11) satisfying Assumptions 2, 3 & 4. The resulting state "
            r"$x(k)$ and input $u(k)$ satisfy constraints (2a) and (2b), respectively.",
        ),
        T(
            "p0005-b004",
            [48.0, 373.0, 301.0, 471.0],
            r"**Proof.** From recursive feasibility, control law (12) and definition of the input constraint tightening (10b) we immediately "
            r"have $u(k) \in \mathcal{U}$, since $\pi_{\text{tube}}(e) \in \mathcal{E}_u$ for all $e \in \mathbb{R}^n$ from Assumption 2. From "
            r"Assumption 3 we furthermore have that $\Pr(e(k) \in \mathcal{R}^j_k) \ge p_j$. Given that $z(k) \in \mathcal{Z}_0(k)$ due to "
            r"recursive feasibility and $\mathcal{Z}_0(k) = \bigcap_{j=1}^{n_c} \left( \mathcal{X}^j \ominus \mathcal{R}^j_k \right)$ according "
            r"to (10a), we therefore have $\Pr(x(k) \in \mathcal{X}^j) \ge p_j$ for all $j = 1, \ldots, n_c$. $\square$",
        ),
        H("p0005-b005", [54.0, 491.0, 295.0, 511.0], "## IV. Probabilistic Reachable Sets using Scenario Optimization"),
        T(
            "p0005-b006",
            [48.0, 521.0, 301.0, 607.0],
            r"In the following, we describe a sampling-based design procedure for $k$-step PRS computation. The inputs to this procedure are a "
            r"number of disturbance scenarios over the run-time sampled from $W$, i.e. "
            r"$W^{(i)} = [w_0^{(i)}, \ldots, w_{\bar{N}-1}^{(i)}]^{\mathsf{T}} \sim \mathcal{W}$, $i \in \{1, \ldots, N_s\}$, resulting in "
            r"trajectories of the error system (3b) $E^{(i)} = [e_0^{(i)}, \ldots, e_{\bar{N}}^{(i)}]^{\mathsf{T}}$, initialized at "
            r"$e_0^{(i)} = e(0) = 0$.",
        ),
        T(
            "p0005-b006b",
            [48.0, 608.0, 301.0, 749.0],
            r"The general idea is to generate sets that cover given error state realizations, i.e. $e_k^{(i)} \in \mathcal{R}_k$, "
            r"$i \in \mathcal{I}_s$ and apply the result of Theorem 1 to establish that $\mathcal{R}_k$ is a $k$-step PRS with high probability. "
            r"For this, we formulate chance constraint optimization problems similar to (4) to find sets $\mathcal{R}_k$, which are used to "
            r"tighten constraints (10a). In general, it is desirable to generate sets $\mathcal{R}_k$ which result in the smallest possible "
            r"tightening, for instance by aligning the PRS with the considered constraint $\mathcal{X}^j$, e.g. for half-spaces or simple "
            r"polytopic constraints. For general constraint sets, a useful heuristic is to minimize the size of $\mathcal{R}_k$, e.g. by finding "
            r"the minimum volume ellipsoid covering the required number of samples. We discuss selected options in the following sections.",
        ),
        T(
            "p0005-b007",
            [311.0, 57.0, 564.0, 115.0],
            r"**Remark 4.** Scenario-based guarantees along Theorem 1 are given with confidence $1 - \beta$. For the MPC, this implies that "
            r"Assumption 3 and the resulting closed-loop constraint satisfaction property (Theorem 3) hold with probability $1 - \beta$ when "
            r"using a scenario-based construction of the PRS.",
        ),
        H("p0005-b008", [311.0, 134.0, 416.0, 144.0], "### A. Scaling of Convex Set"),
        T(
            "p0005-b009",
            [311.0, 149.0, 564.0, 207.0],
            r"We first consider the scaling of an arbitrary closed convex set $\tilde{\mathcal{R}}$ containing the origin such that "
            r"$\mathcal{R} = \alpha\tilde{\mathcal{R}}$ is a $k$-step PRS for random variable $e(k)$ with given probability $p$. This can be "
            r"stated as the following chance constrained optimization problem:",
        ),
        T(
            "p0005-b010",
            [375.0, 212.0, 500.0, 252.0],
            r"$$\begin{aligned} \min_{\alpha > 0} \quad & \alpha \\ \text{s.t.} \quad & \Pr(e(k) \in \alpha\tilde{\mathcal{R}}) \ge p. \end{aligned}$$",
        ),
        T(
            "p0005-b012",
            [311.0, 256.0, 564.0, 302.0],
            r"The relation to (4) is obtained by noting that $\alpha$ corresponds to $x$ and "
            r"$\mathcal{X}_\delta := \{\alpha \mid e(k) \in \alpha\tilde{\mathcal{R}}\}$. This set is convex in $\alpha$ and closed for each "
            r"realization of $e(k)$ since $\tilde{\mathcal{R}}$ is convex and closed. The sampled version is",
        ),
        T(
            "p0005-b013",
            [381.0, 306.0, 569.0, 348.0],
            r"$$\min_{\alpha > 0} \quad \alpha \tag{13a}$$" "\n\n" r"$$\text{s.t.} \quad e_k^{(i)} \in \alpha\tilde{\mathcal{R}}\,,\ i \in \mathcal{I}_s, \tag{13b}$$",
        ),
        T(
            "p0005-b015",
            [311.0, 350.0, 564.0, 447.0],
            r"where $e_k^{(i)}$ stem from the $N_s$ sampled realizations of the random disturbance sequence $W$. From this set of samples, $N_k$ "
            r"scenarios are discarded resulting in the index set $\mathcal{I}_s$. Note that in this case the index set $\mathcal{I}_s$ "
            r"satisfying Assumption (1) can be obtained by repeatedly solving (13) starting with all samples and successively removing samples "
            r"corresponding to active constraints. The PRS property of the resulting set is directly obtained from Theorem 1.",
        ),
        T(
            "p0005-b016",
            [311.0, 455.0, 564.0, 501.0],
            r"**Corollary 1.** Let $\alpha^*$ be the solution to optimization problem (13) and let $N_s$, $N_k$ satisfy (6) with $d = 1$. With "
            r"probability $1 - \beta$ the set $\alpha^*\tilde{\mathcal{R}}$ is a $k$-step PRS of probability $p$ for process (3b) initialized at "
            r"$e(0) = 0$.",
        ),
        T(
            "p0005-b017",
            [311.0, 509.0, 564.0, 559.0],
            r"**Remark 5 (Half-space PRS).** An important special case is given by a half-space "
            r"$\tilde{\mathcal{R}} = \{ e \mid h^{\mathsf{T}} e \le 1 \}$. We can discard the $k$ samples of $e_k^{(i)}$ with highest value "
            r"$h^{\mathsf{T}} e_k^{(i)}$ and then find $\alpha^* = \max_{i \in \mathcal{I}_s} h^{\mathsf{T}} e_k^{(i)}$.",
        ),
        H("p0005-b018", [311.0, 577.0, 384.0, 587.0], "### B. Polytopic PRS"),
        T(
            "p0005-b019",
            [311.0, 593.0, 564.0, 651.0],
            r"Next we address the case of polytopic PRS containing the origin, with a predefined shape "
            r"$\tilde{\mathcal{R}} = \{ e \mid He \le \mathbf{1} \}$ in which $H \in \mathbb{R}^{n_{hs} \times n}$ and "
            r"$\mathbf{1} \in \mathbb{R}^{n_{hs}}$ is the one-vector. The goal is to optimize the level of each half-space constraint, which is "
            r"formulated as the scenario problem",
        ),
        T(
            "p0005-b020",
            [381.0, 654.0, 569.0, 697.0],
            r"$$\min_{b > 0} \quad \|b\|_1 \tag{14a}$$" "\n\n" r"$$\text{s.t.} \quad H e_k^{(i)} \le b,\ i \in \mathcal{I}_s. \tag{14b}$$",
        ),
        T(
            "p0005-b022",
            [311.0, 701.0, 564.0, 749.0],
            r"Similar to half-space constraints (Remark 5) constraint removal can easily be carried out greedily by successively removing $N_k$ "
            r"samples of $e_k^{(i)}$ with the largest violation $\|H e_k^{(i)}\|_\infty$. Note that through the choice of matrix $H$ an",
        ),
    ]
    notes = (
        "Compared with 200 dpi page render and 300 dpi column crops. First item finishes the statement of Theorem 2 begun on PDF page 4 "
        "(join_previous=space). All 6 extractor 'formula' image items replaced by LaTeX text items: the unnumbered chance-constrained scaling "
        "problem (min over alpha>0, two lines, as one aligned block), (13a)/(13b), (14a)/(14b). Both proofs were almost unreadable in the "
        "extraction (sub/superscripts and following words fused into <sup> tags, big delimiters as replacement characters) and were rebuilt "
        "from the render: V^*, Z^*, candidate \\bar{V}, \\bar{Z}, Z_i(k) = Z_{i-1}(k+1), the intersection Z_0(k) = ∩_{j=1}^{n_c}(X^j ⊖ R^j_k); "
        "the printed end-of-proof boxes are written $\\square$. The opening paragraph of Section IV was split at the printed paragraph break "
        "before 'The general idea is ...' (two items, p0005-b006 and p0005-b006b); the extractor's stray '¯' fragments belonged to the "
        "subscripts \\bar{N}-1 and \\bar{N} of W^{(i)} and E^{(i)}. Headings: 'IV. Probabilistic Reachable Sets using Scenario Optimization' "
        "(two printed lines) as '##', 'A. Scaling of Convex Set' and 'B. Polytopic PRS' as '###'. Labels in bold: Proof (twice, printed "
        "italic), Theorem 3, Remark 4, Corollary 1, Remark 5 (Half-space PRS); theorem/corollary statements are printed in italics (italic "
        "markers not reproduced). Printed peculiarities kept verbatim: 'V^* = {v_0^*, . . . v_{N-1}^*}' without a comma after the dots; "
        "'v_i^* ∈ V for all 1 ≤ i ≤ N' in the proof of Theorem 2; the sampled sequences are written W^{(i)} ~ calligraphic W here although "
        "Section II wrote W ~ calligraphic Q; W^{(i)} runs to index N̄-1 while E^{(i)} runs to N̄; 'Assumption (1)' with parentheses; Remark 5 "
        "says 'discard the k samples' (k, not N_k). Line-wrap hyphens repaired: 'run-time' (real compound, also printed unbroken on PDF page "
        "6), 'definition', 'recursive', 'system', 'optimization', 'problem', 'removal'. Last sentence continues on PDF page 6."
    )
    save(5, items, notes)


# --------------------------------------------------------------------------- page 6
def page6():
    items = [
        T(
            "p0006-b002",
            [48.0, 191.0, 301.0, 212.0],
            "importance weighting can be carried out for each individual half space defining the polytope.",
            join_previous="space",
        ),
        T(
            "p0006-b003",
            [48.0, 220.0, 301.0, 267.0],
            r"**Corollary 2.** Let $b^*$ be the solution to optimization problem (14) and let $N_s$, $N_k$ satisfy (6) with $d = n_{hs}$. With "
            r"probability $1 - \beta$ the set $\{ e \mid He \le b^* \}$ is a $k$-step PRS of probability $p$ for process (3b) initialized at "
            r"$e(0) = 0$.",
        ),
        H("p0006-b013", [48.0, 283.0, 128.0, 293.0], "### C. Ellipsoidal PRS"),
        T(
            "p0006-b014",
            [48.0, 298.0, 301.0, 332.0],
            r"As a third possibility consider the minimum volume ellipsoidal set covering the error $e(k)$ with specified probability $p$. The "
            r"sampled version can be expressed as",
        ),
        T(
            "p0006-b015",
            [65.0, 336.0, 306.0, 379.0],
            r"$$\min_{P > 0,\, e_c} \quad -\log\det P \tag{15a}$$" "\n\n" r"$$\text{s.t.} \quad (e_k^{(i)} - e_c)^{\mathsf{T}} P (e_k^{(i)} - e_c) \le 1\,,\ i \in \mathcal{I}_s, \tag{15b}$$",
        ),
        T(
            "p0006-b017",
            [48.0, 380.0, 301.0, 453.0],
            r"where $d = \frac{n^2+n}{2} + n$ is given by the number of unique entries in the symmetric shape matrix $P$ and vector $e_c$. "
            r"Ensuring Assumption 1 in the construction of $\mathcal{I}_s$ is again possible by sequential removal of active constraint samples. "
            r"Additional information on suitable constraint removal strategies can be found in [9].",
        ),
        T(
            "p0006-b018",
            [48.0, 461.0, 301.0, 520.0],
            r"**Corollary 3.** Let $P^*$, $e_c^*$ be the solution to optimization problem (15) and let $N_s$, $N_k$ satisfy (6) with "
            r"$d = \frac{n^2+n}{2} + n$. With probability $1 - \beta$ the set "
            r"$\{ e \mid (e - e_c^*)^{\mathsf{T}} P^{*-1} (e - e_c^*) \le 1 \}$ is a $k$-step PRS of probability $p$ for process (3b) "
            r"initialized at $e(0) = 0$.",
        ),
        T(
            "p0006-b019",
            [48.0, 528.0, 301.0, 551.0],
            r"**Remark 6.** When fixing the ellipsoid center, e.g. $e_c = 0$, Corollary 3 holds with $d = \frac{n^2+n}{2}$.",
        ),
        T(
            "p0006-b020",
            [48.0, 555.0, 301.0, 589.0],
            r"**Remark 7.** It is possible to speed up constraint removal by initializing $\mathcal{I}_{\text{dis}}$ heuristically, e.g. by "
            r"discarding samples based on the empirical variance of the sample set.",
        ),
        H("p0006-b021", [73.0, 604.0, 276.0, 612.0], "## V. Simulation Example: Overhead Crane"),
        T(
            "p0006-b022",
            [48.0, 619.0, 301.0, 749.0],
            r"As an illustrative example we consider an overhead crane maneuvering a load in windy conditions. The system is depicted in Figure "
            r"(1) with states $x = [p, v, \theta, r]^{\mathsf{T}}$, where $p$, $v$ are the position and velocity of the slider, and $\theta$, "
            r"$r$ the load angle and angular velocity, respectively. The system equations are given in the appendix. The input to the system is "
            r"a force applied to the slider $u$ and the run-time is $\bar{N} = 200$. The load is subject to a disturbance force $w$, representing "
            r"heavy winds, distributed according to $W \sim \mathcal{N}(0, \Sigma^w)$, which is zero mean and strongly correlated in time. The "
            r"system is subject to a number of physical and safety constraints. First, the input is restricted to $|u| \le u_{\max} = 4$ and we "
            r"consider the sliders position and velocity to be subject to physical limitations",
        ),
        T(
            "p0006-b005",
            [355.0, 81.0, 569.0, 103.0],
            r"$$[|p|, |v|]^{\mathsf{T}} \le [p_{\max}, v_{\max}]^{\mathsf{T}} = [1, 0.4]^{\mathsf{T}}, \tag{16}$$",
        ),
        T(
            "p0006-b006",
            [311.0, 107.0, 564.0, 141.0],
            "which we want to enforce with highest possible probability. We additionally consider chance constraints on the load angle for "
            "safety reasons",
        ),
        T(
            "p0006-b007",
            [377.0, 145.0, 569.0, 180.0],
            r"$$\Pr(\theta(k) \ge -0.08) \ge 90\%, \tag{17a}$$" "\n\n" r"$$\Pr(\theta(k) \le 0.08) \ge 90\%. \tag{17b}$$",
        ),
        T(
            "p0006-b009",
            [311.0, 184.0, 547.0, 195.0],
            r"Starting from $x(0) = 0$, the goal is to track the reference",
        ),
        T(
            "p0006-b010",
            [365.0, 196.0, 509.0, 237.0],
            r"$$x_k^{\text{ref}} = \begin{cases} [1, 0, 0, 0]^{\mathsf{T}}, & k \le 100 \\ [-1, 0, 0, 0]^{\mathsf{T}}, & k > 100 \end{cases}$$",
        ),
        T("p0006-b011", [311.0, 238.0, 493.0, 248.0], "as closely as possible, given the constraints."),
        {
            "id": "p0006-b000",
            "kind": "figure",
            "bbox": [60.0, 48.0, 294.0, 155.0],
            "markdown": "",
            "label": "Figure 1",
            "asset_name": "figure-1",
        },
        C("p0006-b001", [48.0, 160.0, 212.0, 168.0], "Fig. 1. Illustration of the overhead crane system."),
        H("p0006-b012", [311.0, 266.0, 395.0, 276.0], "### A. Simulation Setup"),
        T(
            "p0006-b023",
            [311.0, 280.0, 564.0, 471.0],
            r"Using the cost function $(x_i - x^{\text{ref}}_{k+i})^{\mathsf{T}} Q (x_i - x^{\text{ref}}_{k+i}) + u^{\mathsf{T}} R u$ with "
            r"$Q = I$, $R = 10^{-4}$, we compute the expected cost (11a) based on $N_s^{\text{MPC}} = 10$ samples and consider a prediction "
            r"horizon of $N = 30$. We design the tube controller $\pi_{\text{tube}}$ as an LQR controller with the same weights, which we "
            r"saturate at $\pm 0.4$ to enable hard input constraints. We compute suitable half-space and box constraints aligned with the "
            r"respective state constraints in order to obtain a constraint tightening with little conservatism. Using $N_s = 10000$ scenario "
            r"samples, we compute PRS $\mathcal{R}_k^{|p|,|v|}$ as minimum-size boxes containing all sampled error positions and velocities in "
            r"each time step according to Corollary 2. To enforce the constraint with maximum probability, we remove no constraint samples, and "
            r"find according to (8) that the probability of satisfying (16) in each time step is at least $p_1 = 99.6\%$ with probability "
            r"$1 - \beta \approx 1 - 10^{-7}$. For chance constraints (17) we use",
        ),
        {
            "id": "p0006-b024",
            "kind": "figure",
            "bbox": [316.0, 486.0, 562.0, 713.0],
            "markdown": "",
            "label": "Figure 2",
            "asset_name": "figure-2",
        },
        C(
            "p0006-b025",
            [311.0, 720.0, 564.0, 746.0],
            r"Fig. 2. Overhead crane system with reference $p_{ref} = 1$ for $k \le 100$ and $p_{ref} = -1$ for $k > 100$. The plot depicts 10000 "
            r"simulations, highlighting one realization. Dashed lines show chance and hard input constraints.",
        ),
    ]
    notes = (
        "Compared with 200 dpi page render, 300 dpi column crops and 500 dpi zooms of (15a)/(15b) and Corollary 3. Reading order rebuilt: the "
        "extractor had interleaved the right column ((16), (17), reference, 'A. Simulation Setup') into the left column. Order now: "
        "continuation of the sentence from PDF page 5 ('importance weighting ...', join_previous=space), Corollary 2, 'C. Ellipsoidal PRS' "
        "with (15a)/(15b), Corollary 3, Remarks 6 and 7, 'V. Simulation Example: Overhead Crane' and its text, then 'A. Simulation Setup'. The "
        "first paragraph of Section V is split by the column break after 'First, the input' and was merged with its continuation 'is "
        "restricted to |u| ≤ u_max = 4 ...' (former item p0006-b004). Figure 1 (top of the left column, where it interrupts the sentence "
        "running over from page 5) is placed with its caption at the end of the Section V introduction, before 'A. Simulation Setup'. Figure 2 "
        "(bottom of the right column) interrupts the sentence 'For chance constraints (17) we use | Corollary 1 with Remark 5 ...' that "
        "continues on PDF page 7; plan.json reading_order moves Figure 2 and its caption to after that paragraph on page 7. Figure crops "
        "checked on renders: Figure 1 includes labels u, p, θ, w, p_0, p_1; Figure 2 includes the four panels with y-labels w(k), p(k), θ(k), "
        "u(k), all tick labels and the x-label k; captions are separate items; the extractor's picture-text fragments were discarded (they "
        "are visible inside the crops). All 6 extractor 'formula' image items replaced by LaTeX text items: (15a)/(15b), (16), (17a)/(17b), the "
        "unnumbered piecewise reference x_k^{ref}. Inline math rebuilt from the render: d = (n^2+n)/2 + n (extractor had underlined "
        "fragments), R_k^{|p|,|v|}, x^{ref}_{k+i}, I_dis. Printed peculiarities kept verbatim: 'Figure (1)' with parentheses; 'the sliders "
        "position' (no apostrophe); in (15a) the constraint is printed 'P>0' with a plain greater-than sign; Corollary 3 prints the matrix as "
        "P^{*-1} (star and -1 in one superscript) although (15b) uses P; Remark 7 uses the index set I_dis, which is not defined elsewhere; "
        "the Fig. 2 caption prints p_{ref} with an italic subscript while the text uses upright 'ref' superscripts. Labels in bold: Corollary "
        "2, Corollary 3, Remark 6, Remark 7 (corollary statements printed in italics; italic markers not reproduced). Line-wrap hyphens "
        "repaired: 'problem', 'ellipsoidal', 'depicted'. Last sentence of the page continues on PDF page 7."
    )
    save(6, items, notes)


# --------------------------------------------------------------------------- page 7
def page7():
    refs = [
        ("p0007-b014", [315.0, 266.0, 564.0, 292.0], "[1] M. Farina, L. Giulioni, and R. Scattolini, “Stochastic Linear Model Predictive Control with Chance Constraints - A Review,” *J. Process Control*, vol. 44, pp. 53–67, 2016."),
        ("p0007-b015", [315.0, 293.0, 564.0, 319.0], "[2] M. Cannon, B. Kouvaritakis, and X. Wu, “Model Predictive Control for Systems with Stochastic Multiplicative Uncertainty and Probabilistic Constraints,” *Automatica*, vol. 45, no. 1, pp. 167–172, 2009."),
        ("p0007-b016", [315.0, 320.0, 564.0, 346.0], "[3] M. Cannon, B. Kouvaritakis, and D. Ng, “Probabilistic Tubes in Linear Stochastic Model Predictive Control,” *Systems & Control Letters*, vol. 58, no. 10-11, pp. 747–753, 2009."),
        ("p0007-b017", [315.0, 346.0, 564.0, 373.0], "[4] M. Lorenzen, F. Dabbene, R. Tempo, and F. Allgöwer, “Constraint-Tightening and Stability in Stochastic Model Predictive Control,” *IEEE Transactions on Automatic Control*, vol. 62, no. 7, pp. 3165–3177, 2017."),
        ("p0007-b018", [315.0, 373.0, 564.0, 399.0], "[5] M. Farina, L. Giulioni, L. Magni, and R. Scattolini, “A Probabilistic Approach to Model Predictive Control,” *Conf. Decision and Control*, pp. 7734–7739, 2013."),
        ("p0007-b019", [315.0, 400.0, 564.0, 426.0], "[6] L. Hewing and M. N. Zeilinger, “Stochastic Model Predictive Control for Linear Systems using Probabilistic Reachable Sets,” *Conf. Decision and Control*, 2018."),
        ("p0007-b020", [315.0, 427.0, 564.0, 453.0], "[7] L. Hewing, K. P. Wabersich, and M. N. Zeilinger, “Recursively Feasible Stochastic Model Predictive Control using Indirect Feedback,” *arXiv:1812.06860*, 2018."),
        ("p0007-b021", [315.0, 454.0, 564.0, 480.0], "[8] G. Calafiore and M. C. Campi, “Uncertain Convex Programs: Randomized Solutions and Confidence Levels,” *Mathematical Programming*, vol. 102, no. 1, pp. 25–46, Jan 2005."),
        ("p0007-b022", [315.0, 481.0, 564.0, 514.0], "[9] M. C. Campi and S. Garatti, “A Sampling-and-discarding Approach to Chance-constrained Optimization: Feasibility and Optimality,” *Journal of Optimization Theory and Applications*, vol. 148, no. 2, pp. 257–280, Feb 2011."),
        ("p0007-b023", [311.0, 517.0, 564.0, 543.0], "[10] M. Prandini, S. Garatti, and J. Lygeros, “A randomized approach to Stochastic Model Predictive Control,” in *Conf. Decision and Control*, Dec 2012, pp. 7315–7320."),
        ("p0007-b024", [311.0, 544.0, 564.0, 577.0], "[11] X. Zhang, K. Margellos, P. Goulart, and J. Lygeros, “Stochastic Model Predictive Control Using a Combination of Randomized and Robust Optimization,” in *Conf. Decision and Control*, Dec 2013, pp. 7740–7745."),
        ("p0007-b025", [311.0, 580.0, 564.0, 614.0], "[12] G. Schildbach, L. Fagiano, C. Frei, and M. Morari, “The Scenario Approach for Stochastic Model Predictive Control with Bounds on Closed-loop Constraint Violations,” *Automatica*, vol. 50, no. 12, pp. 3009 – 3018, 2014."),
        ("p0007-b026", [311.0, 615.0, 564.0, 642.0], "[13] G. C. Calafiore and L. Fagiano, “Stochastic Model Predictive Control of LPV Systems Via Scenario Optimization,” *Automatica*, vol. 49, no. 6, pp. 1861 – 1866, 2013."),
        ("p0007-b027", [311.0, 642.0, 564.0, 667.0], "[14] M. Lorenzen, F. Dabbene, R. Tempo, and F. Allgöwer, “Stochastic MPC with Offline Uncertainty Sampling,” *Automatica*, vol. 81, pp. 176 – 183, 2017."),
        ("p0007-b028", [311.0, 669.0, 564.0, 695.0], "[15] A. Stoorvogel, S. Weiland, and A. Saberi, “On stabilization of linear systems with stochastic disturbances and input saturation,” in *Conf. Decision and Control*, vol. 3, 2004, pp. 3007–3012 Vol.3."),
        ("p0007-b029", [311.0, 696.0, 564.0, 722.0], "[16] T. Hu, Z. Lin, and B. M. Chen, “Analysis and Design for Discrete-time Linear Systems Subject to Actuator Saturation,” *Systems & Control Letters*, vol. 45, no. 2, pp. 97 – 112, 2002."),
    ]
    items = [
        T(
            "p0007-b003",
            [48.0, 171.0, 301.0, 312.0],
            r"Corollary 1 with Remark 5 and find using (7) that we can remove $k = 820$ samples to determine $\mathcal{R}_k^{\theta_{\max}}$ and "
            r"$\mathcal{R}_k^{\theta_{\min}}$ satisfying the probability level $p_2 = 90\%$ with $\beta = 10^{-7}$. This results in $n_c = 3$ "
            r"time-varying PRS used for tightening in (10a). All offline computations, consisting of sampling, simulations and PRS computations "
            r"were carried out within a few seconds on standard hardware. Note that the use of half-space and box PRS are computationally cheap, "
            r"whereas the use of e.g. ellipsoidal constraints (Section IV-C) can require increased offline computation. The MPC optimization "
            r"problem (11) results in a quadratic program, which is reliably solved in around 20 ms in each time step.",
            join_previous="space",
        ),
        C("p0007-b000", [87.0, 59.0, 262.0, 75.0], "TABLE I. Closed-loop Chance Constraint Evaluation"),
        {
            "id": "p0007-b002",
            "kind": "table",
            "bbox": [54.0, 82.0, 295.0, 150.0],
            "markdown": "",
            "label": "Table I",
            "asset_name": "table-1",
            "rows": [
                ["Constraint", "Guaranteed Probability", "Empirical Probability"],
                ["[|p|; |v|] ≤ [p_max; v_max]", "99.6%", "99.98%"],
                ["θ ≤ θ_max", "90%", "91.2%"],
                ["θ ≥ −θ_max", "90%", "94.33%"],
            ],
        },
        T(
            "p0007-tablenote",
            [54.0, 150.0, 295.0, 168.0],
            r"Table I conversion note (not printed text): the table cells hold the constraints in plain characters. As printed, the three "
            r"entries of the Constraint column are $\begin{bmatrix} |p| \\ |v| \end{bmatrix} \le \begin{bmatrix} p_{\max} \\ v_{\max} \end{bmatrix}$ "
            r"(stacked column vectors), $\theta \le \theta_{\max}$ and $\theta \ge -\theta_{\max}$.",
        ),
        H("p0007-b004", [48.0, 340.0, 92.0, 348.0], "### B. Results"),
        T(
            "p0007-b005",
            [48.0, 360.0, 301.0, 537.0],
            r"We carried out 10000 simulations of the system with different noise realizations, the results of which are shown in Figure 2 and "
            r"Table I. It can be seen that the system approaches the reference position, keeping a safety distance to enable satisfaction of "
            r"constraint (16) which is achieved for almost all of the 10000 realizations. The minimum empirical constraint satisfaction rate over "
            r"all time steps of 91.2% is close to the one specified in the case of the maximum load angle, and somewhat conservative with "
            r"94.33% for the minimum load angle. This conservatism is likely due to the fact that in the latter case constraints on $z$ are "
            r"not simultaneously active for all simulated noise realizations in the same time-step. Finally, it can be observed in Figure 2 that "
            r"the applied input satisfies the given hard input constraints while dealing with Gaussian, and therefore possibly unbounded "
            r"disturbance sequences.",
        ),
        H("p0007-b006", [136.0, 563.0, 213.0, 571.0], "## VI. Conclusion"),
        T(
            "p0007-b007",
            [48.0, 585.0, 301.0, 679.0],
            "This paper presented a stochastic model predictive control approach for additive correlated disturbance sequences making use of "
            "the scenario approach for offline computation of probabilistic reachable sets for constraint tightening. This enabled us to show "
            "recursive feasibility and closed-loop chance satisfaction for systems under unbounded noise and hard input constraints. The "
            "effectiveness of the approach was demonstrated in a simulation example of an overhead crane.",
        ),
        H("p0007-b008", [128.0, 704.0, 221.0, 712.0], "## Acknowledgments"),
        T(
            "p0007-b030",
            [48.0, 727.0, 301.0, 749.0],
            "The authors would like to thank Simone Garatti and Marco Campi for the helpful discussion of the scenario approach.",
        ),
        H("p0007-b009", [415.0, 57.0, 460.0, 65.0], "## Appendix"),
        T("p0007-b010", [321.0, 72.0, 524.0, 82.0], "We consider a damped cart-pole system given by"),
        T(
            "p0007-b011",
            [327.0, 83.0, 548.0, 152.0],
            r"$$\begin{bmatrix} \cos\theta & l \\ m + M & M l \cos\theta \end{bmatrix} \begin{bmatrix} \ddot{p} \\ \ddot{\theta} \end{bmatrix} "
            r"= \begin{bmatrix} -g \sin\theta - d_M \frac{\dot{\theta}}{M} + \frac{w}{M} \cos\theta \\ "
            r"u - d_p \dot{p} - d_M (\dot{p} + l \dot{\theta} \cos\theta) + M l \dot{\theta}^2 \sin\theta + w \end{bmatrix}$$",
        ),
        T(
            "p0007-b012",
            [311.0, 152.0, 564.0, 235.0],
            r"with slider mass $m = 1$ and damping $d_m = 10$, payload mass $M = 1$ and damping $d_M = 1$ and $l = 1$, $g = 9.81$. "
            r"Linearization around the origin and discretization with sampling time $T_s = 0.1$ yields the employed linear system with "
            r"eigenvalues $\lambda = [1, 0.3672, 0.8617 \pm 0.2788i]^{\mathsf{T}}$. The distribution of the disturbance is zero mean Gaussian "
            r"$W \sim \mathcal{N}(0, K)$ with $K_{i,j} = 0.02^2 + 0.2^2 \exp(-\frac{1}{2}(i-j)^2/10^2)$, $i, j \in \{1, \ldots, \bar{N}\}$.",
        ),
        H("p0007-b013", [409.0, 250.0, 466.0, 258.0], "## References"),
    ] + [T(i, b, m) for i, b, m in refs]
    notes = (
        "Compared with 200 dpi page render, 300 dpi column crops and 500 dpi zooms of Table I and of the appendix equation. Reading order: "
        "left column (Table I, end of 'A. Simulation Setup', 'B. Results', 'VI. Conclusion', 'Acknowledgments'), then right column "
        "('Appendix', 'References'). Table I floats at the top of the left column inside the sentence that runs over from PDF page 6; the "
        "continuing paragraph ('Corollary 1 with Remark 5 ...', join_previous=space) is placed first, then the table caption and table. "
        "Table I transcribed as cells (3 columns, header + 3 rows; percentages copied exactly: 99.6%/99.98%, 90%/91.2%, 90%/94.33%) and "
        "checked cell by cell on the 500 dpi zoom. The Constraint column holds small formulas; because the builder doubles backslashes in "
        "table cells, they are stored in plain characters ('[|p|; |v|] ≤ [p_max; v_max]', 'θ ≤ θ_max', 'θ ≥ −θ_max') and an explicitly "
        "labelled conversion-note item after the table gives the printed forms in LaTeX (first entry is printed as two stacked column "
        "vectors). Table caption is printed as two centred small-caps lines 'TABLE I' / 'CLOSED-LOOP CHANCE CONSTRAINT EVALUATION', merged "
        "into one caption item in title case. The appendix equation (2x2 matrix times [p̈; θ̈] equals a 2-vector) was a formula image and "
        "is now LaTeX; verified symbol by symbol at 500 dpi, including the dots/double dots and the fractions θ̇/M and w/M. Inline math "
        "rebuilt: R_k^{θ_max}, R_k^{θ_min}, 10^{-7}, eigenvalue vector, covariance K_{i,j} = 0.02^2 + 0.2^2 exp(-½(i-j)^2/10^2). Printed "
        "peculiarities kept verbatim: 'remove k = 820 samples' (k, not N_k); the appendix equation uses d_p for the slider damping while the "
        "following text defines 'damping d_m = 10'; the sets are named R_k^{θ_max} and R_k^{θ_min} although Table I uses ±θ_max; "
        "'half-space and box PRS are computationally cheap'. Headings: 'B. Results' as '###'; 'VI. Conclusion', 'Acknowledgments', "
        "'Appendix', 'References' as '##' (small caps written in title case; extractor had '#'). References [1]-[16]: one item per entry, "
        "list bullets removed, all 16 compared with the render; line-wrap hyphens repaired ('Linear' in [3], 'Feasible' in [7], 'Randomized' "
        "in [8], page range '7740–7745' in [11]); real hyphens at line ends kept ('Constraint-Tightening' in [4], 'Discrete-time' in [16]); "
        "'Allgöwer' restored from the extractor's 'Allg¨ower' in [4] and [14]; spaced en dashes in the page ranges of [12], [13], [14], [16] "
        "and 'Vol.3' in [15] kept as printed. Line-wrap hyphens repaired in prose: 'control', 'computation'."
    )
    save(7, items, notes)


FUN = {1: page1, 2: page2, 3: page3, 4: page4, 5: page5, 6: page6, 7: page7}
if __name__ == "__main__":
    todo = [int(a) for a in sys.argv[1:]] or sorted(FUN)
    for n in todo:
        FUN[n]()
