from pagelib import *

items = [
    header(13),
    text("p0013-b001", [90.0, 94.0, 523.0, 131.0],
         "Ian Mitchell, Alex Bayen, and Claire J. Tomlin. A time-dependent Hamilton-Jacobi formulation of reachable sets for continuous dynamic games. *IEEE Transactions on Automatic Control (TAC)*, 50(7):947–957, 2005."),
    text("p0013-b002", [90.0, 143.0, 523.0, 168.0],
         "KN Niarchos and John Lygeros. A neural approximation to continuous time reachability computations. In *Conference on Decision and Control*, pages 6313–6318, 2006."),
    text("p0013-b003", [90.0, 180.0, 523.0, 204.0],
         "Petter Nilsson and Necmiye Ozay. Synthesis of separable controlled invariant sets for modular local control design. In *American Control Conference*, pages 5656–5663, 2016."),
    text("p0013-b004", [90.0, 216.0, 523.0, 253.0],
         "Derek Onken, Levon Nurbekyan, Xingjian Li, Samy Wu Fung, Stanley Osher, and Lars Ruthotto. A neural network approach for high-dimensional optimal control applied to multiagent path finding. *IEEE Transactions on Control Systems Technology*, 2022."),
    text("p0013-b005", [90.0, 265.0, 523.0, 303.0],
         "Vicenç Rubies-Royo, David Fridovich-Keil, Sylvia Herbert, and Claire J Tomlin. A classification-based approach for approximate reachability. In *International Conference on Robotics and Automation*, pages 7697–7704. IEEE, 2019."),
    text("p0013-b006", [90.0, 315.0, 523.0, 378.0],
         "Vladimir Vovk. Conditional validity of inductive conformal predictors. In Steven C. H. Hoi and Wray Buntine, editors, *Proceedings of the Asian Conference on Machine Learning*, volume 25 of *Proceedings of Machine Learning Research*, pages 475–490, Singapore Management University, Singapore, 04–06 Nov 2012. PMLR. URL https://proceedings.mlr.press/v25/vovk12.html."),
    pageno(13, "p0013-b007", [301.0, 726.0, 311.0, 733.0]),
]

save(13, items, """
Compared the whole page with the 130 dpi render and with root.bbl. Last 6 bibliography entries (Mitchell et al. to Vovk),
one text item each, extractor list bullets removed; the rest of the page is blank. Every entry was read on the page image
against the .bbl; authors, titles, venues, volume(issue):pages and years agree. Split diacritic repaired ('Vicenc¸' ->
'Vicenç'). Line-wrap hyphens removed (computa-tions, Au-tomation); real hyphens restored or kept ('classification-based'
is broken at the line end after 'classification-' and the extractor had 'classificationbased'; time-dependent,
Hamilton-Jacobi, high-dimensional, Rubies-Royo, Fridovich-Keil). The URL of the Vovk entry is broken across two lines in
the PDF ('https://proceedings.mlr.press/v25/' / 'vovk12.html') and is written in one piece. The bibliography has 31
entries in total (11 + 14 + 6), the same number as the authors' .bbl. This page contains no mathematics. Omitted: running
header and page number.
""")
