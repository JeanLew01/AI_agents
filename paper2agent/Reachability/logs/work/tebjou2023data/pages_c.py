#!/usr/bin/env python3
"""Pages 7-10 of tebjou2023data (PMLR v204 PDF). Run: python3 pages_c.py"""
from lib import page, HDR_ODD, HDR_EVEN, pageno

T = "text"
CAL = r"C_{\mathcal{D}_{\mathrm{cal}}}^{\frac{1}{N}}"
DCAL = r"\mathcal{D}_{\mathrm{cal}}"


def D(s):
    return "$$\n" + s.strip() + "\n$$"


# ---------------------------------------------------------------- page 7
page(7, r"""
Compared with the 170 dpi render of PDF page 7, a 200 dpi crop of Figure 1 with margins, a 240 dpi crop of the
mathematics, and the TeX source. Running header and page number omitted. Figure 1: the extractor had four
separate panel crops and a text item with the sub-captions; they are replaced by one figure item whose crop
contains the four panels with their axis tick labels and the printed sub-captions '(a) d = 3, eps = 0.085',
'(b) d = 6, eps = 0.23', '(c) d = 10, eps = 0.51', '(d) d = 15, eps = 0.9' (all four edges checked on the
wider crop). The sub-captions are also transcribed as the first line of the caption item so that the
values are searchable; the caption proper follows verbatim. Figure 1 belongs to Example 1 (page 6) and is
printed here at the top of the page, inside Section 3; the reading order places it after Example 1. The
three displays (p-value, conformal region, coverage statement (7)) were taken from the TeX source and checked
on the 240 dpi crop; only (7) is numbered. As printed: 'p_value' with an italic subscript 'value', the
conformal region is indexed by the level i/N as a superscript and by the sample D as a subscript, the level
index runs over i in {0,...,N}, and (7) reads >= 1 - (i+1)/(N+1). The citation pair is printed with a
semicolon ('Shafer and Vovk (2008); Angelopoulos and Bates (2021)'). 'non-conformity' (first sentence),
're-sampled' and 'data-driven' are printed hyphens; 'nonconformity' without hyphen in Section 3.1, as
printed. '3.1. Statistical Guarantees' is a level-3 heading. The first paragraph of Section 3.1 continues on
page 8 (same paragraph, new sentence); it is joined there with a space.
""", [
    ("p0007-b000", "omit", ("p0007-b000",), "", {"reason": HDR_ODD}),
    ("p0007-fig1", "figure", [85.0, 85.0, 527.0, 181.0], "", {"label": "Figure 1", "asset_name": "figure-1"}),
    ("p0007-b006", "caption", ("p0007-b006",),
     r"(a) $d = 3$, $\varepsilon = 0.085$ (b) $d = 6$, $\varepsilon = 0.23$ (c) $d = 10$, $\varepsilon = 0.51$ (d) $d = 15$, $\varepsilon = 0.9$"
     "\n\n"
     r"Figure 1: Reach set approximation $\hat{S}$ for Example 1, using the sublevel set of the empirical Christoffel polynomial in (6) (purple outline) on a sample of size $N = 10000$ (black dots), for different degrees $d$ and corresponding uncertainty bound $\varepsilon$, according to Conjecture 1.", {}),
    ("p0007-b007", T, [90.0, 288.0, 523.0, 317.0],
     r"Let $r : \mathbb{R}^n \rightarrow \mathbb{R}$ be a non-conformity function. Given a sample $\mathcal{D} = \bigl\{ \boldsymbol{x}^{1}, \ldots, \boldsymbol{x}^{N} \bigr\}$, the $p$-value at $\boldsymbol{x}$ is", {}),
    ("p0007-b008", T, [217.0, 318.0, 395.0, 340.0],
     D(r"p_{value}(\boldsymbol{x}) = \tfrac{1}{N} \Bigl| \bigl\{\ i \bigm| r(\boldsymbol{x}^i) \geq r(\boldsymbol{x}) \;\bigr\} \Bigr|"), {}),
    ("p0007-b009", T, ("p0007-b009",),
     r"For $i \in \{0, ..., N\}$, the conformal region is defined as", {}),
    ("p0007-b010", T, ("p0007-b010",),
     D(r"C_{\mathcal{D}}^{\frac{i}{N}} = \Bigl\{ \boldsymbol{x} \in \mathbb{R}^n \Bigm| p_{value}(\boldsymbol{x}) \geq \tfrac{i}{N} \Bigr\}"), {}),
    ("p0007-b011", T, ("p0007-b011",),
     r"According to conformal prediction theory, see Shafer and Vovk (2008); Angelopoulos and Bates (2021), a new i.i.d sample $\boldsymbol{x}^{N+1}$ satisfies", {}),
    ("p0007-b012", T, ("p0007-b012",),
     D(r"\mathbb{P}\left( \boldsymbol{x}^{N+1} \in C_{\mathcal{D}}^{\frac{i}{N}} \right) \geq 1 - \tfrac{i+1}{N+1}. \tag{7}"), {}),
    ("p0007-b013", T, ("p0007-b013",),
     r"Note that in (7), the set $\mathcal{D}$ is also subject to randomness. In other words, (7) stands on average only if the set $\mathcal{D}$ is re-sampled for each $\boldsymbol{x}^{N+1}$. However, in reachability analysis and data-driven applications more generally, we may be restricted to a single, fixed data set $\mathcal{D}$. Therefore, we need to take into account the probability on the left hand side of (7), conditioned on the sample $\mathcal{D}$.", {}),
    ("p0007-b014", "heading", ("p0007-b014",), "### 3.1. Statistical Guarantees", {}),
    ("p0007-b015", T, ("p0007-b015",),
     r"In this section, we ensure statistical independence between the nonconformity function $r$ and the set $\mathcal{D}$ by splitting it into a training set $\mathcal{D}_{\mathrm{train}}$ and a calibration set $\mathcal{D}_{\mathrm{cal}}$. The use of distinct sets of samples from the same measurement (i.e., a training set and a calibration set) is essential to ensure the independence of the samples used for computing the p-values and conformal regions from the nonconformity function, which is computed based on the training set, see Angelopoulos and Bates (2021) and Bates et al. (2023). This is a special case of conformal prediction called split conformal prediction or inductive conformal prediction. The computational advantage of this method lies in its requirement to fit the model only once. However, this comes at the cost of statistical efficiency as the method necessitates the division of the data into separate, and therefore smaller, training and calibration data sets.", {}),
    ("p0007-b016", "omit", ("p0007-b016",), "", {"reason": pageno(7)}),
])

