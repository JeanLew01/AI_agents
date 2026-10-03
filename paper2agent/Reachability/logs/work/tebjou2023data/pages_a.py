#!/usr/bin/env python3
"""Pages 1-3 of tebjou2023data (PMLR v204 PDF). Run: python3 pages_a.py"""
from lib import page, HDR_ODD, HDR_EVEN, pageno

T = "text"

# ---------------------------------------------------------------- page 1
page(1, r"""
Compared with the 170 dpi render of PDF page 1 and with the authors' arXiv TeX source (main.tex). The
proceedings banner at the top ('Proceedings of Machine Learning Research 204:1-20, 2023 Conformal and
Probabilistic Prediction with Applications') is page furniture and is omitted; its content is recorded in the
conversion notes. Title kept as the single level-1 heading (bold markers removed, the two printed lines
joined). Author block rewritten as one item per author with name, e-mail (printed in small caps, written in
lower case as in the PDF text layer) and affiliation lines; the diacritics damaged by the extractor
('Fa¨ıcel', 'Bostr¨om') are restored to 'Faïcel' and 'Boström' as printed. The editor line is kept. 'Abstract'
is printed as a centred bold heading and is a level-2 heading here. Line-wrap hyphens in the abstract
('re-cently', 'statis-tical') were removed; 'real-life', 'Data-based', 'data-based', 'data-driven' are printed
compound hyphens. The 'Keywords:' run-in label is kept in bold. '1. Introduction' is a level-2 heading with the
printed number. The copyright line printed in the page footer ('(c) 2023 A. Tebjou, G. Frehse & F.
Chamroukhi.') is kept as a text item and placed after the editor line, so that it does not interrupt the last
sentence of the page, which continues on page 2 ('... scalability, tightness, | or efficient computability');
the continuation is joined on page 2. Line-wrap hyphen 'approxi-mations' removed; 'cyber-physical' is a
printed compound hyphen. Citations are author-year as printed. No mathematics on this page. The prose
agrees word for word with the TeX source.
""", [
    ("p0001-b000", "omit", ("p0001-b000",), "",
     {"reason": "Proceedings banner in the page header: 'Proceedings of Machine Learning Research 204:1-20, 2023 Conformal and Probabilistic Prediction with Applications'. Page furniture; the venue and volume are recorded in the conversion notes."}),
    ("p0001-b001", "heading", ("p0001-b001",),
     "# Data-driven Reachability using Christoffel Functions and Conformal Prediction", {}),
    ("p0001-b002", T, ("p0001-b002",),
     "**Abdelmouaiz Tebjou** (abdelmouaiz.tebjou@irt-systemx.fr)\n"
     "IRT SystemX, 2 boulevard Thomas Gobert, 91120 Palaiseau, France.\n"
     "U2IS, ENSTA Paris, Institut Polytechnique de Paris, Palaiseau, France.", {}),
    ("p0001-b003", T, ("p0001-b003",),
     "**Goran Frehse** (goran.frehse@ensta-paris.fr)\n"
     "U2IS, ENSTA Paris, Institut Polytechnique de Paris, Palaiseau, France.", {}),
    ("p0001-b004", T, ("p0001-b004", "p0001-b005"),
     "**Faïcel Chamroukhi** (faicel.chamroukhi@irt-systemx.fr)\n"
     "IRT SystemX, 2 boulevard Thomas Gobert, 91120 Palaiseau, France.", {}),
    ("p0001-b006", T, ("p0001-b006",),
     "**Editor:** Harris Papadopoulos, Khuong An Nguyen, Henrik Boström and Lars Carlsson", {}),
    ("p0001-b012", T, ("p0001-b012",),
     "© 2023 A. Tebjou, G. Frehse & F. Chamroukhi.", {}),
    ("p0001-b007", "heading", ("p0001-b007",), "## Abstract", {}),
    ("p0001-b008", T, ("p0001-b008",),
     "An important mathematical tool in the analysis of dynamical systems is the approximation of the reach set, i.e., the set of states reachable after a given time from a given initial state. This set is difficult to compute for complex systems even if the system dynamics are known and given by a system of ordinary differential equations with known coefficients. In practice, parameters are often unknown and mathematical models difficult to obtain. Data-based approaches are promised to avoid these difficulties by estimating the reach set based on a sample of states. If a model is available, this training set can be obtained through numerical simulation. In the absence of a model, real-life observations can be used instead. A recently proposed approach for data-based reach set approximation uses Christoffel functions to approximate the reach set. Under certain assumptions, the approximation is guaranteed to converge to the true solution. In this paper, we improve upon these results by notably improving the sample efficiency and relaxing some of the assumptions by exploiting statistical guarantees from conformal prediction with training and calibration sets. In addition, we exploit an incremental way to compute the Christoffel function to avoid the calibration set while maintaining the statistical convergence guarantees. Furthermore, our approach is robust to outliers in the training and calibration set.", {}),
    ("p0001-b009", T, ("p0001-b009",),
     "**Keywords:** data-driven reachability, Christoffel functions, conformal prediction, probably approximately correct analysis, statistical learning", {}),
    ("p0001-b010", "heading", ("p0001-b010",), "## 1. Introduction", {}),
    ("p0001-b011", T, ("p0001-b011",),
     "The problem of reach set approximation arises in different branches of applied mathematics and computer science, and in particular in control theory. In mathematics, the study of initial value problems and their guaranteed solution raises the question of which states can be reached under different configurations; see, for instance the work of Berz and Makino (1998). In computer science, the computation of reach sets is a fundamental operation in formal methods, which establish the correctness of a system with mathematical rigor. Initially, it was applied to program analysis, e.g., by Halbwachs et al. (1994). Later, the approach was extended to cyber-physical systems, which can involve interacting physical components, software, and communication channels, see Alur (2015). Reach set approximations may take different forms based on whether the focus is on scalability, tightness,", {}),
])

