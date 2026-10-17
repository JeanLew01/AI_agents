from pagelib import *
P = 23
items = [
    figure("p0023-b001", [88.0, 94.0, 524.0, 664.0], "Figure 8", "figure-8"),
    caption("p0023-b002", B(P, "p0023-b002"), O(P, "p0023-b002", ("with offlinecalibrated CP bounds", "with offline-calibrated CP bounds"))),
    run_header(P),
    page_number(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 23 (a float page) and with appendix.tex. Figure 8 (appendix figure; label
'Figure 8', asset 'figure-8', main category): four panels printed with the bold panel letters (a), (b), (c), (d) at
their lower left, each with six time plots (p_x (m), v_x (m/s), theta (rad); p_z (m), v_z (m/s), omega (rad/s)),
x-axes 'Time (s)' and the legend 'GT Rollouts', 'Reference', 'KRS', 'CKRS'. One crop [88, 94, 524, 664] containing all
four panels, their letters and legends (union of the figure's text lines [90.5, 99.8, 484.3, 658.9]; edges checked on
the render). The panel letters carry no sub-caption text, so nothing was added to the caption. The PDF text layer
encodes the minus signs of the tick labels as a degree sign and theta/omega as 'µ' and '!' (font encoding inside the
figure); this is figure-internal text and stays in the image; the extractor's scattered picture text was deleted after
checking it lies inside the crop. Caption verbatim; the line-wrap 'offline-/calibrated' is a real compound (TeX
'offline-calibrated'), restored (extractor 'offlinecalibrated'). Placement: the figure belongs to 8.3.6 (planar
quadcopter, cited there as 'Figure 8' and 'Fig. 8a-d'); plan.json reading_order moves it with its caption to the end
of the 8.3.6 paragraph (page 21). Omitted: running header (short title) and page number 23.
""")
