#!/usr/bin/env python3
"""Pages 15-20 of tebjou2023data (PMLR v204 PDF). Run: python3 pages_e.py"""
from lib import page, HDR_ODD, HDR_EVEN, pageno

T = "text"
XI = r"\boldsymbol{x^{(i)}}"
MINV = r"\widehat{\mathbf{M}}^{-1}_d"


def D(s):
    return "$$\n" + s.strip() + "\n$$"


# ---------------------------------------------------------------- page 15
ALG2 = "\n\n".join([
    r"**Algorithm 2:** Reachability analysis with outliers",
    r"**Input:** Transition function $f$; initial set $\mathcal{I} \subset \mathbb{R}^n$; Christoffel function order $d$, $N$ the size of the calibration set and $p$ the upper bound number of outliers in the calibration; $M$ the total number of simulations with $M > N$ and an i.i.d data sample $\mathcal{D} = \{\boldsymbol{x}^{(i)} \ \}$ for $i \in \{1,...,M\}$. The sample $" + XI + r"$ is an *inlier* if $" + XI + r" \in f(\mathcal{I})$ and an *outlier* otherwise. .",
    r"**Output:** Set $\hat{\mathcal{S}}$ representing an $\epsilon$-accurate approximation of the true reachable set $\mathcal{S}$ with confidence $\sum_{i=p+1}^{N-p} \binom{N-p}{i} \epsilon^i (1-\epsilon)^{N-p-i}$",
    r"1. Compute the empirical moment matrix with the associated Christoffel degree $d$ using $M-N$ samples: $\widehat{\mathbf{M}}_d = \frac{1}{M-N} \sum_{i=N+1}^{M} \mathbf{v}_{d}\left(" + XI + r"\right) \mathbf{v}_{d}\left(" + XI + r"\right)^{\top}$",
    r"2. Use a calibration set of $N$ samples: $\mathcal{D}_{\mathrm{cal}} = \{ " + XI + r" \mid i \in \{1,..,N\}\}$ and:",
    r"&emsp;&emsp;(a) Compute the scores: $\text{score}_i = \mathbf{v}_{d}(" + XI + r")^{\top} " + MINV + r" \mathbf{v}_{d}(" + XI + r")$ for $i = 1, \ldots, N$",
    r"&emsp;&emsp;(b) Sort the scores in descending order such that: $\text{score}_1 \geq \text{score}_2 \geq ... \geq \text{score}_N$",
    r"&emsp;&emsp;(c) Set the conformal region $C_{\mathcal{D}}^{\frac{p+1}{N}}$ as $\hat{\mathcal{S}} = \left\{ \boldsymbol{x} \in \mathbb{R}^{n} : \mathbf{v}_{d}(\boldsymbol{x})^{\top} " + MINV + r" \mathbf{v}_{d}(\boldsymbol{x}) \leq \text{score}_{p+1} \right\}$",
])

