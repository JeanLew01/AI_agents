"""Milestone 3: stage 3 (identity, both modes, editing artifacts) and stage 4 (consistency)."""

from __future__ import annotations

import json
import shutil
import subprocess
import zipfile

import pytest

from conftest import FIXTURES, VENUE, find, line_of, needs_tex, run_fixture
from papergate.config import load_config
from papergate.context import Options
from papergate.pipeline import run_check


def _run(paper, mode="camera-ready", only=None, **kw):
    return run_check(paper, load_config(VENUE), mode, Options(no_llm=True, only=only or [], **kw))


def _git_apply_check(paper, patch: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "apply", "--check", "-"], input=patch, text=True, cwd=paper, capture_output=True)


@needs_tex
def test_clean_paper_has_no_stage3_or_stage4_findings():
    led = run_fixture("clean")
    assert [(f.check_id, f.message) for f in led.findings if f.stage in (3, 4)] == []


@needs_tex
def test_leftover_anonymous_author():
    led = run_fixture("leftover_anonymous")
    f = find(led, "identity.placeholder_authors", "BLOCKER")
    assert f and {x.location.line for x in f} == {line_of("leftover_anonymous", "main.tex", "\\author{Anonymous")}
    assert find(led, "identity.author_list", "BLOCKER")


@needs_tex
def test_author_order_mismatch():
    led = run_fixture("author_order")
    f = find(led, "identity.author_list", "BLOCKER")
    assert len(f) == 1 and "order differs" in f[0].message
    assert "Grace Hopper, Alan Turing" in f[0].message
    assert f[0].location.line == line_of("author_order", "main.tex", "\\author{")


@needs_tex
def test_missing_final_option_and_review_markers(tmp_path):
    paper = tmp_path / "p"
    shutil.copytree(FIXTURES / "clean", paper)
    (paper / "main.tex").write_text((paper / "main.tex").read_text().replace("\\usepackage[final]{pgtest}", "\\usepackage{pgtest}"))
    led = _run(paper, only=["identity"])
    fm = find(led, "identity.final_markers", "BLOCKER")
    assert len(fm) == 1 and fm[0].fix.kind == "patch"
    assert "+\\usepackage[final]{pgtest}" in fm[0].fix.patch
    subprocess.run(["git", "init", "-q"], cwd=paper, check=True)
    assert _git_apply_check(paper, fm[0].fix.patch).returncode == 0
    msgs = " | ".join(f.message for f in find(led, "identity.review_markers", "BLOCKER"))
    assert "Under review" in msgs and "line numbers" in msgs and "anonymous author block" in msgs


@needs_tex
def test_pdf_metadata_patch(tmp_path):
    paper = tmp_path / "p"
    shutil.copytree(FIXTURES / "clean", paper)
    main = paper / "main.tex"
    main.write_text(main.read_text().replace("\\hypersetup{pdftitle={Gated Diffusion Planning for Safe Navigation},\n"
                                             "  pdfauthor={Ada Lovelace, Alan Turing, Grace Hopper}}\n", ""))
    led = _run(paper, only=["identity.pdf_metadata"])
    f = find(led, "identity.pdf_metadata", "WARN")
    assert len(f) == 1 and "Title is empty" in f[0].message and f[0].fix.kind == "patch"
    assert "pdfauthor={Ada Lovelace, Alan Turing, Grace Hopper}" in f[0].fix.patch
    subprocess.run(["git", "init", "-q"], cwd=paper, check=True)
    assert _git_apply_check(paper, f[0].fix.patch).returncode == 0


@needs_tex
def test_submission_mode_identity_leaks():
    led = run_fixture("submission_leak", mode="submission")
    pdf = find(led, "identity.terms_pdf", "BLOCKER")
    assert any("metadata field author" in f.message for f in pdf)
    ack_line = line_of("submission_leak", "main.tex", "We thank the Analytical Engine Lab")
    assert any(f.location.line == ack_line and "Analytical Engine Lab" in f.message for f in pdf)
    assert find(led, "structure.forbidden_sections", "BLOCKER")
    sc = find(led, "identity.self_citation_phrasing", "WARN")
    assert sc and sc[0].location.file == "sec/method.tex" and sc[0].location.line == line_of("submission_leak", "sec/method.tex", "In our prior work")
    src = find(led, "identity.terms_source", "WARN")
    assert src and "comment" in src[0].message and src[0].location.line == line_of("submission_leak", "sec/method.tex", "% TODO(Ada")
    assert not find(led, "identity.final_markers")  # review mode is on


