# Pages 6-10 of sartipizadeh2019voronoi (executed by make_pages.py; page() and dd() come from there).

# ---------------------------------------------------------------- page 6
page(6, r"""
Compared with the 150 dpi render and two 230 dpi crops of PDF page 6 and with the TeX source. The
page holds Lemma 2 (Hoeffding's inequality), Theorem 1 with the scenario bound (13), its proof, and
the paragraph after the proof. All mathematics rewritten in LaTeX from the TeX source (\Prob ->
\mathbb{P}, \Exp -> \mathbb{E}, \mcS -> \mathcal{S}; \mbox -> \text; asterisks written \ast) and
checked symbol by symbol on the crops; TeX and PDF agree. The extractor 'formula' images were
replaced by $$ blocks with the printed numbers (12), (13), (14a), (14b), (14c) (three $$
blocks in one item so that each keeps its number), (15), (16) (two aligned lines, the number is printed on the
second line), and the unnumbered chain of inequalities ending in $e^{-2K\delta^2}$. The extractor had
scrambled the inline fractions and the two inline set expressions of the proof; they are restored
from the TeX source. Lemma 2 and Theorem 1 start with the printed bold label; the title
'(Hoeffding's inequality)' is printed in bold italics. Lemma 2 ends with (12) and Theorem 1 ends with
(13) (TeX environments; the bodies are printed in italics, written upright). 'Proof:' is the printed
italic run-in label (written bold); the proof ends with the printed filled square after
'$K\geq\frac{-\ln(\beta)}{2\delta^2}$.', written $\blacksquare$. IMPORTANT, kept exactly as printed
and confirmed on the 230 dpi crop: the statement of Theorem 1 prints the event as
$\{p^\ast(x_0)-p_{K}^{\ast}(x_0)\geq\delta\}$, whereas Question 1 (page 4), equation (15), the final
chain and the last sentence of the proof all use $\{p_{K}^{\ast}(x_0)-p^\ast(x_0)\geq\delta\}$; this
order reversal is in the source (TeX and PDF) and is not a conversion error. Also as printed:
$\overline{Z}$ (with bar) in the two inline sets but $Z$ elsewhere; (14c) has no end punctuation;
$\mathcal{S}_1$, $\mathcal{S}_2$ denote generic sets here. Citation [24] checked.
""", [
    ("p0006-b000", "text", [56.0, 56.0, 556.0, 80.0],
     r"**Lemma 2. (Hoeffding’s inequality)** Define $\overline{Y}=\frac{\mathbf{1}^\top Y}{K}=\frac{\sum_{i=1}^K y^{(i)}}{K}$, and $\mu_{\overline{Y}}\triangleq\mathbb{E}\left[ \overline{Y} \right]$. For any $\delta>0$,", {}),
    ("p0006-b000b", "text", [56.0, 82.0, 556.0, 101.0],
     dd(r"\mathbb{P}_{Y}^K\left\{ \overline{Y} - \mu_{\overline{Y}} \geq \delta \right\}\leq e^{-2K\delta^2}.", "12"), {}),
    ("p0006-b001", "text", ("p0006-b001",),
     r"**Theorem 1.** Given a violation parameter $\delta\in[0,1]$, risk of failure $\beta\in[0,1]$, initial state $x_0\in \mathcal{S}$, and the optimal solution $U^\ast_K\in \mathcal{U}^N$ to Problem 2, we have the risk of failure $\mathbb{P}_{Z}^{x_0, U^\ast_K}\{ p^\ast(x_0) - p_{K}^{\ast}(x_0) \geq \delta\}\leq \beta$, if", {}),
    ("p0006-b002", "text", ("p0006-b002",), dd(r"K\geq \frac{-\ln(\beta)}{2\delta^2}.", "13"), {}),
    ("p0006-b003", "text", ("p0006-b003",),
     r"**Proof:** Let the optimal solution to Problem 1 be $U^\ast\in \mathcal{U}^N$ (which may not be equal to $U^\ast_K$). For $x_0\in \mathcal{S}$,", {}),
    ("p0006-b004", "text", ("p0006-b004",),
     dd(r"p^\ast(x_0)= \mathbb{E}_z^{x_0,U^\ast}\left[ z \right]=\frac{\mathbb{E}_Z^{x_0,U^\ast}\left[ \mathbf{1}^\top Z \right]}{K},", "14a") + "\n\n"
     + dd(r"p^\ast_K(x_0)=\frac{1}{K}\sum_{i=1}^K z^{(i)}=\frac{\mathbf{1}^\top Z}{K}\text{ under } U^\ast_K,", "14b") + "\n\n"
     + dd(r"\mathbb{E}_z^{x_0,U^\ast}\left[ z \right] \geq \mathbb{E}_z^{x_0,U^\ast_K}\left[ z \right]", "14c"), {}),
    ("p0006-b005", "text", ("p0006-b005",), "Using (14a) and (14b),", {}),
    ("p0006-b006", "text", ("p0006-b006",),
     dd(r"\mathbb{P}_{Z}^{x_0, U^\ast_K}\{ p_{K}^{\ast}(x_0)-p^\ast(x_0) \geq \delta\} =\mathbb{P}_{Z}^{x_0, U^\ast_K}\left\{\left( \frac{1}{K}\sum_{i=1}^K z^{(i)} - \mathbb{E}_z^{x_0,U^\ast}\left[ z \right] \right) \geq \delta\right\}.", "15"), {}),
    ("p0006-b007", "text", ("p0006-b007",),
     r"Adding and subtracting $\mathbb{E}_z^{x_0,U^\ast_K}\left[ z \right]$, we have", {}),
    ("p0006-b008", "text", ("p0006-b008",),
     dd(r"""\begin{aligned}
\left( \frac{1}{K}\sum_{i=1}^K z^{(i)} - \mathbb{E}_z^{x_0,U^\ast}\left[ z \right] \right) &\ = \left( \frac{1}{K}\sum_{i=1}^K z^{(i)} - \mathbb{E}_z^{x_0,U^\ast_K}\left[ z \right] \right) +\left( \mathbb{E}_z^{x_0,U^\ast_K}\left[ z \right] - \mathbb{E}_z^{x_0,U^\ast}\left[ z \right] \right) \\
&\ \leq \left( \frac{1}{K}\sum_{i=1}^K z^{(i)} - \mathbb{E}_z^{x_0,U^\ast_K}\left[ z \right] \right)
\end{aligned}""", "16"), {}),
    ("p0006-b009", "text", ("p0006-b009",),
     r"where (16) follows from (14c). Thus, $\left\{ \overline{Z}\in\{0,1\}^K: \left( \frac{\mathbf{1}^\top \overline{Z}}{K} - \mathbb{E}_z^{x_0,U^\ast}\left[ z \right]\right)\geq \delta\right\}$ is a subset of $\left\{\overline{Z}\in\{0,1\}^K: \left( \frac{\mathbf{1}^\top \overline{Z}}{K} - \mathbb{E}_z^{x_0,U^\ast_K}\left[ z \right]\right)\geq \delta\right\}$ by (14b) and (16). Using the fact that $\mathbb{P}\{ \mathcal{S}_1\}\leq \mathbb{P}\{ \mathcal{S}_2\}$ for any two sets $\mathcal{S}_1\subseteq \mathcal{S}_2$, Hoeffding’s inequality (12), $\mathbb{E}_z^{x_0,U^\ast_K}\left[ z \right]=\frac{\mathbb{E}_Z^{x_0,U^\ast_K}\left[ \mathbf{1}^\top Z \right]}{K}$, and (15), we have", {}),
    ("p0006-b010", "text", ("p0006-b010",),
     dd(r"\mathbb{P}_{Z}^{x_0, U^\ast_K}\{ p_{K}^{\ast}(x_0)-p^\ast(x_0) \geq \delta\} \leq\mathbb{P}_{Z}^{x_0, U^\ast_K}\left\{\left( \frac{\mathbf{1}^\top Z}{K} - \frac{\mathbb{E}_Z^{x_0,U^\ast_K}\left[ \mathbf{1}^\top Z \right]}{K} \right) \geq \delta\right\}\leq e^{-2K\delta^2}."), {}),
    ("p0006-b011", "text", ("p0006-b011",),
     r"To obtain the desired probabilistic guarantee $\mathbb{P}_{Z}^{x_0, U^\ast_K}\{ p_{K}^{\ast}(x_0)-p^\ast(x_0) \geq \delta\} \leq\beta$, we require $e^{-2K\delta^2}\leq \beta$. Solving for $K$, we obtain $K\geq \frac{-\ln(\beta)}{2\delta^2}$. $\blacksquare$", {}),
    ("p0006-b012", "text", ("p0006-b012",),
     r"Theorem 1 addresses Question 1. Specifically, choosing at least $K$ scenarios, Theorem 1 guarantees that the probability of the event that the MILP-based estimated terminal time probability (the optimal solution to Problem 2) exceeds the true terminal time probability (the optimal solution to Problem 1) by more than $\delta$ is less than $\beta$ (a small value). Here, both $\delta$ and $\beta$ are provided by the user. Note that although $p^{\ast}$ and $p_{K}^{\ast}$ are functions of the time horizon $N$, $K$ is independent of the choice of $N$. A similar bound is used for the application of aircraft conflict detection in [24].", {}),
])

