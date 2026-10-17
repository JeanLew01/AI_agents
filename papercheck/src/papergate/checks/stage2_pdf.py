"""Stage 2: PDF compliance (page limit, fonts, margins, size, version, links)."""

from __future__ import annotations

import ipaddress
import re
from urllib.parse import urlparse

import numpy as np
import pymupdf

from ..models import Severity
from ..pdf.doc import text_block
from ..registry import Check, SkipCheck, register
from ..tex.source import find_commands

DEFAULT_HEADINGS = {
    "references": r"(?:\d+\.?\s*)?(?:references|bibliography|reference list|literature cited)",
    "acknowledgments": r"(?:\d+\.?\s*)?acknowledge?ments?",
    "appendix": r"(?:appendix|appendices|supplementary materials?)(?:\s+.{0,60})?",
    "limitations": r"(?:\d+\.?\s*)?limitations?",
    "checklist": r".{0,40}checklist",
    "impact_statement": r"(?:\d+\.?\s*)?(?:broader|societal) impacts?(?: statement)?",
}

MATPLOTLIB_FIX = ("Regenerate the figure with TrueType/Type 42 fonts: in matplotlib set "
                  "plt.rcParams['pdf.fonttype'] = 42 and plt.rcParams['ps.fonttype'] = 42 before saving "
                  "(papergate never regenerates figures; do it in your plotting script).")


def _layout(ctx) -> dict[str, float]:
    return ctx.config.template.layout or (ctx.build.layout if ctx.build else {}) or {}


def main_body_extent(ctx) -> dict:
    """Locate the end of the counted main body. Returns {'pages': n, 'end': (page, y, name)|None}."""
    if "body_extent" in ctx.cache:
        return ctx.cache["body_extent"]
    pdf = ctx.pdf
    cfg = ctx.config.page_limit
    pats = dict(DEFAULT_HEADINGS)
    pats.update(cfg.heading_patterns)
    proj = ctx.project
    if "appendix" in cfg.excluded_sections and proj.appendix_start is not None:
        first = next((s for s in proj.sections if s.start >= proj.appendix_start and s.level <= 1), None)
        if first and first.title:
            title = r"\s*".join(re.escape(w) for w in first.title.split())
            pats["appendix"] = r"(?:[A-Z](?:\.\d+)*\.?\s*)?" + title + "|" + pats["appendix"]
    starts = []
    for name in cfg.excluded_sections:
        pat = pats.get(name)
        if not pat:
            continue
        ln = pdf.find_heading(pat, start_page=0)
        if ln is not None and not (ln.page == 0 and ln.bbox[1] < 0.25 * pdf.page_size(0)[1]):
            starts.append((ln.page, ln.bbox[1], name, ln.text))
    lay = _layout(ctx)
    res: dict = {"total_pages": pdf.page_count, "end": None}
    if not cfg.excluded_sections:  # everything counts (e.g. IEEE: references included)
        res["pages"] = pdf.page_count
        res["end"] = {"page": pdf.page_count, "y": 0, "section": "end of document", "heading": ""}
    elif not starts:
        res["pages"] = pdf.page_count
    else:
        page, y, name, text = min(starts)
        tb = text_block(lay, page) if lay else None
        top = (tb[1] - 2) if tb else 0.06 * pdf.page_size(page)[1]
        above = [l for l in pdf.lines(page) if l.bbox[3] < y - 1 and l.bbox[1] >= top]
        res["pages"] = page + (1 if above else 0)
        res["end"] = {"page": page + 1, "y": round(y, 1), "section": name, "heading": text}
    ctx.cache["body_extent"] = res
    return res


