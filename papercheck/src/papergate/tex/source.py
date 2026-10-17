"""Low-level LaTeX text helpers. Every transformation keeps string length, so an offset in a
processed view is the same offset in the raw file and maps back to a file:line."""

from __future__ import annotations

import bisect
import re
from dataclasses import dataclass, field

VERBATIM_ENVS = ("verbatim", "verbatim*", "lstlisting", "minted", "Verbatim", "comment", "filecontents",
                 "filecontents*")
MATH_ENVS = ("equation", "equation*", "align", "align*", "alignat", "alignat*", "gather", "gather*",
             "multline", "multline*", "eqnarray", "eqnarray*", "math", "displaymath", "flalign",
             "flalign*", "dmath", "dmath*")


def _blank(s: str) -> str:
    """Replace every character except newlines by a space."""
    return re.sub(r"[^\n]", " ", s)


def strip_comments(text: str) -> str:
    """Blank out TeX comments (unescaped % to end of line); length and newlines preserved."""
    out = []
    for line in text.split("\n"):
        cut = None
        i = 0
        while i < len(line):
            c = line[i]
            if c == "\\":
                i += 2
                continue
            if c == "%":
                cut = i
                break
            i += 1
        out.append(line if cut is None else line[:cut] + " " * (len(line) - cut))
    return "\n".join(out)


_VERB_BEGIN = re.compile(r"\\begin\{(" + "|".join(re.escape(e) for e in VERBATIM_ENVS) + r")\}")
_IFFALSE = re.compile(r"\\iffalse\b(.*?)\\fi\b", re.S)
_VERB_CMD = re.compile(r"\\(?:verb|lstinline)\*?([^a-zA-Z\s{])(.*?)\1")


def blank_verbatim(text: str) -> str:
    """Blank verbatim-like environments, \\iffalse..\\fi blocks and \\verb|..| (on the comment-stripped view)."""
    out = list(text)
    pos = 0
    while True:
        m = _VERB_BEGIN.search(text, pos)
        if not m:
            break
        end_tag = "\\end{" + m.group(1) + "}"
        e = text.find(end_tag, m.end())
        e = len(text) if e < 0 else e + len(end_tag)
        out[m.end():e] = _blank(text[m.end():e])
        pos = e
    s = "".join(out)
    s = _IFFALSE.sub(lambda m: m.group(0)[:8] + _blank(m.group(1)) + m.group(0)[-3:], s)
    s = _VERB_CMD.sub(lambda m: _blank(m.group(0)), s)
    return s


@dataclass
class SourceFile:
    rel: str
    text: str
    stripped: str = ""
    line_starts: list[int] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.stripped:
            self.stripped = blank_verbatim(strip_comments(self.text))
        self.line_starts = [0] + [m.end() for m in re.finditer(r"\n", self.text)]

    def line_of(self, offset: int) -> int:
        return bisect.bisect_right(self.line_starts, offset)

    def line_text(self, line: int) -> str:
        if line < 1 or line > len(self.line_starts):
            return ""
        start = self.line_starts[line - 1]
        end = self.text.find("\n", start)
        return self.text[start:] if end < 0 else self.text[start:end]

    @property
    def lines(self) -> list[str]:
        return self.text.split("\n")


# --- brace-aware argument reading ------------------------------------------------------

def skip_ws(s: str, i: int) -> int:
    while i < len(s) and s[i] in " \t\n\r":
        i += 1
    return i


def read_group(s: str, i: int) -> tuple[str, int] | None:
    """If s[i:] (after whitespace) starts with '{', return (content, index after the matching '}')."""
    i = skip_ws(s, i)
    if i >= len(s) or s[i] != "{":
        return None
    depth = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    return None


def read_optional(s: str, i: int) -> tuple[str, int] | None:
    i2 = skip_ws(s, i)
    if i2 >= len(s) or s[i2] != "[":
        return None
    depth = 0
    j = i2
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
        elif c == "]" and depth == 0:
            return s[i2 + 1:j], j + 1
        j += 1
    return None


def read_args(s: str, i: int, n_mandatory: int, max_optional: int = 2) -> tuple[list[str], list[str], int] | None:
    """Read [opt]...{arg}{arg}: returns (optionals, mandatories, end)."""
    opts = []
    j = i
    if j < len(s) and s[j] == "*":
        j += 1
    while len(opts) < max_optional:
        r = read_optional(s, j)
        if not r:
            break
        opts.append(r[0])
        j = r[1]
    args = []
    for _ in range(n_mandatory):
        r = read_group(s, j)
        if not r:
            return None
        args.append(r[0])
        j = r[1]
    return opts, args, j


