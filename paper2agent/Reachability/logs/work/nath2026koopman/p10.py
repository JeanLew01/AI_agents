from pagelib import *
P = 10
M = "−"
HDR = ["Experiment", "System dimension", "Time steps", "Confidence Level (1 − δ)", "CP time", "KRS time",
       "Total time (online)", "Avg. Log volume (online)", "Avg. Log volume (offline)", "Calibration dataset size", "Empirical coverage"]
ROWS = [
    ["Unicycle", "3", "100", "99.0%", "0.038s", "0.277s", "0.315s", M + "11.543", M + "8.690", "100", "100%"],
    ["2D Quad", "6", "100", "99.0%", "0.055s", "0.349s", "0.404s", M + "21.491", M + "5.333", "100", "100%"],
    ["3D Quad", "12", "200", "99.0%", "0.175s", "0.500s", "0.675s", M + "42.954", M + "35.275", "100", "100%"],
    ["Hopper", "11", "225", "99.0%", "10.597s", "0.387s", "10.983s", M + "4.969", M + "1.806", "100", "100%"],
    ["Swimmer", "28", "400", "95.0%", "20.818s", "0.593s", "21.411s", "32.595", "42.617", "100", "99.5%"],
]
items = [
    text("p0010-b003", B(P, "p0010-b003"),
         r"system safety. In contrast, our method attains 100% empirical coverage across all tested calibration set sizes, avoiding this variance-data trade-off and achieving target coverage with far fewer samples.",
         join_previous="space"),
    figure("p0010-b004", [86.0, 222.0, 526.0, 338.0], "Figure 3", "figure-3"),
    caption("p0010-b005", B(P, "p0010-b005"),
            r"Figure 3: To visualize empirical reachable set coverage, we compute Beta posteriors for the SNSA baseline and ScaRe-Kro on the 3D quadcopter (left) and Hopper (right). The dotted lines indicate the mode of the Beta posterior. For SNSA, coverage rate slowly converges to the target $1-\delta$ as calibration dataset size increases, whereas ScaRe-Kro maintains 100% coverage even for small $K^\textrm{cal}$."),
    text("p0010-hybrid", [89.0, 410.0, 523.0, 516.0],
         r"*Hybrid Reachability methods (CP+NNV).* For a 3D quadcopter (14), we compare with a hybrid data-driven/NNV reachability method (Hashemi et al., 2024) (denoted CP-NNV), that computes an RSOA by applying NNV on a learned NN trajectory predictor and using CP to bound RSOA underapproximation error induced by learning error. As shown in Fig. 6, CP-NNV yields much larger reachable sets (avg. log volume: -23.35), especially in attitude and velocity. This reflects difficulties in scaling NNV and CP to high-dimensional state spaces and long horizons, which we address with Koopman operators. Our method produces tighter RSOAs (avg. log volume: -40.66) while maintaining coverage, improving scalability with horizon and reducing conservativeness."),
    text("p0010-purennv", [89.0, 518.0, 523.0, 578.0],
         r"*Pure NNV Reachability.* On a unicycle model, we compare with our prior work (Nath et al., 2025), which used NNV tools for one-shot RSOA computation, requiring $51.95$s and achieving an average log-volume of $-3.98$. In contrast, our method computes the RSOA in $0.32$s with a log-volume of $-11.54$ (Table 1). This highlights that our method is much faster and also reduces conservativeness."),
    caption("p0010-b001", B(P, "p0010-b001"),
            r"Table 1: Numerical RSOA results for SCaRe-Kro on unicycle, quadcopters and MuJoCo models."),
    table("p0010-b002", [98.0, 104.0, 514.0, 176.0], "Table 1", "table-1", [HDR] + ROWS),
    text("p0010-b007", B(P, "p0010-b007"),
         r"**Unicycle** We evaluate on CKRS computations on a unicycle model (12), where $\phi$ and $\psi$ have 3 hidden layers with 128 neurons each, and $z \in \mathbb{R}^{10}$. As shown in Fig. 7, the certified reachable sets verify both safety and goal attainment. Full metrics are in Table 1. We view this benchmark as a sanity check on a simple system, paving the way for more substantive scalability results."),
    text("p0010-b008", B(P, "p0010-b008"),
         r"**Planar Quadcopter** We evaluate a 6-state planar quadcopter (13) navigating around a circular obstacle for $T=100$. Here, $\phi$ and $\psi$ have 3 hidden layers with 128 neurons each, and $z \in \mathbb{R}^{24}$. We visualize offline-calibrated CKRSs for multiple reference trajectories in Fig. 8; metrics are in Table 1. An NNV-only baseline (Nath et al., 2025) required $59.85\,\mathrm{s}$ and achieved an average log-volume of $-18.709$. Overall, these results support our claim of reduced RSOA conservativeness."),
    run_header(P),
    page_number(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 10, a 280 dpi crop of Table 1, a 200 dpi crop of Figure 3, and with
experiments.tex. Printed order: Table 1 (caption above the table) and Figure 3 at the top, then the end of the 'Pure
CP based verification.' paragraph. Items reordered within the page so that the prose reads continuously: first the
continuation 'system safety. In contrast, ...' (join_previous 'space' to page 9), then Figure 3 and its caption (the
figure discussed in that paragraph), then the 'Hybrid ...' and 'Pure NNV ...' paragraphs, then Table 1 (caption first,
as printed above the table; placed after the paragraph that ends '(Table 1)', where the TeX declares it), then
'Unicycle' and 'Planar Quadcopter'. Table 1: 11 columns x 5 rows plus header; the extractor's cells had glyph-soup
markers ('99_._0%', '_−_11_._543', stray 'i', 'l'); all cells rewritten and compared one by one with the 280 dpi crop
and the TeX tabular. Each header is printed on two or three lines (\shortstack); the lines are joined with spaces into
one header cell ('System dimension', 'Time steps', 'Confidence Level (1 − δ)', 'CP time', 'KRS time', 'Total time
(online)', 'Avg. Log volume (online)', 'Avg. Log volume (offline)', 'Calibration dataset size', 'Empirical coverage');
no merged cells. Cells as printed, with the units 's' and '%'; minus signs written as the Unicode minus (U+2212) as in
the PDF. Caption as printed with 'SCaRe-Kro' (capital C; the method is 'ScaRe-Kro' elsewhere) - source slip kept.
Figure 3: two violin-style coverage plots ('3D Quadrotor (12D)', 'MuJoCo Hopper (11D)'), y-axis 'Empirical Coverage'
0.90-1.00, x-axes 'Number of Calibration Samples (K^cal)', colour bar 'Std. Devs. from Mean' 1-3+, legend '95% Target',
'CKRS (ours) (Beta distribution mode)', 'SNSA (Beta distribution mode)'; one crop 'figure-3' with all labels inside
(edges checked at 200 dpi); the extractor's scattered picture text was deleted after checking it lies inside the
crop. The caption was extracted as a text item; now a caption item, verbatim, with $1-\delta$ and $K^\textrm{cal}$;
'100%' kept plain (typed in math in the TeX). Run-in titles 'Hybrid Reachability methods (CP+NNV).' and 'Pure NNV
Reachability.' are underlined italic (contour text, repeated by the extractor); written in italics inside their text
items, split into two items as printed. '(avg. log volume: -23.35)' and '-40.66' are printed with a text hyphen
(typed in text mode) and kept so; '51.95s', '-3.98', '0.32s', '-11.54' are typed in math (Unicode minus in the PDF).
Run-in bold titles 'Unicycle', 'Planar Quadcopter'; 'log-/volume' is a real compound. Mathematics from the TeX: $\phi$,
$\psi$, $z \in \mathbb{R}^{10}$, $\mathbb{R}^{24}$, $T=100$, $59.85\,\mathrm{s}$, $-18.709$. Citations (Hashemi et al.,
2024), (Nath et al., 2025). Equation references (12), (13), (14) and figure references Fig. 5-8 as printed. Omitted:
running header 'NATH YIN CHOU' and page number 10.
""")
