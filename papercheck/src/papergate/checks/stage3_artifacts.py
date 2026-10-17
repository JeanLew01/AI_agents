"""Stage 3: leftover editing artifacts (todo notes, highlights, coloured text, change marks,
NEW:/TODO markers, large commented-out blocks)."""

from __future__ import annotations

import re

from ..models import Fix, Severity
from ..patching import edit_patch
from ..registry import Check, register
from ..tex.source import find_commands, prose_mask, read_args
from .stage3_identity import usepackage_options

DEFAULT_COLORS = ["red", "magenta", "orange", "violet", "purple", "cyan"]


def _span_patch(ctx, start: int, end: int, replacement_from_arg: bool = False, arg_index: int = -1):
    """Patch removing the command at flat [start, end); if replacement_from_arg, keep the raw text
    of its last mandatory argument. Whole-line commands are removed with their line."""
    proj = ctx.project
    if not proj.same_segment(start, end):
        return None
    rel, fs = proj.file_offset(start)
    fe = fs + (end - start)
    text = proj.files[rel].text
    repl = ""
    if replacement_from_arg:
        r = read_args(text, fs + len(re.match(r"\\[A-Za-z@]+", text[fs:]).group(0)), 2 if arg_index == 1 else 1)
        if not r:
            return None
        repl = r[1][arg_index]
    else:
        ls = text.rfind("\n", 0, fs) + 1
        le = text.find("\n", fe)
        le = len(text) if le < 0 else le
        if text[ls:fs].strip() == "" and text[fe:le].strip() in ("", "%"):
            return edit_patch(ctx.paper_dir, rel, [(ls, min(le + 1, len(text)), "")])
    return edit_patch(ctx.paper_dir, rel, [(fs, fe, repl)])


def _body_commands(ctx, names: str):
    for start, name, star, opts, arg, end in find_commands(ctx.project.flat, names):
        if start >= ctx.project.body_start:
            yield start, name, star, opts, arg, end


@register
class TodoNotes(Check):
    id = "artifacts.todo"
    stage = 3
    severity = Severity.WARN
    why = "Todo notes left in the paper are visible to readers (and ship with the arXiv source)."

    def run(self, ctx):
        renders = any("disable" not in opts for _s, opts, _r in usepackage_options(ctx, "todonotes"))
        out = []
        for start, name, _st, _o, arg, end in _body_commands(ctx, r"todo|missingfigure|fxnote|fxwarning|fxerror|fxfatal"):
            patch = _span_patch(ctx, start, end)
            sev = Severity.BLOCKER if renders and name in ("todo", "missingfigure") else Severity.WARN
            out.append(self.at(ctx, start, f"\\{name} note: {arg.strip()[:80]}", severity=sev,
                               fix=Fix(kind="patch", patch=patch, instructions="Remove the note.") if patch else None))
        for m in re.finditer(r"\\listoftodos\b", ctx.project.flat):
            patch = _span_patch(ctx, m.start(), m.end())
            out.append(self.at(ctx, m.start(), "\\listoftodos left in the document",
                               fix=Fix(kind="patch", patch=patch, instructions="Remove it.") if patch else None))
        return out


@register
class Highlights(Check):
    id = "artifacts.highlight"
    stage = 3
    severity = Severity.WARN
    why = "Highlighting from the revision is an editing artifact."

    def run(self, ctx):
        out = []
        for start, name, _st, _o, arg, end in _body_commands(ctx, r"hl|highlight"):
            patch = _span_patch(ctx, start, end, replacement_from_arg=True)
            out.append(self.at(ctx, start, f"\\{name}{{...}} highlight left in the text",
                               fix=Fix(kind="patch", patch=patch, instructions="Keep the text, drop the highlight.") if patch else None))
        return out


