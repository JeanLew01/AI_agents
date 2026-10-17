"""Milestone 6: stage 7 (figures) and the shipped venue configs."""

from __future__ import annotations

from pathlib import Path

import numpy as np
from typer.testing import CliRunner

from conftest import FIXTURES, find, line_of, needs_tex, run_fixture
from papergate.checks.stage7_figures import collapses, palette, parse_length
from papergate.cli import app
from papergate.config import load_config

VENUES = Path(__file__).resolve().parents[1] / "venues"


@needs_tex
def test_figure_checks_on_fixture():
    led = run_fixture("figures")
    cap = find(led, "figures.captions", "WARN")
    assert len(cap) == 1 and "empty" in cap[0].message and cap[0].location.line == line_of("figures", "main.tex", "\\caption{}")
    ts = find(led, "figures.text_size", "WARN")
    assert len(ts) == 1 and "plot_tiny.pdf" in ts[0].message
    col = find(led, "figures.colors", "WARN")
    assert len(col) == 1 and "plot_redgreen.png" in col[0].message and "deuteranopia" in col[0].message
    sizes = {m["figure"]: m["median_pt"] for m in led.metrics["figure_text"]["measured"]}
    assert sizes["fig/plot.pdf"] > 8 and sizes["fig/plot_tiny.pdf"] < 3


@needs_tex
def test_clean_has_no_figure_findings():
    assert [f.check_id for f in run_fixture("clean").findings if f.stage == 7] == []


def test_palette_and_cvd_collapse():
    img = np.full((100, 200, 3), 255, np.uint8)
    img[:, :100] = (214, 39, 40)   # red
    img[:, 100:] = (44, 160, 44)   # green
    res = collapses(palette(img))
    assert res["deuteranopia"]
    img[:, 100:] = (31, 119, 180)  # blue instead: safe
    res = collapses(palette(img))
    assert not res["deuteranopia"] and not res["protanopia"]


def test_parse_length():
    lay = {"textwidth": 500.0}
    assert parse_length("0.5\\linewidth", 400.0, lay) == 200.0
    assert parse_length("\\textwidth", 400.0, lay) == 500.0
    assert abs(parse_length("1in", 400.0, lay) - 72.27) < 1e-9
    assert parse_length("\\figwidth", 400.0, lay) is None


def test_shipped_venue_configs_load():
    corl = load_config(VENUES / "corl2026.yaml")
    assert corl.page_limit.submission == 8 and corl.page_limit.camera_ready == 9
    assert corl.final_mode_markers[0].option == "final" and corl.todo
    icra = load_config(VENUES / "icra2027.yaml")
    assert icra.page_limit.excluded_sections == [] and "template.layout" in icra.todo


@needs_tex
def test_measure_template_cli():
    r = CliRunner().invoke(app, ["measure-template", str(FIXTURES / "_base"), "--main", "main.tex"])
    assert r.exit_code == 0 and "textwidth: 397.48499" in r.output
