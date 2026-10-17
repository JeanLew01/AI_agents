"""Shared machinery for LLM-assisted checks: quote verification and severity capping."""

from __future__ import annotations

from ..llm.verify import project_index
from ..models import DiscardedFinding, Fix, Severity
from ..registry import Check


class LLMCheck(Check):
    source = "llm"
    requires = frozenset({"llm"})

    def verified(self, ctx, *, quote: str, file: str | None, line: int | None, message: str,
                 severity: str | Severity = Severity.WARN, why: str = "", instructions: str = "",
                 check_id: str | None = None):
        """A Finding if `quote` occurs verbatim in the sources, else None (counted as discarded)."""
        hit = project_index(ctx).find(quote, file, line)
        if hit is None:
            ctx.discarded.append(DiscardedFinding(check_id=check_id or self.id, reason="quote not found in the source",
                                                  quote=quote[:300], file=file, line=line))
            return None
        f_name, f_line = hit
        sev = Severity(severity) if not isinstance(severity, Severity) else severity
        cap = ctx.config.llm.max_severity
        if sev.rank < cap.rank:
            sev = cap
        loc_file = str(ctx.options.rebuttal) if f_name == "rebuttal" and ctx.options.rebuttal else f_name
        return self.finding(ctx, message, severity=sev, file=loc_file, line=f_line, quote=" ".join(quote.split()),
                            why=why or self.why, check_id=check_id,
                            fix=Fix(kind="manual", instructions=instructions or "Review and fix by hand (LLM finding)."))
