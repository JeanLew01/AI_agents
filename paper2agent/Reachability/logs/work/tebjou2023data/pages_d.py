#!/usr/bin/env python3
"""Pages 11-14 of tebjou2023data (PMLR v204 PDF). Run: python3 pages_d.py"""
from lib import page, HDR_ODD, HDR_EVEN, pageno

T = "text"
LX = r"\Lambda^{-1}_{\hat{\mu}_x, d}"
LH = r"\Lambda^{-1}_{\hat{\mu}, d}"
BX = r"\boldsymbol{x}"
BINOM = r"\binom{N-p}{i} \epsilon^i (1-\epsilon)^{N-p-i}"
CIN = r"C_{\mathcal{D}_{inliers}}^{\frac{p+1}{N-m}}"
CD = r"C_{\mathcal{D}}^{\frac{p+1}{N}}"


def D(s):
    return "$$\n" + s.strip() + "\n$$"


# ---------------------------------------------------------------- page 11
page(11, r"""
Compared with the 170 dpi render of PDF page 11, a 200 dpi crop of Figure 3 with margins, a 230 dpi crop of the
rest of the page, and the TeX source. Running header and page number omitted. Figure 3: the extractor's three
panel crops and a 'picture text' crop of the sub-captions are replaced by one figure item containing the
three panels, their tick labels and the printed sub-captions '(a) d = 6, eps = 0.02', '(b) d = 10, eps =
0.02', '(c) d = 15, eps = 0.02' (edges checked); the sub-captions are repeated as the first line of the
caption item, followed by the caption verbatim. The italic paragraph below the figure is the second half of
Example 2, begun on page 9 ('... the degree of the empirical | Christoffel polynomial d.'); it carries
join_previous: space and the reading order puts it directly after the page-9 item, with Figures 2 and 3 after
the completed example. The example ends with '... is greater than 99%.' (end of the example environment in the
TeX source), directly before the heading of Section 3.2. Kept as printed: 'the coverage error eps will be
lower than eps <= 0.02', 'we repeated this experiment 1000 times', 'how many of these 10000 samples', 'In only
6 experiments'. '3.2. Avoiding the Calibration Set' is a level-3 heading. 'transductive conformal prediction'
is underlined in the PDF (\emph, broken 'trans-ductive' at the line end; the TeX source has a discretionary
hyphen) and is written in italics, followed by the citation 'Vovk (2013)' without parentheses around the whole
citation, as printed. Kept as printed: 'we circumvent split between', 'a new non conformity is modulated',
'Let the training set be D = {...} be N i.i.d samples'. Mathematics from the TeX source, checked on the crop:
D_x = D union {x} with an italic (non-bold) subscript x, the empirical measure mu-hat_x, the moment matrix
M-hat_x, the nonconformity function r(x) = Lambda^{-1}_{mu-hat_x, d}(x) = v_d(x)^T M-hat_x^{-1} v_d(x), and the
p-value display (unnumbered) in which both Christoffel polynomials carry the subscript mu-hat_x. Both displays
replace extractor formula images. The page ends with the p-value display; the sentence that follows on page 12
('In particular, ...') starts a new item there.
""", [
    ("p0011-b000", "omit", ("p0011-b000",), "", {"reason": HDR_ODD}),
    ("p0011-fig3", "figure", [86.0, 85.0, 527.0, 205.0], "", {"label": "Figure 3", "asset_name": "figure-3"}),
    ("p0011-b005", "caption", ("p0011-b005",),
     r"(a) $d = 6$, $\varepsilon = 0.02$ (b) $d = 10$, $\varepsilon = 0.02$ (c) $d = 15$, $\varepsilon = 0.02$"
     "\n\n"
     r"Figure 3: Reach set approximations (outlined in purple) from Example 2, with a reduced sample size of $M = 1000$, of which $N = 200$ are used as a calibration set.", {}),
    ("p0011-b006", T, ("p0011-b006",),
     r"Christoffel polynomial $d$. It only depends on the confidence parameter $\delta$ and the size $N$ of the calibration set. Figure 3 shows the same result for $M = 1000$ samples, of which $N = 200$ samples were utilized as a calibration set. Here, the coverage error $\epsilon$ will be lower than $\epsilon \leq 0.02$. To empirically verify the theoretical guarantees obtained in Theorem 4, we repeated this experiment 1000 times. The empirical error was computed by checking how many of these 10000 samples were not contained in the approximated reachable set. In only $6$ experiments, the coverage error exceeded $\epsilon = 0.02$, confirming that the confidence $1-\delta$ is greater than 99%.",
     {"join_previous": "space"}),
    ("p0011-b007", "heading", ("p0011-b007",), "### 3.2. Avoiding the Calibration Set", {}),
    ("p0011-b008", T, ("p0011-b008",),
     r"In this section, we circumvent split between training and calibration sets by using *transductive conformal prediction* Vovk (2013). Transductive conformal prediction is a method used to construct prediction regions for a new data point without relying on a separate training set or calibration set. The calibration set is taken to be the entire training set plus the point at which the function is evaluated, in other words a new non conformity is modulated by the data point. The statistical guarantees of the previous section, and in particular of Theorem 4, hold also for this choice of nonconformity function, with $\mathcal{D}_{\mathrm{cal}} := \mathcal{D}$. This approach allows us to use all the available sample points from the measure $\mu$ to train the Christoffel function and compute the conformal region, but at the price of higher computational cost, as will be discussed below.", {}),
    ("p0011-b009", T, ("p0011-b009",),
     r"Let the training set be $\mathcal{D} = \{ " + BX + r"^1, " + BX + r"^2, ..., " + BX + r"^N \}$ be $N$ i.i.d samples from the probability distribution $\mu$. To compute the p-value at any point $" + BX + r" \in \mathbb{R}^n$, we add $" + BX + r"$ to the set $\mathcal{D}$ before computing the empirical Christoffel polynomial. Let $\mathcal{D}_x = \mathcal{D} \cup \{ " + BX + r" \}$, let the empirical measure for $\mathcal{D}_x$ be $\hat{\mu}_x$, and let $\widehat{\mathbf{M}}_x$ be its moment matrix. Using $\mathcal{D}_x$ in the empirical Christoffel polynomial, we get the nonconformity function", {}),
    ("p0011-b010", T, ("p0011-b010",),
     D(r"r(" + BX + r") = " + LX + r"(" + BX + r") = \mathbf{v}_{d}(" + BX + r")^T \widehat{\mathbf{M}}_x^{-1} \mathbf{v}_{d}(" + BX + r")."), {}),
    ("p0011-b011", T, [90.0, 664.0, 523.0, 687.5],
     r"We now have to evaluate a different empirical Christoffel polynomial each time we evaluate the p-value", {}),
    ("p0011-b012", T, [200.0, 688.0, 412.0, 716.0],
     D(r"p_{value}(" + BX + r") = \tfrac{1}{N} \left| \bigl\{ i \bigm| " + LX + r"(" + BX + r"^{i}) \geq " + LX + r"(" + BX + r") \bigr\} \right|"), {}),
    ("p0011-b013", "omit", ("p0011-b013",), "", {"reason": pageno(11)}),
])

