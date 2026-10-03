# Pages 11-15 of sartipizadeh2019voronoi (executed by make_pages.py; page() and dd() come from there).

# ---------------------------------------------------------------- page 11
page(11, r"""
Compared with the 150 dpi render and a 230 dpi crop of PDF page 11 and with the TeX source. The
first item continues the last paragraph of page 10 ('... and then | compute the buffers from Lemma
4.'; join_previous 'space'). Heading '## 5 Illustrative Example: Spacecraft Rendezvous'
(capitalisation as printed). All mathematics rewritten in LaTeX from the TeX source and checked on
the crop; TeX and PDF agree. The extractor 'formula' images were replaced by $$ blocks with the
printed numbers (23) (two equations on one line separated by \qquad), (24), (25), (26) (two $$
blocks in one item so that each keeps its number). Every number of the example was read on the crop: $m_d=300$
kg, altitude 850 km, sampling time 20 s, noise covariance
$10^{-4}\times\text{diag}(1,1,5\times10^{-4},5\times10^{-4})$, target set bounds 0.1, -0.1, 0, 0.01,
0.01, safe set bounds -1, 0.05, 0.05, $N=5$, initial position $x=y=-0.75$ km, initial velocity 0
km/s, $\mathcal{U}=[-0.1,0.1]\times[-0.1,0.1]$, reference probability 0.86, $K=2000$, 100
experiments, 2.8 GHz, i5, 16 GB, up to 100 cells, $\hat{K}=20$, 2.68 s, '100 $k$-means with 1 to 100
cells', '20 to 40 cells'. Numbers that the source sets in math mode inside prose (40, 850, 20, 100,
2.8, 16, 2.68, ...) are written as plain digits. Citations checked: [4], [25], [4], [4, 10], [26],
[18, Rem. 1]. References to 'Figure 4a/4b/4c', 'Algorithm 1', 'Theorem 1', 'Problem 3' resolved to
the printed numbers. Kept as printed (source slips, not conversion errors): in (23) the term
'$3\omega x$' (not $3\omega^2x$) and $\omega$ without a factor in '$2\omega\dot{y}$'; '$m_d$' is
called the mass of the chief; row vectors $\zeta=[x,y,\dot{x},\dot{y}]$ and $u=[F_x,F_y]$ without
transpose; in (26) '$|\zeta_1|\leq\zeta_2$' together with '$-1\leq\zeta_2$'; '$\mathcal{W}_N$' (index
$N$, not $K$) in 'in each experiment $\mathcal{W}_N$ is generated randomly'; '$WSS$' in math italics
once; 'coincides the “knee”'; 'exponentially increases exponentially'; '$\hat{K}$s'. The last
paragraph breaks at the page end after 'The computed terminal time probability and the' and
continues on page 12 below the Figure 4 float (page-12 item joined with a space). In the reading
order Figure 4 and its caption (printed at the top of page 12, inside that sentence) follow the
paragraph 'We set $K=2000$ ...' of this page, which introduces Figure 4a-4c.
""", [
    ("p0011-b000", "text", ("p0011-b000",),
     r"compute the buffers from Lemma 4. All these steps are executed offline (independent of $x_0$), while solving Problem 3 and probability reconstruction using (22) is done online (dependent on $x_0$).", {"join_previous": "space"}),
    ("p0011-b001", "heading", ("p0011-b001",), "## 5 Illustrative Example: Spacecraft Rendezvous", {}),
    ("p0011-b002", "text", ("p0011-b002",),
     "We consider the spacecraft rendezvous example discussed in [4]. In this example, two spacecraft are in the same elliptical orbit. One spacecraft, referred to as the deputy, must approach and dock with another spacecraft, referred to as the chief, while remaining in a line-of-sight cone, in which accurate sensing of the other vehicle is possible. The relative dynamics are described by the Clohessy-Wiltshire-Hill (CWH) equations as given in [25],", {}),
    ("p0011-b003", "text", ("p0011-b003",),
     dd(r"\ddot{x} - 3 \omega x - 2 \omega \dot{y} = m_{d}^{-1}F_{x},\qquad\ddot{y} + 2 \omega \dot{x} = m_{d}^{-1}F_{y}.", "23"), {}),
    ("p0011-b004", "text", ("p0011-b004",),
     r"The position of the deputy is denoted by $x,y \in \mathbb{R}$ when the chief, with the mass $m_d=300$ kg, is located at the origin. For the gravitational constant $\mu$ and the orbital radius of the spacecraft $R_{0}$, $\omega = \sqrt{\mu/R_{0}^{3}}$ represents the orbital frequency. In this example, the spacecraft is in a circular orbit at an altitude of 850 km above the earth.", {}),
    ("p0011-b005", "text", ("p0011-b005",),
     r"We define $\zeta = [x,y,\dot{x},\dot{y}] \in \mathbb{R}^{4}$ as the system state and $u = [F_{x},F_{y}] \in \mathcal{U}\subseteq\mathbb{R}^{2}$ as the system input, then discretize the dynamics (23) with a sampling time of 20 s to obtain the discrete-time LTI system,", {}),
    ("p0011-b006", "text", ("p0011-b006",), dd(r"\zeta_{t+1} = A \zeta_{t} + B u_{t} + w_{t}.", "24"), {}),
    ("p0011-b007", "text", [56.0, 348.0, 556.0, 375.0],
     r"The additive stochastic noise, modeled by the Gaussian i.i.d. disturbance $w_{t} \in \mathbb{R}^{4}$, with $\mathbb{E}[w_{t}] = 0$, and $\mathbb{E}[w_{t}w_{t}^\top] = 10^{-4}\times\text{diag}(1, 1, 5 \times 10^{-4}, 5 \times 10^{-4})$, accounts for disturbances and model uncertainty.", {}),
    ("p0011-b007b", "text", [56.0, 376.0, 556.0, 388.0], "We define the target set and the safe set as in [4],", {}),
    ("p0011-b008", "text", [148.0, 394.0, 561.0, 436.0],
     dd(r"\mathcal{T} = \left\{ \zeta \in \mathbb{R}^{4}: |\zeta_{1}| \leq 0.1, -0.1 \leq \zeta_{2} \leq 0, |\zeta_{3}| \leq 0.01, |\zeta_{4}| \leq 0.01 \right\},", "25") + "\n\n"
     + dd(r"\mathcal{S} = \left\{\zeta \in \mathbb{R}^{4}: |\zeta_{1}| \leq \zeta_{2}, -1\leq \zeta_{2}, |\zeta_{3}| \leq 0.05, |\zeta_{4}| \leq 0.05 \right\},", "26"), {}),
    ("p0011-b010", "text", ("p0011-b010",),
     r"with a horizon of $N = 5$. We consider the initial position $x=y=-0.75$ km, the initial velocity $\dot{x}=\dot{y}=0$ km/s and $\mathcal{U} = [-0.1, 0.1]\times [-0.1, 0.1]$. The terminal time probability for this problem using existing approaches [4, 10] is known to be 0.86, which we assume to be the best open-loop controller-based reach-avoid probability estimate.", {}),
    ("p0011-b011", "text", ("p0011-b011",),
     r"We set $K=2000$ as the number of original samples to estimate the terminal time probability, with guarantees afforded by Theorem 1, and run 100 random experiments in which in each experiment $\mathcal{W}_N$ is generated randomly. Simulations are carried out using CVX [26] on a 2.8 GHz processor Intel Core i5 with 16 GB RAM. Figure 4a shows the $\mathrm{WSS}$ curve (mean value and standard deviation of the results of the 100 experiments) with up to 100 cells. Figure 4b shows the terminal time probability approximation provided by Algorithm 1. As proposed, the “knee” of Figure 4a coincides the “knee” of Figure 4b; improvements in the accuracy of Algorithm 1 are insignificant beyond $\hat{K}=20$. In practice, $\hat{K}$ can be selected from one single experiment in which $WSS$ is calculated for a random disturbance set $\mathcal{W}_K$ for up to 100 (maximum allowable) cells. The computation of $\mathrm{WSS}$ curve shown in Figure 4a, for one experiment using $k$-means method, took only about 2.68 s, hence is reasonable for *offline* computation to select $\hat{K}$. The reported time includes the computation time for solving 100 $k$-means with 1 to 100 cells. This time, which is associated with offline step, can be further reduced by changing the step size of $\hat{K}$ variation (horizontal axis) or calculating $\mathrm{WSS}$ for arbitrary $\hat{K}$s (e.g. finer steps at the beginning and coarser steps at the end). The run time for the online component of Algorithm 1 is shown in Figure 4c. Since Problem 3 is a mixed-integer linear program, the time complexity exponentially increases exponentially with the number of cells [18, Rem. 1].", {}),
    ("p0011-b012", "text", ("p0011-b012",),
     "We see in Figure 4b, that partitions with 20 to 40 cells provide a reasonable estimate of the terminal time probability, without significant loss of precision. The computed terminal time probability and the", {}),
])

