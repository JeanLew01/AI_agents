# Reviewer report: liebenwein2018sampling

## Result

- Paper: Liebenwein, Baykal, Gilitschenski, Karaman, Rus, "Sampling-Based Approximation Algorithms for Reachability Analysis with Provable Guarantees".
- Source version: RSS 2018 proceedings PDF, 10 pages, two-column. No TeX source, so all mathematics was transcribed visually.
- `verify --strict`: status `reviewed_with_limitations`, exit code 0 (19 adjudications applied, 0 stale, no mechanical issues, all 7 image crops match the source).
- Final package: `/home/jixia/AI_agents/paper2agent/Reachability/skills/liebenwein2018sampling-paper`
- Review directory: `/home/jixia/AI_agents/paper2agent/Reachability/paper-review/liebenwein2018sampling-paper`
- Scratch (page scripts, renders, checks, `verify-strict.out`, `review-queue-after-s2.json`): `/home/jixia/AI_agents/paper2agent/Reachability/logs/work/liebenwein2018sampling/`
- Staging builds: `staging/liebenwein2018sampling-paper-s1`, `-s2`, `-s3`. The final `paper.md` is byte-identical to s3.

## Counts

| Item | Count |
| --- | --- |
| Pages reviewed | 10 of 10 |
| Figures | 4 (Figure 1-4) |
| Tables | 0 (the paper has none) |
| Algorithms | 3 (image crop plus transcription each) |
| Displayed formulas transcribed to LaTeX | 24 (printed numbers (1)-(7) as `\tag`) |
| Formulas kept as images | 0 |
| Omitted regions | 0 (the PDF has no page numbers, headers or banners) |
| Adjudications | 19 (8 missing-lines, 6 number, 5 second-parser number) |
| Bibliography entries | 36, each read against a 260 dpi crop |

## What was corrected

- **Mathematics (pages 2-6).** Every inline and displayed formula was rewritten in LaTeX. Pages 4-6 were read on 330 dpi crops; Theorem 7, Corollaries 8-9 and Theorem 10 on 600 dpi crops. The extractor's formula image boxes were all replaced.
- **Reading order.** Paragraphs split across columns were merged on pages 1, 2, 4 and 7. The paragraph running from page 3 to page 4 and reference [28] running from page 9 to page 10 are joined with `join_previous`.
- **Floats.** Algorithms 1-3 sit after Sections IV-A, IV-B and IV-C. Figures 2-3 (printed above the VI-B heading) sit inside VI-B. No float interrupts a sentence.
- **Headings.** All were level 1 in the extraction and are now level 2 or 3. "IV. METHOD" had been extracted as a formula image, "2000. 2" (the end of reference [14]) as a heading, and "REFERENCES" as plain text.
- **Theorem-like blocks.** Bold labels with the printed numbering and punctuation, including `**Proof:**`. The conversion notes say where each statement ends.
- **Algorithms.** One paragraph per printed line, printed line numbers, `&emsp;&emsp;` per nesting level, small-caps names in CamelCase.
- **Text repairs.** All 70 line-end hyphens in the PDF text layer were each classified as a wrap or a real compound. Diacritics were restored in references [5], [9], [10], [27]. `IIS-1723943`, the URL in [35], and the volume(issue):pages strings of [23] and [33] were closed up.

## Checks run

- Extended symbol count (`symbol_check2.py`): 36 counters per page (relations, set symbols, quantifiers, arrows, norm bars, primes, hats, Greek letters) agree between the PDF text layer and the markdown on all 10 pages.
- `mathcheck.py`: all 24 displays and 409 inline formulas compile with pdflatex; I compared the rendered displays with the page crops.
- `check_missing.py`: 17 of the 227 "missing" lines fail the word-order test; each is a glyph-soup token (`mini`, `maxx`, `limi`, `supX`, `FSi`, `vmin`), a line-end word fragment, or the split diacritics of "Ivančić".
- Number differences: every one is accounted for. They are Unicode versus ASCII minus in `d − 1` and `−1/d`, the algorithm transcriptions, the Figure 1 sub-captions, and the hyphen in `IIS-1723943`. The second-parser differences on pages 4-6 were confirmed in pypdf's raw text.

## Limitations and uncertainties

No symbol of any formula is left uncertain. The points below are printed that way in the paper and transcribed as printed; they are also listed in the conversion notes.

