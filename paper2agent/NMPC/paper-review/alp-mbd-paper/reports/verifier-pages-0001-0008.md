# Independent verifier report: ALP-MBD (arXiv:2602.02831v1), pages 1-8

Status: COMPLETE

- PKG (actual): /home/jixia/AI_agents/paper2agent/NMPC/paper-review/staging/alp-mbd-paper-s1
  (the path first given in the assignment, NMPC/staging/alp-mbd-paper-s1, does not exist; the coordinator confirmed the correct path)
- DOC: /home/jixia/AI_agents/paper2agent/NMPC/paper-review/alp-mbd-paper/documents/s001-alp-mbd
- Ground truth: DOC/source.pdf (8 pages). Crops at 200-330 dpi with p2s_tools.py `crop`; native text with `lines`.
- Scratch: /home/jixia/AI_agents/paper2agent/NMPC/paper-review/_scratch/alp-mbd-v1 (crops, line dumps, diff scripts and outputs)
- The authors' TeX source was not consulted. Nothing from the paper was executed.

## Summary

**0 errors, 3 minors** (plus one note on the assignment path). The text, mathematics, tables, algorithm, figures and
references are faithful to the PDF. The only defect in the content is a double-escaped LaTeX header cell in the Markdown
copy of Table II (M1). The other two minors concern index boilerplate and one claim in the conversion notes that cannot be verified.

## Coverage (what was actually done)

All 8 pages, all checks; nothing was sampled except where stated.

1. **Prose, all pages, automated and complete.** I dumped the native text lines of every page and diffed them against
   paper.md. Display and inline maths, figure/table links and URLs were masked, and the comparison was run twice:
   (a) word/number tokens; (b) whitespace tokens with punctuation, quotes, dashes and en dashes. All non-equal opcodes
   were inspected. The only differences left were masked maths, the rejoined URL, diacritics split by extraction
   (H¨onig, M¨uller), and line-end hyphenation. For each of the 66 line-end hyphens I checked separately whether the package
   joined the word or kept a real hyphen: all 66 are correct (soft hyphens joined; real hyphens kept in variance-preserving,
   state-of-the-art, finite-horizon, Monte-Carlo, trial-and-error, decision-making, flow-matching–inspired, VP-/LP-/ALP-/AVP-MBD,
   sampling-based, Neural-swarm2, actor-critic, Thirty-seventh). No word, number, punctuation mark or sentence was missing,
   duplicated or reordered. This covers the abstract, the footnote, all sections, all captions, the Algorithm 1 text,
   both table captions and all 41 references.
2. **Display maths (1a)-(22)**: every equation compared with a 260-300 dpi crop, symbol by symbol (bars, hats/tildes,
   sub/superscripts, fractions, roots, signs, brackets, underbraces in (6) and (12), stacked subscript in (19), tags).
3. **Inline maths**: every inline expression in III-A to V-C, the Fig. 2 and Fig. 4 captions and Algorithm 1 compared
   with crops.
4. **LaTeX sanity**: script check of all 24 display blocks (brace balance, \left/\right, \begin/\end, one \tag each; tags
   are 1a,1b,1c,2..22 in order) and of every inline $...$ (balanced, even $ count per line).
5. **Tables**: all 30 cells of Table I and all 20 cells of Table II, CSV and Markdown copies, against 330 dpi crops;
   bold cells checked.
6. **Algorithm 1**: transcription compared line by line (13 numbered lines plus the wrapped lines 1 and 5) with a 300 dpi crop
   and with algorithm-1.jpg.
7. **Figures**: opened figure-1..6.jpg and algorithm-1.jpg and compared each with the PDF region: complete, no caption
   or body text inside, colour bars, axis labels and panel titles present.
8. **References [1]-[41]**: all present and in order. Every entry was checked token by token by the automated diff (authors,
   titles, venues, volumes, pages, years, URLs). In addition, every entry [1]-[41] was checked visually for italics and the "——"
   in [12] on 230 dpi crops.
9. **SKILL.md, index.md, supplement.md, conversion notes**: read in full. Every index heading was grep-checked as an exact
   heading in paper.md, and each claim in the notes was checked (see below).

## Findings

