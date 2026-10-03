#!/usr/bin/env python3
"""Copy every unresolved diagnostic's adjudication_entry from the review queue and attach the reason
established by the page review (image crops), delatex_check.py, symbol_check.py, number_explain.py and
pypdf_peek.py.  Fails if the queue contains a diagnostic for which no reason was prepared."""
import json, os
R = os.path.expanduser("~/AI_agents/paper2agent/Reachability")
W = f"{R}/paper-review/devonport2020estimating-paper"
D = f"{W}/documents/s001-devonport2020estimating"
COMMON = (" Independent checks: converting the LaTeX back to the text-layer glyph order reproduces the alphanumeric "
          "content of every one of these lines, and the page's counts of <=, >=, subset, element-of, arrow, =, + and "
          "minus signs are identical in the text layer and in the markdown.")
REASON = {
    (3, "missing_lines"):
        "All 20 lines differ only in mathematical notation now written in LaTeX: Phi(t_1; t_0, x_0, u, d), x_0 in "
        "R^n, u:[t_0,t_1]->R^p, d:[t_0,t_1]->R^w, xdot(t)=f(...), phi(t_1), calligraphic X_0/U/D, R_{[t_0,t_1]} and "
        "its hatted version, theta, the ellipsoid set {x : ||Ax-b||_2 <= 1}, P_Z, epsilon, and display (1). Each line "
        "was read against the 260-dpi crops of PDF page 3; the surrounding prose matches word for word." + COMMON,
    (4, "missing_lines"):
        "The 12 lines are: one prose line with 'epsilon-accurate' twice; the two rows of display (2); the chance "
        "constraint of (3); the 'where J and g ... Theta in R^{n_theta} ... P_Z' line; the constraint row of (4); "
        "the two text-layer fragments of '{z^{(i)}}_{i=1}^N are N independently ...'; the Theorem 1 header line "
        "(delta in (0,1); label in bold, punctuation as printed); the 'log 1' fragment of (5); and the two lines of the "
        "clause after (5) ('e' written \\mathrm{e}, '>= 1 - delta'). All are LaTeX-versus-glyph differences; each "
        "was read against the 260-dpi crops of PDF page 4 and no prose word is missing." + COMMON,
    (4, "number_differences"):
        "Single place: the denominator 'e - 1' of equation (5). The text layer writes it with a Unicode minus "
        "('e −1', token '−1'); the LaTeX writes 'e-1' (token '-1'). Same quantity, confirmed on the 260-dpi crop. "
        "All other numbers on the page (equation tags (2)-(5), 2012, 12.1, subscripts 0 and 1) match.",
    (4, "independent_parser_number_differences"):
        "Same place as the first parser: pypdf renders the denominator of (5) as 'e− 1', i.e. an unsigned '1', "
        "where the LaTeX 'e-1' is tokenised as '-1' (checked by printing the pypdf text of the page). No other "
        "number differs.",
    (5, "missing_lines"):
        "The 19 lines are: display (6); the 'x, b in R^n, A in R^{n x n}, ... >= 1 or infinity' and 'p = 2 ... "
        "p = infinity' lines; two lines with hat R_{[t_0,t_1]}(A,b), -log det(A) and epsilon-accurate; the "
        "constraint row of (7) (printed '<= 1 - epsilon', kept); three prose lines with Phi, Z, X_0, U, D, epsilon; "
        "the four text-layer lines/fragments of the Theorem 2 statement incl. the ceiling formula for N ('log 1', "
        "'delta + n(n+1)/2 + n'); displays (9) and (10); and four lines of the proof (label in bold as printed, "
        "n x n, n_theta, n(n+1)/2 + n, 1 - delta). All are LaTeX-versus-glyph differences, read against the two "
        "260-dpi crops of PDF page 5; no prose word is missing." + COMMON,
    (5, "number_differences"):
        "Text layer has '−1' (Unicode minus) three times: in '||AZ −b||p −1 ≤0' of (7), in '||AZ −b||p −1 are "
        "convex' and in the 'e−1' denominator of the Theorem 2 sample size. In LaTeX the first two are "
        "'\\|AZ - b\\|_p - 1' (spaced, unsigned '1') and the third is 'e-1' ('-1'). Conversely 'n(n + 1)/2' "
        "(unsigned '1' in the text layer, twice: Theorem 2 and proof) is written 'n(n+1)/2' and tokenised '+1'. "
        "The counts balance exactly (attributed token by token with number_explain.py); every value was confirmed "
        "on the 260-dpi crops.",
    (5, "independent_parser_number_differences"):
        "pypdf prints 'p− 1≤ 0' and 'p− 1 are' (unsigned '1', same as the LaTeX), 'e−1' (Unicode '−1' versus "
        "LaTeX 'e-1' = '-1') and 'n(n + 1)/2' twice (unsigned '1' versus LaTeX 'n(n+1)/2' = '+1'); that is exactly "
        "the reported missing {'1': 2, '−1': 1} / extra {'-1': 1, '+1': 2}. Verified by printing the pypdf text; "
        "no value differs.",
    (6, "missing_lines"):
        "Six prose lines below the Algorithm 1 box that contain inline math now in LaTeX: the three text-layer "
        "fragments of 'is O(1/epsilon) and O(log 1/delta). For Algorithm 1, the sample', and the lines with "
        "n_theta, 'n_theta = n(n+1)/2 + n ... O(n^2)' and 'epsilon and delta'. Read against the 260-dpi crop of the "
        "lower half of PDF page 6; no prose word is missing." + COMMON,
    (6, "number_differences"):
        "Nothing is missing; all extras come from two known causes. (1) The LaTeX transcription of Algorithm 1 "
        "(item p0006-algorithm1-text) repeats text that the line/number check excludes because the box is also "
        "kept as an image crop; its tokens are 1 x11, 0 x7, -1, +1, 2, 8 and were checked one by one against the "
        "260-dpi crop of the box (Algorithm 1, X_0, t_0, t_1, <= 1, 1 - delta, 1/epsilon, e-1, log 1/delta, "
        "n(n+1)/2, {1,...,N}, - 1 <= 0, i = 1, tag (8)). (2) In the prose, 'n(n + 1)/2' occurs twice and is written "
        "'n(n+1)/2', tokenised '+1' instead of '1'. 11 - 2 = 9 extra '1', 1 + 2 = 3 extra '+1', as reported.",
    (6, "independent_parser_number_differences"):
        "Identical diagnostic to the first parser (same fingerprint): only extras, all from the Algorithm 1 "
        "transcription that duplicates the image-cropped box (1 x11, 0 x7, -1, +1, 2, 8, each checked against the "
        "260-dpi crop) and from 'n(n+1)/2' written without spaces twice in the prose ('+1' instead of '1').",
    (7, "missing_lines"):
        "Seven lines with math now in LaTeX: the 'log 1' fragment of display (11); 'n_theta = 2n'; 'R^n ... p-norm "
        "ball ... A'; 'p = infinity'; 'p = 2 ... epsilon = 0.05, delta = 10^{-9}'; and two lines containing "
        "'epsilon-accurate'. Read against the two 260-dpi crops of PDF page 7; all digits (0.05, 10^{-9}) and prose "
        "match." + COMMON,
    (7, "number_differences"):
        "Three notation-only differences, each confirmed on the 260-dpi crop: the 'e −1' denominator of (11) "
        "(Unicode '−1' versus LaTeX 'e-1' = '-1'); 'δ = 10−9' (superscript flattened, '−9') versus '10^{-9}' "
        "('-9'); and the sample count typeset in math mode as '46, 052' (tokens '46' and '052') versus '$46,052$' "
        "(one token '46,052'). All other numbers (2n, 2, 0.05, 0.95, 1510, 1036, 12, 3.5, 5%, .01, 0.9999, 3.6, "
        "2018) match exactly.",
    (7, "independent_parser_number_differences"):
        "Same three places as the first parser: pypdf prints 'e− 1' (unsigned '1' versus LaTeX '-1'), '10 −9' "
        "('−9' versus '-9') and '46, 052' ('46' and '052' versus '46,052'). Verified by printing the pypdf text; "
        "no value differs.",
}
# The live queue lists only UNRESOLVED diagnostics, so once adjudications exist it is empty.  Use the copy
# saved after the first staging build; its fingerprints were verified to equal the currently applied set.
queue = json.load(open(f"{R}/logs/work/devonport2020estimating/review-queue-s1.json"))
entries, used = [], set()
for item in queue["sources"][0]["items"]:
    if item["kind"] != "unresolved_diagnostic":
        continue
    e = dict(item["adjudication_entry"])
    key = (e["page"], e["check"])
    e["reason"] = REASON[key]            # KeyError = a diagnostic nobody looked at
    used.add(key)
    entries.append(e)
assert used == set(REASON), f"prepared reasons without a diagnostic: {set(REASON) - used}"
json.dump({"schema_version": 1, "entries": entries}, open(f"{D}/adjudications.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
print(len(entries), "adjudications written")
