"""Stage 3, submission mode: nothing in the source, PDF, metadata, figures or supplementary
material may identify the authors."""

from __future__ import annotations

import io
import json
import re
import tarfile
import zipfile
from pathlib import Path

import pymupdf

from ..models import Severity
from ..registry import Check, SkipCheck, register
from ..tex.project import TEXT_EXTS
from ..tex.source import SourceFile, find_commands, prose_mask
from .stage3_identity import pdf_text_norm

SUBMISSION = ("submission",)
HIDDEN_BY_TEMPLATE = r"author|thanks|IEEEauthorblockN|IEEEauthorblockA|affiliation|affil|email|institute|address|corresp"
ABS_PATH_RX = re.compile(r"(?:/home/|/Users/|/mnt/[a-z]/Users/|[A-Za-z]:\\\\?Users\\\\?)([A-Za-z0-9._-]+)")


def term_rx(ctx) -> re.Pattern | None:
    terms = [t for t in ctx.config.identity_terms if t.strip()]
    if not terms:
        return None
    alts = sorted((re.escape(t.strip()).replace(r"\ ", r"\s+") for t in terms), key=len, reverse=True)
    return re.compile(r"(?<![A-Za-z0-9])(?:" + "|".join(alts) + r")(?![A-Za-z0-9])", re.I)


def _hidden_ranges(sf: SourceFile) -> list[tuple[int, int]]:
    return [(s, e) for s, _n, _st, _o, _a, e in find_commands(sf.stripped, HIDDEN_BY_TEMPLATE)]


def _context(text: str, a: int, b: int, w: int = 40) -> str:
    return re.sub(r"\s+", " ", text[max(0, a - w):b + w]).strip()


@register
class IdentitySource(Check):
    id = "identity.terms_source"
    stage = 3
    applies_to_modes = SUBMISSION
    severity = Severity.WARN
    why = "Identity terms in the source leak if the source is shared (supplementary material, arXiv)."

    def run(self, ctx):
        rx = term_rx(ctx)
        if rx is None:
            raise SkipCheck("no identity_terms in the config")
        out = []
        proj = ctx.project
        tmpl = ctx.config.template.file
        included = set(proj.order)
        for p in proj.all_text_files():
            rel = p.relative_to(ctx.paper_dir).as_posix()
            if p.suffix in (".bib", ".bbl", ".bst") or (tmpl and p.name == tmpl) or p.stat().st_size > 5_000_000:
                continue
            sf = proj.files.get(rel) or SourceFile(rel, p.read_text(encoding="utf-8", errors="replace"))
            is_tex = p.suffix == ".tex"
            hidden = _hidden_ranges(sf) if is_tex else []
            for m in rx.finditer(sf.text):
                in_comment = is_tex and not sf.stripped[m.start():m.end()].strip()
                if any(a <= m.start() < b for a, b in hidden):
                    continue
                visible = is_tex and rel in included and not in_comment
                if visible and ctx.pdf is not None:
                    continue  # reported with a BLOCKER by identity.terms_pdf
                line = sf.line_of(m.start())
                where = "a comment" if in_comment else ("a file not included in the paper" if is_tex and rel not in included
                                                        else ("the paper text" if visible else "a supplementary source file"))
                out.append(self.finding(ctx, f"identity term '{m.group(0)}' in {where}", file=rel, line=line,
                                        quote=sf.line_text(line).strip(),
                                        severity=Severity.BLOCKER if visible else Severity.WARN,
                                        instructions="Remove or anonymise it."))
            for m in ABS_PATH_RX.finditer(sf.text):
                line = sf.line_of(m.start())
                out.append(self.finding(ctx, f"absolute path with a user name ('{m.group(0)}')", file=rel, line=line,
                                        quote=sf.line_text(line).strip(), instructions="Use a relative path."))
        return out


