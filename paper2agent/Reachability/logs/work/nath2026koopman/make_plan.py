#!/usr/bin/env python3
"""Set title/notes/reading_order in plan.json and title/review/navigation in bundle.json (idempotent) for nath2026koopman."""
import json
from pathlib import Path
R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/nath2026koopman-paper"
D = W / "documents/s001-nath2026koopman"
TITLE = "Scalable Data-Driven Reachability Analysis and Control via Koopman Operators with Conformal Coverage Guarantees"

plan = json.loads((D / "plan.json").read_text(encoding="utf-8"))
plan["title"] = TITLE
plan["notes"] = [
    "Source version: arXiv:2601.01076v1 [eess.SY], 3 Jan 2026, by Devesh Nath, Haoran Yin and Glen Chou (Georgia Institute of Technology); 28 pages in the single-column PMLR / L4DC 2026 style (class l4dc2026.cls, built on jmlr); the PDF is byte-identical to the arXiv v1 download. Main text pages 1-12 (Sections 1-7), references pages 12-14 (40 entries, author-year style), appendix pages 15-27 (Section 8: 8.1 Proofs, 8.2 Algorithm, 8.3 Experiment Details and Additional Experiments with 8.3.1-8.3.9); page 28 carries only the running header and the page number and is otherwise blank. The key nath2026koopman of this package comes from the user's TRO 2027 bibliography (`~/overleaf_project/Jixian_TRO_2027/reference.bib`), not from the CoRL bibliography used for the other papers of this collection.",
    "Omitted as page furniture: the first-page banner 'Proceedings of Machine Learning Research vol vvv:1–28, 2026' (a placeholder of the class, not a real volume), the vertical arXiv stamp, the running headers ('NATH YIN CHOU' on even pages, 'SCALABLE KOOPMAN REACHABILITY WITH CONFORMAL COVERAGE GUARANTEES' on odd pages) and the page numbers. Kept: the author block with the printed marks (Nath *1, Yin *1, Chou 2; no footnote text explains the asterisk anywhere in the PDF), the affiliation line, the e-mail addresses (printed in small caps, written in lower case), the keywords line, and the copyright line '© 2026 D. Nath, H. Yin & G. Chou.' printed at the foot of page 1 (placed directly after the author block).",
    "Mathematics was transcribed to LaTeX from the authors' arXiv TeX source (`main.tex` with the inputs `abstract`, `introduction`, `related_work`, `preliminary`, `problem_statement`, `methodology`, `experiments`, `conclusion` and `appendix`; macros in `symbols.tex`; `main.bbl`) and checked against the PDF (170 dpi page renders, 220-280 dpi crops of displays, statements and tables). The authors' private macros were expanded: encoder/lifting function phi, decoder psi, Koopman matrices K_{A}, K_{B} (typed with braces), the TKFL graph Gamma, z^{ref} and u^{ref} with an upright 'ref', delta z, delta u, LQR gains G, nonconformity score R, calligraphic B, K, X, U. A script check found all 471 math snippets identical to the macro-expanded TeX after whitespace removal (the only differences are the author marks of the title block); layout-only commands (small, negative hspace, looseness) were dropped. No formula is kept as an image only; TeX source and PDF agree everywhere.",
    "Equation numbers are kept as printed with `\\tag{...}`: (1a)-(1b), (2)-(9), (10), (11), (12)-(14). The pairs (3)/(4) and (8)/(9) are printed side by side on one line and are kept together, one display block per number. The CKRS of Theorem 1 is defined in display (10) in Section 5.4 and in display (11) in the appendix restatement (8.1); because both share one TeX label, the text cites '(11)' in Section 5.4 ('using (11)'), in the Offline Calibration paragraph ('as defined in (11)') and in Section 6 ('computed via (11)'); all tags and citations are kept as printed. (12), (13), (14) are the unicycle, planar-quadcopter and 3D-quadcopter dynamics in 8.3.1; (14) is one 12-row vector. Unnumbered displays (the CP coverage statement in 5.4, the probability bound of the restated Theorem 1 and the proof inequalities) carry no tag.",
    "Theorem-like statements keep the printed labels in bold without trailing punctuation: Proposition 1 (CG Robustness (Xu et al., 2020)) in Section 3, Problem 1 (Model learning & controller design) and Problem 2 ((1 − δ)-confident RSOA computation) in Section 4, Lemma 1 (KRS overapproximation) in 5.3 and Theorem 1 (CKRS Coverage Guarantee) in 5.4. Lemma 1 and Theorem 1 are printed twice, in Section 5 and again in Appendix 8.1 where each is followed by its proof; both copies are kept with the same numbers. Statement bodies are printed in italics (not reproduced); where a statement ends was taken from the TeX environments. Theorem 1 consists of the lead-in item, the CKRS display and the item 'where diag(...) ...' that ends with the probability bound (in 8.1 the bound is a separate unnumbered display). 'Proof' labels are bold as printed and the filled end-of-proof square is written ∎.",
    "Figures 1-12 are numbered continuously across main text and appendix and are all image crops in assets/figure (figure-1 ... figure-12); Figures 5-12 belong to the appendix (Section 8.3). Figure 2 is a vector block diagram with native text; Figures 3-12 are plots whose labels and legends are inside the crops. The caption of Figure 1 refers to panels '(a)' (the swimmer, top) and '(b)' (the hopper, bottom), but no panel letters are printed in that figure; Figures 8 and 9 carry printed panel letters (a)-(d) inside the image. In Figures 8 and 9 the PDF text layer encodes minus signs of tick labels as a degree sign; that text is figure-internal. Algorithm 1 (page 17) is an image crop (assets/figure/algorithm-1) followed by a line-by-line transcription with the printed line numbers 1-10; its comments are printed in blue and start with '//', kept as '//'.",
    "Tables: Table 1 (page 10, caption printed above the table) has 11 columns whose headers are printed on two or three lines; the lines of each header are joined with spaces into one header cell ('System dimension', 'Confidence Level (1 − δ)', 'Total time (online)', 'Avg. Log volume (online)', 'Avg. Log volume (offline)', 'Calibration dataset size', ...); cells as printed with units 's' and '%' and the Unicode minus. Table 2 (page 18, caption printed below) gives the RMSE of the polynomial lifting and of the neural lifting for the 11 hopper states with all printed digits.",
    "Placement of floats: items were reordered within their page on pages 7 (Figure 2 after the last paragraph of Section 5.3), 10 (Figure 3 after the 'Pure CP based verification.' paragraph; Table 1 after the 'Pure NNV Reachability.' paragraph) and 21. plan.json reading_order moves the appendix figures from the float pages to the subsections that discuss them: Figure 7 (printed on page 21) to the end of 8.3.5, Figure 8 (page 23) to the end of 8.3.6, Figures 9 and 10 (pages 24-25) to the end of 8.3.7, Figure 11 (page 26) to the end of 8.3.8 and Figure 12 (page 27) to the end of 8.3.9. Algorithm 1, printed at the top of page 17 below the heading of 8.3, is moved back to the end of 8.2 (where the TeX declares it and which describes it).",
    "Typography not reproduced: the run-in titles in Section 6 'Unsafe behavior from learned reachability estimators.', 'Pure CP based verification.', 'Hybrid Reachability methods (CP+NNV).' and 'Pure NNV Reachability.' are printed underlined and italic (written in italics); the letters 'Sca', 'Re', 'K', 'r', 'o' of 'Scalable Reachability via Koopman Operators' are underlined to spell ScaRe-Kro (written plain); venue names in the bibliography are underlined (written plain). The bold run-in paragraph titles (Koopman Operators, Reachability via NN Verification (NNV), Conformal Prediction (CP), Offline Calibration, Baselines, Unicycle, Planar Quadcopter, 3D Quadcopter, MuJoCo: Hopper, MuJoCo: Customized Swimmer, Reachability via Linear Relaxation, Koopman Reachability, Data-Driven Reachability) stay inside their paragraphs. The appendix headings 8.3.1-8.3.9 are printed in small caps and are written in the sentence case of the TeX source with the printed numbering and final period (8.3.2 has none).",
    "Text and formulas are kept as printed. The following are in the source and are not conversion errors: 'We are a planner P' (Section 4); the lifting function is called 'g' once in Section 3 ('with the lifting function g parameterized using polynomials or NNs') and phi everywhere else; the exact reachable set in Section 3 is printed with an extra closing brace; the dataset in Problem 1 lacks a closing parenthesis; 'state space.The latent consistency term' without a space (5.1); 'as a CG the describes' and 'memory costs that increases' (5.3); the latent trajectory is printed 'z_{0:T} = {z_0, z_2, ..., z_T}' (5.3); Lemma 1 concludes 'x-hat_t in X-hat_t' without the overline of the KRS symbol; in (9) the parenthesis opened by 'f(' is not closed; the index set of e^max_{t,j} is printed 'i in {K^cal + 1, ..., K^cal + M}' with M instead of M^lambda (5.4); Offline Calibration says 'x_t^(i) and x-hat_t^(i) are as defined in (8) and (9), respectively', although (8) defines x-hat and (9) defines x; 'via (7))' with an extra parenthesis; the caption of Table 1 spells the method 'SCaRe-Kro' (elsewhere 'ScaRe-Kro'); the conclusion mentions 'a 13-link MuJoCo swimmer' (the experiments describe a 28-dimensional swimmer); 8.2 writes the nominal KRS without hat and the CKRS without overline; row 8 of (14) contains 'cos phi · sin phi'; 'the the analytical dynamics' (8.3); 'Figure 6 illustrate' (8.3.4); 'remain with with probability' (8.3.5); the caption of Figure 9 says 'for a different reference trajectory' while four references are shown.",
    "Values that exist only inside figures: Figure 3 plots the Beta-posterior empirical coverage (y-axis 0.90-1.00) against the calibration size K^cal (3D quadrotor: 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000; Hopper: 50, 100, 200, 500, 1000) with a red '95% Target' line; the CKRS (ours) mode is at 1.00 for every K^cal, the SNSA mode starts near 0.98 at K^cal = 50 and approaches 0.95; colour bar 'Std. Devs. from Mean' 1 to 3+. The legends of Figures 5 and 7 read 'CKRS (99.0%)'. Figures 4, 6, 9, 11 and 12 plot per-state reachable sets over time (3D quadcopter: 12 states, x-axis 'Time Step (t)' up to about 200; hopper: 11 states over about 4.5 s; swimmer: 28 states, x-axis 'Timestep'); curve values were not digitised.",
]
for n in plan["notes"]:
    assert "$" not in n, n[:60]

