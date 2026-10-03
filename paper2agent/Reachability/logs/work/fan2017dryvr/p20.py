from pagelib import *
from refs import ref_items

items = ref_items(20, 23, 33) + [pageno(20, [300.0, 696.0, 311.0, 703.0])]

save(20, items, r"""
Compared with a 190-dpi render of the text block and with main2.bbl. Bibliography entries [23]-[33], one item per entry, generated from the authors' .bbl and compared automatically with the PDF text layer (letters and digits identical for all eleven entries) and read entry by entry on the render. Checked details: [23] 'C2E2', the italic venue ends with 'April 11-18, 2015.' followed by a comma ('2015.*, volume 9035 of *Lecture Notes in Computer Science*'), the hyphen of '11-18' is real (line end in the PDF); [25] '410:4262–4291'; [26] 'pages 3567–3572'; [28] "EMSOFT ’16, pages 6:1–6:10"; [29] 'Sanghai, China.' inside the italic venue (printed spelling), 'volume 9364 of *LNCS*', 'pages 446–463'; [30] lower-case 'c2e2'; [31] 'Python package PyGLPK.' with the URL http://tfinley.net/software/pyglpk/ (the first line of this entry is printed stretched); [33] 'Donzé', 'pages 379–395'. Real hyphens kept ('on-the-fly', 'over-approximation', 'continuous-time', 's-taliro'); line-wrap hyphens removed. Omitted: page number 20.
""")
