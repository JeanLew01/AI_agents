"""Render report.md and report.html from the JSON ledger."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from jinja2 import Environment, PackageLoader, select_autoescape

from .models import Ledger

STAGES = {0: "Project", 1: "Build", 2: "PDF compliance", 3: "Identity", 4: "Internal consistency",
          5: "Math rigor", 6: "Claims and rebuttal", 7: "Figures"}


def _env() -> Environment:
    env = Environment(loader=PackageLoader("papergate", "templates"),
                      autoescape=select_autoescape(["html"]), trim_blocks=True, lstrip_blocks=True,
                      keep_trailing_newline=True)
    env.filters["mdcode"] = _md_code
    return env


def _md_code(s: str) -> str:
    """Inline code span that survives backticks in the quote."""
    s = " ".join(s.split())
    fence = "``" if "`" in s else "`"
    return f"{fence} {s} {fence}" if fence == "``" else f"`{s}`"


def _context(ledger: Ledger) -> dict:
    by_sev = defaultdict(list)
    for f in ledger.findings:
        by_sev[f.severity.value].append(f)
    return {"L": ledger, "h": ledger.header, "by_sev": by_sev, "stages": STAGES,
            "severities": ["BLOCKER", "WARN", "INFO"]}


def render_markdown(ledger: Ledger) -> str:
    return _env().get_template("report.md.j2").render(**_context(ledger))


def render_html(ledger: Ledger) -> str:
    return _env().get_template("report.html.j2").render(**_context(ledger))


def write_reports(ledger: Ledger, out_dir: Path) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    md = out_dir / "report.md"
    html = out_dir / "report.html"
    md.write_text(render_markdown(ledger), encoding="utf-8")
    html.write_text(render_html(ledger), encoding="utf-8")
    return [md, html]
