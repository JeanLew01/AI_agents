from pagelib import *
P = 19
items = [
    heading("p0019-b001", B(P, "p0019-b001"), "#### 8.3.3. Baseline comparison with Bansal and Tomlin (2021)."),
    text("p0019-b002", B(P, "p0019-b002"), O(P, "p0019-b002")),
    figure("p0019-b003", [90.0, 245.0, 522.0, 532.0], "Figure 5", "figure-5"),
    caption("p0019-b004", B(P, "p0019-b004"), O(P, "p0019-b004")),
    heading("p0019-b005", B(P, "p0019-b005"), "#### 8.3.4. Baseline comparison with Hashemi et al. (2024)."),
    text("p0019-b006", B(P, "p0019-b006"), O(P, "p0019-b006")),
    run_header(P),
    page_number(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 19, a 120 dpi crop of Figure 5, and with appendix.tex. Headings '8.3.3.
Baseline comparison with Bansal and Tomlin (2021).' and '8.3.4. Baseline comparison with Hashemi et al. (2024).' are
printed in small caps with a final period, the citation (\cite) inside the heading; level 4, written in the TeX's
sentence case with the printed citation text. The extractor had classified the 8.3.4 heading as a caption; fixed.
8.3.3 paragraph: extractor prose checked on the render (curly quotes around 'reach-avoid' as printed; 'tra-jectories'
closed up). Figure 5 (appendix figure; numbered continuously with the main-text figures, so label 'Figure 5' and
asset 'figure-5' in the main category): unicycle x-y plot with the red obstacle, orange DeepReach rollouts, green GT
rollouts, blue CKRS tube, yellow goal with the label 'Goal tol', axes 'x' and 'y' with ticks -0.75 ... 0.75 and -0.6
... 0.2, legend 'GT rollouts', 'Reference', 'DeepReach rollouts', 'CKRS (99.0%)'; one crop [90, 245, 522, 532] with all
labels inside (edges checked); the extractor's scattered picture text was deleted after checking it lies inside the
crop. Caption verbatim ('prob-ability' closed up; 'probability 0.99'). 8.3.4 paragraph: extractor prose checked on the
render; 'Figure 6 illustrate' kept as printed; the paragraph continues on page 20 ('approach and Hashemi et al. (2024)
is ...'), joined there with join_previous 'space'. References 'Figure 5', 'Figure 6', 'Section 6' as printed. Omitted:
running header (short title) and page number 19.
""")