# ---------------------------------------------------------------- page 12
page(12, r"""
Compared with the 150 dpi render of PDF page 12 and with the TeX source. The page prints the Figure 4
float at the top, in the middle of the sentence that starts on page 11 ('The computed terminal time
probability and the | mean value of the online run time ...'). The continuing text is therefore the
first item of this page (join_previous 'space'), and in the reading order (plan.json) Figure 4 and
its caption are placed after the page-11 paragraph 'We set $K=2000$ ...'. Figure 4 has three panels
with printed panel labels (a), (b), (c) above them; crop bbox from the ink extent of the render
(x 97.6-509.9, y 56.8-381.3) plus a margin, so that the panel labels, the axis labels ('wss',
$\hat{p}$, 'cpu time (s)', $\hat{K}$), all tick labels and the legend of panel (b) ('Algorithm 1',
'exact solution') are inside; the extractor's scattered picture text (tick labels, legend) is not
kept as text. Only panel (c) prints the horizontal axis label $\hat{K}$. Caption verbatim (double
space after 'Figure 4:' in the PDF not kept; no punctuation between '(a) ... offline)', '(b) ...'
and '(c) ...', as printed). Citations checked: [10], [4, 13], [10]; 'Table 1', 'Algorithm 1',
'Figure 5' resolved to the printed numbers. Heading '## 6 Conclusion'. Table 1 and Figure 5, which
the two paragraphs above the Conclusion refer to, are printed on page 13 (after the Conclusion); in
the reading order they follow these paragraphs. Kept as printed: '$\hat{K}=20$, 40 and 100 are
reported', 'large $K$s', 'of MILP problem', 'significantly decrease the running time'; the line-wrap
hyphens 'Fur-thermore' and 'Algo-rithm' are not real hyphens.
""", [
    ("p0012-b002", "text", ("p0012-b002",),
     r"mean value of the online run time for $\hat{K}=20$, 40 and 100 are reported in Table 1. As desired, Algorithm 1 provides a flexible trade-off between the accuracy and computation time by selecting a suitable partition, and can be significantly faster than the existing Fourier transform approach [10] and particle filter [4, 13] (which fails to deal with large $K$s due to the exponential complexity of MILP problem).", {"join_previous": "space"}),
    ("p0012-b003", "text", ("p0012-b003",),
     r"Figure 5 shows the position trajectory, associated with $\zeta_1$ and $\zeta_2$, obtained by the Fourier method [10] (blue dots) and the proposed Voronoi partition-based method (green stars) with 40 cells. Green regions show the uncertainty regions of Voronoi method at different time instants obtained by 2000 original scenarios.", {}),
    ("p0012-b000", "figure", [91.0, 51.0, 517.0, 387.0], "", {"label": "Figure 4", "asset_name": "figure-4"}),
    ("p0012-b001", "caption", ("p0012-b001",),
     r"Figure 4: Mean and standard deviation of (a) within-cluster sum of squares (used to select $\hat{K}$, offline) (b) terminal time probability (c) online run time with increasing number of cells $\hat{K}$, obtained from 100 experiments with 2000 original scenarios.", {}),
    ("p0012-b004", "heading", ("p0012-b004",), "## 6 Conclusion", {}),
    ("p0012-b005", "text", ("p0012-b005",),
     "In this paper we presented a novel partition-based method for under-approximating the terminal time probability through sample reduction. By using Hoeffding’s inequality, we provided a bound on the required number of scenarios to achieve a desired probabilistic bound on the approximation error. Furthermore, we proposed a method which clusters the taken scenarios in few cells, each cell represented by a seed, where the number of cells is selected by the user in a systematic manner using the trend of a given curve or based on the desired running time. The proposed method scales easily with dimension since the clustering computational complexity increases linearly with the dimension of data. In addition, the simulation results confirm that the proposed method significantly decrease the running time, and therefore, it can be easily applied to real-time systems.", {}),
])

