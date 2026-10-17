"""Milestone 1: config loader, registry, ledger, read-only guard, CLI plumbing."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest
from typer.testing import CliRunner

from conftest import FIXTURES, VENUE, find, needs_tex, run_fixture
from papergate.cli import app
from papergate.config import ConfigError, load_config
from papergate.guard import ReadOnlyGuard, compare, snapshot
from papergate.ledger import finalize, read_ledger, write_ledger
from papergate.models import Finding, Ledger, Location, RunHeader, Severity
from papergate.registry import REGISTRY, Check, load_checks, register, select, unregister


def test_config_loads_and_resolves_paths():
    cfg = load_config(VENUE)
    assert cfg.page_limit.for_mode("camera-ready") == 3
    assert cfg.page_limit.for_mode("submission") == 2
    assert Path(cfg.template.official_path).is_file()
    assert [s.name for s in cfg.sections_for("required", "camera-ready")] == ["Limitations", "Acknowledgments"]
    assert cfg.notes_for("submission") == ["Check the supplementary video length."]
    assert len(cfg.config_hash) == 16


def test_config_extends_and_rejects_unknown_keys(tmp_path):
    child = tmp_path / "paper.yaml"
    child.write_text(f"extends: {VENUE}\nauthors: []\npage_limit: {{camera_ready: 9}}\n")
    cfg = load_config(child)
    assert cfg.page_limit.camera_ready == 9 and cfg.page_limit.submission == 2  # deep merge
    assert cfg.authors == []
    bad = tmp_path / "bad.yaml"
    bad.write_text("name: x\npage_limits: 3\n")
    with pytest.raises(ConfigError):
        load_config(bad)


def test_registry_rejects_duplicates_and_selects_by_prefix():
    load_checks()

    class Dup(Check):
        id = "config.unconfirmed"
        stage = 0

    with pytest.raises(ValueError):
        register(Dup)
    ids = [c.id for c in select("camera-ready", ["config"])]
    assert ids == ["config.unconfirmed"]


def test_guard_detects_add_modify_remove(tmp_path):
    (tmp_path / "a.tex").write_text("x")
    (tmp_path / "sub").mkdir()
    (tmp_path / "sub" / "b.tex").write_text("y")
    before = snapshot(tmp_path)
    (tmp_path / "a.tex").write_text("x2")
    (tmp_path / "sub" / "b.tex").unlink()
    (tmp_path / "c.aux").write_text("z")
    changes = compare(before, snapshot(tmp_path))
    assert changes == ["removed: sub/b.tex", "added: c.aux", "modified: a.tex"]


def _ledger(findings):
    h = RunHeader(tool_version="0", paper_dir="/p", venue_name="v", venue_config="c", venue_config_hash="h",
                  mode="camera-ready", source_tree_hash="t", started="now")
    h.read_only.verified = True
    return Ledger(header=h, findings=findings)


def test_fingerprint_ignores_line_numbers_and_ids_follow_severity():
    cfg = load_config(VENUE)
    a = Finding(check_id="x.y", stage=1, severity=Severity.WARN, message="m", quote="q  text",
                location=Location(file="main.tex", line=10))
    b = Finding(check_id="x.y", stage=1, severity=Severity.BLOCKER, message="m2", quote="other",
                location=Location(file="main.tex", line=3))
    l1 = finalize(_ledger([a.model_copy(), b.model_copy()]), cfg)
    moved = a.model_copy(update={"location": Location(file="main.tex", line=42), "quote": "q text"})
    l2 = finalize(_ledger([moved, b.model_copy()]), cfg)
    assert [f.id for f in l1.findings] == ["F1", "F2"] and l1.findings[0].severity == Severity.BLOCKER
    assert {f.fingerprint for f in l1.findings} == {f.fingerprint for f in l2.findings}
    assert l1.header.verdict == "FAIL"


def test_ledger_roundtrip(tmp_path):
    cfg = load_config(VENUE)
    led = finalize(_ledger([Finding(check_id="a", stage=0, severity=Severity.INFO, message="m")]), cfg)
    write_ledger(led, tmp_path)
    assert read_ledger(tmp_path).findings[0].id == "F1"
    data = json.loads((tmp_path / "findings.json").read_text())
    assert set(data) == {"header", "findings", "manual_checklist", "metrics"}


def _tree_bytes(root: Path) -> dict[str, bytes]:
    return {p.relative_to(root).as_posix(): p.read_bytes() for p in sorted(root.rglob("*")) if p.is_file()}


@needs_tex
def test_check_leaves_fixture_byte_identical():
    before = _tree_bytes(FIXTURES / "clean")
    led = run_fixture("clean")
    assert _tree_bytes(FIXTURES / "clean") == before
    assert led.header.read_only.verified and led.header.read_only.files_hashed >= 5
    assert led.header.main_file == "main.tex"


def test_guard_fails_run_when_a_check_writes_into_the_paper(tmp_path):
    paper = tmp_path / "paper"
    shutil.copytree(FIXTURES / "clean", paper)

    @register
    class Vandal(Check):
        id = "test.vandal"
        stage = 0

        def run(self, ctx):
            (ctx.paper_dir / "main.aux").write_text("oops")
            return []

    try:
        from papergate.context import Options
        from papergate.pipeline import run_check

        led = run_check(paper, load_config(VENUE), "camera-ready", Options(only=["test.vandal"]))
        assert led.header.verdict == "ERROR"
        assert led.header.read_only.changes == ["added: main.aux"]
    finally:
        unregister("test.vandal")


def test_crashing_check_becomes_info_finding(tmp_path):
    @register
    class Boom(Check):
        id = "test.boom"
        stage = 0

        def run(self, ctx):
            raise RuntimeError("kaputt")

    try:
        from papergate.context import Options
        from papergate.pipeline import run_check

        led = run_check(FIXTURES / "clean", load_config(VENUE), "camera-ready", Options(only=["test.boom"]))
        assert led.header.checks_crashed[0].check_id == "test.boom"
        assert find(led, "test.boom", "INFO")
        assert led.header.read_only.verified
    finally:
        unregister("test.boom")


def test_cli_refuses_report_dir_inside_paper(tmp_path):
    paper = tmp_path / "paper"
    shutil.copytree(FIXTURES / "clean", paper)
    r = CliRunner().invoke(app, ["check", str(paper), "--venue", str(VENUE), "--out", str(paper / "rep"),
                                 "--no-llm"])
    assert r.exit_code == 2 and "inside the paper directory" in r.output
    assert not (paper / "rep").exists()


def test_cli_check_and_report(tmp_path):
    out = tmp_path / "rep"
    r = CliRunner().invoke(app, ["check", str(FIXTURES / "clean"), "--venue", str(VENUE), "--out", str(out),
                                 "--no-llm", "--only", "config,project", "-q"])
    assert r.exit_code == 0, r.output
    assert (out / "findings.json").is_file() and (out / "report.md").is_file() and (out / "report.html").is_file()
    (out / "report.md").unlink()
    r = CliRunner().invoke(app, ["report", str(out)])
    assert r.exit_code == 0 and (out / "report.md").is_file()
