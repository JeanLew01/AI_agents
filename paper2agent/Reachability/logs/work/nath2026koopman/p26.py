from pagelib import *
P = 26
items = [
    figure("p0026-b001", [92.0, 264.0, 520.0, 494.0], "Figure 11", "figure-11"),
    caption("p0026-b002", B(P, "p0026-b002"), O(P, "p0026-b002")),
    run_header(P),
    page_number(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 26 (a float page) and with appendix.tex. Figure 11 (appendix figure; label
'Figure 11', asset 'figure-11', main category): hopper snapshots on the checkerboard (top), a large 'Height z' plot
with the legend 'Koopman Reachable Set', 'Conformalized Koopman Reachable Set', 'Reference', 'Simulation Ground Truth
Rollouts', 'Snapshots' (bottom left), and ten small plots 'Torso Angle', 'Thigh Joint', 'Leg Joint', 'Foot Joint',
'Velocity x', 'Velocity z', 'Velocity Torso', 'Velocity Thigh', 'Velocity Leg', 'Velocity Foot', x-axes 'Time (s)'.
One crop [92, 264, 520, 494] with all labels inside (union of the figure's text lines [100.0, 387.5, 491.7, 488.3];
image edges checked on the render); the extractor's scattered picture text was deleted after checking it lies inside
the crop. Caption verbatim ('11-D MuJoCo Hopper', 'multi-colored'). Placement: the figure belongs to 8.3.8 (cited
there as 'Figure 11' and in Section 6 as 'Fig. 11'); plan.json reading_order moves it with its caption to the end of
the 8.3.8 paragraph (page 21). The page is otherwise empty. Omitted: running header 'NATH YIN CHOU' and page number 26.
""")
