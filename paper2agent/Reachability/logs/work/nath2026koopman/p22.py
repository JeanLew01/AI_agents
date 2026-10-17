from pagelib import *
P = 22
items = [
    heading("p0022-b001", B(P, "p0022-b001"), "#### 8.3.9. Additional results on MuJoCo swimmer system."),
    text("p0022-b002", B(P, "p0022-b002"), O(P, "p0022-b002", ("by the phaseshifted oscillations", "by the phase-shifted oscillations"))),
    run_header(P),
    page_number(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 22 and with appendix.tex. Heading '8.3.9. Additional results on MuJoCo
swimmer system.' (small caps, final period) written as level 4 in the TeX's spelling. Paragraph: extractor prose
checked on the render; the line-wrap 'phase-/shifted' is a real compound (TeX 'phase-shifted'), restored (the
extractor had 'phaseshifted'); 'Swim-mer' closed up; 'component-wise', '28-dimensional', 'high-dimensional',
'closed-loop', 'globally-linear', 'multi-body', 'long-horizon' kept; textual citation 'Todorov et al. (2012)' as
printed; 'Figure 12' as printed. The rest of the page is empty (the appendix figures follow as float pages 23-27).
Omitted: running header 'NATH YIN CHOU' and page number 22.
""")
