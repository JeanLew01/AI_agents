from pagelib import *
P = 7
items = [
    text("p0007-b003", B(P, "p0007-b003"),
         r"reached under (5) at timestep $t$, starting from any initial condition $x_0 \in {\mathcal{X}}_0$. This resulting hyper-rectangular set $\hat{\overline{\mathcal{X}}}_{0:T}$, which we refer to as the Koopman reachable set (KRS), is found by solving the optimization (7), which is computed efficiently by `auto_LiRPA`:",
         join_previous="space"),
    text("p0007-eq7", [84.0, 359.0, 528.0, 388.0],
         "$$\n\\hat{\\overline{\\mathcal{X}}}_{0:T} \\doteq \\big\\{ \\textsf{Int}\\big( \\textstyle\\min_{\\substack{x_0 \\in \\mathcal{X}_0}} \\underline{\\Gamma}_t(x_0, u^{\\text{ref}}_{0:T-1}, z^{\\text{ref}}_{0:T}), \\max_{\\substack{x_0 \\in \\mathcal{X}_0}} \\overline{\\Gamma}_t(x_0, u^{\\text{ref}}_{0:T-1}, z^{\\text{ref}}_{0:T}) \\big) \\big\\}_{t=0}^{T} \\tag{7}\n$$"),
    text("p0007-krs", [89.0, 389.0, 523.0, 429.0],
         r"The KRS $\hat{\overline{\mathcal{X}}}_{0:T}$ overapproximates $\hat{x}_{0:T}$ so that $\hat{x}_{t} \in \hat{\overline{\mathcal{X}}}_{t}$, for all $t \in \mathcal{T}$, ensuring the decoded closed-loop lifted dynamics (5) remain in $\hat{\overline{\mathcal{X}}}_{0:T}$. Formally, we state the following result (proof in App. 8.1):"),
    text("p0007-b005", [89.0, 434.0, 523.0, 485.0],
         r"**Lemma 1 (KRS overapproximation)** Let $\Gamma$ denote the closed-loop CG of TKFL, and let $\mathcal{X}_0$ be the initial set. Suppose the KRS $\hat{\overline{\mathcal{X}}}_{0:T}$ is defined as in (7). Then, for any initial state $x_0 \in \mathcal{X}_0$, the decoded closed-loop trajectory (5), i.e., $\hat{x}_{0:T} = \Gamma(x_0, z^{\text{ref}}_{0:T}, u^{\text{ref}}_{0:T-1})$ satisfies $\hat{x}_t \in \hat{\mathcal{X}}_t$ for all $t \in \mathcal{T}$."),
    text("p0007-b006", B(P, "p0007-b006"), ital(O(P, "p0007-b006"))),
    figure("p0007-b001", [118.0, 84.0, 496.0, 260.0], "Figure 2", "figure-2"),
    caption("p0007-b002", B(P, "p0007-b002"), O(P, "p0007-b002")),
    heading("p0007-b007", B(P, "p0007-b007"), "### 5.4. Conformalizing Koopman Reachable Sets"),
    text("p0007-b008", B(P, "p0007-b008"),
         r"We now explain how to inflate the KRS to guarantee it contains the true system (1b) trajectories with a user-specified probability $1-\delta$. We use CP to compute a high-probability upper bound on the state-space prediction error of the decoded closed-loop lifted dynamics (5). Specifically, we adapt the single nonconformity score approach (SNSA) (Lindemann et al., 2024) to compute state- and dimension-dependent error bounds using a calibration dataset $\mathcal{D}_C = \{(x_{0:T}^{(i)}, \hat x_{0:T}^{(i)})\}_{i=1}^{K^\textrm{cal}}$ of trajectories of the true closed-loop dynamics $x_{0:T}$ (1b) and the decoded closed-loop lifted dynamics $\hat x_{0:T}$ (5). To construct each data tuple in $\mathcal{D}_C$, we sample a reference trajectory $x_{0:T}^{\text{ref},(i)}$ from planner $P$ and an initial state $x_0^{(i)}$ uniformly from $\mathcal{B}_{\epsilon}(x_{0}^{\text{ref}})$. We then compute the latent reference trajectory $z_{0:T}^{\text{ref}, (i)} = \{\phi(x_{t}^{\text{ref},(i)})\}_{t=0}^T$ and the feedforward control sequence $u_{0:T-1}^{\text{ref}, (i)}$ using (2). We use $u_{0:T-1}^{\text{ref}, (i)}$ to calculate the trajectory returned by 1) tracking $z_{0:T}^{\text{ref}}$ in the lifted state space (8) and decoding to the state space via $\psi$ and 2) executing the Koopman controller on the true *nonlinear dynamics* (9):"),
    run_header(P),
    page_number(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 7, a 220 dpi crop of Figure 2, a 250 dpi crop of display (7) and Lemma 1,
and with methodology.tex (macros expanded: \tnfl = \Gamma, \zref = z^{\text{ref}}, \uref = u^{\text{ref}}, \enc =
\phi, \dec = \psi). Figure 2 (block diagram, vector graphics with native text: 'latent input set, reference
generation', 'reference controller generation', 'Koopman dynamics', 'target nonlinear system', 'Koopman LQR',
'samples', 'conformal prediction', 'Koopman reachable set (KRS)', 'conformalized Koopman reachable set (CKRS)', the
'T times, t in {0, ..., T-1}' loops and all math labels) is printed at the top of the page; the extractor had
classified it as a table with leaked '<latexit>' base64 strings. It is now one figure crop 'figure-2' [118, 84, 496,
260] with every label inside (edges checked on the 220 dpi crop); the extractor text was deleted after checking that
it lies inside the crop. Caption verbatim ('ScaRe-Kro'). Placement: the first text item continues the sentence of
page 6 ('... that bound the states / reached under (5) at timestep t, ...', join_previous 'space'), so Figure 2 and
its caption are placed after the paragraph 'Crucially, ... This motivates Sec. 5.4.', i.e. at the end of Section 5.3
which discusses the figure. 'hyper-/rectangular' is a real compound (restored). Display (7) from the TeX with \tag{7}
(\small and the negative \hspace dropped; \textstyle kept because it places the min/max subscripts beside the
operators as printed). The extractor's formula box had swallowed the prose paragraph 'The KRS ... (proof in App.
8.1):', now its own text item. Lemma 1: bold label 'Lemma 1 (KRS overapproximation)' as printed, no trailing
punctuation; italic body (not reproduced); ends with '... for all t in T.' (end of the TeX lemma environment); 'ref'
printed italic inside the statement. As printed, the Lemma concludes '$\hat{x}_t \in \hat{\mathcal{X}}_t$' with a hat
but without the overline of the KRS symbol (checked at 250 dpi; same in the TeX). 'Crucially ...' paragraph: italic
'not the true nonlinear dynamics' kept. Heading '5.4. Conformalizing Koopman Reachable Sets' level 3. Last paragraph
from the TeX: 'state- and dimension-dependent' keeps the printed suspended hyphen; 'tra-jectories' closed up; italic
'nonlinear dynamics'; K^cal written with \textrm{cal} as in the TeX; the paragraph ends with '(9):' and the displays
(8)-(9) follow on page 8 (no join needed). Citation (Lindemann et al., 2024). Omitted: running header (short title)
and page number 7.
""")
