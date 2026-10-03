#!/usr/bin/env python3
from pagelib import write_page

NOTES = r"""
Compared with the 170 dpi render, 260 dpi crops of the two prose regions of the left column and
300 dpi crops of both tables, Figure 2 and Figure 3, and with the TeX source and main.bbl. Printed
layout: left column = Section VI-A text, TABLE I, one paragraph, TABLE II, Figure 2, Section VI-B text;
right column = Figure 3 (top), Section VII, start of the references. The extractor had interleaved the
two columns; the items are now in reading order: left column as printed, then Figure 3 with its caption
(directly after the Ablation Study paragraph that discusses it), Section VII, References [1]-[7].
Tables: both are transcribed as cells (3 rows x 5 columns each, all strings, values copied digit for
digit from the 300 dpi crop: 1.111, 0.370, 0.123, 0.041; 0.510, 0.900, 0.953, 1; 0.02 s, 0.19 s, 2.33 s,
83.73 s; 0.13 s, 0.61 s, 3.19 s, 19.75 s). Cells hold plain characters only: the header cell is
printed 'Methods \ r_min' (TABLE I) and 'Method \ r_min' (TABLE II), i.e. a backslash followed by r
with subscript min (LaTeX $r_{\min}$); the pifont marks are written as the Unicode characters of the
PDF text layer, ballot x (U+2717) and check mark (U+2713); in TABLE II the four numbers of the
'Recurrent Set' row are printed in bold, which the cells cannot show (stated in the conversion notes).
The extractor had split the fourth column of TABLE II wrongly ('0.1' | '23 0.041'); corrected. Labels
'Table I' / 'Table II' follow the printed Roman numbering; asset names table-1 / table-2. The table
captions are printed above the tables (prefix 'TABLE I:' / 'TABLE II:') and are caption items placed
before the tables. Figures: Figure 2 (two contour panels with their axis labels, tick labels, legend
and the sub-captions '(a) HJ Reachability', '(b) Recurrent Set Approximation') and Figure 3 (two line
plots with axis labels, legends alpha = 0.1 / 0.5 / 1.0 and the sub-captions '(a) Volume Difference',
'(b) Computation Time') are one crop each; all four edges were checked on the 300 dpi crops (y-axis
labels, right-most tick labels and sub-captions inside, main caption outside). The sub-captions are
inside the crops and are also repeated as the first line of the caption item so that they are
searchable; the tick and legend texts that the extractor had put into the figure items' markdown were
dropped (they are visible in the crops). Captions verbatim with LaTeX math; the Figure 3 caption is
printed 'n_s=3000, r_min=0.370.' with an upright subscript s. Inline math from main.tex, checked on the
crops: V_{BRT} with italic subscript in Section VI-A but upright V_BRT in Section VI-B (kept as
printed), the subscript 'BRT cap h' <= 0' of the intersection ratio, 'beta = alpha = 0.05'. Kept as
printed: the TABLE II caption says 'alpha = 1' while the text says beta = alpha = 0.05; 'tau = 1 s'.
'I', 'II' in 'Table I'/'Table II' and 'Figure 2', 'Figure 3', 'Definition 6' are the printed
cross-references. References [1]-[7]: every entry read against the page image and the .bbl; one item
per entry; titles are printed in sentence case with lower-case proper names ('hamilton-jacobi',
'control-lyapunov', 'koopman', 'Deepreach'), kept. Line-wrap hyphens removed (Table, Precision,
Different, normalized, approximates, provably, automatic, verification, International); real hyphens
kept (low-precision, finite-time, sampling-based, over-approximated, trade-off, time-dependent,
Hamilton-jacobi, control-lyapunov, high-dimensional, Data-driven, safety-critical).
"""

T1 = [
    ["Methods \\ r_min", "1.111", "0.370", "0.123", "0.041"],
    ["HJ BRT [19]", "0.510 (✗)", "0.900 (✗)", "0.953 (✗)", "1 (✓)"],
    ["Recurrent Set", "1 (✓)", "1 (✓)", "1 (✓)", "1 (✓)"],
]
T2 = [
    ["Method \\ r_min", "1.111", "0.370", "0.123", "0.041"],
    ["HJ BRT [19]", "0.02 s (✗)", "0.19 s (✗)", "2.33 s (✗)", "83.73 s (✓)"],
    ["Recurrent Set", "0.13 s (✓)", "0.61 s (✓)", "3.19 s (✓)", "19.75 s (✓)"],
]

