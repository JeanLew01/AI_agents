from pagelib import *
o = orig(9)
B = lambda k: o[k]["bbox"]

items = [
    text("p0009-b000", B("p0009-b000"), X(
         r"""Given the initial state, $\statee_0 \sim \mathcal{W}$, assume a trajectory $\statee_1, \ldots, \statee_\horizon$ that is not necessarily sampled from $\distzero$ and also is not necessarily a member of the training dataset. For any segment $q \in [N]$ of this trajectory, we map its vector of prediction errors $\PE^q = \left[ R^{t_q n+1}, R^{t_q n+2}, \ldots, R^{(t_q+T_q)n} \right]$ to the principal axes. We do this with a linear map, as,""")),
    text("p0009-b001", B("p0009-b001"), X(
         r"""$$\left[ r^{t_q n+1},r^{t_q n+2}, \ldots, r^{(t_q+T_q)n} \right] = \transpose{\eigvecseg{q}} (\PE^q - \overline{\PE}^{q}), \tag{11}$$""")),
    text("p0009-b002", [90.0, 184.0, 522.0, 216.0], X(
         r"""and utilize the parameters $r^j,\ t_q n + 1\leq j \leq (t_q+T_q)n$ to define the residual. Collecting the mapped prediction errors for all segments $q\in[N]$, we propose our definition for residual as follows:""")),
    text("p0009-b003", [213.0, 217.0, 529.0, 253.0], X(
         r"""$$\rho:= \max \left(\ \frac{|r^1|}{\omega_1} ,\ \frac{|r^2|}{\omega_2} ,\ \ldots \ , \ \frac{|r^{n\horizon}|}{\omega_{n\horizon}}\ \right) \tag{12}$$""")),
    text("p0009-b004", B("p0009-b004"), X(
         r"""where the scaling factors $\omega_j , j \in [n\horizon]$ are the maximum magnitude of parameters $r^j_i , i\in |\traindataset|$, that are obtained from the training dataset. In other words,""")),
    text("p0009-b005", B("p0009-b005"), X(
         r"""$$\omega_j = \max( |r^{j}_1|,\ |r^{j}_2|,\ \ldots,\ |r^{j}_{|\traindataset|}| ),\ \ j \in[n\horizon]. \tag{13}$$""")),
    text("p0009-b006", B("p0009-b006"), X(
         r"""Although we use the training dataset $\traindataset$ to determine hyperparameters, $\eigvecseg{q}$, $\overline{\PE}^q$, and $\omega_j$ for defining the residual, reusing $\traindataset$ to generate the inflating hypercube with robust conformal inference violates CI rules. Thus, in order to generate the inflating hypercube, we first sample a new i.i.d. set of trajectories from the training environment $\distzero$, which we denote as the calibration dataset.""")),
    text("p0009-b007", B("p0009-b007"), X(
         r"""**Definition 4 (Calibration Dataset).** The calibration dataset $\calibdataset$ is defined as:""")),
    text("p0009-b008", B("p0009-b008"), X(
         r"""$$\calibdataset = \left\{ \left(\statee_{0,i}, \rho_i \right) \middle| \begin{array}{l} \statee_{0,i}\sim \mathcal{W}, \, \trajsim_{\statee_{0,i}} \sim \distzero, \\ \rho_i = \max( \frac{|r^1_i|}{\omega_1}, \ldots, \frac{|r^{n\horizon}_i|}{\omega_{n\horizon}}) \end{array} \right\}. \tag{14}$$""")),
    text("p0009-b009", B("p0009-b009"), X(
         r"""Here, $\trajsim_{\statee_{0,i}}, i \in |\calibdataset|$ refers to the trajectory starting at the $i^{th}$ initial state sampled from $\mathcal{W}$, generated from $\distzero$. The parameters $r^j_i$ are also as defined in equation (11).""")),
    text("p0009-b010", [89.0, 493.0, 524.0, 567.0], X(
         r"""Consider sorting the i.i.d. residuals $\rho_i \sim \distzeroR$ collected in the calibration dataset $\calibdataset$ by their magnitude: $\rho_1 < \rho_2 < \ldots < \rho_{|\calibdataset|}$. Our goal is to provide a provable upper bound for the $\delta$-quantile of a residual $\rho \sim \distR$, given knowledge of a radius $\tau > 0$ such that the total variation $\tv(\distR, \distzeroR) < \tau$. In this case, robust conformal inference Cauchois et al. (2024) suggests using the rank $\ell^*$ from equation (4) and selecting $\rho^*_{\delta, \tau} := \rho_{\ell^*}$ as an upper bound for the residual’s $\delta$-quantile. In other words, for a residual $\rho \sim \distR$, we have $\Pr[\rho < \rho^*_{\delta, \tau}] > \delta$.""")),
    text("p0009-b010b", [89.0, 572.0, 524.0, 648.0], X(
         r"""**Proposition 5.** Assume $\rho^*_{\delta,\tau}$ is the $\delta$-quantile of $\rho \sim \distR$, computed over the residuals $\rho_i \sim \distzeroR$ from the calibration dataset $\calibdataset$ where $\tv(\distR, \distzeroR)<\tau$. For the residual $\rho= \max \left(\ \frac{|r^1|}{\omega_1} ,\ \frac{|r^2|}{\omega_2} ,\ \ldots \ , \ \frac{|r^{n\horizon}|}{\omega_{n\horizon}}\ \right)$ sampled from the distribution $\distR$, and the trajectory division setting, $T_q, q\in[N]$, it holds that, $\Pr\left[ P(r^1,\ldots,r^{n\horizon}) = \top \right] > \delta$, where,""")),
    text("p0009-b010c", [89.0, 649.0, 529.0, 703.0], X(
         r"""$$P(r^1,\ldots,r^{n\horizon}) = \bigwedge_{q=1}^{N} P_q(r^{t_qn+1},\ldots,r^{(t_q+T_q)n}),\ \ P_q(r^{t_qn+1},\ldots,r^{(t_q+T_q)n}) := \bigwedge_{j=t_qn+1}^{(t_q+T_q)n} \left(-\omega_j\rho^*_{\delta,\tau}\leq r^j \leq \omega_j\rho^*_{\delta,\tau} \right) , \tag{15}$$""")),
    text("p0009-b011", B("p0009-b011"), X(
         r"""and $r^j$ is the mapped version of prediction errors $R^j,\ j\in [n\horizon]$ on principal axes.""")),
    omit("p0009-b012", B("p0009-b012"), "9",
         "Printed page number 9 centred at the foot of the page; page furniture, checked on the 170 dpi render."),
]

