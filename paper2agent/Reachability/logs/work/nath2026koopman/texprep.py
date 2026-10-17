#!/usr/bin/env python3
"""Make full.tex: main.tex with every \\input inlined (symbols.tex excluded), comments stripped and the authors'
private macros of symbols.tex expanded into standard LaTeX. \\cite/\\ref are left for resolution against the page."""
import re, os
T = os.path.expanduser("~/AI_agents/paper2agent/Reachability/tex-source/nath2026koopman")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "full.tex")


def strip_comments(s):
    return "\n".join(re.sub(r"(?<!\\)%.*$", "", ln) for ln in s.split("\n"))


def inline(name):
    s = open(os.path.join(T, name + ".tex"), encoding="utf-8").read()
    s = strip_comments(s)
    return re.sub(r"\\input\{([^}]*)\}", lambda m: "" if m.group(1) == "symbols" else inline(m.group(1)), s)


MACROS = {
    "infKoop": r"\mathcal{K}", "ka": r"K_{A}", "kb": r"K_{B}", "enc": r"\phi", "dec": r"\psi",
    "tnfl": r"\Gamma", "B": r"\mathcal{B}", "zr": r"z^{ref}_t", "ur": r"u^{ref}_t", "uf": r"u^{ff}_t",
    "zref": r"z^{\text{ref}}", "uref": r"u^{\text{ref}}", "delfz": r"\delta z", "delfu": r"\delta u",
    "lqrmat": "G", "xrefdistr": r"\text{MP}", "ncscore": "R", "ctrlSpace": r"\mathcal{U}",
    "stateSpace": r"\mathcal{X}", "ctrlSpaceDim": r"\mathbb{R}^m", "stateSpaceDim": r"\mathbb{R}^n",
}


def expand(s):
    for k in sorted(MACROS, key=len, reverse=True):
        s = re.sub(r"\\" + k + r"(?![a-zA-Z])", lambda m, v=MACROS[k]: v, s)
    return s


if __name__ == "__main__":
    s = expand(inline("main"))
    s = re.sub(r"\n{3,}", "\n\n", s)
    open(OUT, "w", encoding="utf-8").write(s)
    print(OUT, len(s.split("\n")), "lines")