@register
class PageLimit(Check):
    id = "pdf.page_limit"
    stage = 2
    requires = frozenset({"pdf"})
    severity = Severity.BLOCKER
    why = "Over-length papers are rejected or returned without review."

    def run(self, ctx):
        limit = ctx.config.page_limit.for_mode(ctx.mode)
        ext = main_body_extent(ctx)
        ctx.metrics["pages"] = {**ext, "limit": limit, "excluded_sections": ctx.config.page_limit.excluded_sections}
        out = []
        if ext["end"] is None:
            out.append(self.finding(ctx, f"could not find where the counted main body ends "
                                         f"({', '.join(ctx.config.page_limit.excluded_sections)} headings not found "
                                         f"in the PDF); counting all {ext['total_pages']} pages",
                                    severity=Severity.WARN,
                                    instructions="Set page_limit.heading_patterns in the venue config."))
        if limit is not None and ext["pages"] > limit:
            end = ext["end"]
            where = f"; the {end['section']} heading is on page {end['page']}" if end else ""
            out.append(self.finding(ctx, f"main body is {ext['pages']} pages, limit is {limit} for {ctx.mode}{where}",
                                    page=end["page"] if end else ext["total_pages"],
                                    quote=end["heading"] if end else "",
                                    instructions=f"Cut the main body to {limit} pages."))
        return out


def _figure_fonts(ctx, rel: str):
    """Fonts of an included PDF figure: list of (basefont, type, embedded)."""
    key = ("figfonts", rel)
    if key not in ctx.cache:
        res = []
        try:
            doc = pymupdf.open(str(ctx.paper_dir / rel))
            for page in doc:
                for xref, ext, typ, base, *_ in page.get_fonts(full=True):
                    res.append((base, typ, ext not in ("n/a", "")))
            doc.close()
        except Exception:
            pass
        ctx.cache[key] = res
    return ctx.cache[key]


def _strip_subset(name: str) -> str:
    return re.sub(r"^[A-Z]{6}\+", "", name or "")


@register
class Type3Fonts(Check):
    id = "pdf.fonts.type3"
    stage = 2
    requires = frozenset({"pdf"})
    severity = Severity.BLOCKER
    why = "Type 3 (bitmap) fonts are rejected by IEEE PDF eXpress/PaperCept and render poorly."

    def run(self, ctx):
        if not ctx.config.fonts.forbid_type3:
            return []
        pdf = ctx.pdf
        pages: dict[str, set[int]] = {}
        for i in range(pdf.page_count):
            for xref, ext, typ, base, *_ in pdf.page_fonts(i):
                if typ == "Type3":
                    pages.setdefault(_strip_subset(base) or f"xref{xref}", set()).add(i + 1)
        if not pages:
            return []
        out = []
        attributed = set()
        for off, name, rel in ctx.project.graphics:
            if not rel or not rel.lower().endswith(".pdf"):
                continue
            t3 = sorted({_strip_subset(b) or "[unnamed]" for b, typ, _e in _figure_fonts(ctx, rel) if typ == "Type3"})
            if t3:
                attributed.update(t3)
                out.append(self.at(ctx, off, f"figure {rel} embeds Type 3 font(s): {', '.join(t3)}",
                                   instructions=MATPLOTLIB_FIX))
        rest = {n: p for n, p in pages.items() if n not in attributed}
        for name, pgs in sorted(rest.items()):
            bitmap_tex = bool(re.match(r"(ec|tc|cm|sf|la|lmr)[a-z]*\d+$", name, re.I)) or name.startswith("xref")
            hint = ("This looks like a bitmap TeX font: add \\usepackage{lmodern} (or install cm-super) when "
                    "using \\usepackage[T1]{fontenc}." if bitmap_tex else
                    "Find the figure that uses this font (pdffonts on each figure file) and regenerate it "
                    "with embedded Type 1/TrueType fonts. " + MATPLOTLIB_FIX)
            out.append(self.finding(ctx, f"Type 3 font {name} on page(s) {', '.join(map(str, sorted(pgs)))}",
                                    page=min(pgs), quote=name, instructions=hint))
        return out