page(15, r"""
Compared with the 170 dpi render of PDF page 15, a 240 dpi crop of Algorithm 2, and the TeX source. Running
header and page number omitted. Algorithm 2: the extractor had split the box into eight damaged text items;
it is replaced by one image crop of the whole box (top rule to bottom rule, edges checked) and a text
transcription taken from the TeX algorithm2e environment and checked line by line on the crop: title, Input,
Output, steps 1 and 2 and sub-steps (a)-(c). Kept as printed (authors' slips, not conversion errors): the
input is described as a transition function and an initial set although the steps only use the data sample;
'the upper bound number of outliers in the calibration'; 'D = {x^(i) }' with a space before the closing brace;
the sample is printed x^(i) with a bold superscript after its first occurrence; the Input paragraph ends with
'otherwise. .' (two periods); '{1,..,N}' with two dots in step 2; the conformal region in step (c) has
subscript D (not D_cal). As printed: the moment matrix is normalised by 1/(M-N) and summed over i = N+1..M;
scores are sorted in descending order and the threshold is score_{p+1}, the (p+1)-th largest calibration
score; the output confidence is the sum from i = p+1 to N-p of binom(N-p, i) eps^i (1-eps)^(N-p-i). 'inlier'
and 'outlier' are underlined in the PDF (\emph) and written in italics. Because the PDF text of the box lies
inside the image crop, the tool's number check lists the numbers of the transcription as extra. Algorithm 2
belongs to Section 4 but is printed here, after the heading and first sentence of Section 5 (page 14); the
reading order places it at the end of Section 4. '5.1. Empirical False Positive Rate' is a level-3 heading.
Prose of Section 5.1 compared line by line with the PDF text and the TeX source: 'example 2' in lower case,
'(Liu et al., 2008)' in parentheses, '10,000' with a comma, 'from the Figure 6' as printed. Line-wrap
hyphens removed: 'ap-proximation', 'Ta-ble'; printed compound hyphens kept: 'one-class', 'false-positive',
'non-conformity' (twice in the last paragraph; 'nonconformity' in the second paragraph, as printed). The
last sentence continues on page 16 below Table 2 and Figure 6 ('... under the presence of outliers | in the
training set.'); joined there in the reading order.
""", [
    ("p0015-b000", "omit", ("p0015-b000",), "", {"reason": HDR_ODD}),
    ("p0015-alg2", "figure", [86.0, 91.0, 527.0, 346.0], "", {"label": "Algorithm 2", "asset_name": "algorithm-2"}),
    ("p0015-alg2-text", T, [90.0, 94.0, 522.0, 342.0], ALG2, {}),
    ("p0015-b009", "heading", ("p0015-b009",), "### 5.1. Empirical False Positive Rate", {}),
    ("p0015-b010", T, ("p0015-b010",),
     r"We start by examining the tightness of the reachable set approximation in example 2 through the empirical measurement of false positives.", {}),
    ("p0015-b011", T, ("p0015-b011",),
     r"We compare the empirical Christoffel polynomial with other prevalent nonconformity functions: one-class SVM, Isolation Forest (Liu et al., 2008), and Local Outlier Factor (LOF), as shown in Figure 6. Only the approximation using LOF seems comparable to that of the Christoffel polynomial, while Isolation Forest exhibits significant variability depending on the random seed.", {}),
    ("p0015-b012", T, ("p0015-b012",),
     r"To gauge the number of false positives and assess the accuracy of the reachable set approximation, we generated 10,000 uniformly distributed samples within the domain $[-4, 4]^2$. The false-positive rate was empirically determined for various degrees $d$, as shown in Table 2. As observed in earlier plots, a higher degree results in a more accurate fit of the reachable set. The false-positive rates for the other algorithms can also be observed in Table 2 for varying sizes of the training and calibration sets. Consistent with the findings from the Figure 6, only the LOF provides results that are comparable in quality to those obtained using the Christoffel polynomial.", {}),
    ("p0015-b013", T, ("p0015-b013",),
     r"To further demonstrate the effectiveness of the empirical Christoffel polynomial as a non-conformity function, we examine its robustness in the presence of outliers within the training set. Although the theoretical guarantees discussed in this article and in general conformal prediction hold for any choice of non-conformity function, even with outliers in the training set, the presence of these outliers can impact the accuracy of the model. To compare the empirical Christoffel polynomial with LOF, we conducted two experiments. In the first experiment, we considered the region $[-1,1]^2$ as the reachable set to approximate. We focused on comparing the performance of the algorithms under the presence of outliers", {}),
    ("p0015-b014", "omit", ("p0015-b014",), "", {"reason": pageno(15)}),
])

