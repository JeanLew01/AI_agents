from pagelib import *
P = 14
ROWS = [
    ["Symbol", "Meaning"],
    ["$r$", "reward function"],
    ["$h$", "safety loss function"],
    ["$V^π$", "cumulative discounted reward value function"],
    ["$V^π_c$", "cumulative discounted cost value function"],
    ["$V^π_h$", "reachability value function"],
    ["$𝟙_{s∈𝒮_v}$", "instantaneous violation indicator function"],
    ["$ϕ^π$", "reachability estimation function (REF) of a given policy"],
    ["$ϕ^{∗}$", "reachability estimation function (REF) of safest policy"],
    ["$p$", "predicted reachability estimation function (REF) of safest policy"],
    ["$H_{max}$", "upper bound of function $h$"],
    ["$H_{min}$", "minimum non-zero value of of function $h$"],
    ["$λ_{max}$", "maximum value to clip lagrange multiplier"],
    ["$R_{max}$", "upper bound of function $r$"],
    ["$𝒮_s$", "safe set"],
    ["$𝒮_v$", "unsafe set"],
    ["$𝒮_f$", "feasible set (persistent safe set)"],
    ["$𝔼_{s'∼π,P}$", "expectation taken over possible next states"],
    ["$𝔼_{τ∼π,P}$", "expectation taken over possible trajectories"],
    ["$𝔼_{s∼d_0}$", "expectation taken over initial distribution"],
]
t1 = table("p0014-b001", [150.0, 99.0, 460.0, 310.0], "Table 1", "supplementary-table-1", ROWS)
t1["asset_category"] = "supp_table"
items = [
    heading("p0014-b000", B(P, "p0014-b000"), "## A Notation"),
    t1,
    caption("p0014-b002", B(P, "p0014-b002"), r"Table 1: Notation used in the paper."),
    text("p0014-b002n", [153.0, 310.5, 456.0, 316.5],
         r"Conversion note for Table 1 (not part of the paper): the printed table has two columns separated by a vertical rule and no header row; the header 'Symbol | Meaning' was added for the CSV. The table cells use Unicode characters; in LaTeX notation the first column reads, in row order: $r$; $h$; $V^\pi$; $V^\pi_c$; $V^\pi_h$; $\mathbb{1}_{s\in \mathcal{S}_v}$; $\phi^\pi$; $\phi^{\ast}$; $p$; $H_{\max}$; $H_{\min}$; $\lambda_{\max}$; $R_{\max}$; $\mathcal{S}_s$; $\mathcal{S}_v$; $\mathcal{S}_f$; $\mathbb{E}_{s' \sim \pi,P}$; $\mathbb{E}_{\tau \sim \pi,P}$; $\mathbb{E}_{s \sim d_0}$."),
    heading("p0014-b003", B(P, "p0014-b003"), "## B Gradient estimates"),
    text("p0014-b004", B(P, "p0014-b004"),
         r"The Q value losses based on the MSE between the Q networks and the respective sampled returns result in the gradients:"),
    display("p0014-b005", B(P, "p0014-b005"), r"""\begin{aligned}
\hat{\nabla}_\eta J_{Q}(\eta) = \nabla_\eta Q(s_t,a_t;\eta)\cdot [Q_\eta(s_t, a_t) - (r(s_t, a_t) + \gamma Q(s_{t+1}, a_{t+1};\eta))] \\
\hat{\nabla}_\kappa J_{Q_c}(\kappa) = \nabla_\kappa Q_c(s_t,a_t;\kappa)\cdot [Q_\kappa(s_t, a_t) - (h(s_t) + \gamma Q_c(s_{t+1}, a_{t+1};\kappa))]
\end{aligned}"""),
    text("p0014-b006", B(P, "p0014-b006"), r"Similarly the REF gradient update is:"),
    display("p0014-b007", B(P, "p0014-b007"),
            r"\hat{\nabla}_\eta J_{p}(\xi) = \nabla_\xi p(s_t;\xi)\cdot [p(s_t;\xi) - \max\{\mathbb{1}_{s_t\in S_v}, \gamma p(s_{t+1};\xi)\}]"),
    text("p0014-b008", B(P, "p0014-b008"),
         r"From the policy gradient theorem in [52], we get the policy gradient loss as:"),
    display("p0014-b009", B(P, "p0014-b009"), r"""\begin{aligned}
\hat{\nabla}_\theta J_\pi(\theta) = \gamma^t \bigg[&-Q_\eta(s_t,a_t) [1 - p_\xi(s_t)] \\
&+Q_c(s_t,a_t) [\lambda_\omega (1 - p_\xi(s_t)) + p_\xi(s_t)]\bigg] \nabla_\theta \log\pi_\theta (a_t | s_t)
\end{aligned}"""),
    text("p0014-b010", B(P, "p0014-b010"), r"and the stochastic gradient of the multiplier is"),
    display("p0014-b011", B(P, "p0014-b011"),
            r"\hat{\nabla}_\omega J_\lambda(\omega) = Q_c(s_t,a_t;\kappa)(1-p_\xi(s_t)) \nabla_\omega \lambda_\omega"),
    text("p0014-b012", B(P, "p0014-b012"),
         r"and $\lambda_\omega$ is clipped to be in range $[0,\lambda_{\max}]$ (in particular, projection operator $\Gamma_\Omega(\lambda_\omega)=\arg\min_{\hat{\lambda}_\omega\in [0,\lambda_{\max}]} || \lambda_\omega - \hat{\lambda}_\omega||^2$)."),
    heading("p0014-b013", B(P, "p0014-b013"), "## C Proofs"),
    heading("p0014-b014", B(P, "p0014-b014"), "### C.1 Theorem 1 with Proof"),
    text("p0014-b015", B(P, "p0014-b015"),
         r"**Theorem 3.** The REF can be reduced to the following recursive Bellman formulation:"),
    pageno(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 14 and with main.tex (appendix A, B and the start of C). First page of the
appendix. Table 1 (notation list, 19 rows, two centred columns separated by a vertical rule, no header row): the
extractor had flattened it into one text item; it is now a table item with category supp_table and asset name
'supplementary-table-1' (printed label 'Table 1' kept). A header row 'Symbol | Meaning' was added because CSV needs
one; the symbol cells are written with Unicode characters (double-struck 1 and E, script S, Greek letters) because the
builder doubles backslashes inside table cells, and a clearly marked conversion note under the caption gives the same
19 symbols in LaTeX in row order. Rows read on the render one by one; as printed: 'minimum non-zero value of of function
h' (doubled 'of'), 'lagrange multiplier' in lower case. Appendix B: the five gradient formulas rewritten in LaTeX from
the TeX source (align* environments, none numbered) and checked on the render; the extractor had the first pair as
glyph-soup text and the others as formula images. The first display has two lines (reward critic and cost critic); the
policy gradient display is broken after the first bracket term as printed. As printed (kept, TeX and PDF agree): the
REF gradient is written with subscript eta on the nabla, $\hat{\nabla}_\eta J_p(\xi)$, although the parameter is
$\xi$; the cost-critic bracket contains $Q_\kappa(s_t,a_t)$; the violation set in the REF gradient is an italic $S_v$;
the norm is typed with double bars. The last sentence 'and $\lambda_\omega$ is clipped ...' continues the sentence of
the multiplier display. Appendix C: the heading 'C.1 Theorem 1 with Proof' is followed by the restatement of Theorem 1
of the main text, which the PDF numbers 'Theorem 3.' because the theorem counter continues (kept as printed; noted in
the conversion notes). Its display and the rest of the statement are on page 15. Citation [52] checked. Headings: A, B,
C level 2; C.1 level 3. Omitted: printed page number 14.
""")