# ---------------------------------------------------------------- page 8
page(8, r"""
Compared with the 170 dpi render of PDF page 8, two 240 dpi crops covering the whole text block, and the TeX
source. Running header and page number omitted. The first item continues the first paragraph of Section 3.1
from page 7 (join_previous: space; the paragraph is not broken in the PDF). 'trade-off' is a printed compound
hyphen; 'section 3.2' is printed with a lower-case s. All seven displays were taken from the TeX source with
macros expanded and checked symbol by symbol on the crops; the extractor's seven formula images were replaced.
Printed equation numbers: (8) in Theorem 2 and (9) in Theorem 3; the other displays are unnumbered.
Theorem-like blocks: the PDF prints the headers in bold without punctuation ('Theorem 2 (Thm. 4 from Bates et
al. (2023))', 'Theorem 3', 'Proof') and the theorem bodies in italics (not reproduced); the proof body is
upright and ends with a filled square, written as \blacksquare. Kept as printed (authors' notation, not
conversion errors): the thresholds are called 'b_1, ..., b_n' (lower-case n) twice in the paragraph before
Theorem 2 and the last event in the hypothesis of Theorem 2 is 'U_(N) <= b_n', while the chain of inequalities
uses b_N; the conditional-probability display before Theorem 2 has the region C with subscript D (not D_cal)
and conditions on D_cal; the proof of Theorem 3 writes 'U_N = F_mu(r(x^N))' without parentheses in the
subscript; 'i.i.d vector', 'sampled i.i.d from' without final period; 'an analogous, theorem' with the comma.
In Theorem 2 the i.i.d. sign is a tilde with 'i.i.d.' stacked above it and Unif([0,1]) has \bigl/\bigr
parentheses. Theorem 3 assumes that r is continuous and the measure mu is continuous, and its conclusion (9)
is stated for the region with level 1/N. Cross-references written as printed: 'Thm. 2', 'Thm. 3', 'Algorithm
1', '(9)'.
""", [
    ("p0008-b000", "omit", ("p0008-b000",), "", {"reason": HDR_EVEN}),
    ("p0008-b001", T, [90.0, 94.0, 523.0, 158.0],
     r"A smaller calibration set increases the coverage error, while a smaller training set reduces the tightness of the approximation. An alternative to this trade-off will be examined in section 3.2. Here, we use the training set for computing the empirical Christoffel polynomial, while the calibration set is used to compute the conformal region. This will lead to bounds on the conditional probability",
     {"join_previous": "space"}),
    ("p0008-b002", T, [244.0, 158.5, 368.0, 185.5],
     D(r"\mathbb{P}\Bigl( \boldsymbol{x}^{N+1} \in C_{\mathcal{D}}^{\frac{i}{N}}\ \Bigm| \mathcal{D}_{\mathrm{cal}} \Bigr)."), {}),
    ("p0008-b003", T, ("p0008-b003",),
     r"Note that the theorems in this section apply to any choice of nonconformity function. The following theorem provides PAC guarantees for conformal regions that are defined with suitably chosen probability thresholds $b_1, \ldots, b_n$. We will afterwards propose values for $b_1, \ldots, b_n$ that correspond to the special case of set approximation.", {}),
    ("p0008-b004", T, ("p0008-b004",),
     r"**Theorem 2 (Thm. 4 from Bates et al. (2023))** Consider $N$ uniform random samples $U_1, \ldots, U_N \stackrel{\text{i.i.d.}}{\sim} \operatorname{Unif}\bigl([0,1]\bigr)$, with order statistics $U_{(1)} \leq U_{(2)} \leq \ldots \leq U_{(N)}$, and fix any $\delta \in (0,1)$. Suppose $0 \leq b_1 \leq b_2 \leq \ldots \leq b_N \leq 1$ are reals such that", {}),
    ("p0008-b005", T, ("p0008-b005",),
     D(r"\mathbb{P}\left[ U_{(1)} \leq b_1, \ldots, U_{(N)} \leq b_n \right] \geq 1-\delta."), {}),
    ("p0008-b006", T, ("p0008-b006",),
     r"Let also $b_0 = 0$. Then for any i.i.d vector $\boldsymbol{x}$ sampled from $\mu$:", {}),
    ("p0008-b007", T, ("p0008-b007",),
     D(r"\mathbb{P}\left[ \mathbb{P}\Bigl( \boldsymbol{x} \in C_{\mathcal{D}_{\mathrm{cal}}}^{\frac{i}{N}} \Bigm| \mathcal{D}_{\mathrm{cal}} \Bigr) \geq 1 - b_i \right] \geq 1-\delta \tag{8}"), {}),
    ("p0008-b008", T, ("p0008-b008",),
     r"We propose an analogous, theorem to bound the conditional probability from above.", {}),
    ("p0008-b009", T, ("p0008-b009",),
     r"**Theorem 3** Under the assumptions of Thm. 2, suppose further that the nonconformity function $r(\boldsymbol{x})$ is continuous, the measure $\mu$ is continuous, and that $\alpha$ is a real such that", {}),
    ("p0008-b010", T, ("p0008-b010",),
     D(r"\mathbb{P}\bigl( U_{(N)} \leq \alpha \bigr) \geq 1-\delta."), {}),
    ("p0008-b011", T, ("p0008-b011",),
     r"Then for any i.i.d vector $\boldsymbol{x}$ sampled from $\mu$:", {}),
    ("p0008-b012", T, ("p0008-b012",),
     D(r"\mathbb{P}\left[ \mathbb{P}\Bigl( \boldsymbol{x} \in " + CAL + r" \Bigm| " + DCAL + r" \Bigr) \leq \alpha \right] \geq 1-\delta \tag{9}"), {}),
    ("p0008-b013", T, ("p0008-b013",),
     r"**Proof** Under the assumptions, $r(\boldsymbol{x})$ has a continuous distribution. Let $F_{\mu}$ be the cumulative distribution function of $r(\boldsymbol{x})$. Since $r(\boldsymbol{x})$ has a continuous distribution, $F_{\mu}(r(\boldsymbol{x}))$ follows $\operatorname{Unif}([0,1])$ and $F_{\mu}(r(\boldsymbol{x}^1)), F_{\mu}(r(\boldsymbol{x}^2)), ..., F_{\mu}(r(\boldsymbol{x}^N))$ all follow $\operatorname{Unif}([0,1])$. Without loss of generality, we assume $r(\boldsymbol{x}^1) \leq r(\boldsymbol{x}^2) \leq ... \leq r(\boldsymbol{x}^N)$. Letting $U_N = F_{\mu}(r(\boldsymbol{x}^N))$, we obtain", {}),
    ("p0008-b014", T, ("p0008-b014",),
     D(r"\mathbb{P}\Bigl[ F_{\mu}(r(\boldsymbol{x}^N)) \leq \alpha \Bigr] \geq 1-\delta."), {}),
    ("p0008-b015", T, ("p0008-b015",),
     r"Considering $\boldsymbol{x}$ sampled i.i.d from $\mu$, we get", {}),
    ("p0008-b016", T, ("p0008-b016",),
     D(r"\mathbb{P}\Bigl( \boldsymbol{x} \in " + CAL + r" \Bigm| " + DCAL + r" \Bigr) = \mathbb{P}\Bigl( r(\boldsymbol{x}) \leq r(\boldsymbol{x}^N) \Bigm| " + DCAL + r" \Bigr) = F_{\mu}\Bigl( r(\boldsymbol{x}^N) \Bigr)"), {}),
    ("p0008-b017", T, ("p0008-b017",),
     r"Combining the latter two results, we obtain (9). $\blacksquare$", {}),
    ("p0008-b018", T, ("p0008-b018",),
     r"We now use the results of Thm. 2 and Thm. 3 to provide a guarantee on the accuracy of approximated reachable set $\hat{\mathcal{S}}$ in Algorithm 1. Note that Thm. 3 requires the nonconformity function to be continuous, which is the case for the empirical Christoffel polynomial.", {}),
    ("p0008-b019", "omit", ("p0008-b019",), "", {"reason": pageno(8)}),
])

