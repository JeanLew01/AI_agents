#!/usr/bin/env python3
"""Set title/notes/reading_order in plan.json and title/review/navigation in bundle.json (idempotent)."""
import json
from pathlib import Path
R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/lin2024verification-paper"
D = W / "documents/s001-lin2024verification"
TITLE = "Verification of Neural Reachable Tubes via Scenario Optimization and Conformal Prediction"

plan = json.loads((D / "plan.json").read_text(encoding="utf-8"))
plan["title"] = TITLE
plan["notes"] = [
    "Source version: arXiv:2312.08604v2 [cs.RO], 10 Apr 2024 (16 pages, single column, PMLR/L4DC style: main text on pages 1-10, acknowledgments and references on pages 11-13, Appendices A and B on pages 14-16); authors Albert Lin and Somil Bansal. The paper was published at L4DC 2024 (Proceedings of Machine Learning Research vol. 242, pp. 719-731). This package was made from the arXiv v2 PDF, not from the proceedings PDF. The first page of the arXiv PDF prints the banner 'Proceedings of Machine Learning Research vol vvv:1–16, 2024' (with the template placeholder 'vvv') and the foot line '© 2024 A. Lin & S. Bansal.'; these, the arXiv stamp, the running headers and the page numbers are page furniture and are not part of the text below.",
    "Mathematics was transcribed to LaTeX from the authors' arXiv TeX source (root.tex, notation.tex, sections/*.tex), with the authors' private macros expanded to standard LaTeX, and every formula was checked against the PDF pages; the TeX source and the PDF agree and no formula is kept as an image only. Notational choices that do not change the printed symbols: the mathtools definition symbol (coloneqq, printed ':=') is written ':=', a superscript star is written with `^{\\ast}`, the authors' macro for the reachable tube prints the upright word BRT and is written as plain text in prose, and percentages and plain decimal numbers in prose and captions (99.974%, 0.56, ...) are plain text.",
    "Numbering. The 14 printed equation numbers (1)-(14) are written with `\\tag{n}`. Numbers (11) and (12) belong to the last line of a three-line and of a two-line display in Appendix B.1; these displays are written as consecutive display blocks with the tag on the last one. Theorem-like statements share one counter: Remark 1, Theorem 2, Theorem 3, Remark 4, Lemma 5, Remark 6, and Lemma 7 (in Appendix A). Their labels are printed in bold without punctuation and their bodies in italics (not reproduced). Statement ends, taken from the TeX environments: Theorem 2 ends with display (3), Theorem 3 with display (4), Lemma 5 with display (6), Lemma 7 with display (10); Remarks 1, 4 and 6 are one paragraph each. Proofs start with a bold 'Proof' and end with a filled square, written as a black square symbol.",
    "The main text says three times that the proofs are 'in the Appendix of the extended version of this article' with footnote mark 1 (the footnote, printed once, gives a URL). This arXiv version already contains that appendix (Appendix A: Lemma 7 and the proof of Theorem 2; Appendix B: proofs of Theorem 3, of the reduction of split conformal prediction to robust scenario optimization, and of Lemma 5). The sentences are kept verbatim; footnote 1 is placed after the Section 4 paragraph that first carries its mark.",
    "Figures 1-6 are image crops (assets/figure/figure-1.jpg to figure-6.jpg) with verbatim captions; Figure 1 consists of two stacked panels printed at the left of its caption and is one crop. Figure 5 is printed at the top of PDF page 10, inside a sentence of Section 6.3; here it follows the Section 6.2 paragraph that discusses it. The figures are raster images, so their labels are not searchable; values printed only inside figures: Figure 1(a) is titled with a fixed N of about 3.7M, marks 'Vol. = 0.56' (grey point) and 'Vol. = 0.81' (dashed line), and its right axis pairs log10(epsilon) with safety as -3.5 (99.968%), -4.0 (99.990%), -4.5 (99.997%), -5.0 (99.999%); Figure 2(b) labels its four points with N about 116K and k = 0, N about 368K and k = 36, N about 1.2M and k = 193, N about 3.7M and k = 731; Figure 3 is titled with N about 3.7M and k = 731 and annotated '1-epsilon = about 0.99979' and '1-beta = 0.9'; Figures 4(b), 5(b) and 6(b) mark 'Vol. = 0.782' and 'Vol. = 0.8', 'Vol. = 0.334' and 'Vol. = 0.366', and 'Vol. = 0.19' next to the dashed 99.990% safety line (in Figure 4(b) both markers and in Figure 5(b) the grey 0.334 marker lie on the line; the cyan 0.366 marker of Figure 5(b) is drawn slightly below it and the cyan 0.19 marker of Figure 6(b) clearly below it) (the figures write 'about' as a tilde, e.g. '~3.7M'; the text gives the exact N = 3684118 for the k = 731 run). The paper has no tables and no algorithm boxes.",
    "The text and formulas are kept as printed. The following are in the source and are not conversion errors: 'split conform prediction' (Section 5, after Lemma 5); 'HJI-VI' in Section 6.3 where Section 3.1 defines 'HJB-VI'; 'side length 20m' next to target-set bounds of 20.0 in Section 6.2; in Appendix B.2 the solution of the sample problem is written with subscript N,k although the calibration set there has size n, and the final binomial sum uses n while the Equation (9) it is identified with uses N. The bibliography is unnumbered (author-year citations, 31 entries). Reading hint: Theorem 2 and Lemma 5 state the guarantee for the true value function V (probability that V(x,0) is at most 0), whereas Theorem 3, Remark 4 and the appendix proofs work with the induced cost of the learned policy; the proofs link the two through the inequality that this cost is at most V.",
]
# Reading order: page order, except that Figure 5 and its caption (printed at the top of page 10)
# follow the Section 6.2 paragraph on page 9 (p0009-b007).
MOVED = ("p0010-b001", "p0010-b002")
order = []
for entry in plan["pages"]:
    st = json.loads((D / entry["file"]).read_text(encoding="utf-8"))
    assert st["reviewed"], entry
    for it in st["items"]:
        if it["kind"] == "omit" or it["id"] in MOVED:
            continue
        order.append(it["id"])
        if it["id"] == "p0009-b007":
            order += list(MOVED)