@register
class IdentityPdf(Check):
    id = "identity.terms_pdf"
    stage = 3
    applies_to_modes = SUBMISSION
    requires = frozenset({"pdf"})
    severity = Severity.BLOCKER
    why = "The anonymous PDF must not identify the authors (text, metadata or XMP)."

    def run(self, ctx):
        rx = term_rx(ctx)
        if rx is None:
            raise SkipCheck("no identity_terms in the config")
        out = []
        proj = ctx.project
        located = set()
        # visible occurrences in the included source, if they made it into the PDF text
        pdf_all = " ".join(pdf_text_norm(ctx)).lower()
        for rel in proj.order:
            sf = proj.files[rel]
            hidden = _hidden_ranges(sf)
            for m in rx.finditer(sf.stripped):
                if any(a <= m.start() < b for a, b in hidden):
                    continue
                term = re.sub(r"\s+", " ", m.group(0)).lower()
                if term in pdf_all:
                    located.add(term)
                    line = sf.line_of(m.start())
                    out.append(self.finding(ctx, f"identity term '{m.group(0)}' appears in the PDF text", file=rel,
                                            line=line, quote=sf.line_text(line).strip(),
                                            instructions="Remove it or rephrase in the third person."))
        for i, t in enumerate(pdf_text_norm(ctx)):
            for m in rx.finditer(t):
                if re.sub(r"\s+", " ", m.group(0)).lower() in located:
                    continue
                out.append(self.finding(ctx, f"identity term '{m.group(0)}' on page {i + 1}", page=i + 1,
                                        quote=_context(t, m.start(), m.end())))
        for key, val in ctx.pdf.metadata.items():
            for m in rx.finditer(val or ""):
                out.append(self.finding(ctx, f"identity term '{m.group(0)}' in PDF metadata field {key}",
                                        quote=f"{key}: {val}",
                                        instructions="Clear pdfauthor/pdftitle-related fields (e.g. \\hypersetup{pdfauthor={}}) for the submission."))
        xmp = ctx.pdf.xmp
        for m in rx.finditer(xmp):
            out.append(self.finding(ctx, f"identity term '{m.group(0)}' in the PDF's XMP metadata",
                                    quote=_context(xmp, m.start(), m.end())))
        return out


def _image_metadata_text(path: Path) -> str:
    suf = path.suffix.lower()
    parts = []
    if suf == ".pdf":
        try:
            d = pymupdf.open(str(path))
            parts += [f"{k}: {v}" for k, v in (d.metadata or {}).items() if v]
            parts.append(d.get_xml_metadata() or "")
            d.close()
        except Exception:
            pass
    elif suf in (".png", ".jpg", ".jpeg", ".tif", ".tiff"):
        try:
            from PIL import Image

            with Image.open(path) as im:
                for k, v in (im.info or {}).items():
                    if isinstance(v, (str, bytes)):
                        parts.append(f"{k}: {v.decode('utf-8', 'replace') if isinstance(v, bytes) else v}")
                for tag, v in im.getexif().items():
                    if isinstance(v, (str, bytes)):
                        parts.append(f"exif{tag}: {v.decode('utf-16-le', 'replace') if isinstance(v, bytes) else v}")
        except Exception:
            pass
    elif suf in (".eps", ".ps", ".svg"):
        parts.append(path.read_text(errors="replace")[:20000])
    return "\n".join(parts)


@register
class IdentityFigures(Check):
    id = "identity.terms_figures"
    stage = 3
    applies_to_modes = SUBMISSION
    severity = Severity.BLOCKER
    why = "Figure files carry metadata (author, creator paths) into the submission PDF."

    def run(self, ctx):
        rx = term_rx(ctx)
        out = []
        seen = set()
        for off, _name, rel in ctx.project.graphics:
            if not rel or rel in seen:
                continue
            seen.add(rel)
            meta = _image_metadata_text(ctx.paper_dir / rel)
            if rx:
                for m in rx.finditer(meta):
                    out.append(self.at(ctx, off, f"identity term '{m.group(0)}' in the metadata of {rel}",
                                       instructions="Strip the figure metadata (e.g. exiftool -all= / re-export)."))
            for m in ABS_PATH_RX.finditer(meta):
                out.append(self.at(ctx, off, f"absolute path '{m.group(0)}' in the metadata of {rel}",
                                   severity=Severity.WARN, instructions="Strip the figure metadata."))
        return out


SELF_CITE_RX = re.compile(
    r"\b(?:our|my)\s+(?:own\s+)?(?:prior|previous|earlier|recent|past|preliminary|conference|workshop)\s+"
    r"(?:work|paper|study|studies|results?|approach|method|version)s?\b|"
    r"\bin\s+our\s+(?:\w+\s+){0,2}(?:work|paper|study|article)\b|\bwe\s+(?:have\s+)?previously\s+\w+|"
    r"\b(?:extends|extending|builds on|building on)\s+our\b", re.I)


