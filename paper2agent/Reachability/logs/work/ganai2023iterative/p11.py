from pagelib import *
from bib import BIB
import json
P = 11
bm = {int(n): v for n, v in json.load(open(S / "bibmap.json")).items()}
items = [heading("p0011-b000", B(P, "p0011-b000"), "## References")]
for n in sorted(bm):
    pg, iid = bm[n]
    if pg == P:
        items.append(text(iid, B(P, iid), BIB[n]))
assert len(items) == 20
items.append(pageno(P))
save(P, items, r"""
Compared with a 170 dpi render of PDF page 11 and with the thebibliography environment in main.tex (the reference list
is typeset from an embedded bibliography, so the source text is available). The unnumbered heading 'References' is
level 2. Entries [1]-[19], one text item per entry, generated from the TeX entries (ties, \newblock and protective
braces removed, '--' written as an en dash, accents composed, {\em ...} written as italics) and checked in two ways: a
script comparison of the letters and digits of every entry with the PDF text layer (identical for all 19), and reading
every entry on the render (author lists, italic venue names, volume(issue):pages, years). The extractor's list markers
('- [n]') and its spaces before commas after italic titles were removed. As printed: lower-case words in titles ('Cup:',
'Neural lyapunov control', 'almost lyapunov critics', 'lyapunov-like'), the author name 'Shegnbo Eben Li' in [9], the
straight apostrophe in 'd'Alché-Buc' in [16], abbreviated venues ('European Control Conf.', 'Conf. on Decision and
Control', 'Trans. on Automatic Control', 'Int. Federation of Automatic Control'). The compound 'self-driving' in [18] is
broken at a line end in the PDF ('self-/driving'); the hyphen is real (present in the source). Omitted: printed page
number 11.
""")