@register
class ColoredText(Check):
    id = "artifacts.color"
    stage = 3
    severity = Severity.WARN
    why = "Coloured revision text is an editing artifact."

    def run(self, ctx):
        colors = [c.lower() for c in self.opt(ctx, "colors", DEFAULT_COLORS)]
        out = []
        flat = ctx.project.flat
        for start, _n, _st, _o, color, end in _body_commands(ctx, "textcolor"):
            if color.strip().lower() not in colors:
                continue
            r = read_args(flat, end, 1, 0)
            if not r:
                continue
            full_end = r[2]
            patch = _span_patch(ctx, start, full_end, replacement_from_arg=True, arg_index=1)
            out.append(self.at(ctx, start, f"\\textcolor{{{color.strip()}}}{{...}} left in the text",
                               fix=Fix(kind="patch", patch=patch, instructions="Keep the text, drop the colour.") if patch else None))
        for m in re.finditer(r"\\color\s*\{\s*(" + "|".join(map(re.escape, colors)) + r")\s*\}", flat):
            if m.start() >= ctx.project.body_start and not any(e.name in ("tikzpicture", "axis") for e in ctx.project.enclosing_envs(m.start())):
                out.append(self.at(ctx, m.start(), f"\\color{{{m.group(1)}}} left in the text"))
        return out


@register
class ChangeMarks(Check):
    id = "artifacts.changes"
    stage = 3
    severity = Severity.WARN
    why = "Change bars and tracked-change markup are editing artifacts."

    def run(self, ctx):
        out = []
        rx = re.compile(r"\\(?:cbstart|cbend|cbdelete|added|deleted|replaced|DIFadd|DIFdel|DIFaddbegin|DIFdelbegin)\b")
        for m in rx.finditer(ctx.project.flat):
            if m.start() >= ctx.project.body_start:
                out.append(self.at(ctx, m.start(), f"change markup {m.group(0)} left in the text"))
        return out


@register
class TextMarkers(Check):
    id = "artifacts.markers"
    stage = 3
    severity = Severity.WARN
    why = "Revision markers such as NEW: or TODO are visible to readers."

    def run(self, ctx):
        flat = ctx.project.flat
        masked = prose_mask(flat[: ctx.project.body_end])
        out = []
        for m in re.finditer(r"\b(?:NEW|TODO|FIXME|XXX|TBD|TBA)\b:?|\?\?\?", masked):
            if m.start() >= ctx.project.body_start:
                out.append(self.at(ctx, m.start(), f"revision marker '{m.group(0)}' in the text"))
        return out


@register
class CommentedBlocks(Check):
    id = "artifacts.commented_blocks"
    stage = 3
    severity = Severity.WARN
    why = "Commented-out text ships with the arXiv source and can reveal old claims or reviews."

    def run(self, ctx):
        n_min = int(self.opt(ctx, "min_lines", 10))
        out = []
        for rel in ctx.project.order:
            lines = ctx.project.files[rel].lines
            blocks = []
            run_start, run_len = None, 0
            for i, ln in enumerate(lines + ["x"], 1):
                if ln.strip().startswith("%"):
                    if run_start is None:
                        run_start = i
                    run_len += 1
                    continue
                if run_start is not None and run_len >= n_min:
                    blocks.append((run_start, run_len))
                run_start, run_len = None, 0
            if not blocks:
                continue
            first = blocks[0][0]
            where = ", ".join(f"{a}-{a + n - 1}" for a, n in blocks[:15]) + (" ..." if len(blocks) > 15 else "")
            msg = (f"{blocks[0][1]}-line commented-out block" if len(blocks) == 1 else
                   f"{len(blocks)} commented-out blocks ({sum(n for _a, n in blocks)} lines) at lines {where}")
            out.append(self.finding(ctx, msg, file=rel, line=first, quote=lines[first - 1].strip(),
                                    instructions="Delete them before uploading the source (e.g. arxiv_latex_cleaner)."))
        return out


@register
class ArtifactPackages(Check):
    id = "artifacts.packages"
    stage = 3
    applies_to_modes = ("camera-ready",)
    severity = Severity.INFO
    why = "Revision packages are usually not needed in the final version."

    def run(self, ctx):
        out = []
        for pkg in ("todonotes", "changes", "changebar", "fixme", "soul", "trackchanges"):
            for start, _opts, _raw in usepackage_options(ctx, pkg):
                out.append(self.at(ctx, start, f"package {pkg} is loaded in the final version"))
        return out
