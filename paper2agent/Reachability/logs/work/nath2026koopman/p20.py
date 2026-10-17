from pagelib import *
P = 20
items = [
    text("p0020-b001", B(P, "p0020-b001"),
         O(P, "p0020-b001", ("velocity ( _p, q, r_ ) and angle ( _ϕ, θ, ψ_ )", r"velocity ($p, q, r$) and angle ($\phi, \theta, \psi$)")),
         join_previous="space"),
    figure("p0020-b002", [88.0, 194.0, 524.0, 345.0], "Figure 6", "figure-6"),
    caption("p0020-b003", B(P, "p0020-b003"), O(P, "p0020-b003")),
    heading("p0020-b004", B(P, "p0020-b004"), "#### 8.3.5. Additional results on unicycle system."),
    text("p0020-b005", B(P, "p0020-b005"),
         O(P, "p0020-b005", ("at least 1 _− δ_ , illustrating", r"at least $1-\delta$, illustrating"))),
    heading("p0020-b006", B(P, "p0020-b006"), "#### 8.3.6. Additional results on planar quadcopter system."),
    text("p0020-b007", B(P, "p0020-b007"), O(P, "p0020-b007")),
    run_header(P),
    page_number(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 20 and with appendix.tex. First paragraph: continuation of the 8.3.4
paragraph from page 19 (join_previous 'space'); the extractor's '( _p, q, r_ )' and '( _ϕ, θ, ψ_ )' rewritten as
'($p, q, r$)' and '($\phi, \theta, \psi$)' as in the TeX; curly quotes around 'wrapping effect' and the compound
'over-approximation' as printed. Figure 6 (appendix figure, label 'Figure 6', asset 'figure-6', main category): 4 x 3
grid of time plots, columns 'Position (m)', 'Angles (rad)', 'Velocity (m/s)', 'Angular Velocity (rad/s)', rows p_x/p_y/
p_z, psi/theta/phi, v_x/v_y/v_z, p/q/r, x-axes 'Time Step (t)', legend 'NNV Conformal', 'Koopman Conformal', 'GT
Rollouts', 'Reference'; one crop [88, 194, 524, 345] with all labels inside (edges checked on the render: union of
the figure's text lines is [90.6, 199.3, 512.0, 339.1]); the extractor's scattered picture text was deleted after
checking it lies inside the crop. Caption verbatim, printed without a final period. Headings '8.3.5. Additional
results on unicycle system.' and '8.3.6. Additional results on planar quadcopter system.' (small caps, final period)
written as level 4 in the TeX's sentence case. 8.3.5 paragraph: extractor prose checked on the render with
'$1-\delta$' from the TeX; source slip kept as printed: 'guaranteed to remain with with probability'. 8.3.6 paragraph:
extractor prose checked on the render ('No-tably', 'rel-atively', 'show-cases' closed up); as printed 'Fig. 11',
'Sec. 5.4', '(Fig. 8a-d)'; it continues on page 21 ('the resulting closed-loop trajectories remain ...'), joined there
with join_previous 'space'. Omitted: running header 'NATH YIN CHOU' and page number 20.
""")
