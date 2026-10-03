from pagelib import *

refs = [
"[20] J. B. Lasserre and E. Pauwels, *The empirical Christoffel function with applications in data analysis*, Advances in Computational Mathematics, 45 (2019), pp. 1439–1468.",
"[21] G. R. Marseglia, J. Scott, L. Magni, R. D. Braatz, and D. M. Raimondo, *A hybrid stochastic-deterministic approach for active fault diagnosis using scenario optimization*, IFAC Proceedings Volumes, 47 (2014), pp. 1102–1107.",
"[22] D. A. McAllester, *Some PAC-Bayesian theorems*, Machine Learning, 37 (1999), pp. 355–363.",
"[23] I. M. Mitchell, J. Budzis, and A. Bolyachevets, *Invariant, viability and discriminating kernel under-approximation via zonotope scaling*, in Proceedings of the 22nd ACM International Conference on Hybrid Systems: Computation and Control, 2019, pp. 268–269.",
"[24] P. Nevai, *Géza Freud, orthogonal polynomials and Christoffel functions. a case study*, Journal of approximation theory, 48 (1986), pp. 3–167.",
"[25] E. Pauwels and J.-B. Lasserre, *Sorting out typicality with the inverse moment matrix SOS polynomial*, Advances in Neural Information Processing Systems, 29 (2016), pp. 190–198.",
"[26] E. Pauwels, M. Putinar, and J.-B. Lasserre, *Data analysis from empirical moments and the Christoffel function*, Foundations of Computational Mathematics, 21 (2021), pp. 243–273.",
"[27] B. Qi, C. Fan, M. Jiang, and S. Mitra, *DryVR 2.0: a tool for verification and controller synthesis of black-box cyber-physical systems*, in Proceedings of the 21st International Conference on Hybrid Systems: Computation and Control (part of CPS Week), 2018, pp. 269–270.",
"[28] H. Sartipizadeh, A. P. Vinod, B. Açikmeşe, and M. Oishi, *Voronoi partition-based scenario reduction for fast sampling-based stochastic reachability computation of linear systems*, in 2019 American Control Conference (ACC), IEEE, 2019, pp. 37–44.",
"[29] M. Seeger, *PAC-Bayesian generalisation error bounds for Gaussian process classification*, Journal of Machine Learning Research, 3 (2002), pp. 233–269.",
"[30] C. F. Van Loan and G. Golub, *Matrix computations*, The Johns Hopkins University Press, 1996.",
"[31] M. Vidyasagar, *Learning and Generalisation: With Applications to Neural Networks*, Springer Science & Business Media, 2002.",
"[32] C. Williams and M. Seeger, *Using the Nyström method to speed up kernel machines*, in Proceedings of the 14th Annual Conference on Neural Information Processing Systems, 2001, pp. 682–688.",
"[33] Y. Xu, *Christoffel functions and Fourier series for multivariate orthogonal polynomials*, Journal of Approximation Theory, 82 (1995), pp. 205–239.",
"[34] Y. Yang, J. Zhang, K.-Q. Cai, and M. Prandini, *Multi-aircraft conflict detection and resolution based on probabilistic reach sets*, IEEE Transactions on Control Systems Technology, 25 (2016), pp. 309–316.",
]

items = [
    running_header(18),
    text("p0018-refs", [74.0, 100.0, 442.0, 440.0], "\n\n".join(refs)),
    heading("p0018-b013", [89.0, 481.0, 369.0, 491.0], "## Appendix A. Background on Gaussian Process Models"),
    text("p0018-b014", [71.0, 493.0, 442.0, 564.0],
         r"A Gaussian process $g$ is a stochastic process such that vectors $(g(x_1),\dotsc,g(x_m))$ of point evaluations are multivariate Gaussian distributions. Similar to how a Gaussian random variable is completely characterized by its mean and variance, a Gaussian process is completely characterized by a mean function $m$, defined pointwise as $m(x)=\mathbb{E}\left[g(x)\right]$, and a positive semidefinite covariance function $k$, defined on all pairs of points $x,y\in\mathcal{X}$ as $k(x,y)=\mathbb{E}\left[g(x)g(y)\right]$."),
    text("p0018-b015", [71.0, 565.0, 442.0, 636.0],
         r"Gaussian processes can also be defined according to a finite set of basis functions, admitting a direct construction as a finite weighted sum. For an $m$-dimensional space of functions with basis $b_1,\dotsc,b_m:\mathcal{X}\to\mathbb{R}$, we form the stochastic weighted average $\sum_{i=1}^m w_i b_i$, where $w=(w_{1},\dotsc,w_{m})\sim\mathcal{N}\left(0,\Sigma\right)$. This weighted average is a Gaussian process whose support is the span of $b_{1},\dotsc,b_{m}$, with mean $m(x)=0$ and covariance $k(x,y)=\sum_{i=1}^m b(x)^\top \Sigma b(y)$, where $b(\cdot) = (b_1(\cdot),\dotsc,b_m(\cdot))^\top$."),
    text("p0018-b016", [71.0, 637.0, 442.0, 695.0],
         r"The Gaussian process regression model is Bayesian regression model that uses a Gaussian process as the prior over regression functions. In our case, we take the mean of the prior process to be zero. The data is assumed to be of the form $g(x_i)=h_i+\varepsilon$, where $\varepsilon$ is a Gaussian noise term with variance $\sigma^2$. Under these conditions, the posterior for the unknown function is also a Gaussian process, whose mean and"),
]

save(18, items, r"""
Compared with the 130-dpi render. Bibliography entries [20]-[34] taken from the authors' .bbl file and each compared with the page (numbers, authors, titles, venues, volume/year/pages agree); the extractor had merged [22]-[24] and [25]-[27] into two blocks and written the accented names as 'Ac¸ikmes¸e' and 'Nystr¨om': restored as 'Açikmeşe' ([28], printed with c-cedilla and s-cedilla), 'Nyström' ([32]) and 'Géza' ([24]). Printed peculiarities kept: [24] 'functions. a case study' with lower-case 'a' and 'Journal of approximation theory' in lower case. One entry per paragraph in a single text item; small-capital author names written in normal case; titles italic. The extractor's heading '# 18' (the page number) is part of the omitted running header. 'Appendix A. Background on Gaussian Process Models.' (bold) written as ## heading. Appendix text and inline math from the authors' TeX with macros expanded (\Ex, \dom, \Norm, \sumio{m} -> \sum_{i=1}^m, \liston[m]{w} -> w_1,\dotsc,w_m) and compared with the page. Source peculiarities kept as printed: the covariance of the finite-basis process is printed with a summation sign, $k(x,y)=\sum_{i=1}^m b(x)^\top\Sigma b(y)$; 'is Bayesian regression model' (missing article); the data model is written $g(x_i)=h_i+\varepsilon$; $m$ denotes both the mean function and the number of basis functions/points. Line-wrap hyphens removed (resolu-tion, Inter-national, Con-ference, Jour-nal). The last item ends in the middle of a sentence ('whose mean and') that continues on page 19 (join there). Omitted: running header (page number 18 and author short list).
""")
