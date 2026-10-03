import json, os
W = os.path.expanduser("~/AI_agents/paper2agent/Reachability/paper-review/liebenwein2018sampling-paper")
D = W + "/documents/s001-liebenwein2018sampling"
TITLE = "Sampling-Based Approximation Algorithms for Reachability Analysis with Provable Guarantees"

plan = json.load(open(D + "/plan.json"))
plan["title"] = TITLE
plan["notes"] = [
 "Source version: Liebenwein, Baykal, Gilitschenski, Karaman, Rus, \"Sampling-Based Approximation Algorithms for Reachability Analysis with Provable Guarantees\", Robotics: Science and Systems (RSS) 2018 proceedings PDF, 10 pages, two-column.",
 "The authors' TeX source was not available. All mathematics (inline and displayed) was transcribed visually to LaTeX from 200-900 dpi renders of the PDF pages and checked symbol by symbol against those renders; no displayed formula had to be kept as an image. Printed equation numbers (1)-(7) are given as \\tag.",
 "Theorem-like statements keep the printed numbering and are labelled in bold (Problem 1, Assumptions 1-3, Theorem 1, Lemmas 2-6, Theorem 7, Corollaries 8-9, Theorem 10, Proposition 11); their italic typography was dropped. Small-caps algorithm names are written in CamelCase (GreedyPack, ApproximateReachability, AnytimeApproximateReachability).",
 "Where each theorem-like statement ends (the statements are printed in italics, the surrounding text upright): Problem 1 ends with inequality (1); Assumptions 1, 2 and 3 are one sentence each; Theorem 1 ends with '... is the Euler gamma function [15].'; Lemma 2 ends with '... are defined as in Theorem 1.'; Lemma 3 and Lemma 4 each end with '... is the Minkowski Content as defined in (2).'; Lemma 5 and Lemma 6 each end with '... is the Lipschitz constant from Assumption 2.'; Theorem 7 ends with the restated inequality '... <= mu(F(X)).'; Corollary 8, Corollary 9, Theorem 10 and Proposition 11 are one paragraph each. Proofs start with 'Proof:' and end at the end-of-proof box (written as a black square).",
 "Algorithms 1-3 are given both as image crops and as transcriptions with one paragraph per printed line, the printed line numbers, and '&emsp;&emsp;' marking one nesting level. Figures 1-4 are image crops; their plot contents (curves, tick values) are not transcribed. The paper has no tables.",
 "This proceedings version prints proofs only for Lemmas 2, 4, 5 and 6; it states that some proofs are omitted, and no proof is printed for Lemma 3, Theorem 7, Corollaries 8-9, Theorem 10 or Proposition 11. There is no appendix.",
 "Authors' wording and apparent misprints are transcribed as printed, not corrected. Notable cases: Corollary 8 and Theorem 10 state the bound with mu(F(S)) on the right-hand side whereas Theorem 7 and the Output line of Algorithm 2 use mu(F(X)); Algorithm 1 line 2 prints the loop condition with '>= delta' whereas the proof of Lemma 2 negates a statement with '> delta'; Section III prints 'f(x) subseteq 2^Y'; Assumption 2 prints d_H with an italic H (upright H elsewhere); the definition of m-rectifiable prints 'onto Y'; the proof of Lemma 6 prints an equality where (6) has an inclusion.",
 "Floats are placed next to the text that discusses them, never inside a sentence: Algorithm 1 after Section IV-A, Algorithm 2 after Section IV-B, Algorithm 3 after Section IV-C (it is printed below the first paragraphs of Section V), and Figures 2 and 3 (printed at the top of page 7, above the heading of Section VI-B) inside Section VI-B. The sub-captions (a)-(d) of Figure 1 are printed inside the figure and are repeated as text above its caption.",
 "In the reference list the number(s) printed after each entry are the paper's back-references to the page(s) on which the entry is cited.",
]
json.dump(plan, open(D + "/plan.json", "w"), ensure_ascii=False, indent=2)

