from pagelib import *
P = 15
R = [
 ("p0015-b000", "[24] L. Bortolussi, F. Cairoli, N. Paoletti, S. A. Smolka, and S. D. Stoller, “Neural predictive monitoring,” in *Runtime Verification: 19th International Conference, RV 2019, Porto, Portugal, October 8–11, 2019, Proceedings 19*. Springer, 2019, pp. 129–147."),
 ("p0015-b001", "[25] F. Cairoli, N. Paoletti, and L. Bortolussi, “Conformal quantitative predictive monitoring of stl requirements for stochastic processes,” in *Proceedings of the 26th ACM International Conference on Hybrid Systems: Computation and Control*, 2023, pp. 1–11."),
 ("p0015-b002", "[26] L. Lindemann, X. Qin, J. V. Deshmukh, and G. J. Pappas, “Conformal prediction for stl runtime verification,” in *Proceedings of the ACM/IEEE 14th International Conference on Cyber-Physical Systems (with CPS-IoT Week 2023)*, 2023, pp. 142–153."),
 ("p0015-b003", "[27] X. Qin, Y. Xia, A. Zutshi, C. Fan, and J. V. Deshmukh, “Statistical verification of cyber-physical systems using surrogate models and conformal inference,” in *2022 ACM/IEEE 13th International Conference on Cyber-Physical Systems (ICCPS)*. IEEE, 2022, pp. 116–126."),
 ("p0015-b004", "[28] A. B. Kurzhanski and P. Varaiya, “Ellipsoidal techniques for reachability analysis,” in *Hybrid Systems: Computation and Control: Third International Workshop, HSCC 2000 Pittsburgh, PA, USA, March 23–25, 2000 Proceedings*. Springer, 2002, pp. 202–214."),
 ("p0015-b005", "[29] J. Lei, M. G’Sell, A. Rinaldo, R. J. Tibshirani, and L. Wasserman, “Distribution-free predictive inference for regression,” *Journal of the American Statistical Association*, vol. 113, no. 523, pp. 1094–1111, 2018."),
 ("p0015-b006", "[30] A. N. Angelopoulos and S. Bates, “A gentle introduction to conformal prediction and distribution-free uncertainty quantification,” *arXiv preprint arXiv:2107.07511*, 2021."),
 ("p0015-b007", "[31] L. Lindemann, M. Cleaveland, G. Shim, and G. J. Pappas, “Safe planning in dynamic environments using conformal prediction,” *IEEE Robotics and Automation Letters*, 2023."),
 ("p0015-b008", "[32] R. Luo, S. Zhao, J. Kuck, B. Ivanovic, S. Savarese, E. Schmerling, and M. Pavone, “Sample-efficient safety assurances using conformal prediction,” in *Algorithmic Foundations of Robotics XV: Proceedings of the Fifteenth Workshop on the Algorithmic Foundations of Robotics*. Springer, 2022, pp. 149–169."),
 ("p0015-b009", "[33] R. J. Tibshirani, R. Foygel Barber, E. Candes, and A. Ramdas, “Conformal prediction under covariate shift,” *Advances in neural information processing systems*, vol. 32, 2019."),
 ("p0015-b010", "[34] H.-D. Tran, D. Manzanas Lopez, P. Musau, X. Yang, L. V. Nguyen, W. Xiang, and T. T. Johnson, “Star-based reachability analysis of deep neural networks,” in *Formal Methods–The Next 30 Years: Third World Congress, FM 2019, Porto, Portugal, October 7–11, 2019, Proceedings 3*. Springer, 2019, pp. 670–686."),
 ("p0015-b011", "[35] H.-D. Tran, F. Cai, M. L. Diego, P. Musau, T. T. Johnson, and X. Koutsoukos, “Safety verification of cyber-physical systems with reinforcement learning control,” *ACM Transactions on Embedded Computing Systems (TECS)*, vol. 18, no. 5s, pp. 1–22, 2019."),
 ("p0015-b012", "[36] M. Cleaveland, I. Lee, G. J. Pappas, and L. Lindemann, “Conformal prediction regions for time series using linear complementarity programming,” *arXiv preprint arXiv:2304.01075*, 2023."),
 ("p0015-b013", "[37] M. Althoff, “An introduction to cora 2015.” *ARCH@ CPSWeek*, vol. 34, pp. 120–151, 2015."),
]
items = [text(i, B(P, i), md) for i, md in R] + [pageno(P)]
save(P, items, r"""
Compared with the 130 dpi render of PDF page 15 and with main.bbl. The page contains only references [24]-[37], the end of
the paper; this arXiv version has no appendix (the TeX source archive contains an unused sections/appendix.tex, 'Training
the Model', which is not included by main.tex and is not printed in the PDF). One item per entry, the extractor's bullet
markers removed, italics as printed. Every entry was read on the page image and compared with the .bbl and, by script,
with the PDF text layer. Kept as printed: lower-case 'stl' in [25] and [26], 'cora' in [37]; 'G’Sell' in [29] with the
printed apostrophe; 'HSCC 2000 Pittsburgh' without a comma and '2000 Proceedings' in [28]; 'Formal Methods–The Next 30
Years' with an en dash in [34]; the full stop inside the quotation marks in [37]. Line-wrap hyphens removed in
'monitoring' ([24]), 'environments' ([31]), 'verification' ([35]); 'cyber-physical' ([27]), 'Sample-efficient' ([32]) and
the name 'Johnson' ([34], broken as 'John-son') were restored after checking the .bbl.
""")
