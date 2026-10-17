from pagelib import *
P = 13
FIX = {"p0013-b002": [("for datadriven reachability", "for data-driven reachability")],
       "p0013-b013": [("efficient samplingbased algorithm", "efficient sampling-based algorithm")]}
items = [ref(P, "p0013-b%03d" % k, *FIX.get("p0013-b%03d" % k, [])) for k in range(1, 15)] + [
    run_header(P),
    page_number(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 13 and with main.bbl. Page consists only of bibliography entries: 14
entries (Chou, Ozay, Berenson 2022 ... Lindemann et al. 2024), one text item per entry in printed order, each read
on the render word by word. Venue/book titles printed underlined (not reproduced; extractor <u> tags and '- ' list
markers removed). Two real compounds broken at line ends were restored ('data-driven' in Dietrich et al. 2024,
'sampling-based' in Lew et al. 2022; the extractor had 'datadriven', 'samplingbased'); ordinary wraps ('guar-antees',
'con-trol') closed up. As printed: 'IEEE Access, 9, 2021.', 'Explicit error bounds for carleman linearization. 2017.',
'volume 13035', '43(11):4250–4261', 'Fastrack', '23–24 Jun 2022', 'Formal verification and control with conformal
prediction. 2024.' Omitted: running header (short title) and page number 13.
""")
