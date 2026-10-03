from pagelib import *

items = [
    header(6),
    heading("p0006-b001", [89.0, 94.0, 506.0, 105.0],
            "### 4.1. Comparison of Robust and Iterative Scenario-Based Probabilistic Safety Verification"),
    text("p0006-b002", [89.0, 108.0, 523.0, 186.0],
         r"The key difference between the proposed robust scenario-based method and the iterative scenario-based method discussed in Section 3.2 is that the former can handle nonzero empirical safety violations $k$. This enables several crucial advantages that we demonstrate in Figures 1 and 2 for a solution learned by DeepReach on the multi-vehicle collision avoidance running example in Section 2. We have fixed the confidence parameter $\beta = 10^{-16}$ to be so close to $0$ that it has no practical significance ($\beta$ plays the same role in both methods)."),
    figure("p0006-b003", [85.0, 188.0, 229.0, 400.0], "Figure 1", "figure-1"),
    caption("p0006-b005", [229.5, 209.0, 520.0, 369.0],
            r"Figure 1: (Top) For a fixed simulation budget $N$, the cyan curve shows the number of empirical safety violations $k$ for different learned volumes (different super-levels of $" + V + r"(x,0)$). The red curve shows the trade-off in safety strength $\epsilon$ (in log scale) for each $k$ using the robust method. The grey point indicates the iterative method baseline. The robust method is able to provide safety assurances even for the volumes that have non-zero outliers. (Dashed black line) By a small decrease in safety level (from 99.999% to 99.974%) caused by outliers, we are able to significantly increase the assured safe volume from 0.56 to 0.81. (Bottom) Correspondingly, the safe set $\mathcal{S}$ increases greatly from the complement of the grey region to the complement of the blue region."),
    text("p0006-b006", [89.0, 400.5, 523.0, 493.0],
         r"Firstly, for a fixed simulation budget $N$, the robust method allows one to trade off the probabilistic strength of safety (increasing $\epsilon$) for resilience (increasing $k$). In other words, the method can verify any given neural safe set $\mathcal{S}$ in an outlier-robust fashion by automatically attenuating the level of safety assurance based on the number of empirical outliers (i.e., safety violations). The iterative method, in contrast, can only verify a region that is outlier-free. Consequently, the robust method enables one to engage in a trade-off if a large increase in safe set volume can be attained by a tolerable decrease in safety, as illustrated in Figure 1."),
    figure("p0006-b007", [94.0, 493.5, 516.0, 620.0], "Figure 2", "figure-2"),
    caption("p0006-b008", [89.0, 625.0, 523.0, 676.0],
            r"Figure 2: (Left) Computing the safety strength $\epsilon$ across different volumes (different super-levels of $" + V + r"(x,0)$) for different simulation budgets $N$ using the robust method. The grey points indicate the iterative method baselines. (Right) As we increase $N$, the largest volume achieving the desired 99.968% safety using the robust method increases up to a limit."),
    text("p0006-b009", [90.0, 681.0, 523.0, 706.0],
         r"Secondly, by allowing nonzero safety violations $k$, the robust method provides stronger safety assurances for a *fixed* volume with increment in the simulation budget $N$, as long as the outlier rate"),
    pageno(6, "p0006-b010", [303.0, 725.0, 309.0, 733.0]),
]

save(6, items, r"""
Compared the whole page with the 130 dpi render, with 170-200 dpi crops of both figures taken with a margin (to check the
crop edges) and with sections/scenario-based_method.tex. Figure 1 is printed as two stacked panels, (a) and (b), at the
left of its caption; the extractor had made two separate figure items, which are merged into one item 'figure-1' whose
box contains both panels with their titles ('Fixed N = ~3.7M', 'theta_1 = -1.57'), the left and right axis labels
('Volume', 'log10(eps) (% safety)'), all tick labels and the panel letters, and stops just left of the caption text
(checked on an exact 200 dpi crop of the box). Figure 2 is one full-width image with panels (a) and (b), its common title
and all axis labels inside the box. Both captions are separate caption items, transcribed from the TeX source and
compared with the page; percentages and plain numbers are written as plain text (99.999%, 99.974%, 0.56, 0.81, 99.968%).
The figures are JPEG images in the PDF, so their in-figure labels are not in the text layer; the values readable in
Figure 2(b) (N = ~116K, k = 0; N = ~368K, k = 36; N = ~1.2M, k = 193; N = ~3.7M, k = 731) are recorded in the conversion
notes because the caption does not state them. Heading 4.1 is level 3 (the extractor had level 1). Inline mathematics from
the TeX source (beta = 10^{-16}, k, N, eps, \tilde{V}(x,0), \mathcal{S}); printed cross-references 'Section 3.2',
'Figures 1 and 2', 'Section 2', 'Figure 1' checked. Line-wrap hyphens removed (vi-olations, proba-bilistic,
Correspond-ingly, as-surances); real hyphens restored or kept ('scenario-based' is broken at a line end after
'scenario-' and the extractor had 'scenariobased'; 'Sec-tion' is a line wrap; trade-off, outlier-robust, outlier-free,
non-zero, multi-vehicle). The last sentence continues on page 7 ('... as long as the outlier rate | does not grow ...');
the first item of page 7 has join_previous 'space'. Omitted: running header and page number.
""")