@register
class EmbeddedFonts(Check):
    id = "pdf.fonts.embedded"
    stage = 2
    requires = frozenset({"pdf"})
    severity = Severity.BLOCKER
    why = "Non-embedded fonts are rejected by IEEE PDF eXpress/PaperCept and print with substitutes."

    def run(self, ctx):
        if not ctx.config.fonts.require_embedded:
            return []
        bad = [f for f in ctx.pdf.fonts() if not f.embedded and f.type != "Type 3"]
        if not bad:
            return []
        out = []
        names = {_strip_subset(f.name) for f in bad}
        attributed = set()
        for off, _name, rel in ctx.project.graphics:
            if not rel or not rel.lower().endswith(".pdf"):
                continue
            miss = sorted({_strip_subset(b) for b, typ, emb in _figure_fonts(ctx, rel) if not emb and typ != "Type3"} & names)
            if miss:
                attributed.update(miss)
                out.append(self.at(ctx, off, f"figure {rel} uses non-embedded font(s): {', '.join(miss)}",
                                   instructions="Re-export the figure with fonts embedded (matplotlib: "
                                                "pdf.fonttype=42; Inkscape/Illustrator: embed fonts)."))
        for n in sorted(names - attributed):
            out.append(self.finding(ctx, f"font {n} is not embedded", quote=n,
                                    instructions="Embed all fonts (e.g. pdflatex with updmap "
                                                 "pdftexDownloadBase14 true, or re-export the source figure)."))
        return out


@register
class FileSize(Check):
    id = "pdf.file_size"
    stage = 2
    requires = frozenset({"pdf"})
    severity = Severity.BLOCKER
    why = "Submission systems reject PDFs above the size limit."

    def run(self, ctx):
        size_mb = ctx.pdf.file_size / 1e6
        ctx.metrics["pdf_size_mb"] = round(size_mb, 2)
        limit = ctx.config.max_size_mb(ctx.mode)
        if limit is not None and size_mb > limit:
            return [self.finding(ctx, f"PDF is {size_mb:.1f} MB, limit is {limit} MB",
                                 instructions="Compress raster figures (e.g. JPEG for photos) or downsample them.")]
        return []


@register
class PdfVersion(Check):
    id = "pdf.version"
    stage = 2
    requires = frozenset({"pdf"})
    severity = Severity.WARN
    why = "Some submission systems only accept particular PDF versions."

    def run(self, ctx):
        ver = ctx.pdf.version
        ctx.metrics["pdf_version"] = ver
        allowed = ctx.config.pdf_version.allowed
        if allowed and ver not in allowed:
            return [self.finding(ctx, f"PDF version {ver} is not among the allowed {', '.join(allowed)}",
                                 instructions="With pdflatex, put \\pdfminorversion=4 before \\documentclass "
                                              "(or set it in the venue's recommended way).")]
        return []


_PRIVATE_HOST = re.compile(r"^(localhost|.*\.local|.*\.localdomain|.*\.internal)$", re.I)


def link_problem(uri: str) -> str | None:
    if any(c.isspace() for c in uri.strip()):
        return "contains whitespace"
    p = urlparse(uri)
    scheme = p.scheme.lower()
    if scheme in ("mailto",):
        return None if "@" in p.path else "mailto link without an address"
    if scheme == "file":
        return "points to a local file (file://)"
    if scheme == "" :
        if uri.startswith("/") or re.match(r"^[A-Za-z]:\\", uri):
            return "is an absolute local path"
        return "has no scheme (relative link)"
    if scheme not in ("http", "https", "ftp", "doi"):
        return f"uses the unusual scheme '{scheme}'"
    if scheme == "doi":
        return None
    host = (p.hostname or "").strip()
    if not host:
        return "has no host"
    if _PRIVATE_HOST.match(host):
        return f"points to a local host ({host})"
    try:
        ip = ipaddress.ip_address(host)
        if ip.is_private or ip.is_loopback or ip.is_unspecified or ip.is_link_local:
            return f"points to a private address ({host})"
    except ValueError:
        if "." not in host:
            return f"host '{host}' has no domain"
    return None


def source_urls(ctx) -> list[tuple[int, str]]:
    out = []
    for start, name, _star, _opts, arg, _end in find_commands(ctx.project.flat, r"url|href"):
        out.append((start, arg.strip()))
    return out


