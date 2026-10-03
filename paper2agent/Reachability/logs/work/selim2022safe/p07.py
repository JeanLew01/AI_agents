from pagelib import *
from refs import entries

P = 7
E = entries()
M = ["BRSL", "RTS", "SAILR", "SECAS", "Baseline"]

T1 = [
    [""] + ["Turtlebot " + m for m in M] + ["Quadrotor " + m for m in M],
    ["Goal Rate [%]", "57", "52", "48", "53", "42", "76", "66", "61", "59", "54"],
    ["Collision Rate [%]", "0.0", "0.0", "7.3", "0.0", "48", "0.0", "0.0", "9.2", "0.0", "59"],
    ["Mean/Max Speed [m/s]", ".07 / 0.18", "0.05 / 0.15", ".07 / 0.17", ".06 / 0.15", ".08 / .18",
     "3.6 / 7.9", "3.3 / 7.8", "3.7 / 7.9", "3.2 / 7.8", "3.7 / 7.9"],
    ["Mean Reward", "86", "78", "68", "66", "63", "82", "73", "61", "68", "57"],
    ["Mean ± Std. Dev. Compute Time [ms]", "50.41 ± 20.5", "100.74 ± 60.5", "30.53 ± 10.8", "22.4 ± 14.66",
     "10.21 ± 10.05", "60.33 ± 20.34", "260.85 ± 140.67", "45.31 ± 20.84", "39.7 ± 34.08", "20.63 ± 30.2"],
]
T2 = [
    [""] + ["Point Environment " + m for m in M] + ["Hexarotor " + m for m in M],
    ["Collisions [%]", "0.0", "0.0", "4.9", "0.0", "11.4", "0.0", "2", "14", "7", "63"],
    ["Mean Speed [m/s]", "0.76", "0.72", "0.78", "0.68", "0.86", "3.81", "3.4", "3.84", "3.1", "3.94"],
    ["Max Speed [m/s]", "2.00", "1.89", "2.00", "1.74", "2.00", "8.4", "8.1", "8.2", "7.95", "8.7"],
    ["Mean Reward", "118", "93", "88", "78", "73", "84", "78", "69", "62", "57"],
    ["Compute Time [ms]", "30.0 ± 10.2", "60.18 ± 20.09", "20.49 ± 10.34", "16.42 ± 8.7", "8.64 ± 1.14",
     "71.93 ± 34.52", "290.96 ± 157.24", "67.86 ± 22.34", "48.53 ± 28.69", "32.79 ± 27.6"],
]

REFBOX = {1: ("b012",), 2: ("b013",), 3: ("b014",), 4: ("b016",), 5: ("b017",), 6: ("b018",), 7: ("b019",),
          8: ("b020",), 9: ("b021",), 10: ("b022",), 11: ("b023",), 12: ("b024",), 13: ("b025",), 14: ("b026",),
          15: ("b027",), 16: ("b028",)}

items = furniture(P) + [
    text("p0007-b008", B(P, "b008"),
         r"time increases with state space dimension due to computing a halfspace representation of reachable set zonotopes, which grows exponentially in the number of generators [40]. BRSL avoids this computation by using (6). Instead, the quantity of data for BRSL determines the computation time of $\mathbf{M}_j$ from Algorithm 2, used for reachability and adjusting unsafe actions. Therefore, one can ensure the amount of data allows real time operation; choosing the data optimally is left to future work. Finally, BRSL uses zonotopes to exactly represent safety constraints, whereas SECAS uses a more conservative first-order approximation. This results in BRSL achieving higher reward with slightly slower computation time (but still fast enough for real time operation).",
         join_previous="space"),
    figure("p0007-fig4", [70.0, 54.0, 542.0, 150.0], "Figure 4", "figure-4"),
    caption("p0007-fig4-cap", [126.0, 156.0, 486.0, 164.5],
            "Fig. 4: Average reward over time of BRSL, RTS [28], SAILR [24], and a vanilla TD3 baseline for each of our experiments.\n\n"
            "Sub-captions printed under the panels: (a) Turtlebot3 Reward; (b) Quadrotor Reward; (c) Point Reward; (d) Hexarotor Reward"),
    caption("p0007-tab1-cap", [215.0, 168.5, 397.0, 176.5],
            "TABLE I: Goal-based experiment results (best values in bold)"),
    table("p0007-tab1", [52.0, 177.5, 560.0, 244.0], "Table I", "table-1", T1),
    text("p0007-tab1-note", [52.0, 244.2, 560.0, 246.5],
         "Note on Table I (added in conversion, not part of the paper): the printed header has two levels, the robot (Turtlebot, Quadrotor) above the method (BRSL, RTS, SAILR, SECAS, Baseline); the column names above combine both levels. The label of the last row is printed on two lines, “Mean ± Std. Dev.” above “Compute Time [ms]”. Cells of the row Mean/Max Speed [m/s] give mean and max separated by a slash, with leading zeros as printed. Bold face (best values) in the printed table, Turtlebot block: Goal Rate of BRSL; Collision Rate of BRSL, RTS and SECAS; the max speed of BRSL and both speed values of Baseline; Mean Reward of BRSL; the mean compute time of Baseline. Quadrotor block: Goal Rate of BRSL; Collision Rate of BRSL, RTS and SECAS; the max speed of BRSL and both speed values of SAILR and of Baseline; Mean Reward of BRSL; the mean compute time of Baseline."),
    caption("p0007-tab2-cap", [224.0, 247.0, 388.0, 255.0],
            "TABLE II: Path Following Results (best values in bold)"),
    table("p0007-tab2", [52.0, 257.0, 560.0, 319.0], "Table II", "table-2", T2),
    text("p0007-tab2-note", [52.0, 319.2, 560.0, 322.0],
         "Note on Table II (added in conversion, not part of the paper): the printed header has two levels, the environment (Point Environment, Hexarotor) above the method (BRSL, RTS, SAILR, SECAS, Baseline); the column names above combine both levels. Bold face (best values) in the printed table, Point Environment block: Collisions of BRSL, RTS and SECAS; Mean Speed of Baseline; Max Speed of BRSL, SAILR and Baseline; Mean Reward of BRSL; the mean compute time of Baseline. Hexarotor block: Collisions of BRSL; Mean Speed of Baseline; Max Speed of Baseline; Mean Reward of BRSL; the whole Compute Time entry (mean and standard deviation) of Baseline."),
    heading("p0007-b009", B(P, "b009"), "## V. Conclusion"),
    text("p0007-b010", B(P, "b010"),
         "This paper proposes the Black-box Reachability Safety Layer, or BRSL, for safe RL without having a system model *a priori*. BRSL ensures safety via data-driven reachability analysis and a novel technique to push reachable sets out of collision. To enable the RL agent to make dynamics-informed decisions, BRSL also learns an environment model online, which does not affect the safety guarantee. The framework was evaluated on four robot motion planning problems, wherein BRSL respects safety constraints while achieving a high reward over time in comparison to state-of-the-art methods. For future work, we will explore continuous-time settings, reducing the conservativeness of our reachability analysis, and minimizing the amount of data needed to guarantee safety."),
    heading("p0007-b011", B(P, "b011"), "## References"),
] + [text(f"p0007-ref{n:02d}", B(P, *REFBOX[n]), E[n]) for n in range(1, 17)]

