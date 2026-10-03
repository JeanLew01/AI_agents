from pagelib import *
P = 11
HDR = ["Failure Probability", "Conformal inference Run-time", "Reachability Run-time",
       "Failure Probability", "Conformal inference Run-time", "Reachability Run-time"]
rows2 = [HDR,
         ["0.10", "2.475 sec", "7.3779 sec", "0.05", "2.4762 sec", "7.5 sec"],
         ["0.09", "2.4754 sec", "6.8911 sec", "0.04", "2.4822 sec", "7.3542 sec"],
         ["0.08", "2.5894 sec", "7.2825 sec", "0.03", "2.5316 sec", "7.5548 sec"],
         ["0.07", "2.6046 sec", "7.5339 sec", "0.02", "2.364 sec", "7.2504 sec"],
         ["0.06", "2.4674 sec", "7.1876 sec", "0.01", "3.5858 sec", "7.4376 sec"]]
rows3 = [HDR,
         ["0.10", "89.9305 sec", "93.8766 sec", "0.05", "71.3700 sec", "49.7159 sec"],
         ["0.09", "72.0818 sec", "53.0224 sec", "0.04", "67.8528 sec", "50.1378 sec"],
         ["0.08", "74.2623 sec", "50.0363 sec", "0.03", "72.8819 sec", "50.1828 sec"],
         ["0.07", "71.7105 sec", "49.7770 sec", "0.02", "85.9235 sec", "49.7792 sec"],
         ["0.06", "69.4149 sec", "50.7159 sec", "0.01", "91.9276 sec", "92.9743 sec"]]
items = [
    table("p0011-b000", B(P, "p0011-b000"), "Table 2", "table-2", rows2),
    caption("p0011-b001", B(P, "p0011-b001"),
            r"Table 2: Quadcopter: Computation times of our method for different user-provided failure probabilities $\varepsilon$. The reachability run-time is the overall time for reachability analysis over the surrogate model and constructing the probabilistic flowpipe with conformal inference. The data generation time for the test dataset is $273\ \mathrm{sec}$ and the run time for training the ReLU model on training dataset is 2 hours and 25 minutes."),
    table("p0011-b002", B(P, "p0011-b002"), "Table 3", "table-3", rows3),
    caption("p0011-b003", B(P, "p0011-b003"),
            r"Table 3: Laubloomis: Computation times of our method for different user-provided failure probabilities $\varepsilon$. The reachability run-time is the overall time for reachability analysis over the surrogate model and constructing the probabilistic flowpipe with conformal inference. The data generation time for the test dataset is 19 minutes, and the run time for training the ReLU model on the training dataset is 2 hours and 30 minutes."),
    text("p0011-b004", B(P, "p0011-b004"),
         r"Again, we train a surrogate model as a neural network with ReLU activation functions and layers $[7, 20, 20, 20, 7]$. Since the horizon length of trajectories is long, we utilize the approx-star approach instead of the exact-star approach which is more efficient at the cost of conservatism. The simulation of the results for $\varepsilon = 0.01$ is also demonstrated in Fig.3. The reachability run time for our data driven probabilistic approach for a range of failure probabilities $\varepsilon \in [0.01, 0.1 ]$ is shown in Table 3. Finally, we utilize the CORA toolbox [37] to compare to our results, which is shown in Fig.3. We emphasize that the CORA toolbox is only applicable to deterministic systems and assumes access to the model, while our approach only assumes availability of data."),
    heading("p0011-b005", B(P, "p0011-b005"), "## 5 Conclusion"),
    text("p0011-b006", B(P, "p0011-b006"),
         "We proposed a data-driven approach to analyze the reachability of stochastic dynamical systems. Particularly, we studied stochastic dynamical systems when no mathematical model of the system is available, and the only information available to us is data observed from the system. We showed how to compute probabilistic reach sets, so called probabilistic flowpipes, for this system from data. Probabilistic flowpipes ensure that the probability of a new trajectory not being in the flowpipe is upper bounded by a user-defined threshold. Our approach consists of first learning a surrogate model"),
    pageno(P),
]
save(P, items, r"""
Compared with the 130 dpi render of PDF page 11 and with sections/experimental_results.tex and sections/conc.tex.
Tables 2 (Quadcopter) and 3 (Laubloomis) have the same layout as Table 1: two side-by-side blocks of three columns
(failure probabilities 0.10-0.06 left, 0.05-0.01 right) with two-line headers; they are transcribed as printed with six
columns, the three header names repeated and each written on one line (the extractor had split the Table 3 header into
two rows). All 60 cells were compared with the page image and the TeX source; printed precision kept ('2.475 sec',
'7.5 sec', '2.364 sec', '71.3700 sec', '49.7770 sec'). Captions verbatim; in the Table 2 caption '273 sec' is typed
with the operator \sec in the source (upright 'sec', seconds) and written $273\ \mathrm{sec}$. Both tables are floats printed at the top of this page, between the
Laubloomis paragraph and equation (8) of page 10 and the paragraph 'Again, we train ...'; in the reading order Table 2
follows the Quadcopter paragraph and Table 3 follows the paragraph 'Again, we train ...', which refers to it. Kept as
printed: 'Fig.3' without a space (twice), 'data driven' without hyphen, 'so called', 'on training dataset' (Table 2
caption) versus 'on the training dataset' (Table 3 caption). Spaces after the commas were added in the layer list
'$[7, 20, 20, 20, 7]$'. References checked on the page: Fig.3 (twice), Table 3, [37]. Section heading '5 Conclusion' is
level 2. Line-wrap hyphens removed in 'probabilities' (both captions). The Conclusion paragraph ends in the middle of a
sentence ('first learning a surrogate model'); it continues on page 12 below equation (7).
""")