| # | severity | PDF page | item id | package says | PDF shows | suggested fix |
|---|---|---|---|---|---|---|
| M1 | minor | 7 | p0007-b006 (Table 2) | paper.md line 335, Markdown header of Table II: `$\\sigma_{\\max}$` (double backslashes). In $...$ maths this renders as a line break plus "sigma", not σ_max. The CSV is correct (`$\sigma_{\max}$`). | header σ_max | Write `$\sigma_{\max}$` in the paper.md table header. |
| M2 | minor | — | index.md (Assets) | index.md lists `assets/supp_figs/` and `assets/supp_table/` as asset folders | the package has only `assets/figure/` and `assets/table/` (there is no supplement) | Drop the two lines, or mark them "(none in this package)". |
| M3 | minor | — | paper.md Conversion notes, bullet 1 | "byte-identical to the arXiv PDF" | Cannot be verified offline. The local copy NMPC/papers/alp-mbd.pdf, also an "arXiv GenPDF (tex2pdf:57610bf)" build of v1 with the same 8 pages, is **not** byte-identical to DOC/source.pdf (1,657,960 vs 2,459,994 bytes). Extracted text and the embedded-image list are identical, so the content is the same. | Reword to "identical in content to arXiv:2602.02831v1" or drop "byte-identical". |

Note (not a package defect): the PKG path given in the assignment did not exist; the coordinator's correction matches the directory used.

No errors found: no wrong symbol, sign, number, cell, heading, omitted sentence or reference.

## Checked and found correct (by page)

- **p1**: title; author line; affiliation footnote (moved after the author line as "Footnote (printed without a marker):", by convention); abstract
  complete, including the URL rejoined from "…/adaptive_l" + "inear_path_model_based_diffusion-C58C" (correct);
  I. INTRODUCTION paragraphs 1-6 and contributions 1)-2) with their bold lead-ins; arXiv stamp omitted (convention).
- **p2**: contribution 3); Fig. 1 (both panels complete) and caption; II. RELATED WORK (3 paragraphs, all citations);
  III intro; III-A heading; (1a), (1b) with "s.t.", (1c) with t = 0,…,T−1; Y=[x_{1:T};u_{1:T}]; (2); p_J ∝ exp(−J/λ), λ>0;
  {α_i}_{i=1}^N; (3); (4) with sqrt(\bar α_i), sqrt((1−\bar α_i)) with parentheses as printed, product k=1..i;
  ε∼N(0,I); Var[Y^(0)]=1; c²_{i,0}+c²_{i,1}=1; β0=1.0×10^-4, β1=1.0×10^-2, α_i=1−β_i.
- **p3**: (5) (two lines; first coefficient c_{i−1,0}/c_{i,0} with c²_{i,1}, second 1/√α_i, no bar, with (1−\bar α_i));
  (6) (signs, √\bar α_i/(1−\bar α_i), the underbrace label, sum over 𝒴^{(i)}_{VP-MBD}); w(Y)=p_J p_g; (7) mean Y/√\bar α_i,
  variance (1−\bar α_i)/\bar α_i; (8) √\bar α_{i−1}; the coupling paragraph; III-B heading; italic *linear probability path*;
  (9); t_i=i/N; (10); c_{i,0}=1−t_i, c_{i,1}=t_i; endpoint sentence; (11) with (1−t_{i−1})/(1−t_i) and t_i²; (12) with −Y/t_i² + (1−t_i)/t_i²
  and the underbrace; (13) with mean Y/(1−t_i) and variance t_i²/(1−t_i)²; (14) with (1−t_{i−1}); σ_i=t_i/(1−t_i); (15); (16) with the
  bracketed "equivalently" form.
- **p4**: III-C (italic *decoupled*); IV intro (2 paragraphs); IV-A; MDP tuple; s′∼𝒫(·|s,a); (17), both lines; 𝒯={T_min,…,T_max};
  a_t=(T_t,σ_{max,t}); (18) w_T T_t/T_max; w_T>0; π_LP-MBD(·|s_t,a_t); (19), including the two-line stacked subscript, the
  brackets around Σ_{t=0}^∞ γ^t \tilde r_t and the trailing comma; γ∈(0,1); 𝓑; Fig. 2 (complete) and caption; IV-B heading.
- **p5**: IV-B paragraphs (DDPG[31], SAC[29][38][39], TD3[32]; \tilde r_t, φ, ψ); Algorithm 1 (all 13 lines; nesting; Eq. (18);
  (s_t,a_t,u_t,\tilde r_t,s_{t+1}); 𝓑); V. EXPERIMENTS intro (RTX 4090; β0=0.0001, β1=0.01, σ_max=1.8); V-A paragraphs 1-4;
  T=2; (20) (√((1−\bar α_i)/\bar α_i)=[0.1, 0.01], t_i/(1−t_i)=[1.8, 0.0], (i=1,0)); β0=10^-2, β1=10^-4 kept as printed; T=5, 0.16;
  REINFORCE [40], w_T=1.0, (30) updates; T=3; (σ_max,T).
