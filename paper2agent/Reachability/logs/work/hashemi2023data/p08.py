from pagelib import *
P = 8
items = [
    figure("p0008-b000", [67.0, 67.0, 545.0, 336.0], "Figure 1", "figure-1"),
    caption("p0008-b001", B(P, "p0008-b001"),
            r"Figure 1: Adaptive Cruise Control: The black lines indicate the probabilistic flowpipe computed using the exact-star technique on the learned surrogate model combined with conformal inference with failure probability $\varepsilon=0.01$. The green shaded areas and blue lines are computed from 100000 random trajectories from the ODE model. The green area shows the maximum and minimum value of the trajectory components over this dataset, and the blue line represents their average value."),
    text("p0008-b002", B(P, "p0008-b002"),
         r"equivalent to $\delta= 1- \frac{1-\Delta}{n\mathrm{K}}$. The minimum required size $L$ of the calibration dataset has to satisfy $\lceil (L + 1)\delta \rceil \leq L$ which gives us the explicit lower bound $L \geq \lceil \frac{1+\delta}{1-\delta} \rceil$. In this work, we defined the residual component-wise, recall Definition 3. As observed in the proof of Theorem 1, we thus had to apply the union bound over all residuals $R^j$. This may in some cases be conservative, i.e., for large system dimension $n$ or large trajectory horizon $\mathrm{K}$. However, there are possible ways to define a residual in a way that removes this conservatism. For example, in our recent work [36] we show how to obtain tight conformal prediction regions for time series. Applying this method will also result in better data efficiency. We intend to explore this method in the context of this paper in future work and refer the reader to [36] for more details.",
         join_previous="space"),
    heading("p0008-b003", B(P, "p0008-b003"), "## 4 Experimental Results"),
    text("p0008-b004", B(P, "p0008-b004"),
         r"We consider an adaptive cruise controller, a quadcopter, and the Laubloomis benchmarks in [6]. In all case studies, we train 1-step surrogate models that we combine into a $\mathrm{K}$-step surrogate model for trajectory prediction. For reachability analysis of the surrogate model we use the approx-star algorithm from [21] for the Laubloomis case study, while we use the exact-star algorithm from [21] for the adaptive cruise controller and the quadcopter. The underlying system is described by an ordinary differential equation (ODE), potentially affected by noise, and we consider the system at discrete time points. Therefore, we let the control input and the noise be fixed over the sampling"),
    pageno(P),
]
save(P, items, r"""
Compared with the 130 dpi render, a 190 dpi crop of the text and a crop of the figure region of PDF page 8, and with
sections/verification.tex and sections/experimental_results.tex. Figure 1 (six panels $x_1,\ldots,x_6$ with tick labels
and the in-plot axis text 'Time steps') is one image crop; all four edges were checked on the crop (tick labels 250/90 on
the left, 50 on the right, the bottom tick row complete, caption excluded). The extractor produced no stray text items
from the figure. Caption verbatim, with $\varepsilon=0.01$ in LaTeX; '100000' printed without a separator. The figure is
a float printed at the top of this page, in the middle of the sentence that runs from page 7 to this page; in the reading
order it is moved to the Adaptive Cruise Control paragraph of Section 4 that refers to it (page 9). The text item
'equivalent to ...' continues the page-7 sentence with join_previous 'space'. Its two inline fractions were read on the
190 dpi crop and agree with the TeX source: $\delta = 1-\frac{1-\Delta}{n\mathrm{K}}$ and
$L \ge \lceil\frac{1+\delta}{1-\delta}\rceil$; the extractor had turned this passage into glyph soup with sup tags and
glued words, and it was rewritten from the TeX source. The explicit bound is kept as printed, with numerator $1+\delta$; by itself the stated condition
$\lceil (L+1)\delta\rceil\le L$ is equivalent to $L\ge\delta/(1-\delta)$, so the printed bound is larger than what the
condition requires (reviewer's arithmetic remark, not a statement of the paper). Spaces were put around the plus sign in
'$(L + 1)\delta$' as printed. References 'Definition 3', 'Theorem 1', [36] (twice), [6], [21]
(twice) checked on the page. '1-step' is typed $1$-step in the TeX and written as plain text. Section heading
'4 Experimental Results' is level 2. The last paragraph ends in the middle of a sentence ('fixed over the sampling'); it
continues on page 9 below Table 1.
""")
