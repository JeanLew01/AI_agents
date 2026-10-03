from pagelib import *
P = 10
items = [
    figure("p0010-b000", [46.0, 67.0, 572.0, 362.0], "Figure 2", "figure-2"),
    caption("p0010-b001", B(P, "p0010-b001"),
            r"Figure 2: Quadcopter: The black lines indicate the probabilistic flowpipe computed using the exact-star technique on the learned surrogate model combined with conformal inference with failure probability $\varepsilon=0.01$. The green shaded areas and blue lines are computed from 100000 random trajectories from the ODE model. The green area shows the maximum and minimum value of trajectory components over this dataset, and the blue line represents their average value."),
    text("p0010-b002", [71.0, 456.0, 540.0, 497.0],
         r"also train our surrogate model as a neural network with layers $[12, 20, 20, 20, 12]$ from an additional training dataset. The run time for our data-driven reachability analysis is shown in Table 2 and the projections of the probabilistic flowpipes onto its state components for $\varepsilon = 0.01$ is shown in Fig. 2.",
         join_previous="space"),
    text("p0010-b002b", [71.0, 499.0, 540.0, 578.0],
         r"*Laubloomis.* Finally, we consider a 7-dimensional system which is known as Laubloomis [6]. The ODE model for Laubloomis is shown in Eq. (8). To provide a comparison with deterministic reachability analysis techniques, we do not add noise to the system in this case so that the system is effectively deterministic. However, note that in our approach we need to sample the initial conditions. We thus generate a test dataset of size $L =160000$ consisting of 200-step trajectories with sampling time $\delta t =0.01$."),
    display("p0010-b003", B(P, "p0010-b003"),
            r"\begin{bmatrix}\dot{x}_1\\ \dot{x}_2\\ \dot{x}_3\\ \dot{x}_4\\ \dot{x}_5\\ \dot{x}_6\\ \dot{x}_7\end{bmatrix} =\begin{bmatrix} 1.4 x_3-0.9 x_1\\ 2.5 x_5-1.5 x_2\\ 0.6  x_7-0.8 x_3 x_2\\ 2.0-1.3 x_4 x_3\\ 0.7 x_1-1.0 x_4 x_5\\ 0.3 x_1-3.1 x_6 \\ 1.8 x_6-1.5  x_7 x_2 \end{bmatrix}, \ \  \mathcal{I}=\left\{  s_0\ \middle| \  \begin{bmatrix} 1.05\\ 0.9\\ 1.35\\ 2.25\\ 0.85\\ -0.05\\ 0.3 \end{bmatrix} \leq s_0 \leq \begin{bmatrix} 1.35\\ 1.2\\ 1.65\\ 2.55\\ 1.15\\ 0.25\\ 0.6\end{bmatrix} \right\} \tag{8}"),
    pageno(P),
]
save(P, items, r"""
Compared with the 130 dpi render, a 200 dpi crop of the text and equation and a crop of the figure region of PDF page 10,
and with sections/experimental_results.tex. Figure 2 (twelve panels $x_1,\ldots,x_{12}$ in three rows of four, small tick
labels, no axis titles) is one image crop wider than the text block; all four edges were checked (tick labels of the
leftmost column and the '50' ticks at the right edge complete, caption excluded). Caption verbatim; it differs from the
Figure 1 caption only in 'Quadcopter' and 'of trajectory components' (no 'the'). The figure is a float printed at the top
of the page in the middle of the Quadcopter paragraph; in the reading order it follows that paragraph. The item 'also
train our surrogate model ...' continues the page-9 sentence ('We | also train') with join_previous 'space'. The extractor
had merged that continuation with the Laubloomis paragraph; they are separate items now (paragraph break at y about
498 pt). Equation (8) (Laubloomis dynamics and initial set) replaces the extractor's 'formula' image; it is taken from
the TeX source and was checked entry by entry on the 200 dpi crop: $1.4x_3-0.9x_1$, $2.5x_5-1.5x_2$,
$0.6x_7-0.8x_3x_2$, $2.0-1.3x_4x_3$, $0.7x_1-1.0x_4x_5$, $0.3x_1-3.1x_6$, $1.8x_6-1.5x_7x_2$; lower bounds 1.05, 0.9,
1.35, 2.25, 0.85, -0.05, 0.3 and upper bounds 1.35, 1.2, 1.65, 2.55, 1.15, 0.25, 0.6; printed number (8) as \tag.
Equation (7), referred to in the Quadcopter paragraph, is printed as a float on page 12. Spaces after the commas were
added in the layer list '$[12, 20, 20, 20, 12]$'. Kept as printed: 'the projections ... is shown in Fig. 2'; the
sampling time '$\delta t = 0.01$' without a unit; the run-in italic title 'Laubloomis.'. References checked on the page:
Table 2, Fig. 2, [6], Eq. (8).
""")