# ---------------------------------------------------------------- page 16
CH = "Christoffel with d = "
page(16, r"""
Compared with the 170 dpi render of PDF page 16, a 170 dpi crop of Table 2 and Figure 6 with margins, and the
TeX source. Running header and page number omitted. Table 2 (caption printed above the table; the extractor's
list marker before 'Table 2:' removed) is a table item with rows as strings; all 15 data rows were compared
cell by cell with the crop and with the PDF text lines. Header cells are written in plain characters: |D|,
|D_train|, |D_cal| (printed calligraphic D with roman subscripts), 'ϵ in %', 'FP%'. The columns |D|,
|D_train|, |D_cal| are printed only in the first row of each block (10000 / 8000 / 2000 and 1000 / 800 / 200)
and in the last row (1000 / 1000 / 1000); the rows below carry either nothing or vertical dots, which
are printed across the rows 'Christoffel with d = 18' and 'LOF score' of each block (two \vdots multirows in
the TeX source). The cells are transcribed as printed (empty, or a vertical-ellipsis character in those two
rows), not forward-filled; the meaning 'same as the first row of the block' is recorded in the conversion
notes. 'FP%' of the row 'Christoffel with d = 10' in the second block is printed '20' without a decimal. The
two-line note under the table is kept as a text item. Figure 6: the extractor's three panel crops, a
'picture text' crop and a text item for sub-caption (a) are replaced by one figure item containing the three
panels with their in-plot titles ('SVM', 'Isolation Forest'), axis labels, tick labels and the printed
sub-captions '(a) One-class SVM', '(b) Isolation Forest', '(c) LOF' (edges checked); the sub-captions are
repeated as the first line of the caption item, followed by the caption verbatim. The paragraph at the bottom
of the page continues the last sentence of page 15 (join_previous: space) and ends in the middle of a word at
the page break ('Figure 9 il-' | 'lustrates'); the item ends with 'il' and page 17 continues with
join_previous: none. Kept as printed: '1,200' with a comma; 'Figure 9' although the sentence describes what
Figures 7 and 8 show (hard-coded number in the TeX source). In the reading order Table 2 and Figure 6 are
placed after the third paragraph of Section 5.1 (page 15), which discusses them, so that they do not interrupt
the sentence that runs from page 15 to this page.
""", [
    ("p0016-b000", "omit", ("p0016-b000",), "", {"reason": HDR_EVEN}),
    ("p0016-b001", "caption", ("p0016-b001",),
     r"Table 2: Experimentally estimated false-positive rates for different algorithms applied to the reach set approximation of Example 1, with confidence $1-\delta =$ 99%", {}),
    ("p0016-tab2", "table", [134.0, 152.0, 474.0, 360.0], "",
     {"label": "Table 2", "asset_name": "table-2",
      "rows": [
          ["Nonconformity function", "|D|", "|D_train|", "|D_cal|", "ϵ in %", "FP%"],
          [CH + "6", "10000", "8000", "2000", "0.2", "49.5"],
          [CH + "10", "", "", "", "0.2", "39.5"],
          [CH + "15", "", "", "", "0.2", "11.7"],
          [CH + "18", "⋮", "⋮", "⋮", "0.2", "7.2"],
          ["LOF score", "⋮", "⋮", "⋮", "0.2", "3.4"],
          ["IsolationForest score", "", "", "", "0.2", "92.9"],
          ["Oneclass SVM score", "", "", "", "0.2", "65.7"],
          [CH + "6", "1000", "800", "200", "2.2", "44.6"],
          [CH + "10", "", "", "", "2.2", "20"],
          [CH + "15", "", "", "", "2.2", "12.7"],
          [CH + "18", "⋮", "⋮", "⋮", "2.2", "12.4"],
          ["LOF score", "⋮", "⋮", "⋮", "2.2", "10.6"],
          ["IsolationForest score", "", "", "", "2.2", "86.8"],
          ["Oneclass SVM score", "", "", "", "2.2", "60.7"],
          ["Transduct. Christ. with d = 15", "1000", "1000", "1000", "0.5", "46.6"],
      ]}),
    ("p0016-b003", T, ("p0016-b003",),
     r"$\epsilon$ = Coverage error, at least $1-\epsilon$ of the measure is covered; FP% = False positives in %, measured by uniform sampling of a sufficiently large bounding box and counting samples in $\hat{S} \setminus S$", {}),
    ("p0016-fig6", "figure", [88.0, 400.0, 527.0, 532.0], "", {"label": "Figure 6", "asset_name": "figure-6"}),
    ("p0016-b009", "caption", ("p0016-b009",),
     r"(a) One-class SVM (b) Isolation Forest (c) LOF"
     "\n\n"
     r"Figure 6: Reach set approximations (purple outline) of Example 1 using one-class SVM, Isolation Forest, and Local Outlier Factor (LOF) as nonconformity functions, for a common training set of size 800 (black dots) and calibration set of size 200 (red dots).", {}),
    ("p0016-b010", T, ("p0016-b010",),
     r"in the training set. We generated a training set of size 1,200 containing 200 outliers and a calibration set of size 200, all belonging to the reachable set. The second experiment was similar to the first one, with a star-shaped region as the reachable set. We generated a training set of size 900 containing 100 outliers and a calibration set of size 200. Figure 9 il",
     {"join_previous": "space"}),
    ("p0016-b011", "omit", ("p0016-b011",), "", {"reason": pageno(16)}),
])

