#!/usr/bin/env python3
"""Reviewed items for PDF pages 11-14 (bibliography) of dietrich2024nonconvex."""
from pagelib import T, H, O, write_pages, RUNHEAD, PAGENO

PAGES, NOTES = {}, {}

COMMON = ("The bibliography is unnumbered (author-year style); each entry is one text item, the extractor's list "
          "bullets ('- ') were removed because the print has none, and journal / book titles are italic as printed. "
          "URLs are printed in typewriter type and broken across lines; they are joined without spaces. ")

# ----------------------------------------------------------------------------- page 11
NOTES[11] = COMMON + r"""
Page 11: all 10 entries (Alanwar ... Campi and Garatti) read against the 170 dpi render, word by word. Running
header and page number 11 omitted; 'References' set to level 2. Corrections of extraction damage: split
diacritics restored ('Allgöwer', 'Universität München'); line-wrap hyphens removed ('reachability' three times,
'inclusions', 'Heidelberg', 'implementation', 'Berkeley'); broken URLs closed up
('.../v144/alanwar21a.html', 'https://www.sciencedirect.com/...', 'https://doi.org/10.1146/annurev-control-...',
'https://doi.org/10.1007/978-3-319-95246-8_4', '.../TechRpts/2012/EECS-2012-241.html',
'https://doi.org/10.1007/s10107-016-1056-9'); the extractor's strikethrough artefact in 'doi:
10.1007/978-3-319-95246-8_4' removed (the print has an underscore before the 4); 'volume(issue):pages' strings
broken across lines closed up ('4(2):233–249', '167(1):155–189'). Kept as printed: '07 – 08 June 2021' with
spaced dash, 'Hamilton-jacobi' in lower case, 'jan 2018', 'doi: https://doi.org/10.1016/...' (a URL after
'doi:').
"""
PAGES[11] = [
    O("p0011-b000", RUNHEAD),
    H("p0011-b001", "## References"),
    T("p0011-b002",
      "Amr Alanwar, Anne Koch, Frank Allgöwer, and Karl Henrik Johansson. Data-driven reachability analysis using "
      "matrix zonotopes. In *Proceedings of the 3rd Conference on Learning for Dynamics and Control*, volume 144 of "
      "*Proceedings of Machine Learning Research*, pages 163–175. PMLR, 07 – 08 June 2021. URL "
      "https://proceedings.mlr.press/v144/alanwar21a.html."),
    T("p0011-b003",
      "Matthias Althoff. *Reachability analysis and its application to the safety assessment of autonomous cars*. PhD "
      "thesis, Technische Universität München, 2010."),
    T("p0011-b004",
      "Matthias Althoff and Goran Frehse. Combining zonotopes and support functions for efficient reachability "
      "analysis of linear systems. In *2016 IEEE 55th Conference on Decision and Control (CDC)*, pages 7439–7446, "
      "2016. doi: 10.1109/CDC.2016.7799418."),
    T("p0011-b005",
      "Matthias Althoff, Olaf Stursberg, and Martin Buss. Computing reachable sets of hybrid systems using a "
      "combination of zonotopes and polytopes. *Nonlinear Analysis: Hybrid Systems*, 4(2):233–249, 2010. ISSN "
      "1751-570X. doi: https://doi.org/10.1016/j.nahs.2009.03.009. URL "
      "https://www.sciencedirect.com/science/article/pii/S1751570X09000442. IFAC World Congress 2008."),
    T("p0011-b006",
      "Matthias Althoff, Goran Frehse, and Antoine Girard. Set propagation techniques for reachability analysis. "
      "*Annual Review of Control, Robotics, and Autonomous Systems*, 4(1):369–395, 2021. doi: "
      "10.1146/annurev-control-071420-081941. URL https://doi.org/10.1146/annurev-control-071420-081941."),
    T("p0011-b007",
      "Murat Arcak and John Maidens. *Simulation-Based Reachability Analysis for Nonlinear Systems Using "
      "Componentwise Contraction Properties*, pages 61–76. Springer International Publishing, Cham, 2018. ISBN "
      "978-3-319-95246-8. doi: 10.1007/978-3-319-95246-8_4. URL https://doi.org/10.1007/978-3-319-95246-8_4."),
    T("p0011-b008",
      "Somil Bansal, Mo Chen, Sylvia Herbert, and Claire J. Tomlin. Hamilton-jacobi reachability: A brief overview and "
      "recent advances. In *2017 IEEE 56th Annual Conference on Decision and Control (CDC)*, pages 2242–2253, 2017. "
      "doi: 10.1109/CDC.2017.8263977."),
    T("p0011-b009",
      "Oleg Botchkarev and Stavros Tripakis. Verification of hybrid systems with linear differential inclusions using "
      "ellipsoidal approximations. In Nancy Lynch and Bruce H. Krogh, editors, *Hybrid Systems: Computation and "
      "Control*, pages 73–88, Berlin, Heidelberg, 2000. Springer Berlin Heidelberg."),
    T("p0011-b010",
      "Patrick Bouffard. On-board model predictive control of a quadrotor helicopter: Design, implementation, and "
      "experiments. Master’s thesis, EECS Department, University of California, Berkeley, Dec 2012. URL "
      "http://www2.eecs.berkeley.edu/Pubs/TechRpts/2012/EECS-2012-241.html."),
    T("p0011-b011",
      "M. C. Campi and S. Garatti. Wait-and-judge scenario optimization. *Math. Program.*, 167(1):155–189, jan 2018. "
      "ISSN 0025-5610. doi: 10.1007/s10107-016-1056-9. URL https://doi.org/10.1007/s10107-016-1056-9."),
    O("p0011-b012", PAGENO),
]

