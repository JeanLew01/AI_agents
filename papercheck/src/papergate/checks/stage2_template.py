"""Stage 2: template integrity (official file unmodified, layout unchanged, no layout hacks)."""

from __future__ import annotations

import difflib
import hashlib
import re
from pathlib import Path

from ..models import Severity
from ..registry import Check, SkipCheck, register
from ..tex.source import SourceFile


def _sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


@register
class TemplateFile(Check):
    id = "template.file"
    stage = 2
    severity = Severity.BLOCKER
    why = "Venues require the official template, unmodified."

    def run(self, ctx):
        spec = ctx.config.template
        if not spec.file:
            raise SkipCheck("no template.file in the venue config")
        stem = Path(spec.file).stem
        pre = ctx.project.preamble
        used = re.search(r"\\(?:usepackage|documentclass|RequirePackage)\s*(?:\[[^\]]*\])?\s*\{[^}]*\b"
                         + re.escape(stem) + r"\b[^}]*\}", pre)
        out = []
        if not used:
            out.append(self.finding(ctx, f"the paper does not load the official template {spec.file}",
                                    file=ctx.project.main, line=1,
                                    quote=ctx.project.files[ctx.project.main].line_text(1).strip()))
        official_hash = spec.sha256
        official_text = None
        if spec.official_path and Path(spec.official_path).is_file():
            official_hash = official_hash or _sha256(Path(spec.official_path))
            official_text = Path(spec.official_path).read_text(errors="replace")
        copies = [p for p in ctx.paper_dir.rglob(spec.file) if ".git" not in p.parts]
        for p in copies:
            rel = p.relative_to(ctx.paper_dir).as_posix()
            if official_hash and _sha256(p) != official_hash:
                diff = ""
                if official_text is not None:
                    diff = "".join(difflib.unified_diff(official_text.splitlines(True), p.read_text(errors="replace").splitlines(True),
                                                        "official/" + spec.file, rel, n=1))[:3000]
                out.append(self.finding(ctx, f"{rel} differs from the official {spec.file} (sha256 mismatch)",
                                        file=rel, quote=spec.file,
                                        instructions="Replace it with the official file.\n" + diff))
        ctx.metrics["template"] = {"file": spec.file, "copies": [p.relative_to(ctx.paper_dir).as_posix() for p in copies],
                                   "used": bool(used)}
        return out


@register
class TemplateLayout(Check):
    id = "template.layout"
    stage = 2
    requires = frozenset({"build"})
    severity = Severity.BLOCKER
    why = "Changing the text block (margins, text height/width) violates the template."

    def run(self, ctx):
        expected = ctx.config.template.layout
        if not expected:
            raise SkipCheck("no template.layout in the venue config")
        got = ctx.build.layout
        if not got:
            raise SkipCheck("layout probe did not run")
        tol = ctx.config.template.layout_tolerance_pt
        diffs = [f"{k}: {got[k]:.2f}pt (template {v:.2f}pt)" for k, v in expected.items()
                 if k in got and abs(got[k] - v) > tol]
        if diffs:
            return [self.finding(ctx, "page layout differs from the template: " + "; ".join(diffs),
                                 file=ctx.project.main, quote=diffs[0].split(":")[0],
                                 instructions="Remove geometry/length changes from the preamble.")]
        return []


