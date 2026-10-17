"""Stage 0: project-level sanity (config and source tree)."""

from __future__ import annotations

from ..models import Severity
from ..registry import Check, register


@register
class UnconfirmedConfig(Check):
    id = "config.unconfirmed"
    stage = 0
    severity = Severity.INFO
    why = "Venue values marked TODO were not confirmed against the official call for papers."

    def run(self, ctx):
        todo = ctx.config.todo
        if not todo:
            return []
        keys = ", ".join(sorted(todo))
        return [self.finding(ctx, f"{len(todo)} venue value(s) unconfirmed: {keys}",
                             file=ctx.config.source_files[-1] if ctx.config.source_files else None,
                             instructions="Confirm each value against the venue's call for papers and "
                                          "remove it from the config's `todo:` map.")]


@register
class MissingIncludes(Check):
    id = "project.includes"
    stage = 0
    severity = Severity.BLOCKER
    why = "A missing \\input/\\include file means part of the paper is not in the PDF."

    def run(self, ctx):
        out = []
        for rel, line, name in ctx.project.missing_includes:
            out.append(self.finding(ctx, f"included file not found: {name}", file=rel, line=line,
                                    quote=ctx.project.files[rel].line_text(line).strip()))
        return out