save(9, items, r"""
Compared with the 170 dpi render, three 280-300 dpi crops covering the whole text area ((11)-(13); the calibration paragraph,
Definition 4 with (14) and the paragraph 'Consider sorting ...'; Proposition 5 with (15)) and the TeX source (sections/PCA.tex). This
page carries the paper's central definitions and its guarantee, so every symbol was compared. The five extractor formula images
were replaced by LaTeX displays with the printed tags (11), (12), (13), (14), (15); all inline math is from the TeX source with
macros expanded (\eigvecseg{q} -> \mathsf{V}^{q}, \transpose{...} -> {...}^{\top}, \calibdataset -> \mathcal{R}^{\mathsf{calib}},
\traindataset -> \mathcal{T}^{\mathsf{trn}}, \PE -> \mathsf{PE}, \distR / \distzeroR -> \mathcal{J}^{\mathsf{real}}_{S,\mathrm{K}} /
\mathcal{J}^{\mathsf{sim}}_{S,\mathrm{K}}); TeX and PDF agree. In (15) the TeX uses long runs of \! to squeeze the display into the
line (in the print the commas of '$r^{t_qn+1},\ldots$' overlap the superscripts); these spacing commands were dropped, the symbols are
unchanged. Checked: (11) $[r^{t_qn+1},\ldots,r^{(t_q+T_q)n}] = {\mathsf{V}^{q}}^{\top}(\mathsf{PE}^q-\overline{\mathsf{PE}}^{q})$;
(12) $\rho := \max(|r^1|/\omega_1,\ldots,|r^{n\mathrm{K}}|/\omega_{n\mathrm{K}})$; (13) $\omega_j = \max(|r^j_1|,\ldots,
|r^j_{|\mathcal{T}^{\mathsf{trn}}|}|)$; (14) calibration set of pairs $(s_{0,i},\rho_i)$; '$\mathsf{TV}(\mathcal{J}^{\mathsf{real}},
\mathcal{J}^{\mathsf{sim}}) < \tau$' with strict '<' (twice: paragraph before Proposition 5 and inside it; page 5 has '$\le\tau$');
$\rho^{\ast}_{\delta,\tau} := \rho_{\ell^{\ast}}$ with $\ell^{\ast}$ 'from equation (4)'; $\Pr[\rho<\rho^{\ast}_{\delta,\tau}]>\delta$;
Proposition 5 conclusion $\Pr[P(r^1,\ldots,r^{n\mathrm{K}})=\top] > \delta$ (strict), predicate (15) with non-strict
$-\omega_j\rho^{\ast}_{\delta,\tau}\le r^j\le\omega_j\rho^{\ast}_{\delta,\tau}$. Printed wording kept as is: Proposition 5 says
'Assume $\rho^{\ast}_{\delta,\tau}$ is the $\delta$-quantile of $\rho\sim\mathcal{J}^{\mathsf{real}}_{S,\mathrm{K}}$' (the preceding
paragraph calls it an upper bound for that quantile); '$i\in|\mathcal{T}^{\mathsf{trn}}|$' and '$i\in|\mathcal{R}^{\mathsf{calib}}|$'
without square brackets; 'equation (4)', 'equation (11)' are the printed reference numbers. Theorem-like blocks: 'Definition 4
(Calibration Dataset).' (label written fully in bold; it ends after '... as defined in equation (11).', end of the TeX environment) and
'Proposition 5.' (ends after '... on principal axes.'); both bodies are italic in the print and written upright. The numbering is
shared (Definition 1, 2, Lemma 3, Definition 4, Proposition 5, Remark 6). Proposition 5 is split into three items (statement, display
(15), closing line); the extractor had merged it with the paragraph 'Consider sorting ...'. All asterisks written ^{\ast}. The proof is
on page 10. Omitted: page number 9.
""")
