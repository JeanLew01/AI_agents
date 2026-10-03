from pagelib import *
o = orig(15)
B = lambda k: o[k]["bbox"]

items = [
    figure("p0015-b000", [100.0, 140.0, 506.0, 351.0], "Figure 4", "figure-4"),
    caption("p0015-b001", [90.0, 353.5, 523.0, 380.0], X(
         r"""Figure 4: Shows the projection of our $\delta$-confident flowpipe on each component of the trajectory state. The shaded area are the simulation of trajectories from $\traindataset$.""")),
    figure("p0015-b003", [80.0, 468.0, 423.0, 603.0], "Figure 5", "figure-5"),
    caption("p0015-b005", [90.0, 606.0, 420.0, 660.0], X(
         r"""Figure 5: Shows the projection of our $\delta$-confident flowpipe on the first $8$ components of the trajectory state. There is a shift between the distribution of deployment and training environments. The shaded area are the trajectories sampled from the deployment environment.""")),
    figure("p0015-b002", [425.0, 466.0, 520.0, 558.0], "Figure 6", "figure-6"),
    caption("p0015-b004", [426.0, 565.0, 520.0, 660.0],
         "Figure 6: Shows the comparison of angular velocity of the last rotating mass in presence and absence of the process noise."),
    omit("p0015-b006", B("p0015-b006"), "15",
         "Printed page number 15 centred at the foot of the page; page furniture, checked on the 170 dpi render."),
]

save(15, items, r"""
Compared with the 170 dpi render, two 220 dpi crops (Figure 4; Figures 5 and 6 with their captions) and the TeX source
(sections/Appendix.tex). The page contains only three floats and their captions. Figure 4: one crop with all 12 panels ($x_1$ to
$x_{12}$), tick labels and in-panel labels 'time(seconds)'; Figure 5: one crop with the 8 panels $x_1$ to $x_8$; Figure 6: the single
panel printed to the right of Figure 5, with its legend ('Absence of process noise', 'Presence of process noise'), the label $x_{27}$,
tick labels and 'time (seconds)'. All three bboxes come from ink profiles of the render (Figure 4 ink 106.3-499.8 x 144.8-346.4 pt,
caption from 355.0 pt; Figure 5 ink 86.8-418.4 x 475.6-598.0 pt, caption from 607.8 pt; Figure 6 ink 429.5-515.4 x 470.1-554.4 pt,
caption from 567.5 pt); the crops do not overlap each other or the captions. The extractor had the bboxes of Figures 5 and 6
overlapping and had put plot tick labels into the figure items' text; tick and legend text is kept only inside the crops. Captions
verbatim, with $\delta$, $8$ and $\mathcal{T}^{\mathsf{trn}}$ in LaTeX ('The shaded area are ...' is printed so, in both captions). The
caption of Figure 6 is set in a narrow column (two or three words per line); no word is hyphenated. plan.json 'reading_order' places
Figure 4 after the end of Section A.2 and Figures 5 and 6 after Section A.3 (page 16), i.e. each after the text that cites it (Figure 6
is cited in Section 4.2, 'Figure 6 shows the angular velocity of the last rotating mass', and is printed here beside Figure 5). Small
tick labels inside Figures 4 and 5 are legible only at 220 dpi or more. Omitted: page number 15.
""")