@needs_tex
def test_editing_artifacts_with_patches(tmp_path):
    led = run_fixture("editing_artifacts")
    todo = find(led, "artifacts.todo", "BLOCKER")
    assert todo and todo[0].fix.kind == "patch" and "-explicitly, yet it needs a good initial guess.\\todo{cite an MPC survey}" in todo[0].fix.patch
    hl = find(led, "artifacts.highlight", "WARN")[0]
    assert "+a plan only if it is certified safe." in hl.fix.patch
    col = find(led, "artifacts.color", "WARN")[0]
    added = [l for l in col.fix.patch.splitlines() if l.startswith("+") and not l.startswith("+++")]
    assert any("motion. NEW: The gate rejects" in l for l in added) and not any("textcolor" in l for l in added)
    assert find(led, "artifacts.markers", "WARN")[0].quote.startswith("assumptions")
    cb = find(led, "artifacts.commented_blocks", "WARN")
    assert cb and cb[0].location.line == line_of("editing_artifacts", "main.tex", "% \\section{Old conclusion}")
    paper = tmp_path / "p"
    shutil.copytree(FIXTURES / "editing_artifacts", paper)
    subprocess.run(["git", "init", "-q"], cwd=paper, check=True)
    for f in (todo[0], hl, col):
        assert _git_apply_check(paper, f.fix.patch).returncode == 0, f.fix.patch


@needs_tex
def test_consistency_fixture():
    led = run_fixture("consistency")
    uf = find(led, "consistency.unreferenced_floats", "WARN")
    assert len(uf) == 1 and "fig:plot" in uf[0].message
    ac = find(led, "text.acronyms", "WARN")
    assert len(ac) == 1 and "RRT" in ac[0].message and ac[0].location.line == line_of("consistency", "main.tex", "work well with RRT")
    dup = find(led, "bib.duplicates", "WARN")
    assert dup and "ho2020ddpm" in dup[0].message and "ho2020denoising" in dup[0].message
    assert find(led, "bib.venue_format", "WARN") and "NeurIPS" in find(led, "bib.venue_format")[0].message
    assert "chi2023diffusion" in find(led, "bib.arxiv_published", "INFO")[0].message
    assert "unused2021" in find(led, "bib.unused_entries", "INFO")[0].message
    rs = find(led, "math.restatements", "WARN")
    assert len(rs) == 1 and "2\\delta" in rs[0].message and "sec/method.tex" in rs[0].message


@needs_tex
def test_number_mismatch_reports_both_locations():
    led = run_fixture("number_mismatch")
    f = find(led, "consistency.numbers", "WARN")
    assert len(f) == 1
    assert f[0].location.line == line_of("number_mismatch", "main.tex", "87.5\\%")
    cell_line = line_of("number_mismatch", "main.tex", "GDP (ours) & 85.7")
    assert f"main.tex:{cell_line}" in f[0].message and "85.7" in f[0].message
    assert not find(run_fixture("clean"), "consistency.numbers")  # 40% is derived from the table


def test_notation_used_before_definition(tmp_path):
    (tmp_path / "main.tex").write_text(
        "\\documentclass{article}\n\\begin{document}\n\\section{Introduction}\nWe study control.\n\n"
        "\\section{Method}\nThe cost $J(\\mathcal{Z})$ is minimised.\n\n"
        "\\section{Preliminaries}\nLet $\\mathcal{Z}$ denote the latent space.\n\n"
        "Later, let $\\mathcal{Z}$ be the set of goals.\n\\end{document}\n")
    led = _run(tmp_path, only=["math.notation"])
    msgs = [f.message for f in find(led, "math.notation")]
    assert any("used before its definition" in m for m in msgs)
    assert any("defined again" in m for m in msgs)


def test_supplementary_archive_scan(tmp_path):
    paper = tmp_path / "p"
    shutil.copytree(FIXTURES / "clean", paper)
    supp = tmp_path / "supp.zip"
    nb = {"cells": [{"cell_type": "code", "source": ["load('/home/ada/data.npz')"], "outputs": []}], "metadata": {}}
    with zipfile.ZipFile(supp, "w") as z:
        z.writestr("code/.git/HEAD", "ref: refs/heads/main")
        z.writestr("code/run.py", "# author: Ada Lovelace\n")
        z.writestr("code/demo.ipynb", json.dumps(nb))
    led = _run(paper, mode="submission", only=["identity.supplementary"], supplementary=[supp])
    msgs = [f.message for f in find(led, "identity.supplementary")]
    assert any("git repository" in m for m in msgs)
    assert any("Ada Lovelace" in m for m in msgs)
    assert any("/home/ada" in m for m in msgs)