assert all(m in order for m in MOVED) and len(order) == len(set(order))
plan["reading_order"] = order
for n in plan["notes"]:
    assert "$" not in n and "~~" not in n
(D / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

b = json.loads((W / "bundle.json").read_text(encoding="utf-8"))
b["title"] = TITLE
src = b["sources"][0]
src["title"] = TITLE
src["reviewed"] = True
src["review_notes"] = (
    "All 16 PDF pages (arXiv:2312.08604v2) were compared item by item with 130 dpi page renders and 200-220 dpi crops of "
    "every mathematical region and every figure, and with the authors' TeX source and .bbl. All inline and display "
    "mathematics was rewritten in LaTeX from the TeX source with private macros expanded; the 14 extractor 'formula' "
    "image items were replaced by display blocks carrying the 14 printed equation numbers (1)-(14). Theorem 2, Theorem 3, "
    "Lemma 5, Lemma 7 and Remarks 1, 4, 6 carry their printed bold labels; the four proofs of the appendix start with a "
    "bold 'Proof' and end with a black square. Figures 1-6 are image crops whose edges were checked on wider renders "
    "(the two panels of Figure 1 were merged into one crop), each followed by its verbatim caption; Figure 5 was moved by "
    "reading_order from the top of page 10 to Section 6.2. Sentences and formulas split by page breaks (pages 1/2, 3/4, "
    "4/5, 6/7, 8/9, 9/10) were joined. The 31 unnumbered references were each compared with the page image; split "
    "diacritics and broken page ranges/URLs were repaired. Footnote 1 was placed after the paragraph that carries its "
    "mark. Omitted regions: proceedings banner, arXiv stamp and copyright line on page 1, running headers and page "
    "numbers. As an end-to-end check, the binomial-tail condition (2) as transcribed reproduces the paper's printed "
    "values (99.974% safety for k = 731, N = 3684118, beta = 1e-16; 99.999% for k = 0; 1-epsilon = 0.99979 for "
    "1-beta = 0.9). Authors' typos and inconsistencies are kept and listed in the page review notes and the conversion "
    "notes. Review was done by one agent; no independent second verifier was used."
)
P = "references/paper.md"
b["navigation"] = [
    {"file": P, "heading": "Abstract", "purpose": "Summary of the two verification methods, their equivalence and the outlier-adjusted approach; keywords"},
    {"file": P, "heading": "1. Introduction", "purpose": "Motivation, related work on reachability and neural reachable tubes, limits of the earlier iterative scenario method, list of contributions"},
    {"file": P, "heading": "2. Problem Setup", "purpose": "System, target set, definition of the BRT, the probabilistic goal for the safe set, and the 9D multi-vehicle running example with its parameter values"},
    {"file": P, "heading": "3. Background: Hamilton-Jacobi Reachability, DeepReach, and Safety Verification", "purpose": "Short introduction to the background section (overview of Sections 3.1 and 3.2)"},
    {"file": P, "heading": "3.1. Hamilton-Jacobi (HJ) Reachability", "purpose": "Target function, cost function, value function (1), HJB-VI, Hamiltonian and optimal safety controller"},
    {"file": P, "heading": "3.2. DeepReach and an Iterative Scenario-Based Probabilistic Safety Verification Method", "purpose": "Learned value function and induced policy, uniform value correction bound of the earlier iterative method, Remark 1"},
    {"file": P, "heading": "4. Robust Scenario-Based Probabilistic Safety Verification Method", "purpose": "Sampling procedure (what is sampled, definition of N and of the outlier count k), Theorem 2 with condition (2) and guarantee (3), interpretation of epsilon and beta, reach case, footnote 1"},
    {"file": P, "heading": "4.1. Comparison of Robust and Iterative Scenario-Based Probabilistic Safety Verification", "purpose": "Trade-off between outlier count and safety level at fixed N and across N; Figures 1 and 2"},
    {"file": P, "heading": "5. Conformal Probabilistic Safety Verification Method", "purpose": "Theorem 3 (Beta distribution (4) of the safe fraction), Figure 3, Remark 4 (coverage property), Lemma 5 with (5)-(6), Remark 6 (equivalence with the scenario method)"},
    {"file": P, "heading": "6. Outlier-Adjusted Probabilistic Safety Verification Approach", "purpose": "Retraining on cost labels with a weighted MSE loss, validation metric, settings used in all case studies (w, beta, target epsilon)"},
    {"file": P, "heading": "6.1. Multi-Vehicle Collision Avoidance", "purpose": "Case study on the running example; Figure 4"},
    {"file": P, "heading": "6.2. Rocket Landing", "purpose": "6D rocket dynamics, target set, results and discussion of the training-regime limitation; Figure 5"},
    {"file": P, "heading": "6.3. Rocket Landing with No-Go Zones", "purpose": "Reach-avoid case study; Figure 6"},
    {"file": P, "heading": "7. Discussion and Future Work", "purpose": "Summary and stated future directions"},
    {"file": P, "heading": "Acknowledgments", "purpose": "Funding"},
    {"file": P, "heading": "References", "purpose": "Bibliography, 31 unnumbered entries sorted by author (author-year citations)"},
    {"file": P, "heading": "Appendix A. Robust Scenario-Based Proofs", "purpose": "Lemma 7: 1-D chance-constrained problem (7), sample counterpart with discarded constraints (8), condition (9), guarantee (10), and its proof from the sampling-and-discarding theorem"},
    {"file": P, "heading": "A.1. Proof of Theorem 2", "purpose": "How the verification procedure is cast as the sample problem of Lemma 7 and how the bound on the induced cost transfers to the value function"},
    {"file": P, "heading": "Appendix B. Conformal Proofs", "purpose": "Start of the conformal-prediction proofs (Sections B.1-B.3)"},
    {"file": P, "heading": "B.1. Proof of Theorem 3", "purpose": "Choice of score, calibration size and error rate; quantile computation; marginal coverage (11) and Beta distribution (12)"},
    {"file": P, "heading": "B.2. Proof that Split Conformal Prediction Reduces to Robust Scenario Optimization", "purpose": "General split conformal prediction setup, calibration-conditional coverage (13), reduction to Lemma 7 giving (14), equivalence via the incomplete beta function"},
    {"file": P, "heading": "B.3. Proof of Lemma 5", "purpose": "Lemma 5 as a special case of Section B.2 and Lemma 7"},
    {"file": P, "heading": "Conversion notes", "purpose": "Source version, how the mathematics was transcribed, numbering conventions, values printed only inside figures, source slips kept as printed (at the end of the file)"},
]
(W / "bundle.json").write_text(json.dumps(b, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("plan.json and bundle.json updated;", len(order), "items in reading order")
