#!/usr/bin/env python3
"""Set title/notes/reading_order in plan.json and title/review/navigation in bundle.json (idempotent)."""
import json
from pathlib import Path
R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/tebjou2023data-paper"
D = W / "documents/s001-tebjou2023data"
TITLE = "Data-driven Reachability using Christoffel Functions and Conformal Prediction"

plan = json.loads((D / "plan.json").read_text(encoding="utf-8"))
plan["title"] = TITLE
NOTES = [
    "Source version: the PMLR proceedings PDF. A. Tebjou, G. Frehse, F. Chamroukhi, 'Data-driven Reachability using Christoffel Functions and Conformal Prediction', Proceedings of Machine Learning Research vol. 204, Conformal and Probabilistic Prediction with Applications (COPA 2023), editors H. Papadopoulos, K. A. Nguyen, H. Boström and L. Carlsson. 20 pages, single column. The page banner prints 'Proceedings of Machine Learning Research 204:1–20, 2023' and the pages are numbered 1-20; the paper is cited with the volume pagination 194-213, which is not printed in the PDF. The banner, the running headers and the page numbers are omitted from the text.",
    "Mathematics was transcribed to LaTeX from the authors' TeX source of the arXiv version (arXiv:2309.08976v1, main.tex), with the jmlr class macros expanded to standard LaTeX, and every formula was checked against the PMLR PDF on 170 dpi page renders and 230-260 dpi crops. The arXiv TeX is not the source of the PMLR PDF; where they differ the PDF is followed. Differences found: (i) the PDF prints the transition function as a displayed formula, f : R^n -> R^n, at the start of Section 2; the arXiv TeX has no formula for f at that place (it reads 'by a transition function which maps a state ...'); (ii) the PDF prints theorem-like headers in bold without a colon and theorem/example bodies in italics, whereas the preamble of the arXiv TeX asks for small-caps headers with a colon and upright bodies; (iii) floats are placed differently. No other difference in the wording or in any formula was found. No formula is kept as an image.",
    "Printed equation numbers are (1) to (14) and are given with `\\tag{n}`; all other displays are unnumbered in the paper. Bold italic symbols (vectors x, y, alpha, and v_d in Section 2.1 and in the moment-matrix integral) are written with `\\boldsymbol`, upright bold symbols (M, and v_d from equation (1) on) with `\\mathbf`, as printed. Slanted fractions are written with a slash: the interval (0, 1/2) in Theorem 4 and the exponent 1/N in the output line of Algorithm 1. Percentages are written outside math mode. 'N = 10 000' in Example 1 is printed with a thin space and written 10000.",
    "The PDF underlines emphasised terms (the authors load the ulem package); they are written in italics, as are the venue titles in the references. Theorem-like blocks: the label is given in bold exactly as printed (no punctuation after it); the italic type of the bodies is not reproduced. Where each block ends: Conjecture 1 ends with the sentence 'If N >= ... then P(mu(S-hat) >= 1 - epsilon) >= 1 - delta.'; Example 1 ends directly before the heading of Section 3; Theorem 2 ends with display (8); Theorem 3 with display (9); Theorem 4 with display (12); Example 2 ends with '... is greater than 99%.' directly before the heading of Section 3.2; Example 3 ends directly before the heading of Section 4; Theorem 5 ends with display (14) (the sentence 'This bound is tight ...' is outside the theorem); Example 4 ends with '... 98.9% confidence.'. Each of the three proofs ends with a filled square.",
    "Reading order differs from the page order of the PDF in the following places, so that floats do not interrupt sentences: Figure 1 (printed at the top of PDF page 7, inside Section 3) follows Example 1 in Section 2.3; Algorithm 1 (PDF page 10) follows the proof of Theorem 4 and precedes Example 2, as in the TeX source; the text of Example 2 (PDF pages 9 and 11) is joined and Figures 2 and 3 (PDF pages 10 and 11) follow it; Figure 4 follows Example 3; Table 1 follows the paragraph that introduces it and Figure 5 follows Example 4; Algorithm 2 (printed at the top of PDF page 15, after the heading of Section 5) is at the end of Section 4; Table 2 and Figure 6 (PDF page 16) follow the third paragraph of Section 5.1; Figures 7 and 8 (PDF page 17) are at the end of Section 5.1; Figure 9 (PDF page 18) is at the end of Section 5.2. Footnote 1 (printed at the foot of PDF page 4) is placed directly after equation (1). The copyright line from the foot of the first page is placed after the editor line.",
    "Algorithms 1 and 2 are given as image crops (assets/figure/algorithm-1.jpg, algorithm-2.jpg) followed by text transcriptions, one paragraph per step. Figures 1-9 are image crops; the sub-captions printed under the panels ('(a) d = 3, epsilon = 0.085', ...) are inside the crops and are repeated as the first line of each caption. Tables 1 and 2 are CSV files with a Markdown copy in the text. Table 1: the printed header 'confidence in %' spans the four epsilon columns and is repeated as a prefix in each of these column names. Table 2: the columns |D|, |D_train|, |D_cal| (printed with a calligraphic D) are filled only in the first row of each block and in the last row; the cells below are printed empty or with vertical dots and are transcribed as printed, not forward-filled; they mean the values of the first row of the block (10000 / 8000 / 2000 for the first seven rows, 1000 / 800 / 200 for the next seven).",
    "The text and formulas are kept as printed. The following are in the source and are not conversion errors: 'Table 4' in the paragraph after the proof of Theorem 5 refers to the table printed as Table 1; 'Figure 9 illustrates how ...' in Section 5.1 describes what Figures 7 and 8 show (Figure 9 is the Duffing figure); 'For fixed d and n -> infinity' (twice) in Section 2.3, where the sample size N is evidently meant; 'in these sense of'; the thresholds 'b_1, ..., b_n' and the event 'U_(N) <= b_n' in and before Theorem 2 next to b_N; the region with subscript D instead of D_cal in the conditional probability before Theorem 2 and in step 2(c) of Algorithm 2; 'U_N' without parentheses in the proofs of Theorems 3 and 4; the product written with a capital Pi; 'Combing (10) and (11)'; 'The reduces the cost'; the subscripts 'inlier', 'oulier', 'outlier', 'inliers' and the variables 'V_i, ..., V_{N-p}' in the proof of Theorem 5; 'otherwise. .' in Algorithm 2; 'provides ... and proposed' and 'compared that the most relevant approaches' in the Conclusion; plain italic S and S-hat (instead of calligraphic) in Example 1 and in the note under Table 2; epsilon printed in two shapes (`\\epsilon` in the text, `\\varepsilon` in figure sub-captions, in the captions of Figures 1 and 9 and once in Example 1).",
    "Reviewer's numerical checks (not part of the paper), made by recomputing printed numbers from the transcribed formulas. Algorithm 1 / Theorem 4 with delta = 0.01: 1 - delta^(1/N) is 0.0023 for N = 2000, 0.0228 for N = 200 and 0.0046 for N = 1000; the paper prints 0.002, 0.02 and 0.45% in the examples and 0.2, 2.2 and 0.5 (in %) in Table 2. Example 4: equation (14) as printed with N = 500, p = 50, epsilon = 0.15 gives 0.9897, matching the printed 98.9%. Table 1: equation (14) as printed (sum from i = p+1) with p = 0.05 N gives 18.1 / 33.9 / 50.9 / 92.2 for N = 100, 6.9 / 34.6 / 71.2 / 99.99 for N = 500, 2.3 / 32.1 / 81.2 / 100.0 for N = 1000 and 0.3 / 27.8 / 90.6 / 100.0 for N = 2000, which are not the printed entries; the printed entries coincide, after truncation, with the same sum started at i = p (33.1 / 51.8 / 68.1 / 96.7, 10.2 / 42.5 / 77.7 / 99.99, 3.2 / 37.5 / 84.8 / 100.0, 0.41 / 31.4 / 92.2 / 100.0). Figure 1: with N = 10000, delta = 0.01 and n = 2 the bound of Conjecture 1 requires about 10488, 10335, 9938 and 10489 samples for the printed pairs (d, epsilon) = (3, 0.085), (6, 0.23), (10, 0.51), (15, 0.9), consistent with epsilon rounded to two digits.",
]
for n in NOTES:
    assert "$" not in n, n[:60]
