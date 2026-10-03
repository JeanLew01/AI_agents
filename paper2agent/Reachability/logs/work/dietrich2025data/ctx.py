"""Print pypdf and pymupdf raw text around patterns (run with the tool's cached environment python; read-only)."""
import re, sys
from pathlib import Path
from pypdf import PdfReader
import pymupdf
src = Path.home() / "AI_agents/paper2agent/Reachability/paper-review/dietrich2025data-paper/documents/s001-dietrich2025data/source.pdf"
page = int(sys.argv[1]); pats = sys.argv[2:]
t1 = PdfReader(str(src)).pages[page - 1].extract_text()
t2 = pymupdf.open(src)[page - 1].get_text()
for name, t in (("pypdf", t1), ("pymupdf", t2)):
    for p in pats:
        for m in re.finditer(p, t):
            print(f"{name} p{page} /{p}/: {t[max(0, m.start()-30):m.end()+30]!r}")
