from pagelib import *
P = 24
items = [
    figure("p0024-b001", [87.0, 89.0, 524.0, 684.0], "Figure 9", "figure-9"),
    caption("p0024-b002", B(P, "p0024-b002"), O(P, "p0024-b002")),
    run_header(P),
    page_number(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 24 (a float page) and with appendix.tex. Figure 9 (appendix figure; label
'Figure 9', asset 'figure-9', main category): four panels with the printed bold panel letters (a), (b), (c), (d), each a
4 x 3 grid of time plots (columns 'Position (m)', 'Angles (rad)', 'Velocity (m/s)', 'Angular Velocity (rad/s)'; rows
p_x/p_y/p_z, psi/theta/phi, v_x/v_y/v_z, p/q/r; x-axes 'Time Step (t)') and the legend 'CKRS', 'KRS', 'GT Rollouts',
'Reference'. One crop [87, 89, 524, 684] with all four panels, letters and legends (union of the figure's text lines
[89.0, 93.1, 514.8, 679.2]; edges checked on the render). The PDF text layer encodes the minus signs of many tick
labels as a degree sign (38 lines on this page); this is figure-internal text and stays in the image; the extractor's
scattered picture text was deleted after checking it lies inside the crop. The panel letters carry no sub-caption
text, so nothing was added to the caption. Caption verbatim ('Alternative CKRSs computed for 3D quadcopter model for a
different reference trajectory.' - singular 'trajectory' as printed, although four panels are shown). Placement: the
figure belongs to 8.3.7 (cited as 'Fig. 9' there and in Section 6); plan.json reading_order moves it with its caption
to the end of the 8.3.7 paragraph (page 21). Omitted: running header 'NATH YIN CHOU' and page number 24.
""")
