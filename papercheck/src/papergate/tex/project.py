"""The LaTeX project as a document: main file, includes, flattened text with file:line mapping,
environments, sections, labels, references and citations."""

from __future__ import annotations

import bisect
import re
from dataclasses import dataclass, field
from functools import cached_property
from pathlib import Path

from .source import SourceFile, find_commands, latex_to_text, read_args, read_group, read_optional

TEXT_EXTS = {".tex", ".bib", ".sty", ".cls", ".bst", ".bbl", ".txt", ".md", ".cfg", ".def", ".py",
             ".m", ".json", ".yaml", ".yml", ".csv", ".ipynb", ".sh", ".r", ".jl", ".cpp", ".c", ".h",
             ".tikz", ".pgf", ".dat", ".xml", ".html", ".svg", ".eps", ".ps"}
MAIN_NAMES = ("main.tex", "paper.tex", "root.tex", "ms.tex", "manuscript.tex", "article.tex")
THEOREM_DEFAULTS = {
    "theorem": "Theorem", "lemma": "Lemma", "proposition": "Proposition", "corollary": "Corollary",
    "assumption": "Assumption", "definition": "Definition", "remark": "Remark", "claim": "Claim",
    "conjecture": "Conjecture", "example": "Example", "fact": "Fact", "property": "Property",
}
REF_CMDS = r"ref|cref|Cref|autoref|eqref|pageref|nameref|vref|Vref|labelcref|cpageref|Cpageref|subref|crefrange|Crefrange"
INCLUDE_RE = re.compile(r"\\(input|include|subfile|InputIfFileExists)\s*\{([^{}]+)\}")
IMPORT_RE = re.compile(r"\\(import|subimport|inputfrom|subinputfrom|includefrom|subincludefrom)\*?\s*\{([^{}]*)\}\s*\{([^{}]+)\}")


class ProjectError(Exception):
    pass


@dataclass
class Segment:
    flat_start: int
    flat_end: int
    rel: str
    file_offset: int


@dataclass
class Env:
    name: str
    start: int  # offset of \begin
    body_start: int
    body_end: int  # offset of \end
    end: int  # offset after \end{name}
    opt: str | None = None

    def contains(self, off: int) -> bool:
        return self.start <= off < self.end


@dataclass
class Section:
    level: int
    command: str
    starred: bool
    title: str  # plain text
    raw_title: str
    start: int
    end: int  # end of the section command
    label: str | None = None
    in_appendix: bool = False


@dataclass
class Label:
    key: str
    start: int
    kind: str  # figure, table, equation, theorem name, section, item, other
    env: Env | None = None


@dataclass
class Ref:
    keys: list[str]
    start: int
    end: int
    command: str


@dataclass
class Cite:
    keys: list[str]
    start: int
    end: int
    command: str


@dataclass
class Located:
    file: str
    line: int