# ---------------------------------------------------------------- page 9
page(9, r"""
Compared with the 170 dpi render of PDF page 9, two 240 dpi crops (Theorem 4; proof), and the TeX source.
Running header and page number omitted. Theorem 4 (the paper's main coverage guarantee): header 'Theorem 4' in
bold without punctuation, body italic in the PDF (not reproduced); the body consists of the continuity
assumption on r, display (10), 'If the measure mu is continuous, then', display (11), 'Combining these
results, we obtain for all delta in (0, 1/2):' and display (12), and ends with (12) as in the TeX theorem
environment. The three displays were taken from the TeX source and checked on the 240 dpi crop, including the
direction of every inequality, the arguments log(delta) and log(1 - delta), the division by N, the commas
ending (10) and (11), the period ending (12) and the right-hand sides 1 - delta, 1 - delta, 1 - 2 delta. The
interval in 'for all delta in (0, 1/2)' is printed with a slanted fraction (\sfrac{1}{2}); it is written
1/2. Proof: all four displays and the inline formulas from the TeX source, checked on the crop. Kept as printed
(authors' slips, not conversion errors): 'b_1 ..., b_N' and 'b_2 ..., b_N = 1' without the comma after the
first index, 'b_2 = .... = b_N = 1' with four dots, 'U_N <= b_N' (no parentheses in the subscript) in the
first display of the proof and 'P[U_N <= alpha]' in the last paragraph, the product written with a capital
Pi (\Pi_{i=1}^N), '>=' in P(U_(1) >= b_1), 'Combing (10) and (11)'. The inline exponent in 'b_1 = 1 -
delta^(1/N)' is a stacked fraction. The proof ends with a filled square (\blacksquare), printed on its own
line. The extractor had merged the line 'As mu(C) = P[...] we obtain the result in (10).' into a formula
image and garbled the following paragraph ('log(1 - delta) Fixing alpha = exp N'); both are restored as
text. Example 2: header 'Example 2' in bold, body italic in the PDF (not reproduced). The example starts at
the bottom of this page and its text continues on page 11 below Figure 3 ('... the degree of the empirical |
Christoffel polynomial d.'); page 10 (Algorithm 1 and Figure 2) lies in between. The reading order places
Algorithm 1 before the example and joins the two halves of the example text. Percentages are written
outside math mode ('99%').
""", [
    ("p0009-b000", "omit", ("p0009-b000",), "", {"reason": HDR_ODD}),
    ("p0009-b001", T, ("p0009-b001",),
     r"**Theorem 4** Suppose that the nonconformity function $r(\boldsymbol{x})$ is continuous. $\forall \delta \in (0,1),$", {}),
    ("p0009-b002", T, ("p0009-b002",),
     D(r"\mathbb{P}\left[ \mu\left( " + CAL + r" \right) \geq \exp\left( \frac{\log(\delta)}{N} \right) \right] \geq 1-\delta, \tag{10}"), {}),
    ("p0009-b003", T, ("p0009-b003",),
     r"If the measure $\mu$ is continuous, then", {}),
    ("p0009-b004", T, ("p0009-b004",),
     D(r"\mathbb{P}\left[ \exp\left( \frac{\log(1-\delta)}{N} \right) \geq \mu\left( " + CAL + r" \right) \right] \geq 1-\delta, \tag{11}"), {}),
    ("p0009-b005", T, ("p0009-b005",),
     r"Combining these results, we obtain $\forall \delta \in (0, 1/2)$:", {}),
    ("p0009-b006", T, ("p0009-b006",),
     D(r"\mathbb{P}\left[ \exp\left( \frac{\log(1-\delta)}{N} \right) \geq \mu\left( " + CAL + r" \right) \geq \exp\left( \frac{\log(\delta)}{N} \right) \right] \geq 1-2\delta. \tag{12}"), {}),
    ("p0009-b007", T, ("p0009-b007",),
     r"**Proof** We instantiate Theorem 2 for a particular choice of $b_1 \ldots, b_N$. Since we are interested in the support of the measure, we take $b_1$ as the smallest possible value and set the other values $b_2 \ldots, b_N = 1$. To satisfy the conditions of Theorem 2, we first show the following intermediate result: Let $U_1, \ldots, U_N \stackrel{\text{i.i.d.}}{\sim} \operatorname{Unif}([0,1])$, with order statistics $U_{(1)} \leq U_{(2)} \leq \ldots \leq U_{(N)}$. Fixing $b_1 = 1 - \delta^{\frac{1}{N}}$ and $b_2 = .... = b_N = 1$, it is straightforward that", {}),
    ("p0009-b008", T, ("p0009-b008",),
     D(r"\mathbb{P}\left( U_{(1)} \leq b_1, \ldots, U_{N} \leq b_N \right) = \mathbb{P}\left( U_{(1)} \leq b_1 \right) = 1 - \mathbb{P}\left( U_{(1)} \geq b_1 \right)."), {}),
    ("p0009-b009", T, ("p0009-b009",),
     r"Since $U_{(1)}$ is the smallest of the random variables, $U_1, \ldots, U_N$, $\mathbb{P}\left( U_{(1)} \geq b_1 \right)$ is equivalent to all of the $U_i$ being greater or equal to $b_1$:", {}),
    ("p0009-b010", T, ("p0009-b010",),
     D(r"1 - \mathbb{P}\left( U_{(1)} \geq b_1 \right) = 1 - \Pi_{i=1}^N \mathbb{P}\left( U_{i} \geq b_1 \right) = 1 - (1 - b_1)^N = 1-\delta."), {}),
    ("p0009-b011", T, ("p0009-b011",),
     r"Applying the above in Theorem 2, we obtain", {}),
    ("p0009-b012", T, [150.0, 459.0, 462.0, 495.0],
     D(r"\mathbb{P}\left[ \mathbb{P}\Bigl( \boldsymbol{x} \in " + CAL + r" \Bigm| " + DCAL + r" \Bigr) \geq \exp\left( \frac{\log(\delta)}{N} \right) \right] \geq 1-\delta."), {}),
    ("p0009-b012b", T, [90.0, 498.0, 523.0, 527.0],
     r"As $\mu\left( " + CAL + r" \right) = \mathbb{P}\left[ \boldsymbol{x} \in " + CAL + r" \mid " + DCAL + r" \right]$ we obtain the result in (10).", {}),
    ("p0009-b013", T, [90.0, 528.0, 523.0, 588.0],
     r"Fixing $\alpha = \exp\left( \frac{\log(1-\delta)}{N} \right)$, we have $\mathbb{P}\left[ U_{N} \leq \alpha \right] = \alpha^N = 1-\delta$, since $U_{(N)} \leq \alpha$ means all $U_{i}$ have to be lower than $\alpha$. Substituting the above value of $\alpha$ in Theorem 3, we obtain the result in (11). Combing (10) and (11), we obtain the result in (12). $\blacksquare$", {}),
    ("p0009-b014", T, ("p0009-b014",),
     r"**Example 2** We illustrate Algorithm 1 on the running Example 1. We take $M = 10000$ i.i.d samples from the reachable set $\mathcal{S}$ by sampling uniformly $M$ i.i.d samples in $\mathcal{I}$, which we then split into a calibration set of size $N = 2000$ and a training set of size $M-N$. Figure 2 shows the approximated reachable set produced by Algorithm 1 for various degrees $d$. Theorem 4 guarantees that with confidence $1-\delta =$ 99%, the coverage error $\epsilon$ is lower than $\epsilon \leq 0.002$. Notably, in contrast to the algorithm presented in Devonport et al. (2021), this guarantee is independent of the dimension of the samples $n$ and the degree of the empirical", {}),
    ("p0009-b015", "omit", ("p0009-b015",), "", {"reason": pageno(9)}),
])

