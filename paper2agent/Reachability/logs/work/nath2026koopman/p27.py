from pagelib import *
P = 27
items = [
    figure("p0027-b001", [90.0, 205.0, 522.0, 551.0], "Figure 12", "figure-12"),
    caption("p0027-b002", B(P, "p0027-b002"), O(P, "p0027-b002")),
    run_header(P),
    page_number(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 27 (a float page) and with appendix.tex. Figure 12 (appendix figure; label
'Figure 12', asset 'figure-12', main category): a 7 x 4 grid of 28 small time plots, one per swimmer state, labelled
body_rot, motor1_rot ... motor12_rot, vel_x, vel_y, vel_body_rot, vel_motor1 ... vel_motor12, x-axes 'Timestep',
legend 'CKRS', 'KRS', 'Reference', 'Ground Truth'. One crop [90, 205, 522, 551] with all 28 panels, labels and the
legend inside (union of the figure's text lines [92.2, 208.9, 478.3, 545.9]; frame edges checked on the render). The
tick labels are printed at about 3 pt and are only marginally legible even in the PDF; the panel names are legible.
The extractor's scattered picture text was deleted after checking it lies inside the crop. Caption verbatim ('28-D
MuJoCo Swimmer'). Placement: the figure belongs to 8.3.9 (cited there as 'Figure 12' and in Section 6 as 'Fig. 12');
plan.json reading_order moves it with its caption to the end of the 8.3.9 paragraph (page 22). The page is otherwise
empty. Omitted: running header (short title) and page number 27.
""")
