from pagelib import *
from refs import entries
o = orig(14)
B = lambda k: o[k]["bbox"]
R = dict(entries)

items = [
    text("p0014-b002", B("p0014-b002"), R["tumu2024multi"]),
    text("p0014-b003", B("p0014-b003"), R["vovk2012conditional"]),
    text("p0014-b004", B("p0014-b004"), R["zecchin2024forking"]),
    text("p0014-b005", B("p0014-b005"), R["zhang2023reachability"]),
    heading("p0014-b006", B("p0014-b006"), "## Appendix A. Detail of the Experiments"),
    heading("p0014-b007", B("p0014-b007"), "### A.1 Experiment 1:[Comparison with Hashemi et al. (2024b)]"),
    text("p0014-b008", B("p0014-b008"), X(
         r"""Here we address Experiment 2 from Hashemi et al. (2024b) for comparison of the results. In this experiment, a quadcopter hovers at a specific elevation, and its trajectories are simulated over a horizon of $\horizon = 100$ time steps, with a sampling time of $\delta t = 0.05$. The $\delta$-confident flowpipe has a confidence level of $\delta =$ 99.99%. Compared to Hashemi et al. (2024b), our approach achieves a higher level of accuracy. This improvement is due to our training strategy, which allows us to use exact-star for surrogate reachability, and our PCA-based technique, which results in smaller inflating hypercubes. In this experiment, we use a trajectory division""")),
    figure("p0014-b000", [96.0, 85.0, 510.0, 293.0], "Figure 3", "figure-3"),
    caption("p0014-b001", [90.0, 297.0, 522.0, 337.0], X(
         r"""Figure 3: Shows the comparison with Hashemi et al. (2024b). The blue and red borders are projections of our and their $\delta$-confident flowpipes respectively with $\delta =$ 99.99%. The shaded regions show the density of the trajectories from $\traindataset$.""")),
    omit("p0014-b009", B("p0014-b009"), "14",
         "Printed page number 14 centred at the foot of the page; page furniture, checked on the 170 dpi render."),
]

save(14, items, r"""
Compared with the 170 dpi render, a 220 dpi crop of Figure 3 with margins, and the TeX source (neus2025-arxiv.bbl,
sections/Appendix.tex). The page prints Figure 3 (a float) at the top, between the bibliography entries of page 13 and the last four
entries; the items are ordered so that the bibliography reads continuously: the four entries (Tumu et al. 2024, Vovk 2012, Zecchin et
al. 2024, Zhang et al. 2023; generated from the .bbl, alphanumeric content identical to the PDF text layer, read on the render;
'tem-plates' line-wrap hyphen removed), then the appendix headings and the first part of the A.1 paragraph, then Figure 3 with its
caption. plan.json 'reading_order' places Figure 3 and its caption after the end of the A.1 paragraph (which continues on page 16 and
is the text that cites Figure 3). Headings as printed: 'Appendix A. Detail of the Experiments' (##) and 'A.1 Experiment 1:[Comparison
with Hashemi et al. (2024b)]' (###; no space after the colon in the print, the square brackets are printed). A.1 paragraph: math from
the TeX ($\mathrm{K}=100$, $\delta t=0.05$, '$\delta$ = 99.99%' written with the percent sign outside the math so that the number
stays searchable); note that it says 'Here we address Experiment 2 from Hashemi et al. (2024b)' (the experiment number in the cited
paper). The paragraph is cut by the page break after 'we use a trajectory division'; page 15 holds only floats and the paragraph
continues on page 16 (join_previous 'space', resolved in reading order). Figure 3: one image crop with all 12 panels ($x_1$ to
$x_{12}$), their tick labels and the in-panel axis labels 'time (seconds)'; bbox from an ink profile (figure ink 100.4-505.7 x
88.9-289.7 pt, caption from 298.7 pt). The tick labels are part of the figure and are not transcribed; as printed, the horizontal
tick labels of panel $x_4$ read '-1.5 0 1.5 -1.5 0 1.5' and those of panel $x_5$ '-2 -1 0 1 2 -2' (unlike the other panels, 0-5), and
some tick labels are very small (legible only at 220 dpi or more). Figures 3-6 are numbered in the main sequence although they are printed
in the appendix; they keep the asset names figure-3 ... figure-6 in the main figure category. Caption verbatim. Omitted: page number
14.
""")