# ---------------------------------------------------------------- page 17
page(17, r"""
Compared with the 170 dpi render of PDF page 17, two 170 dpi crops of Figures 7 and 8 with margins, and the
TeX source. Running header and page number omitted. Figures 7 and 8: for each figure the extractor's two panel
crops and a 'picture text' crop are replaced by one figure item containing both panels with axis labels, tick
labels and the printed sub-captions '(a) Christoffel polynomial' and '(b) LOF' (edges checked); the
sub-captions are repeated as the first line of the caption item, followed by the caption verbatim. Line-wrap
hyphens in the captions removed ('polyno-mial', 'differ-ences', 'en-countering'); 'star-shaped' is a printed
compound hyphen. The two prose fragments at the bottom of the page are (1) the end of the paragraph that runs
from page 15 over page 16 ('il-' | 'lustrates how ...', join_previous: none) and (2) a new paragraph 'Figures 7
and 8 display ...', which ends in the middle of a word at the page break ('situ-' | 'ations'); the item ends
with 'situ' and page 18 continues with join_previous: none. In the reading order both fragments come before
the two figures, and Figures 7 and 8 follow the completed paragraph 'Figures 7 and 8 display ... across both
experiments.' at the end of Section 5.1. No mathematics on this page except the interval [-1,1]^2 in the
caption of Figure 7.
""", [
    ("p0017-b000", "omit", ("p0017-b000",), "", {"reason": HDR_ODD}),
    ("p0017-fig7", "figure", [124.0, 85.0, 490.0, 244.0], "", {"label": "Figure 7", "asset_name": "figure-7"}),
    ("p0017-b004", "caption", ("p0017-b004",),
     r"(a) Christoffel polynomial (b) LOF"
     "\n\n"
     r"Figure 7: Comparison of reachable set approximations for the empirical Christoffel polynomial (degree 10) and LOF in the first experiment, with the region $[-1,1]^2$ as the target. The training set, containing outliers, is represented by black dots, while the calibration set is shown in red. The plot highlights the performance differences and robustness of both methods in the presence of outliers, demonstrating how the empirical Christoffel polynomial is far more robust.", {}),
    ("p0017-fig8", "figure", [124.0, 362.0, 490.0, 520.0], "", {"label": "Figure 8", "asset_name": "figure-8"}),
    ("p0017-b008", "caption", ("p0017-b008",),
     r"(a) Christoffel polynomial (b) LOF"
     "\n\n"
     r"Figure 8: A comparison of reach set approximation (purple outline) using the Christoffel polynomial with degree 15 and LOF for the second experiment, which targets a star-shaped region. Training set samples are in black and calibration set in red. This plot highlights the performance and robustness of both methods when encountering outliers in a complex geometric scenario, illustrating the effectiveness of the empirical Christoffel polynomial under the presence of outliers.", {}),
    ("p0017-b009", T, ("p0017-b009",),
     r"lustrates how the empirical Christoffel polynomial and LOF approximate the true reachable set in the presence of outliers.",
     {"join_previous": "none"}),
    ("p0017-b010", T, ("p0017-b010",),
     r"Figures 7 and 8 display the performance of both the empirical Christoffel polynomial and LOF in handling outliers within the training set across distinct and complex geometric situ", {}),
    ("p0017-b011", "omit", ("p0017-b011",), "", {"reason": pageno(17)}),
])