# ---------------------------------------------------------------- page 13
page(13, r"""
Compared with the 150 dpi render of PDF page 13 and with the TeX source. The page contains only two
floats, printed after the Conclusion: Table 1 with its caption below it, and Figure 5 with its
caption. In the reading order (plan.json) Table 1 follows the Section 5 paragraph that cites it
('... are reported in Table 1. ...') and Figure 5 follows the paragraph 'Figure 5 shows ...'.
Table 1 was rebuilt as a 3-column cell table from the page and the TeX tabular (the extractor's
cells contained <br> line breaks and split '$K=2000,\hat{K}=$ | 20'): header 'Method', 'Terminal
reach-avoid probability', 'Online run time (s)' (each header is wrapped over three lines in the
PDF); the first body cell of the printed table holds four lines, 'Algorithm 1' and the three
parameter settings, with the values 0.83/0.2, 0.8492/0.6, 0.8604/2.7 aligned with the three
settings: it is written as a label row 'Algorithm 1' with empty value cells followed by the three
setting rows; the cells are plain text with the Unicode letter K̂ (K with combining circumflex) for
$\hat{K}$, because the builder doubles backslashes when it renders table cells. The 'Particle filter [4, 13] (Problem 2), $K=2000$' row prints a
hyphen '-' in both value cells, and the last row is 'Fourier transform [10]' 0.862 and 66. All
values read on the render with their printed precision. Table bbox = the ruled box (ink extent
x 197.9-414.4, y 113.4-321.3) plus a margin. Caption verbatim ('Algo-rithm 1' is a line-wrap hyphen);
it has no final period. Figure 5 crop bbox from the non-white extent of the render (the plot has a
very light grey background, x 196.0-412.5, y 474.4-647.7) plus a margin; it contains the axis labels
$x$ and $y$, all tick labels and the legend ('Safe set', 'Target set', 'Initial state', 'Optimal
mean trajectory', 'Voronoi mean trajectory', 'Voronoi uncertainty region'). The legend text is small
(about 4 pt in the PDF) but legible in the crop at the build resolution. Caption verbatim; citation
[10] checked.
""", [
    ("p0013-b000", "table", [195.0, 110.0, 417.0, 325.0], "", {
        "label": "Table 1", "asset_name": "table-1",
        "rows": [
            ["Method", "Terminal reach-avoid probability", "Online run time (s)"],
            ["Algorithm 1", "", ""],
            ["K = 2000, K̂ = 20", "0.83", "0.2"],
            ["K = 2000, K̂ = 40", "0.8492", "0.6"],
            ["K = 2000, K̂ = 100", "0.8604", "2.7"],
            ["Particle filter [4, 13] (Problem 2), K = 2000", "-", "-"],
            ["Fourier transform [10]", "0.862", "66"],
        ]}),
    ("p0013-b001", "caption", ("p0013-b001",),
     "Table 1: Terminal reach-avoid probability estimate and computation time of existing methods and Algorithm 1", {}),
    ("p0013-b002", "figure", [194.0, 472.0, 415.0, 650.0], "", {"label": "Figure 5", "asset_name": "figure-5"}),
    ("p0013-b003", "caption", ("p0013-b003",),
     "Figure 5: Position trajectory for Fourier algorithm given in [10] and the proposed Voronoi partition-based method with 40 cells.", {}),
])

