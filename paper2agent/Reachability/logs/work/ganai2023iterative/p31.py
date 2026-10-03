from pagelib import *
P = 31
items = [
    heading("p0031-b000", B(P, "p0031-b000"), "### D.9 Ablation – Learning Rate"),
    figure("p0031-fig13", [107.0, 97.0, 504.0, 392.0], "Figure 13", "supplementary-figure-13", asset_category="supp_figs"),
    caption("p0031-b002", [107.0, 393.0, 505.0, 402.0], O(P, "p0031-b002")),
    text("p0031-b003", B(P, "p0031-b003"),
         r"""We performance Ablation study of varying the learning rate of the REF function to verify the importance of the multi-timescale assumption. Particular, we compare our algorithm’s approach of placing the learning rate of the REF between the policy and lagrange multiplier with making the REF’s learning rate in various orders of magnitudes slower and faster. Our approach with the learning rate satisfying the multi-timescale assumption experimentally appears to still have the best balance of reward optimization and constraint satisfaction. Particularly when we change the learning rate by one order of magnitude (i.e. $\times10$ or $\times0.1$), we see the reward performance reduce by around half and while the cost violations generally don’t change. But when we change the learning rates by another order of magnitude, there reward performance effective becomes zero and the cost violations generally reduce further. By increasing the learning rate of the REF function, we can no longer guarantee that the REF convergences to near the optimally safe REF value. Instead, it becomes the REF of the policy in question. So instead, the optimization can learn to “hack" the REF function to obtain a policy (and lagrange multiplier) that is not a local optimal for the optimization formulation. On the other hand, when the learning rate is too slow, the lagrange multiplier quickly explodes, thereby creating a very conservative solution – notice the similarity of the orange line in Figure 13 with learning rate $0.01$ times that of standard in training behavior with **PPOLag** where $\chi=0$ in the ablation study on optimization."""),
    pageno(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 31, a 100 dpi crop of Figure 13, and with main.tex (D.9). Figure 13
(appendix): one crop of the four panels in a 2x2 grid, 'CarGoal Cumulative Rewards', 'CarGoal Cumulative Costs' (top),
'PointButton Cumulative Rewards', 'PointButton Cumulative Costs' (bottom), '1e6' on all x axes, legend in the first
panel: 'RESPO w/ lr*0.01' (orange), 'RESPO w/ lr*0.1' (purple), 'RESPO' (red, thick), 'RESPO w/ lr*10' (green),
'RESPO w/ lr*100' (blue); an enlarged version of Figure 5. Asset name 'supplementary-figure-13', category supp_figs,
printed label 'Figure 13' kept; bbox from the evidence line extent (116.0-497.7 x 99.3-390.1 pt) with a margin, ending
above the caption (393.3 pt); checked on the crop. Caption verbatim (centred one-line caption). The single paragraph
was taken from the TeX source and checked on the render: mathematics '$\times10$ or $\times0.1$', '$0.01$' and
'$\chi=0$' in LaTeX; bold 'PPOLag'; en dash in 'solution – notice'; the quotation marks around 'hack' are printed as
an opening curly double quote and a straight closing double quote (kept). Authors' wording kept: 'We performance
Ablation study', 'Particular, we compare', 'reduce by around half and while', 'there reward performance effective
becomes zero', 'convergences', 'not a local optimal', 'lagrange multiplier'. Reference 'Figure 13' as printed. The
heading is printed with an en dash ('D.9 Ablation – Learning Rate'), level 3. The lower part of the page is blank.
Omitted: printed page number 31.
""")
