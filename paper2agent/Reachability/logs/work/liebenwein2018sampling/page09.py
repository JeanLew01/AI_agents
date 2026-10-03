from pt import *
refsL = [
 (83, 128, "[1] A. Alam, A. Gattami, K. H. Johansson, and C. J. Tomlin. Guaranteeing safety for heavy duty vehicle platooning: Safe set computations and experimental evaluations. *Control Engineering Practice*, 24:33–41, 2014. 2"),
 (130, 164, "[2] M. Althoff. An introduction to CORA 2015. In *Workshop on Applied Verification for Continuous and Hybrid Systems*, 2015. 2"),
 (166, 210, "[3] M. Althoff and J. M. Dolan. Online Verification of Automated Road Vehicles Using Reachability Analysis. *IEEE Transactions on Robotics*, 30(4):903–918, 2014. 1, 2"),
 (214, 260, "[4] R. Alur, C. Courcoubetis, N. Halbwachs, T.A. Henzinger, P.-H. Ho, X. Nicollin, A. Olivero, J. Sifakis, and S. Yovine. The Algorithmic Analysis of Hybrid Systems. *Theoretical Computer Science*, 138(1):3–34, 1995. 2"),
 (262, 307, "[5] R. Alur, T. Dang, and F. Ivančić. Predicate Abstraction for Reachability Analysis of Hybrid Systems. *ACM Transactions on Embedded Computing Systems (TECS)*, 5(1):152–199, 2006. 2"),
 (310, 355, "[6] A. Bhatia and E. Frazzoli. Incremental Search Methods for Reachability Analysis of Continuous and Hybrid Systems. In *International Workshop on Hybrid Systems: Computation and Control*, 2004. 2"),
 (358, 403, "[7] D. Bresolin, L. Geretti, R. Muradore, P. Fiorini, and T. Villa. Verification of Robotic Surgery Tasks by Reachability Analysis: A Comparison of Tools. In *Euromicro Conference on Digital System Design*, 2014. 2"),
 (405, 451, "[8] M. Chen and C. J. Tomlin. Exact and efficient hamilton-jacobi reachability for decoupled systems. In *Decision and Control (CDC), 2015 IEEE 54th Annual Conference on*, pages 1297–1303. IEEE, 2015. 2"),
 (451, 497, "[9] X. Chen, E. Ábrahám, and S. Sankaranarayanan. Flow*: An Analyzer for Non-Linear Hybrid Systems. In *International Conference on Computer Aided Verification*, 2013. 2"),
 (499, 547, "[10] X. Chen, S. Schupp, I.B. Makhlouf, E. Ábrahám, G. Frehse, and S. Kowalewski. A Benchmark Suite for Hybrid Systems Reachability Analysis. In *NASA Formal Methods Symposium*, 2015. 2"),
 (549, 594, "[11] P. Cheng and V. Kumar. Sampling-based Falsification and Verification of Controllers for Continuous Dynamic Systems. *The International Journal of Robotics Research*, 27(11-12):1232–1245, 2008. 2"),
 (597, 642, "[12] A. Chutinan and B.H. Krogh. Verification of Polyhedral-Invariant Hybrid Automata Using Polygonal Flow Pipe Approximations. In *International workshop on hybrid systems: computation and control*, 1999. 2"),
 (644, 690, "[13] E. Clarke, O. Grumberg, and D. Long. Verification Tools for Finite-State Concurrent Systems. In *Workshop/School/Symposium of the REX Project (Research and Education in Concurrent Systems)*, 1993. 2"),
 (692, 726, "[14] E. Clarke, O. Grumberg, S. Jha, Y. Lu, and H. Veith. Counterexample-Guided Abstraction Refinement. In *International Conference on Computer Aided Verification*, 2000. 2"),
]
refsR = [
 (71, 104, "[15] P.J. Davis. Leonhard Euler’s Integral: A Historical Profile of the Gamma Function. *The American Mathematical Monthly*, 66(10):849–869, 1959. 4"),
 (106, 152, "[16] L. E. Dubins. On Curves of Minimal Length with a Constraint on Average Curvature, and with Prescribed Initial and Terminal Positions and Tangents. *American Journal of Mathematics*, 79(3):497–516, 1957. 6"),
 (154, 210, "[17] K. Edelberg, D. Wai, J. Reid, E. Kulczycki, and P. Backes. Workspace and Reachability Analysis of a Robotic Arm for Sample Cache Retrieval from a Mars Rover. In *AIAA SPACE Conference and Exposition*, 2015. 2"),
 (214, 260, "[18] S. M. Erlien, S. Fujita, and J. C. Gerdes. Shared steering control using safe envelopes for obstacle avoidance and vehicle stability. *IEEE Transactions on Intelligent Transportation Systems*, 17(2):441–451, 2016. 2"),
 (262, 283, "[19] H. Federer. *Geometric Measure Theory*. Springer, 1969. 4, 5"),
 (286, 344, "[20] J. F. Fisac, M. Chen, C. J. Tomlin, and S. S. Sastry. Reach-avoid problems with time-varying dynamics, targets and constraints. In *Proceedings of the 18th international conference on hybrid systems: computation and control*, pages 11–20. ACM, 2015. 2"),
 (346, 379, "[21] R. Geraerts and M.H. Overmars. Reachability Analysis of Sampling Based Planners. In *Robotics and Automation (ICRA)*, 2005. 2"),
 (381, 427, "[22] J.H. Gillula, G.M. Hoffmann, H. Huang, M.P. Vitus, and C.J. Tomlin. Applications of Hybrid Reachability Analysis to Robotic Aerial Vehicles. *The International Journal of Robotics Research*, 30(3):335–354, 2011. 2"),
 (429, 475, "[23] T.A. Henzinger, P.-H. Ho, and H. Wong-Toi. HyTech: A Model Checker for Hybrid Systems. *International Journal on Software Tools for Technology Transfer*, 1(1-2):110–122, 1997. 2"),
 (477, 523, "[24] F. Immler. Verified Reachability Analysis of Continuous Systems. In *International Conference on Tools and Algorithms for the Construction and Analysis of Systems (TACAS)*, 2015. 2"),
 (525, 582, "[25] J. Kapinski, J.V. Deshmukh, S. Sankaranarayanan, and N. Arechiga. Simulation-guided Lyapunov Analysis for Hybrid Dynamical Systems. In *Proceedings of the International Conference on Hybrid Systems: Computation and Control*, 2014. 2"),
 (585, 628, "[26] L. Liebenwein, W. Schwarting, C.-I. Vasile, J. DeCastro, J. Alonso-Mora, S. Karaman, and D. Rus. Compositional and contract-based verification for autonomous driving on road networks. 2017. 2"),
 (632, 690, "[27] S.B. Liu, H. Roehm, C. Heinzemann, I. Lütkebohle, J. Oehlerking, and M. Althoff. Provably Safe Motion of Mobile Robots in Human Environments. In *IEEE/RSJ International Conference on Intelligent Robots and Systems*, 2017. 2"),
 (692, 726, "[28] I. M. Mitchell, A. M. Bayen, and C. J. Tomlin. A Time-Dependent Hamilton-Jacobi Formulation of Reachable Sets for Continuous Dynamic Games. *Transactions on"),
]
items = [H("## References", (146, 203), 59, 67)]
items += [T(md, L, y0, y1) for (y0, y1, md) in refsL]
items += [T(md, R, y0, y1) for (y0, y1, md) in refsR]
notes = ("Compared with a 200 dpi render and 260 dpi crops of both columns; every one of the 28 entries on this page was read against the crop (authors, title, venue, volume/pages, year, trailing back-reference page numbers). "
 "'REFERENCES' was extracted as plain text (flagged as a possible header/footer by the extractor; it is the real section heading) and is now a level-2 heading; the fragment '2000. 2' that the extractor turned into a heading is the end of entry [14], which runs from the bottom of the left column to the top of the right column, and was merged into [14]. "
 "One entry per item, printed [n] markers kept, list bullets removed. Each entry ends with the printed back-reference(s) to the page(s) of this paper on which it is cited (e.g. '2014. 2', '1969. 4, 5'); these are part of the printed bibliography and are kept. "
 "Diacritics restored from the crop: Ivančić [5], Ábrahám [9], [10], Lütkebohle [27]. Line-wrap hyphens repaired; compound hyphens kept where the hyphen falls at a line end: 'hamilton-jacobi' [8], 'Polyhedral-Invariant' [12], 'Time-Dependent' [28]; 'Workshop/School/Symposium' [13] and 'International' rejoined. "
 "[23] is printed with a line break between the volume '1' and '(1-2)'; written '1(1-2):110–122' like the other volume(issue) entries. [28] continues on page 10 ('Automatic Control, 50(7):947–957, 2005. 2'); its italic journal title is therefore closed in the page-10 item. Journal/venue names kept in italics as printed. No page number or running header.")
write(9, items, notes)