- **Page 6:** Corollary 8 and Theorem 10 print the guarantee as μ(F̂_S) ≥ (1 − ε)μ(F(S)), with calligraphic S inside F (confirmed at 600 dpi). Theorem 7 and the Output line of Algorithm 2 compare with μ(F(X)). This looks like a misprint in the paper.
- **Page 6:** the proof of Lemma 6 prints "=" where (6) has "⊆". Section VI-A prints "X ∈ R^3".
- **Pages 3 and 4:** Algorithm 1 line 2 prints the loop condition with "≥ δ"; the proof of Lemma 2 negates a statement with "> δ".
- **Page 2:** "f(x) ⊆ 2^Y" is printed where f(x) ⊆ Y would be expected.
- **Page 4:** Assumption 2 prints d_H with an italic H (upright elsewhere). The m-rectifiable definition prints "onto Y".
- **Page 5:** a short bar above A in the inline fraction for h(δ) is the lower stroke of "≥" in the subscript of R≥0 on the line above (checked at 900 dpi), so it is transcribed as μ(A_δ).
- **Omitted proofs:** the paper prints proofs only for Lemmas 2, 4, 5 and 6. Lemma 3, Theorem 7, Corollaries 8-9, Theorem 10 and Proposition 11 have none, and there is no appendix.
- **Figures:** plot contents (curves, tick values) are only in the image crops.
- **Figure 1 (page 1):** the sub-captions "(a) (1 − ε) = 0.2 ... (d) (1 − ε) = 0.8" are inside the crop and also repeated as a caption item so they are searchable. This causes the page-1 number adjudications.
- **References:** each entry ends with the paper's printed back-reference page numbers (for example "2014. 2"); they are kept.
- **Package directory mode:** the final directory was created with mode 700 by the builder, like the two packages already in `skills/`; I did not change it.

## Self-check question

**Question.** State the approximation guarantee: what ε and δ bound, the assumptions on the dynamics, and the sample size.

**Answer from the package.**

- **Setting** (Section III): ẋ = h(x,u), x ∈ R^d, u ∈ U ⊂ R^m compact, h continuously differentiable. X ⊂ R^d is the compact set of initial states, f(x) = H(x,T) the set reachable at terminal time T, F(X') = ∪_{x∈X'} f(x), and μ the Lebesgue measure. X and F(X) are compact.
- **Assumptions** (Section V-A):
  1. f(x) is measurable with μ(f(x)) > 0 for all x ∈ X.
  2. d_H(f(x), f(y)) ≤ K‖x − y‖ for all x, y ∈ X.
  3. F(X') is compact, and its δ-fattening is (d − 1)-rectifiable for every δ ≥ 0 and every X' ⊆ X.
- **Theorem 7:** for any ε ∈ (0,1), the GreedyPack δ-packing S ⊂ X with δ ≤ d((1 − ε)^{−1/d} − 1)/(αKc) satisfies (1 − ε)μ(F(X)) ≤ μ(F(S)) ≤ μ(F(X)). Here α = sup_{X'⊆X} λ(∂F(X'))/μ(F(X')) < ∞ and c = max{M/(dμ(B_1(·))^{1/d}), 1} is the constant of Lemma 3.
- **Sample size:** Corollary 9 gives |S| ≤ (3αKΔ(X)c/ε)^d. Lemma 2 gives (1/δ)^d μ(X)/C ≤ |S| ≤ (3Δ(X)/δ)^d with C = π^{d/2}/Γ(d/2+1) and Δ(X) = max_{x,y∈X}‖x − y‖.
- **Running time** (Theorem 10): O(C_α + C_K + C_c + C_S + (αKΔ(X)c/ε)^d C_f).
- **Meaning of ε and δ:** ε is the relative volume error of an under-approximation and δ is the packing precision. The guarantee is deterministic; δ is not a confidence level and there is no probabilistic statement.

**Where it came from.** `references/paper.md`, headings "III. Problem Definition", "A. Preliminaries" and "B. Analysis of Algorithms 2 and 3".

**Check against the PDF.** Compared with the 600 dpi crops of page 6 and the 330 dpi crops of page 4; it matches. As a consistency check, Bernoulli's inequality gives (1 − ε)^{−1/d} − 1 ≥ ε/d, so the largest admissible δ is at least ε/(αKc), and Lemma 2 then gives |S| ≤ (3αKΔ(X)c/ε)^d, which is Corollary 9 as transcribed.

## Tool pitfalls and brief feedback

- **Proof label.** The brief's first example `**Proof.**` conflicts with the later rule to keep the printed label punctuation; this paper prints "Proof:". That cost one page regeneration and one staging build.
- **Algorithm format.** The rule (one paragraph per line, `&emsp;&emsp;`) arrived after my first final build, so I had to delete and rebuild the final directory. The diagnostic fingerprints did not change, so the adjudications stayed valid. The rule belongs in the "Figures, tables, algorithms" section.
- **`symbol_check.py` as shipped** counts `\subseteq` as `\subset`, `∉` as `∈`, `≠` as `=`, and mixes single bars with norm bars, so it reports false differences on set-heavy pages. `symbol_check2.py` in my scratch folder separates these and adds quantifiers, ∪, ∂, primes, hats, ← and Greek letters.
- **pypdf.** It is not importable from the system `python3`. To explain second-parser differences without `uv run`, I imported it read-only with `PYTHONPATH=~/.cache/uv/archive-v0/<hash>` pointing at the cached wheel.
- **Figure sub-captions.** The brief does not say what to do with sub-captions printed inside a figure. Transcribing them is useful for search but always produces "extra number" diagnostics.
- **Overlapping text lines.** A subscript stroke from the line above can look like an overline in an inline fraction (page 5). Such spots need 600-900 dpi.
- **Staging count.** The brief implies one staging build may suffice. A second is needed whenever wording changes after the diagnostics review, so settle label and algorithm conventions before the first staging build.
