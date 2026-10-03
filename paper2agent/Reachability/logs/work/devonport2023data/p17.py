from pagelib import *

refs = [
"[1] T. Alamo, R. Tempo, and E. F. Camacho, *Randomized strategies for probabilistic solutions of uncertain feasibility and optimization problems*, IEEE Transactions on Automatic Control, 54 (2009), pp. 2545–2559.",
"[2] A. Askari, F. Yang, and L. El Ghaoui, *Kernel-based outlier detection using the inverse Christoffel function*, arXiv preprint arXiv:1806.06775, (2018).",
"[3] P. Bouffard, *On-board model predictive control of a quadrotor helicopter: Design, implementation, and experiments*, (2012), http://www.eecs.berkeley.edu/Pubs/TechRpts/2012/EECS-2012-241.html.",
"[4] F. M. Callier and C. A. Desoer, *Linear system theory*, Springer Science & Business Media, 1991.",
"[5] S. Coogan and M. Arcak, *A benchmark problem in transportation networks*, arXiv preprint arXiv:1803.00367, (2018).",
"[6] A. Cuevas and R. Fraiman, *A plug-in approach to support estimation*, The Annals of Statistics, 25 (1997), pp. 2300–2312.",
"[7] C. F. Daganzo, *The cell transmission model: A dynamic representation of highway traffic consistent with the hydrodynamic theory*, Transportation Research Part B: Methodological, 28 (1994), pp. 269–287.",
"[8] A. Devonport and M. Arcak, *Data-driven reachable set computation using adaptive Gaussian process classification and Monte Carlo methods*, in 2020 American Control Conference (ACC), IEEE, 2020, pp. 2629–2634.",
"[9] A. Devonport and M. Arcak, *Estimating reachable sets with scenario optimization*, vol. 120 of Proceedings of Machine Learning Research, PMLR, 10–11 Jun 2020, pp. 75–84.",
"[10] A. Devonport, F. Yang, L. El Ghaoui, and M. Arcak, *Data-driven reachability analysis with Christoffel functions*, 2021, https://arxiv.org/abs/2104.13902.",
"[11] F. Djeumou, A. P. Vinod, E. Goubault, S. Putot, and U. Topcu, *On-the-fly control of unknown smooth systems from limited data*, arXiv preprint arXiv:2009.12733, (2020).",
"[12] A. N. Dolia, T. De Bie, C. J. Harris, J. Shawe-Taylor, and D. M. Titterington, *The minimum volume covering ellipsoid estimation in kernel-defined feature spaces*, in European Conference on Machine Learning, Springer, 2006, pp. 630–637.",
"[13] R. M. Dudley, *Central limit theorems for empirical measures*, The Annals of Probability, (1978), pp. 899–929.",
"[14] C. Fan, B. Qi, S. Mitra, and M. Viswanathan, *DryVR: data-driven verification and compositional reasoning for automotive systems*, in International Conference on Computer Aided Verification, Springer, 2017, pp. 441–461.",
"[15] L. Hewing and M. N. Zeilinger, *Scenario-based probabilistic reachable sets for recursively feasible stochastic model predictive control*, IEEE Control Systems Letters, 4 (2019), pp. 450–455.",
"[16] D. Ioli, A. Falsone, H. Marianne, B. Axel, and M. Prandini, *A smart grid energy management problem for data-driven design with probabilistic reachability guarantees*, in 4th International Workshop on Applied Verification of Continuous and Hybrid Systems, vol. 48, 2017, pp. 2–19.",
"[17] J. Langford and R. Schapire, *Tutorial on practical prediction theory for classification*, Journal of Machine Learning Research, 6 (2005).",
"[18] J. Langford and J. Shawe-Taylor, *PAC-Bayes & margins*, Advances in Neural Information Processing Systems, (2003), pp. 439–446.",
"[19] J. B. Lasserre and E. Pauwels, *The empirical Christoffel function in statistics and machine learning*, arXiv preprint arXiv:1701.02886, (2017).",
]

items = [
    running_header(17),
    text("p0017-b002", [72.0, 99.0, 442.0, 203.0],
         "Improvements to the general theory can advance in step with advances in Bayesian PAC analysis. For instance, there are new results in theory of *derandomizing* Bayesian PAC bounds, which could offer sample efficiency improvements over the argument used in Lemma 3.9 to apply the Bayesian PAC bound to the central concept. Furthermore, domain-specific knowledge could be applied to the GP prior used to construct the Christoffel functions. For instance, in reachability problems and estimate of the system sensitivity matrix could be used to intelligently select length-scales in the kernel, along with other algorithm hyper-parameters such as the initial sample size and batch size."),
    heading("p0017-b003", [227.0, 223.0, 286.0, 230.0], "## References"),
    text("p0017-refs", [74.0, 243.0, 442.0, 688.0], "\n\n".join(refs)),
]

save(17, items, r"""
Compared with the 130-dpi render. Second paragraph of the Conclusion taken from the authors' TeX and compared with the page ('in reachability problems and estimate of the system sensitivity matrix' is printed like this; 'Lemma 3.9' resolved). 'REFERENCES' (centred capitals) written as '## References'. Bibliography entries [1]-[19] taken from the authors' .bbl file (siamplain style) and each entry compared with the page: numbers, author lists, titles, venues, volume/year/pages all agree. One entry per paragraph in a single text item; author names are printed in small capitals and written in normal case; titles are italic. Peculiarities of the printed list kept: stray comma before the year in entries [2], [5], [11], [13], [18], [19] (', (2018).'), entry [13] without volume number, entry [17] without pages. Entry [3]: the URL is printed across a line break after 'TechRpts/2012/' and is written as one URL without space; entry [16] page range '2–19' and entry [15] '450–455' (broken across lines in the print) checked. Line-wrap hyphens removed (Fur-thermore, con-struct, Statis-tics, Gaus-sian, compo-sitional, fea-sible, man-agement, Jour-nal, Euro-pean, imple-mentation); real hyphens kept (domain-specific, length-scales, hyper-parameters, Kernel-based, On-board, plug-in, Data-driven, On-the-fly, kernel-defined, Scenario-based, PAC-Bayes, Shawe-Taylor). Omitted: running header (short title and page number 17).
""")
