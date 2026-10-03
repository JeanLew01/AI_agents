from common import Page
p = Page(7)

p.text('by de-randomization are large relative to this baseline, we argue that whenever a sampling-based approach is deemed acceptable, the circumstances where de-randomization is worth the price are rare.', [54, 55, 299, 101], join_previous='space')
p.heading('## VI. Conclusion', [138, 110, 215, 118])
p.text('In this paper, we demonstrate that the holdout method can significantly decrease the sample complexity in finding probabilistically tight reachable sets; this method is highly efficient when collecting scenarios is computationally cheap. Furthermore, we complement our work with a discussion on the necessity of probabilistic reachability bounds within the context of data-driven analysis.', [54, 126, 299, 208])
p.heading('## VII. Acknowledgments', [118, 218, 234, 226])
p.text('This paper is supported in part by the NSF project CNS-2111688. The first author was also supported by an NSF Graduate Research Fellowship.', [54, 234, 299, 267])
p.heading('## References', [148, 277, 205, 285])

refs = [
 '[1] M. Althoff, “Reachability analysis and its application to the safety assessment of autonomous cars,” Ph.D. dissertation, Technische Universität München, 2010.',
 '[2] S. Prajna and A. Jadbabaie, “Safety verification of hybrid systems using barrier certificates,” in *Hybrid Systems: Computation and Control*. Berlin, Heidelberg: Springer Berlin Heidelberg, 2004, pp. 477–492.',
 '[3] M. Chen and C. J. Tomlin, “Hamilton–Jacobi reachability: Some recent theoretical advances and applications in unmanned airspace management,” *Annual Review of Control, Robotics, and Autonomous Systems*, vol. 1, no. 1, pp. 333–358, 2018.',
 '[4] M. Althoff, G. Frehse, and A. Girard, “Set propagation techniques for reachability analysis,” *Annual Review of Control, Robotics, and Autonomous Systems*, vol. 4, no. 1, pp. 369–395, 2021.',
 '[5] A. Girard, “Reachability of uncertain linear systems using zonotopes,” in *Hybrid Systems: Computation and Control*. Berlin, Heidelberg: Springer Berlin Heidelberg, 2005, pp. 291–305.',
 '[6] A. Devonport and M. Arcak, “Estimating reachable sets with scenario optimization,” in *Proceedings of the 2nd Conference on Learning for Dynamics and Control*, ser. Proceedings of Machine Learning Research, vol. 120. PMLR, 10–11 Jun 2020, pp. 75–84.',
 '[7] ——, “Data-driven reachable set computation using adaptive gaussian process classification and monte carlo methods,” in *2020 American Control Conference (ACC)*, 2020, pp. 2629–2634.',
 '[8] H. Sartipizadeh, A. P. Vinod, B. Açikmeşe, and M. Oishi, “Voronoi partition-based scenario reduction for fast sampling-based stochastic reachability computation of linear systems,” in *2019 American Control Conference (ACC)*, 2019, pp. 37–44.',
 '[9] A. Devonport, F. Yang, L. E. Ghaoui, and M. Arcak, “Data-driven reachability and support estimation with Christoffel functions,” *IEEE Transactions on Automatic Control*, vol. 68, no. 9, pp. 5216–5229, 2023.',
 '[10] T. Lew and M. Pavone, “Sampling-based reachability analysis: A random set theory approach with adversarial sampling,” *ArXiv*, 2020.',
 '[11] P. Griffioen and M. Arcak, “Data-driven reachability analysis for Gaussian process state space models,” in *2023 62nd IEEE Conference on Decision and Control (CDC)*, 2023, pp. 4100–4105.',
 '[12] A. Alanwar, A. Koch, F. Allgöwer, and K. H. Johansson, “Data-driven reachability analysis from noisy data,” *IEEE Transactions on Automatic Control*, vol. 68, no. 5, pp. 3054–3069, 2023.',
 '[13] D. Sun and S. Mitra, “Neureach: Learning reachability functions from simulations,” in *Tools and Algorithms for the Construction and Analysis of Systems*, 2022, pp. 322–337.',
 '[14] A. Devonport, F. Yang, L. El Ghaoui, and M. Arcak, “Data-driven reachability analysis with Christoffel functions,” in *2021 60th IEEE Conference on Decision and Control (CDC)*. IEEE Press, 2021, p. 5067–5072.',
 '[15] M. Stone, “Cross-validatory choice and assessment of statistical predictions,” *Journal of the Royal Statistical Society. Series B (Methodological)*, vol. 36, no. 2, pp. 111–147, 1974.',
 '[16] R. Kohavi, “A study of cross-validation and bootstrap for accuracy estimation and model selection,” in *Proceedings of the 14th International Joint Conference on Artificial Intelligence (IJCAI)*, 1995, pp. 1137–1143.',
 '[17] T. Hastie, R. Tibshirani, and J. Friedman, *The Elements of Statistical Learning: Data Mining, Inference, and Prediction*, 2nd ed., ser. Springer Series in Statistics. Springer, 2009.',
 '[18] R. Tempo, G. Calafiore, and F. Dabbene, *Randomized Algorithms for Analysis and Control of Uncertain Systems: With Applications*, 2nd ed. Springer Publishing Company, Incorporated, 2012.',
 '[19] E. Dietrich, A. Devonport, and M. Arcak, “Nonconvex scenario optimization for data-driven reachability,” in *Proceedings of the 6th Annual Learning for Dynamics & Control Conference*, ser. Proceedings of Machine Learning Research, vol. 242. PMLR, 15–17 Jul 2024, pp. 514–527.',
 '[20] A. Lin and S. Bansal, “Verification of neural reachable tubes via scenario optimization and conformal prediction,” in *Proceedings of the 6th Annual Learning for Dynamics & Control Conference*, ser. Proceedings of Machine Learning Research, vol. 242. PMLR, 15–17 Jul 2024, pp. 719–731.',
 '[21] L. Hewing and M. N. Zeilinger, “Scenario-based probabilistic reachable sets for recursively feasible stochastic model predictive control,” *IEEE Control Systems Letters*, vol. 4, no. 2, pp. 450–455, 2020.',
 '[22] N. Hashemi, X. Qin, L. Lindemann, and J. V. Deshmukh, “Data-driven reachability analysis of stochastic dynamical systems with conformal inference,” in *2023 62nd IEEE Conference on Decision and Control (CDC)*, 2023, pp. 3102–3109.',
 '[23] A. Tebjou, G. Frehse, and F. Chamroukhi, “Data-driven reachability using Christoffel functions and conformal prediction,” in *Proceedings of the Twelfth Symposium on Conformal and Probabilistic Prediction with Applications*, vol. 204. PMLR, Sep 2023, pp. 194–213.',
 '[24] A. Muthali, H. Shen, S. Deglurkar, M. H. Lim, R. Roelofs, A. Faust, and C. Tomlin, “Multi-agent reachability calibration with conformal prediction,” in *2023 62nd IEEE Conference on Decision and Control (CDC)*, 2023, pp. 6596–6603.',
 '[25] A. K. Akametalu, J. F. Fisac, J. H. Gillula, S. Kaynama, M. N. Zeilinger, and C. J. Tomlin, “Reachability-based safe learning with Gaussian processes,” in *53rd IEEE Conference on Decision and Control*, 2014, pp. 1424–1431.',
 '[26] R. S. Dembo, “Scenario optimization,” *Annals of Operations Research*, vol. 30, pp. 63–80, 1991.',
 '[27] M. C. Campi, S. Garatti, and F. A. Ramponi, “A general scenario theory for nonconvex optimization and decision making,” *IEEE Transactions on Automatic Control*, vol. 63, no. 12, pp. 4067–4078, 2018.',
 '[28] J. Langford, “Tutorial on practical prediction theory for classification,” *Journal of Machine Learning Research*, vol. 6, pp. 273–306, 2005.',
 '[29] M. Hardt and B. Recht, *Patterns, predictions, and actions: Foundations of machine learning*. Princeton University Press, 2022.',
 '[30] I. M. Mitchell, J. Budzis, and A. Bolyachevets, “Invariant, viability and discriminating kernel under-approximation via zonotope scaling: Poster abstract,” in *Proceedings of the 22nd ACM International Conference on Hybrid Systems: Computation and Control*. HSCC, 2019, p. 268–269.',
 '[31] P. Bouffard, “On-board model predictive control of a quadrotor helicopter: Design, implementation, and experiments,” Master’s thesis, EECS Department, University of California, Berkeley, Dec 2012.',
 '[32] L. G. Valiant, “A theory of the learnable,” *Commun. ACM*, vol. 27, no. 11, p. 1134–1142, Nov. 1984.',
 '[33] A. Lecchini-Visintini, J. Lygeros, and J. M. Maciejowski, “Stochastic optimization on continuous domains with finite-time guarantees by markov chain monte carlo methods,” *IEEE Transactions on Automatic Control*, vol. 55, no. 12, pp. 2858–2863, 2010.',
 '[34] P. M. Esfahani, T. Sutter, and J. Lygeros, “Performance bounds for the scenario approach and an extension to a class of non-convex programs,” *IEEE Transactions on Automatic Control*, vol. 60, no. 1, pp. 46–58, 2014.',
 '[35] N. Boffi, S. Tu, N. Matni, J.-J. Slotine, and V. Sindhwani, “Learning stability certificates from data,” in *Proceedings of the 2020 Conference on Robot Learning*, ser. Proceedings of Machine Learning Research, vol. 155. PMLR, 16–18 Nov 2021, pp. 1341–1350.',
 '[36] Y. Nesterov *et al.*, *Lectures on convex optimization*. Springer, 2018, vol. 137.',
]
assert len(refs) == 36
for i, r in enumerate(refs, 1):
    assert r.startswith(f'[{i}] ')
    if i <= 15:
        box = [54, 294 + (i - 1) * 27.0, 299, 294 + i * 27.0]
    else:
        box = [313, 56 + (i - 16) * 30.0, 559, 56 + (i - 15) * 30.0]
    p.text(r, box)

