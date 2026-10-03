from pagelib import *
P = 9
items = [
    text("p0009-b006", B(P, "p0009-b006"), O(P, "p0009-b006"), join_previous="space"),
    figure("p0009-fig3", [105.0, 68.0, 507.0, 125.0], "Figure 3", "figure-3"),
    caption("p0009-b001", [107.0, 126.0, 506.0, 185.0], O(P, "p0009-b001", ("0 _._ 5 meters", "$0.5$ meters"), ("0 _._ 8 meters", "$0.8$ meters"))),
    heading("p0009-b007", B(P, "p0009-b007"), "### 6.3 Ablation Studies"),
    text("p0009-b008", B(P, "p0009-b008"), O(P, "p0009-b008")),
    figure("p0009-fig4", [103.0, 185.5, 309.0, 343.5], "Figure 4", "figure-4"),
    caption("p0009-b003", [107.0, 345.0, 308.0, 394.0], O(P, "p0009-b003", ("with 0 violations", "with $0$ violations"))),
    figure("p0009-fig5", [311.0, 185.5, 507.0, 343.0], "Figure 5", "figure-5"),
    caption("p0009-b005", [313.0, 344.0, 506.0, 393.0], O(P, "p0009-b005")),
    text("p0009-b009", B(P, "p0009-b009"), O(P, "p0009-b009", ("in accordance with Assumption 1.", "in accordance with Assumption $1$."))),
    text("p0009-b010", B(P, "p0009-b010"),
         r"In Figure 6, we compare **RESPO** with RCRL implemented with our REF and **PPOLag** in the CMDP framework with cost threshold $\chi=0$ to ensure hard constraint satisfaction. The difference between **RESPO** and the RCRL-based ablation approach is that the ablation still uses $V^\pi_h$ instead of $V^\pi_c$. The ablation aproach’s high cumulative cost can be attributed to the limitations of using $V^\pi_h$ – particularly, the lower sensitivity of $V^\pi_h$ to safety improvement and its lack of guarantees on feasible set (re)entrance. **PPOLag** with $\chi=0$ produces low violations but also very low reward performance that’s close to zero. Naively using $V^\pi_c$ in a hard constraints framework leads to very conservative"),
    pageno(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 9, a 200 dpi crop of Figure 3, a 130 dpi crop of Figures 4-5, and with
main.tex. Layout: Figures 3, 4 and 5 are floats at the top of the page and the text below them starts in the middle of
the sentence begun on page 8 ('... where the higher | Drone makes way ...'). Item order on this page was therefore
changed to the logical reading order: first the continuing paragraph of Section 6.2 (join_previous 'space'), then
Figure 3 with its caption (the figure that paragraph discusses), then the heading 6.3 and its first paragraph, then
Figures 4 and 5 with their captions (in the TeX source the float containing both is declared at this point), then the
two remaining paragraphs. Figure 3: one crop of the four trajectory panels titled 'RESPO (ours)', 'PPOLag', 'RCRL',
'FAC' with their axes and the colour bars labelled 'Trajectory Step Number' (tick labels of the colour bars are very
small in the PDF); the extractor's box overlapped the caption. Figure 4 (left half of the page): Reacher and HalfCheetah
Cumulative Rewards (top) and Cumulative Costs (bottom), legend in the first panel (PPOLag, RCRL, FAC, RESPO (ours),
CBF, Vanilla PPO, CRPO, P3O, PCPO). Figure 5 (right half): CarGoal and PointButton Cumulative Rewards (top) and Costs
(bottom), legend in the first panel ('RESPO w/ lr*0.01', 'RESPO w/ lr*0.1', 'RESPO', 'RESPO w/ lr*10', 'RESPO w/
lr*100'). Bboxes of the three figures were set from the render and the evidence line positions and checked on the
crops (all tick labels, '1e6' exponents and panel titles inside; captions outside). Captions verbatim; printed
side by side in two narrow columns, so the line-wrap hyphens of 'MuJoCo' and 'violations' in the Figure 4 caption were
removed; math-mode numbers restored ($0.5$, $0.8$, $0$) and 'Assumption $1$' in the prose (the source says 'Assumption
1' in math mode; the step-size assumption is called A1 in Section 5.4). Last paragraph: inline mathematics ($\chi=0$,
$V^\pi_h$, $V^\pi_c$) rewritten in LaTeX from the TeX source (the extractor had <sup> glyph soup); the references to the
RCRL equation print as the name 'RCRL'; en dashes as printed; authors' typo 'aproach’s' kept. The paragraph is cut by
the page break in the middle of a sentence ('... leads to very conservative | behavior that sacrifices ...') and
continues on page 10 (join_previous there). References 'Figure 5', 'Figure 6' as printed. Heading 6.3 set to level 3.
Omitted: printed page number 9.
""")
