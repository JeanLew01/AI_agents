#!/usr/bin/env python3
"""Pages 4-6 of tebjou2023data (PMLR v204 PDF). Run: python3 pages_b.py"""
from lib import page, HDR_ODD, HDR_EVEN, pageno

T = "text"


def D(s):
    return "$$\n" + s.strip() + "\n$$"


# ---------------------------------------------------------------- page 4
page(4, r"""
Compared with the 170 dpi render of PDF page 4, with 230-260 dpi crops of the notation paragraph and of all
displays, and with the TeX source. Running header and page number omitted. '2.1. Preliminaries' and '2.2.
Christoffel Functions' are level-3 headings with the printed numbers. All mathematics was taken from the TeX
source with the jmlr macros expanded (\Vec{x} -> \boldsymbol{x}; \mathbf kept for the upright bold v, M, x, z)
and checked symbol by symbol on the crops; the extractor's five formula images were replaced by LaTeX
displays. Only the definition of the Christoffel function carries a printed number, (1). Typography kept as
printed: the vector of monomials is bold italic v_d in the text and in the moment-matrix integral but upright
bold v_d in (1); the transpose is \top in the integral and T in (1); 'the invertibility of M_d' prints a plain
italic M_d; the infimum formula prints upright bold z and x in P(z), P(x); 'less or equal to d evaluated at'
prints an upright (text) d; 'n-variate' is in text; the degree is written with a double-bar norm
||alpha|| = sum_i alpha_i with a bold alpha_i; the empirical measure display has the limits of the sum set
as sub/superscripts and ends with a comma (the sentence continues on page 5 with 'where ...'). The footnote
marker after 'M_d.' is written as a LaTeX superscript 1. Footnote 1 is printed at the bottom of the page,
below the empirical-measure display; here it is placed directly after display (1), i.e. after the sentence that
carries the marker, so that it does not separate the empirical-measure display from its continuation on page
5. 'Christoffel function', 'moment matrix' and 'empirical measure' are underlined in the PDF (\emph) and
written in italics. 'defined as :' has a space before the colon as printed. 'i.i.d samples' (no final period)
as printed.
""", [
    ("p0004-b000", "omit", ("p0004-b000",), "", {"reason": HDR_EVEN}),
    ("p0004-b001", "heading", ("p0004-b001",), "### 2.1. Preliminaries", {}),
    ("p0004-b002", T, ("p0004-b002",),
     r"We start by introducing some mathematical notation. Given a vector $\boldsymbol{x} \in \mathbb{R}^n$, we denote its elements as $\boldsymbol{x} = (x_1,...,x_n)$. An integer coefficient vector $\boldsymbol{\alpha} = (\alpha_1,...,\alpha_n) \in \mathbb{N}^n$ defines the monomial $\boldsymbol{x}^{\boldsymbol{\alpha}} = x_1^{\alpha_1} \times x_2^{\alpha_2} ... \times x_n^{\alpha_n}$. For $d \in \mathbb{N}$, we consider $\mathbb{R}[\boldsymbol{X}]_d^n$ to be the vector space of n-variate polynomials whose degree is less or equal to $d$. With each coefficient vector $\boldsymbol{\alpha} \in \mathbb{N}^n$, we associate the monomial $\boldsymbol{x}^{\boldsymbol{\alpha}}$ whose degree is equal to $\| \boldsymbol{\alpha} \| = \sum_{i=1}^{n} \boldsymbol{\alpha}_i$. The monomials $\boldsymbol{x}^{\boldsymbol{\alpha}}$ with $\| \boldsymbol{\alpha} \| \leq d$ form a canonical basis of $\mathbb{R}[\boldsymbol{X}]_d^n$. We denote the number of monomials of degree less or equal to $d$ with", {}),
    ("p0004-b003", T, ("p0004-b003",), D(r"s(d) = \binom{n+d}{n}."), {}),
    ("p0004-b004", T, ("p0004-b004",),
     r"Let $\boldsymbol{v}_d(\boldsymbol{x}) \in \mathbb{R}^{s(d)}$ be the vector of monomials of degree less or equal to d evaluated at $\boldsymbol{x}$. For example, if $d = 2$ and $n = 2$, then $\boldsymbol{v}_{d}(\boldsymbol{x}) = [ 1 \ x_1 \ x_2 \ x_{1}x_{2} \ x_{1}^2 \ x_{2}^2 ]$.", {}),
    ("p0004-b005", "heading", ("p0004-b005",), "### 2.2. Christoffel Functions", {}),
    ("p0004-b006", T, ("p0004-b006",),
     r"Christoffel functions are a class of functions associated with a finite measure and a parameter degree $d \in \mathbb{N}$. They have a strong connection to approximation theory and in this section we briefly summarize some results by Lasserre and Pauwels (2019). For a finite measure $\mu$ on $\mathbb{R}^{n}$ and an integer degree $d$, the *Christoffel function* $\Lambda_{\mu, d}(\boldsymbol{x}) : \mathbb{R}^n \mapsto \mathbb{R}$ is defined in terms of the *moment matrix* of the measure $\mu$:", {}),
    ("p0004-b007", T, ("p0004-b007",),
     D(r"\mathbf{M}_d = \int_{\mathbb{R}^{n}} \boldsymbol{v}_{d}(\boldsymbol{x}) \boldsymbol{v}_{d}(\boldsymbol{x})^{\top} d\mu(\boldsymbol{x})."), {}),
    ("p0004-b008", T, ("p0004-b008",),
     r"The moment matrix is semi-definite positive for all $d \in \mathbb{N}$. We furthermore assume that the matrix is positive definite, which ensures the invertibility of $M_d$.$^{1}$ With the help of the moment matrix, the Christoffel function is defined as :", {}),
    ("p0004-b009", T, ("p0004-b009",),
     D(r"\Lambda_{\mu, d}(\boldsymbol{x}) = \Bigl( \mathbf{v}_{d}(\boldsymbol{x})^{T} \mathbf{M}_{d}^{-1} \mathbf{v}_{d}(\boldsymbol{x}) \Bigr)^{-1}. \tag{1}"), {}),
    ("p0004-b014", T, ("p0004-b014",),
     r"Footnote 1: In fact, the moment matrix of any finite measure $\mu$ is definite positive unless the support of $\mu$ is contained in the zeros of a polynomial; for a closer look at the moment matrix, we refer the reader to Lasserre and Pauwels (2019).", {}),
    ("p0004-b010", T, ("p0004-b010",),
     r"The following alternative formulation of the Christoffel function can be useful when the moment matrix is large. It can be computed by solving a convex quadratic programming problem, which can be done efficiently using numerical techniques, even for high degrees $d$:", {}),
    ("p0004-b011", T, ("p0004-b011",),
     D(r"\Lambda_{\mu, d}(\boldsymbol{x}) = \inf_{P \in \mathbb{R}[\boldsymbol{X}]_d^n} \left\{ \int_{\mathbb{R}^{n}} P(\mathbf{z})^{2} d\mu(\mathbf{z}), \quad \text{s.t.} \quad P(\mathbf{x}) = 1 \right\}"), {}),
    ("p0004-b012", T, [90.0, 591.0, 523.0, 636.5],
     r"In a data-driven setting, the exact measure $\mu$ is unknown. One way to obtain information about $\mu$ is by sampling a set of points independently drawn from its distribution. For every $N \in \mathbb{N}$, when disposing of $N$ i.i.d samples $\{ \boldsymbol{x}^{1}, \ldots, \boldsymbol{x}^{N} \}$ from $\mu$, we approximate $\mu$ with the *empirical measure*", {}),
    ("p0004-b013", T, [261.0, 637.0, 351.0, 669.0],
     D(r"\hat{\mu} = \tfrac{1}{N} {\sum}_{i=1}^{N} \delta_{\boldsymbol{x}^i},"), {}),
    ("p0004-b015", "omit", ("p0004-b015",), "", {"reason": pageno(4)}),
])