@register
class SelfCitationPhrasing(Check):
    id = "identity.self_citation_phrasing"
    stage = 3
    applies_to_modes = SUBMISSION
    severity = Severity.WARN
    why = "First-person references to prior work reveal the authors in a double-blind review."

    def run(self, ctx):
        masked = prose_mask(ctx.project.flat[: ctx.project.body_end])
        out = []
        for m in SELF_CITE_RX.finditer(masked):
            if m.start() >= ctx.project.body_start:
                out.append(self.at(ctx, m.start(), f"first-person self-citation '{re.sub(chr(10), ' ', m.group(0))}'",
                                   instructions="Cite your prior work in the third person ('Smith et al. [3] showed ...')."))
        return out


ARCHIVE_EXTS = (".zip", ".tar", ".tgz", ".tar.gz", ".ipynb")


def _iter_supp_members(path: Path):
    """Yield (member name, bytes or None) for a supplementary file/dir."""
    name = path.name.lower()
    if path.is_dir():
        for p in sorted(path.rglob("*")):
            rel = p.relative_to(path).as_posix()
            if p.is_dir():
                if p.name == ".git":
                    yield rel + "/", None
                continue
            yield rel, p.read_bytes() if p.stat().st_size < 2_000_000 else None
    elif name.endswith(".zip"):
        with zipfile.ZipFile(path) as z:
            for info in z.infolist():
                yield info.filename, z.read(info) if (not info.is_dir() and info.file_size < 2_000_000) else None
    elif name.endswith((".tar", ".tgz", ".tar.gz")):
        with tarfile.open(path) as t:
            for m in t.getmembers():
                data = None
                if m.isfile() and m.size < 2_000_000:
                    f = t.extractfile(m)
                    data = f.read() if f else None
                yield m.name, data
    else:
        yield path.name, path.read_bytes() if path.stat().st_size < 20_000_000 else None


def _notebook_text(data: bytes) -> str:
    try:
        nb = json.loads(data)
    except Exception:
        return data.decode("utf-8", "replace")
    parts = [json.dumps(nb.get("metadata", {}))]
    for c in nb.get("cells", []):
        parts.append("".join(c.get("source", [])) if isinstance(c.get("source"), list) else str(c.get("source", "")))
        for o in c.get("outputs", []):
            parts.append(json.dumps(o)[:200000])
    return "\n".join(parts)


@register
class Supplementary(Check):
    id = "identity.supplementary"
    stage = 3
    applies_to_modes = SUBMISSION
    severity = Severity.BLOCKER
    why = "Supplementary archives often leak identity through .git history, paths or notebooks."

    def run(self, ctx):
        targets = list(ctx.options.supplementary)
        for p in ctx.paper_dir.rglob("*"):
            if ".git" not in p.relative_to(ctx.paper_dir).parts and p.is_file() and p.name.lower().endswith(ARCHIVE_EXTS):
                targets.append(p)
        if not targets:
            raise SkipCheck("no supplementary material (--supp) and no archives/notebooks in the paper dir")
        rx = term_rx(ctx)
        out = []
        for t in targets:
            label = t.name
            try:
                members = list(_iter_supp_members(t))
            except Exception as e:
                out.append(self.finding(ctx, f"cannot read supplementary file {label}: {e}", severity=Severity.WARN, quote=label))
                continue
            gitdirs = sorted({m.split(".git/")[0] + ".git" for m, _d in members if "/.git/" in "/" + m or m.startswith(".git")})
            for g in gitdirs[:5]:
                out.append(self.finding(ctx, f"{label} contains a git repository ({g})", quote=f"{label}:{g}",
                                        instructions="Remove .git directories; commit history names the authors."))
            for mname, data in members:
                if data is None:
                    continue
                low = mname.lower()
                if low.endswith((".png", ".jpg", ".jpeg", ".pdf", ".mp4", ".zip", ".gz", ".npz", ".npy", ".pt", ".pth", ".bin")):
                    continue
                text = _notebook_text(data) if low.endswith(".ipynb") else data.decode("utf-8", "replace")
                if rx:
                    for m in list(rx.finditer(text))[:3]:
                        out.append(self.finding(ctx, f"identity term '{m.group(0)}' in {label}:{mname}",
                                                quote=_context(text, m.start(), m.end())))
                for m in list(ABS_PATH_RX.finditer(text))[:2]:
                    out.append(self.finding(ctx, f"absolute path '{m.group(0)}' in {label}:{mname}", severity=Severity.WARN,
                                            quote=_context(text, m.start(), m.end()),
                                            instructions="Clear notebook outputs / use relative paths."))
        return out