- **p6**: end of the Fig. 4 paragraph; Fig. 3 (9 panels, 3 colour bars, all axis labels) and caption; Fig. 4 (6 panels, 2 colour bars)
  and caption (3x_0−x_1≥2.0; β0=0.000028, β1=0.361, T=3; σ_max=2.11, T=3); V-B paragraphs; Table I caption and all cells;
  V-C opening; state x=[x,y,θ,v]; (21), all four lines; Δt; (22), including the line break, the italic w_v, the upright subscripts
  lat/yaw/ref/collision and the bold 1; ψ_ref kept as printed; w_•; RL input state tuple; d_θ, d_vel definitions.
- **p7**: H=50, sampling number 100, Python 3.11/PyTorch; Table II paragraph; Fig. 5 and Fig. 6 paragraphs ("efficiency of VP-MBD" kept as printed);
  Table II caption and all cells; Fig. 5 and Fig. 6 (both panels, colour bars, axes) and captions; VI. CONCLUSIONS; refs [1]-[4].
- **p8**: refs [5]-[41]: text, punctuation, italics, URLs, "——" in [12], "p." vs "pp." as printed, "FreiburgimBreisgau" and
  "algorithms.”" punctuation as printed.
- **Tables**: Table I bold = header row; Ant/CEM; Hopper, HalfCheetah, Walker2D LP-MBD; Reacher VP-MBD and LP-MBD; Pusher VP-MBD.
  This matches the notes exactly (Hopper VP-MBD 2.74 ± 0.03 is correctly not bold). Table II bold = header "Methods" only, LP-MBD
  runtime 36.9, ALP-MBD reward -3342 ± 128. This matches the notes exactly. Minus signs are printed as hyphens and stored as ASCII hyphen-minus.
  The Table I Markdown copy matches the CSV.
- **Index**: all 15 headings exist exactly once in paper.md at the stated levels (## sections, ### subsections). The topic
  descriptions are accurate (equation ranges, figure and table placement). "Document beginning" for supplement.md follows the
  convention used in the other NMPC packages.
- **Conversion notes, claim by claim**: 8 pages, IEEE two-column, authors, UC Berkeley, no supplement: true. URL rejoined from
  two lines: true. Multi-line equations (5), (6), (12), (17), (20), (21), (22) as single aligned blocks with one \tag, and (1a)-(1c)
  one block each: true. Underbrace label kept: true. (20) spacing: the printed gaps (about 5 mm after the method label and about 4 mm
  before "(i = 1, 0)", measured on the 260 dpi crop) are rendered as \qquad/\quad; this changes spacing only, so the claim is
  true. Algorithm 1 kept as image plus transcription: true. Bold lists: true (see above). Authors' slips, each confirmed on
  the PDF: β0/β1 swapped in V-A; T in the VP triplet vs N in (3)-(4), and T as the horizon in (1); ψ_ref vs θ_ref; "efficiency
  of VP-MBD"; Fig. 4 caption "top row shows the result of VP-MBD" while the first sentence says AVP-MBD; "ALP-MBD successfully discover".
  Figures not tabulated, floats near printed position, subsection letters restart: true. The only questionable claim is
  "byte-identical" (M3). "Transcribed from the authors' arXiv TeX source" is a provenance statement and was not checked, because
  the TeX was deliberately not consulted; I found no disagreement between the package maths and the PDF.
- **SKILL.md**: generic navigation instructions; nothing false about this package. supplement.md: "No corresponding
  materials were supplied." This is consistent.

## Technical question test

**Question:** "With the default σ_max = 1.8 used for LP-MBD, at what interpolation time t_max is the linear path truncated,
and what is the Gaussian proposal standard deviation at the first (noisiest) denoising step compared with VP-MBD for the T = 2
example?"

**Answer using only the package:** paper.md III-B, Eq. (16) gives t_max = σ_max/(1+σ_max) = 1.8/2.8 ≈ 0.643 (σ_max = 1.8 is
stated in the V intro). Eq. (13) gives the LP-MBD proposal std σ_i = t_i/(1−t_i), which equals σ_max = 1.8 at t_i = t_max.
V-A, Eq. (20), for T = 2: LP-MBD gives [1.8, 0.0] for i = 1, 0, while VP-MBD gives √((1−\bar α_i)/\bar α_i) = [0.1, 0.01]. The
noisiest LP step therefore explores with std 1.8, versus 0.1 for VP-MBD, which the text says suppresses exploration.

**Check against the PDF:** the crop of p.3 (16) shows σ_max = t_max/(1−t_max) and, equivalently, t_max = σ_max/(1+σ_max). The crop of p.3
(13) shows the variance t_i²/(1−t_i)², and the text gives σ_i = t_i/(1−t_i). The p.5 crop of (20) shows [0.1, 0.01] and [1.8, 0.0] with
(i = 1, 0), and the V intro on p.5 gives σ_max = 1.8. The answer is fully supported by the PDF.