# ----------------------------------------------------------------------------- page 12
NOTES[12] = COMMON + r"""
Page 12: all 12 entries (Campi, Garatti and Ramponi ... Girard) read against the 170 dpi render, word by word.
Running header and page number 12 omitted. Corrections of extraction damage: split diacritics restored ('Donzé',
'Kunčak'); line-wrap hyphens removed ('theory', 'models', 'Publishing', 'Programming'); broken URLs closed up
('http://www2.eecs.berkeley.edu/Pubs/TechRpts/2023/EECS-2023-207.html',
'https://doi.org/10.1007/s10107-024-02074-3'). Kept as printed: 'Hamilton–jacobi' with en dash and lower-case j,
'Ron S Dembo' without period, 'adaptive gaussian process classification and monte carlo methods', '2020a' /
'2020b' year suffixes, 'christoffel functions', 'page 5067–5072' and 'page 174–189' (singular 'page'),
'HSCC’07', 'Dryvr'.
"""
PAGES[12] = [
    O("p0012-b000", RUNHEAD),
    T("p0012-b001",
      "Marco Claudio Campi, Simone Garatti, and Federico Alessandro Ramponi. A general scenario theory for nonconvex "
      "optimization and decision making. *IEEE Transactions on Automatic Control*, 63(12):4067–4078, 2018. doi: "
      "10.1109/TAC.2018.2808446."),
    T("p0012-b002",
      "Mo Chen and Claire J. Tomlin. Hamilton–jacobi reachability: Some recent theoretical advances and applications "
      "in unmanned airspace management. *Annual Review of Control, Robotics, and Autonomous Systems*, 1(1):333–358, "
      "2018. doi: 10.1146/annurev-control-060117-104941. URL https://doi.org/10.1146/annurev-control-060117-104941."),
    T("p0012-b003", "Ron S Dembo. Scenario optimization. *Annals of Operations Research*, 30:63–80, 1991."),
    T("p0012-b004",
      "Alex Devonport. *Contributions to the Statistical Foundation of Data-Driven Control*. PhD thesis, EECS "
      "Department, University of California, Berkeley, Aug 2023. URL "
      "http://www2.eecs.berkeley.edu/Pubs/TechRpts/2023/EECS-2023-207.html."),
    T("p0012-b005",
      "Alex Devonport and Murat Arcak. Data-driven reachable set computation using adaptive gaussian process "
      "classification and monte carlo methods. In *2020 American Control Conference (ACC)*, pages 2629–2634, 2020a. "
      "doi: 10.23919/ACC45564.2020.9147918."),
    T("p0012-b006",
      "Alex Devonport and Murat Arcak. Estimating reachable sets with scenario optimization. In *Proceedings of the "
      "2nd Conference on Learning for Dynamics and Control*, volume 120 of *Proceedings of Machine Learning "
      "Research*, pages 75–84. PMLR, 10–11 Jun 2020b. URL https://proceedings.mlr.press/v120/devonport20a.html."),
    T("p0012-b007",
      "Alex Devonport, Forest Yang, Laurent El Ghaoui, and Murat Arcak. Data-driven reachability analysis with "
      "christoffel functions. In *2021 60th IEEE Conference on Decision and Control (CDC)*, page 5067–5072. IEEE "
      "Press, 2021. doi: 10.1109/CDC45484.2021.9682860. URL https://doi.org/10.1109/CDC45484.2021.9682860."),
    T("p0012-b008",
      "Alexandre Donzé and Oded Maler. Systematic simulation using sensitivity analysis. In *Proceedings of the 10th "
      "International Conference on Hybrid Systems: Computation and Control*, HSCC’07, page 174–189, Berlin, "
      "Heidelberg, 2007. Springer-Verlag. ISBN 9783540714927."),
    T("p0012-b009",
      "Parasara Sridhar Duggirala, Sayan Mitra, and Mahesh Viswanathan. Verification of annotated models from "
      "executions. In *2013 Proceedings of the International Conference on Embedded Software (EMSOFT)*, pages 1–10, "
      "2013. doi: 10.1109/EMSOFT.2013.6658604."),
    T("p0012-b010",
      "Chuchu Fan, Bolun Qi, Sayan Mitra, and Mahesh Viswanathan. Dryvr: Data-driven verification and compositional "
      "reasoning for automotive systems. In Rupak Majumdar and Viktor Kunčak, editors, *Computer Aided Verification*, "
      "pages 441–461, Cham, 2017. Springer International Publishing. ISBN 978-3-319-63387-9."),
    T("p0012-b011",
      "Simone Garatti and Marco C. Campi. Non-convex scenario optimization. *Mathematical Programming*, 2024. doi: "
      "10.1007/s10107-024-02074-3. URL https://doi.org/10.1007/s10107-024-02074-3."),
    T("p0012-b012",
      "Antoine Girard. Reachability of uncertain linear systems using zonotopes. In Manfred Morari and Lothar Thiele, "
      "editors, *Hybrid Systems: Computation and Control*, pages 291–305, Berlin, Heidelberg, 2005. Springer Berlin "
      "Heidelberg."),
    O("p0012-b013", PAGENO),
]

