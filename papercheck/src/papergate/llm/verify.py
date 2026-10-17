"""Anti-hallucination: every LLM finding must quote the source verbatim (whitespace-insensitive)."""

from __future__ import annotations

import bisect
import re


def _norm_with_map(text: str) -> tuple[str, list[int]]:
    """Collapse whitespace runs to one space; return the normalized text and, for each of its
    characters, the offset in the original text."""
    out, idx = [], []
    prev_space = False
    for i, c in enumerate(text):
        if c.isspace():
            if not prev_space:
                out.append(" ")
                idx.append(i)
            prev_space = True
        else:
            out.append(c)
            idx.append(i)
            prev_space = False
    return "".join(out), idx


def norm_quote(q: str) -> str:
    q = re.sub(r"^\s*\d+\|\s?", "", q, flags=re.M)  # a copied line-number prefix is tolerated
    return re.sub(r"\s+", " ", q).strip()


class QuoteIndex:
    """Searchable sources: name -> text (project .tex files, the rebuttal, ...)."""

    def __init__(self, sources: dict[str, str]):
        self.sources = sources
        self._norm = {k: _norm_with_map(v) for k, v in sources.items()}
        self._lines = {k: [0] + [m.end() for m in re.finditer(r"\n", v)] for k, v in sources.items()}

    def find(self, quote: str, file: str | None = None, line: int | None = None, min_len: int = 6):
        """(file, line) of the occurrence nearest to `line` in `file` (else anywhere), or None."""
        q = norm_quote(quote)
        if len(q) < min_len:
            return None
        order = ([file] if file in self.sources else []) + [k for k in self.sources if k != file]
        for name in order:
            ntext, idx = self._norm[name]
            hits = [m.start() for m in re.finditer(re.escape(q), ntext)]
            if not hits:
                continue
            lines = [bisect.bisect_right(self._lines[name], idx[h]) for h in hits]
            best = min(lines, key=lambda l: abs(l - line) if (line and name == file) else 0)
            return name, best
        return None


def project_index(ctx, extra: dict[str, str] | None = None) -> QuoteIndex:
    key = "quote_index"
    if key not in ctx.cache:
        srcs = {rel: ctx.project.files[rel].text for rel in ctx.project.order}
        if ctx.rebuttal_text is not None:
            srcs["rebuttal"] = ctx.rebuttal_text
        ctx.cache[key] = QuoteIndex(srcs)
    return ctx.cache[key]
