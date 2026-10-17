"""Build the fixture papers from tests/fixtures/_base by seeding one defect (or one family of
defects) each. The generated directories are committed; rerun after editing _base or this file.
Usage: python tests/fixtures/_tools/make_fixtures.py"""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "_base"
COMMON = ROOT / "_common"

# name -> list of (file, old, new); `old` must occur exactly once.
FIXTURES: dict[str, list[tuple[str, str, str]]] = {
    "clean": [],
    "over_page_limit": [
        ("main.tex", r"\usepackage{booktabs}", "\\usepackage{booktabs}\n\\usepackage{lipsum}"),
        ("main.tex", "shows the success rate as the noise level grows.\n",
         "shows the success rate as the noise level grows.\n\n\\subsection{Extended evaluation}\n\\lipsum[1-14]\n"),
    ],
    "type3_font": [
        ("main.tex", r"\includegraphics[width=0.6\linewidth]{fig/plot.pdf}",
         r"\includegraphics[width=0.6\linewidth]{fig/plot_type3.pdf}"),
    ],
    "leftover_anonymous": [
        ("main.tex", "\\author{Ada Lovelace\\\\Analytical Engine Lab\\\\\\texttt{ada@test.edu}\n"
                     "  \\and Alan Turing\\\\Computable Numbers Inst.\\\\\\texttt{alan@icn.org}\n"
                     "  \\and Grace Hopper\\\\Compiler Research Center\\\\\\texttt{grace@crc.org}}",
         "\\author{Anonymous Author(s)}"),
    ],
    "author_order": [
        ("main.tex", "\\author{Ada Lovelace\\\\Analytical Engine Lab\\\\\\texttt{ada@test.edu}\n"
                     "  \\and Alan Turing\\\\Computable Numbers Inst.\\\\\\texttt{alan@icn.org}\n"
                     "  \\and Grace Hopper\\\\Compiler Research Center\\\\\\texttt{grace@crc.org}}",
         "\\author{Ada Lovelace\\\\Analytical Engine Lab\\\\\\texttt{ada@test.edu}\n"
         "  \\and Grace Hopper\\\\Compiler Research Center\\\\\\texttt{grace@crc.org}\n"
         "  \\and Alan Turing\\\\Computable Numbers Inst.\\\\\\texttt{alan@icn.org}}"),
    ],
    "undefined_ref": [
        ("main.tex", "We compare GDP with an MPC baseline on 200 navigation episodes.",
         "We compare GDP with an MPC baseline on 200 navigation episodes (setup in Section~\\ref{sec:setup})."),
    ],
    "number_mismatch": [
        ("main.tex", "certifies it. On a cluttered navigation benchmark the planner reaches a success rate of\n85.7\\%",
         "certifies it. On a cluttered navigation benchmark the planner reaches a success rate of\n87.5\\%"),
    ],
    "unused_assumption": [
        ("sec/method.tex", "per step. By Assumption~\\ref{asm:noise}, each step adds at most $\\sigma$. The scenario bound",
         "per step. Each step adds a bounded error. The scenario bound"),
    ],
    "rebuttal_unfulfilled": [],
    "submission_leak": [
        ("main.tex", r"\usepackage[final]{pgtest}", r"\usepackage{pgtest}"),
        ("main.tex", "\\acknowledgments{We thank the anonymous reviewers. This work was supported by grant GRANT-12345.}",
         "\\section*{Acknowledgments}\nWe thank the Analytical Engine Lab for support (grant GRANT-12345)."),
        ("sec/method.tex", "The planner draws $N$ candidate plans",
         "% TODO(Ada Lovelace): cite the workshop version\nIn our prior work~\\cite{campi2008exact} we analysed the gate. The planner draws $N$ candidate plans"),
    ],
    "editing_artifacts": [
        ("main.tex", r"\usepackage{booktabs}", "\\usepackage{booktabs}\n\\usepackage{todonotes}\n\\usepackage{soul}"),
        ("main.tex", "explicitly, yet it needs a good initial guess.",
         "explicitly, yet it needs a good initial guess.\\todo{cite an MPC survey}"),
        ("main.tex", "a plan only if it is certified safe.", "a plan only if it is \\hl{certified safe}."),
        ("main.tex", "The gate rejects\nplans conservatively,",
         "\\textcolor{red}{NEW: The gate rejects\nplans conservatively,}"),
        ("main.tex", "\\section{Conclusion}", "% \\section{Old conclusion}\n% We had a different story here.\n"
         "% It said GDP is always optimal.\n% Line four of the old text.\n% Line five of the old text.\n"
         "% Line six of the old text.\n% Line seven of the old text.\n% Line eight of the old text.\n"
         "% Line nine of the old text.\n% Line ten of the old text.\n% Line eleven of the old text.\n"
         "\\section{Conclusion}"),
    ],
    "consistency": [
        # unreferenced figure (remove the only \ref to it), acronym used before its definition,
        # duplicate and unused bib entries, an arXiv entry, a restatement that drifted
        ("main.tex", ", and Figure~\\ref{fig:plot}\nshows the success rate as the noise level grows.",
         ".\nThe success rate decreases as the noise level grows."),
        ("main.tex", "Diffusion models generate diverse plans for robot navigation, but a sampled plan may still",
         "Diffusion models generate diverse plans for robot navigation and work well with RRT, but a sampled plan may still"),
        ("main.tex", "a plan only if it is certified safe.",
         "a plan only if it is certified safe. Unlike a rapidly-exploring random tree (RRT), GDP is learned."),
        ("main.tex", "Under Assumptions~\\ref{asm:lip} and~\\ref{asm:noise}, every plan accepted by the gate stays in\n$\\mathcal{X}$ with probability at least $1-\\delta$.\n\\end{theorem}\n\n\\end{document}",
         "Under Assumptions~\\ref{asm:lip} and~\\ref{asm:noise}, every plan accepted by the gate stays in\n$\\mathcal{X}$ with probability at least $1-2\\delta$.\n\\end{theorem}\n\n\\end{document}"),
        ("refs.bib", "@book{rawlings2017model,",
         "@inproceedings{ho2020ddpm,\n  title     = {Denoising diffusion probabilistic models},\n"
         "  author    = {Ho, Jonathan and Jain, Ajay and Abbeel, Pieter},\n  booktitle = {NeurIPS},\n"
         "  year      = {2020}\n}\n\n@article{chi2023diffusion,\n  title   = {Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n"
         "  author  = {Chi, Cheng and Feng, Siyuan and Du, Yilun},\n  journal = {arXiv preprint arXiv:2303.04137},\n"
         "  year    = {2023}\n}\n\n@misc{unused2021,\n  title  = {An Entry Nobody Cites},\n  author = {Nobody, N.},\n  year   = {2021}\n}\n\n"
         "@book{rawlings2017model,"),
        ("sec/method.tex", "from a diffusion model~\\cite{ho2020denoising}",
         "from a diffusion model~\\cite{ho2020denoising,ho2020ddpm} as in diffusion policy~\\cite{chi2023diffusion}"),
    ],
    "template_hacks": [
        ("main.tex", r"\usepackage{booktabs}",
         "\\usepackage{booktabs}\n\\linespread{0.95}\n\\setlength{\\textfloatsep}{4pt}"),
        ("main.tex", "\\section{Experiments}\\label{sec:exp}", "\\vspace{-6pt}\n\\section{Experiments}\\label{sec:exp}"),
        ("main.tex", "  \\begin{tabular}{lcc}", "  \\hspace*{-5in}\\begin{tabular}{lcc}"),
    ],
    "figures": [
        ("main.tex", "\\section{Limitations}\\label{sec:limits}",
         "\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=0.45\\linewidth]{fig/plot_tiny.pdf}\\hfill\n"
         "  \\includegraphics[width=0.45\\linewidth]{fig/plot_redgreen.png}\n  \\caption{}\\label{fig:extra}\n\\end{figure}\n"
         "Figure~\\ref{fig:extra} repeats the comparison.\n\n\\section{Limitations}\\label{sec:limits}"),
    ],
}

