from pagelib import *
P = 28
items = [
    run_header(P),
    page_number(P),
]
save(P, items, r"""
Compared with a 100 dpi render of PDF page 28: the page carries only the running header 'NATH YIN CHOU' and the page
number 28 and is otherwise blank (the last page of the arXiv PDF, after the float page with Figure 12). Both items are
omitted as page furniture; nothing else is on the page (the PDF text layer of the page has only these two lines).
""")