# ---------------------------------------------------------------- page 14
page(14, r"""
Compared with the 150 dpi render of PDF page 14 and with the authors' .bbl file. Heading
'## References' (unnumbered in the PDF). The page holds entries [1]-[15], one text item per entry
with the printed '[n]' label; the list bullets added by the extractor were removed and italics kept
for journal, proceedings and book titles. Every entry on this page was compared with the page image
(authors, title, venue, volume/number/pages, year). Line-wrap hyphens removed: 'reach-ability' ->
'reachability' in [7], 'com-pactness' -> 'compactness' in [11], 'approxi-mation' -> 'approximation'
in [13], 'Auto-matica' -> 'Automatica' in [14]. Printed compound hyphens kept: 'reach-avoid',
'discrete-time', 'multi-stage', 'stage-wise', 'particle-based', 'Reach-Avoid', 'High-Dimensional',
'particle-control', 'chance-constrained'. As printed: [4] 'Proc. IEEE Conf. Dec. & Ctrl. IEEE, 2013'
(no comma before the publisher); [5] the URL is followed by a period inside the link text
('https://arxiv.org/abs/1704.03555.'); [9] has no volume; [10] title in capitals and
'IEEE Ctrl. Syst. Letters.,'; [11] starts with the repeated-author dash '——,' (same authors as
[10], A. Vinod and M. Oishi); [14] 'A new robust mpc' in lower case and no volume/pages; [15]
'Açıkmeşe' with restored diacritics.
""", [
    ("p0014-b000", "heading", ("p0014-b000",), "## References", {}),
    ("p0014-b001", "text", ("p0014-b001",), "[1] S. Summers and J. Lygeros, “Verification of discrete time stochastic hybrid systems: A stochastic reach-avoid decision problem,” *Automatica*, vol. 46, no. 12, pp. 1951–1961, 2010.", {}),
    ("p0014-b002", "text", ("p0014-b002",), "[2] B. HomChaudhuri, A. P. Vinod, and M. Oishi, “Computation of forward stochastic reach sets: Application to stochastic, dynamic obstacle avoidance,” in *American Control Conf.*, Seattle, WA, 2017.", {}),
    ("p0014-b003", "text", ("p0014-b003",), "[3] N. Malone, K. Lesser, M. Oishi, and L. Tapia, “Stochastic reachability based motion planning for multiple moving obstacle avoidance,” in *Proc. Hybrid Syst.: Comput. and Ctrl.*, 2014, pp. 51–60.", {}),
    ("p0014-b004", "text", ("p0014-b004",), "[4] K. Lesser, M. Oishi, and R. S. Erwin, “Stochastic reachability for control of spacecraft relative motion,” in *Proc. IEEE Conf. Dec. & Ctrl.* IEEE, 2013, pp. 4705–4712.", {}),
    ("p0014-b005", "text", ("p0014-b005",), "[5] J. Gleason, A. Vinod, and M. Oishi, “Underapproximation of reach-avoid sets for discrete-time stochastic systems via Lagrangian methods,” in *IEEE Conf. Dec. Ctrl.*, 2017. [Online]. Available: https://arxiv.org/abs/1704.03555.", {}),
    ("p0014-b006", "text", ("p0014-b006",), "[6] A. Abate, M. Prandini, J. Lygeros, and S. Sastry, “Probabilistic reachability and safety for controlled discrete time stochastic hybrid systems,” *Automatica*, vol. 44, no. 11, pp. 2724–2734, 2008.", {}),
    ("p0014-b007", "text", ("p0014-b007",), "[7] A. Abate, S. Amin, M. Prandini, J. Lygeros, and S. Sastry, “Computational approaches to reachability analysis of stochastic hybrid systems,” in *Proc. Hybrid Syst.: Comput. and Ctrl.*, 2007, pp. 4–17.", {}),
    ("p0014-b008", "text", ("p0014-b008",), "[8] N. Kariotoglou, K. Margellos, and J. Lygeros, “On the computational complexity and generalization properties of multi-stage and stage-wise coupled scenario programs,” *Syst. and Ctrl. Lett.*, vol. 94, pp. 63–69, 2016.", {}),
    ("p0014-b009", "text", ("p0014-b009",), "[9] G. Manganini, M. Pirotta, M. Restelli, L. Piroddi, and M. Prandini, “Policy search for the optimal control of Markov Decision Processes: A novel particle-based iterative scheme,” *IEEE Trans. Cybern.*, pp. 1–13, 2015.", {}),
    ("p0014-b010", "text", ("p0014-b010",), "[10] A. Vinod and M. Oishi, “Scalable Underapproximation for the Stochastic Reach-Avoid Problem for High-Dimensional LTI Systems Using Fourier Transforms,” *IEEE Ctrl. Syst. Letters.*, vol. 1, no. 2, pp. 316–321, 2017.", {}),
    ("p0014-b011", "text", ("p0014-b011",), "[11] ——, “Scalable underapproximative verification of stochastic LTI systems using convexity and compactness,” in *Proc. Hybrid Syst.: Comput. and Ctrl.*, 2018, pp. 1–10.", {}),
    ("p0014-b012", "text", ("p0014-b012",), "[12] D. Drzajic, N. Kariotoglou, M. Kamgarpour, and J. Lygeros, “A semidefinite programming approach to control synthesis for stochastic reach-avoid problems,” in *Int’l Workshop on Applied Verification for Continuous and Hybrid Syst.*, 2016, pp. 134–143.", {}),
    ("p0014-b013", "text", ("p0014-b013",), "[13] L. Blackmore, M. Ono, A. Bektassov, and B. C. Williams, “A probabilistic particle-control approximation of chance-constrained stochastic predictive control,” *IEEE Trans. Robot.*, vol. 26, no. 3, pp. 502–517, 2010.", {}),
    ("p0014-b014", "text", ("p0014-b014",), "[14] H. Sartipizadeh and T. L. Vincent, “A new robust mpc using an approximate convex hull,” *Automatica*, 2018.", {}),
    ("p0014-b015", "text", ("p0014-b015",), "[15] H. Sartipizadeh and B. Açıkmeşe, “Approximate convex hull based sample truncation for scenario approach to chance constrained trajectory optimization,” in *Proc. American Ctrl. Conf.*, 2018, pp. 4700–4705.", {}),
])