# ---------------------------------------------------------------- page 7
page(7, r"""
Compared with the 150 dpi render and two 230 dpi crops of PDF page 7 and with the TeX source.
Headings '## 4 Partition-based sample reduction' and '### 4.1 Seed Selection and Buffer Computation'
(capitalisation as printed). All mathematics rewritten in LaTeX from the TeX source and checked on
the crops; TeX and PDF agree. The extractor 'formula' images were replaced by $$ blocks: the
unnumbered MILP of Problem 3 (aligned block with the printed 's.t.'), the unnumbered display
$\phi(W):=G_{w}W.$ inside Problem 3, and the unnumbered display of $\hat{X}(\psi^{(j)})$ inside
Lemma 3 (the extractor had made a 'formula' image of the last text line of Lemma 3 as well; it is
text again). Problem 3 and Lemma 3 start with the printed bold label; bodies printed in italics,
written upright. Problem 3 ends after '... a lower bound on the solution of Problem 2.' and Lemma 3
after '... sampled state trajectory set $\mathcal{X}_{K}^{x_0,U}$.' (end of the italic text = TeX
environments). The proof of Lemma 3 starts with the printed italic 'Proof:' (written bold) and ends
with the printed filled square, written $\blacksquare$. Checked on the crops: the hats in
$\hat{X}^{(j)}$, $\hat{z}^{(j)}$, $\hat{K}$; the buffer $\varepsilon^{(j)}$ (varepsilon) in
$F\hat{X}^{(j)}\leq h-\varepsilon^{(j)}+M(1-\hat{z}^{(j)})\mathbf{1}$; the objective weight
$\frac{1}{K}$ (not $1/\hat{K}$) with the sum running to $\hat{K}$; $p_{\hat{K}}^{\ast}(x_0)$;
$\sum_{j=1}^{\hat{K}}\alpha^{(j)}=K$ and $\alpha^{(j)}\in\mathbb{N}_{[1,K]}$; $j^{th}$ with italic
'th'; $\Psi_{\hat{K}}$, $\Phi_{K}:=\phi(\mathcal{W}_{K})$, $\hat{\mathcal{X}}_{\hat{K}}^{x_0,U}$.
Kept as printed: after the display $\phi(W):=G_{w}W.$ the next sentence starts with
'$\alpha^{(j)}$ is the importance rate'; 'Figure 2 shows a 2D partition with 11 seeds'; 'Results
directly from Lemma 1.'.
""", [
    ("p0007-b000", "heading", ("p0007-b000",), "## 4 Partition-based sample reduction", {}),
    ("p0007-b001", "text", ("p0007-b001",),
     r"As implied from the concentration probability bounds given in Theorem 1, Problem 2 typically needs a large number of samples to provide a precise approximation for Problem 1 with a small deviation $\delta$ and small risk of failure $\beta$. Therefore, solving Problem 2 can be computationally expensive or even intractable for real-time applications. In this section, we address Question 2 by proposing a *partition-based* method which provides an underapproximation to Problem 2 with flexible computational complexity, as opposed to the sampling-based approach, presented in Problem 2. To this end, we propose the following MILP problem with $\hat{K}$ binary variables, where $\hat{K}$ can be significantly smaller than $K$ and is selected by the user.", {}),
    ("p0007-b002", "text", ("p0007-b002",), "**Problem 3.** The partition-based terminal time problem is", {}),
    ("p0007-b003", "text", ("p0007-b003",),
     dd(r"""\begin{aligned}
\max_{U\in\mathcal{U}^N} \quad & \frac{1}{K}\sum_{j=1}^{\hat{K}}\alpha^{(j)}\hat{z}^{(j)} \\
\text{s.t.} \quad & \hat{X}^{(j)} = G_{x}x_{0} + G_{u} U + \psi^{(j)}, \quad j\in \mathbb{N}_{[1,\hat{K}]}, \\
& F\hat{X}^{(j)} \leq h -\varepsilon^{(j)}+ M(1-\hat{z}^{(j)})\mathbf{1}, \quad j\in \mathbb{N}_{[1,\hat{K}]}, \\
& \hat{z}^{(j)} \in\{0,1\}, \quad j\in \mathbb{N}_{[1,\hat{K}]}
\end{aligned}"""), {}),
    ("p0007-b004", "text", ("p0007-b004",),
     r"with the optimal value denoted by $p_{\hat{K}}^{\ast}(x_0)$. Here, $M \in \mathbb{R}$ is some large positive number, and $\psi^{(j)}$ for $j\in\mathbb{N}_{[1,\hat{K}]}$ are $\hat{K}$ selected representatives (seeds) of uncertainty, computed in a prediction mapping $\phi:\mathcal{W}^{N}\rightarrow \mathcal{X}^{N}$ with", {}),
    ("p0007-b005", "text", ("p0007-b005",), dd(r"\phi(W):=G_{w}W."), {}),
    ("p0007-b006", "text", ("p0007-b006",),
     r"$\alpha^{(j)}$ is the importance rate of the $j^{th}$ seed with $\sum_{j=1}^{\hat{K}}\alpha^{(j)}=K$ and $\alpha^{(j)}\in\mathbb{N}_{[1,K]}$. For $j\in\mathbb{N}_{[1,\hat{K}]}$, $\varepsilon^{(j)}$ is an appropriately designed buffer that guarantees the solution of Problem 3 is a lower bound on the solution of Problem 2.", {}),
    ("p0007-b007", "text", ("p0007-b007",),
     r"In Problem 3, the state uncertainty is characterized by $\hat{K}$ seeds where the $j^{th}$ seed represents $\alpha^{(j)}$ scenarios of $\mathcal{W}_{K}$. Then the reach-avoid constraints are only checked at the selected seeds instead of being checked at every scenario, which reduces the number of binary variables and constraints.", {}),
    ("p0007-b008", "heading", ("p0007-b008",), "### 4.1 Seed Selection and Buffer Computation", {}),
    ("p0007-b009", "text", [56.0, 520.0, 556.0, 575.0],
     r"Given a sample set $\mathcal{W}_K$, $x_{0}\in\mathcal{S}$, and $U$, we define $\mathcal{X}_{K}^{x_0,U}:=X(x_0,U,\mathcal{W}_K)$ as the set of sampled state trajectories. We desire that the elements $\mathcal{X}_{K}^{x_0,U}$ remain in reach-avoid set $\mathcal{R}$. The set $\mathcal{X}_{K}^{x_0,U}$ can be partitioned into cells, where each cell consists of some of the random state trajectories and is represented by a seed. Figure 2 shows a 2D partition with 11 seeds.", {}),
    ("p0007-b009b", "text", [56.0, 588.0, 556.0, 619.0],
     r"**Lemma 3.** Let $\Psi_{\hat{K}}:=\{\psi^{(1)},\cdots,\psi^{(\hat{K})}\}$ be the set of optimal seeds of $\Phi_{K}:=\phi(\mathcal{W}_{K})$ with $\phi(W):=G_{w}W$ that minimizes $\mathrm{WSS}$. Then $\hat{\mathcal{X}}_{\hat{K}}^{x_0,U}=\hat{X}(\Psi_{\hat{K}})=\{\hat{X}(\psi^{(1)}),\cdots,\hat{X}(\psi^{(\hat{K})})\}$ with", {}),
    ("p0007-b010", "text", ("p0007-b010",), dd(r"\hat{X}(\psi^{(j)})=G_{x}x_{0}+G_{u}U+\psi^{(j)},"), {}),
    ("p0007-b011", "text", ("p0007-b011",),
     r"represents the set of optimal seeds for sampled state trajectory set $\mathcal{X}_{K}^{x_0,U}$.", {}),
    ("p0007-b012", "text", ("p0007-b012",),
     r"**Proof:** Results directly from Lemma 1. Since there is no uncertainty in $G_x$ and $G_u$, $G_{x}x_0+G_{u}U$ in (2) can be interpreted as a translation term. $\blacksquare$", {}),
    ("p0007-b013", "text", ("p0007-b013",),
     r"According to Lemma 3, although the state trajectory is an optimization variable, it can be clustered through the prediction mapping $\phi(W)$ *offline*, independent of the choice of $x_0$ and $U$.", {}),
])