# ----------------------------------------------------------------------------- page 13
NOTES[13] = COMMON + r"""
Page 13: all 11 entries (Girard and Pappas ... Prajna and Jadbabaie) read against the 170 dpi render, word by
word. Running header and page number 13 omitted. Corrections of extraction damage: split diacritic restored
('João'); line-wrap hyphens removed ('approximation', 'Proceedings', 'Automation', 'discriminating',
'Conference'); the compound 'stochastic-deterministic' is broken at its real hyphen (extractor had
'stochasticdeterministic'); broken DOIs / URLs closed up ('https://doi.org/10.1016/S0167-6911(00)00059-1',
'https://www.sciencedirect.com/science/article/pii/S0167691100000591',
'https://api.semanticscholar.org/CorpusID:221266413', 'https://doi.org/10.3182/20140824-6-ZA-1003.02590',
'https://www.sciencedirect.com/science/article/pii/S1474667016417611', 'https://doi.org/10.1145/3302504.3313354');
'50(7):947–957' closed up across the line break. Kept as printed: 'Systems Control Letters' (the ampersand of
the journal name is missing in the print, which shows only a wider gap), '60(1):265 – 270' with spaced dash,
'HSCC ’19' with a space, 'page 268–269' (singular), 'hamilton-jacobi' in lower case, 'pages 2884–2889 Vol.3',
'(IEEE Cat. No.03CH37475)'.
"""
PAGES[13] = [
    O("p0013-b000", RUNHEAD),
    T("p0013-b001",
      "Antoine Girard and George J. Pappas. Verification using simulation. In João P. Hespanha and Ashish Tiwari, "
      "editors, *Hybrid Systems: Computation and Control*, pages 272–286, Berlin, Heidelberg, 2006. Springer Berlin "
      "Heidelberg."),
    T("p0013-b002",
      "Lukas Hewing and Melanie N. Zeilinger. Scenario-based probabilistic reachable sets for recursively feasible "
      "stochastic model predictive control. *IEEE Control Systems Letters*, 4(2):450–455, 2020. doi: "
      "10.1109/LCSYS.2019.2949194."),
    T("p0013-b003",
      "A.B. Kurzhanski and P. Varaiya. Ellipsoidal techniques for reachability analysis: internal approximation. "
      "*Systems Control Letters*, 41(3):201–211, 2000. ISSN 0167-6911. doi: "
      "https://doi.org/10.1016/S0167-6911(00)00059-1. URL "
      "https://www.sciencedirect.com/science/article/pii/S0167691100000591."),
    T("p0013-b004",
      "Thomas Lew and Marco Pavone. Sampling-based reachability analysis: A random set theory approach with "
      "adversarial sampling. *ArXiv*, abs/2008.10180, 2020. URL https://api.semanticscholar.org/CorpusID:221266413."),
    T("p0013-b005",
      "John Maidens and Murat Arcak. Reachability analysis of nonlinear systems using matrix measures. *IEEE "
      "Transactions on Automatic Control*, 60(1):265 – 270, 2015."),
    T("p0013-b006",
      "G.R. Marseglia, J.K. Scott, L. Magni, R.D. Braatz, and D.M. Raimondo. A hybrid stochastic-deterministic "
      "approach for active fault diagnosis using scenario optimization. *IFAC Proceedings Volumes*, 47(3):1102–1107, "
      "2014. ISSN 1474-6670. doi: https://doi.org/10.3182/20140824-6-ZA-1003.02590. URL "
      "https://www.sciencedirect.com/science/article/pii/S1474667016417611. 19th IFAC World Congress."),
    T("p0013-b007",
      "P.-J. Meyer, A. Devonport, and M. Arcak. *Interval Reachability Analysis: Bounding Trajectories of Uncertain "
      "Systems with Boxes for Control and Verification*. SpringerBriefs in Control, Automation and Robotics. "
      "Springer, 2021. doi: 10.1007/978-3-030-65110-7."),
    T("p0013-b008",
      "Ian M. Mitchell, Jacob Budzis, and Andriy Bolyachevets. Invariant, viability and discriminating kernel "
      "under-approximation via zonotope scaling: Poster abstract. In *Proceedings of the 22nd ACM International "
      "Conference on Hybrid Systems: Computation and Control*, HSCC ’19, page 268–269, New York, NY, USA, 2019. "
      "Association for Computing Machinery. ISBN 9781450362825. doi: 10.1145/3302504.3313354. URL "
      "https://doi.org/10.1145/3302504.3313354."),
    T("p0013-b009",
      "I.M. Mitchell, A.M. Bayen, and C.J. Tomlin. A time-dependent hamilton-jacobi formulation of reachable sets for "
      "continuous dynamic games. *IEEE Transactions on Automatic Control*, 50(7):947–957, 2005. doi: "
      "10.1109/TAC.2005.851439."),
    T("p0013-b010",
      "S. Prajna. Barrier certificates for nonlinear model validation. In *42nd IEEE International Conference on "
      "Decision and Control (IEEE Cat. No.03CH37475)*, volume 3, pages 2884–2889 Vol.3, 2003. doi: "
      "10.1109/CDC.2003.1273063."),
    T("p0013-b011",
      "Stephen Prajna and Ali Jadbabaie. Safety verification of hybrid systems using barrier certificates. In Rajeev "
      "Alur and George J. Pappas, editors, *Hybrid Systems: Computation and Control*, pages 477–492, Berlin, "
      "Heidelberg, 2004. Springer Berlin Heidelberg. ISBN 978-3-540-24743-2."),
    O("p0013-b012", PAGENO),
]

