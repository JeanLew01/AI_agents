from pt import *
refs = [
 (71, 80, "[29] J. Munkres. *Topology*. Pearson Education, 2014. 4"),
 (83, 128, "[30] V. S. Patsko, S. G. Pyatko, and A. A. Fedotov. Three-dimensional reachability set for a nonlinear control system. *Journal of Computer and Systems Sciences International*, 42(3):320–328, 2003. 6"),
 (130, 176, "[31] E. Plaku, L.E. Kavraki, and M.Y. Vardi. Falsification of LTL Safety Properties in Hybrid Systems. In *International Conference on Tools and Algorithms for the Construction and Analysis of Systems*, 2009. 2"),
 (178, 236, "[32] O. Porges, R. Lampariello, J. Artigas, A. Wedler, C. Borst, and M. A. Roa. Reachability and Dexterity: Analysis and Applications for Space Robotics. In *Workshop on Advanced Space Technologies for Robotics and Automation (ASTRA)*, 2015. 2"),
 (238, 271, "[33] H. Seraji. Reachability Analysis for Base Placement in Mobile Manipulators. *Journal of Field Robotics*, 12(1):29–43, 1995. 2"),
 (274, 306, "[34] P. Tabuada. *Verification and control of hybrid systems: a symbolic approach*. Springer Science & Business Media, 2009. 2"),
 (310, 356, "[35] Y. Wu. Yale ECE598, Lecture Notes: Information-Theoretic Methods in High-Dimensional Statistics, March 2016. URL http://www.stat.yale.edu/~yw562/teaching/598/lec14.pdf. 3, 4"),
 (358, 391, "[36] Z. Xue and R. Dillmann. Efficient Grasp Planning with Reachability Analysis. In *International Conference on Intelligent Robotics and Applications*, 2010. 2"),
]
items = [T("Automatic Control*, 50(7):947–957, 2005. 2", L, 59, 68, join="space")]
items += [T(md, L, y0, y1) for (y0, y1, md) in refs]
notes = ("Compared with the page preview and a 260 dpi crop of the left column; the page holds only the end of the bibliography (rest of the page is blank). All 9 items read against the crop. "
 "First item is the continuation of entry [28] from page 9 (join_previous=space; it closes the italic journal title opened on page 9: 'Transactions on Automatic Control', printed without 'IEEE'). "
 "One entry per item with printed [n] markers and the printed trailing back-reference page numbers. Line-wrap hyphens repaired; compound hyphens at line ends kept: 'Three-dimensional' [30], 'Information-Theoretic' [35]; 'system', 'International', 'Workshop' rejoined. "
 "[33] is printed with a line break after '12(1):'; written '12(1):29–43'. [35]: URL printed across two lines, written as one string with the tilde restored (extractor had a superscript ∼). No page number or running header.")
write(10, items, notes)