# ---------------------------------------------------------------- page 8
page(8, r"""
Compared with the 150 dpi render and two 230 dpi crops of PDF page 8 and with the TeX source.
Figure 2 is a float at the top of the page, between two paragraphs (the last paragraph of page 7 is
complete); it is kept at that position. Crop bbox from the ink extent of the render (x 202.2-401.4,
y 63.0-199.8: magnified inset circle on the left and the coloured partition) plus a margin; the
figure has no text labels. Caption verbatim ('Figure 1' resolved from the reference, $\hat{K}$ in
LaTeX). All mathematics rewritten in LaTeX from the TeX source and checked on the crops; TeX and PDF
agree. The extractor 'formula' images were replaced by $$ blocks with the printed numbers (17),
(18), (19), (20), (21); spacing commands \hspace{5mm}/\hspace{10mm} of the source written \qquad.
Lemma 4, Remark 2 and Theorem 2 start with the printed bold label; bodies printed in italics,
written upright. Lemma 4 ends with (18) (TeX environment; the italic word 'and' between (17) and
(18) belongs to it). The proof of Lemma 4 starts with the printed italic 'Proof:' (written bold) and
ends with the printed filled square after 'the proof is completed.', written $\blacksquare$. Checked
on the crops: two different epsilons are printed and kept: $\varepsilon^{(j)}$ (the buffer vector)
and $\epsilon_{\ell}^{(j)}$ (its components); $\ell$ (script l) as the row index of $F_{\ell}$,
$h_{\ell}$; the cells $V_{\Phi_K}^{(j)}(\Psi_{\hat{K}})$; in (18) the maximisation set
$\phi\in V_{\Phi_K}^{(j)}(\Psi_{\hat{K}})$ under 'max'; $j^{th}$ with italic 'th'; in Remark 2 '1D'
($1$D in the source; the D is italic only because the remark body is italic) is written plainly and
the complexity is
$\mathcal{O}(\sum_{j=1}^{\hat{K}}\alpha^{(j)}\log\alpha^{(j)})$; in Theorem 2
$\alpha^{(j)}=\vert V_{\Phi_{K}}^{(j)}(\Psi_{\hat{K}})\vert$. The sentence 'The buffering concept is
illustrated in Figure 3.' is its own paragraph between the proof and Remark 2. Theorem 2 is the last
item of the page; its proof is printed on page 9 after the Figure 3 float (Figure 3 and its caption
are moved in the reading order to follow the sentence that refers to it on this page, see page 9).
""", [
    ("p0008-b000", "figure", [196.0, 57.0, 408.0, 206.0], "", {"label": "Figure 2", "asset_name": "figure-2"}),
    ("p0008-b001", "caption", ("p0008-b001",),
     r"Figure 2: Partitioning the state uncertainty region of Figure 1 to $\hat{K}$ cells using a Voronoi partition. Larger dots indicate the selected Voronoi seeds. Samples inside each cell are closer to their own seed than other seeds.", {}),
    ("p0008-b002", "text", ("p0008-b002",),
     r"**Lemma 4.** Let a set of points $\Phi_{K}$, a set of selected seeds $\Psi_{\hat{K}}$, as defined in Lemma 3, and their Voronoi partition $\mathcal{V}_{\Phi_{K}}(\Psi_{\hat{K}})$ with cells $V_{\Phi_K}^{(1)}(\Psi_{\hat{K}}),\cdots,V_{\Phi_K}^{(\hat{K})}(\Psi_{\hat{K}})$ be given. Then, for $j\in\mathbb{N}_{[1,\hat{K}]}$, every point $\phi\in V_{\Phi_K}^{(j)}(\Psi_{\hat{K}})$ remains in the original constraint set $FX\leq h$ if $\psi^{(j)}$, the $j^{th}$ seed, remains in the buffered constraint set $F\hat{X}(\psi^{(j)})\leq h-\varepsilon^{(j)}$ with", {}),
    ("p0008-b003", "text", ("p0008-b003",),
     dd(r"\varepsilon^{(j)}=\left[{\epsilon_{1}^{(j)}},\cdots,{\epsilon_{L}^{(j)}}\right]^{\top},", "17"), {}),
    ("p0008-b004", "text", ("p0008-b004",), "and", {}),
    ("p0008-b005", "text", [189.0, 395.0, 561.0, 427.0],
     dd(r"\epsilon_{\ell}^{(j)}:=\max_{\phi\in V_{\Phi_K}^{(j)}(\Psi_{\hat{K}})} \left(F_{\ell}\phi-F_{\ell}\psi^{(j)}\right), \qquad \ell\in\mathbb{N}_{[1,L]}.", "18"), {}),
    ("p0008-b006", "text", ("p0008-b006",),
     r"**Proof:** From (18) we conclude that for all $\ell\in\mathbb{N}_{[1,L]}$, $j\in\mathbb{N}_{[1,\hat{K}]}$,", {}),
    ("p0008-b007", "text", ("p0008-b007",),
     dd(r"F_{\ell}\phi\leq F_{\ell}\psi^{(j)}+\epsilon_{\ell}^{(j)} \qquad \forall \phi\in V_{\Phi_K}^{(j)}(\Psi_{\hat{K}}).", "19"), {}),
    ("p0008-b008", "text", ("p0008-b008",),
     r"By adding $F_{\ell}\left(G_{x}x_0+G_{u}U\right)$ to the right and left sides of (19), we have", {}),
    ("p0008-b009", "text", ("p0008-b009",),
     dd(r"F_{\ell}\left(G_{x}x_0+G_{u}U+\phi\right)\leq F_{\ell}\left(G_{x}x_0+G_{u}U+\psi^{(j)}\right)+\epsilon_{\ell}^{(j)}.", "20"), {}),
    ("p0008-b010", "text", ("p0008-b010",),
     r"Consequently, for all $\phi\in V_{\Phi_K}^{(j)}(\Psi_{\hat{K}})$, the following holds for any initial state and input trajectory,", {}),
    ("p0008-b011", "text", ("p0008-b011",),
     dd(r"F_{\ell}X(x_0,U,\phi)\leq F_{\ell}\hat{X}(x_{0},U,\psi^{(j)})+\epsilon_{\ell}^{(j)}.", "21"), {}),
    ("p0008-b012", "text", [56.0, 583.0, 556.0, 629.0],
     r"Denoting $F_{\ell}X(x_0,U,\phi)$ and $F_{\ell}\hat{X}(x_0,U,\psi^{(j)})$ with $F_{\ell}X(\phi)$ and $F_{\ell}\hat{X}(\psi^{(j)})$, when $F_{\ell}\hat{X}(\psi^{(j)})\leq h_{\ell}-\epsilon_{\ell}^{(j)}$, it is concluded from (21) that $F_{\ell}X(\phi)\leq h_{\ell}$, $\forall \phi\in V_{\Phi_K}^{(j)}(\Psi_{\hat{K}})$. Since (21) is valid for all $\ell\in\mathbb{N}_{[1,L]}$ and $j\in\mathbb{N}_{[1,\hat{K}]}$, the proof is completed. $\blacksquare$", {}),
    ("p0008-b012b", "text", [56.0, 630.0, 556.0, 642.0], "The buffering concept is illustrated in Figure 3.", {}),
    ("p0008-b013", "text", ("p0008-b013",),
     r"**Remark 2.** Computing $\epsilon_{\ell}^{(j)}$ for $\ell=1,\cdots,L$ and $j\in \mathbb{N}_{[1,\hat{K}]}$ is a sorting problem in 1D and can be executed by worst time complexity of $\mathcal{O}(\sum_{j=1}^{\hat{K}}\alpha^{(j)} \log \alpha^{(j)})$.", {}),
    ("p0008-b014", "text", ("p0008-b014",),
     r"**Theorem 2.** Let $\Phi_{K}$ be a set of $K$ disturbance samples mapped through the prediction mapping $\phi(W):=G_{w}W$ and let $\Psi_{\hat{K}}$ be a set of selected seeds. Let $\alpha^{(j)}=\vert V_{\Phi_{K}}^{(j)}(\Psi_{\hat{K}})\vert$, $j\in\mathbb{N}_{[1,\hat{K}]}$, denote the number of elements of $V_{\Phi_{K}}^{(j)}(\Psi_{\hat{K}})$ and define $\varepsilon^{(j)}$ as in Lemma 4. Problem 3 provides a lower bound for Problem 2.", {}),
])

