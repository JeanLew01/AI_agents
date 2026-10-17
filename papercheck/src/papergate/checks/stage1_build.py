"""Stage 1: clean build in a temporary copy, log, BibTeX/Biber and chktex findings."""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

from ..models import Severity
from ..registry import Check, SkipCheck, register
from ..tex.logparse import parse_blg, parse_log


def parsed_log(ctx):
    if "log" not in ctx.cache:
        ctx.cache["log"] = parse_log(ctx.build.log_text()) if ctx.build else None
    return ctx.cache["log"]


def _source_line(ctx, file: str | None, line: int | None) -> str:
    if file and line and file in ctx.project.files:
        return ctx.project.files[file].line_text(line).strip()
    return ""


@register
class BuildErrors(Check):
    id = "build.errors"
    stage = 1
    requires = frozenset({"build"})
    severity = Severity.BLOCKER
    why = "The paper must compile cleanly; errors mean missing or wrong output in the PDF."

    def run(self, ctx):
        b = ctx.build
        out = []
        if b.timed_out:
            out.append(self.finding(ctx, "latexmk timed out", instructions="Raise checks.build.timeout_s or fix the loop."))
        log = parsed_log(ctx)
        for e in log.errors:
            quote = _source_line(ctx, e.file, e.line) or e.context
            out.append(self.finding(ctx, f"LaTeX error: {e.message}", file=e.file, line=e.line, quote=quote))
        if b.pdf is None:
            out.append(self.finding(ctx, "the build produced no PDF",
                                    instructions="Compile locally and fix the first error in the log.\n" + b.output_tail[-1500:]))
        elif b.returncode != 0 and not log.errors:
            out.append(self.finding(ctx, f"latexmk exited with code {b.returncode}", severity=Severity.WARN,
                                    instructions=b.output_tail[-1500:]))
        return out


def _ref_occurrences(ctx, key: str, cites: bool):
    items = ctx.project.cites if cites else ctx.project.refs
    return [it for it in items if key in it.keys]


@register
class UndefinedRefs(Check):
    id = "build.undefined_ref"
    stage = 1
    requires = frozenset({"build"})
    severity = Severity.BLOCKER
    why = "Undefined references print as '??' in the PDF."

    def run(self, ctx):
        out = []
        for key in parsed_log(ctx).undefined_refs:
            occ = _ref_occurrences(ctx, key, cites=False)
            if not occ:
                out.append(self.finding(ctx, f"undefined reference '{key}'", quote=key))
            for r in occ:
                out.append(self.at(ctx, r.start, f"undefined reference '{key}' (no \\label{{{key}}})",
                                   instructions=f"Add \\label{{{key}}} to the intended target or fix the key."))
        return out


@register
class UndefinedCitations(Check):
    id = "build.undefined_citation"
    stage = 1
    requires = frozenset({"build"})
    severity = Severity.BLOCKER
    why = "Undefined citations print as '[?]' in the PDF."

    def run(self, ctx):
        out = []
        for key in parsed_log(ctx).undefined_cites:
            occ = _ref_occurrences(ctx, key, cites=True)
            if not occ:
                out.append(self.finding(ctx, f"undefined citation '{key}'", quote=key))
            for c in occ:
                out.append(self.at(ctx, c.start, f"undefined citation '{key}' (not in any .bib file)",
                                   instructions="Add the entry to the bibliography or fix the key."))
        return out


@register
class MultiplyDefinedLabels(Check):
    id = "build.multiply_defined_label"
    stage = 1
    requires = frozenset({"build"})
    severity = Severity.WARN
    why = "References to a duplicated label may point to the wrong object."

    def run(self, ctx):
        out = []
        for key in parsed_log(ctx).multiply_defined:
            for lab in [l for l in ctx.project.labels if l.key == key]:
                out.append(self.at(ctx, lab.start, f"label '{key}' is defined more than once"))
        return out


@register
class LabelsChanged(Check):
    id = "build.labels_changed"
    stage = 1
    requires = frozenset({"build"})
    severity = Severity.WARN
    why = "Cross-references in the final PDF may be stale."

    def run(self, ctx):
        if parsed_log(ctx).labels_changed:
            return [self.finding(ctx, "'Label(s) may have changed' remains after the final latexmk pass",
                                 instructions="Look for labels whose page depends on themselves (e.g. \\pageref loops).")]
        return []


