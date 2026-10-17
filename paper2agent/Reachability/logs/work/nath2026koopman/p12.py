from pagelib import *
P = 12
items = [
    text("p0012-b001", B(P, "p0012-b001"),
         r"set with a specified probability (i.e., at least $1-\delta$). Across several benchmarks, including a unicycle, planar/3D quadrotors, MuJoCo hopper, and a 13-link MuJoCo swimmer, our method computes reachable sets efficiently and over long time horizons. Future work aims to: 1) remove the dependence on reference trajectories and 2) replace LQR with a robust control policy that satisfies constraints despite model error to increase the time horizon over which the system can be verified.",
         join_previous="space"),
    heading("p0012-b002", B(P, "p0012-b002"), "## References"),
] + [ref(P, "p0012-b%03d" % k) for k in range(3, 15)] + [
    run_header(P),
    page_number(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 12 and with conclusion.tex and main.bbl. First item: end of the Conclusion
paragraph from page 11 (join_previous 'space'); '$1-\delta$' from the TeX; 'unicy-cle', 'de-pendence' closed up.
Source slip kept as printed: 'a 13-link MuJoCo swimmer' (the experiments describe a 28-dimensional swimmer with
extended links). Heading 'References' level 2 (unnumbered, as printed; the extractor had level 1). Bibliography in the
printed author-year style (natbib/jmlr): 12 entries on this page (Althoff 2015 ... Chou, Ozay, Berenson 2021), one
text item per entry in printed order; each entry read on the render word by word and against main.bbl. The venue and
book titles are printed underlined (jmlr bibliography style); the underline is not reproduced (the extractor's <u>
tags were removed) and the extractor's list markers '- ' were dropped (the PDF prints no labels). Lower-case words in
titles as printed ('koopman', 'Hamilton-jacobi', 'Deepreach'); 'page 23–32' (singular, as printed); 'December 14-17,
2021' with a hyphen as printed; en dashes in page ranges as printed. Omitted: running header 'NATH YIN CHOU' and page
number 12.
""")
