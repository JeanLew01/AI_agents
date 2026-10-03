# /// script
# requires-python = ">=3.11"
# dependencies = ["pymupdf==1.28.2", "pymupdf4llm==1.28.2", "pypdf==6.18.1", "pillow==12.2.0"]
# ///
"""Print the independent parser's (pypdf) and pymupdf's raw text around given patterns, to explain number diagnostics."""
import re, sys
from pathlib import Path
from pypdf import PdfReader
import pymupdf
src = Path.home() / "AI_agents/paper2agent/Reachability/paper-review/devonport2021data-paper/documents/s001-devonport2021data/source.pdf"
page = int(sys.argv[1]); pats = sys.argv[2:]
t1 = PdfReader(str(src)).pages[page - 1].extract_text()
t2 = pymupdf.open(src)[page - 1].get_text()
for name, t in (("pypdf", t1), ("pymupdf", t2)):
    for p in pats:
        for m in re.finditer(p, t):
            print(f"{name} p{page} /{p}/: {t[max(0, m.start()-25):m.end()+25]!r}")