b = json.load(open(W + "/bundle.json"))
b["title"] = TITLE
src = b["sources"][0]
src["title"] = TITLE
src["reviewed"] = True
src["review_notes"] = ("All 10 pages of the RSS 2018 proceedings PDF were reviewed against 200 dpi page renders, with 260-900 dpi crops for every page that carries mathematics or references (pages 4, 5, 6, 9, 10) and for all figure/algorithm crops. "
 "No TeX source exists for this paper: all inline and displayed mathematics was transcribed visually to LaTeX; the statements of Problem 1, Assumptions 1-3, Theorem 1, Lemmas 2-6, Theorem 7, Corollaries 8-9, Theorem 10 and Proposition 11 were read at 330-600 dpi. No formula is kept as an image. "
 "Two-column reading order, cross-column and cross-page paragraph continuations (pages 3-4 and reference [28] on pages 9-10), heading levels, line-wrap hyphens and the bibliography (36 entries) were repaired. Figures 1-4 and Algorithms 1-3 are image crops with verbatim captions; the algorithms are also transcribed line by line. No tables, no appendix, no page furniture to omit. "
 "Authors' misprints are kept as printed and listed in the page review notes and the conversion notes.")
b["navigation"] = [
 {"file": "references/paper.md", "heading": "Abstract", "purpose": "Abstract; author block and affiliation are just above it"},
 {"file": "references/paper.md", "heading": "I. Introduction", "purpose": "Motivation, under-approximation setting, list of contributions, Figure 1"},
 {"file": "references/paper.md", "heading": "II. Related Work", "purpose": "Prior reachability tools and verification work the paper positions itself against"},
 {"file": "references/paper.md", "heading": "III. Problem Definition", "purpose": "Dynamics, control set, reachability function f, union F, Lebesgue measure mu, and Problem 1 with inequality (1)"},
 {"file": "references/paper.md", "heading": "IV. Method", "purpose": "Section opener for the algorithms"},
 {"file": "references/paper.md", "heading": "A. Overview", "purpose": "Section IV: idea of the delta-packing approach; Algorithm 1 (GreedyPack) image and transcription"},
 {"file": "references/paper.md", "heading": "B. Approximately-optimal Algorithm", "purpose": "Section IV: Algorithm 2 (ApproximateReachability), including the line that sets delta from epsilon"},
 {"file": "references/paper.md", "heading": "C. Anytime, Asymptotically-optimal Algorithm", "purpose": "Section IV: Algorithm 3 (AnytimeApproximateReachability)"},
 {"file": "references/paper.md", "heading": "V. Analysis", "purpose": "Section opener: what is proved, which proofs are omitted, intuition and roadmap of Lemmas 3-6 and Theorems 7, 10"},
 {"file": "references/paper.md", "heading": "A. Preliminaries", "purpose": "Section V: Hausdorff distance, delta-fattening, Assumptions 1-3, rectifiability, covering/packing numbers, Theorem 1, Lemma 2 (size of the GreedyPack output) with proof"},
 {"file": "references/paper.md", "heading": "B. Analysis of Algorithms 2 and 3", "purpose": "Section V: Minkowski content (2), Lemmas 3-6, Theorem 7 (packing precision delta vs epsilon), Corollary 8, Corollary 9 (sample size), Theorem 10 (running time), Proposition 11 (anytime variant)"},
 {"file": "references/paper.md", "heading": "VI. Results", "purpose": "Section opener: simulation goal, implementation and hardware"},
 {"file": "references/paper.md", "heading": "A. Experimental Setup", "purpose": "Section VI: unicycle dynamics (7), ground-truth reachable set, RSL curve parametrisation"},
 {"file": "references/paper.md", "heading": "B. Evaluation of Computed Reachable Sets", "purpose": "Section VI: scenarios, comparison with uniform sampling, Figures 2-4, number of trials"},
 {"file": "references/paper.md", "heading": "VII. Conclusion", "purpose": "Summary and future work"},
 {"file": "references/paper.md", "heading": "Acknowledgments", "purpose": "Funding"},
 {"file": "references/paper.md", "heading": "References", "purpose": "Bibliography [1]-[36]"},
 {"file": "references/paper.md", "heading": "Conversion notes", "purpose": "Source version, how the mathematics was transcribed, omitted proofs, list of misprints kept as printed"},
]
json.dump(b, open(W + "/bundle.json", "w"), ensure_ascii=False, indent=2)
print("ok")
