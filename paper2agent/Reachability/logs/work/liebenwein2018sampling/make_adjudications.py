#!/usr/bin/env python3
"""Write adjudications.json from the current review queue (liebenwein2018sampling).
Reasons are keyed by (page, check); the script refuses to run if the queue holds a diagnostic
without a written reason or if the reviewed payload (EXPECT) changed."""
import json
from pathlib import Path
R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/liebenwein2018sampling-paper"
D = W / "documents/s001-liebenwein2018sampling"
ML, ND, IP = "missing_lines", "number_differences", "independent_parser_number_differences"
WORDS = (" The prose words of every listed line were looked up, in order, in the built page text with a scripted word-sequence check; "
         "the only lines not matched word for word are explained by glyph-soup math tokens or line-end word fragments, each checked on the page render.")
ALG = ("Extra numbers only, nothing missing. All extras are the numbers of the three algorithm transcriptions; the PDF text of the algorithm boxes lies inside the image crops and is excluded by the tool, and each number was read on the 150 dpi crops: "
       "titles 'Algorithm 1/2/3'; printed line numbers 1-4 (Alg. 1), 1-12 (Alg. 2), 1-5 (Alg. 3); in Alg. 2 '(0, 1)', '(1 - eps)' in the Output line, 'Lemma 3', 'Theorem 7' and line 6 'd((1 - eps)^{-1/d} - 1)/(alpha K c)' (giving 1, -1, 1); in Alg. 3 '1/2' and 'eps/2'. "
       "Tallied against the payload: 1 x9, 2 x6, 3 x5, 4 x3, 5 x2, 7 x2, and one each of 0, 6, 8, 9, 10, 11, 12, -1.")
