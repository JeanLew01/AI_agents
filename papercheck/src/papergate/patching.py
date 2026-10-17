"""Build git-style unified diffs for mechanical fixes. Patches are only proposed here;
`papergate apply` is the only code path that writes them to a paper."""

from __future__ import annotations

import difflib
from pathlib import Path


def unified_patch(rel: str, old: str, new: str) -> str:
    a = old.splitlines(True)
    b = new.splitlines(True)
    lines = list(difflib.unified_diff(a, b, f"a/{rel}", f"b/{rel}", n=3))
    out = []
    for ln in lines:
        if ln.endswith("\n"):
            out.append(ln)
        else:  # last line of a file without trailing newline
            out.append(ln + "\n\\ No newline at end of file\n")
    return "".join(out)


def edit_patch(paper_dir: Path, rel: str, edits: list[tuple[int, int, str]]) -> str | None:
    """Patch replacing raw-file spans [start, end) by text; edits must not overlap."""
    text = (Path(paper_dir) / rel).read_text(encoding="utf-8")
    new = text
    for start, end, repl in sorted(edits, key=lambda e: -e[0]):
        new = new[:start] + repl + new[end:]
    if new == text:
        return None
    return unified_patch(rel, text, new)


def delete_line_patch(paper_dir: Path, rel: str, line: int) -> str | None:
    text = (Path(paper_dir) / rel).read_text(encoding="utf-8")
    lines = text.splitlines(True)
    if not 1 <= line <= len(lines):
        return None
    new = "".join(lines[: line - 1] + lines[line:])
    return unified_patch(rel, text, new)
