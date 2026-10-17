"""What every check receives. Expensive things (source model, build, PDF) are built lazily, once."""

from __future__ import annotations

import shutil
from dataclasses import dataclass, field
from functools import cached_property
from pathlib import Path
from typing import TYPE_CHECKING, Any

from .config import VenueConfig
from .models import DiscardedFinding
from .tex.project import TexProject

if TYPE_CHECKING:
    from .llm.base import LLMBackend
    from .pdf.doc import PdfDoc
    from .workspace import BuildResult, Workspace


@dataclass
class Options:
    rebuttal: Path | None = None
    no_llm: bool = False
    only: list[str] = field(default_factory=list)
    online: bool = False
    main: str | None = None
    supplementary: list[Path] = field(default_factory=list)
    keep_build: bool = False
    model: str | None = None


class CheckContext:
    def __init__(self, paper_dir: Path, config: VenueConfig, mode: str, options: Options,
                 llm: "LLMBackend"):
        self.paper_dir = Path(paper_dir).resolve()
        self.config = config
        self.mode = mode
        self.options = options
        self.llm = llm
        self.discarded: list[DiscardedFinding] = []
        self.metrics: dict[str, Any] = {}
        self.cache: dict[str, Any] = {}
        self._workspace: "Workspace | None" = None
        self._build: "BuildResult | None" = None
        self._build_attempted = False

    # ---- source -----------------------------------------------------------------------
    @cached_property
    def project(self) -> TexProject:
        return TexProject.load(self.paper_dir, self.options.main or self.config.main_file)

    # ---- build ------------------------------------------------------------------------
    @property
    def build(self) -> "BuildResult | None":
        if not self._build_attempted:
            self._build_attempted = True
            if shutil.which("latexmk") is None:
                return None
            from .workspace import Workspace

            self._workspace = Workspace(self.paper_dir, keep=self.options.keep_build)
            self._build = self._workspace.build(
                self.project.main,
                engine=self.config.engine,
                timeout_s=int(self.config.opt("build", "timeout_s", 300)),
                shell_escape=bool(self.config.opt("build", "allow_shell_escape", False)),
                texinputs=self.config.texinputs,
            )
            self.metrics["build"] = {"ok": self._build.ok, "returncode": self._build.returncode,
                                     "duration_s": self._build.duration_s, "engine": self.config.engine,
                                     "layout": self._build.layout}
            if self.options.keep_build:
                self.metrics["build"]["kept_at"] = str(self._workspace.tmp)
        return self._build

    @cached_property
    def pdf(self) -> "PdfDoc | None":
        b = self.build
        if b is None or b.pdf is None:
            return None
        from .pdf.doc import PdfDoc

        return PdfDoc(b.pdf)

    # ---- rebuttal ---------------------------------------------------------------------
    @cached_property
    def rebuttal_text(self) -> str | None:
        p = self.options.rebuttal
        return p.read_text(encoding="utf-8", errors="replace") if p else None

    def cleanup(self) -> None:
        if self.__dict__.get("pdf") is not None:
            self.__dict__["pdf"].close()
        if self._workspace is not None:
            self._workspace.cleanup()