def find_commands(s: str, names: str | tuple[str, ...], start: int = 0, end: int | None = None):
    """Yield (match_start, name, star, optionals, args, end) for \\name[...]{...} occurrences.
    names may be a regex alternative string. Only one mandatory argument is read."""
    if isinstance(names, tuple):
        names = "|".join(re.escape(n) for n in names)
    pat = re.compile(r"\\(" + names + r")(?![a-zA-Z@])(\*?)")
    end = len(s) if end is None else end
    for m in pat.finditer(s, start, end):
        r = read_args(s, m.end(), 1)
        if r is None:
            continue
        opts, args, e = r
        yield m.start(), m.group(1), m.group(2), opts, args[0], e


_TEXT_ARG_CMDS = {"textbf", "textit", "emph", "textsc", "texttt", "textrm", "textsf", "underline",
                  "mbox", "text", "textnormal", "textup", "textmd", "uline", "hl", "fbox", "smash"}


def latex_to_text(s: str) -> str:
    """Rough plain-text rendering of a LaTeX fragment (for titles, names, captions, table cells)."""
    s = strip_comments(s)
    s = re.sub(r"\\(?:label|ref|cref|Cref|eqref|cite[a-z]*|footnote|thanks|index)\*?(\[[^\]]*\])?\{[^{}]*\}", "", s)
    s = re.sub(r"\\textcolor\{[^{}]*\}", "", s)
    s = re.sub(r"\\(?:href)\{[^{}]*\}", "", s)
    s = s.replace("~", " ").replace("\\\\", " ").replace("\\&", "&").replace("\\%", "%")
    s = s.replace("\\_", "_").replace("\\#", "#").replace("\\$", "$")
    s = re.sub(r"\\[,;:! ]", " ", s)
    s = re.sub(r"\\[a-zA-Z@]+\*?", " ", s)
    s = re.sub(r"[{}]", "", s)
    s = s.replace("$", "")
    s = re.sub(r"[ \t\r\n]+", " ", s)
    return s.strip()


def normalize_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def prose_mask(s: str) -> str:
    """Length-preserving view of LaTeX where math, command names, non-prose command arguments,
    braces and float bodies (except captions) are blanked: regexes over it hit prose only."""
    out = list(s)

    def blank(a: int, b: int) -> None:
        for k in range(a, min(b, len(out))):
            if out[k] != "\n":
                out[k] = " "

    # display math environments
    for env in MATH_ENVS:
        tag = re.escape(env)
        for m in re.finditer(r"\\begin\{" + tag + r"\}.*?\\end\{" + tag + r"\}", s, re.S):
            blank(m.start(), m.end())
    # inline / display math delimiters
    for m in re.finditer(r"\$\$.*?\$\$|\\\[.*?\\\]|\\\(.*?\\\)|(?<!\\)\$(?:\\\$|[^$])*?(?<!\\)\$", s, re.S):
        blank(m.start(), m.end())
    # commands whose arguments are not prose
    for start, _name, _star, _opts, _arg, end in find_commands(
        s, r"label|ref|cref|Cref|autoref|eqref|pageref|nameref|vref|cite[a-zA-Z]*|nocite|citep|citet|url|"
           r"includegraphics|input|include|usepackage|documentclass|bibliographystyle|bibliography|"
           r"hspace|vspace|setlength|addtolength|color|pagecolor|graphicspath|addbibresource|"
           r"newcommand|renewcommand|providecommand|DeclareMathOperator|hypersetup|"
           r"begin|end|linewidth|textwidth|setcounter|addtocounter|resizebox|scalebox|"
           r"thispagestyle|pagestyle|bibitem|newtheorem|declaretheorem|captionsetup|acrodef|newacronym"):
        blank(start, end)
    for start, _name, _star, _opts, _arg, end in find_commands(s, r"href|textcolor"):
        blank(start, end)  # keep the second argument (link text / coloured text)
    # tabular bodies are not prose (captions are kept)
    for m in re.finditer(r"\\begin\{(tabular\*?|tabularx|longtable|array|tikzpicture|algorithmic)\}.*?\\end\{\1\}", s, re.S):
        blank(m.start(), m.end())
    masked = "".join(out)
    masked = re.sub(r"\\[a-zA-Z@]+\*?", lambda m: " " * len(m.group(0)), masked)
    masked = re.sub(r"\\\\|\\[,;:! ]", lambda m: " " * len(m.group(0)), masked)
    masked = re.sub(r"\\(?=[%&#_$])", " ", masked)
    masked = re.sub(r"[{}~]", " ", masked)
    return masked