REASONS = {
 (1, ND): "Extra numbers only, nothing missing: '1' x4 and 0.2, 0.4, 0.6, 0.8 once each are the Figure 1 panel sub-captions '(a) (1 - eps) = 0.2 ... (d) (1 - eps) = 0.8', which are printed inside the figure crop (excluded from the source count) and were additionally transcribed as a caption item so that they are searchable; read on the 150 dpi crop of Figure 1.",
 (1, IP): "Same payload as the first parser: the extra '1' x4, 0.2, 0.4, 0.6, 0.8 are the Figure 1 sub-captions '(a) (1 - eps) = 0.2 ... (d) (1 - eps) = 0.8', printed inside the excluded figure crop and transcribed once more as text; read on the 150 dpi crop.",
 (2, ML): "All 24 lines contain inline mathematics now written in LaTeX: $\\varepsilon$ in contribution 3), 'Flow$^{\\star}$' (PDF text 'Flow⋆tool'), and the Section III lines with $\\dot{x} = h(x,u)$, $\\mathbb{R}^d$, $\\mathcal{U} \\subset \\mathbb{R}^m$, $\\mathbf{x}(x_0,t,u(\\cdot))$, $H(x_0,T)$, $\\mathcal{X}$, $\\mathcal{Y}$, $f : \\mathbb{R}^d \\to 2^{\\mathcal{Y}}$, $f(z) = \\emptyset\\ \\forall z \\notin \\mathcal{X}$, $F(\\mathcal{X}') = \\cup_{x \\in \\mathcal{X}'} f(x)$, $|\\mathcal{S}| = n \\in \\mathbb{N}_+$, $F(\\mathcal{S}) \\approx F(\\mathcal{X})$, $\\mu(\\cdot)$. Each formula was compared with the 200 dpi render of the page and with a pdflatex rendering of the transcription." + WORDS,
 (3, ML): "All 19 lines contain inline or displayed mathematics now written in LaTeX: Problem 1 ($\\varepsilon \\in (0,1)$, $\\mathcal{S} \\subset \\mathcal{X}$) and inequality (1); $F(\\mathcal{X})$, $f(x)$, $x \\in \\mathcal{X}$, $F(\\mathcal{S})$, $\\delta$-packing, $\\delta > 0$ in Sec. IV-A; $\\varepsilon$, $\\delta$, $\\mathcal{X}$, $\\mathcal{S}$ in Sec. IV-B/C and the first paragraph of Sec. V. Two of the lines are the halves of 'straight-/forward', written 'straightforward'. Compared with the 200 dpi render; lines inside the three algorithm crops are excluded by the tool and were checked against the crops." + WORDS,
 (3, ND): ALG,
 (3, IP): "Same payload as the first parser. " + ALG,
 (4, ML): "All 51 lines contain mathematics now written in LaTeX: $x \\in \\mathcal{S}$, $F(\\mathcal{S})$, $(1-\\varepsilon)$-approximation in the roadmap paragraph; $d_{\\mathrm{H}}(A,B)$ and its two displays (the fragments 'dH(A, B) = max', 'b∈B ∥a −b∥, sup', 'a∈A ∥a −b∥' are pieces of the first display); $A_\\delta$, $\\mathcal{B}_\\delta(a)$; Assumptions 1-3; the $m$-rectifiable definition; the covering/packing paragraph ($C = \\{c_1,\\ldots,c_N\\}$, $N(B,\\delta)$, $D = \\{d_1,\\ldots,d_M\\}$, $\\min_{i,j\\in[M]:i\\ne j}\\|d_i-d_j\\| > \\delta$, $M(B,\\delta)$); Theorem 1 with $C = \\pi^{d/2}/\\Gamma(d/2+1)$ and its bound; $\\Delta(\\mathcal{X})$; Lemma 2 with its bound and proof; the Minkowski content (2). Every display and statement was read on 330 dpi crops of both columns and compared with a pdflatex rendering. 'GREEDYPACK'/'GREEDY-PACK' lines are the small-caps name written GreedyPack; 'ings with parameter' is the second half of 'pack-/ings'." + WORDS,
 (4, ND): "Sign glyph and spacing only: the PDF has one '−1' (Unicode minus) in '(d −1)-rectifiable' of Assumption 3; the LaTeX is '$(d - 1)$', which the tool reads as '1'. Read on the 330 dpi crop; no other number differs (the second parser reports no difference on this page).",
 (5, ML): "All 67 lines contain mathematics now written in LaTeX: Lemma 3 (statement, constant $c = \\max\\{M/(d\\mu(\\mathcal{B}_1(\\cdot))^{1/d}),1\\} < \\infty$, inequality with exponents $(d-1)/d$); Lemma 4 and inequality (3); the proof of Lemma 4 ($g$, $h(\\delta)$, the liminf/limsup display, $\\lambda'$, $\\xi(\\varepsilon)$, $\\delta'$, display (4), the two derivative displays, the final limit display); Lemma 5 with (5) and its proof (two $d_{\\mathrm{H}}$ displays). Short fragments such as 'µ(Aδ)(d−1)/d ≤', '1 + c δλ(∂A)', 'h(δ) = lim', 'δ→0 h(δ).', '≤1 + cδ′λ′', 'dµ(A)1/d ·' are numerators, denominators and limits of those displays. Every display was read symbol by symbol on 330 dpi crops (one inline fraction at 900 dpi) and compared with a pdflatex rendering." + WORDS,
 (5, ND): "Sign glyph and spacing only. The PDF has eight '−1' (Unicode minus), all in 'd − 1': '(d−1)-rectifiable' in Lemma 3, Lemma 4, the proof of Lemma 4 and '(d −1)-rectifiability', and the exponent '(d−1)/d' four times (twice in the Lemma 3 inequality, once in each derivative display). In LaTeX the four text occurrences are '$(d - 1)$' (read as '1' x4) and the four exponents are '(d-1)/d' with ASCII minus (read as '-1' x4). Counted 8 on the 330 dpi crops and 8 in the text.",
 (5, IP): "Same eight 'd − 1' occurrences as for the first parser (four '(d - 1)' in the text, four exponents '(d-1)/d'); the second parser extracts two of the PDF occurrences with a space after the minus, so it reports six '−1' missing against two extra '1' and four extra ASCII '-1'. All eight read on the 330 dpi crops; no other number differs.",
 (6, ML): "All 63 lines contain mathematics now written in LaTeX: Lemma 6 with (6) and its proof; Theorem 7 (packing precision bound, $\\alpha = \\sup_{\\mathcal{X}'\\subseteq\\mathcal{X}} \\lambda(\\partial F(\\mathcal{X}'))/\\mu(F(\\mathcal{X}'))$, $c$, conclusion); Corollary 8; Corollary 9 ($|\\mathcal{S}| \\le (3\\alpha K\\Delta(\\mathcal{X})c/\\varepsilon)^d$); the complexity paragraph ($\\mathcal{C}_\\alpha$, $\\mathcal{C}_K$, $\\mathcal{C}_c$, $\\mathcal{C}_{\\mathcal{S}}$, $\\mathcal{C}_f$); Theorem 10; the sequence $(\\mathcal{F}_i)$ and Proposition 11; unicycle dynamics (7) (fragments 'uv cos θ', 'uv sin θ'); the RSL parametrisation (fragments 'θRSL', the three vector rows); $\\theta_i = u_v t_i/\\rho$, $t_1+t_2+t_3 \\le T$, $[v_{min}, v_{max}]$. Theorem 7, Corollaries 8-9 and Theorem 10 were read on 600 dpi crops, the rest on 330 dpi crops, and all compared with a pdflatex rendering. 'APPROXIMATEREACHABILITY' lines carry the small-caps name written ApproximateReachability; 'struct S' and 'stant from Lemma 3' are second halves of 'con-/struct' and 'con-/stant'." + WORDS,
 (6, ND): "Sign glyph and spacing only. The PDF has three '−1' (Unicode minus): the exponent in '(1 −ε)^{−1/d}' and the following '−1)' of the Theorem 7 bound, and the leading '−1' of the second row of the RSL vector. In LaTeX these are '^{-1/d}' (ASCII '-1'), '- 1)' (read as '1') and '-1 + 2\\cos' (ASCII '-1'). Read on the 600 dpi crop of Theorem 7 and the 330 dpi crop of the RSL display.",
 (6, IP): "Same three places as for the first parser (exponent '−1/d' and '− 1' in the Theorem 7 bound, leading '−1' of the second RSL row); the second parser extracts the middle one with a space, so it reports two '−1' missing against two extra ASCII '-1'. Read on the 600/330 dpi crops; no other number differs.",
 (7, ML): "The single line 'construction of a δ-covering by a grid construction. The' contains the inline symbol δ, written '$\\delta$-covering' in LaTeX; the sentence was compared with the 200 dpi render and is complete in the text.",
 (8, ML): "The single line 'generate the reachable set of the sampled subset (δ-packing)' contains the inline symbol δ, written '($\\delta$-packing)' in LaTeX; the sentence was compared with the 200 dpi render and is complete in the text.",
 (8, ND): "Hyphen only: the NSF award number is printed 'IIS-' at a line end followed by '1723943' on the next line; the text has 'IIS-1723943', which the tool reads as the signed token '-1723943'. Digits checked on the 200 dpi render.",
 (8, IP): "Same as the first parser: 'IIS-' / '1723943' across a line break in the PDF versus 'IIS-1723943' in the text (read as '-1723943'). Digits checked on the 200 dpi render.",
 (9, ML): "The single line is the first line of reference [5]; the PDF text layer has the name with detached accents ('Ivanˇci´c'), the text has 'Ivančić' as printed (read on the 260 dpi crop). The rest of the line ('[5] R. Alur, T. Dang, and F. ... Predicate Abstraction') is present.",
}
EXPECT_ML = {2: 24, 3: 19, 4: 51, 5: 67, 6: 63, 7: 1, 8: 1, 9: 1}
EXPECT_ND = {
 1: {"missing": {}, "extra": {"1": 4, "0.2": 1, "0.4": 1, "0.6": 1, "0.8": 1}},
 3: {"missing": {}, "extra": {"1": 9, "0": 1, "2": 6, "3": 5, "4": 3, "6": 1, "7": 2, "8": 1, "5": 2, "-1": 1, "9": 1, "10": 1, "11": 1, "12": 1}},
 4: {"missing": {"−1": 1}, "extra": {"1": 1}},
 5: {"missing": {"−1": 8}, "extra": {"1": 4, "-1": 4}},
 6: {"missing": {"−1": 3}, "extra": {"1": 1, "-1": 2}},
 8: {"missing": {"1723943": 1}, "extra": {"-1723943": 1}},
}
EXPECT_IP = dict(EXPECT_ND)
EXPECT_IP[4] = {"missing": {}, "extra": {}}
EXPECT_IP[5] = {"missing": {"−1": 6}, "extra": {"1": 2, "-1": 4}}
EXPECT_IP[6] = {"missing": {"−1": 2}, "extra": {"-1": 2}}
EMPTY = {"missing": {}, "extra": {}}
v = json.loads((D / "verification.json").read_text(encoding="utf-8"))
for p in v["pages"]:
    n = p["page"]
    assert len(p["missing_lines"]) == EXPECT_ML.get(n, 0), ("missing-line count changed", n, len(p["missing_lines"]))
    assert p["number_differences"] == EXPECT_ND.get(n, EMPTY), ("number differences changed", n, p["number_differences"])
    assert p["independent_parser_number_differences"] == EXPECT_IP.get(n, EMPTY), ("second-parser differences changed", n)
q = json.loads((W / "review-aid/review-queue.json").read_text(encoding="utf-8"))
entries = []
for s in q["sources"]:
    for it in s["items"]:
        if it.get("kind") != "unresolved_diagnostic":
            continue
        e = dict(it["adjudication_entry"])
        e["reason"] = REASONS[(e["page"], e["check"])]
        entries.append(e)
assert len(entries) == len(REASONS), (len(entries), len(REASONS))
(D / "adjudications.json").write_text(json.dumps({"schema_version": 1, "entries": entries}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("adjudications written:", len(entries))