# ---------------------------------------------------------------- page 12
page(12, r"""
Compared with the 170 dpi render of PDF page 12, a 200 dpi crop of Figure 4 with margins, a 240 dpi crop of the
text block, and the TeX source. Running header and page number omitted. Figure 4 (single panel, no
sub-caption) is printed at the top of the page; its crop includes the axis tick labels and the axis labels x
and y (edges checked). The figure belongs to Example 3 and is placed, with its caption, directly after the
text of Example 3 instead of between the p-value display of page 11 and its continuation 'In particular,
...'. Equation (13) (two identities separated by \quad, printed number (13)) was taken from the TeX source and
checked on the 240 dpi crop: the first identity is Lambda^{-1}_{mu-hat_x,d}(x) =
Lambda^{-1}_{mu-hat,d}(x) / (1 + Lambda^{-1}_{mu-hat,d}(x)); the second subtracts (v_d(x)^T y^i)^2 /
(1 + Lambda^{-1}_{mu-hat,d}(x)) from Lambda^{-1}_{mu-hat,d}(x^i); the transpose in the numerator is printed
with the small \intercal sign and the display ends with a comma. The inline formulas of the two paragraphs
around (13) (complexities O(s(d)^3), O(N s(d)^2), O(N s(d)), O(s(d)), O(N s(d) + s(d)^2); y^i = M-hat_d^{-1}
v_d(x^i)) were checked on the crop; the extractor had turned them into superscript soup. Kept as printed:
'The reduces the cost of evaluating' (authors' slip for 'This reduces'), 'Sherman-Morrison'. Example 3: header
'Example 3' in bold, body italic in the PDF (not reproduced); the example is the single paragraph ending
'... with confidence 1 - delta = 0.99.', directly before the heading of Section 4. Kept as printed: 'example
1' in lower case, 'M = N = 1000', 'degree 15', '0.45%'. Line-wrap hyphen 'ob-tained' removed. '4. Robustness
to Outliers' is a level-2 heading; 'real-life' is a printed compound hyphen. The last sentence of the page
continues on page 13 ('... theoretical guarantees obtained | using conformal prediction theory'); joined there.
""", [
    ("p0012-b000", "omit", ("p0012-b000",), "", {"reason": HDR_EVEN}),
    ("p0012-b003", T, ("p0012-b003",),
     r"In particular, we need to compute a new moment matrix and invert it for each evaluation. This is computationally expensive, on the order of $\mathcal{O}(s(d)^3)$. To avoid this, we compute the inverse moment matrix of the set $\mathcal{D}_x$ incrementally using the Sherman-Morrison formula, as proposed by Ducharlet et al. (2022). This allows us to replace the evaluation of $" + LX + r"(" + BX + r")$, which depends on $" + BX + r"$, with evaluations of the original Christoffel polynomial $" + LH + r"(" + BX + r")$, plus one additional product:", {}),
    ("p0012-b004", T, ("p0012-b004",),
     D(LX + r"(" + BX + r") = \frac{" + LH + r"(" + BX + r")}{1 + " + LH + r"(" + BX + r")}, \quad "
       + LX + r"(" + BX + r"^{i}) = " + LH + r"(" + BX + r"^{i}) - \frac{\bigl( \mathbf{v}_{d}(" + BX + r")^{\intercal} \boldsymbol{y}^{i} \bigr)^2}{1 + " + LH + r"(" + BX + r")}, \tag{13}"), {}),
    ("p0012-b005", T, ("p0012-b005",),
     r"where $\boldsymbol{y}^{i} = \widehat{\mathbf{M}}_d^{-1} \mathbf{v}_{d}(" + BX + r"^{i})$ are vectors that can be precomputed. The cost of precomputing $" + LH + r"(" + BX + r"^{i})$ and the vectors $\boldsymbol{y}^{i}$ is $\mathcal{O}(N s(d)^2)$, with storage requirements $\mathcal{O}(N s(d))$. The reduces the cost of evaluating $" + LX + r"(" + BX + r"^{i})$ for a given $" + BX + r"$ to $\mathcal{O}(s(d))$. The resulting cost of evaluating $p_{value}(" + BX + r")$ is $\mathcal{O}(N s(d) + s(d)^2)$.", {}),
    ("p0012-b006", T, ("p0012-b006",),
     r"**Example 3** Building on example 1, Figure 4 shows the reachable set approximation obtained using transductive conformal prediction with a Christoffel function of degree 15. In this case, we use the same $M = N = 1000$ sample points to train the Christoffel function and compute the set approximation. The guarantees provided by Theorem 4 assert that, using a training set of 1000 samples, the coverage error is below 0.45% with confidence $1-\delta = 0.99$.", {}),
    ("p0012-fig4", "figure", [210.0, 90.0, 400.0, 226.0], "", {"label": "Figure 4", "asset_name": "figure-4"}),
    ("p0012-b002", "caption", ("p0012-b002",),
     r"Figure 4: Reach set approximation of example 1 using the transductive conformal prediction and a Christoffel polynomial of degree $d = 15$, which avoids the split into training and calibration sets.", {}),
    ("p0012-b007", "heading", ("p0012-b007",), "## 4. Robustness to Outliers", {}),
    ("p0012-b008", T, ("p0012-b008",),
     r"In this section, we address the presence of outliers in the data set. As data may not be very abundant in real-life applications, one may have to work with a calibration set containing outliers without knowing which data point is an outlier and which one isn’t. The presence of outliers in the training set does not affect the theoretical guarantees obtained", {}),
    ("p0012-b009", "omit", ("p0012-b009",), "", {"reason": pageno(12)}),
])

