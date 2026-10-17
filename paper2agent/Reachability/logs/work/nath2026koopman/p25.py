from pagelib import *
P = 25
items = [
    figure("p0025-b001", [92.0, 156.0, 520.0, 600.0], "Figure 10", "figure-10"),
    caption("p0025-b002", B(P, "p0025-b002"), O(P, "p0025-b002")),
    run_header(P),
    page_number(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 25 (a float page) and with appendix.tex. Figure 10 (appendix figure; label
'Figure 10', asset 'figure-10', main category): 3D plot titled 'CKRS for 3D quadcopter with different reference
trajectories', wire-frame CKRS boxes along two references around a red sphere, axes 'x (m)', 'y (m)', 'z (m)' with
ticks, legend 'CKRS (reference trajectory 1)', 'CKRS (reference trajectory 2)', 'reference trajectory 1', 'reference
trajectory 2', 'Obstacle'. One crop [92, 156, 520, 600] with the title, legend and all axis labels inside (union of
the figure's text lines [117.3, 161.9, 507.3, 594.5]; edges checked on the render); the extractor's scattered picture
text was deleted after checking it lies inside the crop. Caption verbatim. Placement: the figure belongs to 8.3.7
(cited there as 'Fig. 10'); plan.json reading_order moves it with its caption after Figure 9 at the end of the 8.3.7
paragraph (page 21). Omitted: running header (short title) and page number 25.
""")
