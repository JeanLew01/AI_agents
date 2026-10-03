from pagelib import *
o = orig(5)
B = lambda k: o[k]["bbox"]

items = [
    text("p0005-b000", B("p0005-b000"), X(
         r"""vectors, and $P : \mathbb{R}^m \rightarrow \{\top, \bot\}$ is a predicate. The basis vectors are arranged to form the star’s $d \times m$ basis matrix. Given variables $\mu_\ell \in \mathbb{R}, \ell = 1,\ldots,m$, the set of states represented by the star is given as:"""),
         join_previous="space"),
    text("p0005-b001", B("p0005-b001"), X(
         r"""$$Y = \left\{ y \mid y = c + \sum_{\ell=1}^{m} (\mu_\ell v_\ell) \text{ s.t. } P(\mu_1, \ldots, \mu_m) = \top \right\}. \tag{3}$$""")),
    heading("p0005-b002", B("p0005-b002"), "### 2.3 Conformal Inference & Probabilistic Reachability"),
    text("p0005-b003", B("p0005-b003"), X(
         r"""A key step toward probabilistic reachability is to provide a provable $\delta$-quantile for the residual. Let $\ressim_1 < \ressim_2 < \ldots < \ressim_L$ represent $L$ different i.i.d. residuals sampled from $\distzeroR$, and sorted in ascending order. Given a confidence probability, $\delta \in (0,1)$, a provable tight upper bound for the $\delta$-quantile of the residuals $\resreal \sim \distR$ is computable from samples $\ressim_i\sim \distzeroR , i\in[L]$, using robust conformal inference proposed in Cauchois et al. (2024) that is an extension of CI, proposed in Vovk (2012).""")),
    text("p0005-b004", B("p0005-b004"), X(
         r"""The theory of conformal inference states that for a new sample $\ressim \sim \distzeroR$, the rank $\ell := \lceil (L + 1)\delta\rceil \le L$ satisfies $\Pr[ \ressim < \ressim_\ell] \geq \delta$. This implies that $\ressim_\ell$ serves as a provable upper bound for the $\delta$-quantile of $\distzeroR$. However, this result does not extend to another residual $\resreal \sim \distR$, which is drawn from a different distribution. To address this distribution shift, the theory of robust conformal inference introduces an adjustment to conformal inference. It establishes that for any random variable $\resreal \sim \distR$ satisfying $\tv(\distR, \distzeroR) \leq \tau$ with a threshold $\tau > 0$, we have $\Pr[\resreal < \ressim_{\ell^*}] > \delta$, where""")),
    text("p0005-b005", B("p0005-b005"), X(
         r"""$$\ell^*:=\lceil (L + 1)(1 + 1/L)(\delta+\tau)\rceil,\ \ \ell^* \leq L. \tag{4}$$""")),
    text("p0005-b006", B("p0005-b006"), X(
         r"""Thus, $\ressim_{\ell^*}$ serves as an upper bound for the $\delta$-quantile of $\distR$.""")),
    text("p0005-b007", B("p0005-b007"), X(
         r"""**Inflating Hypercube**. In reachability analysis, the main purpose for the definition of the residual is to achieve a bounding region that will cover the random sequence of prediction errors, $\PE = [R^1, R^2, \ldots, R^{n\horizon}]$ with a confidence $\delta\in (0,1)$. In this case, as suggested by Cleaveland et al. (2024), the $\max()$ operator over the absolute value of all errors is a suitable choice. The authors in Hashemi et al. (2024b), for some positive constants $\alpha_j, j\in[n\horizon]$ (details on the choice of $\alpha_j$ can be found in Hashemi et al. (2024b)), define the residual""")),
    text("p0005-b008", B("p0005-b008"), X(
         r"""$$\rho:= R = \max( \alpha_1 |R^1|, \alpha_2 |R^2|, \ldots, \alpha_{n\horizon}|R^{n\horizon}|), \tag{5}$$""")),
    text("p0005-b009", B("p0005-b009"), X(
         r"""and show that such a bounding region is achievable by computing an upper bound for the $\delta$-quantile of residual, $R$. In other words, assuming $R^*$ as the mentioned upper bound, we have,""")),
    text("p0005-b010", B("p0005-b010"), X(
         r"""$$\Pr[R<R^*] \geq \delta \iff \Pr[P^*(R^1,\ldots,R^{n\horizon}) = \top] \geq \delta,\ \ P^*(R^1,\ldots,R^{n\horizon}) = \bigwedge_{j=1}^{n\horizon} (|R^j| < \frac{R^*}{\alpha_j}) \tag{6}$$""")),
    text("p0005-b011", B("p0005-b011"), X(
         r"""where $R^*$ is efficiently obtainable via robust conformal inference. As defined in (6), the predicate $P^*$ implies that for every component $R^j, j=1,\ldots,n\horizon$ of the vector $\PE$ we have $-R^*/\alpha_j\leq R^j \leq R^*/\alpha_j$. This describes a hypercube which can be formulated as the following star set:""")),
    text("p0005-b012", B("p0005-b012"), X(
         r"""$$\delta X = \langle\  0_{n\horizon \times 1},\  I_{n\horizon},\  P^*(R^1,\ldots,R^{n\horizon}) \ \rangle \subset \mathbb{R}^{n\horizon}. \tag{7}$$""")),
    omit("p0005-b013", B("p0005-b013"), "5",
         "Printed page number 5 centred at the foot of the page; page furniture, checked on the 170 dpi render."),
]