# ---------------------------------------------------------------- page 10
ALG1 = "\n\n".join([
    r"**Algorithm 1:** Reach set approximation (without outliers)",
    r"**Input:** An i.i.d data sample $\mathcal{D} = \{\boldsymbol{x}^{1}, \ldots, \boldsymbol{x}^{M}\}$, drawn from the reach set $\mathcal{S} = f(\mathcal{I})$, the degree $d$, the size $N$ of the calibration set with $N < M$",
    r"**Output:** $\epsilon$-accurate approximation $\hat{\mathcal{S}}$ of $\mathcal{S}$ with confidence $1-\delta$ and coverage error $\epsilon = 1 - \delta^{1/N}$",
    r"`#` Construct the training set of $M-N$ samples and the calibration set of $N$ samples: $\mathcal{D}_{\mathrm{train}} = \{\boldsymbol{x}^{N+1}, \ldots, \boldsymbol{x}^{M}\}$ and $\mathcal{D}_{\mathrm{cal}} = \{\boldsymbol{x}^{1}, \ldots, \boldsymbol{x}^{N}\}$",
    r"1. Compute the empirical moment matrix $\widehat{\mathbf{M}}_d$ and its inverse",
    r"&emsp;&emsp;(a) $\widehat{\mathbf{M}}_d = \frac{1}{M-N} \sum_{i=N+1}^{M} \mathbf{v}_{d}\left(\boldsymbol{x}^{i}\right) \mathbf{v}_{d}\left(\boldsymbol{x}^{i}\right)^{\top}$, with $\boldsymbol{x}^{i} \in \mathcal{D}_{\mathrm{train}}$",
    r"&emsp;&emsp;(b) Compute $\widehat{\mathbf{M}}^{-1}_d$.",
    r"2. Calculate the threshold $\alpha$: $\alpha = \max_{i=1,\ldots,N} \mathbf{v}_{d}\left(\boldsymbol{x}^{i}\right)^{\top} \widehat{\mathbf{M}}^{-1}_d \mathbf{v}_{d}\left(\boldsymbol{x}^{i}\right)$, with $\boldsymbol{x}^{i} \in \mathcal{D}_{\mathrm{cal}}$",
    r"3. Given the returned $\widehat{\mathbf{M}}^{-1}_d$ and $\alpha$, record the conformal region:",
    D(CAL + r" = \hat{\mathcal{S}} = \Bigl\{ \boldsymbol{x} \in \mathbb{R}^{n} \Bigm| \mathbf{v}_{d}(\boldsymbol{x})^{\top} \widehat{\mathbf{M}}^{-1}_d \mathbf{v}_{d}(\boldsymbol{x}) \leq \alpha \Bigr\}"),
])

