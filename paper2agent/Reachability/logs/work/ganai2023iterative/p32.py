from pagelib import *
P = 32
items = [
    heading("p0032-b000", B(P, "p0032-b000"), "### D.10 Ablation – Optimization"),
    figure("p0032-fig14", [107.0, 121.0, 504.0, 709.5], "Figure 14", "supplementary-figure-14", asset_category="supp_figs"),
    caption("p0032-b002", [107.0, 710.5, 505.0, 719.5], O(P, "p0032-b002")),
    pageno(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 32 and a 90 dpi crop of Figure 14, and with main.tex (D.10). The page holds
only the heading, Figure 14 and its caption; the discussion paragraph of D.10 is on page 33. Figure 14 (appendix): one
crop of the eight panels in a 4x2 grid, rows CarGoal, PointButton, BallRun, DroneCircle, left column 'Cumulative
Rewards', right column 'Cumulative Costs' (scale factors x10^2 on PointButton costs, BallRun costs and DroneCircle
rewards, x10^3 on BallRun rewards; '1e6' on all x axes; dashed horizontal lines in the cost panels), legend in the
first panel: 'PPOLag, chi = 0' (blue), 'RCRL with REF' (orange), 'RESPO (ours)' (red, thick); an enlarged version of
Figure 6. Asset name 'supplementary-figure-14', category supp_figs, printed label 'Figure 14' kept; bbox from the
evidence line extent (114.4-497.6 x 121.8-707.7 pt) with a margin, ending above the caption (710.9 pt); checked on the
crop (all tick labels, scale factors and '1e6' exponents inside). Caption verbatim. The heading is printed with an en
dash ('D.10 Ablation – Optimization'), level 3. Omitted: printed page number 32.
""")
P = 33
items = [
    text("p0033-b000", B(P, "p0033-b000"),
         r"In this ablation study, we examine the various optimization frameworks within the context of hard constraints. Particularly, we compare our **RESPO** framework with **RCRL** and **CMDP**. However, for **RCRL** we implement using our REF function method while still keeping the reachability value function. For **CMDP**, we make the cost threshold $\chi=0$. These comparisons answer important questions about our design choices – specifically is it sufficient to simply to just use the REF component or to just learn the cost returns alone? From this ablation study, we propose that though we have provided theoretical support for adding each of these design components individually, in practice they are both required together in our algorithm. In **RCRL** implemented with our REF, we generally see decently high rewards but the cost violations are always very large. This highlights the problems of the reachability function again – if the agent starts or ever wanders into the infeasible set, there is no guarantee of (re)entrance into the feasible set. So the agent can indefinitely remain in the infeasible set, thereby incurring potentially an unlimited number of constraint violations. In **PPOLag** with $\chi=0$, both the reward performance and constraint violations are very low. By using such hard constraints versions of these purely learning-based methods, even when using the cumulative discounted cost rather than reachability value function, the reward performance is very low because the lagrange multiplier becomes too large quickly and thereby overshadows the reward returns in the optimization. Ultimately, both the REF approach and the usage of the cumulative discounted costs are important components of our algorithm **RESPO** that encourage a good balance between the reward performance and safety constraint satisfaction in such stochastic settings."),
    pageno(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 33 (last page) and with main.tex (the paragraph of D.10 that follows Figure
14). One paragraph, taken from the TeX source and read against the render line by line (19 printed lines): bold RESPO,
RCRL, CMDP, PPOLag as printed; '$\chi=0$' twice in LaTeX; two en dashes ('design choices – specifically', 'function
again – if'). Authors' wording kept: 'is it sufficient to simply to just use the REF component', 'hard constraints
versions', 'lagrange multiplier'. This paragraph belongs to Section D.10, whose heading and figure are on page 32; it
is a new paragraph, so no join is used. The rest of the page is blank; the paper ends here. Omitted: printed page
number 33.
""")