save(5, items, r"""
Compared with the 170 dpi render, two 260 dpi crops (Section 2.3 down to (4); 'Inflating Hypercube' down to (7)) and the TeX source
(sections/prelim.tex). First item is the rest of Definition 2 (join_previous 'space' to the last item of page 4); the definition ends
with display (3) (end of the TeX environment; body italic in the print, written upright). The five extractor formula images were
replaced by LaTeX displays with the printed tags (3), (4), (5), (6), (7); the surrounding glyph-soup text was replaced by LaTeX taken
from the TeX source with macros expanded and the manual negative spaces (\!) dropped; every formula was checked on the crops and agrees
with the TeX. Points checked symbol by symbol: conformal rank $\ell := \lceil (L + 1)\delta\rceil \le L$ with $\Pr[\rho<\rho_\ell]\ge\delta$
(non-strict $\ge$); robust statement $\Pr[\rho<\rho_{\ell^{\ast}}] > \delta$ (strict $>$) under
$\mathsf{TV}(\mathcal{J}^{\mathsf{real}}_{S,\mathrm{K}},\mathcal{J}^{\mathsf{sim}}_{S,\mathrm{K}})\le\tau$ with $\tau>0$; (4)
$\ell^{\ast} := \lceil (L + 1)(1 + 1/L)(\delta+\tau)\rceil$, $\ell^{\ast}\le L$; (5) $\rho := R = \max(\alpha_1|R^1|,\ldots,
\alpha_{n\mathrm{K}}|R^{n\mathrm{K}}|)$; (6) with $\iff$, strict '<' inside the conjunction and ordinary (not auto-sized) parentheses
around $|R^j| < R^{\ast}/\alpha_j$; (7) $\delta X = \langle 0_{n\mathrm{K}\times 1}, I_{n\mathrm{K}}, P^{\ast}(\ldots)\rangle \subset
\mathbb{R}^{n\mathrm{K}}$. All asterisk superscripts are written ^{\ast} (Markdown safety). Note: in this paper $\delta$ is the
confidence/coverage level (e.g. 99.99 %), not a failure probability, and the same letter $\rho$ denotes residuals from both
distributions (see page 4 note). The order of the two arguments of TV differs between Section 2.2 (sim, real) and this page (real, sim),
as printed. Heading '2.3 Conformal Inference & Probabilistic Reachability' as ###; 'Inflating Hypercube' is a bold run-in title.
Printed wording kept: 'the $\max()$ operator', 'quantile of residual, $R$'. Citations (natbib author-year) compared with the render.
The sentence after (7) starts on page 6. Omitted: page number 5.
""")