@dataclass
class TexProject:
    root: Path
    main: str
    files: dict[str, SourceFile] = field(default_factory=dict)
    order: list[str] = field(default_factory=list)
    flat: str = ""
    segments: list[Segment] = field(default_factory=list)
    missing_includes: list[tuple[str, int, str]] = field(default_factory=list)

    # ---- construction -----------------------------------------------------------------
    @classmethod
    def load(cls, root: Path, main: str | None = None) -> "TexProject":
        root = Path(root)
        files: dict[str, SourceFile] = {}
        for p in sorted(root.rglob("*.tex")):
            if ".git" in p.relative_to(root).parts:
                continue
            rel = p.relative_to(root).as_posix()
            files[rel] = SourceFile(rel, _read_text(p))
        main = main or detect_main(root, files)
        if main not in files:
            raise ProjectError(f"main file {main!r} not found under {root}")
        proj = cls(root=root, main=main, files=files)
        proj._flatten()
        return proj

    def _resolve(self, name: str, base_dir: str) -> str | None:
        name = name.strip()
        cands = []
        for d in ("", base_dir):
            for n in (name, name + ".tex"):
                cands.append((Path(d) / n).as_posix() if d else n)
        for c in cands:
            c = _norm(c)
            if c in self.files:
                return c
        return None

    def _flatten(self) -> None:
        pieces: list[str] = []
        pos = 0

        def emit(rel: str, a: int, b: int) -> None:
            nonlocal pos
            if b <= a:
                return
            self.segments.append(Segment(pos, pos + (b - a), rel, a))
            pieces.append(self.files[rel].stripped[a:b])
            pos += b - a

        def walk(rel: str, stack: tuple[str, ...], base_dir: str) -> None:
            self.order.append(rel)
            src = self.files[rel].stripped
            incs = []
            for m in INCLUDE_RE.finditer(src):
                incs.append((m.start(), m.end(), m.group(2), base_dir))
            for m in IMPORT_RE.finditer(src):
                d = m.group(2).strip()
                incs.append((m.start(), m.end(), m.group(3),
                             _norm((Path(base_dir) / d).as_posix()) if m.group(1).startswith("sub") else _norm(d)))
            incs.sort()
            cur = 0
            for a, b, name, bdir in incs:
                emit(rel, cur, a)
                target = self._resolve(name, bdir)
                if target is None:
                    if not re.search(r"\.(sty|cls|bbl|tikz|pgf|pdf_tex|ind|toc)$", name.strip()):
                        self.missing_includes.append((rel, self.files[rel].line_of(a), name))
                elif target in stack:
                    pass
                else:
                    walk(target, stack + (target,), bdir or _norm(str(Path(target).parent)))
                cur = b
            emit(rel, cur, len(src))

        walk(self.main, (self.main,), "")
        self.flat = "".join(pieces)
        self._seg_starts = [s.flat_start for s in self.segments]

    # ---- location mapping -------------------------------------------------------------
    def locate(self, off: int) -> Located:
        if not self.segments:
            return Located(self.main, 1)
        i = max(0, bisect.bisect_right(self._seg_starts, off) - 1)
        seg = self.segments[i]
        f = self.files[seg.rel]
        return Located(seg.rel, f.line_of(seg.file_offset + min(off, seg.flat_end - 1) - seg.flat_start))

    def file_offset(self, off: int) -> tuple[str, int]:
        """(file, offset in that file) for a flat offset."""
        i = max(0, bisect.bisect_right(self._seg_starts, off) - 1)
        seg = self.segments[i]
        return seg.rel, seg.file_offset + off - seg.flat_start

    def same_segment(self, a: int, b: int) -> bool:
        i = max(0, bisect.bisect_right(self._seg_starts, a) - 1)
        return b <= self.segments[i].flat_end

    def raw_slice(self, a: int, b: int) -> str:
        """Raw (uncommented) source text for a flat range, when it lies in one segment."""
        i = max(0, bisect.bisect_right(self._seg_starts, a) - 1)
        seg = self.segments[i]
        if b > seg.flat_end:
            return self.flat[a:b]
        off = seg.file_offset + a - seg.flat_start
        return self.files[seg.rel].text[off:off + (b - a)]

    def line_quote(self, off: int) -> tuple[str, int, str]:
        """(file, line, raw line text stripped) at a flat offset."""
        loc = self.locate(off)
        return loc.file, loc.line, self.files[loc.file].line_text(loc.line).strip()

    # ---- document regions -------------------------------------------------------------
    @cached_property
    def body_start(self) -> int:
        m = re.search(r"\\begin\{document\}", self.flat)
        return m.end() if m else 0

    @cached_property
    def body_end(self) -> int:
        m = re.search(r"\\end\{document\}", self.flat)
        return m.start() if m else len(self.flat)

    @property
    def preamble(self) -> str:
        return self.flat[: self.body_start]

    @cached_property
    def appendix_start(self) -> int | None:
        m = re.search(r"\\appendix\b|\\begin\{appendices\}", self.flat[self.body_start:])
        if m:
            return self.body_start + m.start()
        for s in self.sections:
            if s.level <= 1 and re.match(r"(appendix|appendices|supplementary)", s.title, re.I):
                return s.start
        return None

    def in_appendix(self, off: int) -> bool:
        return self.appendix_start is not None and off >= self.appendix_start

    # ---- environments -----------------------------------------------------------------
    @cached_property
    def envs(self) -> list[Env]:
        out: list[Env] = []
        stack: list[tuple[str, int, int, str | None]] = []
        for m in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", self.flat):
            kind, name = m.group(1), m.group(2).strip()
            if kind == "begin":
                opt = None
                r = read_optional(self.flat, m.end())
                body = m.end()
                if r and name not in ("tabular", "tabular*", "array", "tabularx", "minipage", "figure",
                                      "figure*", "table", "table*", "wrapfigure", "subfigure", "center",
                                      "itemize", "enumerate", "description", "algorithmic"):
                    opt, body = r[0], r[1]
                stack.append((name, m.start(), body, opt))
            else:
                for k in range(len(stack) - 1, -1, -1):
                    if stack[k][0] == name:
                        n, st, bs, opt = stack[k]
                        out.append(Env(n, st, bs, m.start(), m.end(), opt))
                        del stack[k:]
                        break
        out.sort(key=lambda e: e.start)
        return out

    def envs_named(self, *names: str) -> list[Env]:
        return [e for e in self.envs if e.name in names]

    def enclosing_envs(self, off: int) -> list[Env]:
        return [e for e in self.envs if e.contains(off)]

    @cached_property
    def theorem_envs(self) -> dict[str, str]:
        """env name -> printed name, from \\newtheorem / \\declaretheorem plus common defaults."""
        names = dict(THEOREM_DEFAULTS)
        for _s, _n, _star, _opts, arg, end in find_commands(self.preamble, "newtheorem"):
            r = read_optional(self.preamble, end)
            e = r[1] if r else end
            title = read_group(self.preamble, e)
            names[arg.strip()] = latex_to_text(title[0]) if title else arg.strip().capitalize()
        for _s, _n, _star, opts, arg, _e in find_commands(self.preamble, "declaretheorem"):
            for a in arg.split(","):
                m = re.search(r"name\s*=\s*\{?([^,}]+)", opts[0]) if opts else None
                names[a.strip()] = m.group(1).strip() if m else a.strip().capitalize()
        return names

    # ---- sections ---------------------------------------------------------------------
    @cached_property
    def sections(self) -> list[Section]:
        levels = {"part": -1, "chapter": 0, "section": 1, "subsection": 2, "subsubsection": 3,
                  "paragraph": 4, "subparagraph": 5}
        out = []
        for m in re.finditer(r"\\(part|chapter|section|subsection|subsubsection|paragraph|subparagraph)(?![a-zA-Z])(\*?)",
                             self.flat):
            if m.start() < self.body_start:
                continue
            r = read_args(self.flat, m.end(), 1, max_optional=1)
            if not r:
                continue
            _opts, args, end = r
            label = None
            lm = re.match(r"\s*\\label\{([^{}]+)\}", self.flat[end:end + 200])
            if lm:
                label = lm.group(1).strip()
            out.append(Section(levels[m.group(1)], m.group(1), bool(m.group(2)), latex_to_text(args[0]),
                               args[0], m.start(), end, label))
        return out

    def section_at(self, off: int, max_level: int = 1) -> Section | None:
        cur = None
        for s in self.sections:
            if s.start > off:
                break
            if s.level <= max_level:
                cur = s
        return cur

    def section_range(self, sec: Section) -> tuple[int, int]:
        idx = self.sections.index(sec)
        end = self.body_end
        for s in self.sections[idx + 1:]:
            if s.level <= sec.level:
                end = s.start
                break
        bib = re.search(r"\\bibliography\{|\\printbibliography|\\begin\{thebibliography\}", self.flat[sec.end:end])
        if bib:
            end = sec.end + bib.start()
        if self.appendix_start and sec.start < self.appendix_start < end:
            end = self.appendix_start
        return sec.start, end

    def find_section(self, pattern: str, max_level: int = 2) -> Section | None:
        rx = re.compile(pattern, re.I)
        for s in self.sections:
            if s.level <= max_level and rx.search(s.title):
                return s
        return None

    # ---- front matter -----------------------------------------------------------------
    def command_arg(self, name: str) -> tuple[str, int, int] | None:
        for start, _n, _star, _opts, arg, end in find_commands(self.flat, name):
            return arg, start, end
        return None

    @cached_property
    def title(self) -> str | None:
        r = self.command_arg("title")
        return latex_to_text(r[0]) if r else None

    @cached_property
    def abstract_range(self) -> tuple[int, int] | None:
        envs = self.envs_named("abstract")
        if envs:
            return envs[0].body_start, envs[0].body_end
        r = self.command_arg("abstract")
        if r:
            return r[1], r[2]
        return None

    # ---- labels, refs, cites ----------------------------------------------------------
    @cached_property
    def labels(self) -> list[Label]:
        out = []
        float_kinds = {"figure": "figure", "figure*": "figure", "wrapfigure": "figure", "subfigure": "figure",
                       "table": "table", "table*": "table", "wraptable": "table", "algorithm": "algorithm",
                       "algorithm*": "algorithm", "lstlisting": "listing"}
        math = {"equation", "equation*", "align", "align*", "gather", "multline", "eqnarray", "flalign",
                "subequations", "alignat"}
        sec_label_offsets = {}
        for s in self.sections:
            if s.label:
                sec_label_offsets[s.label] = s
        for start, _n, _star, _opts, key, _end in find_commands(self.flat, "label"):
            key = key.strip()
            kind, env = "other", None
            if key in sec_label_offsets and abs(sec_label_offsets[key].end - start) < 200:
                kind = "section"
            else:
                for e in reversed(self.enclosing_envs(start)):
                    if e.name in float_kinds:
                        kind, env = float_kinds[e.name], e
                        break
                    if e.name in math:
                        kind, env = "equation", e
                        break
                    if e.name in self.theorem_envs:
                        kind, env = e.name, e
                        break
                    if e.name in ("enumerate", "itemize", "description"):
                        kind, env = "item", e
                        break
                if kind == "other":
                    prev = self.section_at(start, max_level=5)
                    if prev and 0 <= start - prev.end < 120 and not self.flat[prev.end:start].strip():
                        kind = "section"
            out.append(Label(key, start, kind, env))
        return out

    @cached_property
    def refs(self) -> list[Ref]:
        out = []
        for start, name, _star, _opts, arg, end in find_commands(self.flat, REF_CMDS):
            out.append(Ref([k.strip() for k in arg.split(",") if k.strip()], start, end, name))
        for m in re.finditer(r"\\hyperref\s*\[([^\]]+)\]", self.flat):
            out.append(Ref([m.group(1).strip()], m.start(), m.end(), "hyperref"))
        return out

    @cached_property
    def referenced_keys(self) -> set[str]:
        return {k for r in self.refs for k in r.keys}

    @cached_property
    def cites(self) -> list[Cite]:
        out = []
        pat = re.compile(r"\\([a-zA-Z]*cite[a-zA-Z]*|Cite[a-zA-Z]*)(?![a-zA-Z@])\*?")
        for m in pat.finditer(self.flat):
            name = m.group(1)
            if name in ("citestyle", "citeindextype", "bibliographystyle"):
                continue
            r = read_args(self.flat, m.end(), 1)
            if not r:
                continue
            out.append(Cite([k.strip() for k in r[1][0].split(",") if k.strip()], m.start(), r[2], name))
        return out

    @cached_property
    def cited_keys(self) -> set[str]:
        return {k for c in self.cites for k in c.keys}

    @cached_property
    def bib_files(self) -> list[str]:
        out = []
        for _s, name, _star, _opts, arg, _e in find_commands(self.flat, ("bibliography", "addbibresource")):
            for part in arg.split(","):
                part = part.strip()
                if not part:
                    continue
                cand = part if part.endswith(".bib") else part + ".bib"
                if (self.root / cand).is_file():
                    out.append(_norm(cand))
        return out

    # ---- figures ----------------------------------------------------------------------
    @cached_property
    def graphics(self) -> list[tuple[int, str, str | None]]:
        """(flat offset, name as written, resolved relative path or None) for \\includegraphics."""
        gpaths = [""]
        for _s, _n, _st, _o, arg, _e in find_commands(self.preamble, "graphicspath"):
            gpaths += re.findall(r"\{([^{}]*)\}", arg)
        out = []
        for start, _n, _star, _opts, arg, _e in find_commands(self.flat, "includegraphics"):
            name = arg.strip()
            out.append((start, name, self._resolve_graphic(name, gpaths)))
        return out

    def _resolve_graphic(self, name: str, gpaths: list[str]) -> str | None:
        exts = ["", ".pdf", ".png", ".jpg", ".jpeg", ".eps", ".PDF", ".PNG", ".JPG"]
        for d in gpaths:
            for ext in exts:
                p = self.root / d / (name + ext)
                if p.is_file():
                    return p.relative_to(self.root).as_posix()
        return None

    # ---- misc -------------------------------------------------------------------------
    def all_text_files(self) -> list[Path]:
        out = []
        for p in sorted(self.root.rglob("*")):
            rel = p.relative_to(self.root)
            if ".git" in rel.parts or not p.is_file():
                continue
            if p.suffix.lower() in TEXT_EXTS:
                out.append(p)
        return out


