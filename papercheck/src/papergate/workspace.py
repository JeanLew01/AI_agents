"""Build sandbox: a temporary copy of the paper, compiled with latexmk. Nothing is written to the
paper directory: the copy lives under the system temp dir and TeX may only write inside it."""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path

# Build artefacts that must not leak into a "clean" build of the copy.
AUX_SUFFIXES = (".aux", ".blg", ".fdb_latexmk", ".fls", ".log", ".out", ".synctex.gz", ".toc", ".lof",
                ".lot", ".bcf", ".run.xml", ".nav", ".snm", ".xdv", ".brf", ".idx", ".ilg", ".ind",
                ".loa", ".lol", ".thm", ".vrb", ".synctex", ".auxlock")

# Probe passed via latexmk -usepretex: logs the page layout after \begin{document} has run.
LAYOUT_PROBE = (
    r"\AddToHook{begindocument/end}{\typeout{PAPERGATE-LAYOUT:"
    r"paperwidth=\the\paperwidth;paperheight=\the\paperheight;textwidth=\the\textwidth;"
    r"textheight=\the\textheight;oddsidemargin=\the\oddsidemargin;evensidemargin=\the\evensidemargin;"
    r"topmargin=\the\topmargin;headheight=\the\headheight;headsep=\the\headsep;footskip=\the\footskip;"
    r"hoffset=\the\hoffset;voffset=\the\voffset;columnsep=\the\columnsep;columnwidth=\the\columnwidth;"
    r"baselineskip=\the\baselineskip;marginparwidth=\the\marginparwidth;"
    r"fontsize=\csname f@size\endcsname pt;twocolumn=\csname if@twocolumn\endcsname 1\else 0\fi;"
    r"twoside=\csname if@twoside\endcsname 1\else 0\fi}}"
)


@dataclass
class BuildResult:
    ok: bool
    returncode: int
    pdf: Path | None
    log: Path | None
    outdir: Path
    srcdir: Path
    main: str
    duration_s: float
    output_tail: str = ""
    layout: dict[str, float] = field(default_factory=dict)
    timed_out: bool = False

    @property
    def jobname(self) -> str:
        return Path(self.main).stem

    def aux_file(self) -> Path | None:
        p = self.outdir / (self.jobname + ".aux")
        return p if p.is_file() else None

    def log_text(self) -> str:
        if self.log and self.log.is_file():
            return self.log.read_text(encoding="utf-8", errors="replace")
        return ""

    def bib_logs(self) -> list[Path]:
        return sorted(self.outdir.glob("*.blg"))


def _copy_ignore(src_root: Path):
    has_bib = any(src_root.rglob("*.bib"))

    def ignore(dirpath: str, names: list[str]) -> set[str]:
        out = set()
        for n in names:
            if n == ".git":
                out.add(n)
            elif n.endswith(AUX_SUFFIXES):
                out.add(n)
            elif n.endswith(".bbl") and has_bib:
                out.add(n)
        return out

    return ignore


class Workspace:
    def __init__(self, paper_dir: Path, keep: bool = False):
        self.paper_dir = Path(paper_dir).resolve()
        self.tmp = Path(tempfile.mkdtemp(prefix="papergate-"))
        self.src = self.tmp / "src"
        self.out = self.tmp / "out"
        self.keep = keep
        shutil.copytree(self.paper_dir, self.src, symlinks=False, ignore=_copy_ignore(self.paper_dir),
                        ignore_dangling_symlinks=True)
        self.out.mkdir()

    def cleanup(self) -> None:
        if not self.keep:
            shutil.rmtree(self.tmp, ignore_errors=True)

    def build(self, main: str, engine: str = "pdflatex", timeout_s: int = 300, shell_escape: bool = False,
              texinputs: list[str] | None = None) -> BuildResult:
        flag = {"pdflatex": "-pdf", "lualatex": "-pdflua", "xelatex": "-pdfxe"}[engine]
        cmd = ["latexmk", flag, "-interaction=nonstopmode", "-file-line-error", "-f", "-g",
               f"-outdir={self.out}", f"-auxdir={self.out}", f"-usepretex={LAYOUT_PROBE}"]
        if shell_escape:
            cmd.append("-shell-escape")
        cmd.append(main)
        env = dict(os.environ)
        env.update({
            "openout_any": "p",  # paranoid: TeX may not write to absolute paths or parent dirs
            "shell_escape": "t" if shell_escape else "p",  # restricted shell escape unless asked
            "max_print_line": "10000",  # unwrapped log lines
            "error_line": "254",
            "half_error_line": "238",
            "TEXMFOUTPUT": str(self.out),
        })
        if texinputs:
            env["TEXINPUTS"] = os.pathsep.join(texinputs) + os.pathsep + env.get("TEXINPUTS", "")
            env["BIBINPUTS"] = os.pathsep.join(texinputs) + os.pathsep + env.get("BIBINPUTS", "")
        t0 = time.time()
        timed_out = False
        try:
            proc = subprocess.run(cmd, cwd=self.src, env=env, capture_output=True, text=True,
                                  errors="replace", timeout=timeout_s, stdin=subprocess.DEVNULL)
            rc, output = proc.returncode, proc.stdout + proc.stderr
        except subprocess.TimeoutExpired as e:
            rc, timed_out = -1, True
            output = (e.stdout or b"").decode(errors="replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
        except FileNotFoundError:
            rc, output = -2, "latexmk not found on PATH"
        jobname = Path(main).stem
        pdf = self.out / f"{jobname}.pdf"
        log = self.out / f"{jobname}.log"
        res = BuildResult(ok=(rc == 0 and pdf.is_file()), returncode=rc, pdf=pdf if pdf.is_file() else None,
                          log=log if log.is_file() else None, outdir=self.out, srcdir=self.src, main=main,
                          duration_s=round(time.time() - t0, 2), output_tail=output[-4000:], timed_out=timed_out)
        res.layout = parse_layout(res.log_text())
        return res


def parse_layout(log: str) -> dict[str, float]:
    m = None
    for m in re.finditer(r"PAPERGATE-LAYOUT:(.*)", log):
        pass
    if not m:
        return {}
    out = {}
    for item in m.group(1).split(";"):
        if "=" not in item:
            continue
        k, v = item.split("=", 1)
        num = re.match(r"\s*(-?[\d.]+)", v)
        if num:
            out[k.strip()] = float(num.group(1))
    return out