# ---------------------------------------------------------------- page 5
page(5, r"""
Compared with the 170 dpi render of PDF page 5, with 240-260 dpi crops of the top third and of the lower
half, and with the TeX source. Running header and page number omitted. The first item continues the sentence
of the empirical-measure display of page 4 ('where delta_x is the Dirac measure'); it starts a new item
because a display precedes it. '2.3. Set Approximation with Christoffel Functions' is a level-3 heading.
Mathematics from the TeX source with macros expanded; the extractor's six formula images were replaced by
LaTeX displays with the printed numbers (2)-(6) as \tag. Typography kept as printed: in (2) the sample is
upright bold with an upright bold superscript, v_d(x^i), and the transpose is T; in (3) the hat spans M_d and
the exponent -1 is outside the hat (\widehat{\mathbf{M}_d}^{-1}); in the text before (5) the samples are printed
with a bold italic superscript i (\boldsymbol{x^i}) and the relation is 'x^i subseteq S-hat' as printed; (4)
uses the Christoffel polynomial of the exact measure mu, (5) and (6) the empirical one. Conjecture 1: the PDF
prints the header in bold as 'Conjecture 1 (Thm. 1 in Devonport et al. (2021))' with no punctuation after it
and the body in italics (the italics are not reproduced); the body ends with the inline sample-size condition
and '>= 1 - delta.', as in the TeX conjecture environment. The bound was checked on the 240 dpi crop:
N >= (5/eps)(log(4/delta) + binom(n+2d, n) log(40/eps)). Line-wrap hyphens removed: 'Conse-quently',
'con-verges', 'em-pirical', 'fol-lowing', 'sam-ples'; 'sum-of-squares' is a printed compound hyphen.
'Christoffel polynomial' is underlined in the PDF (\emph) and written in italics. The last sentence continues
on page 6 ('... and the | points used to construct the threshold'); joined there.
""", [
    ("p0005-b000", "omit", ("p0005-b000",), "", {"reason": HDR_ODD}),
    ("p0005-b001", T, [89.0, 90.0, 522.0, 118.5],
     r"where $\delta_{\boldsymbol{x}}$ is the Dirac measure. The moment matrix $\widehat{\mathbf{M}}_d$ associated with the empirical measure $\hat{\mu}$ is", {}),
    ("p0005-b002", T, [232.0, 119.0, 528.0, 144.0],
     D(r"\widehat{\mathbf{M}}_d = \tfrac{1}{N} {\sum}_{i=1}^{N} \mathbf{v}_{d}(\mathbf{x^{i}}) \mathbf{v}_{d}(\mathbf{x^{i}})^{T} \tag{2}"), {}),
    ("p0005-b003", T, ("p0005-b003",),
     r"Therefore, the empirical measure $\hat{\mu}$ defines an empirical Christoffel function. Since we are only interested in superlevel sets of the Christoffel function, we can forego the inversion and instead work with sublevel sets of what we call the empirical *Christoffel polynomial*:", {}),
    ("p0005-b004", T, ("p0005-b004",),
     D(r"\Lambda^{-1}_{\hat{\mu}, d}(\boldsymbol{x}) = \mathbf{v}_{d}(\boldsymbol{x})^{T} \widehat{\mathbf{M}_{d}}^{-1} \mathbf{v}_{d}(\boldsymbol{x}) \tag{3}"), {}),
    ("p0005-b005", T, ("p0005-b005",),
     r"Note that the moment matrix $\widehat{\mathbf{M}}_d$ is almost surely invertible if the number of samples $N \geq s(d)$. The Christoffel polynomial is a sum-of-squares polynomial of degree $2d$. Consequently, it is nonnegative, and if $N > s(d)$, the empirical Christoffel polynomial is strictly positive. Note that, for increasing sample size $N$, the empirical Christoffel function converges uniformly to the Christoffel function of the exact measure.", {}),
    ("p0005-b006", "heading", ("p0005-b006",), "### 2.3. Set Approximation with Christoffel Functions", {}),
    ("p0005-b007", T, ("p0005-b007",),
     r"Lasserre and Pauwels (2019) proposed various thresholding schemes for approximating the support of a probability measure using the Christoffel function or, more precisely, its empirical counterpart. This idea was applied by Devonport et al. (2021) to approximate the reachable set $\mathcal{S}$ with the superlevel sets of the Christoffel function. In this section, we will briefly summarize the approach.", {}),
    ("p0005-b008", T, ("p0005-b008",),
     r"Let $\mu$ be the probability measure of the reachable set $\mathcal{S}$. For a given degree $d \in \mathbb{N}$, the reachable set can be approximated with the sublevel set", {}),
    ("p0005-b009", T, ("p0005-b009",),
     D(r"\hat{\mathcal{S}} = \{ \boldsymbol{x} \in \mathbb{R}^{n} \mid \Lambda^{-1}_{\mu, d}(\boldsymbol{x}) \leq \alpha \} \tag{4}"), {}),
    ("p0005-b010", T, [90.0, 459.0, 523.0, 510.5],
     r"for some $\alpha \in \mathbb{R}$. However, since the exactly reachable set $\mathcal{S}$ is unknown, $\mu$ is unknown. Instead, the Christoffel function $\Lambda_{\mu, d}$ is approximated by an empirical Christoffel function using i.i.d generated samples $\boldsymbol{x^{i}}$ from $\mathcal{S}$. We can obtain a conservative threshold $\alpha$ such that $\boldsymbol{x^{i}} \subseteq \hat{\mathcal{S}}$ by letting", {}),
    ("p0005-b011", T, [258.0, 511.0, 528.0, 534.0],
     D(r"\alpha = \max_i \Lambda^{-1}_{\hat{\mu}, d}(\boldsymbol{x}^{i}). \tag{5}"), {}),
    ("p0005-b012", T, ("p0005-b012",),
     r"Using methods from statistical learning theory, Devonport et al. (2021) proposed the following PAC guarantees:", {}),
    ("p0005-b013", T, ("p0005-b013",),
     r"**Conjecture 1 (Thm. 1 in Devonport et al. (2021))** Given a training set of i.i.d samples $\mathcal{D} = \{ \boldsymbol{x}^1, \ldots, \boldsymbol{x}^N \}$ from $\mathcal{S}$, let", {}),
    ("p0005-b014", T, ("p0005-b014",),
     D(r"\hat{\mathcal{S}} = \{ \boldsymbol{x} \in \mathbb{R}^{n} \mid \Lambda^{-1}_{\hat{\mu}, d}(\boldsymbol{x}) \leq \max_i \Lambda^{-1}_{\hat{\mu}, d}(\boldsymbol{x}^{i}) \}. \tag{6}"), {}),
    ("p0005-b015", T, [90.0, 633.0, 523.0, 664.0],
     r"If $N \geq \frac{5}{\epsilon} \left( \log \frac{4}{\delta} + \binom{n+2d}{n} \log \frac{40}{\epsilon} \right)$, then $\mathbb{P}\Bigl( \mu\bigl( \hat{\mathcal{S}} \bigr) \geq 1-\epsilon \Bigr) \geq 1-\delta.$", {}),
    ("p0005-b016", T, ("p0005-b016",),
     r"In other words, if $N, \delta, \epsilon$ satisfy the condition in Conjecture 1, then with probability bigger than $1-\delta$ we are sure that $\hat{\mathcal{S}}$ contains more than $1-\epsilon$ of the mass of $\mathcal{S}$. However, we believe this result neglects the dependencies between the empirical Christoffel polynomial and the", {}),
    ("p0005-b017", "omit", ("p0005-b017",), "", {"reason": pageno(5)}),
])