# ---------------------------------------------------------------- page 9
page(9, r"""
Compared with the 150 dpi render and a 220 dpi crop of PDF page 9 and with the TeX source. Figure 3
is a float at the top of the page, printed between Theorem 2 (end of page 8) and its proof; in the
reading order (plan.json) the figure and its caption are moved to follow the page-8 sentence 'The
buffering concept is illustrated in Figure 3.', so that the proof follows Theorem 2 directly. Crop
bbox from the ink extent of the render (x 221.9-385.6, y 59.7-226.2) plus a margin; it includes the
rotated labels '$F_2X=h_2-\epsilon_2^{(j)}$' and '$F_2X=h_2$' on the left, the red
'$\epsilon_2^{(j)}$', '$\epsilon_1^{(j)}$' and '$X^{(j)}$' inside the green cell, and
'$F_1X=h_1-\epsilon_1^{(j)}$' and '$F_1X=h_1$' at the bottom; the extractor's scattered picture text
is not kept as text. Caption verbatim with LaTeX math. Mathematics from the TeX source, checked on
the crop; TeX and PDF agree. The two extractor 'formula' images were replaced by $$ blocks: (22)
with its printed number and the unnumbered chain
$p_{\hat{K}}^{\ast}\leq\hat{p}\leq p_{K}^{\ast}$. Heading '### 4.2 Tightening the Voronoi-based
terminal time probability estimate'. Remark 3 and Theorem 3 start with the printed bold label
(bodies printed in italics, written upright); Theorem 3 ends with the unnumbered chain (TeX
environment; the italic 'Then' belongs to it). The proof of Theorem 2 starts with 'Proof:' (written
bold) and ends with the printed filled square ($\blacksquare$). The proof of Theorem 3 starts on
this page with part 'i)' and continues on page 10 with part 'ii)' as a new printed paragraph, so no
cross-page join is needed. Reference '(see (22))' checked. Kept as printed: in the caption
'$X(\psi^{(j)})$' and '$F_{\ell}X^{(j)}$' without hats; 'if seed $\hat{X}(\psi^{(j)})$,
$\forall j\in\mathbb{N}_{[1,\hat{K}]}$, remains'; '$p^{\ast}_{\hat{K}}$ provides a lower bound on
$p^{\ast}_{K}$'; 'when number of cells tends to'.
""", [
    ("p0009-b000", "figure", [215.0, 54.0, 392.0, 230.0], "", {"label": "Figure 3", "asset_name": "figure-3"}),
    ("p0009-b001", "caption", ("p0009-b001",),
     r"Figure 3: Buffering process. Cell $V^{(j)}$ is shown in green. If $X(\psi^{(j)})$, the state trajectory corresponding to the seed of $V^{(j)}$, remains in the buffered constraint $F_{\ell}X^{(j)}\leq h_{\ell}-\epsilon_{\ell}^{(j)}$, the state trajectory of every sample in $V^{(j)}$ will satisfy the original constraint $F_{\ell}X\leq h_{\ell}$.", {}),
    ("p0009-b002", "text", [56.0, 295.0, 556.0, 358.0],
     r"**Proof:** According to the definition of the buffers, if seed $\hat{X}(\psi^{(j)})$, $\forall j\in\mathbb{N}_{[1,\hat{K}]}$, remains in the buffered constraint set, all $\alpha^{(j)}$ points of cell $V_{\Phi_{K}}^{(j)}(\Psi_{\hat{K}})$ remain in the original constraint set. Otherwise, at most $\alpha^{(j)}$ samples belonging to cell $V_{\Phi_{K}}^{(j)}(\Psi_{\hat{K}})$ may violate the original constraints. Since in Problem 3 the worst case is considered by weighting the $j^{th}$ seed with $\alpha^{(j)}$, $p^{\ast}_{\hat{K}}$ provides a lower bound on $p^{\ast}_{K}$. $\blacksquare$", {}),
    ("p0009-b002b", "text", [56.0, 368.0, 556.0, 396.0],
     r"**Remark 3.** If initial state $x_{0}\in\mathcal{S}$ is uncertain, the proposed method can be applied by defining $\phi(x_0,W):=G_{x} x_{0}+G_{w}W$.", {}),
    ("p0009-b003", "text", ("p0009-b003",),
     r"Obviously, having more cells results in a higher accuracy and when number of cells tends to the number of samples, $p^{\ast}_{\hat{K}}$ tends to $p^{\ast}_{K}$. However, this improved accuracy comes at a higher computational cost. We thus have to select $\hat{K}$ by trading off accuracy and computational cost.", {}),
    ("p0009-b004", "heading", ("p0009-b004",), "### 4.2 Tightening the Voronoi-based terminal time probability estimate", {}),
    ("p0009-b005", "text", ("p0009-b005",),
     r"Given $U_{\hat{K}}^{\ast}$ obtained from Problem 3, a tighter underapproximation on $p^{\ast}_{K}$ can be recalculated by simply checking the percentage of the original $K$ sampled trajectories that remain in reach-avoid set $\mathcal{R}$, after applying $U_{\hat{K}}^{\ast}$ to the stochastic system. In contrast to solving a large MILP (as done in Problem 2) whose computational complexity grows exponentially with $K$, this improved estimate (see (22)) is obtained by a policy evaluation that has a computational complexity of $\mathcal{O}(K)$. The following theorem presents the probability underapproximation proposed in this paper.", {}),
    ("p0009-b006", "text", ("p0009-b006",),
     r"**Theorem 3.** Let $p_{K}^{\ast}$ and $p_{\hat{K}}^{\ast}$ be the optimal values of Problem 2 and Problem 3, respectively, with corresponding optimal solutions $U_{K}^{\ast}$ and $U_{\hat{K}}^{\ast}$. Define $\hat{p}$ as", {}),
    ("p0009-b007", "text", ("p0009-b007",),
     dd(r"\hat{p}=\frac{1}{K}\sum_{i\in\mathbb{N}_{[1,K]}} 1_{\mathcal{R}}\left(X(x_{0},U^{\ast}_{\hat{K}},W^{(i)})\right).", "22"), {}),
    ("p0009-b008", "text", ("p0009-b008",), "Then", {}),
    ("p0009-b009", "text", [268.0, 672.0, 344.0, 693.0], dd(r"p_{\hat{K}}^{\ast}\leq \hat{p}\leq p_{K}^{\ast}."), {}),
    ("p0009-b010", "text", ("p0009-b010",),
     r"**Proof:** i) Since $p^{\ast}_{K}$ is the optimal terminal time probability with $K$ samples and $\hat{p}$ is the evaluation of an open-loop controller $U_{\hat{K}}^\ast$ over these $K$ samples, we conclude that $\hat{p}\leq p_{K}^{\ast}$. Equality holds if $U_{\hat{K}}^{\ast}=U_{K}^{\ast}$.", {"paren_ok": True}),
])