# ---------------------------------------------------------------- page 2
page(2, r"""
Compared with the 170 dpi render of PDF page 2 and with the TeX source. Running header and page number
omitted. The first item continues the last sentence of page 1 (join_previous: space). Paragraph structure as
printed (four indented paragraphs plus the run-in paragraph heading 'Related Work', kept as a bold run-in label
because it is a \paragraph heading, not a numbered section). The PDF underlines emphasised words (the authors
load ulem, so \emph prints as underline); 'probably approximately correct' is written in italics and the
extractor's '<u>' tags were removed. Line-wrap hyphens removed: 'construc-tion', 'optimi-sation',
'func-tions'; printed compound hyphens kept: 'sum-of-squares', 'data-based', 'set-based', 'data-driven',
'one-step'. British spellings 'analyse', 'optimisation', 'practise' are as printed. The citation pair is
printed 'Lasserre and Pauwels (2019); Lasserre (2022)' with a semicolon. The last word of the page is split by
the page break ('improve-' | 'ments'); the item ends with 'improve' and page 3 continues with
join_previous: none. No mathematics on this page. Prose agrees with the TeX source.
""", [
    ("p0002-b000", "omit", ("p0002-b000",), "", {"reason": HDR_EVEN}),
    ("p0002-b001", T, ("p0002-b001",),
     "or efficient computability. Examples include polyhedra, ellipsoids, polynomial zonotopes, and others; see the overview by Althoff et al. (2021). In this paper, we establish reach set approximations that are sublevel sets of polynomials, more precisely, sum-of-squares (SOS) polynomials, which are computationally advantageous. Once established, these can readily be used to investigate properties of regions of attraction, stability, and safety or to solve optimization problems. To achieve this, polynomial reach set approximations have been used as barrier certificates, inductive invariants, or Lyapunov functions; see the survey by Doyen et al. (2018).",
     {"join_previous": "space"}),
    ("p0002-b002", T, ("p0002-b002",),
     "Traditionally, reach set approximations are established from first principles, starting from a mathematical model of the dynamics. This approach is limited to cases where sufficiently simple models are available and precise enough. More recently, data-based approaches have been used to deal with systems whose dynamics are too complex or where a model is not available and only observations are at hand. In the following, we provide a brief overview of such approaches.", {}),
    ("p0002-b003", T, ("p0002-b003",),
     "**Related Work** The traditional approach to go from data to reach set approximations is to first identify a model of the system dynamics and then analyse the model. To give an example, a linear model can be identified efficiently by subspace identification as proposed by Van Overschee and De Moor (2012) and then one of the set-based techniques in the survey by Althoff et al. (2021) can be applied to approximate the reach set at a given time in the future. This can be extended to uncertain linear models and nonlinear systems based on linearization, as pursued by Alanwar et al. (2023). More recently, it has been proposed to derive reach set approximations more directly from data, e.g., the approach of Djeumou et al. (2021) uses Taylor series expansions and Lipschitz bounds to derive reach sets for nonlinear systems. These approaches can, in principle, bound the reach set over an arbitrary time horizon, but the approximation error may increase very rapidly with time. Furthermore, these approaches struggle with complex dynamics.", {}),
    ("p0002-b004", T, ("p0002-b004",),
     "Our goal in this paper is different and more modest: We establish an SOS polynomial whose sublevel set contains the reachable set in the sense of a *probably approximately correct* (PAC) property. In particular, we consider the approximation of a single time step. This is sufficient for many of the applications considered above (as a first step in constructing barrier certificates, inductive invariants etc.), but in contrast to the approaches cited in the beginning of this section, it does not readily extend to extrapolating the reach set over longer time horizons (it would involve costly quantifier elimination).", {}),
    ("p0002-b005", T, ("p0002-b005",),
     "One of the earliest data-driven approaches involving SOS polynomials was the construction of barrier certificates by Prajna (2006), e.g., to show that obstacles are avoided by a control system. The scalability was later improved by Han et al. (2015), but the optimisation problem remains somewhat challenging. Approximating the reach set is related to approximating the support of a probability measure, as observed by Devonport et al. (2021). Recent work by Lasserre and Pauwels (2019); Lasserre (2022) suggests that Christoffel functions are particularly useful for approximating the support. Our work is heavily inspired by Devonport et al. (2021), who proposed to approximate the one-step reach set with an SOS polynomial that is the superlevel set of the Christoffel function. The PAC guarantees provided by Devonport et al. (2021) are derived from measure theory and are, in practise, somewhat conservative. Based on conformal prediction, we propose significant improve", {}),
    ("p0002-b006", "omit", ("p0002-b006",), "", {"reason": pageno(2)}),
])