# reading order: page order, with the appendix figures moved to their subsections
order = []
pages = {}
for pg in plan["pages"]:
    p = json.loads((D / pg["file"]).read_text(encoding="utf-8"))
    pages[p["page"]] = [i["id"] for i in p["items"] if i["kind"] != "omit"]
MOVE = {  # anchor id -> ids inserted after it
    "p0016-b009": ["p0017-alg1", "p0017-alg1-text"],
    "p0020-b005": ["p0021-b001", "p0021-b002"],
    "p0021-b003": ["p0023-b001", "p0023-b002"],
    "p0021-b005": ["p0024-b001", "p0024-b002", "p0025-b001", "p0025-b002"],
    "p0021-b007": ["p0026-b001", "p0026-b002"],
    "p0022-b002": ["p0027-b001", "p0027-b002"],
}
moved = {i for v in MOVE.values() for i in v}
for n in sorted(pages):
    for i in pages[n]:
        if i in moved:
            continue
        order.append(i)
        order.extend(MOVE.get(i, []))
allids = [i for n in sorted(pages) for i in pages[n]]
assert sorted(order) == sorted(allids) and len(order) == len(set(order)), "reading order incomplete"
plan["reading_order"] = order
(D / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("plan written:", len(plan["notes"]), "notes,", len(order), "items in reading order")

b = json.loads((W / "bundle.json").read_text(encoding="utf-8"))
b["title"] = TITLE
src = b["sources"][0]
src["title"] = TITLE
src["reviewed"] = True
src["review_notes"] = (
    "All 28 pages of arXiv:2601.01076v1 (L4DC 2026 / PMLR style) compared with 170 dpi renders and higher-resolution crops "
    "of every display, statement, table, figure and the algorithm, and with the authors' TeX source. Corrected: glyph-soup "
    "mathematics with <sup> and strikethrough markers rewritten in LaTeX from the macro-expanded TeX (471 snippets identical "
    "to the source), 17 extractor formula images replaced by LaTeX displays (22 display blocks in all), merged items split (Problems 1-2, "
    "contribution list, Section 6 run-in paragraphs, displays with swallowed prose), heading levels and small-caps "
    "appendix headings fixed, Figure 2 (classified as a table with leaked latexit strings) and Algorithm 1 (four fragments) "
    "rebuilt as crops, Table 1 cells rewritten, real compounds broken at line ends restored, bibliography (40 entries) "
    "cleaned of <u> tags with two compounds and one diacritic repaired. Furniture omitted: banner, arXiv stamp, running "
    "headers, page numbers. Appendix figures moved to their subsections with reading_order. Source slips are kept and "
    "listed in the conversion notes."
)
P = "references/paper.md"
b["navigation"] = [
    {"file": P, "heading": "Abstract", "purpose": "Abstract and keywords; the author block, affiliation line and copyright line are just above it, Figure 1 just below"},
    {"file": P, "heading": "1. Introduction", "purpose": "Motivation (limits of nonlinear, data-driven and Koopman reachability), the name ScaRe-Kro, and the four contributions"},
    {"file": P, "heading": "2. Related Work", "purpose": "Run-in paragraphs on reachability via linear relaxation (NNV, CROWN), Koopman/Carleman reachability, and data-driven reachability"},
    {"file": P, "heading": "3. Preliminaries", "purpose": "System model (1a)/(1b), interval, ball and sequence notation; Koopman operators and the autoencoder lifting; NNV with Proposition 1 (CG Robustness); exact reachable set and RSOA; split conformal prediction"},
    {"file": P, "heading": "4. Problem Statement", "purpose": "Planner, initial-state perturbation, the high-probability RSOA target; Problem 1 (model learning and controller design) and Problem 2 ((1 - delta)-confident RSOA)"},
    {"file": P, "heading": "5. Methodology", "purpose": "One-paragraph roadmap of Sections 5.1-5.4 (Fig. 2, Alg. 1)"},
    {"file": P, "heading": "5.1. Koopman Operator Training", "purpose": "Composite training loss (reconstruction, latent consistency, multi-step prediction), initialisation and activations"},
    {"file": P, "heading": "5.2. Koopman Tracking LQR Design", "purpose": "Feedforward control (2), lifted error dynamics, finite-horizon LQR and the tracking laws (3)-(4)"},
    {"file": P, "heading": "5.3. Reachability Analysis for Closed-Loop Koopman Dynamics", "purpose": "TKFL computational graph, decoded closed-loop rollout (5)-(6), construction of the CG, the KRS optimisation (7), Lemma 1; Figure 2 (block diagram) at the end"},
    {"file": P, "heading": "5.4. Conformalizing Koopman Reachable Sets", "purpose": "Calibration data and rollouts (8)-(9), normalised SNSA score, quantile and error bounds, CP coverage display, Theorem 1 with the CKRS (10), Offline Calibration paragraph and runtime use"},
    {"file": P, "heading": "6. Experiments", "purpose": "Metrics, Baselines, the four baseline comparisons (learned reachability, pure CP with Figure 3, hybrid CP+NNV, pure NNV), Table 1, and per-system paragraphs (unicycle, planar and 3D quadcopter with Figure 4, MuJoCo hopper and swimmer)"},
    {"file": P, "heading": "7. Conclusion", "purpose": "Summary and two directions of future work"},
    {"file": P, "heading": "References", "purpose": "Bibliography, 40 entries in author-year style"},
    {"file": P, "heading": "8. Appendix", "purpose": "Appendix roadmap (proofs, algorithm, experiment details)"},
    {"file": P, "heading": "8.1. Proofs", "purpose": "Lemma 1 restated with its proof, Theorem 1 restated (CKRS display numbered (11)) with its three-step proof"},
    {"file": P, "heading": "8.2. Algorithm", "purpose": "Prose description of the CKRS procedure followed by Algorithm 1 (image and line-by-line transcription)"},
    {"file": P, "heading": "8.3. Experiment Details and Additional Experiments", "purpose": "Roadmap of 8.3.1-8.3.9"},
    {"file": P, "heading": "8.3.1. Dynamics.", "purpose": "Unicycle (12), planar quadcopter (13) and 3D quadcopter (14) dynamics with parameters and time steps"},
    {"file": P, "heading": "8.3.2. Comparison between neural Koopman liftings and polynomial liftings", "purpose": "Polynomial (PyKoopman, degree-3) vs neural lifting on the hopper; Table 2 (RMSE per state)"},
    {"file": P, "heading": "8.3.3. Baseline comparison with Bansal and Tomlin (2021).", "purpose": "DeepReach comparison on the unicycle; Figure 5"},
    {"file": P, "heading": "8.3.4. Baseline comparison with Hashemi et al. (2024).", "purpose": "CP-NNV comparison on the 3D quadcopter; Figure 6"},
    {"file": P, "heading": "8.3.5. Additional results on unicycle system.", "purpose": "Unicycle CKRS; Figure 7"},
    {"file": P, "heading": "8.3.6. Additional results on planar quadcopter system.", "purpose": "Planar quadcopter, offline CP bounds over four references; Figure 8 (panels a-d)"},
    {"file": P, "heading": "8.3.7. Additional results on 3D quadrotor system.", "purpose": "3D quadrotor with alternative references and the obstacle view; Figures 9 (panels a-d) and 10"},
    {"file": P, "heading": "8.3.8. Additional results on MuJoCo hopper system.", "purpose": "Full 11-state hopper results; Figure 11"},
    {"file": P, "heading": "8.3.9. Additional results on MuJoCo swimmer system.", "purpose": "Full 28-state swimmer results; Figure 12"},
    {"file": P, "heading": "Conversion notes", "purpose": "Source version, conversion method, equation-number and float-placement remarks, source slips kept as printed"},
]
(W / "bundle.json").write_text(json.dumps(b, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("bundle written:", len(b["navigation"]), "navigation rows")