@register
class Links(Check):
    id = "pdf.links"
    stage = 2
    requires = frozenset({"pdf"})
    severity = Severity.WARN
    why = "Broken or local links do not work for readers."

    def run(self, ctx):
        out = []
        seen = set()
        src = source_urls(ctx)
        for page, uri, _rect in ctx.pdf.uri_links():
            if uri in seen:
                continue
            seen.add(uri)
            prob = link_problem(uri)
            if not prob:
                continue
            hit = next((off for off, u in src if u == uri or uri.endswith(u)), None)
            msg = f"link {uri} {prob}"
            if hit is not None:
                out.append(self.at(ctx, hit, msg))
            else:
                out.append(self.finding(ctx, msg, page=page + 1, quote=uri))
        for off, u in src:  # \url in the source that the PDF has no link for (e.g. nohyperref)
            if u not in seen and (prob := link_problem(u)) and not u.startswith("#"):
                seen.add(u)
                out.append(self.at(ctx, off, f"link {u} {prob}"))
        return out


@register
class Margins(Check):
    id = "pdf.margins"
    stage = 2
    requires = frozenset({"pdf"})
    severity = Severity.WARN
    why = "Content in the margins violates the template and may be cut off in the proceedings."

    def run(self, ctx):
        lay = _layout(ctx)
        if not lay:
            raise SkipCheck("no template layout (template.layout in the config, or a build layout probe)")
        dpi = int(self.opt(ctx, "dpi", 72))
        tol = float(self.opt(ctx, "tolerance_bp", 3.0))
        min_px = int(self.opt(ctx, "min_pixels", 6))
        allow_ln = ctx.mode == "submission" and bool(self.opt(ctx, "allow_line_numbers_in_submission", True))
        scale = dpi / 72.0
        pt = 72.0 / 72.27
        head = (lay.get("headheight", 12.0) + lay.get("headsep", 12.0)) * pt
        foot = lay.get("footskip", 30.0) * pt + 6
        out = []
        pdf = ctx.pdf
        for i in range(pdf.page_count):
            tb = text_block(lay, i)
            if tb is None:
                raise SkipCheck("template layout is incomplete")
            img = pdf.render_gray(i, dpi)
            ink = img < 180
            h, w = ink.shape
            allowed = np.zeros_like(ink)

            def allow(x0, y0, x1, y1):
                a, b = max(0, int((x0 - tol) * scale)), min(w, int(np.ceil((x1 + tol) * scale)))
                c, d = max(0, int((y0 - tol) * scale)), min(h, int(np.ceil((y1 + tol) * scale)))
                allowed[c:d, a:b] = True

            x0, y0, x1, y1 = tb
            allow(x0, y0, x1, y1)
            allow(x0, y0 - head, x1, y0)  # running header
            allow(x0, y1, x1, y1 + foot)  # footer / page number
            if allow_ln:
                allow(0, y0, x0, y1)
                allow(x1, y0, w / scale, y1)
            outside = ink & ~allowed
            if outside.sum() < min_px:
                continue
            ys, xs = np.nonzero(outside)
            regions = {
                "left margin": xs < x0 * scale, "right margin": xs > x1 * scale,
                "top margin": (ys < y0 * scale) & (xs >= x0 * scale) & (xs <= x1 * scale),
                "bottom margin": (ys > y1 * scale) & (xs >= x0 * scale) & (xs <= x1 * scale),
            }
            for side, sel in regions.items():
                if sel.sum() < min_px:
                    continue
                bx0, bx1 = xs[sel].min() / scale, (xs[sel].max() + 1) / scale
                by0, by1 = ys[sel].min() / scale, (ys[sel].max() + 1) / scale
                depth = {"left margin": x0 - bx0, "right margin": bx1 - x1,
                         "top margin": y0 - by0, "bottom margin": by1 - y1}[side]
                text = pdf.text_in(i, (bx0, by0, bx1, by1))[:120]
                out.append(self.finding(ctx, f"ink {depth:.0f}bp into the {side} on page {i + 1} "
                                             f"(box {bx0:.0f},{by0:.0f}-{bx1:.0f},{by1:.0f} bp)",
                                        page=i + 1, quote=text,
                                        instructions="Shrink or move the element so it stays inside the text block."))
        return out
