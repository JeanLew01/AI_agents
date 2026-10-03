from pagelib import *
from bib import BIB
import json
P = 12
bm = {int(n): v for n, v in json.load(open(S / "bibmap.json")).items()}
items = []
for n in sorted(bm):
    pg, iid = bm[n]
    if pg == P:
        items.append(text(iid, B(P, iid), BIB[n]))
assert len(items) == 20 and items[0]["markdown"].startswith("[20]") and items[-1]["markdown"].startswith("[39]")
items.append(pageno(P))
save(P, items, r"""
Compared with a 170 dpi render of PDF page 12 and with the thebibliography environment in main.tex. Entries [20]-[39],
one text item per entry, generated from the TeX entries (same conversion as on page 11) and checked by a script
comparison of letters and digits with the PDF text layer (identical for all 20) and by reading every entry on the
render. No entry is split across the page break (page 11 ends with [19], this page ends with [39]). The extractor's
list markers and spaces before commas after italic titles were removed. As printed: lower-case title words
('hamilton-jacobi' in [23] and [24], 'Crpo:' in [35], 'IEEE robotics and automation letters' in [22]), 'Nuoya Xiong et
al.' in [26], '7(1):2' in [30], 'CoRR, abs/1707.06347' in [33], 'March 2022' in [39]. Line-wrap hyphens of
'reinforcement' in [30] and 'Decomposition' in [37] are not real hyphens (the source has the unbroken words). Omitted:
printed page number 12.
""")