# ---------------------------------------------------------------- page 15
page(15, r"""
Compared with the 150 dpi render of PDF page 15 and with the authors' .bbl file. The page holds
entries [16]-[26] of the reference list in the upper half; the rest of the page is blank and the
paper ends here (no appendix in this version). One text item per entry with the printed '[n]'
label, extractor bullets removed, italics kept. Every entry was compared with the page image. No
word is hyphenated at a line end on this page; 'NP-hardness', 'sum-of-squares', 'k-means',
'McGraw-Hill' are printed compound hyphens. As printed: [21] 'euclidean' in lower case and the DOI
URL https://doi.org/10.1007/s10994-009-5103-0 without a final period; [22] 'Algorithm as 136: A
k-means clustering algorithm'; [23] 'J. Amer. Statistical Asso.'; [25] the author is printed
'W. E. Weisel'; [26] the URL http://cvxr.com/cvx is followed by ', Mar. 2014.'.
""", [
    ("p0015-b000", "text", ("p0015-b000",), "[16] G. C. Calafiore and L. Fagiano, “Stochastic model predictive control of LPV systems via scenario optimization,” *Automatica*, vol. 49, no. 6, pp. 1861–1866, 2013.", {}),
    ("p0015-b001", "text", ("p0015-b001",), "[17] G. C. Calafiore and M. C. Campi, “The scenario approach to robust control design,” *IEEE Trans. Autom. Ctrl.*, vol. 51, no. 5, pp. 742–753, May 2006.", {}),
    ("p0015-b002", "text", ("p0015-b002",), "[18] A. Bemporad and M. Morari, “Control of systems integrating logic, dynamics, and constraints,” *Automatica*, vol. 35, no. 3, pp. 407–427, 1999.", {}),
    ("p0015-b003", "text", ("p0015-b003",), "[19] S. Boyd and L. Vandenberghe, *Convex optimization*. Cambridge Univ. Press, 2004.", {}),
    ("p0015-b004", "text", ("p0015-b004",), "[20] J. A. Hartigan, *Clustering algorithms*. Wiley, 1975.", {}),
    ("p0015-b005", "text", ("p0015-b005",), "[21] D. Aloise, A. Deshpande, P. Hansen, and P. Popat, “NP-hardness of euclidean sum-of-squares clustering,” *Machine Learning*, vol. 75, no. 2, pp. 245–248, May 2009. [Online]. Available: https://doi.org/10.1007/s10994-009-5103-0", {}),
    ("p0015-b006", "text", ("p0015-b006",), "[22] J. A. Hartigan and M. A. Wong, “Algorithm as 136: A k-means clustering algorithm,” *J. Royal Statistical Society. Series C (Applied Statistics)*, vol. 28, no. 1, pp. 100–108, 1979.", {}),
    ("p0015-b007", "text", ("p0015-b007",), "[23] W. Hoeffding, “Probability Inequalities for Sums of Bounded Random Variables,” *J. Amer. Statistical Asso.*, vol. 58, no. 301, pp. 13–30, 1963.", {}),
    ("p0015-b008", "text", ("p0015-b008",), "[24] M. Prandini, J. Hu, J. Lygeros, and S. Sastry, “A probabilistic approach to aircraft conflict detection,” *IEEE Trans. Intelligent Transportation Syst.*, vol. 1, no. 4, pp. 199–220, 2000.", {}),
    ("p0015-b009", "text", ("p0015-b009",), "[25] W. E. Weisel, *Spaceflight dynamics*. New York, McGraw-Hill Book Co, 1989, vol. 2.", {}),
    ("p0015-b010", "text", ("p0015-b010",), "[26] M. Grant and S. Boyd, “CVX: Matlab software for disciplined convex programming, version 2.1,” http://cvxr.com/cvx, Mar. 2014.", {}),
])
