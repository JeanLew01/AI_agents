from pagelib import *
from refs import entries
o = orig(12)
B = lambda k: o[k]["bbox"]
R = dict(entries)
keys = ["althoff2012avoiding", "bak2017simulation", "bortolussi2019neural", "cauchois2020robust", "cleaveland2023conformal",
        "devonport2020data", "devonport2020estimating", "devonport2021data", "dietrich2024nonconvex", "dryvr", "fisac2018general"]
ids = [f"p0012-b{n:03d}" for n in range(3, 14)]

items = [
    heading("p0012-b000", B("p0012-b000"), "## 6 Conclusion"),
    text("p0012-b001", B("p0012-b001"),
         "We introduced a scalable technique for reachability in real-world settings. Our results demonstrate that integrating PCA with Conformal inference significantly enhances the accuracy of error analysis. We validated the effectiveness of our approach across three distinct high-dimensional environments."),
    heading("p0012-b002", B("p0012-b002"), "## References"),
] + [text(i, B(i), R[k]) for i, k in zip(ids, keys)] + [
    omit("p0012-b014", B("p0012-b014"), "12",
         "Printed page number 12 centred at the foot of the page; page furniture, checked on the 170 dpi render."),
]

save(12, items, r"""
Compared with the 170 dpi render and the TeX source (main file for Section 6, neus2025-arxiv.bbl for the bibliography). Headings: '6
Conclusion' (##; in this arXiv version the Conclusion is Section 6, after the Acknowledgements) and 'References' (##, unnumbered).
The conclusion paragraph is identical to the TeX. Bibliography: natbib author-year style without numbers; the 11 entries of this page
(Althoff and Krogh 2012 to Fisac et al. 2018) are one text item each, in the printed (alphabetical) order, without the list bullets the
extractor had added. Each entry was generated from the authors' .bbl (\emph -> italics, '--' -> en dash, natbib year suffixes
'2020a'/'2020b' as printed), compared automatically with the PDF text layer (alphanumeric content identical for all 11) and read on
the render (author names, venue, volume/pages, year). Line-wrap hyphens removed ('reacha-bility', 'verifica-tion'); 'volume(issue):pages'
strings such as '64(7):2737–2752' are written closed up. Lower-case titles ('christoffel functions', 'gaussian process', 'monte carlo',
'Dryvr') are printed so. No mathematics on this page. Omitted: page number 12.
""")
