from pagelib import *
P = 14
FIX = {"p0014-b008": [("Jorge Cort´es", "Jorge Cortés")]}
items = [ref(P, "p0014-b%03d" % k, *FIX.get("p0014-b%03d" % k, [])) for k in range(1, 15)] + [
    run_header(P),
    page_number(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 14 and with main.bbl. Page consists only of the last 14 bibliography
entries (Liu et al. 2021 ... Zhang et al. 2018), one text item per entry in printed order, each read on the render
word by word; with pages 12-13 the bibliography has 40 entries, equal to the 40 \bibitem of main.bbl. Venue/book
titles printed underlined (not reproduced; extractor <u> tags and '- ' markers removed). Split diacritic repaired:
'Cort´es' -> 'Cortés' (Shi et al. 2024). Kept as printed: 'Herman Øie Kolden', '118(35):e2026805118', 'doi:
10.21105/joss.05881.', 'M.s. thesis, KTH, Stockholm, Sweden, 2015.', 'Grigore Rosu', 'Cham, 2022. Springer
International Publishing.', 'Mujoco', 'Pykoopman', 'Neureach'. The lower part of the page is empty; the appendix
starts on page 15 (\newpage). Omitted: running header 'NATH YIN CHOU' and page number 14.
""")
