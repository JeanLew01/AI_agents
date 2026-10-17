"""PDF access: text lines with positions, fonts, metadata, links, rendering."""

from __future__ import annotations

import re
import shutil
import subprocess
from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import numpy as np
import pymupdf

PT_TO_BP = 72.0 / 72.27


@dataclass
class Line:
    page: int  # 0-based
    text: str
    bbox: tuple[float, float, float, float]  # x0, y0, x1, y1 in bp, origin top-left
    size: float
    font: str


@dataclass
class FontInfo:
    name: str
    type: str
    encoding: str
    embedded: bool
    subset: bool
    unicode: bool
    obj: str


class PdfDoc:
    def __init__(self, path: Path):
        self.path = Path(path)
        self.doc = pymupdf.open(str(self.path))
        self._lines: dict[int, list[Line]] = {}

    def close(self) -> None:
        self.doc.close()

    @property
    def page_count(self) -> int:
        return self.doc.page_count

    @property
    def file_size(self) -> int:
        return self.path.stat().st_size

    def page_size(self, i: int) -> tuple[float, float]:
        r = self.doc[i].rect
        return r.width, r.height

    @property
    def metadata(self) -> dict[str, str]:
        return {k: (v or "") for k, v in (self.doc.metadata or {}).items()}

    @property
    def xmp(self) -> str:
        try:
            return self.doc.get_xml_metadata() or ""
        except Exception:
            return ""

    @property
    def version(self) -> str:
        head = self.path.read_bytes()[:1024]
        m = re.search(rb"%PDF-(\d\.\d)", head)
        ver = m.group(1).decode() if m else "?"
        try:  # a /Version entry in the catalog overrides the header
            cat = self.doc.pdf_catalog()
            kind, val = self.doc.xref_get_key(cat, "Version")
            if kind == "name" and val:
                ver = max(ver, val.lstrip("/"))
        except Exception:
            pass
        return ver

    # ---- text -------------------------------------------------------------------------
    def page_text(self, i: int) -> str:
        return self.doc[i].get_text("text")

    def all_text(self) -> str:
        return "\n".join(self.page_text(i) for i in range(self.page_count))

    def lines(self, i: int) -> list[Line]:
        if i not in self._lines:
            out = []
            d = self.doc[i].get_text("dict")
            for b in d.get("blocks", []):
                for ln in b.get("lines", []):
                    spans = [s for s in ln.get("spans", []) if s.get("text", "").strip()]
                    if not spans:
                        continue
                    text = "".join(s["text"] for s in ln["spans"]).strip()
                    size = max(s["size"] for s in spans)
                    out.append(Line(i, re.sub(r"\s+", " ", text), tuple(ln["bbox"]), size, spans[0]["font"]))
            out.sort(key=lambda l: (round(l.bbox[1], 1), l.bbox[0]))
            self._lines[i] = out
        return self._lines[i]

    def spans(self, i: int) -> list[dict]:
        out = []
        for b in self.doc[i].get_text("dict").get("blocks", []):
            for ln in b.get("lines", []):
                for s in ln.get("spans", []):
                    if s.get("text", "").strip():
                        out.append(s)
        return out

    @property
    def body_font_size(self) -> float:
        c: Counter[float] = Counter()
        for i in range(min(self.page_count, 6)):
            for s in self.spans(i):
                c[round(s["size"], 1)] += len(s["text"])
        return c.most_common(1)[0][0] if c else 10.0

    def find_heading(self, pattern: str, start_page: int = 0) -> Line | None:
        """First line (from start_page) whose whole text matches pattern, ignoring case; letter-spaced
        small caps such as 'R EFERENCES' are matched too."""
        rx = re.compile(r"\s*(?:" + pattern + r")\s*", re.I)
        for i in range(start_page, self.page_count):
            for ln in self.lines(i):
                if len(ln.text) > 90:
                    continue
                if rx.fullmatch(ln.text) or rx.fullmatch(ln.text.replace(" ", "")):
                    return ln
        return None

    # ---- fonts ------------------------------------------------------------------------
    def fonts(self) -> list[FontInfo]:
        return pdffonts(self.path)

    def page_fonts(self, i: int) -> list[tuple]:
        """pymupdf font entries: (xref, ext, type, basefont, name, encoding, referencer)."""
        return self.doc[i].get_fonts(full=True)

    # ---- links ------------------------------------------------------------------------
    def uri_links(self) -> list[tuple[int, str, tuple]]:
        out = []
        for i in range(self.page_count):
            for ln in self.doc[i].get_links():
                if ln.get("kind") == pymupdf.LINK_URI and ln.get("uri"):
                    r = ln["from"]
                    out.append((i, ln["uri"], (r.x0, r.y0, r.x1, r.y1)))
        return out

    def text_in(self, i: int, rect: tuple[float, float, float, float]) -> str:
        return re.sub(r"\s+", " ", self.doc[i].get_textbox(pymupdf.Rect(*rect))).strip()

    # ---- rendering --------------------------------------------------------------------
    def render_gray(self, i: int, dpi: int = 72) -> np.ndarray:
        pix = self.doc[i].get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY, annots=False, alpha=False)
        return np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width)


@lru_cache(maxsize=64)
def _pdffonts_cached(path: str, mtime: float) -> tuple[FontInfo, ...]:
    if shutil.which("pdffonts") is None:
        return tuple(_fonts_via_pymupdf(Path(path)))
    out = subprocess.run(["pdffonts", path], capture_output=True, text=True, errors="replace").stdout
    return tuple(parse_pdffonts(out))


def pdffonts(path: Path) -> list[FontInfo]:
    p = Path(path)
    return list(_pdffonts_cached(str(p), p.stat().st_mtime))


def parse_pdffonts(out: str) -> list[FontInfo]:
    """Parse `pdffonts` output from the right (font names can overflow their column)."""
    res = []
    for ln in out.splitlines()[2:]:
        t = ln.split()
        if len(t) < 8:
            continue
        name, typ = t[0], " ".join(t[1:-6])
        res.append(FontInfo(name, typ, t[-6], t[-5] == "yes", t[-4] == "yes", t[-3] == "yes", f"{t[-2]} {t[-1]}"))
    return res


def _fonts_via_pymupdf(path: Path) -> list[FontInfo]:
    doc = pymupdf.open(str(path))
    seen = {}
    for page in doc:
        for xref, ext, typ, base, name, enc, *_ in page.get_fonts(full=True):
            emb = ext not in ("n/a", "")
            seen[xref] = FontInfo(base, "Type 3" if typ == "Type3" else typ, enc, emb or typ == "Type3",
                                  "+" in base, False, str(xref))
    doc.close()
    return list(seen.values())


def text_block(layout: dict[str, float], page_index: int = 0) -> tuple[float, float, float, float] | None:
    """Text block rectangle in bp (x0, y0, x1, y1; origin top-left) from a TeX layout dict in pt."""
    need = ("textwidth", "textheight", "oddsidemargin", "topmargin", "headheight", "headsep")
    if not all(k in layout for k in need):
        return None
    side = layout["oddsidemargin"]
    if layout.get("twoside") and page_index % 2 == 1 and "evensidemargin" in layout:
        side = layout["evensidemargin"]
    x0 = 72.27 + layout.get("hoffset", 0.0) + side
    y0 = 72.27 + layout.get("voffset", 0.0) + layout["topmargin"] + layout["headheight"] + layout["headsep"]
    return (x0 * PT_TO_BP, y0 * PT_TO_BP, (x0 + layout["textwidth"]) * PT_TO_BP,
            (y0 + layout["textheight"]) * PT_TO_BP)