# ---------------------------------------------------------------- page 18
page(18, r"""
Compared with the 170 dpi render of PDF page 18, a 200 dpi crop of Figure 9 with margins, and the TeX source.
Running header and page number omitted. Figure 9: the extractor's three panel crops and a 'picture text' crop
are replaced by one figure item containing the three panels with axis labels, tick labels and the printed
sub-captions '(a) d = 6, eps = 0.002', '(b) d = 10, eps = 0.002', '(c) d = 15, eps = 0.002' (edges checked);
the sub-captions are repeated as the first line of the caption item, followed by the caption verbatim ('duffing
oscillator' in lower case as printed). The first prose item completes the word split at the page break
('situ-' | 'ations', join_previous: none) and ends Section 5.1. '5.2. Duffing oscillator' is a level-3
heading (the extractor had level 2) and '6. Conclusion' a level-2 heading. The Duffing equation is an
unnumbered display, taken from the TeX source and checked on the render: x-ddot = -delta x-dot + alpha x -
beta x^3 + gamma cos(omega t), with 'cos' printed in math italics. Parameters as printed: alpha = 1, beta = 1,
delta = 0.05, gamma = 0.4, omega = 1.3; initial set I = [-0.95, 1.05] x [-0.05, 0.05]. Figure 9 is printed at
the top of the page, inside the last paragraph of Section 5.1; the reading order places it at the end of
Section 5.2, after the paragraph that refers to it. Conclusion: line-wrap hyphens removed ('dy-namical',
'transduc-tive'); 'sample-efficient' is a printed compound hyphen; kept as printed: 'provides ... and
proposed', 'compared that the most relevant approaches'. The conclusion continues with a new paragraph on
page 19.
""", [
    ("p0018-b000", "omit", ("p0018-b000",), "", {"reason": HDR_EVEN}),
    ("p0018-fig9", "figure", [88.0, 84.0, 527.0, 201.0], "", {"label": "Figure 9", "asset_name": "figure-9"}),
    ("p0018-b005", "caption", ("p0018-b005",),
     r"(a) $d = 6$, $\varepsilon = 0.002$ (b) $d = 10$, $\varepsilon = 0.002$ (c) $d = 15$, $\varepsilon = 0.002$"
     "\n\n"
     r"Figure 9: Reach set approximation (purple outline) of the duffing oscillator using the Christoffel polynomial with the data set split into training (black) and calibration set (red), for different degrees $d$ of the Christoffel function, with corresponding coverage error $\varepsilon$ for confidence $1-\delta = 0.99$.", {}),
    ("p0018-b006", T, ("p0018-b006",),
     r"ations. When employed as a non-conformity function, the empirical Christoffel polynomial demonstrated greater robustness in the presence of outliers across both experiments.",
     {"join_previous": "none"}),
    ("p0018-b007", "heading", ("p0018-b007",), "### 5.2. Duffing oscillator", {}),
    ("p0018-b008", T, ("p0018-b008",),
     r"The Duffing oscillator is a nonlinear mathematical model that captures the behavior of a system that oscillates when subject to an external force. It has been used in a variety of physical systems, from mechanical vibrations to biological dynamics. The Duffing oscillator is described by the following nonlinear second-order differential equation:", {}),
    ("p0018-b009", T, ("p0018-b009",),
     D(r"\ddot{x} = -\delta \dot{x} + \alpha x - \beta x^3 + \gamma cos(\omega t)"), {}),
    ("p0018-b010", T, ("p0018-b010",),
     r"Similar to Devonport et al. (2021), we take $\alpha = 1$, $\beta = 1, \delta = 0.05, \gamma = 0.4$ and $\omega = 1.3$. We choose the initial set to be $\mathcal{I} = [-0.95, 1.05] \times [-0.05, 0.05]$. Figure 9 shows an approximation of the reach set, computed with the Christoffel function as nonconformity function for different degrees. We observe that for increasing degrees, the approximation is more precise and is able to recover holes. The results are comparable to those reported by Devonport et al. (2021), where no split into training and calibration sets was carried out.", {}),
    ("p0018-b011", "heading", ("p0018-b011",), "## 6. Conclusion", {}),
    ("p0018-b012", T, ("p0018-b012",),
     r"In this paper, we studied the mathematical reach set approximation in the analysis of dynamical systems based on conformal prediction. We consider for the first time the use of the Christoffel function as a nonconformity function, thanks to its attractive properties in set and density approximation. Our conformal prediction approach provides stronger and more sample-efficient guarantees on reach set approximation and proposed a version of reach set approximation that is robust to outliers, compared that the most relevant approaches in the literature. We exploited an incremental form of the Christoffel function for transductive conformal prediction that avoids splitting the data into training and calibration sets. Extensive illustrative numerical experiments show the effectiveness and the performance of our proposed approach and its associated algorithms.", {}),
    ("p0018-b013", "omit", ("p0018-b013",), "", {"reason": pageno(18)}),
])