write_page(7, NOTES, [
    ("p0007-b001", "heading", ("p0007-b001",), "### A. Results Comparison", {}),
    ("p0007-b002", "text", ("p0007-b002",),
     r"We use $\tau = 1$ s and a total number of control samples per cell $n_s = 3000$. $V_{BRT}$ denotes the unsafe region volume computed via HJ reachability at $r_{\min} = 0.041$ (the grid resolution). We calculate the intersection ratio $(V_{BRT\cap h'\leq0} /V_{BRT})$ between our method ($\beta = \alpha = 0.05$) and HJ solutions at different precisions. As shown in Table I and Figure 2, low-precision HJ analysis underestimates unsafe regions, risking safety misjudgment. Our method guarantees complete containment of true unsafe regions at all precisions.", {}),
    ("p0007-b004", "caption", ("p0007-b004",),
     "TABLE I: Comparison of the Fraction of the Unsafe Zone Volume Captured by Different Methods at Different Precision", {}),
    ("p0007-b006", "table", [60.0, 241.0, 290.0, 275.0], "", {"label": "Table I", "asset_name": "table-1", "rows": T1}),
    ("p0007-b008", "text", ("p0007-b008",),
     "Beyond safety guarantees, Table II demonstrates our method’s faster computation time at high precision through parallelization.", {}),
    ("p0007-b009", "caption", ("p0007-b009",),
     r"TABLE II: Comparison of Computation Time between HJ reachability and Recurrent Set Approximation under Different Precision, $\tau = 1$ s, $\alpha = 1$, $n_{\mathrm{s}} = 3000$", {}),
    ("p0007-b011", "table", [52.0, 373.0, 304.0, 407.0], "", {"label": "Table II", "asset_name": "table-2", "rows": T2}),
    ("p0007-b012", "figure", [50.0, 430.0, 305.0, 575.0], "", {"label": "Figure 2", "asset_name": "figure-2"}),
    ("p0007-b018", "caption", ("p0007-b018",),
     "(a) HJ Reachability (b) Recurrent Set Approximation\n\n"
     r"Fig. 2: Contour Plot of the Boundary of the Unsafe Region with Different Precision and Different Methods when $x_3 = \pi$", {}),
    ("p0007-b021", "heading", ("p0007-b021",), "### B. Ablation Study", {}),
    ("p0007-b022", "text", ("p0007-b022",),
     r"Definition 6 shows the recurrent set converges to the invariant set as $\tau \to 0$. To gauge parameter effects on RCBF performance, we ran a sweep over two metrics: the normalized volume gap $(V_{\tau}-V_{\mathrm{BRT}})/V_{\mathrm{BRT}}$ and computation time $t$. Figure 3 indicates an inverse $\tau$–accuracy trade-off: smaller $\tau$ reduces the volume gap but drives computation time up (roughly exponentially). Nonetheless, runtimes remain practical and safety is preserved for all tested parameters.", {}),
    ("p0007-b000", "figure", [306.0, 48.0, 563.0, 183.0], "", {"label": "Figure 3", "asset_name": "figure-3"}),
    ("p0007-b003", "caption", ("p0007-b003",),
     "(a) Volume Difference (b) Computation Time\n\n"
     r"Fig. 3: Volume gap and computation time versus $\tau$ (and $\alpha$); $n_{\mathrm{s}}=3000$, $r_{\min}=0.370$.", {}),
    ("p0007-b005", "heading", ("p0007-b005",), "## VII. Conclusion and Discussion", {}),
    ("p0007-b007", "text", ("p0007-b007",),
     r"We introduced Recurrent Control Barrier Functions (RCBFs), generalizing CBFs by enforcing finite-time ($\tau$) return rather than strict invariance. We proved that the signed distance to a $\tau$-recurrent set is a valid RCBF, yielding rigorous safety guarantees. A sampling-based algorithm approximates the safe region. Simulations demonstrate provably safe, though over-approximated, sets with competitive computational performance.", {}),
    ("p0007-b010", "text", ("p0007-b010",),
     "An approximation gap persists between computed and true safe sets. While denser sampling improves accuracy, the precise link between sampling parameters and error remains open. Future work will quantify this relationship and develop corresponding models to guide adaptive sampling for tighter guarantees.", {}),
    ("p0007-b013", "heading", ("p0007-b013",), "## References", {}),
    ("p0007-b014", "text", ("p0007-b014",),
     "[1] I. M. Mitchell, A. M. Bayen, and C. J. Tomlin, “A time-dependent hamilton-jacobi formulation of reachable sets for continuous dynamic games,” *IEEE Transactions on automatic control*, vol. 50, no. 7, pp. 947–957, 2005.", {}),
    ("p0007-b015", "text", ("p0007-b015",),
     "[2] A. D. Ames, S. Coogan, M. Egerstedt, G. Notomista, K. Sreenath, and P. Tabuada, “Control barrier functions: Theory and applications,” in *2019 18th European control conference (ECC)*, IEEE, 2019, pp. 3420–3431.", {}),
    ("p0007-b016", "text", ("p0007-b016",),
     "[3] S. Bansal, M. Chen, S. Herbert, and C. J. Tomlin, “Hamilton-jacobi reachability: A brief overview and recent advances,” in *2017 IEEE 56th Annual Conference on Decision and Control (CDC)*, IEEE, 2017, pp. 2242–2253.", {}),
    ("p0007-b017", "text", ("p0007-b017",),
     "[4] H. Dai and F. Permenter, “Convex synthesis and verification of control-lyapunov and barrier functions with input constraints,” in *2023 American Control Conference (ACC)*, IEEE, 2023, pp. 4116–4123.", {}),
    ("p0007-b019", "text", ("p0007-b019",),
     "[5] A. Clark, “Verification and synthesis of control barrier functions,” in *2021 60th IEEE Conference on Decision and Control (CDC)*, IEEE, 2021, pp. 6105–6112.", {}),
    ("p0007-b020", "text", ("p0007-b020",),
     "[6] S. Bansal and C. J. Tomlin, “Deepreach: A deep learning approach to high-dimensional reachability,” in *2021 IEEE International Conference on Robotics and Automation (ICRA)*, IEEE, 2021, pp. 1817–1824.", {}),
    ("p0007-b023", "text", ("p0007-b023",),
     "[7] C. Folkestad, Y. Chen, A. D. Ames, and J. W. Burdick, “Data-driven safety-critical control: Synthesizing control barrier functions with koopman operators,” *IEEE Control Systems Letters*, vol. 5, no. 6, pp. 2012–2017, 2020.", {}),
])