p.write('Compared the 220 dpi renders of all four quadrants with the text. First item continues the last paragraph of page 6 (join_previous: space). Sections VI and VII checked word by word against the TeX and the render ("CNS-2111688" restored across the line break). The complete bibliography [1]-[36] is kept, one entry per item, in printed order (left column [1]-[15], right column [16]-[36]; the extractor had put [15] after [36]); the text was taken from the authors\' .bbl and every entry was compared with the render (authors, titles, venues, volume/number, pages, years). Corrections to the extraction: diacritics restored (Universität München, Açikmeşe, Allgöwer), line-wrap hyphens removed (using, predictions, Methodological, International, Proceedings, reachable, Transactions, helicopter) while real compounds were kept (Data-driven, cross-validation, On-board, under-approximation, Lecchini-Visintini, J.-J.), list bullets and emphasis debris removed, journal/book titles marked in italics as printed. Entries are as printed, including the authors\' bibliography quirks: "p." instead of "pp." in [14], [30], [32]; lower-case "gaussian"/"monte carlo"/"markov chain monte carlo" in [7], [33]; "Neureach" in [13]; "ArXiv, 2020" without an identifier in [10]; "L. E. Ghaoui" in [9] versus "L. El Ghaoui" in [14]; the repeated-author dash in [7]. No page number, running header or footer is printed on this page.')