# ---------------------------------------------------------------- page 10
page(10, r"""
Compared with the 150 dpi render and 220-240 dpi crops of PDF page 10 and with the TeX source. The
page starts with part 'ii)' of the proof of Theorem 3 (a new indented paragraph; part 'i)' is on
page 9), which ends with the printed filled square ($\blacksquare$). Its mathematics was rewritten
from the TeX source and checked on the 240 dpi crop (the extractor had produced superscript soup):
$\mathcal{J}=\{j\in\mathbb{N}_{[1,\hat{K}]}|\hat{z}^{(j)}=1\}$, the two sums over
$\{i\in\mathbb{N}_{[1,K]}:W^{(i)}\in V^{(j)}\}$, $j^{\mathrm{th}}$ with upright 'th' (elsewhere
italic), $\frac{1}{K}\sum_{j\in\mathcal{J}}\alpha^{(j)}=\hat{p}_{\hat{K}}^\ast$. Kept exactly as
printed (source slips, not conversion errors): the proof writes $\hat{p}_{\hat{K}}^\ast$ (hat on
$p$) twice where Theorem 3 has $p_{\hat{K}}^{\ast}$; '$(z^{(j)}=0)$' without hat; 'the subset of
$\mathcal{C}^\ast$'; '$\alpha^{(j)}$ is the set of original scenarios'; 'but contains scenarios'.
Heading '### 4.3 Implementation'. Algorithm 1 is a float box printed directly under the heading: it
is kept as an image crop (asset algorithm-1; bbox from the ink extent x 56.8-556.0, y 204.1-528.6,
top and bottom rules included) followed by a text transcription made from the TeX source and
checked line by line on the 220 dpi crop: caption line 'Algorithm 1 Proposed Voronoi-based
reach-avoid solution', 'Input:', the offline steps 1-7, the online steps 1-2, 'Output:'. The printed
steps are bold-numbered lists (1.-7. and 1.-2.), written one paragraph per printed step with the
printed bold number and an indent; 'Offline (independent of $x_0$):' and 'Online
(depends on $x_0$):' are printed in bold italics (written bold). The 16 extractor fragments of the
box were replaced by the image and one transcription item; text inside the image crop is excluded
from the tool's line/number checks. References inside the box resolved to the printed numbers: (1),
(9), Lemma 4, Problem 3, (22). After the box, the paragraph 'Algorithm 1 describes ...' ('Section
2.4' resolved) and the paragraph 'After selecting $\hat{K}$ ...', which breaks at the page end after
'and then' and continues on page 11 (page-11 item joined with a space). Kept as printed: 'the
improvement precision is insignificant', '“knee”', 'the knee on the $\hat{p}$ vs. $\hat{K}$.',
'WSS' upright (\mathrm in the source, plain 'WSS' once in 'we compute WSS as a function').
""", [
    ("p0010-b000", "text", ("p0010-b000",),
     r"ii) Let $\mathcal{J}=\{j\in\mathbb{N}_{[1,\hat{K}]}|\hat{z}^{(j)}=1\}$, the subset of $\mathcal{C}^\ast$ which were deemed safe by Problem 3. By definition of $\alpha^{(j)}$, $\sum_{\{i\in \mathbb{N}_{[1,K]}: W^{(i)}\in V^{(j)}\}} 1_{\mathcal{R}}\left(X(x_{0},U^{\ast}_{\hat{K}},W^{(i)})\right) = \sum_{\{i\in \mathbb{N}_{[1,K]}: W^{(i)}\in V^{(j)}\}} 1$ for every $j\in \mathcal{J}$. In other words, since $\alpha^{(j)}$ is the set of original scenarios that fall in the $j^\mathrm{th}$ cell, whenever the solution of Problem 3 deems the representative seed safe, all the scenarios within it are safe. Thus, we have $\hat{p}$ at least as big as $\frac{1}{K}\sum_{j\in \mathcal{J}}\alpha^{(j)}=\hat{p}_{\hat{K}}^\ast$ since there might be other cells that were not deemed safe by Problem 3 $(z^{(j)}=0)$ but contains scenarios that might be safe $\left(1_{\mathcal{R}}\left(X(x_{0},U^{\ast}_{\hat{K}},W^{(i)})\right)=1\right)$. Hence, $\hat{p}\geq \hat{p}_{\hat{K}}^\ast$. $\blacksquare$", {"paren_ok": True}),
    ("p0010-b001", "heading", ("p0010-b001",), "### 4.3 Implementation", {}),
    ("p0010-b002", "figure", [54.0, 201.0, 558.0, 532.0], "", {"label": "Algorithm 1", "asset_name": "algorithm-1"}),
    ("p0010-b003", "text", [54.0, 533.0, 558.0, 540.0],
     "**Algorithm 1** Proposed Voronoi-based reach-avoid solution\n\n"
     r"**Input:** LTI system (1), safe set $\mathcal{S}$, target set $\mathcal{T}$, initial state $x_0$." "\n\n"
     r"**Offline (independent of $x_0$):**" "\n\n"
     r"&emsp;&emsp;**1.** Generate $\mathcal{W}_{K}$ by taking $K$ i.i.d. samples from $(\eta_{w})^{N}$." "\n\n"
     r"&emsp;&emsp;**2.** Construct $\Phi_{K}=\phi(\mathcal{W}_{K})$ with $\phi(W):=G_{w}W$." "\n\n"
     r"&emsp;&emsp;**3.** Select $\hat{K}$ based on the required time complexity or from the $\mathrm{WSS}$ vs. $\hat{K}$ curve." "\n\n"
     r"&emsp;&emsp;**4.** Compute $\Psi_{\hat{K}}$, the optimal $\hat{K}$ seeds of $\Phi_{K}$, by a clustering method." "\n\n"
     r"&emsp;&emsp;**5.** Determine $\mathcal{V}_{\Phi_{K}}(\Psi_{\hat{K}})$ with cells $V_{\Phi_{K}}^{(1)}(\Psi_{\hat{K}}),\cdots,V_{\Phi_{K}}^{(\hat{K})}(\Psi_{\hat{K}})$ from (9)." "\n\n"
     r"&emsp;&emsp;**6.** Compute importance rate vector $\alpha=\{\alpha^{(1)},\cdots,\alpha^{(\hat{K})}\}$ with $\alpha^{(j)}$ the number of elements of $V_{\Phi_{K}}^{(j)}(\Psi_{\hat{K}})$ for $j\in\mathbb{N}_{[1,\hat{K}]}$." "\n\n"
     r"&emsp;&emsp;**7.** Compute $\varepsilon^{(j)}$ for $j\in\mathbb{N}_{[1,\hat{K}]}$ using Lemma 4." "\n\n"
     r"**Online (depends on $x_0$):**" "\n\n"
     r"&emsp;&emsp;**1.** Solve Problem 3 for $U^{\ast}_{\hat{K}}$." "\n\n"
     r"&emsp;&emsp;**2.** Compute $\hat{p}$ from (22)." "\n\n"
     r"**Output:** $\hat{p}$.", {}),
    ("p0010-b016", "text", ("p0010-b016",),
     r"Algorithm 1 describes the proposed Voronoi-based method to solve the open-loop terminal time problem. Given a sample set $\mathcal{W}_K$ with $K$ random samples directly drawn from $(\eta_{w})^{N}$, one can construct $\phi(\mathcal{W}_K)$ and find its optimal $\hat{K}$ seeds. The $k$-means method can be used to find the seeds of a Voronoi partition as explained in Section 2.4. In addition, in order to determine the number of required seeds, $\mathrm{WSS}$ can be used as a measure of variability of points in a cluster. A smaller $\mathrm{WSS}$ implies more compact clusters which reduces the size of defined buffers $\varepsilon^{(1)},\cdots,\varepsilon^{(\hat{K})}$ and the average number of samples in each cell. Note that by increasing $\hat{K}$, clusters become smaller and the precision of Problem 3 grows. However, eventually, the improvement precision is insignificant compared to the imposed computational complexity. Therefore, we compute WSS as a function of $\hat{K}$, to explore this trade-off. We propose that the “knee” of the curve provides an efficient compromise between precision and computational complexity. It is shown experimentally in the next section that the knee of $\mathrm{WSS}$ vs. $\hat{K}$ curve can be a good representative of the knee on the $\hat{p}$ vs. $\hat{K}$. As a result, $\hat{K}$ can be computed and selected in advance.", {}),
    ("p0010-b017", "text", ("p0010-b017",),
     r"After selecting $\hat{K}$ based on the required running time for the real-time process or based on the $\mathrm{WSS}$ vs. $\hat{K}$, one can compute the Voronoi-based partition and the number of elements in each cell, and then", {}),
])