plan["notes"] = NOTES

# ---- reading order: page order with explicit moves ------------------------------------------
pages = {}
for entry in plan["pages"]:
    st = json.loads((D / entry["file"]).read_text(encoding="utf-8"))
    pages[st["page"]] = [it["id"] for it in st["items"] if it["kind"] != "omit"]
order = [i for p in sorted(pages) for i in pages[p]]
allids = set(order)


def move(ids, after):
    """Move the listed ids (kept in the given order) directly after item `after`."""
    global order
    for i in ids:
        assert i in allids, i
    assert after in allids and after not in ids
    order = [i for i in order if i not in ids]
    k = order.index(after) + 1
    order[k:k] = ids


# Figure 1 after Example 1 (end of Section 2.3)
move(["p0007-fig1", "p0007-b006"], after="p0006-b013")
# Algorithm 1 after the proof of Theorem 4, before Example 2
move(["p0010-alg1", "p0010-alg1-text"], after="p0009-b013")
# Example 2 text (pages 9 and 11) joined; Figures 2 and 3 after it
move(["p0011-b006", "p0010-fig2", "p0010-b015", "p0011-fig3", "p0011-b005"], after="p0009-b014")
# Algorithm 2 at the end of Section 4 (after Figure 5 and its caption)
move(["p0015-alg2", "p0015-alg2-text"], after="p0014-b004")
# Table 2 and Figure 6 after the third paragraph of Section 5.1
move(["p0016-b001", "p0016-tab2", "p0016-b003", "p0016-fig6", "p0016-b009"], after="p0015-b012")
# last two paragraphs of Section 5.1 joined across pages 15-18; Figures 7 and 8 after them
move(["p0016-b010", "p0017-b009", "p0017-b010", "p0018-b006",
      "p0017-fig7", "p0017-b004", "p0017-fig8", "p0017-b008"], after="p0015-b013")
