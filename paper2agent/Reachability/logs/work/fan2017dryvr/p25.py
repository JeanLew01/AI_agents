from pagelib import *

items = [
    figure("p0025-alg2", [131.0, 313.5, 480.5, 484.0], "Algorithm 2", "algorithm-2", asset_category="supp_figs"),
    text("p0025-alg2-text", [139.0, 318.0, 470.0, 480.0], r"""
**Algorithm 2:** $\mathit{VerifySafety}(\mathcal{H},\mathcal{U})$ verifies safety of hybrid system $\mathcal{H}$ with respect to unsafe set $\mathcal{U}$.
**initially:** $\mathcal{I}.push(Partition(\Theta))$
1 **while** $\mathcal{I} \neq \emptyset$ **do**
    2 $S \gets \mathcal{I}.pop()$;
    3 $RS \gets \mathit{GraphReach}(\mathcal{H})$ ;
    4 **if** $RS \cap \mathcal{U} = \emptyset$ **then**
        5 continue;
    6 **else if** $\exists (x,l,t) \in RT$ s.t. $\langle RT,v \rangle \in RS$ and $(x,l,t) \subseteq \mathcal{U}$ **then**
        7 **return** UNSAFE, $\langle RT,v \rangle$
    8 **else**
        9 $I.push (Partition(S))$ ;
        10 Or, $G \gets RefineGraph(G)$ ;
11 **return** SAFE
"""),
    pageno(25, [300.0, 695.0, 311.0, 703.0]),
]

save(25, items, r"""
Compared with a 260-dpi render of the upper half of the page, a 330-dpi crop of the algorithm box, and appendix.tex. The page contains only Algorithm 2 (VerifySafety), printed as a float in the middle of the page; it belongs to Appendix A.3, which starts on page 24. Kept as an image crop (label 'Algorithm 2', asset 'algorithm-2', routed to the supplementary figure category because it is printed in the appendix; edges measured on the 330-dpi crop: top rule, two-line caption, rule, the unnumbered 'initially:' line, 11 numbered lines with nesting bars, bottom rule) followed by a transcription from the TeX source checked line by line on the crop. The extractor had read the box as a two-column table with a split caption ('A' / 'lgorithm 2:'); replaced. The transcription keeps the printed line numbers 1-11 (bold in the PDF, written as plain numbers at the start of each line; the 'initially:' line has no number), one paragraph per printed line, and '&emsp;&emsp;' per nesting level (lines 2-4, 6, 8 at level 1; lines 5, 7, 9, 10 at level 2). Pseudocode kept as printed, including its slips: the queue is calligraphic $\mathcal{I}$ in the 'initially' line and lines 1-2 but plain italic $I$ in line 9; line 3 calls $\mathit{GraphReach}(\mathcal{H})$ without the popped subset $S$ as argument; the mode in the triple is written $l$ (not $\ell$) in line 6; 'Or,' in line 10 offers graph refinement as an alternative to partitioning; lines 7 and 11 have no semicolon; in line 6 's.t.' and 'and' are printed in italics as part of the condition (written as plain words between the math spans). In the caption the unsafe set is calligraphic $\mathcal{U}$ (Theorem 3.2 prints '$\mathit{VerifySafety}(\mathcal{H},U)$'). This is the last page of the PDF. Omitted: page number 25.
""")