# ----------------------------------------------------------------------------- page 14
NOTES[14] = COMMON + r"""
Page 14: all 6 entries (Qi ... Yang) read against the 170 dpi render, word by word; the rest of the page is
blank. Running header and page number 14 omitted. Corrections of extraction damage: split cedillas restored
('Behçet Açikmeşe'); line-wrap hyphens removed ('International', 'Incorporated'); the compound 'partition-based'
is broken at its real hyphen (extractor had 'partitionbased'); broken DOI / URL closed up ('doi:
10.23919/ACC.2019.8814354', 'https://doi.org/10.1145/3178126.3187008'). Kept as printed: 'HSCC ’18' with a
space, 'page 269–270' (singular), 'Dryvr 2.0', 'Neureach', 'Pac model checking'. The bibliography has 39
entries in total (10 + 12 + 11 + 6).
"""
PAGES[14] = [
    O("p0014-b000", RUNHEAD),
    T("p0014-b001",
      "Bolun Qi, Chuchu Fan, Minghao Jiang, and Sayan Mitra. Dryvr 2.0: A tool for verification and controller "
      "synthesis of black-box cyber-physical systems. In *Proceedings of the 21st International Conference on Hybrid "
      "Systems: Computation and Control (Part of CPS Week)*, HSCC ’18, page 269–270, New York, NY, USA, 2018. "
      "Association for Computing Machinery. ISBN 9781450356428. doi: 10.1145/3178126.3187008. URL "
      "https://doi.org/10.1145/3178126.3187008."),
    T("p0014-b002",
      "Hossein Sartipizadeh, Abraham P. Vinod, Behçet Açikmeşe, and Meeko Oishi. Voronoi partition-based scenario "
      "reduction for fast sampling-based stochastic reachability computation of linear systems. In *2019 American "
      "Control Conference (ACC)*, pages 37–44, 2019. doi: 10.23919/ACC.2019.8814354."),
    T("p0014-b003",
      "Dawei Sun and Sayan Mitra. Neureach: Learning reachability functions from simulations. In Dana Fisman and "
      "Grigore Rosu, editors, *Tools and Algorithms for the Construction and Analysis of Systems*, pages 322–337, "
      "Cham, 2022. Springer International Publishing."),
    T("p0014-b004",
      "Roberto Tempo, Giuseppe Calafiore, and Fabrizio Dabbene. *Randomized Algorithms for Analysis and Control of "
      "Uncertain Systems: With Applications*. Springer Publishing Company, Incorporated, 2nd edition, 2012. ISBN "
      "1447146093."),
    T("p0014-b005",
      "Bai Xue, Miaomiao Zhang, Arvind Easwaran, and Qin Li. Pac model checking of black-box continuous-time "
      "dynamical systems. *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, "
      "39(11):3944–3955, 2020. doi: 10.1109/TCAD.2020.3012251."),
    T("p0014-b006",
      "Yang Yang, Jun Zhang, Kai-Quan Cai, and Maria Prandini. Multi-aircraft conflict detection and resolution based "
      "on probabilistic reach sets. *IEEE Transactions on Control Systems Technology*, 25(1):309–316, 2017. doi: "
      "10.1109/TCST.2016.2542046."),
    O("p0014-b007", PAGENO),
]

if __name__ == "__main__":
    write_pages(PAGES, NOTES)
