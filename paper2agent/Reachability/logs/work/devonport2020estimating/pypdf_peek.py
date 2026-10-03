#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pymupdf==1.28.2", "pymupdf4llm==1.28.2", "pypdf==6.18.1", "pillow==12.2.0"]
# ///
"""Show how the independent parser (pypdf) renders the lines that carry signed numbers, pages 4-7.
Same dependency header as paper_bundle.py so that uv reuses the cached environment (no install)."""
import os, re, sys
from pypdf import PdfReader
D = os.path.expanduser("~/AI_agents/paper2agent/Reachability/paper-review/devonport2020estimating-paper/documents/s001-devonport2020estimating")
r = PdfReader(f"{D}/source.pdf")
for pn in (4, 5, 6, 7):
    t = r.pages[pn - 1].extract_text()
    print(f"=== page {pn}")
    for line in t.splitlines():
        if re.search(r"[−-]\s*\d|e\s*−|46|log|\+ ?1", line):
            print("   ", repr(line))
