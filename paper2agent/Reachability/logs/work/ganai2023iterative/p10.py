from pagelib import *
P = 10
items = [
    text("p0010-b002", B(P, "p0010-b002"),
         r"behavior that sacrifices reward performance. Ultimately, this ablation study experimentally highlights the importance of learning our REF *and* using value function $V^\pi_c$ in our algorithm’s design.",
         join_previous="space"),
    figure("p0010-fig6", [106.0, 70.0, 506.0, 215.8], "Figure 6", "figure-6"),
    caption("p0010-b001", [107.0, 217.0, 505.0, 266.0],
            r"Figure 6: Ablation study on optimization framework. Top row plots show performance measured in reward (higher is better). Bottom row plots show cost (lower is better). RESPO (red curve) achieves best balance of maximizing reward and minimizing cost. RCRL framework implemented with our REF without $V^\pi_c$ incurs very high costs. PPOLag in CMDP framework with $\chi=0$ has very low reward performance. So, learning REF and learning $V^\pi_c$ are both crucial components in our design and work in tandem to contribute to RESPO’s efficacy."),
    heading("p0010-b003", B(P, "p0010-b003"), "## 7 Discussion and Conclusion"),
    text("p0010-b004", B(P, "p0010-b004"), O(P, "p0010-b004", ("safetyconstrained", "safety-constrained"))),
    heading("p0010-b005", B(P, "p0010-b005"), "## 8 Acknowledgements"),
    text("p0010-b006", B(P, "p0010-b006"), O(P, "p0010-b006")),
    pageno(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 10, a 130 dpi crop of Figure 6, and with main.tex. Layout: Figure 6 is a
float at the top of the page and the text below it starts in the middle of the sentence begun on page 9 ('... leads to
very conservative | behavior that sacrifices reward performance.'). Item order was changed so that the continuing
paragraph comes first (join_previous 'space') and Figure 6 with its caption follows the paragraph that discusses it.
Figure 6: one crop of the eight panels (top row CarGoal, PointButton, BallRun, DroneCircle Cumulative Rewards; bottom
row the corresponding Cumulative Costs) with ticks, scale factors and the legend printed in the first panel ('PPOLag,
chi = 0', 'RCRL with REF', 'RESPO (ours)'); the extractor's box overlapped the caption; edges checked on the crop.
Caption verbatim with $V^\pi_c$ and $\chi=0$ rewritten in LaTeX from the TeX source. Section 7 is a single paragraph in
the PDF (the source has a line break but no blank line before 'We leave open ...'); extractor text compared with render
and TeX; the compound 'safety-constrained', broken at a line end, had lost its hyphen and was repaired. Authors' wording
kept: 'in least-violation policy’s feasible state space', 'converge a locally optimal policy', 'high-dimension feature
spaces'. Section 8 (Acknowledgements) grant numbers read on the render: NSF Career CCF 2047034, NSF CCF DASS 2217723,
ONR YIP N00014-22-1-2292. Italic 'and' kept. Heading levels fixed (7, 8 level 2). The rest of the page is blank (the
references start on page 11 after a page break). Omitted: printed page number 10.
""")
