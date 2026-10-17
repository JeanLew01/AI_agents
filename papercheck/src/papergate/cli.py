"""papergate command-line interface."""

from __future__ import annotations

import datetime as dt
import os
import sys
from enum import Enum
from pathlib import Path
from typing import Annotated, Optional

import typer

from . import __version__

app = typer.Typer(add_completion=False, no_args_is_help=True,
                  help="Read-only pre-submission checker for LaTeX papers.")

EXIT_PASS, EXIT_BLOCKERS, EXIT_USAGE, EXIT_READONLY = 0, 1, 2, 3


class ModeChoice(str, Enum):
    camera_ready = "camera-ready"
    submission = "submission"


def _die(msg: str, code: int = EXIT_USAGE) -> None:
    typer.echo(f"papergate: {msg}", err=True)
    raise typer.Exit(code)


def _inside(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def default_report_dir(paper_dir: Path, mode: str) -> Path:
    base = Path(os.environ.get("PAPERGATE_REPORTS", Path.home() / ".cache" / "papergate" / "reports"))
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    return base / paper_dir.resolve().name / f"{stamp}-{mode}"


def _llm_backend(no_llm: bool, model: str | None, config):
    from .llm.base import NullBackend

    if no_llm:
        return NullBackend()
    try:
        from .llm.anthropic_backend import AnthropicBackend
    except ImportError:
        return NullBackend()
    backend = AnthropicBackend(model=model or config.llm.model, max_tokens=config.llm.max_tokens,
                               effort=config.llm.effort)
    if not backend.available:
        typer.echo("papergate: no Anthropic credentials (ANTHROPIC_API_KEY or `ant auth login`); "
                   "LLM stages will be skipped", err=True)
    return backend if backend.available else NullBackend()


@app.command()
def check(
    paper_dir: Annotated[Path, typer.Argument(help="Paper source directory (never modified).")],
    venue: Annotated[Path, typer.Option("--venue", help="Venue config YAML.")],
    mode: Annotated[ModeChoice, typer.Option("--mode")] = ModeChoice.camera_ready,
    rebuttal: Annotated[Optional[Path], typer.Option("--rebuttal", help="Rebuttal text (md/txt/tex).")] = None,
    no_llm: Annotated[bool, typer.Option("--no-llm", help="Skip LLM-assisted stages (fully offline).")] = False,
    only: Annotated[Optional[str], typer.Option("--only", help="Comma-separated check ids or id prefixes.")] = None,
    out: Annotated[Optional[Path], typer.Option("--out", help="Report directory (outside the paper dir).")] = None,
    main: Annotated[Optional[str], typer.Option("--main", help="Main .tex file, relative to paper_dir.")] = None,
    online: Annotated[bool, typer.Option("--online", help="Allow network lookups (arXiv/DBLP).")] = False,
    supp: Annotated[Optional[list[Path]], typer.Option("--supp", help="Supplementary file/dir (repeatable).")] = None,
    model: Annotated[Optional[str], typer.Option("--model", help="LLM model name (overrides the config).")] = None,
    keep_build: Annotated[bool, typer.Option("--keep-build", help="Keep the temporary build directory.")] = False,
    quiet: Annotated[bool, typer.Option("--quiet", "-q")] = False,
) -> None:
    """Check a paper and write findings.json, report.md and report.html."""
    from .config import ConfigError, load_config
    from .context import Options
    from .ledger import write_ledger
    from .pipeline import run_check
    from .render import write_reports

    paper_dir = paper_dir.expanduser().resolve()
    if not paper_dir.is_dir():
        _die(f"not a directory: {paper_dir}")
    out_dir = (out.expanduser() if out else default_report_dir(paper_dir, mode.value)).resolve()
    if _inside(out_dir, paper_dir):
        _die(f"report directory {out_dir} is inside the paper directory; choose --out elsewhere")
    if rebuttal is not None and not rebuttal.is_file():
        _die(f"rebuttal file not found: {rebuttal}")
    try:
        config = load_config(venue)
    except ConfigError as e:
        _die(str(e))
    options = Options(rebuttal=rebuttal.resolve() if rebuttal else None, no_llm=no_llm,
                      only=[s.strip() for s in only.split(",") if s.strip()] if only else [],
                      online=online, main=main, supplementary=[p.resolve() for p in (supp or [])],
                      keep_build=keep_build, model=model)
    llm = _llm_backend(no_llm, model, config)
    ledger = run_check(paper_dir, config, mode.value, options, llm=llm, venue_path=str(Path(venue).resolve()))
    write_ledger(ledger, out_dir)
    write_reports(ledger, out_dir)
    _link_latest(out_dir)
    h = ledger.header
    if not quiet:
        _print_summary(ledger)
    typer.echo(f"report: {out_dir}")
    if not h.read_only.verified:
        typer.echo("READ-ONLY VIOLATION: the paper directory changed during the run:", err=True)
        for c in h.read_only.changes:
            typer.echo(f"  {c}", err=True)
        raise typer.Exit(EXIT_READONLY)
    raise typer.Exit(EXIT_BLOCKERS if h.verdict == "FAIL" else EXIT_PASS)


def _link_latest(out_dir: Path) -> None:
    latest = out_dir.parent / "latest"
    try:
        if latest.is_symlink() or not latest.exists():
            if latest.is_symlink():
                latest.unlink()
            latest.symlink_to(out_dir.name)
    except OSError:
        pass


def _print_summary(ledger) -> None:
    h = ledger.header
    c = h.counts
    typer.echo(f"{h.venue_name} [{h.mode}] {h.main_file}: {h.verdict}  "
               f"BLOCKER {c.get('BLOCKER', 0)}  WARN {c.get('WARN', 0)}  INFO {c.get('INFO', 0)}")
    ro = "verified" if h.read_only.verified else "FAILED"
    typer.echo(f"read-only: {ro} ({h.read_only.files_hashed} files hashed)")
    for f in ledger.findings:
        if f.severity.value == "BLOCKER":
            typer.echo(f"  {f.id:>4} BLOCKER {f.check_id:<28} {f.location}  {f.message[:110]}")


@app.command()
def report(
    report_dir: Annotated[Path, typer.Argument(help="Directory containing findings.json.")],
    fmt: Annotated[str, typer.Option("--format", help="md, html or both")] = "both",
    stdout: Annotated[bool, typer.Option("--stdout", help="Print the Markdown report.")] = False,
) -> None:
    """Re-render report.md / report.html from findings.json."""
    from .ledger import read_ledger
    from .render import render_html, render_markdown

    try:
        ledger = read_ledger(report_dir)
    except FileNotFoundError as e:
        _die(str(e))
    if fmt in ("md", "both"):
        (report_dir / "report.md").write_text(render_markdown(ledger), encoding="utf-8")
    if fmt in ("html", "both"):
        (report_dir / "report.html").write_text(render_html(ledger), encoding="utf-8")
    if stdout:
        typer.echo(render_markdown(ledger))
    else:
        typer.echo(f"rendered: {report_dir}")


@app.command()
def diff(
    old_report: Annotated[Path, typer.Argument()],
    new_report: Annotated[Path, typer.Argument()],
    as_json: Annotated[bool, typer.Option("--json")] = False,
) -> None:
    """Resolved / new / persisting findings between two runs (matched by fingerprint)."""
    from .diffing import diff_ledgers, format_diff
    from .ledger import read_ledger

    try:
        d = diff_ledgers(read_ledger(old_report), read_ledger(new_report))
    except FileNotFoundError as e:
        _die(str(e))
    typer.echo(d.model_dump_json(indent=2) if as_json else format_diff(d))


@app.command()
def apply(
    paper_dir: Annotated[Path, typer.Argument()],
    report_dir: Annotated[Path, typer.Argument()],
    findings: Annotated[str, typer.Option("--findings", help="Comma-separated finding IDs, e.g. F3,F7.")],
    branch: Annotated[Optional[str], typer.Option("--branch", help="Name of the new branch.")] = None,
    no_commit: Annotated[bool, typer.Option("--no-commit", help="Leave the changes uncommitted on the branch.")] = False,
    no_recheck: Annotated[bool, typer.Option("--no-recheck", help="Do not re-run check afterwards.")] = False,
) -> None:
    """Apply the patches of the named findings on a new git branch, then re-run check."""
    from .apply import ApplyError, apply_findings

    ids = [x.strip() for x in findings.split(",") if x.strip()]
    if not ids:
        _die("--findings is empty")
    try:
        res = apply_findings(paper_dir.expanduser().resolve(), report_dir.expanduser().resolve(), ids,
                             branch=branch, commit=not no_commit, recheck=not no_recheck)
    except ApplyError as e:
        _die(str(e))
    typer.echo(res)


@app.command("measure-template")
def measure_template(
    template_dir: Annotated[Path, typer.Argument(help="Directory with the official template's example paper.")],
    main: Annotated[str, typer.Option("--main", help="Example .tex file, e.g. root.tex.")],
) -> None:
    """Compile an official example (in a temporary copy) and print template.layout for a venue config."""
    from .workspace import Workspace

    ws = Workspace(template_dir.expanduser().resolve())
    try:
        b = ws.build(main)
    finally:
        ws.cleanup()
    if not b.layout:
        _die("layout probe did not run (the example failed to compile)")
    keys = ("paperwidth", "paperheight", "textwidth", "textheight", "oddsidemargin", "topmargin", "headheight",
            "headsep", "footskip", "columnsep", "columnwidth")
    typer.echo("  layout: {" + ", ".join(f"{k}: {b.layout[k]}" for k in keys if k in b.layout) + "}")


@app.command("list-checks")
def list_checks(markdown: Annotated[bool, typer.Option("--markdown", help="Markdown table.")] = False) -> None:
    """List every registered check (id, stage, default severity, modes, requirements)."""
    from .registry import load_checks

    rows = sorted(load_checks().values(), key=lambda c: (c.stage, c.id))
    if markdown:
        typer.echo("| Check | Stage | Default severity | Modes | Needs | Source |\n|---|---|---|---|---|---|")
    for c in rows:
        modes = "both" if len(c.applies_to_modes) == 2 else c.applies_to_modes[0]
        needs = ", ".join(sorted(c.requires)) or "-"
        if markdown:
            typer.echo(f"| `{c.id}` | {c.stage} | {c.severity.value} | {modes} | {needs} | {c.source} |")
        else:
            typer.echo(f"{c.stage}  {c.id:<34} {c.severity.value:<7} {modes:<12} {needs:<14} {c.source}")


@app.command()
def version() -> None:
    """Print the papergate version."""
    typer.echo(__version__)


def main() -> None:
    app()


if __name__ == "__main__":
    sys.exit(main())