@register
class OverfullBoxes(Check):
    id = "build.overfull_hbox"
    stage = 1
    requires = frozenset({"build"})
    severity = Severity.WARN
    why = "Text running into the margin is visible and may violate the template."

    def run(self, ctx):
        thr = float(self.opt(ctx, "overfull_threshold_pt", 2.0))
        out = []
        for b in parsed_log(ctx).boxes:
            if b.kind != "Overfull" or b.box != "h" or b.amount_pt <= thr:
                continue
            quote = _source_line(ctx, b.file, b.line)
            out.append(self.finding(ctx, f"overfull \\hbox, {b.amount_pt:.1f}pt too wide", file=b.file,
                                    line=b.line, quote=quote or b.context[:120],
                                    instructions="Rephrase, allow hyphenation, or shrink the offending box."))
        return out


def _bib_entry_location(ctx, key: str):
    for bib in ctx.project.bib_files:
        text = (ctx.paper_dir / bib).read_text(encoding="utf-8", errors="replace")
        m = re.search(r"@\w+\s*[{(]\s*" + re.escape(key) + r"\s*,", text)
        if m:
            line = text.count("\n", 0, m.start()) + 1
            return bib, line, text.splitlines()[line - 1].strip()
    return None, None, ""


@register
class BibWarnings(Check):
    id = "build.bibtex"
    stage = 1
    requires = frozenset({"build"})
    severity = Severity.WARN
    why = "BibTeX/Biber problems produce incomplete or malformed reference entries."

    def run(self, ctx):
        out = []
        for blg in ctx.build.bib_logs():
            for msg in parse_blg(blg.read_text(encoding="utf-8", errors="replace")):
                if msg.key and "didn't find a database entry" in msg.message:
                    continue  # reported as build.undefined_citation
                file, line, quote = (None, None, "")
                if msg.key:
                    file, line, quote = _bib_entry_location(ctx, msg.key)
                if file is None and msg.bibfile:
                    file, line = Path(msg.bibfile).name, msg.line
                    rel = next((b for b in ctx.project.bib_files if Path(b).name == file), None)
                    if rel and line:
                        file = rel
                        quote = (ctx.paper_dir / rel).read_text(errors="replace").splitlines()[line - 1].strip()
                sev = Severity.BLOCKER if msg.level == "error" else Severity.WARN
                out.append(self.finding(ctx, f"{blg.suffix[1:]} {msg.level}: {msg.message}", severity=sev,
                                        file=file, line=line, quote=quote or (msg.key or "")))
        return out


DEFAULT_CHKTEX = [1, 2, 8, 9, 10, 11, 12, 13, 17, 26, 36, 44]


@register
class Chktex(Check):
    id = "build.chktex"
    stage = 1
    requires = frozenset({"build"})
    severity = Severity.INFO
    why = "chktex flags typographic slips (spacing, dashes, quotes) that reviewers notice."

    def run(self, ctx):
        exe = shutil.which("chktex")
        if not exe:
            raise SkipCheck("chktex is not installed (sudo apt install chktex)")
        counted = set(self.opt(ctx, "counted_warnings", DEFAULT_CHKTEX))
        sev = Severity(self.opt(ctx, "severity", "INFO"))
        out = []
        for rel in ctx.project.order:
            proc = subprocess.run([exe, "-q", "-v0", "-I0", "-f", "%f:%l:%c:%n:%m\n", rel],
                                  cwd=ctx.build.srcdir, capture_output=True, text=True, errors="replace")
            for ln in proc.stdout.splitlines():
                m = re.match(r"(.+?):(\d+):(\d+):(\d+):(.*)", ln)
                if not m or int(m.group(4)) not in counted:
                    continue
                line = int(m.group(2))
                out.append(self.finding(ctx, f"chktex {m.group(4)}: {m.group(5).strip()}", severity=sev,
                                        file=rel, line=line, quote=_source_line(ctx, rel, line)))
        return out
