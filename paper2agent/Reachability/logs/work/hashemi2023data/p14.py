from pagelib import *
P = 14
R = [
 ("p0014-b000", "[11] L. Bortolussi and G. Sanguinetti, “A statistical approach for computing reachability of non-linear and stochastic dynamical systems,” in *International Conference on Quantitative Evaluation of Systems*. Springer, 2014, pp. 41–56."),
 ("p0014-b001", "[12] M. Kwiatkowska, G. Norman, and D. Parker, “Stochastic model checking,” *Formal Methods for Performance Evaluation: 7th International School on Formal Methods for the Design of Computer, Communication, and Software Systems, SFM 2007, Bertinoro, Italy, May 28-June 2, 2007, Advanced Lectures 7*, pp. 220–270, 2007."),
 ("p0014-b002", "[13] A. Legay, A. Lukina, L. M. Traonouez, J. Yang, S. A. Smolka, and R. Grosu, “Statistical model checking,” in *Computing and software science: state of the art and perspectives*. Springer, 2019, pp. 478–504."),
 ("p0014-b003", "[14] A. Devonport, F. Yang, L. El Ghaoui, and M. Arcak, “Data-driven reachability analysis with christoffel functions,” in *2021 60th IEEE Conference on Decision and Control (CDC)*. IEEE, 2021, pp. 5067–5072."),
 ("p0014-b004", "[15] A. Alanwar, A. Koch, F. Allgöwer, and K. H. Johansson, “Data-driven reachability analysis from noisy data,” *IEEE Transactions on Automatic Control*, 2023."),
 ("p0014-b005", "[16] A. Devonport and M. Arcak, “Data-driven reachable set computation using adaptive gaussian process classification and monte carlo methods,” in *2020 American Control Conference (ACC)*. IEEE, 2020, pp. 2629–2634."),
 ("p0014-b006", "[17] J. F. Fisac, A. K. Akametalu, M. N. Zeilinger, S. Kaynama, J. Gillula, and C. J. Tomlin, “A general safety framework for learning-based control in uncertain robotic systems,” *IEEE Transactions on Automatic Control*, vol. 64, no. 7, pp. 2737–2752, 2018."),
 ("p0014-b007", "[18] A. Lin and S. Bansal, “Generating formal safety assurances for high-dimensional reachability,” in *2023 IEEE International Conference on Robotics and Automation (ICRA)*. IEEE, 2023, pp. 10 525–10 531."),
 ("p0014-b008", "[19] C. Fan, B. Qi, S. Mitra, and M. Viswanathan, “Dryvr: Data-driven verification and compositional reasoning for automotive systems,” in *International Conference on Computer Aided Verification*. Springer, 2017, pp. 441–461."),
 ("p0014-b009", "[20] N. Matni and S. Tu, “A tutorial on concentration bounds for system identification,” in *2019 IEEE 58th Conference on Decision and Control (CDC)*. IEEE, 2019, pp. 3741–3749."),
 ("p0014-b010", "[21] H.-D. Tran, X. Yang, D. Manzanas Lopez, P. Musau, L. V. Nguyen, W. Xiang, S. Bak, and T. T. Johnson, “Nnv: the neural network verification tool for deep neural networks and learning-enabled cyber-physical systems,” in *Computer Aided Verification: 32nd International Conference, CAV 2020, Los Angeles, CA, USA, July 21–24, 2020, Proceedings, Part I*. Springer, 2020, pp. 3–17."),
 ("p0014-b011", "[22] V. Vovk, A. Gammerman, and G. Shafer, *Algorithmic learning in a random world*. Springer, 2005, vol. 29."),
 ("p0014-b012", "[23] J. Lei and L. Wasserman, “Distribution-free prediction bands for non-parametric regression,” *Journal of the Royal Statistical Society: Series B: Statistical Methodology*, pp. 71–96, 2014."),
]
items = [text(i, B(P, i), md) for i, md in R] + [pageno(P)]
save(P, items, r"""
Compared with the 130 dpi render of PDF page 14 and with main.bbl. The page contains only references [11]-[23]. One item
per entry, the extractor's bullet markers removed, italics as printed. Every entry was read on the page image (authors,
title, venue, volume/number/pages, year) and compared with the .bbl and, by script, with the PDF text layer. Kept as
printed: lower-case 'christoffel' in [14], 'gaussian' and 'monte carlo' in [16], 'Nnv' in [21], 'Dryvr' in [19]; the page
range of [18] is printed with thin spaces as '10 525–10 531'; 'May 28-June 2' in [12] with a hyphen; 'July 21–24' in
[21] with an en dash; 'Allgöwer' in [15] with umlaut. The compounds 'non-linear' in [11] and
'learning-enabled' in [21] are broken at their own hyphens and keep them; line-wrap hyphens were removed in 'Evaluation'
([11]), 'compositional' ([19]) and 'Conference' ([21]).
""")