# (check id, severity, regex, message, why)
HACK_RULES = [
    ("template.geometry", Severity.BLOCKER,
     r"\\usepackage\s*(?:\[[^\]]*\])?\s*\{geometry\}|\\(?:new)?geometry\s*\{",
     "geometry changes the page layout", "Margins and text block are fixed by the template."),
    ("template.layout_length", Severity.BLOCKER,
     r"\\(?:setlength|addtolength)\s*\{?\s*\\(?:textheight|textwidth|oddsidemargin|evensidemargin|topmargin|"
     r"headheight|headsep|footskip|columnsep|hoffset|voffset|paperwidth|paperheight)\b|"
     r"\\(?:textheight|textwidth|oddsidemargin|topmargin|columnsep)\s*=",
     "a page-layout length is changed", "Margins and text block are fixed by the template."),
    ("template.linespread", Severity.BLOCKER,
     r"\\linespread\s*\{|\\renewcommand\s*\{?\s*\\baselinestretch|\\setstretch\s*\{|"
     r"\\usepackage\s*(?:\[[^\]]*\])?\s*\{setspace\}|\\(?:setlength|addtolength)\s*\{?\s*\\baselineskip",
     "line spacing is changed", "Squeezing line spacing violates the template."),
    ("template.fontsize", Severity.WARN,
     r"\\renewcommand\s*\{?\s*\\(?:normalsize|small|footnotesize|scriptsize|large)\b|\\fontsize\s*\{",
     "a font size is redefined", "Body and caption font sizes are fixed by the template."),
    ("template.caption_format", Severity.WARN,
     r"\\captionsetup\s*(?:\[[^\]]*\])?\s*\{[^}]*\b(?:font|labelfont|textfont|skip|aboveskip|belowskip|format|"
     r"labelsep|size|margin|width|justification|singlelinecheck|parskip|indention)\b|"
     r"\\usepackage\s*\[[^\]]*\b(?:font|labelfont|skip|size|margin|labelsep|format)\b[^\]]*\]\s*\{(?:sub)?caption\}|"
     r"\\(?:setlength|addtolength)\s*\{?\s*\\(?:abovecaptionskip|belowcaptionskip)",
     "caption format or spacing is changed", "Caption format is fixed by the template."),
    ("template.spacing", Severity.WARN,
     r"\\(?:setlength|addtolength)\s*\{?\s*\\(?:textfloatsep|floatsep|intextsep|dbltextfloatsep|dblfloatsep|"
     r"abovedisplayskip|belowdisplayskip|abovedisplayshortskip|belowdisplayshortskip|parskip|parsep|"
     r"itemsep|topsep)\b|\\titlespacing|\\enlargethispage",
     "float/paragraph/display spacing is changed", "Spacing hacks to gain room violate most templates."),
    ("template.negative_vspace", Severity.WARN,
     r"\\vspace\*?\s*\{\s*-|\\vskip\s*-|\\vspace\*?\s*\{\s*\\(?:dimexpr\s*)?-",
     "negative \\vspace", "Negative spacing to gain room violates most templates."),
]


def _scan_sources(ctx):
    """(text, locate) pairs: the flattened document plus project style files other than the template."""
    proj = ctx.project
    yield proj.flat, proj.locate, lambda off: proj.line_quote(off)
    tmpl = ctx.config.template.file
    for p in sorted(ctx.paper_dir.rglob("*")):
        if p.suffix not in (".sty", ".cls") or ".git" in p.parts or (tmpl and p.name == tmpl):
            continue
        rel = p.relative_to(ctx.paper_dir).as_posix()
        if not re.search(r"\\(?:usepackage|documentclass|RequirePackage)\s*(?:\[[^\]]*\])?\s*\{[^}]*\b"
                         + re.escape(p.stem) + r"\b", proj.flat):
            continue
        sf = SourceFile(rel, p.read_text(errors="replace"))
        yield sf.stripped, None, (lambda sf: (lambda off: (sf.rel, sf.line_of(off), sf.line_text(sf.line_of(off)).strip())))(sf)


def _make_rule(cid: str, sev: Severity, rx: str, msg: str, why_text: str):
    class _Rule(Check):
        id = cid
        stage = 2
        severity = sev
        why = why_text
        pattern = re.compile(rx)

        def run(self, ctx):
            out = []
            for text, _loc, quote_at in _scan_sources(ctx):
                for m in self.pattern.finditer(text):
                    file, line, q = quote_at(m.start())
                    out.append(self.finding(ctx, msg, file=file, line=line, quote=q,
                                            instructions="Remove it and fit the content by editing the text instead."))
            return out

    _Rule.__name__ = "Rule_" + cid.replace(".", "_")
    return register(_Rule)


for _r in HACK_RULES:
    _make_rule(*_r)