# Figure 9 at the end of Section 5.2
move(["p0018-fig9", "p0018-b005"], after="p0018-b010")
assert len(order) == len(allids) == len(set(order))
plan["reading_order"] = order
(D / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# ---- bundle.json ------------------------------------------------------------------------------
b = json.loads((W / "bundle.json").read_text(encoding="utf-8"))
b["title"] = TITLE
src = b["sources"][0]
src["title"] = TITLE
src["reviewed"] = True
src["review_notes"] = (
    "All 20 pages of the PMLR v204 PDF were compared item by item with 170 dpi page renders and with 200-260 dpi "
    "crops of every mathematical region, algorithm box, table and figure, and with the authors' arXiv TeX source "
    "(arXiv:2309.08976v1) and .bbl, which were used as a transcription aid only. All inline and display mathematics "
    "was rewritten in LaTeX with the jmlr macros expanded; the extractor's 41 formula images were replaced by LaTeX "
    "displays (equation numbers (1)-(14) as \\tag) and no formula is kept as an image. Conjecture 1, Theorems 2-5, "
    "Examples 1-4 and the three proofs carry their printed labels in bold. Algorithms 1 and 2 are image crops plus "
    "transcriptions; Figures 1-9 are single crops per figure (panels, tick labels and sub-captions inside, edges "
    "checked on wider crops) with verbatim captions; Tables 1 and 2 are cell tables checked cell by cell. Floats that "
    "interrupt sentences in the PDF (pages 9-11 and 15-18) were moved with reading_order and the split sentences joined. "
    "The 19 references were each read against the page image; split diacritics and volume/page strings broken across "
    "lines were repaired. Omitted regions: the proceedings banner on page 1, 19 running headers and 19 page numbers. "
    "One difference between the arXiv TeX and the PMLR PDF affects the text (a displayed formula on page 3); the PDF "
    "was followed. Authors' slips are kept and listed in the page notes and conversion notes. Printed numbers were "
    "recomputed from the transcribed bounds as an end-to-end check. Review was done by one agent; no independent "
    "second verifier was used."
)
P = "references/paper.md"
b["navigation"] = [
    {"file": P, "heading": "Abstract", "purpose": "One-paragraph statement of the method and its claims; keywords"},
    {"file": P, "heading": "1. Introduction", "purpose": "Motivation, related work on data-driven reach sets and SOS/Christoffel approaches, list of contributions, structure of the paper"},
    {"file": P, "heading": "2. Data-driven Reach Set Approximation with Christoffel Functions", "purpose": "Problem setting: transition function f, initial set, reachable set S as the support of a measure"},
    {"file": P, "heading": "2.1. Preliminaries", "purpose": "Notation: monomials, polynomial space, number of monomials s(d), monomial vector v_d(x)"},
    {"file": P, "heading": "2.2. Christoffel Functions", "purpose": "Moment matrix, Christoffel function (1), variational form, empirical measure, empirical moment matrix (2), empirical Christoffel polynomial (3), invertibility condition; footnote 1"},
    {"file": P, "heading": "2.3. Set Approximation with Christoffel Functions", "purpose": "Sublevel-set estimate (4)-(6), the PAC bound of Devonport et al. restated as Conjecture 1 and the authors' objection to it, convergence remarks, Example 1 (four squares) and Figure 1"},
    {"file": P, "heading": "3. Reach Set Approximation with Conformal Prediction", "purpose": "Nonconformity function, p-value, conformal region, marginal coverage statement (7) and why a guarantee conditional on the data set is needed"},
    {"file": P, "heading": "3.1. Statistical Guarantees", "purpose": "Split into training and calibration sets; Theorem 2 (from Bates et al.), Theorem 3 with proof, Theorem 4 (coverage bounds (10)-(12)) with proof, Algorithm 1 (image and transcription), Example 2, Figures 2 and 3"},
    {"file": P, "heading": "3.2. Avoiding the Calibration Set", "purpose": "Transductive variant: nonconformity function with the test point added, Sherman-Morrison update (13), computational cost, Example 3, Figure 4"},
    {"file": P, "heading": "4. Robustness to Outliers", "purpose": "Theorem 5 (bound (14) with at most p outliers in the calibration set) with proof, Table 1, Example 4, Figure 5, Algorithm 2 (image and transcription)"},
    {"file": P, "heading": "5. Experiments", "purpose": "One-sentence lead-in to the experimental section"},
    {"file": P, "heading": "5.1. Empirical False Positive Rate", "purpose": "Comparison with one-class SVM, Isolation Forest and LOF as nonconformity functions: Table 2, Figure 6; outliers in the training set: Figures 7 and 8"},
    {"file": P, "heading": "5.2. Duffing oscillator", "purpose": "Duffing dynamics, parameter values, initial set, Figure 9"},
    {"file": P, "heading": "6. Conclusion", "purpose": "Authors' summary, scope of the results, numerical issues left for future work"},
    {"file": P, "heading": "Acknowledgments", "purpose": "Funding programme"},
    {"file": P, "heading": "References", "purpose": "Bibliography, 19 unnumbered author-year entries in alphabetical order"},
    {"file": P, "heading": "Conversion notes", "purpose": "Source version, how the mathematics was transcribed, differences between the arXiv TeX and the PMLR PDF, where theorem-like blocks end, moved floats, table conventions, source slips kept as printed, reviewer's numerical checks (at the end of the file)"},
]
(W / "bundle.json").write_text(json.dumps(b, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("plan.json and bundle.json updated; reading_order items:", len(order))
