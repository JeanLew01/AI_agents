"""Milestone 2: stage 1 (build) and stage 2 (PDF compliance, template integrity)."""

from __future__ import annotations

import shutil

from conftest import FIXTURES, VENUE, find, line_of, needs_tex, run_fixture
from papergate.checks.stage2_pdf import link_problem
from papergate.config import load_config
from papergate.context import Options
from papergate.pdf.doc import parse_pdffonts
from papergate.pipeline import run_check
from papergate.tex.logparse import parse_blg, parse_log

LOG = """This is pdfTeX
(./main.tex (/usr/share/texlive/texmf-dist/tex/latex/base/article.cls (/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))
(./sec/method.tex
Overfull \\hbox (12.5pt too wide) in paragraph at lines 7--9
[]\\T1/lmr/m/n/10 some (unbalanced text
[]

) [1]
Overfull \\hbox (3.1pt too wide) in paragraph at lines 40--41
[]\\T1/lmr/m/n/10 x

LaTeX Warning: Reference `sec:x' on page 1 undefined on input line 44.
LaTeX Warning: Citation `foo' on page 1 undefined on input line 45.
Package natbib Warning: Citation `bar' on page 1 undefined on input line 46.
LaTeX Warning: Label `dup' multiply defined.
./main.tex:50: Undefined control sequence.
l.50 \\foo
LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.
)
"""


def test_parse_log_tracks_files_and_messages():
    p = parse_log(LOG)
    assert [(b.file, b.line, b.amount_pt) for b in p.boxes] == [("sec/method.tex", 7, 12.5), ("main.tex", 40, 3.1)]
    assert p.undefined_refs == ["sec:x"] and p.undefined_cites == ["foo", "bar"]
    assert p.multiply_defined == ["dup"] and p.labels_changed
    assert (p.errors[0].file, p.errors[0].line) == ("main.tex", 50)


def test_parse_blg_bibtex_and_biber():
    blg = ("Warning--empty journal in smith2020\n"
           "I was expecting a `,' or a `}'---line 12 of file refs.bib\n"
           "[42] Biber.pm:131> WARN - Duplicate entry key 'x1' in file 'refs.bib', skipping ...\n")
    msgs = parse_blg(blg)
    assert (msgs[0].level, msgs[0].key) == ("warning", "smith2020")
    assert (msgs[1].level, msgs[1].bibfile, msgs[1].line) == ("error", "refs.bib", 12)
    assert msgs[2].level == "warning"


def test_parse_pdffonts_handles_spaces_in_type():
    out = ("name                                 type              encoding         emb sub uni object ID\n"
           "------------------------------------ ----------------- ---------------- --- --- --- ---------\n"
           "ABCDEF+DejaVuSans                    Type 3            Custom           yes yes yes     17  0\n"
           "Helvetica                            Type 1            WinAnsi          no  no  no      20  0\n")
    f = parse_pdffonts(out)
    assert [(x.name, x.type, x.embedded) for x in f] == [("ABCDEF+DejaVuSans", "Type 3", True), ("Helvetica", "Type 1", False)]


def test_link_problems():
    assert link_problem("https://github.com/x/y") is None
    assert "local host" in link_problem("http://localhost:8000/demo")
    assert "private" in link_problem("http://192.168.1.4/x")
    assert "local file" in link_problem("file:///home/me/video.mp4")
    assert link_problem("mailto:a@b.org") is None


@needs_tex
def test_clean_has_no_stage1_or_stage2_findings():
    led = run_fixture("clean")
    assert led.header.counts["BLOCKER"] == 0
    assert [f.check_id for f in led.findings if f.stage in (1, 2)] == []
    assert led.metrics["pages"]["pages"] == 2 and led.metrics["pages"]["limit"] == 3


@needs_tex
def test_undefined_ref_located():
    led = run_fixture("undefined_ref")
    f = find(led, "build.undefined_ref", "BLOCKER")
    assert len(f) == 1
    assert (f[0].location.file, f[0].location.line) == ("main.tex", line_of("undefined_ref", "main.tex", "\\ref{sec:setup}"))
    assert "sec:setup" in f[0].message


@needs_tex
def test_over_page_limit():
    led = run_fixture("over_page_limit")
    f = find(led, "pdf.page_limit", "BLOCKER")
    assert len(f) == 1 and "limit is 3" in f[0].message
    assert led.metrics["pages"]["pages"] > 3


@needs_tex
def test_type3_font_attributed_to_figure():
    led = run_fixture("type3_font")
    f = find(led, "pdf.fonts.type3", "BLOCKER")
    assert len(f) == 1
    assert (f[0].location.file, f[0].location.line) == ("main.tex", line_of("type3_font", "main.tex", "plot_type3.pdf"))
    assert "fig/plot_type3.pdf" in f[0].message and "pdf.fonttype" in f[0].fix.instructions


@needs_tex
def test_template_hacks_and_margin_ink():
    led = run_fixture("template_hacks")
    ls = find(led, "template.linespread", "BLOCKER")
    assert ls and ls[0].location.line == line_of("template_hacks", "main.tex", "\\linespread")
    assert find(led, "template.negative_vspace", "WARN")[0].location.line == line_of("template_hacks", "main.tex", "\\vspace{-6pt}")
    assert find(led, "template.spacing", "WARN")
    m = find(led, "pdf.margins", "WARN")
    assert len(m) == 1 and "left margin" in m[0].message and "GDP" in m[0].quote


@needs_tex
def test_modified_template_and_geometry(tmp_path):
    paper = tmp_path / "paper"
    shutil.copytree(FIXTURES / "clean", paper)
    (paper / "pgtest.sty").write_text((paper / "pgtest.sty").read_text().replace("9in", "9.5in"))
    main = paper / "main.tex"
    main.write_text(main.read_text().replace("\\usepackage{booktabs}", "\\usepackage{booktabs}\n\\usepackage[margin=0.8in]{geometry}"))
    led = run_check(paper, load_config(VENUE), "camera-ready", Options(no_llm=True, only=["template", "pdf.margins"]))
    assert find(led, "template.file", "BLOCKER") and "differs from the official" in find(led, "template.file")[0].message
    assert "9.5in" in find(led, "template.file")[0].fix.instructions  # diff against the official copy
    assert find(led, "template.geometry", "BLOCKER")[0].location.line == 8
    lay = find(led, "template.layout", "BLOCKER")
    assert lay and "textheight" in lay[0].message