def _norm(p: str) -> str:
    parts: list[str] = []
    for part in Path(p).as_posix().split("/"):
        if part in ("", "."):
            continue
        if part == ".." and parts:
            parts.pop()
        else:
            parts.append(part)
    return "/".join(parts)


def _read_text(p: Path) -> str:
    data = p.read_bytes()
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return data.decode("latin-1")


def detect_main(root: Path, files: dict[str, SourceFile]) -> str:
    cands = []
    for rel, f in files.items():
        if re.search(r"\\documentclass", f.stripped) and re.search(r"\\begin\{document\}", f.stripped):
            magic = re.search(r"^%\s*!\s*TEX\s+root\s*=\s*(\S+)", f.text, re.M | re.I)
            if magic and _norm((Path(rel).parent / magic.group(1)).as_posix()) != rel:
                continue
            cands.append(rel)
    top = [c for c in cands if "/" not in c]
    pool = top or cands
    if len(pool) == 1:
        return pool[0]
    if not pool:
        raise ProjectError(f"no main .tex file (with \\documentclass and \\begin{{document}}) under {root}")
    for n in MAIN_NAMES + (root.name + ".tex",):
        if n in pool:
            return n
    raise ProjectError("several candidate main files, pass --main: " + ", ".join(sorted(pool)))