# ---------------------------------------------------------------- page 3
page(3, r"""
Compared with the 170 dpi render of PDF page 3 and with the TeX source. Running header and page number
omitted. The first item completes the word split by the page break ('improve-' | 'ments', join_previous:
none). 'Contributions' and 'Structure of the paper' are run-in \paragraph headings, kept as bold run-in
labels; the extractor's spurious list marker before 'Contributions' was removed. The four contributions are
one list item each. Line-wrap hyphens removed: 'confor-mal', 'func-tions', 'Sec-tion'; 'sample-efficient'
and 'data-driven' are printed compound hyphens. Section cross-references are written with the printed
numbers (Section 2, 3, 3.1, 3.2, 4, 5). '2. Data-driven Reach Set Approximation with Christoffel Functions'
is a level-2 heading (the extractor had made it level 1). DIFFERENCE FROM THE arXiv TeX SOURCE: the PMLR PDF
prints the transition function as a displayed formula 'f : R^n -> R^n,' after 'by a transition function'; the
arXiv TeX has no such display ('by a transition function which maps a state ...'). The PDF is followed. Both
displays on this page (the transition function and the reachable set S = {f(x) : x in I}) are unnumbered
and were transcribed to LaTeX and checked on the render; the extractor's two formula images were replaced.
Inline mathematics from the TeX source with the jmlr macros expanded (\Vec{x} -> \boldsymbol{x}, printed
bold italic; \set{S} -> \mathcal{S}). As printed, the sentence 'Every set S can be represented ...' uses a
plain italic S twice (not calligraphic) and reads 'such as S is the support'. 'reachable set' is underlined
in the PDF (\emph) and written in italics.
""", [
    ("p0003-b000", "omit", ("p0003-b000",), "", {"reason": HDR_ODD}),
    ("p0003-b001", T, ("p0003-b001",),
     "ments that we outline below. Further work on conformal prediction will be cited in the text.",
     {"join_previous": "none"}),
    ("p0003-b002", T, ("p0003-b002",),
     "**Contributions** In this paper, we make the following contributions:", {}),
    ("p0003-b003", T, ("p0003-b003",),
     "- We use conformal prediction to provide stronger and more sample-efficient guarantees on reach set approximation than those given by Devonport et al. (2021).", {}),
    ("p0003-b004", T, ("p0003-b004",),
     "- We propose a version of reach set approximation that is robust to outliers, in contrast to the approach of Devonport et al. (2021).", {}),
    ("p0003-b005", T, ("p0003-b005",),
     "- We exploit an incremental form of the Christoffel function for transductive conformal prediction, thanks to which we don’t need to split the data set into training and calibration sets.", {}),
    ("p0003-b006", T, ("p0003-b006",),
     "- To the best of our knowledge, this is the first use of the Christoffel function in conformal prediction. The particular properties of the Christoffel function in set and density approximation make it an excellent candidate for a nonconformity function.", {}),
    ("p0003-b007", T, ("p0003-b007",),
     "**Structure of the paper** The paper is organized as follows. Section 2 presents the data-driven framework for reachability analysis using Christoffel functions. It describes the theoretical developments related to the reach set approximation and to Christoffel functions. In Section 3, we introduce our proposed approach to the reach set approximation with conformal prediction, whose statistical guarantees are presented in Section 3.1. Section 3.2 presents a technique to avoid the calibration set by using transductive conformal prediction and an incremental version of the Christoffel function. In Section 4, we discuss the robustness of our methodology to outliers. Section 5 provides numerical experiments on simulated data to support our theoretical results, and to highlight the effectiveness and potential of the proposed approach.", {}),
    ("p0003-b008", "heading", ("p0003-b008",),
     "## 2. Data-driven Reach Set Approximation with Christoffel Functions", {}),
    ("p0003-b009", T, ("p0003-b009",),
     "Reachability analysis aims to determine the possible future states of a dynamical system starting from a given initial state. For our purposes, we consider the system to be defined (explicitly or implicitly) by a transition function", {}),
    ("p0003-b010", T, ("p0003-b010",),
     "$$\nf : \\mathbb{R}^n \\rightarrow \\mathbb{R}^n,\n$$", {}),
    ("p0003-b011", T, ("p0003-b011",),
     r"which maps a state $\boldsymbol{x} \in \mathbb{R}^{n}$ to its successor state. We forego extending the notation to nondeterministic or stochastic systems, since our focus is on estimating the image of $f$ applied to a set of initial states; in the case of a stochastic system we are interested in approximating the support of the image distribution. Beginning with a given initial set of states $\mathcal{I}$, we are interested in computing the *reachable set*", {}),
    ("p0003-b012", T, ("p0003-b012",),
     "$$\n\\mathcal{S} = \\{ f(\\boldsymbol{x}) : \\boldsymbol{x} \\in \\mathcal{I} \\}.\n$$", {}),
    ("p0003-b013", T, ("p0003-b013",),
     r"When $f$ is not precisely known or complex, obtaining the exact solution may not be possible or economical. Instead, we compute an approximation $\hat{\mathcal{S}}$ that covers most of $\mathcal{S}$. Every set $S$ can be represented by a probability measure $\mu$ such as $S$ is the support of $\mu$. This motivated Devonport et al. (2021) to use the Christoffel function to approximate the set $\mathcal{S}$. In the following subsection, we introduce the Christoffel function, its empirical counterpart, and discuss how to compute it.", {}),
    ("p0003-b014", "omit", ("p0003-b014",), "", {"reason": pageno(3)}),
])