# ---------------------------------------------------------------- page 13
page(13, r"""
Compared with the 170 dpi render of PDF page 13, two 240 dpi crops covering the whole text block, and the TeX
source. Running header and page number omitted. The first item completes the sentence begun on page 12
(join_previous: space). Theorem 5: header 'Theorem 5' in bold without punctuation, body italic in the PDF (not
reproduced); the body ends with display (14), as in the TeX theorem environment; the sentence 'This bound is
tight ...' that follows is upright and outside the theorem. Display (14) was taken from the TeX source and
checked on the crop: the conformal region has level (p+1)/N and subscript D, the sum runs from i = p+1 to
N-p, the binomial coefficient is binom(N-p, i) (text-style \tbinom in the source, written \binom) and the
summand is eps^i (1-eps)^(N-p-i); there is no punctuation after (14). Proof: the TeX source uses forced line
breaks; the proof is split into items at these breaks ('For eps in (0,1) let ...', 'Let x be an i.i.d
vector ...'). The aligned two-line display (unnumbered) and the two further displays were checked on the
crops; the extractor had merged the last display with the following line 'Since ... which leads us to (14).'
into one formula image; that line is restored as text. The proof ends with a filled square (\blacksquare).
Kept as printed (authors' slips, not conversion errors): the subscripts 'inlier', 'oulier' (sic), 'outlier'
and later 'inliers' for the same sets; 'N - p random variable V_i, ..., V_{N-p}' (first index i); 'we get :'
with a space before the colon; 'i.i.d vector'; and the reference 'Table 4' in the last paragraph, which points
to the table printed as Table 1 on page 14 (the paper has only Tables 1 and 2). Percentages are written
outside math mode. The three i.i.d. signs are a tilde with 'i.i.d.' stacked above it. Cross-references as
printed: (14), (10), Theorem 2, Theorem 5 (14), Theorem 4 (10).
""", [
    ("p0013-b000", "omit", ("p0013-b000",), "", {"reason": HDR_ODD}),
    ("p0013-b001", T, ("p0013-b001",),
     r"using conformal prediction theory, though it will affect the tightness of the approximated reachable set. On the other hand, the presence of outliers in the calibration set will impact those guarantees.",
     {"join_previous": "space"}),
    ("p0013-b002", T, ("p0013-b002",),
     r"The following theorem provides PAC guarantees on the reach set approximation even with outliers in the calibration set. Under the assumption that no more than $p$ outliers are in the calibration set $\mathcal{D}$, the confidence in the result depends on $\epsilon$, $p$, and the size of the calibration set $N$.", {}),
    ("p0013-b003", T, ("p0013-b003",),
     r"**Theorem 5** Consider a set of points $\mathcal{D} = \{ " + BX + r"^1, " + BX + r"^2, ..., " + BX + r"^N \}$ containing no more than $p$ outliers, with $2p+1 < N$, and where the rest of samples are i.i.d from a probability measure $\mu$. Then for any i.i.d vector $" + BX + r"$ sampled from $\mu$ and $\epsilon \in (0,1)$,", {}),
    ("p0013-b004", T, ("p0013-b004",),
     D(r"\mathbb{P}\biggl( \mu\Bigl( " + CD + r" \Bigr) \geq 1-\epsilon \biggr) \geq \sum_{i=p+1}^{N-p} " + BINOM + r" \tag{14}"), {}),
    ("p0013-b005", T, [90.0, 285.0, 523.0, 312.0],
     r"This bound is tight in the sense that for $p = 0$, (14) is identical to the case without outliers, i.e., we obtain (10).", {}),
    ("p0013-b005b", T, [90.0, 312.5, 523.0, 340.0],
     r"**Proof** Let $\mathcal{D} = \mathcal{D}_{inlier} \cup \mathcal{D}_{oulier}$, with $m \leq p$ being the unknown real size of $\mathcal{D}_{outlier}$. Let $U_1, \ldots, U_{N-m} \stackrel{\text{i.i.d.}}{\sim} \operatorname{Unif}([0,1])$, with order statistics $U_{(1)} \leq U_{(2)} \leq \ldots \leq U_{(N-m)}$.", {}),
    ("p0013-b005c", T, [90.0, 340.5, 523.0, 354.0],
     r"For $\epsilon \in (0,1)$ let $b_1 = ... = b_{p+1} = \epsilon$ and $b_{p+2} = ... = b_{N-p} = ... = b_{N-m} = 1$. Then $\forall m \leq p$:", {}),
    ("p0013-b006", T, ("p0013-b006",),
     D(r"\begin{aligned}" "\n"
       r"\mathbb{P}\left[ U_{(1)} \leq b_1, \ldots, U_{(N-m)} \leq b_{N-m} \right] & \geq \mathbb{P}\left[ U_{(1)} \leq b_1, \ldots, U_{(N-p)} \leq b_{N-p} \right] \\" "\n"
       r"& \geq \sum_{i=p+1}^{N-p} " + BINOM + "." "\n"
       r"\end{aligned}"), {}),
    ("p0013-b007", T, [90.0, 423.0, 523.0, 478.5],
     r"The above result is obtained by the following reasoning: let $0 < i \leq N-p$, if we have $N-p$ random variable $V_i, \ldots, V_{N-p} \stackrel{\text{i.i.d.}}{\sim} \operatorname{Unif}([0,1])$ the probability to have exactly $i$ of them below $\epsilon$ is equal to $" + BINOM + r"$, therefore, the probability of having at least $p+1$ of them below $\epsilon$ is equal to $\sum_{i=p+1}^{N-p} " + BINOM + r".$", {}),
    ("p0013-b007b", T, [90.0, 479.0, 523.0, 493.0],
     r"Let $" + BX + r"$ be an i.i.d vector sampled from $\mu$. By definition,", {}),
    ("p0013-b008", T, ("p0013-b008",),
     D(r"\mu\Bigl( " + CIN + r" \Bigr) = \mathbb{P}\Bigl( " + BX + r" \in " + CIN + r" \Bigm| \mathcal{D}_{inliers} \Bigr)."), {}),
    ("p0013-b009", T, ("p0013-b009",), r"Using Theorem 2, we get :", {}),
    ("p0013-b010", T, [150.0, 545.0, 465.0, 592.0],
     D(r"\mathbb{P}\biggl( \mu\Bigl( " + CIN + r" \Bigr) \geq 1-\epsilon \biggr) \geq \sum_{i=p+1}^{N-p} " + BINOM), {}),
    ("p0013-b010b", T, [90.0, 593.0, 523.0, 622.0],
     r"Since $" + CIN + r" \subseteq " + CD + r"$, we have $\mu\Bigl( " + CD + r" \Bigr) \geq \mu\Bigl( " + CIN + r" \Bigr)$, which leads us to (14). $\blacksquare$", {}),
    ("p0013-b011", T, ("p0013-b011",),
     r"Note that the bound in Theorem 5 (14) is tight in the sense that for $p = 0$ we obtain the same lower bound as in Theorem 4 (10). Table 4 shows the confidence bound of (14) for different values of the calibration set size and the approximation uncertainty $\epsilon$ under the assumption that no more than 5% of the calibration set are outliers. We observe that the confidence rapidly approaches 100% when the admissible coverage error is above the ratio of outliers; it rapidly drops to 0% when it is below.", {}),
    ("p0013-b012", "omit", ("p0013-b012",), "", {"reason": pageno(13)}),
])