# ---------------------------------------------------------------- page 19
page(19, r"""
Compared with the 170 dpi render of PDF page 19 and with the authors' main.bbl. Running header and page number
omitted. The first paragraph is the second (indented) paragraph of the Conclusion. 'Acknowledgments' and
'References' are unnumbered headings, written as level-2 headings. The quotation marks around 'France 2030'
are curly in the PDF and kept. References: the bibliography is unnumbered (author-year style, natbib); one
text item per entry, the extractor's list markers and '<u>' tags removed. Journal, book and proceedings titles
are underlined in the PDF (\emph with ulem) and written in italics. All nine entries of this page were read
against the page image (authors, title, venue, volume/pages, year, DOI/URL). Corrections of extraction damage:
'Cand`es' -> 'Candès'; in the Althoff entry the volume and pages are broken across lines ('4: | 369-395') and
are closed up to '4:369-395'; in the Djeumou entry the DOI is broken across lines ('10.1145/ |
3447928.3457355') and is closed up; line-wrap hyphens removed ('reach-ability' twice, 'predic-tion',
'reacha-bility'); printed compound hyphens kept ('Data-driven', 'cyber-physical', 'distribution-free',
'high-order', 'On-the-fly', 'F-16'). Kept as printed: lower-case 'odes', 'taylor', 'christoffel' in titles,
'Allgower' without umlaut, 'MIT press', the initials-only author list 'L Doyen, G Frehse, GJ Pappas, and A
Platzer', and 'HSCC ’21'. The two URLs are printed in typewriter type and kept as plain text.
""", [
    ("p0019-b000", "omit", ("p0019-b000",), "", {"reason": HDR_ODD}),
    ("p0019-b001", T, ("p0019-b001",),
     r"The theoretical results that we presented here in the context of reach set approximation are equally valid to approximate compact sets, or the support of probability distributions, in other application domains. Naturally, the computation of the Christoffel function is subject to numerical errors. The impact of such numerical issues will be studied in future work.", {}),
    ("p0019-b002", "heading", ("p0019-b002",), "## Acknowledgments", {}),
    ("p0019-b003", T, ("p0019-b003",),
     r"This work has been supported by the French government under the “France 2030” program as part of the SystemX Technological Research Institute. This work was conducted as part of the Confiance.AI program, which aims to develop innovative solutions for enhancing the reliability and trustworthiness of AI-based systems.", {}),
    ("p0019-b004", "heading", ("p0019-b004",), "## References", {}),
    ("p0019-b005", T, ("p0019-b005",),
     r"Amr Alanwar, Anne Koch, Frank Allgower, and Karl Henrik Johansson. Data-driven reachability analysis from noisy data. *IEEE Transactions on Automatic Control*, pages 1–16, 2023. doi: 10.1109/tac.2023.3257167.", {}),
    ("p0019-b006", T, ("p0019-b006",),
     r"Matthias Althoff, Goran Frehse, and Antoine Girard. Set propagation techniques for reachability analysis. *Annual Review of Control, Robotics, and Autonomous Systems*, 4:369–395, 2021.", {}),
    ("p0019-b007", T, ("p0019-b007",),
     r"Rajeev Alur. *Principles of cyber-physical systems*. MIT press, 2015.", {}),
    ("p0019-b008", T, ("p0019-b008",),
     r"Anastasios N. Angelopoulos and Stephen Bates. A gentle introduction to conformal prediction and distribution-free uncertainty quantification. *CoRR*, abs/2107.07511, 2021. URL https://arxiv.org/abs/2107.07511.", {}),
    ("p0019-b009", T, ("p0019-b009",),
     r"Stephen Bates, Emmanuel Candès, Lihua Lei, Yaniv Romano, and Matteo Sesia. Testing for outliers with conformal p-values. *The Annals of Statistics*, 51(1):149–178, 2023.", {}),
    ("p0019-b010", T, ("p0019-b010",),
     r"Martin Berz and Kyoko Makino. Verified integration of odes and flows using differential algebraic methods on high-order taylor models. *Reliable Computing*, 4(4):361–369, 1998. doi: 10.1023/A:1024467732637. URL https://doi.org/10.1023/A:1024467732637.", {}),
    ("p0019-b011", T, ("p0019-b011",),
     r"Alex Devonport, Forest Yang, Laurent El Ghaoui, and Murat Arcak. Data-driven reachability analysis with christoffel functions. In *2021 60th IEEE Conference on Decision and Control (CDC)*, pages 5067–5072, 2021. doi: 10.1109/CDC45484.2021.9682860.", {}),
    ("p0019-b012", T, ("p0019-b012",),
     r"Franck Djeumou, Aditya Zutshi, and Ufuk Topcu. On-the-fly, data-driven reachability analysis and control of unknown systems: An F-16 aircraft case study. In *Proceedings of the 24th International Conference on Hybrid Systems: Computation and Control*, HSCC ’21, New York, NY, USA, 2021. Association for Computing Machinery. doi: 10.1145/3447928.3457355.", {}),
    ("p0019-b013", T, ("p0019-b013",),
     r"L Doyen, G Frehse, GJ Pappas, and A Platzer. *Verification of Hybrid Systems*, chapter 28. Springer, 2018.", {}),
    ("p0019-b014", "omit", ("p0019-b014",), "", {"reason": pageno(19)}),
])

