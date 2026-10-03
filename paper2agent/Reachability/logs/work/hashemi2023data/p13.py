from pagelib import *
P = 13
items = [
    figure("p0013-b000", [49.0, 67.0, 575.0, 362.0], "Figure 3", "figure-3"),
    caption("p0013-b001", B(P, "p0013-b001"),
            r"Figure 3: Laubloomis: Shows our data driven reachability analysis from 200-step dataset along with 100 random trajectories generated from $M$. We also included the reachability analysis from CORA toolbox that is based on the ideally known model depicted as green regions. The bounds in black line shows the reachability analysis with approx-star technique combined with conformal inference with prescribed failure probability $\varepsilon=0.01$."),
    text("p0013-b002", B(P, "p0013-b002"),
         "[6] C. Huang, J. Fan, X. Chen, W. Li, and Q. Zhu, “Polar: A polynomial arithmetic framework for verifying neural-network controlled systems,” in *International Symposium on Automated Technology for Verification and Analysis*. Springer, 2022, pp. 414–430."),
    text("p0013-b003", B(P, "p0013-b003"),
         "[7] X. Chen, E. Ábrahám, and S. Sankaranarayanan, “Flow\\*: An analyzer for non-linear hybrid systems,” in *Computer Aided Verification: 25th International Conference, CAV 2013, Saint Petersburg, Russia, July 13-19, 2013. Proceedings 25*. Springer, 2013, pp. 258–263."),
    text("p0013-b004", B(P, "p0013-b004"),
         "[8] S. Dutta, X. Chen, S. Jha, S. Sankaranarayanan, and A. Tiwari, “Sherlock-a tool for verification of neural network feedback systems: demo abstract,” in *Proceedings of the 22nd ACM International Conference on Hybrid Systems: Computation and Control*, 2019, pp. 262–263."),
    text("p0013-b005", B(P, "p0013-b005"),
         "[9] X. Koutsoukos and D. Riley, “Computational methods for reachability analysis of stochastic hybrid systems,” in *Hybrid Systems: Computation and Control: 9th International Workshop, HSCC 2006, Santa Barbara, CA, USA, March 29-31, 2006. Proceedings 9*. Springer, 2006, pp. 377–391."),
    text("p0013-b006", B(P, "p0013-b006"),
         "[10] S. Bansal, M. Chen, S. Herbert, and C. J. Tomlin, “Hamilton-jacobi reachability: A brief overview and recent advances,” in *2017 IEEE 56th Annual Conference on Decision and Control (CDC)*. IEEE, 2017, pp. 2242–2253."),
    pageno(P),
]
save(P, items, r"""
Compared with the 130 dpi render and a crop of the figure region of PDF page 13, and with
sections/experimental_results.tex and main.bbl. Figure 3 (seven panels $x_1,\ldots,x_7$, four in the first row and three
in the second, small tick labels, no axis titles) is one image crop wider than the text block; all four edges were
checked (leftmost tick labels and the '200' ticks at the right edge complete, caption excluded). Caption verbatim,
including the authors' wording 'Shows our data driven reachability analysis from 200-step dataset' and 'The bounds in
black line shows'. The figure is a float printed at the top of this page, inside the reference list; in the reading
order it follows the Laubloomis paragraph 'Again, we train ...' of Section 4 (page 11), which refers to it.
References [6]-[10]: one item per entry, the extractor's bullet markers removed, italics as printed; every entry compared
with the page image and the .bbl. In [7] the asterisk of 'Flow*' is escaped for Markdown. Hyphens '13-19' in [7] and
'29-31' in [9] are printed as hyphens (not en dashes), as in the .bbl; lower-case 'Hamilton-jacobi' in [10] and
'Sherlock-a tool' in [8] as printed. Line-wrap hyphen removed in 'verification' ([8]).
""")
