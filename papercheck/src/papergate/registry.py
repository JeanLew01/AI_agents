"""Check registry. A check is a small class decorated with @register; dropping a module into
papergate/checks/ (or exposing one through the `papergate.checks` entry-point group) adds it."""

from __future__ import annotations

import importlib
import pkgutil
from importlib.metadata import entry_points
from typing import TYPE_CHECKING, ClassVar

from .models import MODES, Finding, Fix, Location, Severity

if TYPE_CHECKING:
    from .context import CheckContext

REQUIREMENTS = {"build", "pdf", "llm", "rebuttal", "online"}


class SkipCheck(Exception):
    """Raise from run() when a check cannot run here (missing tool, nothing to check)."""


class Check:
    id: ClassVar[str]
    stage: ClassVar[int]
    title: ClassVar[str] = ""
    applies_to_modes: ClassVar[tuple[str, ...]] = MODES
    requires: ClassVar[frozenset[str]] = frozenset()
    severity: ClassVar[Severity] = Severity.WARN  # default severity of this check's findings
    why: ClassVar[str] = ""  # default why_it_matters
    source: ClassVar[str] = "deterministic"

    def run(self, ctx: "CheckContext") -> list[Finding]:
        raise NotImplementedError

    def opt(self, ctx: "CheckContext", key: str, default=None):
        return ctx.config.opt(self.id, key, default)

    def finding(self, ctx: "CheckContext", message: str, *, severity: Severity | None = None,
                file: str | None = None, line: int | None = None, page: int | None = None,
                quote: str = "", why: str | None = None, fix: Fix | None = None,
                instructions: str = "", check_id: str | None = None) -> Finding:
        return Finding(
            check_id=check_id or self.id,
            stage=self.stage,
            severity=severity or self.severity,
            mode=ctx.mode,
            location=Location(file=file, line=line, page=page),
            quote=quote,
            message=message,
            why_it_matters=self.why if why is None else why,
            fix=fix or Fix(kind="manual", instructions=instructions),
            source=self.source,  # type: ignore[arg-type]
        )

    def at(self, ctx: "CheckContext", offset: int, message: str, *, quote: str | None = None, **kw) -> Finding:
        """Finding located at a flat-text offset of the project (quote defaults to the source line)."""
        file, line, text = ctx.project.line_quote(offset)
        return self.finding(ctx, message, file=file, line=line, quote=text if quote is None else quote, **kw)


REGISTRY: dict[str, type[Check]] = {}
_loaded = False


def register(cls: type[Check]) -> type[Check]:
    for attr in ("id", "stage"):
        if not hasattr(cls, attr):
            raise TypeError(f"{cls.__name__}: missing class attribute {attr!r}")
    bad = set(cls.requires) - REQUIREMENTS
    if bad:
        raise TypeError(f"{cls.id}: unknown requirement(s) {sorted(bad)}")
    bad_modes = set(cls.applies_to_modes) - set(MODES)
    if bad_modes:
        raise TypeError(f"{cls.id}: unknown mode(s) {sorted(bad_modes)}")
    if cls.id in REGISTRY and REGISTRY[cls.id] is not cls:
        raise ValueError(f"duplicate check id {cls.id!r} ({REGISTRY[cls.id].__name__} and {cls.__name__})")
    REGISTRY[cls.id] = cls
    return cls


def unregister(check_id: str) -> None:
    REGISTRY.pop(check_id, None)


def load_checks() -> dict[str, type[Check]]:
    global _loaded
    if not _loaded:
        from . import checks

        for mod in pkgutil.walk_packages(checks.__path__, checks.__name__ + "."):
            importlib.import_module(mod.name)
        for ep in entry_points(group="papergate.checks"):
            ep.load()
        _loaded = True
    return REGISTRY


def matches(check_id: str, selectors: list[str]) -> bool:
    return any(check_id == s or check_id.startswith(s.rstrip(".") + ".") for s in selectors)


def select(mode: str, only: list[str] | None = None, disabled=lambda _id: False) -> list[type[Check]]:
    load_checks()
    out = []
    for cid, cls in REGISTRY.items():
        if mode not in cls.applies_to_modes or disabled(cid):
            continue
        if only and not matches(cid, only):
            continue
        out.append(cls)
    return sorted(out, key=lambda c: (c.stage, c.id))
