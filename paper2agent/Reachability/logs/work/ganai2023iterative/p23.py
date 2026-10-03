from pagelib import *
P = 23
FR = r"\frac{\phi(s)}{(1 - \phi(s))}"
items = [
    text("p0023-b000", B(P, "p0023-b000"), r"So we can find the bound for $\lambda_{\max}$:"),
    display("p0023-b001", B(P, "p0023-b001"), r"""\begin{aligned}
\Delta \mathbb{E}_{s\sim d_0} [V(s)\cdot (1-\phi(s))] &< \Delta \mathbb{E}_{s\sim d_0} [V_c(s)\cdot (\lambda\cdot (1 - \phi(s)) + \phi(s)) ]\\
\Delta \mathbb{E}_{s\sim d_0} [V(s)] &< \Delta \mathbb{E}_{s\sim d_0} [V_c(s)\cdot (\lambda + \frac{\phi(s)}{(1 - \phi(s))}) ]\\
\frac{R_{\max}}{1-\gamma} &< \gamma^T\cdot H_{\Delta}\cdot P_{\min}\cdot (\lambda+\frac{\phi(s)}{(1 - \phi(s))})\\
\frac{R_{\max}}{(1-\gamma)\cdot\gamma^T\cdot H_{\Delta}\cdot P_{\min}} &<\lambda+\frac{\phi(s)}{(1 - \phi(s))} \\
\frac{R_{\max}}{(1-\gamma)\cdot\gamma^T\cdot H_{\Delta}\cdot P_{\min}} - \frac{\phi(s)}{(1-\phi(s))} &<\lambda
\end{aligned}"""),
    text("p0023-b002", B(P, "p0023-b002"),
         r"The second line holds since we are simply rearranging the comparative weightages of the reward and cost returns. Now $- \frac{\phi(s)}{(1-\phi(s))}\leq 0$ (recall that if $\phi(s)=1$, then $\lambda$ is irrelevant in the lagrangian optimization). Thus, if $\lambda>\frac{R_{\max}}{(1-\gamma)\cdot\gamma^T\cdot H_{\Delta}\cdot P_{\min}}$ then minimizing the cost returns is prioritized over maximizing reward returns."),
    heading("p0023-b003", B(P, "p0023-b003"), "## D Complete Experiment Details and Analysis"),
    heading("p0023-b004", B(P, "p0023-b004"), "### D.1 Baselines"),
    text("p0023-b005", B(P, "p0023-b005"),
         r"We compare our algorithm **RESPO** with $7$ other safety RL baselines, which can be divided to CMDP class and hard constraints class, and unconstrained Vanilla PPO for reference."),
    text("p0023-b006", B(P, "p0023-b006"), r"CMDP Approaches"),
    text("p0023-b007", B(P, "p0023-b007"), lead_italic(O(P, "p0023-b007"))),
    text("p0023-b008", B(P, "p0023-b008"), lead_italic(O(P, "p0023-b008"))),
    text("p0023-b009", B(P, "p0023-b009"), lead_italic(O(P, "p0023-b009"))),
    text("p0023-b010", B(P, "p0023-b010"), lead_italic(O(P, "p0023-b010"))),
    text("p0023-b011", B(P, "p0023-b011"), r"Hard Constraints Approaches"),
    text("p0023-b012", B(P, "p0023-b012"), lead_italic(O(P, "p0023-b012"))),
    text("p0023-b013", B(P, "p0023-b013"),
         r"*Control Barrier Function.* This **CBF**-based approach is inspired by the various energy-based certification approaches [56, 17, 18, 11, 57, 58]. This is implemented as a primal-dual approach where the control barrier-based constraint $\dot{h}(s) + \nu\cdot h(s)\leq 0$ is to ensure stabilization toward the safe set."),
    text("p0023-b014", B(P, "p0023-b014"), lead_italic(O(P, "p0023-b014", ("_χ_ = 0", r"$\chi=0$")))),
    pageno(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 23 and with main.tex (end of C.4.4; D and D.1). The five-line derivation of
the bound on $\lambda$ (extractor formula image) was rewritten in LaTeX from the TeX source as one aligned block
(aligned at the '<' signs, unnumbered, no punctuation) and checked line by line on the render: (1) weighted comparison
with $(1-\phi(s))$, (2) division by $(1-\phi(s))$, (3) insertion of the two bounds from page 22, (4) and (5) solved
for $\lambda$. The following paragraph was rebuilt from the source (the extractor had underlined glyph debris from
the two inline fractions); as printed the final threshold is
$\lambda>\frac{R_{\max}}{(1-\gamma)\cdot\gamma^T\cdot H_{\Delta}\cdot P_{\min}}$ and $\phi(s)$ carries no
superscript. Appendix D: heading 'D Complete Experiment Details and Analysis' level 2, 'D.1 Baselines' level 3. The
two group labels 'CMDP Approaches' and 'Hard Constraints Approaches' are printed as underlined lines of normal text
(not numbered headings; the extractor had made them headings); they are kept as plain one-line paragraphs without
underline markup. Each baseline paragraph starts with a run-in italic title ending in a full stop followed by the bold
abbreviation; italics and bold kept as printed (PPOLag, CRPO, P3O, PCPO, RCRL, CBF, FAC, RESPO). Prose paragraphs:
extractor text compared with render and TeX and used with the emphasis markers normalised; mathematics restored in
'with $7$ other safety RL baselines', the CBF constraint $\dot{h}(s)+\nu\cdot h(s)\leq 0$ (dot over h checked) and
'$\chi=0$'. The citation list '[56, 17, 18, 11, 57, 58]' is in this printed order; other citations [33], [7], [35],
[32], [3], [27], [9] checked. Line-wrap hyphen removed in 'certification'; en dash in 'likelihood – both approaches'
as printed. Authors' wording kept: 'based off of', 'can be divided to', 'cumulative discount sum of costs',
'lagrange multiplier'. Omitted: printed page number 23.
""")
