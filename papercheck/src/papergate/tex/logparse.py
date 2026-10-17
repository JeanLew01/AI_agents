"""Parse a LaTeX log (built with max_print_line=10000, -file-line-error) and BibTeX/Biber logs."""

from __future__ import annotations

import re
from dataclasses import dataclass

_FILE_OPEN = re.compile(r"\(((?:\.{0,2}/)?[^\s()\[\]{}]+?\.(?:tex|sty|cls|cfg|def|clo|fd|bbl|aux|out|toc|ldf|dict|lbx|bbx|cbx|mkii|ltx|tikz|pgf|pdf_tex|lco|enc|map))(?=[\s()]|$)")
_ERROR_FLE = re.compile(r"^((?:\./|/)?[^\s:]+\.(?:tex|sty|cls|bbl|aux|def|cfg)):(\d+): (.*)$")
_OVERFULL = re.compile(r"^(Overfull|Underfull) \\([hv])box \((?:(\d+(?:\.\d+)?)pt too (?:wide|high)|badness \d+)\) "
                       r"(?:in paragraph at lines (\d+)--(\d+)|in alignment at lines (\d+)--(\d+)|"
                       r"detected at line (\d+)|has occurred while \\output is active)")
_UNDEF_REF = re.compile(r"Reference [`']([^'`]+)' on page \d+ undefined")
_UNDEF_CITE = re.compile(r"Citation [`']([^'`]+)'(?: on page \d+)? undefined")
_MULTI = re.compile(r"Label [`']([^'`]+)' multiply defined")


@dataclass
class LogError:
    file: str | None
    line: int | None
    message: str
    context: str = ""


@dataclass
class BoxWarning:
    kind: str  # Overfull / Underfull
    box: str  # h / v
    amount_pt: float
    file: str | None
    line: int | None
    context: str = ""


@dataclass
class ParsedLog:
    errors: list[LogError]
    boxes: list[BoxWarning]
    undefined_refs: list[str]
    undefined_cites: list[str]
    multiply_defined: list[str]
    labels_changed: bool
    raw_warnings: list[str]


def _clean(path: str) -> str:
    return path[2:] if path.startswith("./") else path


def parse_log(text: str) -> ParsedLog:
    lines = text.splitlines()
    stack: list[str | None] = []
    errors: list[LogError] = []
    boxes: list[BoxWarning] = []
    refs, cites, multi, warns = [], [], [], []
    changed = False
    skip_box_body = False

    def current_file() -> str | None:
        for f in reversed(stack):
            if f and not f.startswith("/"):
                return _clean(f)
        return None

    i = 0
    while i < len(lines):
        ln = lines[i]
        m = _ERROR_FLE.match(ln)
        if m:
            ctx = " ".join(x.strip() for x in lines[i + 1:i + 3] if x.strip())
            errors.append(LogError(_clean(m.group(1)), int(m.group(2)), m.group(3).strip(), ctx))
        elif ln.startswith("! "):
            ctx_line = None
            ctx = ""
            for j in range(i + 1, min(i + 12, len(lines))):
                lm = re.match(r"l\.(\d+) ?(.*)", lines[j])
                if lm:
                    ctx_line, ctx = int(lm.group(1)), lm.group(2)
                    break
            errors.append(LogError(current_file(), ctx_line, ln[2:].strip(), ctx))
        bm = _OVERFULL.match(ln)
        if bm:
            amount = float(bm.group(3)) if bm.group(3) else 0.0
            start = bm.group(4) or bm.group(6) or bm.group(8)
            ctx = lines[i + 1].strip() if i + 1 < len(lines) else ""
            boxes.append(BoxWarning(bm.group(1), bm.group(2), amount, current_file(),
                                    int(start) if start else None, ctx))
            skip_box_body = True
            i += 1
            continue
        if skip_box_body:
            if not ln.strip():
                skip_box_body = False
            i += 1
            continue
        for rx, bucket in ((_UNDEF_REF, refs), (_UNDEF_CITE, cites), (_MULTI, multi)):
            for mm in rx.finditer(ln):
                if mm.group(1) not in bucket:
                    bucket.append(mm.group(1))
        if "Label(s) may have changed" in ln:
            changed = True
        if "Warning" in ln:
            warns.append(ln.strip())
        _track_files(ln, stack)
        i += 1
    return ParsedLog(errors, boxes, refs, cites, multi, changed, warns)


def _track_files(ln: str, stack: list[str | None]) -> None:
    pos = 0
    while pos < len(ln):
        c = ln[pos]
        if c == "(":
            m = _FILE_OPEN.match(ln, pos)
            if m:
                stack.append(m.group(1))
                pos = m.end()
                continue
            stack.append(None)
        elif c == ")":
            if stack:
                stack.pop()
        pos += 1


@dataclass
class BibMessage:
    level: str  # error / warning
    message: str
    key: str | None
    bibfile: str | None
    line: int | None


def parse_blg(text: str) -> list[BibMessage]:
    out = []
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        m = re.match(r"Warning--(.*)", ln)
        if m:
            msg = m.group(1).strip()
            km = re.search(r"\bin ([^\s,]+)\s*$", msg) or re.search(r'entry for "([^"]+)"', msg)
            loc = None
            if i + 1 < len(lines):
                lm = re.match(r"--line (\d+) of file (\S+)", lines[i + 1])
                loc = (int(lm.group(1)), lm.group(2)) if lm else None
            out.append(BibMessage("warning", msg, km.group(1) if km else None, loc[1] if loc else None,
                                  loc[0] if loc else None))
            continue
        m = re.search(r"---line (\d+) of file (\S+)", ln)
        if m and i > 0:
            prev = lines[i - 1].strip()
            out.append(BibMessage("error", (prev + " " + ln.split("---")[0]).strip(), None, m.group(2), int(m.group(1))))
            continue
        m = re.match(r"\[\d+\] .*?> (WARN|ERROR) - (.*)", ln)  # biber
        if m:
            msg = m.group(2).strip()
            km = re.search(r"entry '([^']+)'", msg)
            fm = re.search(r"file '([^']+)'", msg)
            lm = re.search(r"line (\d+)", msg)
            out.append(BibMessage("error" if m.group(1) == "ERROR" else "warning", msg,
                                  km.group(1) if km else None, fm.group(1) if fm else None,
                                  int(lm.group(1)) if lm else None))
    return out