# ---------------------------------------------------------------- page 20
page(20, r"""
Compared with the 170 dpi render of PDF page 20 and with the authors' main.bbl. Running header and page number
omitted. The page contains the last ten bibliography entries (Ducharlet ... Vovk); the lower half of the page
is blank and the paper has no appendix. One text item per entry, list markers and '<u>' tags removed, venue
titles (underlined in the PDF) in italics. All ten entries were read against the page image. Corrections of
extraction damage: split diacritics restored ('K´evin' -> 'Kévin', 'Trav´e-Massuy`es' -> 'Travé-Massuyès',
'Marie-V´eronique' -> 'Marie-Véronique', 'Math´ematique' -> 'Mathématique'); 'barrier-certificatebased'
restored to 'barrier-certificate-based' (compound hyphen at a line end, confirmed in the .bbl); in the Prajna
entry the issue and pages are broken across lines ('42(1): | 117-126') and are closed up to '42(1):117-126';
line-wrap hyphen 'ap-plications' removed. Kept as printed: lower-case 'christoffel' and '2008 eighth ieee
international conference on data mining'; 'SAS’94'; the em dashes in 'Theory—Implementation—Applications';
'September 30–October 2, 2013, Proceedings 9'; the Ducharlet entry has no venue.
""", [
    ("p0020-b000", "omit", ("p0020-b000",), "", {"reason": HDR_EVEN}),
    ("p0020-b001", T, ("p0020-b001",),
     r"Kévin Ducharlet, Louise Travé-Massuyès, Jean-Bernard Lasserre, Marie-Véronique Le Lann, and Youssef Miloudi. Leveraging the Christoffel-Darboux kernel for online outlier detection, 2022.", {}),
    ("p0020-b002", T, ("p0020-b002",),
     r"Nicolas Halbwachs, Yann-Eric Proy, and Pascal Raymond. Verification of linear hybrid systems by means of convex approximations. In *International Static Analysis Symposium, SAS’94*, Namur (Belgium), September 1994.", {}),
    ("p0020-b003", T, ("p0020-b003",),
     r"Shuo Han, Ufuk Topcu, and George J. Pappas. A sublinear algorithm for barrier-certificate-based data-driven model validation of dynamical systems. In *2015 54th IEEE Conference on Decision and Control (CDC)*, pages 2049–2054, 2015. doi: 10.1109/CDC.2015.7402508.", {}),
    ("p0020-b004", T, ("p0020-b004",),
     r"Jean-Bernard Lasserre. On the Christoffel function and classification in data analysis. *Comptes Rendus. Mathématique*, 360:919–928, 2022. doi: 10.5802/crmath.358.", {}),
    ("p0020-b005", T, ("p0020-b005",),
     r"Jean-Bernard Lasserre and Edouard Pauwels. The empirical christoffel function with applications in data analysis. *Advances in Computational Mathematics*, 45(3):1439–1468, 2019.", {}),
    ("p0020-b006", T, ("p0020-b006",),
     r"Fei Tony Liu, Kai Ming Ting, and Zhi-Hua Zhou. Isolation forest. In *2008 eighth ieee international conference on data mining*, pages 413–422. IEEE, 2008.", {}),
    ("p0020-b007", T, ("p0020-b007",),
     r"Stephen Prajna. Barrier certificates for nonlinear model validation. *Automatica*, 42(1):117–126, 2006.", {}),
    ("p0020-b008", T, ("p0020-b008",),
     r"Glenn Shafer and Vladimir Vovk. A tutorial on conformal prediction. *Journal of Machine Learning Research*, 9(3), 2008.", {}),
    ("p0020-b009", T, ("p0020-b009",),
     r"Peter Van Overschee and Bart De Moor. *Subspace identification for linear systems: Theory—Implementation—Applications*. Springer Science & Business Media, 2012.", {}),
    ("p0020-b010", T, ("p0020-b010",),
     r"Vladimir Vovk. Transductive conformal predictors. In *Artificial Intelligence Applications and Innovations: 9th IFIP WG 12.5 International Conference, AIAI 2013, Paphos, Cyprus, September 30–October 2, 2013, Proceedings 9*, pages 348–360. Springer, 2013.", {}),
    ("p0020-b011", "omit", ("p0020-b011",), "", {"reason": pageno(20)}),
])
