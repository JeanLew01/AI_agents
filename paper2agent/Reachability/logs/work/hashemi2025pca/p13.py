from pagelib import *
from refs import entries
o = orig(13)
B = lambda k: o[k]["bbox"]
R = dict(entries)
keys = ["hashemi2024scaling", "hashemi2024statistical", "komendera2012intelligent", "lasserre2019empirical", "lindemann2023safe",
        "lindemann2024formal", "marx2021semi", "schilling2022verification", "sharma2024pac", "takezawa2005introduction",
        "tebjou2023data", "tonkens2023scalable", "tran2020nnv"]
ids = [f"p0013-b{n:03d}" for n in range(0, 13)]
items = [text(i, B(i), R[k]) for i, k in zip(ids, keys)] + [
    omit("p0013-b013", B("p0013-b013"), "13",
         "Printed page number 13 centred at the foot of the page; page furniture, checked on the 170 dpi render."),
]
save(13, items, r"""
Compared with the 170 dpi render and the authors' .bbl. Bibliography continued: 13 entries (Hashemi et al. 2024a to Tran et al. 2020),
one text item each in the printed order, without the list bullets the extractor had added. Each entry was generated from the .bbl,
compared automatically with the PDF text layer (alphanumeric content identical for all 13) and read on the render. Checked in
particular: the year suffixes '2024a' (Hashemi, Hoxha, Prokhorov, Fainekos, Deshmukh; ACM TCPS 8(4):1–28) and '2024b' (Hashemi,
Lindemann, Deshmukh; IEEE TCAD 43(11):4250–4261), which the citations in the text rely on; 'Sebastián' with accent; 'christoffel–darboux'
with an en dash; 'arXiv preprint arXiv:2409.00536'; 'Tebjou, Goran Frehse, et al.' as printed. Line-wrap hyphen removed in
'reach-ability' (Komendera et al.). Every entry starts and ends on this page, so no join across pages is needed. No mathematics on this
page. Omitted: page number 13.
""")
