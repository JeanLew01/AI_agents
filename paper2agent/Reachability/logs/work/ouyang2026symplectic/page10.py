from pt import *
LR = (54, 299); RR = (313, 559)
refs = [
 ("[1] V. N. Vapnik, *Statistical Learning Theory*. Wiley, 1998.", LR, 69, 78),
 ("[2] S. Shalev-Shwartz and S. Ben-David, *Understanding Machine Learning: From Theory to Algorithms*. Cambridge University Press, 2014.", LR, 79, 107.5),
 ("[3] C. M. Bishop, *Pattern Recognition and Machine Learning*. Springer, 2006.", LR, 108.5, 127.5),
 ("[4] S. Oymak and N. Ozay, “Non-asymptotic identification of linear dynamical systems from a single trajectory,” *arXiv preprint arXiv:1806.05722*, 2018.", LR, 128.5, 157.5),
 ("[5] Y. Zheng and N. Li, “Non-asymptotic identification of linear dynamical systems using multiple trajectories,” *IEEE Control Systems Letters*, vol. 5, no. 5, pp. 1693–1698, 2021.", LR, 158.5, 187.5),
 ("[6] Y. Hu, A. Wierman, and G. Qu, “On the sample complexity of stabilizing lti systems on a single trajectory,” in *Advances in Neural Information Processing Systems*, vol. 35, 2022, pp. 16 989–17 002.", LR, 188.5, 227.5),
 ("[7] S. W. Werner and B. Peherstorfer, “On the sample complexity of stabilizing linear dynamical systems from data,” *Foundations of Computational Mathematics*, vol. 24, no. 3, pp. 955–987, 2024.", LR, 228.5, 267.5),
 ("[8] L. F. Toso, L. Ye, and J. Anderson, “Learning stabilizing policies via an unstable subspace representation,” in *IEEE Conference on Decision and Control (CDC)*, IEEE, 2025, pp. 7543–7550.", LR, 268, 307.5),
 ("[9] S. Dean, H. Mania, N. Matni, B. Recht, and S. Tu, “On the sample complexity of the linear quadratic regulator,” *Foundations of Computational Mathematics*, vol. 20, no. 4, pp. 633–679, 2020.", LR, 308, 347),
 ("[10] C. De Persis and P. Tesi, “Formulas for data-driven control: Stabilization, optimality, and robustness,” *IEEE Transactions on Automatic Control*, vol. 65, no. 3, pp. 909–924, 2020.", LR, 348, 377),
 ("[11] J. Coulson, J. Lygeros, and F. Dörfler, “Data-enabled predictive control: In the shallows of the deepc,” in *European Control Conference (ECC)*, IEEE, 2019, pp. 307–312.", LR, 377.5, 407),
 ("[12] J. Berberich, J. Köhler, M. A. Müller, and F. Allgöwer, “Data-driven model predictive control with stability and robustness guarantees,” *IEEE Transactions on Automatic Control*, vol. 66, no. 4, pp. 1702–1717, 2021.", LR, 407.5, 447),
 ("[13] T. Dai and M. Sznaier, “A semi-algebraic optimization approach to data-driven control of continuous-time nonlinear systems,” *IEEE Control Systems Letters*, vol. 5, no. 2, pp. 487–492, 2020.", LR, 447.5, 486.5),
 ("[14] M. Guo, C. De Persis, and P. Tesi, “Data-driven stabilization of nonlinear polynomial systems with noisy data,” *IEEE Transactions on Automatic Control*, vol. 67, no. 8, pp. 4210–4217, 2021.", LR, 487, 526.5),
 ("[15] R. Strässer, J. Berberich, and F. Allgöwer, “Data-driven control of nonlinear systems: Beyond polynomial dynamics,” in *IEEE Conference on Decision and Control (CDC)*, IEEE, 2021, pp. 4344–4351.", LR, 527, 566.5),
 ("[16] N. Monshizadeh, C. De Persis, and P. Tesi, “A versatile framework for data-driven control of nonlinear systems,” *IEEE Transactions on Automatic Control*, 2025, to appear.", LR, 567, 596.5),
 ("[17] N. M. Boffi, S. Tu, N. Matni, J.-J. Slotine, and V. Sindhwani, “Learning stability certificates from data,” *arXiv preprint arXiv:2008.05952*, 2020.", LR, 597, 626),
 ("[18] R. Siegelmann and E. Mallada, “Data-driven practical stabilization of nonlinear systems via chain policies: Sample complexity and incremental learning,” *arXiv preprint arXiv:2510.03982*, 2025.", LR, 626.5, 666),
 ("[19] T. Lew, L. Janson, R. Bonalli, and M. Pavone, “A simple and efficient sampling-based algorithm for general reachability analysis,” in *Learning for Dynamics and Control Conference*, PMLR, 2022, pp. 1086–1099.", LR, 666.5, 706),
 ("[20] R. Siegelmann, Y. Shen, F. Paganini, and E. Mallada, “A recurrence-based direct method for stability analysis and gpu-based verification of non-monotonic lyapunov functions,” in *2023 62nd IEEE Conference on Decision and Control (CDC)*, IEEE, 2023, pp. 6665–6672.", LR, 706.5, 726),
 ("[21] H. Sibai and E. Mallada, “Recurrence of nonlinear control systems: Entropy, bit rates, and finite alphabet controllers,” *Nonlinear Analysis: Hybrid Systems*, vol. 59, p. 101 649, 2026.", RR, 85.5, 124.5),
 ("[22] J. Liu and E. Mallada, “Recurrent control barrier functions: A path towards nonparametric safety verification,” in *2025 IEEE 64th Conference on Decision and Control (CDC)*, IEEE, 2025, pp. 7721–7727.", RR, 125.5, 164.5),
 ("[23] J. Liu and E. Mallada, “Safety-critical control via recurrent tracking functions,” *arXiv preprint arXiv:2510.01147*, 2025.", RR, 165, 184.5),
 ("[24] M. Viana and K. Oliveira, *Foundations of ergodic theory*. Cambridge University Press, 2016.", RR, 185, 204.5),
 ("[25] J. F. Plante, “Anosov flows,” *American Journal of Mathematics*, vol. 94, no. 3, pp. 729–754, 1972.", RR, 205, 224.5),
 ("[26] E. Hopf, “Ergodic theory and the geodesic flow on surfaces of constant negative curvature,” 1971.", RR, 225, 244.5),
 ("[27] R. Bowen and D. Ruelle, “The ergodic theory of axiom a flows,” in *The theory of chaotic attractors*, Springer, 1975, pp. 55–76.", RR, 245, 274.5),
 ("[28] J. G. Romero, “A robust adaptive velocity observer for mechanical systems transformed in cascade form,” *Automatica*, vol. 165, p. 111 671, 2024.", RR, 275, 304.5),
 ("[29] T. T. Zhang, D. Pfrommer, C. Pan, N. Matni, and M. Simchowitz, “Action chunking and data augmentation yield exponential improvements in behavior cloning for continuous spaces,” in *International Conference on Learning Representations (ICLR)*, 2026.", RR, 305, 354),
]
items = [H("## References", (148, 205), 55, 65)] + [T(*r) for r in refs]
notes = """
Compared with 230 dpi crops of both columns of PDF page 10; all 29 reference entries were read one by one against the crops and against the text-layer lines (the bibliography is produced by biblatex from reference.bib;
no .bbl is in the source bundle, so the PDF is the only authority for the printed form). 'REFERENCES' (small caps, unnumbered) is a level-2 heading 'References'.
One text item per entry, starting with the printed number in brackets; the extractor's list dashes were removed. Italic titles and venue names are kept in italics; quotation marks are the printed curly quotes; page ranges use the printed en dash.
Reading order repaired: the extractor placed the right-column entries [21]-[29] between [11] and [12] and had merged entry [11] into the item of [10]; entry [20] starts at the bottom of the left column
('... stability analysis and') and continues at the top of the right column ('gpu-based verification ...'); merged into one item.
Diacritics restored from the split accents of the text layer ('D¨orfler', 'K¨ohler', 'M¨uller', 'Allg¨ower', 'Str¨asser') to Dörfler, Köhler, Müller, Allgöwer, Strässer as printed.
Line-wrap hyphens removed (Ma-chine, com-plexity, pre-dictive, sta-bilization, Sam-ple, func-tions, Mathe-matics, me-chanical, continu-ous, Rep-resentations); the page range of [14] broken after the en dash ('4210–' / '4217') is closed up;
real compounds kept (Shalev-Shwartz, Ben-David, Non-asymptotic, data-driven, Data-enabled, semi-algebraic, continuous-time, sampling-based, recurrence-based, gpu-based, non-monotonic, Safety-critical, J.-J.).
Kept as printed: lower-case words produced by the bibliography style ('lti systems' in [6], 'deepc' in [11], 'gpu-based ... lyapunov functions' in [20], 'axiom a flows' and 'The theory of chaotic attractors' in [27],
'Foundations of ergodic theory' in [24]); article numbers and page numbers printed with a thin space as thousands separator are written with an ordinary space ('pp. 16 989–17 002' in [6], 'p. 101 649' in [21], 'p. 111 671' in [28]);
entry [26] has no venue ('... of constant negative curvature,” 1971.'); entry [16] ends with '2025, to appear.'. arXiv identifiers checked digit by digit: 1806.05722, 2008.05952, 2510.03982, 2510.01147.
The lower part of the right column is blank. No page number, running header, figure or table on this page.
"""
write(10, items, notes)
