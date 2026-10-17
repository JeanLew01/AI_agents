"""Extract numeric table cells (with row/column headers and source offsets) from tabular environments."""

from __future__ import annotations

import re
from dataclasses import dataclass

from .project import TexProject
from .source import latex_to_text, read_group

NUM_IN_CELL = re.compile(r"(?<![\w.])[-−]?\d+(?:\.\d+)?")


@dataclass
class Cell:
    table_label: str | None
    table_index: int
    row: int
    col: int
    text: str
    value: float
    raw: str  # the number as written
    decimals: int
    offset: int  # flat offset of the cell
    row_header: str
    col_header: str


def _split_top(s: str, sep: str) -> list[tuple[int, str]]:
    """Split s on sep at brace depth 0, skipping escaped separators; returns (offset, piece)."""
    out, depth, start, i = [], 0, 0, 0
    while i < len(s):
        c = s[i]
        if c == "\\":
            if sep == "\\\\" and s.startswith("\\\\", i) and depth == 0:
                out.append((start, s[start:i]))
                i += 2
                start = i
                continue
            i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
        elif depth == 0 and sep == "&" and c == "&":
            out.append((start, s[start:i]))
            start = i + 1
        i += 1
    out.append((start, s[start:]))
    return out


def table_cells(proj: TexProject) -> list[Cell]:
    cells: list[Cell] = []
    floats = proj.envs_named("table", "table*", "wraptable")
    tabulars = proj.envs_named("tabular", "tabular*", "tabularx", "longtable", "tabulary")
    for ti, tab in enumerate(tabulars):
        flt = next((f for f in floats if f.start <= tab.start < f.end), None)
        label = None
        if flt:
            lab = next((l for l in proj.labels if flt.start <= l.start < flt.end), None)
            label = lab.key if lab else None
        body_start = tab.body_start
        # skip the column spec {lcc} (and the width for tabular*/tabularx)
        n_specs = 2 if tab.name in ("tabular*", "tabularx", "tabulary") else 1
        pos = body_start
        for _ in range(n_specs):
            g = read_group(proj.flat, pos)
            if g:
                pos = g[1]
        body = proj.flat[pos:tab.body_end]
        rows = []
        for roff, row in _split_top(body, "\\\\"):
            row_clean = re.sub(r"\\(?:toprule|midrule|bottomrule|hline|cline\{[^}]*\}|cmidrule(?:\([^)]*\))?\{[^}]*\}|addlinespace)", " ", row)
            if not row_clean.strip():
                continue
            rows.append([(pos + roff + coff, piece) for coff, piece in _split_top(row, "&")])
        if not rows:
            continue
        header = [latex_to_text(re.sub(r"\\(?:toprule|midrule|hline)", "", p)) for _o, p in rows[0]]
        for r_i, row in enumerate(rows):
            row_header = latex_to_text(re.sub(r"\\(?:toprule|midrule|bottomrule|hline)", "", row[0][1])) if row else ""
            for c_i, (off, piece) in enumerate(row):
                text = latex_to_text(re.sub(r"\\(?:toprule|midrule|bottomrule|hline)", "", piece)).replace("−", "-")
                text = re.sub(r"\\pm|±", " ± ", text)
                for m in NUM_IN_CELL.finditer(text):
                    raw = m.group(0).replace("−", "-")
                    dec = len(raw.split(".")[1]) if "." in raw else 0
                    cells.append(Cell(label, ti, r_i, c_i, text, float(raw), raw, dec, off, row_header,
                                      header[c_i] if c_i < len(header) else ""))
    return cells