EXTRA_FILES = {
    "type3_font": {"fig/plot_type3.pdf": COMMON / "plot_type3.pdf"},
    "figures": {"fig/plot_tiny.pdf": COMMON / "plot_tiny.pdf", "fig/plot_redgreen.png": COMMON / "plot_redgreen.png"},
}

REBUTTALS = {
    "rebuttal_unfulfilled": (
        "# Response to reviewers\n\n"
        "**R1, runtime.** We will add a runtime comparison with the MPC baseline to Section 4.\n\n"
        "**R2, hardware.** We will add a discussion of hardware limitations to the Limitations section.\n\n"
        "**R3, typo.** Thank you, fixed.\n"
    ),
    "clean": (
        "# Response to reviewers\n\n"
        "**R2, hardware.** We will add a discussion of hardware limitations to the Limitations section.\n"
    ),
}


def build(name: str) -> None:
    dst = ROOT / name
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(BASE, dst)
    for rel, old, new in FIXTURES[name]:
        p = dst / rel
        text = p.read_text()
        n = text.count(old)
        if n != 1:
            raise SystemExit(f"{name}: {rel}: expected 1 occurrence of {old[:60]!r}, found {n}")
        p.write_text(text.replace(old, new))
    for rel, src in EXTRA_FILES.get(name, {}).items():
        (dst / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(src, dst / rel)
    if name in REBUTTALS:
        (ROOT / f"{name}.rebuttal.md").write_text(REBUTTALS[name])


if __name__ == "__main__":
    for n in FIXTURES:
        build(n)
    print("built:", ", ".join(FIXTURES))