page(10, r"""
Compared with the 170 dpi render of PDF page 10, a 240 dpi crop of Algorithm 1, a 200 dpi crop of Figure 2
with margins, and the TeX source. Running header and page number omitted. The page contains only two floats.
Algorithm 1: the extractor had split the box into a heading, four text items and two formula images; it is
replaced by one image crop of the whole box (from above the top rule to below the bottom rule, edges checked)
and a text transcription taken from the TeX algorithm2e environment and checked line by line on the crop:
title 'Algorithm 1: Reach set approximation (without outliers)', Input, Output, the unnumbered comment line
marked '#' (typewriter, written as a code span so that it is not read as a heading), steps 1, 1(a), 1(b), 2,
3 and the final display. As printed: the output line states the coverage error eps = 1 - delta^(1/N) with a
slanted fraction in the exponent; the training set is x^(N+1),...,x^M (M - N samples) and the calibration set
x^1,...,x^N; the moment matrix is normalised by 1/(M-N); the threshold is the maximum over the calibration
points i = 1,...,N; the returned set is called both the conformal region C with level 1/N and S-hat. Because
the PDF text of the box lies inside the image crop, the tool's number check lists the numbers of the
transcription as extra. Figure 2: the extractor's three panel crops and three caption fragments are replaced
by one figure item containing the three panels, their tick labels and the printed sub-captions '(a) d = 6,
eps = 0.002', '(b) d = 10, eps = 0.002', '(c) d = 15, eps = 0.002' (edges checked on the wider crop); the
sub-captions are repeated as the first line of the caption item, followed by the caption verbatim (the
extractor's list marker before 'Figure 2:' removed). In the reading order Algorithm 1 is placed after the proof
of Theorem 4 (where the TeX source defines it), before Example 2, and Figure 2 after the text of Example 2.
""", [
    ("p0010-b000", "omit", ("p0010-b000",), "", {"reason": HDR_EVEN}),
    ("p0010-alg1", "figure", [86.0, 122.0, 527.0, 390.0], "", {"label": "Algorithm 1", "asset_name": "algorithm-1"}),
    ("p0010-alg1-text", T, [90.0, 126.0, 522.0, 386.0], ALG1, {}),
    ("p0010-fig2", "figure", [88.0, 454.0, 527.0, 571.0], "", {"label": "Figure 2", "asset_name": "figure-2"}),
    ("p0010-b015", "caption", ("p0010-b015",),
     r"(a) $d = 6$, $\varepsilon = 0.002$ (b) $d = 10$, $\varepsilon = 0.002$ (c) $d = 15$, $\varepsilon = 0.002$"
     "\n\n"
     r"Figure 2: Reach set approximations (outlined in purple) from Example 2, obtained with Algorithm 1, which uses the Christoffel polynomial as a nonconformity function, for $M = 10000$ samples, of which $N = 2000$ are the calibration set (red dots) and the remainder the training set (black dots). Higher degrees $d$ lead to tighter approximation.", {}),
    ("p0010-b016", "omit", ("p0010-b016",), "", {"reason": pageno(10)}),
])
