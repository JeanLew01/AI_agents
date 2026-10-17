"""`papergate apply`: the only code path that modifies a paper. It applies the stored patches of
explicitly named findings on a new git branch, commits them there, and re-runs the check."""

from __future__ import annotations

import datetime as dt
import re
import subprocess
from pathlib import Path

from .ledger import read_ledger, write_ledger


class ApplyError(Exception):
    pass


def _git(args: list[str], cwd: Path, input: str | None = None, check: bool = True) -> subprocess.CompletedProcess:
    p = subprocess.run(["git", *args], cwd=cwd, input=input, text=True, capture_output=True)
    if check and p.returncode != 0:
        raise ApplyError(f"git {' '.join(args)} failed: {p.stderr.strip() or p.stdout.strip()}")
    return p


def _patch_files(patch: str) -> list[str]:
    return sorted(set(re.findall(r"^\+\+\+ b/(.+)$", patch, re.M)))


def apply_findings(paper_dir: Path, report_dir: Path, ids: list[str], branch: str | None = None,
                   commit: bool = True, recheck: bool = True) -> str:
    ledger = read_ledger(report_dir)
    if Path(ledger.header.paper_dir).resolve() != paper_dir.resolve():
        raise ApplyError(f"the report was produced for {ledger.header.paper_dir}, not {paper_dir}")
    top_p = _git(["rev-parse", "--show-toplevel"], paper_dir, check=False)
    if top_p.returncode != 0:
        raise ApplyError(f"{paper_dir} is not inside a git repository")
    top = Path(top_p.stdout.strip())
    rel = paper_dir.resolve().relative_to(top.resolve()).as_posix()
    rel = "" if rel == "." else rel
    dirty = _git(["status", "--porcelain", "--untracked-files=all", "--", "."], paper_dir).stdout.strip()
    if dirty:
        raise ApplyError("the paper directory has uncommitted changes; commit or stash them first:\n" + dirty)

    by_id = {f.id: f for f in ledger.findings}
    unknown = [i for i in ids if i not in by_id]
    if unknown:
        raise ApplyError(f"unknown finding id(s): {', '.join(unknown)}")
    nopatch = [i for i in ids if by_id[i].fix.kind != "patch" or not by_id[i].fix.patch]
    if nopatch:
        raise ApplyError(f"finding(s) without a patch (manual fixes): {', '.join(nopatch)}")
    dir_args = [f"--directory={rel}"] if rel else []
    for i in ids:  # every patch must apply to HEAD on its own before anything is touched
        p = _git(["apply", "--check", *dir_args, "-"], top, input=by_id[i].fix.patch, check=False)
        if p.returncode != 0:
            raise ApplyError(f"{i} no longer applies cleanly (re-run check): {p.stderr.strip()}")

    head = _git(["rev-parse", "--abbrev-ref", "HEAD"], top).stdout.strip()
    if head == "HEAD":
        head = _git(["rev-parse", "HEAD"], top).stdout.strip()
    branch = branch or f"papergate/fix-{dt.datetime.now().strftime('%Y%m%d-%H%M%S')}"
    if _git(["rev-parse", "--verify", "--quiet", f"refs/heads/{branch}"], top, check=False).returncode == 0:
        raise ApplyError(f"branch {branch} already exists")
    _git(["switch", "-c", branch], top)
    touched: list[str] = []
    try:
        for i in ids:
            patch = by_id[i].fix.patch
            p = _git(["apply", *dir_args, "-"], top, input=patch, check=False)
            if p.returncode != 0:  # an earlier patch in the set changed this patch's context lines
                p = _git(["apply", "-C1", *dir_args, "-"], top, input=patch, check=False)
            if p.returncode != 0:
                raise ApplyError(f"{i} conflicts with an earlier patch in this set: {p.stderr.strip()}")
            touched += [f"{rel}/{f}" if rel else f for f in _patch_files(patch)]
    except ApplyError:
        if touched:
            _git(["checkout", "--", *sorted(set(touched))], top, check=False)
        _git(["switch", head], top, check=False)
        _git(["branch", "-D", branch], top, check=False)
        raise
    touched = sorted(set(touched))
    lines = [f"created branch {branch} (from {head}); patched: {', '.join(touched)}"]
    if commit:
        _git(["add", "--", *touched], top)
        msg = "papergate: apply " + ", ".join(ids) + "\n\n" + "\n".join(
            f"- {i} {by_id[i].check_id}: {by_id[i].message[:100]}" for i in ids)
        c = _git(["commit", "-q", "-m", msg], top, check=False)
        if c.returncode == 0:
            sha = _git(["rev-parse", "--short", "HEAD"], top).stdout.strip()
            lines.append(f"committed {sha} on {branch}; review with: git -C {top} diff {head}..{branch}")
        else:
            lines.append(f"commit failed ({c.stderr.strip()}); changes are staged on {branch}")
    else:
        lines.append(f"changes left uncommitted on {branch}; review with: git -C {top} diff")
    lines.append(f"to go back: git -C {top} switch {head}")
    if recheck:
        lines.append(_recheck(paper_dir, report_dir, ledger))
    return "\n".join(lines)


def _recheck(paper_dir: Path, report_dir: Path, old) -> str:
    from .config import load_config
    from .context import Options
    from .diffing import diff_ledgers, format_diff
    from .pipeline import run_check
    from .render import write_reports

    inv = old.header.invocation
    if not inv.get("venue"):
        return "re-check skipped: the report does not record the venue config"
    out = report_dir.parent / f"{report_dir.name}-after-apply"
    n = 2
    while out.exists():
        out = report_dir.parent / f"{report_dir.name}-after-apply-{n}"
        n += 1
    opts = Options(rebuttal=Path(inv["rebuttal"]) if inv.get("rebuttal") else None, no_llm=True,
                   only=inv.get("only") or [], online=bool(inv.get("online")), main=inv.get("main"),
                   supplementary=[Path(p) for p in inv.get("supplementary") or []])
    led = run_check(paper_dir, load_config(inv["venue"]), inv.get("mode", old.header.mode), opts,
                    venue_path=inv["venue"])
    write_ledger(led, out)
    write_reports(led, out)
    return f"re-check (LLM stages off) written to {out}\n" + format_diff(diff_ledgers(old, led))