# ---------------------------------------------------------------- page 6
page(6, r"""
Compared with the 170 dpi render of PDF page 6, with a 240 dpi crop of Example 1, and with the TeX source.
Running header and page number omitted. The first item completes the sentence begun on page 5
(join_previous: space). The three convergence results are one list item each; '(non-empirical)' is a compound
hyphen at a line end (confirmed in the TeX source). Kept as printed (authors' slips, not conversion errors):
'in these sense of a Hausdorff distance' (twice), and 'For fixed d and n -> infinity' in the second and third
bullet, where n is the state dimension and the sample size N is evidently meant. Example 1: the PDF prints
the header in bold as 'Example 1 (Four squares)' without punctuation and the body in italics (not
reproduced); the example ends with '... covers nearly 100% of S.', directly before the heading of Section 3
(end of the example environment in the TeX source). The two displays of the example (transition function and
the four-squares set) are unnumbered; 'sign' is printed in math italics. In the example the estimate and the
set are printed with a plain italic S (S-hat, S), not calligraphic, as in the TeX source. The sample size is
printed 'N = 10 000' with a thin space (TeX 10\,000); it is written 10000 so that the number stays searchable
(the caption of Figure 1 prints 10000). The example uses \varepsilon once ('uncertainty bound') and \epsilon
twice, as printed. Line-wrap hyphen 'increas-ing' removed. '100%' is written outside math mode. '3. Reach Set Approximation with Conformal
Prediction' is a level-2 heading; its first two paragraphs end the page with a complete sentence. Cross
references written with the printed numbers (Section 3, Section 2, Figure 1, (6), Conjecture 1). Figure 1,
which belongs to this example, is printed at the top of page 7; the reading order places it directly after
the example.
""", [
    ("p0006-b000", "omit", ("p0006-b000",), "", {"reason": HDR_EVEN}),
    ("p0006-b001", T, ("p0006-b001",),
     r"points used to construct the threshold $\alpha$. As will be discussed in more detail in Section 3, different samples should be used for constructing the empirical Christoffel polynomial and for constructing the threshold $\alpha$ to ensure independence.",
     {"join_previous": "space"}),
    ("p0006-b002", T, ("p0006-b002",),
     r"We informally note convergence results by Lasserre and Pauwels (2019), which hold for uniform probability measures (and some generalizations):", {}),
    ("p0006-b003", T, ("p0006-b003",),
     r"- As $d \rightarrow \infty$ and with an appropriately chosen threshold, the sublevel set of the (non-empirical) Christoffel polynomial converges to the support of the measure, i.e., to the exact reach set in these sense of a Hausdorff distance.", {}),
    ("p0006-b004", T, ("p0006-b004",),
     r"- For fixed $d$ and $n \rightarrow \infty$, the empirical Christoffel function converges uniformly to the Christoffel function.", {}),
    ("p0006-b005", T, ("p0006-b005",),
     r"- For fixed $d$ and $n \rightarrow \infty$, the border of the empirical Christoffel polynomial converges to the border of the Christoffel polynomial in these sense of a Hausdorff distance.", {}),
    ("p0006-b006", T, ("p0006-b006",),
     r"In consequence, we can informally expect that for a large enough degree $d$ and large enough sample size $N$, the sublevel sets of the Christoffel polynomial are close enough to the reachable set.", {}),
    ("p0006-b007", T, ("p0006-b007",),
     r"We will use the following running example throughout the paper to illustrate the different concepts.", {}),
    ("p0006-b008", T, ("p0006-b008",),
     r"**Example 1 (Four squares)** Let the transition function $f : \mathbb{R}^2 \rightarrow \mathbb{R}^2$ be", {}),
    ("p0006-b009", T, ("p0006-b009",),
     D(r"f(x,y) = (1 + sign(x) \cdot x^2, 1 + sign(y) \cdot y^2)"), {}),
    ("p0006-b010", T, ("p0006-b010",),
     r"and let the initial set be $\mathcal{I} = [-1,1]^2$. The reachable set consists of four squares, i.e.,", {}),
    ("p0006-b011", T, ("p0006-b011",),
     D(r"\mathcal{S} = [-3,-1]^2 \cup [-3,-1] \times [1,3] \cup [1,3] \times [-3,-1] \cup [1,3]^2."), {}),
    ("p0006-b012", T, ("p0006-b012",),
     r"Figure 1 shows the reach set approximation given by (6), for a sample of size $N = 10000$ and different degrees $d$. The caption includes the corresponding uncertainty bound $\varepsilon$ for confidence $1-\delta = 0.99$ obtained by Conjecture 1.", {}),
    ("p0006-b013", T, ("p0006-b013",),
     r"We observe that, as intended by construction, all samples are included in $\hat{S}$. For increasing degrees, $\hat{S}$ becomes more precise. However, the uncertainty in the covered probability mass $\epsilon$, increases substantially. Indeed, the bound $\epsilon$ seems rather conservative since, in all instances, $\hat{S}$ covers nearly 100% of $S$.", {}),
    ("p0006-b014", "heading", ("p0006-b014",), "## 3. Reach Set Approximation with Conformal Prediction", {}),
    ("p0006-b015", T, ("p0006-b015",),
     r"Following the reasoning of Section 2, we can expect a sublevel of the Christoffel polynomial to converge to the support of the distribution. Intuitively, the Christoffel polynomial takes high values where the density is low and low values where the density is high, which makes it a good candidate for a nonconformity function.", {}),
    ("p0006-b016", T, ("p0006-b016",),
     r"In this section, we briefly recall relevant results from conformal prediction and instantiate them to the special case of estimating the support of distribution, which in our setting is equivalent to approximating the reach set $\mathcal{S}$.", {}),
    ("p0006-b017", "omit", ("p0006-b017",), "", {"reason": pageno(6)}),
])
