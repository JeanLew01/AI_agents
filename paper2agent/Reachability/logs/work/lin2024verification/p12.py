from pagelib import *

items = [
    header(12),
    text("p0012-b001", [89.0, 94.0, 523.0, 145.0],
         "DLMF. *NIST Digital Library of Mathematical Functions*. https://dlmf.nist.gov/, Release 1.1.11 of 2023-09-15, 2023. URL https://dlmf.nist.gov/. F. W. J. Olver, A. B. Olde Daalhuis, D. W. Lozier, B. I. Schneider, R. F. Boisvert, C. W. Clark, B. R. Miller, B. V. Saunders, H. S. Cohl, and M. A. McClain, eds."),
    text("p0012-b002", [90.0, 156.0, 523.0, 180.0],
         "Tommaso Dreossi, Thao Dang, and Carla Piazza. Parallelotope bundles for polynomial reachability. In *International Conference on Hybrid Systems: Computation and Control*, 2016."),
    text("p0012-b003", [90.0, 191.0, 523.0, 228.0],
         "Jaime F. Fisac, Neil F. Lugovoy, Vicenç Rubies-Royo, Shromona Ghosh, and Claire J. Tomlin. Bridging Hamilton-Jacobi Safety Analysis and Reinforcement Learning. *International Conference on Robotics and Automation*, 2019."),
    text("p0012-b004", [90.0, 239.0, 523.0, 277.0],
         "G. Frehse, C. Le Guernic, A. Donzé, S. Cotton, R. Ray, O. Lebeltel, R. Ripado, A. Girard, T. Dang, and O. Maler. SpaceEx: Scalable verification of hybrid systems. In *International Conference Computer Aided Verification*, 2011."),
    text("p0012-b005", [90.0, 287.0, 523.0, 312.0],
         "Antoine Girard. Reachability of uncertain linear systems using zonotopes. In *International Workshop on Hybrid Systems: Computation and Control*, pages 291–305, 2005."),
    text("p0012-b006", [90.0, 322.0, 523.0, 360.0],
         "Mark R. Greenstreet and Ian Mitchell. Integrating projections. In Thomas A. Henzinger and Shankar Sastry, editors, *Hybrid Systems: Computation and Control*, pages 159–174, Berlin, Heidelberg, 1998. Springer Berlin Heidelberg. ISBN 978-3-540-69754-1."),
    text("p0012-b007", [90.0, 370.0, 523.0, 395.0],
         "D. Henrion and M. Korda. Convex computation of the region of attraction of polynomial control systems. *IEEE Transactions on Automatic Control*, 59(2):297–312, 2014."),
    text("p0012-b008", [89.0, 405.0, 523.0, 442.0],
         "Alexander Kurzhanski and Pravin Varaiya. On ellipsoidal techniques for reachability analysis. part ii: Internal approximations box-valued constraints. *Optimization Methods and Software*, 17:207–237, 01 2002. doi: 10.1080/1055678021000012435."),
    text("p0012-b009", [90.0, 453.0, 523.0, 478.0],
         "Alexander B Kurzhanski and Pravin Varaiya. Ellipsoidal techniques for reachability analysis: internal approximation. *Systems & Control Letters*, 2000."),
    text("p0012-b010", [90.0, 488.0, 523.0, 525.0],
         "Albert Lin and Somil Bansal. Generating formal safety assurances for high-dimensional reachability. In *2023 IEEE International Conference on Robotics and Automation (ICRA)*, pages 10525–10531. IEEE, 2023."),
    text("p0012-b011", [90.0, 536.0, 522.0, 559.0],
         "John Lygeros. On reachability and minimum cost optimal control. *Automatica*, 40(6):917–927, 2004."),
    text("p0012-b012", [90.0, 571.0, 523.0, 608.0],
         "John N Maidens, Shahab Kaynama, Ian M Mitchell, Meeko MK Oishi, and Guy A Dumont. Lagrangian methods for approximating the viability kernel in high-dimensional systems. *Automatica*, 2013."),
    text("p0012-b013", [90.0, 619.0, 523.0, 644.0],
         "A. Majumdar and R. Tedrake. Funnel libraries for real-time robust feedback motion planning. *The International Journal of Robotics Research*, 36(8):947–982, 2017."),
    text("p0012-b014", [90.0, 654.0, 523.0, 705.0],
         "Anirudha Majumdar, Ram Vasudevan, Mark M. Tobenkin, and Russ Tedrake. Convex optimization of nonlinear feedback controllers via occupation measures. *The International Journal of Robotics Research*, 33(9):1209–1230, 2014. doi: 10.1177/0278364914528059. URL https://doi.org/10.1177/0278364914528059."),
    pageno(12, "p0012-b015", [301.0, 726.0, 311.0, 733.0]),
]

save(12, items, """
Compared the whole page with the 130 dpi render and with root.bbl. Bibliography continued: 14 entries (DLMF to Majumdar et
al. 2014), one text item each, extractor list bullets removed. Every entry was read on the page image against the .bbl:
authors, titles, venues, volume(issue):pages, years, ISBN and DOIs agree. Split diacritics repaired ('Vicenc¸' ->
'Vicenç', 'Donz´e' -> 'Donzé'). Page ranges broken across lines closed up ('17:207–' / '237', '10525–' / '10531'); the
URL of the last entry is broken across two lines in the PDF ('https://doi.' / 'org/10.1177/0278364914528059') and is
written in one piece. Line-wrap hyphens removed (Re-lease, Confer-ence, Work-shop, inter-nal, reachabil-ity, La-grangian,
Automat-ica); real hyphens kept (Rubies-Royo, Hamilton-Jacobi, box-valued, high-dimensional, real-time, ISBN
978-3-540-69754-1, date 2023-09-15). Kept as printed: the DLMF entry gives the address https://dlmf.nist.gov/ twice and
ends with the editor list '..., eds.'; 'part ii: Internal approximations box-valued constraints'; '17:207–237, 01 2002';
'International Conference Computer Aided Verification'. This page contains no mathematics. Omitted: running header and
page number.
""")
