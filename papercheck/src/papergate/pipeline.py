"""Runs the selected checks inside the read-only guard and aggregates the findings."""

from __future__ import annotations

import datetime as dt
import traceback
from pathlib import Path

from . import __version__
from .config import VenueConfig
from .context import CheckContext, Options
from .guard import ReadOnlyGuard, tree_hash
from .ledger import finalize
from .models import CrashedCheck, Finding, Ledger, RunHeader, Severity, SkippedCheck
from .registry import SkipCheck, select


def _now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def run_check(paper_dir: Path, config: VenueConfig, mode: str, options: Options,
              llm=None, venue_path: str = "") -> Ledger:
    from .llm.base import NullBackend

    paper_dir = Path(paper_dir).resolve()
    llm = llm if llm is not None else NullBackend()
    guard = ReadOnlyGuard(paper_dir)
    guard.start()
    header = RunHeader(
        tool_version=__version__, paper_dir=str(paper_dir), venue_name=config.name,
        venue_config=venue_path, venue_config_hash=config.config_hash, mode=mode,
        source_tree_hash=tree_hash(guard.before), model=llm.model_name, started=_now(),
        unconfirmed_config=dict(config.todo),
        invocation={
            "venue": venue_path, "mode": mode,
            "rebuttal": str(options.rebuttal) if options.rebuttal else None,
            "no_llm": options.no_llm, "only": options.only, "online": options.online,
            "main": options.main, "supplementary": [str(p) for p in options.supplementary],
            "model": options.model,
        },
    )
    ctx = CheckContext(paper_dir, config, mode, options, llm)
    findings: list[Finding] = []
    try:
        try:
            header.main_file = ctx.project.main
        except Exception as e:  # no main file: report it, other checks will crash/skip
            findings.append(Finding(check_id="project.main", stage=0, severity=Severity.BLOCKER, mode=mode,
                                    message=str(e), why_it_matters="Nothing can be checked without a main file."))
        for cls in select(mode, options.only or None, config.is_disabled):
            reason = _unmet(cls, ctx)
            if reason:
                header.checks_skipped.append(SkippedCheck(check_id=cls.id, reason=reason))
                continue
            try:
                res = cls().run(ctx) or []
                header.checks_run.append(cls.id)
                findings.extend(res)
            except SkipCheck as e:
                header.checks_skipped.append(SkippedCheck(check_id=cls.id, reason=str(e)))
            except Exception as e:
                tb = traceback.format_exc(limit=4)
                header.checks_crashed.append(CrashedCheck(check_id=cls.id, error=f"{type(e).__name__}: {e}"))
                findings.append(Finding(check_id=cls.id, stage=cls.stage, severity=Severity.INFO, mode=mode,
                                        message=f"check crashed: {type(e).__name__}: {e}",
                                        why_it_matters="This check did not run; its defects are unknown.",
                                        quote="", fix={"kind": "manual", "instructions": tb}))
    finally:
        ctx.cleanup()
        changes = guard.finish()
        header.read_only.files_hashed = guard.files_hashed
        header.read_only.changes = changes
        header.read_only.verified = not changes
    header.discarded_unverifiable = ctx.discarded
    header.finished = _now()
    ledger = Ledger(header=header, findings=findings, manual_checklist=config.notes_for(mode),
                    metrics=ctx.metrics)
    return finalize(ledger, config)


def _unmet(cls, ctx: CheckContext) -> str | None:
    req = cls.requires
    if "llm" in req and (ctx.options.no_llm or not ctx.llm.available):
        return "LLM stage skipped (--no-llm or no LLM backend configured)"
    if "rebuttal" in req and ctx.options.rebuttal is None:
        return "no --rebuttal file given"
    if "online" in req and not ctx.options.online:
        return "needs --online"
    if "build" in req or "pdf" in req:
        try:
            b = ctx.build
        except Exception as e:
            return f"build could not run: {e}"
        if b is None:
            return "latexmk not found"
        if "pdf" in req and ctx.pdf is None:
            return "build produced no PDF"
    return None
