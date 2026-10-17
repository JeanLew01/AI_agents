from __future__ import annotations

import shutil
from pathlib import Path

import pytest

FIXTURES = Path(__file__).parent / "fixtures"
VENUE = FIXTURES / "venue_test.yaml"
HAVE_TEX = shutil.which("latexmk") is not None and shutil.which("pdflatex") is not None

needs_tex = pytest.mark.skipif(not HAVE_TEX, reason="latexmk/pdflatex not installed")

_cache: dict = {}


def run_fixture(name: str, mode: str = "camera-ready", rebuttal: str | None = None, llm=None,
                only: list[str] | None = None, no_llm: bool = True):
    """Run papergate on a fixture once per session (keyed by its arguments) and return the ledger."""
    from papergate.config import load_config
    from papergate.context import Options
    from papergate.pipeline import run_check

    key = (name, mode, rebuttal, id(llm) if llm else None, tuple(only or ()), no_llm)
    if key not in _cache:
        cfg = load_config(VENUE)
        opts = Options(rebuttal=FIXTURES / rebuttal if rebuttal else None, no_llm=no_llm, only=only or [])
        _cache[key] = run_check(FIXTURES / name, cfg, mode, opts, llm=llm, venue_path=str(VENUE))
    return _cache[key]


def find(ledger, check_id: str, severity: str | None = None):
    return [f for f in ledger.findings
            if (f.check_id == check_id or f.check_id.startswith(check_id + "."))
            and (severity is None or f.severity.value == severity)]


def line_of(fixture: str, rel: str, needle: str) -> int:
    text = (FIXTURES / fixture / rel).read_text()
    idx = text.index(needle)
    return text.count("\n", 0, idx) + 1
