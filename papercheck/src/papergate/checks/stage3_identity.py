"""Stage 3: identity checks. Camera-ready: final mode, real authors, metadata, acknowledgments,
no anonymisation leftovers. Shared: mode markers and required/forbidden sections."""

from __future__ import annotations

import re
import unicodedata

from ..config import Marker, SectionSpec
from ..models import Fix, Severity
from ..patching import edit_patch
from ..pdf.doc import text_block
from ..registry import Check, SkipCheck, register
from ..tex.source import find_commands, latex_to_text, prose_mask, read_group

CAMERA = ("camera-ready",)
SUBMISSION = ("submission",)
ACK_RX = r"acknowledge?ments?|acknowledge?ment|funding"


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    s = re.sub(r"[^a-z0-9@.\-\s]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


# ---- shared helpers --------------------------------------------------------------------

def usepackage_options(ctx, pkg: str, cmd: str = "usepackage"):
    """[(flat offset of command, option list, raw option string or None)] for \\usepackage[...]{pkg}."""
    out = []
    pre = ctx.project.preamble
    for start, _n, _star, opts, arg, _end in find_commands(pre, cmd):
        if pkg in [a.strip() for a in arg.split(",")]:
            raw = opts[0] if opts else None
            out.append((start, [o.strip() for o in raw.split(",")] if raw else [], raw))
    return out


def option_patch(ctx, pkg: str, option: str, add: bool, cmd: str = "usepackage"):
    """Patch adding/removing an option of \\usepackage{pkg} or \\documentclass{pkg}."""
    proj = ctx.project
    for start, opts, raw in usepackage_options(ctx, pkg, cmd):
        if not proj.same_segment(start, start + 200):
            continue
        rel, fstart = proj.file_offset(start)
        text = proj.files[rel].text
        m = re.compile(r"\\" + cmd + r"\s*(\[[^\]]*\])?\s*\{").match(text, fstart)
        if not m:
            continue
        if add:
            if m.group(1):
                inner = m.group(1)[1:-1].strip()
                new = "[" + (inner + "," if inner else "") + option + "]"
                return edit_patch(ctx.paper_dir, rel, [(m.start(1), m.end(1), new)])
            pos = fstart + len("\\" + cmd)
            return edit_patch(ctx.paper_dir, rel, [(pos, pos, f"[{option}]")])
        if m.group(1):
            keep = [o.strip() for o in m.group(1)[1:-1].split(",") if o.strip() and o.strip() != option]
            return edit_patch(ctx.paper_dir, rel, [(m.start(1), m.end(1), f"[{','.join(keep)}]" if keep else "")])
    return None


def pdf_text_norm(ctx) -> list[str]:
    if "pdf_pages_norm" not in ctx.cache:
        pages = []
        for i in range(ctx.pdf.page_count):
            t = ctx.pdf.page_text(i)
            t = re.sub(r"-\n(?=[a-z])", "", t)  # undo hyphenation at line ends
            pages.append(re.sub(r"\s+", " ", t))
        ctx.cache["pdf_pages_norm"] = pages
    return ctx.cache["pdf_pages_norm"]


def detect_line_numbers(ctx) -> list[int]:
    """1-based pages with a column of line numbers in a margin (lineno-style)."""
    pdf = ctx.pdf
    lay = ctx.config.template.layout or (ctx.build.layout if ctx.build else {})
    pages = []
    for i in range(pdf.page_count):
        w, _h = pdf.page_size(i)
        tb = text_block(lay, i) if lay else None
        left, right = (tb[0] - 2, tb[2] + 2) if tb else (0.12 * w, 0.88 * w)
        nums = [s for s in pdf.spans(i) if re.fullmatch(r"\d{1,4}", s["text"].strip())
                and (s["bbox"][2] < left or s["bbox"][0] > right)]
        if len(nums) >= 10:
            pages.append(i + 1)
    return pages


def marker_hits(ctx, m: Marker) -> list[dict]:
    """Evidence that a marker is present: [{'offset': flat offset} | {'page': n, 'text': ...}]."""
    if m.kind in ("package_option", "class_option"):
        cmd = "usepackage" if m.kind == "package_option" else "documentclass"
        return [{"offset": s} for s, opts, _raw in usepackage_options(ctx, m.package or "", cmd) if m.option in opts]
    if m.kind == "source_regex":
        return [{"offset": x.start()} for x in re.finditer(m.pattern or "", ctx.project.flat)]
    if ctx.pdf is None:
        return []
    if m.kind == "pdf_text":
        rx = re.compile(m.pattern or "", re.I)
        hits = []
        for i, t in enumerate(pdf_text_norm(ctx)):
            x = rx.search(t)
            if x:
                hits.append({"page": i + 1, "text": t[max(0, x.start() - 30):x.end() + 30].strip()})
        return hits
    if m.kind == "line_numbers":
        return [{"page": p, "text": "line numbers"} for p in detect_line_numbers(ctx)]
    return []


def _hit_finding(check, ctx, hit, msg, **kw):
    if "offset" in hit:
        return check.at(ctx, hit["offset"], msg, **kw)
    return check.finding(ctx, msg, page=hit.get("page"), quote=hit.get("text", ""), **kw)


@register
class FinalMarkers(Check):
    id = "identity.final_markers"
    stage = 3
    requires = frozenset({"pdf"})
    severity = Severity.BLOCKER

    def run(self, ctx):
        out = []
        for m in ctx.config.final_mode_markers:
            hits = marker_hits(ctx, m)
            if ctx.mode == "camera-ready" and not hits:
                fix = None
                if m.kind in ("package_option", "class_option"):
                    cmd = "usepackage" if m.kind == "package_option" else "documentclass"
                    patch = option_patch(ctx, m.package or "", m.option or "", add=True, cmd=cmd)
                    if patch:
                        fix = Fix(kind="patch", patch=patch, instructions=f"Add the [{m.option}] option.")
                loc = usepackage_options(ctx, m.package or "", "usepackage" if m.kind == "package_option" else "documentclass")
                msg = f"final-version marker missing: {m.label()}"
                why = "Without it the PDF is still the anonymous review version."
                if loc:
                    out.append(self.at(ctx, loc[0][0], msg, why=why, fix=fix))
                else:
                    out.append(self.finding(ctx, msg, why=why, fix=fix, file=ctx.project.main))
            elif ctx.mode == "submission":
                for h in hits:
                    out.append(_hit_finding(self, ctx, h, f"final-version marker present in a submission: {m.label()}",
                                            why="The final option de-anonymises the paper."))
        return out


@register
class ReviewMarkers(Check):
    id = "identity.review_markers"
    stage = 3
    requires = frozenset({"pdf"})
    severity = Severity.BLOCKER

    def run(self, ctx):
        out = []
        for m in ctx.config.review_mode_markers:
            hits = marker_hits(ctx, m)
            if ctx.mode == "camera-ready":
                for h in hits[:3]:
                    fix = None
                    if "offset" in h and m.kind == "source_regex":
                        file, line, q = ctx.project.line_quote(h["offset"])
                        if re.fullmatch(m.pattern or "", q.strip()):
                            from ..patching import delete_line_patch
                            p = delete_line_patch(ctx.paper_dir, file, line)
                            fix = Fix(kind="patch", patch=p, instructions="Delete the line.") if p else None
                    more = f" (and {len(hits) - 3} more)" if len(hits) > 3 and h is hits[2] else ""
                    out.append(_hit_finding(self, ctx, h, f"review-mode marker in the camera-ready version: {m.label()}{more}",
                                            why="The final PDF must not look like a review copy.", fix=fix))
            elif not hits and m.kind != "source_regex":
                out.append(self.finding(ctx, f"review-mode marker not found in the submission: {m.label()}",
                                        severity=Severity.WARN,
                                        why="Submissions are usually built in the template's review mode."))
        return out


def heading_present(ctx, spec: SectionSpec) -> dict | None:
    rx = re.compile(spec.pattern, re.I)
    prefix = re.compile(r"^(?:[0-9IVX]+|[A-Z])(?:\.\d+)*\.?\s+")

    def ok(title: str) -> bool:
        t = re.sub(r"[.:]\s*$", "", title.strip())
        return bool(rx.search(t) or rx.search(prefix.sub("", t)) or rx.search(t.replace(" ", "")))

    for s in ctx.project.sections:
        if ok(s.title):
            return {"offset": s.start}
    if ok("Acknowledgments"):
        for start, _n, _st, _o, arg, _e in find_commands(ctx.project.flat, r"acknowledgments|acknowledgements"):
            if start >= ctx.project.body_start and latex_to_text(arg):
                return {"offset": start}
    for e in ctx.project.envs_named("ack", "acks", "acknowledgments", "acknowledgements"):
        if ok("Acknowledgments"):
            return {"offset": e.start}
    if ctx.pdf is not None:
        for i in range(ctx.pdf.page_count):
            for ln in ctx.pdf.lines(i):
                if len(ln.text) < 60 and ok(ln.text):
                    return {"page": i + 1, "text": ln.text}
    return None


def pdf_heading(ctx, spec: SectionSpec) -> dict | None:
    if ctx.pdf is None:
        return None
    rx = re.compile(spec.pattern, re.I)
    prefix = re.compile(r"^(?:[0-9IVX]+|[A-Z])(?:\.\d+)*\.?\s+")
    for i in range(ctx.pdf.page_count):
        for ln in ctx.pdf.lines(i):
            t = re.sub(r"[.:]\s*$", "", ln.text.strip())
            if len(t) < 60 and (rx.search(prefix.sub("", t)) or rx.search(t.replace(" ", ""))):
                return {"page": i + 1, "text": ln.text}
    return None


@register
class RequiredSections(Check):
    id = "structure.required_sections"
    stage = 3
    severity = Severity.BLOCKER
    why = "The venue requires this section."

    def run(self, ctx):
        out = []
        for spec in ctx.config.sections_for("required", ctx.mode):
            if heading_present(ctx, spec) is None:
                out.append(self.finding(ctx, f"required section missing: {spec.name}", file=ctx.project.main,
                                        quote=spec.name, instructions=f"Add a '{spec.name}' section."))
        return out


@register
class ForbiddenSections(Check):
    id = "structure.forbidden_sections"
    stage = 3
    requires = frozenset({"pdf"})
    severity = Severity.BLOCKER
    why = "The venue forbids this section in this version (e.g. acknowledgments in an anonymous submission)."

    def run(self, ctx):
        out = []
        for spec in ctx.config.sections_for("forbidden", ctx.mode):
            hit = pdf_heading(ctx, spec)
            if hit:
                src = next((s for s in ctx.project.sections if re.search(spec.pattern, s.title, re.I)), None)
                msg = f"section not allowed in the {ctx.mode} version: {spec.name} (page {hit['page']})"
                if src:
                    out.append(self.at(ctx, src.start, msg))
                else:
                    out.append(self.finding(ctx, msg, page=hit["page"], quote=hit["text"]))
        return out


def _ack_spec_configured(ctx, which: str) -> bool:
    return any(re.search("acknowledg", s.pattern + s.name, re.I) for s in ctx.config.sections_for(which, ctx.mode))


@register
class Acknowledgments(Check):
    id = "identity.acknowledgments"
    stage = 3
    severity = Severity.WARN

    def run(self, ctx):
        spec = SectionSpec(name="Acknowledgments", pattern="^(?:" + ACK_RX + ")$")
        if ctx.mode == "camera-ready":
            if _ack_spec_configured(ctx, "required"):
                return []
            if heading_present(ctx, spec) is None and not re.search(r"\\thanks\{[^}]*(support|fund|grant)", ctx.project.flat, re.I):
                return [self.finding(ctx, "no acknowledgments/funding section", file=ctx.project.main,
                                     why="Funding agencies usually require acknowledgment in the final version.",
                                     instructions="Add acknowledgments (the template's \\acknowledgments{} or a starred section).")]
            return []
        if _ack_spec_configured(ctx, "forbidden") or ctx.pdf is None:
            return []
        hit = pdf_heading(ctx, spec)
        if hit:
            return [self.finding(ctx, f"acknowledgments appear in the anonymous submission (page {hit['page']})",
                                 severity=Severity.BLOCKER, page=hit["page"], quote=hit["text"],
                                 why="Acknowledgments and funding information identify the authors.")]
        return []


PLACEHOLDER_RX = re.compile(
    r"\banonymous\b|\bauthor\s*\(s\)|\bauthor names? (?:omitted|hidden)|\b(?:first|second|third) author\b|"
    r"\bfirst\s*name\s+last\s*name\b|\bname\s+surname\b|\byour name\b|\bemail@(?:domain|example)\b|"
    r"\binstitution\b(?:\s+name)?\s*$|\baffiliation\s*\d*\s*$", re.I)


@register
class PlaceholderAuthors(Check):
    id = "identity.placeholder_authors"
    stage = 3
    applies_to_modes = CAMERA
    severity = Severity.BLOCKER
    why = "The camera-ready version must show the real author list."

    def run(self, ctx):
        out = []
        flat = ctx.project.flat
        for start, name, _st, _o, arg, end in find_commands(flat, r"author|IEEEauthorblockN|IEEEauthorblockA|affiliation|institute"):
            arg_start = end - len(arg) - 1
            for m in PLACEHOLDER_RX.finditer(arg):
                out.append(self.at(ctx, arg_start + m.start(), f"placeholder author text '{m.group(0)}'"))
        if out or ctx.pdf is None:
            return out
        header = first_page_header(ctx)
        m = PLACEHOLDER_RX.search(header)
        if m:
            out.append(self.finding(ctx, f"first page shows placeholder author text '{m.group(0)}'", page=1,
                                    quote=header[max(0, m.start() - 20):m.end() + 20]))
        return out


def first_page_header(ctx) -> str:
    """Text of page 1 above the abstract (title and author block)."""
    lines = ctx.pdf.lines(0)
    out = []
    for ln in lines:
        if re.match(r"^\s*(abstract|a b s t r a c t)\b", ln.text, re.I) or ln.text.startswith("Abstract"):
            break
        out.append(ln.text)
    if len(out) == len(lines):  # no abstract heading: top 40% of the page
        h = ctx.pdf.page_size(0)[1]
        out = [ln.text for ln in lines if ln.bbox[1] < 0.4 * h]
    return "\n".join(out)


def _author_cmd_offset(ctx) -> int | None:
    for start, *_ in find_commands(ctx.project.flat, r"author|IEEEauthorblockN"):
        return start
    return None


@register
class AuthorList(Check):
    id = "identity.author_list"
    stage = 3
    applies_to_modes = CAMERA
    requires = frozenset({"pdf"})
    severity = Severity.BLOCKER
    why = "The published author list must match the accepted paper's canonical list exactly."

    def run(self, ctx):
        authors = ctx.config.authors
        if not authors:
            raise SkipCheck("no canonical author list in the config (authors:)")
        header = first_page_header(ctx)
        hn = norm(header)
        off = _author_cmd_offset(ctx)

        def mk(msg, sev=None, instructions=""):
            if off is not None:
                return self.at(ctx, off, msg, severity=sev, instructions=instructions)
            return self.finding(ctx, msg, page=1, severity=sev, instructions=instructions)

        out = []
        found = []
        for a in authors:
            n = norm(a.name)
            pos = hn.find(n)
            if pos < 0:
                last = n.split()[-1]
                m = re.search(r"\b" + re.escape(last) + r"\b", hn)
                if m:
                    ctxs = hn[max(0, m.start() - 25):m.end()]
                    out.append(mk(f"author '{a.name}' not found verbatim on the first page (found '{ctxs.strip()}')",
                                  Severity.BLOCKER, "Use exactly the canonical spelling."))
                    found.append((m.start(), a.name))
                else:
                    out.append(mk(f"author '{a.name}' missing from the first page", Severity.BLOCKER))
                continue
            found.append((pos, a.name))
        order_pdf = [n for _p, n in sorted(found)]
        order_cfg = [a.name for a in authors if a.name in order_pdf]
        if order_pdf != order_cfg:
            out.append(mk(f"author order differs: PDF has {', '.join(order_pdf)}; canonical order is {', '.join(order_cfg)}",
                          instructions="Reorder the author block to match the canonical list."))
        missing = {a.name for a in authors if a.name not in order_pdf}
        for a in authors:
            if a.name in missing:
                continue
            for aff in a.affiliations:
                if norm(aff) not in hn:
                    out.append(mk(f"affiliation '{aff}' of {a.name} not found on the first page", Severity.WARN))
            if a.email:
                local, _, dom = a.email.lower().partition("@")
                if a.email.lower() not in hn and not (local in hn and dom in hn):
                    out.append(mk(f"email '{a.email}' of {a.name} not found on the first page", Severity.WARN))
        return out


def hypersetup_patch(ctx, title: str | None, author: str | None) -> str | None:
    proj = ctx.project
    pre = proj.preamble
    keys = {k: v for k, v in (("pdftitle", title), ("pdfauthor", author)) if v}
    hs = list(find_commands(pre, "hypersetup"))
    if hs:
        start, _n, _s, _o, arg, end = hs[0]
        rel, fstart = proj.file_offset(start)
        if not proj.same_segment(start, end):
            return None
        text = proj.files[rel].text
        body_start = text.index("{", fstart) + 1
        body = text[body_start:body_start + len(arg)]
        edits = []
        for k, v in keys.items():
            m = re.search(k + r"\s*=\s*", body)
            if m:
                g = read_group(body, m.end())
                vend = g[1] if g else (body.find(",", m.end()) if "," in body[m.end():] else len(body))
                edits.append((body_start + m.end(), body_start + vend, "{" + v + "}"))
            else:
                edits.append((body_start, body_start, f"{k}={{{v}}},"))
        return edit_patch(ctx.paper_dir, rel, edits)
    setup = "\\hypersetup{" + ",".join(f"{k}={{{v}}}" for k, v in keys.items()) + "}"
    for start, opts, _raw in usepackage_options(ctx, "hyperref"):
        rel, fstart = proj.file_offset(start)
        text = proj.files[rel].text
        eol = text.find("\n", fstart)
        eol = len(text) if eol < 0 else eol
        return edit_patch(ctx.paper_dir, rel, [(eol, eol, "\n" + setup)])
    # hyperref loaded by the template (or not at all): set the keys just before \begin{document}
    m = re.search(r"\\begin\{document\}", proj.flat)
    if m and proj.same_segment(m.start(), m.end()):
        rel, fstart = proj.file_offset(m.start())
        return edit_patch(ctx.paper_dir, rel, [(fstart, fstart, "\\ifdefined\\hypersetup" + setup + "\\fi\n")])
    return None


@register
class PdfMetadata(Check):
    id = "identity.pdf_metadata"
    stage = 3
    applies_to_modes = CAMERA
    requires = frozenset({"pdf"})
    severity = Severity.WARN
    why = "Indexing services and the proceedings use the PDF Title/Author metadata."

    def run(self, ctx):
        md = ctx.pdf.metadata
        want_title = ctx.config.title or ctx.project.title
        want_authors = [a.name for a in ctx.config.authors]
        problems = []
        sev = Severity.WARN
        if not md.get("title", "").strip():
            problems.append("Title is empty")
        elif want_title and norm(md["title"]) != norm(want_title):
            problems.append(f"Title is '{md['title']}' (expected '{want_title}')")
        a = md.get("author", "")
        if not a.strip():
            problems.append("Author is empty")
        elif re.search(r"anonymous", a, re.I):
            problems.append(f"Author is '{a}'")
            sev = Severity.BLOCKER
        elif want_authors:
            pos = [norm(a).find(norm(n)) for n in want_authors]
            if any(p < 0 for p in pos) or pos != sorted(pos):
                problems.append(f"Author is '{a}' (expected {', '.join(want_authors)})")
        if not problems:
            return []
        patch = hypersetup_patch(ctx, want_title if any(p.startswith("Title") for p in problems) else None,
                                 ", ".join(want_authors) if want_authors and any(p.startswith("Author") for p in problems) else None)
        fix = Fix(kind="patch", patch=patch, instructions="Set pdftitle/pdfauthor via \\hypersetup.") if patch else \
            Fix(kind="manual", instructions="Set pdftitle and pdfauthor with \\hypersetup (load hyperref) or the venue's metadata mechanism.")
        hs = list(find_commands(ctx.project.preamble, "hypersetup"))
        msg = "PDF metadata: " + "; ".join(problems)
        if hs:
            return [self.at(ctx, hs[0][0], msg, severity=sev, fix=fix)]
        return [self.finding(ctx, msg, severity=sev, file=ctx.project.main, quote="pdfinfo", fix=fix)]


ANON_CITE_RX = re.compile(
    r"\[\s*anonymous|\banonymous\s*(?:et al\.?|,?\s*\(?\d{4}\)?)|anonymi[sz]ed\s+for\s+(?:review|submission|blind)|"
    r"omitted\s+for\s+(?:anonymity|(?:double[- ])?blind\s+review|review)|"
    r"(?:reference|citation|link|url)s?\s+(?:removed|redacted|hidden)\s+for", re.I)


def bib_entries(ctx):
    """Parsed bibliography entries: list of dicts with ID, ENTRYTYPE, fields, plus _file and _line."""
    if "bib_entries" in ctx.cache:
        return ctx.cache["bib_entries"]
    import bibtexparser
    from bibtexparser.bparser import BibTexParser

    out = []
    for rel in ctx.project.bib_files:
        text = (ctx.paper_dir / rel).read_text(encoding="utf-8", errors="replace")
        parser = BibTexParser(common_strings=True, ignore_nonstandard_types=False)
        parser.homogenize_fields = False
        try:
            db = bibtexparser.loads(text, parser=parser)
        except Exception:
            continue
        for e in db.entries:
            m = re.search(r"@\w+\s*[{(]\s*" + re.escape(e["ID"]) + r"\s*,", text)
            line = text.count("\n", 0, m.start()) + 1 if m else None
            out.append({**{k.lower(): v for k, v in e.items()}, "ID": e["ID"], "_file": rel, "_line": line,
                        "_quote": text.splitlines()[line - 1].strip() if line else e["ID"]})
    ctx.cache["bib_entries"] = out
    return out


@register
class AnonymousSelfCitations(Check):
    id = "identity.anonymous_selfcite"
    stage = 3
    applies_to_modes = CAMERA
    severity = Severity.BLOCKER
    why = "Anonymised self-citations must be restored in the final version."

    def run(self, ctx):
        out = []
        cited = ctx.project.cited_keys
        for e in bib_entries(ctx):
            if e["ID"] not in cited and "*" not in cited:
                continue
            if re.search(r"\banonymous\b", e.get("author", ""), re.I) or re.search(r"anonymi[sz]ed", e.get("title", ""), re.I):
                out.append(self.finding(ctx, f"bibliography entry '{e['ID']}' is still anonymised", file=e["_file"],
                                        line=e["_line"], quote=e["_quote"],
                                        instructions="Restore the real authors/title of the self-citation."))
        masked = prose_mask(ctx.project.flat)
        for m in ANON_CITE_RX.finditer(masked):
            out.append(self.at(ctx, m.start(), f"anonymisation leftover '{m.group(0).strip()}'"))
        if not out and ctx.pdf is not None:
            for i, t in enumerate(pdf_text_norm(ctx)):
                m = ANON_CITE_RX.search(t)
                if m:
                    out.append(self.finding(ctx, f"anonymisation leftover in the PDF: '{m.group(0)}'", page=i + 1,
                                            quote=t[max(0, m.start() - 30):m.end() + 30]))
        return out


@register
class AnonymizedLinks(Check):
    id = "identity.anonymized_links"
    stage = 3
    applies_to_modes = CAMERA
    severity = Severity.BLOCKER
    why = "Anonymisation-service links expire; the final version must link to the real code/data."

    def run(self, ctx):
        services = [s.lower() for s in ctx.config.anonymization_services]
        out = []
        seen = set()
        for start, _n, _s, _o, arg, _e in find_commands(ctx.project.flat, r"url|href"):
            if any(s in arg.lower() for s in services):
                seen.add(arg.strip())
                out.append(self.at(ctx, start, f"link to an anonymisation service: {arg.strip()}",
                                   instructions="Replace it with the de-anonymised repository/project URL."))
        for e in bib_entries(ctx):
            for fld in ("url", "howpublished", "note"):
                v = e.get(fld, "")
                if any(s in v.lower() for s in services):
                    out.append(self.finding(ctx, f"bibliography entry '{e['ID']}' links to an anonymisation service",
                                            file=e["_file"], line=e["_line"], quote=e["_quote"]))
        if ctx.pdf is not None:
            for page, uri, _r in ctx.pdf.uri_links():
                if uri not in seen and any(s in uri.lower() for s in services):
                    seen.add(uri)
                    out.append(self.finding(ctx, f"PDF link to an anonymisation service: {uri}", page=page + 1, quote=uri))
        return out


@register
class AbstractLength(Check):
    id = "structure.abstract_length"
    stage = 3
    severity = Severity.WARN
    why = "The submission form (and some templates) cap the abstract length."

    def run(self, ctx):
        limit = ctx.config.abstract_limit(ctx.mode)
        rng = ctx.project.abstract_range
        if not limit or not rng:
            return []
        words = len(latex_to_text(ctx.project.flat[rng[0]:rng[1]]).split())
        ctx.metrics["abstract_words"] = words
        if words > limit:
            return [self.at(ctx, rng[0], f"abstract has {words} words, limit is {limit}",
                            instructions="Shorten the abstract (the PDF and the submission form should match).")]
        return []