save(P, items, r"""
Compared with the 170 dpi render of PDF page 7, a 300 dpi crop of Figure 4, a 330 dpi crop of Tables I and II, the
TeX source (Sections/7_eval.tex, 8_conc.tex) and main.bbl. Running header (odd-page form) and page number 7 omitted.
The top of the page is a block of floats (Figure 4, Table I, Table II) that interrupts the 'Results and Discussion'
paragraph begun on page 6: the first item is the continuation of that paragraph ('Furthermore RTS' planning | time
increases with ...'), join_previous 'space'; the figure and the two tables follow that paragraph, before Section V.
Figure 4: the extractor had five image fragments; replaced by one crop with the four reward plots and their printed
sub-captions (a)-(d) (edges checked: y-axis labels 'Avg. Reward', x-axis labels 'Time Steps' with the '1e6'
multiplier, legends BRSL / TD3 / RTS / SAILR / SECAS; the plot tick labels are small but legible in the crop). The
caption line is outside the crop; the sub-captions are repeated in the caption item so that they are searchable. The
legends show five curves including SECAS, while the printed caption names only BRSL, RTS, SAILR and the TD3
baseline; kept as printed. Tables I and II: the extractor had swallowed both tables and their captions into one
figure image; they are now transcribed as table items with string cells. Every cell was read on the 330 dpi crop
and compared with the PDF text layer and the TeX source: precision, the missing leading zeros ('.07', '.06',
'.08 / .18'), '±' and the slash separators are as printed. The two-level printed headers are combined into single
column names ('Turtlebot BRSL', ..., 'Hexarotor Baseline'); the two-line row label 'Mean ± Std. Dev. / Compute Time
[ms]' of Table I is written in one cell; bold face cannot be stored in the cells, so the bold (best) cells are
listed without numbers in a note item after each table, clearly marked as added in conversion (bold cells checked on
the crop and against the \textbf commands in the TeX source). Captions 'TABLE I: ...' and 'TABLE II: ...' are
printed above the tables and kept verbatim in that position. 'V. CONCLUSION' and 'REFERENCES' (small caps) are
level-2 headings in title case. Line-end hyphen 'first-|order' is a real compound (extractor had 'firstorder').
References [1]-[16]: one item per entry, generated from the authors' main.bbl and compared entry by entry with the
PDF text layer (identical alphanumeric content) and with the page image; italics follow the printed italics. Entry
[3] starts at the bottom of the left column and continues at the top of the right column below the floats
('reinforce-|ment learning'); merged. '[3] J. Garcıa' is printed with a dotless i and no accent (as in the authors'
.bbl); 'Fernández' and '[12] Jovanović' carry their accents. In [8] the page range '207–|213' and the URL
'.../science/|article/pii/S0167691104001276' are broken across lines in the PDF and were closed up; '[9]
Risk-constrained' is a real compound hyphen at a line end. URLs in [6] and [8] are plain text as printed.
""")