# ---------------------------------------------------------------- page 14
page(14, r"""
Compared with the 170 dpi render of PDF page 14, a 170 dpi crop of Table 1 and Figure 5 with margins, and the
TeX source. Running header and page number omitted. Table 1 (caption printed above the table) is a table item
with rows as strings; every cell was compared with the crop: sizes 100, 500, 1000, 2000; columns eps = 4%, 5%,
6%, 10%; values 33/51/68/96, 10/42/77/99.99, 3/37/84/99.99, 0.4/31/92/99.99. The printed header 'confidence in
%' spans the four eps columns; in the CSV it is repeated as a prefix of each of the four column names. The
extractor had split the header ('confide|ince in %'). The caption has no final period, as printed. Example 4:
header 'Example 4' in bold, body italic in the PDF (not reproduced); the example is one paragraph ending
'... the theoretical guarantee of 98.9% confidence.' (in the TeX source Figure 5 is declared inside the
example). Kept as printed: 'on example 1' in lower case, 'the coverage error eps = 0.15 with a confidence =
98.9%', 'i.i.d. samples' with periods here. Percentages are written outside math mode. Figure 5 (single panel,
no sub-caption) is printed between Table 1 and Example 4; its crop includes the tick labels (edges checked;
the plot has no axis labels) and it is placed, with its caption, after the text of Example 4. '5. Experiments'
is a level-2 heading; 'non-conformity' is hyphenated at the line end and in the TeX source. Algorithm 2, which
belongs to Section 4, is printed at the top of page 15, after the heading and first sentence of Section 5; the
reading order places it before the heading '5. Experiments'. The reference 'Table 4' on page 13 points to
this Table 1.
""", [
    ("p0014-b000", "omit", ("p0014-b000",), "", {"reason": HDR_EVEN}),
    ("p0014-b001", "caption", ("p0014-b001",),
     r"Table 1: The confidence bound of (14) for different sizes $N$ of the calibration set and the desired coverage error $\epsilon$ for a calibration set with 5% outliers or less", {}),
    ("p0014-tab1", "table", [188.0, 152.0, 424.0, 257.0], "",
     {"label": "Table 1", "asset_name": "table-1",
      "rows": [
          ["size N", "confidence in %: ϵ = 4%", "confidence in %: ϵ = 5%", "confidence in %: ϵ = 6%", "confidence in %: ϵ = 10%"],
          ["100", "33", "51", "68", "96"],
          ["500", "10", "42", "77", "99.99"],
          ["1000", "3", "37", "84", "99.99"],
          ["2000", "0.4", "31", "92", "99.99"],
      ]}),
    ("p0014-b005", T, ("p0014-b005",),
     r"**Example 4** To evaluate the performance of Algorithm 2 on example 1, we construct a data set from $M = 1500$ samples of the reach set and substitute 10% with outliers, i.e., i.i.d. samples outside the reachable set. We use a calibration set of size $N = 500$, and the rest of the samples are used as a training set to compute the empirical Christoffel polynomial. Figure 5 shows the resulting approximation. With Theorem 5, the coverage error $\epsilon = 0.15$ with a confidence = 98.9%. To empirically confirm these bounds, as in Example 2, we repeat the experiment 1000 times with different samples. For each experiment, we take 10000 samples of the reach set in order to compute the empirical coverage error. None of the experiments resulted in an empirical coverage error above 15%, which is consistent with the theoretical guarantee of 98.9% confidence.", {}),
    ("p0014-fig5", "figure", [215.0, 262.0, 400.0, 384.0], "", {"label": "Figure 5", "asset_name": "figure-5"}),
    ("p0014-b004", "caption", ("p0014-b004",),
     r"Figure 5: An approximation of the reach set of example 1 (purple outline) obtained with Algorithm 2 using a Christoffel polynomial of degree 15, on a data set with 10% outliers. The training set is shown in black, the calibration set in red.", {}),
    ("p0014-b006", "heading", ("p0014-b006",), "## 5. Experiments", {}),
    ("p0014-b007", T, ("p0014-b007",),
     r"We now turn our focus to the suitability of the empirical Christoffel polynomial as a non-conformity function.", {}),
    ("p0014-b008", "omit", ("p0014-b008",), "", {"reason": pageno(14)}),
])
