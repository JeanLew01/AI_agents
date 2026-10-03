from pagelib import *
P = 26
items = [
    heading("p0026-b000", B(P, "p0026-b000"), "### D.4 Double Integrator"),
    figure("p0026-fig8", [188.0, 99.0, 424.0, 314.5], "Figure 8", "supplementary-figure-8", asset_category="supp_figs"),
    caption("p0026-b002", [107.0, 316.5, 505.0, 366.0], O(P, "p0026-b002")),
    text("p0026-b003", B(P, "p0026-b003"),
         r"We use the Double Integrator environment as a motivating example to demonstrate how performing constrained optimization using solely reachability-based value functions as in **RCRL** can produce nonoptimal behavior when the agent is outside the feasiblity set. Double Integrator has a 2 dimensional observation space $[x_1, x_2]$, 1 dimension action space $a\in[-0.5,0.5]$, system dynamics is $\dot{s} = [x_2, a]$, and constraint as $||s||_\infty \leq 5$. Particularly, we make the cost as $1$ if $||s||_\infty > 5$, and $0$ otherwise to emphasize the importance of capturing the frequency of violation during training."),
    text("p0026-b004", B(P, "p0026-b004"), tidy(O(P, "p0026-b004", ("or near 1 in the infeasible set", "or near $1$ in the infeasible set")))),
    pageno(P),
]
for i in items:
    assert "** ." not in i["markdown"], i["id"]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 26, a 120 dpi crop of Figure 8, and with main.tex (D.4). Figure 8 (appendix
figure, printed directly under the heading): phase-plane plot on $[-10,10]^2$ with a yellow background labelled
'Infeasible Set', a blue region labelled 'Feasible Set' with a black boundary, a dashed purple square (corners at
about +-5) and two trajectories from the point marked 'Start' (near (2.7, 2.5)): a red arrow leaving to the right
(RCRL) and a green curve that loops back into the blue region (RESPO); legend 'RESPO (ours)', 'RCRL', 'Safe set
boundry' (sic, spelling inside the figure). Asset name 'supplementary-figure-8', category supp_figs, printed label
'Figure 8' kept; the extractor's box overlapped the caption, bbox reset from the evidence line positions and checked
on the crop (all tick labels and the legend inside). Caption: extractor text compared with render and TeX and used
unchanged. First paragraph rewritten from the TeX source with LaTeX mathematics checked on the render: observation
space $[x_1,x_2]$, action space $a\in[-0.5,0.5]$ (ASCII minus in LaTeX), dynamics $\dot{s}=[x_2,a]$ with a dot over
s, constraint $||s||_\infty\leq 5$, cost $1$ if $||s||_\infty>5$ and $0$ otherwise; the plain numerals in '2
dimensional' and '1 dimension' are text in the source. Second paragraph: extractor text checked and used with the
space before the full stop after bold 'RESPO' removed and the math-mode '$1$' restored. Bold RCRL / RESPO as printed.
Authors' wording kept: 'feasiblity set', '1 dimension action space', 'constraint as', 'magnitude same or less',
'reentering' and 're-entering' (both spellings occur). Reference 'Figure 8' as printed. The lower third of the page is
blank (page break in the source). Heading D.4 level 3. Omitted: printed page number 26.
""")
