"""Milestone 4: report rendering, diff across runs, apply on a git branch."""

from __future__ import annotations

import shutil
import subprocess

import pytest
from typer.testing import CliRunner

from conftest import FIXTURES, VENUE, find, needs_tex, run_fixture
from papergate.apply import ApplyError, apply_findings
from papergate.cli import app
from papergate.config import load_config
from papergate.context import Options
from papergate.diffing import diff_ledgers
from papergate.ledger import read_ledger, write_ledger
from papergate.pipeline import run_check
from papergate.render import render_html, render_markdown, write_reports

GIT = ["git", "-c", "user.name=Test", "-c", "user.email=test@example.org"]


def _repo(tmp_path, fixture="editing_artifacts"):
    paper = tmp_path / "paper"
    shutil.copytree(FIXTURES / fixture, paper)
    subprocess.run(["git", "init", "-q", "-b", "main"], cwd=paper, check=True)
    subprocess.run(GIT + ["add", "-A"], cwd=paper, check=True)
    subprocess.run(GIT + ["commit", "-q", "-m", "init"], cwd=paper, check=True)
    return paper


def _check(paper, out, only=("artifacts",)):
    led = run_check(paper, load_config(VENUE), "camera-ready", Options(no_llm=True, only=list(only)),
                    venue_path=str(VENUE))
    write_ledger(led, out)
    write_reports(led, out)
    return led


@needs_tex
def test_reports_render_all_sections():
    led = run_fixture("editing_artifacts")
    md, html = render_markdown(led), render_html(led)
    for f in led.findings:
        assert f"### {f.id} " in md and f'id="{f.id}"' in html
    assert "- [ ] Upload the signed licence form." in md
    assert "Read-only verification | PASSED" in md
    assert "```diff" in md and "<details>" in html


def test_diff_tracks_findings_across_line_shifts(tmp_path):
    paper = tmp_path / "p"
    shutil.copytree(FIXTURES / "editing_artifacts", paper)
    a = _check(paper, tmp_path / "r1")
    main = paper / "main.tex"
    text = main.read_text()
    text = text.replace("\\documentclass[letterpaper,10pt]{article}\n", "\\documentclass[letterpaper,10pt]{article}\n% shifted\n% lines\n")
    text = text.replace("\\hl{certified safe}", "certified safe")
    main.write_text(text + "\n\\iffalse\n\\fi\n")
    (paper / "sec" / "method.tex").write_text((paper / "sec" / "method.tex").read_text().replace("practice~", "practice~\\todo{check}"))
    b = _check(paper, tmp_path / "r2")
    d = diff_ledgers(a, b)
    assert [f.check_id for f in d.resolved] == ["artifacts.highlight"]
    assert [f.check_id for f in d.new] == ["artifacts.todo"]
    assert {p.finding.check_id for p in d.persisting} >= {"artifacts.todo", "artifacts.color", "artifacts.markers"}
    r = CliRunner().invoke(app, ["diff", str(tmp_path / "r1"), str(tmp_path / "r2")])
    assert r.exit_code == 0 and "resolved: 1" in r.output and "new: 1" in r.output


def test_apply_creates_branch_commits_and_rechecks(tmp_path):
    paper = _repo(tmp_path)
    rep = tmp_path / "rep"
    led = _check(paper, rep)
    todo = find(led, "artifacts.todo")[0]
    hl = find(led, "artifacts.highlight")[0]
    msg = apply_findings(paper, rep, [todo.id, hl.id])
    branch = subprocess.run(["git", "branch", "--show-current"], cwd=paper, capture_output=True, text=True).stdout.strip()
    assert branch.startswith("papergate/fix-") and "committed" in msg
    text = (paper / "main.tex").read_text()
    assert "\\todo{" not in text and "\\hl{" not in text and "\\textcolor{red}" in text  # only the named ones
    assert subprocess.run(["git", "status", "--porcelain"], cwd=paper, capture_output=True, text=True).stdout == ""
    log = subprocess.run(["git", "log", "-1", "--format=%s"], cwd=paper, capture_output=True, text=True).stdout
    assert todo.id in log and hl.id in log
    after = read_ledger(tmp_path / "rep-after-apply")
    assert not find(after, "artifacts.todo") and not find(after, "artifacts.highlight")
    assert "resolved: 2" in msg
    subprocess.run(["git", "switch", "-q", "main"], cwd=paper, check=True)
    assert "\\todo{" in (paper / "main.tex").read_text()  # main branch untouched


def test_apply_refusals(tmp_path):
    paper = _repo(tmp_path)
    rep = tmp_path / "rep"
    led = _check(paper, rep)
    manual = find(led, "artifacts.markers")[0]
    with pytest.raises(ApplyError, match="without a patch"):
        apply_findings(paper, rep, [manual.id], recheck=False)
    with pytest.raises(ApplyError, match="unknown finding"):
        apply_findings(paper, rep, ["F999"], recheck=False)
    (paper / "main.tex").write_text((paper / "main.tex").read_text() + "% dirty\n")
    with pytest.raises(ApplyError, match="uncommitted changes"):
        apply_findings(paper, rep, [find(led, "artifacts.todo")[0].id], recheck=False)
    # committed change that breaks the patch context
    text = (paper / "main.tex").read_text().replace("\\todo{cite an MPC survey}", "\\todo{cite two MPC surveys}")
    (paper / "main.tex").write_text(text)
    subprocess.run(GIT + ["commit", "-q", "-am", "edit"], cwd=paper, check=True)
    with pytest.raises(ApplyError, match="no longer applies cleanly"):
        apply_findings(paper, rep, [find(led, "artifacts.todo")[0].id], recheck=False)
    branches = subprocess.run(["git", "branch"], cwd=paper, capture_output=True, text=True).stdout
    assert "papergate/" not in branches


def test_apply_refuses_outside_git(tmp_path):
    paper = tmp_path / "p"
    shutil.copytree(FIXTURES / "editing_artifacts", paper)
    rep = tmp_path / "rep"
    led = _check(paper, rep)
    with pytest.raises(ApplyError, match="not inside a git repository"):
        apply_findings(paper, rep, [find(led, "artifacts.todo")[0].id], recheck=False)


def test_apply_in_subdirectory_of_repo(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    shutil.copytree(FIXTURES / "editing_artifacts", repo / "paper")
    subprocess.run(["git", "init", "-q", "-b", "main"], cwd=repo, check=True)
    subprocess.run(GIT + ["add", "-A"], cwd=repo, check=True)
    subprocess.run(GIT + ["commit", "-q", "-m", "init"], cwd=repo, check=True)
    rep = tmp_path / "rep"
    led = _check(repo / "paper", rep)
    apply_findings(repo / "paper", rep, [find(led, "artifacts.highlight")[0].id], recheck=False)
    assert "\\hl{" not in (repo / "paper" / "main.tex").read_text()
