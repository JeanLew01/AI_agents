# Review report: DiffPF (s001-diffpf), pages 1-8

Reviewer scope: all 8 pages. TeX source: `tex-source/diffpf/main.tex` (active document starts at line 660; lines 1-658 are a commented-out older draft and were ignored). `\bm` expanded to `\boldsymbol` throughout.

## Per-page log

- **Page 1** (done, check OK 96/96). Omitted running header, page number "1", rotated arXiv stamp. Title `#`, author line, three unnumbered `\thanks` footnotes placed right after the author line. Abstract / Index Terms as run-in text. Drop-cap scramble in first Intro paragraph repaired. Hyphens restored: high-dimensional, data-driven, sample-based. Para "An alternative line of work" joined across columns (`join_previous: space`), Fig. 1 + caption placed after it. **Figure 1** -> `figure-1`, bbox [313,150,563,272]. Last item ends "elimi" (hyphen removed) -> continues on page 2.
- **Page 2** (done; 7 missing lines, all inline maths, category (a), adjudication note written). First item joins page 1 with `join_previous: none` ("elimi|nates"). New item `p0002-b002a` ("Our main contributions are summarized as follows:") split off as its own paragraph. Headings: `## II. RELATED WORKS`, `### A./B./C.`, `## III. METHOD`. Hyphens restored: real-world, state-of-the-art, Sampling-Importance-Resampling.
- **Page 3** (done; 40 missing lines + minus-sign number differences, all category (a), adjudication note written). **Figure 2** (full-width diagram, top of page) -> `figure-2`, bbox [44,50,566,163]. Equations (1)-(7) as LaTeX display blocks with `\tag{}`; (7) is one `aligned` block with `\tag{7}`. Headings `### A. Prediction and Perception Modeling`, `### B. Update Step`. Cross-column join (`p0003-b017`, space). Hyphens restored: time-dependent, noise-perturbed. Author typo kept: `x^{(i)}_{t.k}` in (7) (PDF and TeX agree). Last item continues on page 4.
- **Page 4** (done; 21 missing lines + minus-sign number differences, all category (a), note written). First item joins page 3 (`space`). Equations (8), (9), (10) as LaTeX. Headings `### C. End-to-End Training`, `## IV. EXPERIMENTS`, `### A. Vision-based Disk Tracking`. Left-column paragraph ending "cosine annealing" joined to right-column "schedule. ..." (`p0004-b014`, space); **Figure 3** placed after it -> `figure-3`, bbox [311,51,565,160]. New item `p0004-b020a` ("**Results:** ...") split from the Implementation paragraph. Hyphen restored: Deep State-Space.
- **Page 5** (done; 21 missing lines + exponent-glue number differences, all category (a), note written). **Table I** -> `table-1` (13x3; multirow "Setting" groups repeated per row), **Table II** -> `table-2` (2x6); captions kept above tables as printed. List items 2)/bullets repaired. Overview paragraph joined across columns (`p0005-b016`, space); **Figure 4** placed after it -> `figure-4`, bbox [311,51,564,150]. Equation (11) bmatrix LaTeX. Heading `### B. Global Localization`. Hyphens restored: real-time, particle-based. Kept as printed: "Eq. 10", "with $o_t$, We encode", $\theta_t$ without $(i)$ in row 3 of (11). Last item continues on page 6.
- **Page 6** (done; 1 missing line, $10\Sigma$ maths, category (a), note written). First item joins page 5 (`space`) and precedes the tables. **Table III** -> `table-3` (12x4), **Table IV** -> `table-4` (7x4), **Table V** -> `table-5` (3x6). Paragraph "As shown in Fig. 5" joined across columns (`p0006-b014`, space); **Figure 5** -> `figure-5` [312,51,563,233], **Figure 6** -> `figure-6` [310,273,565,333] placed after it. Heading `### C. KITTI Visual Odometry`. Last item continues on page 7.
- **Page 7** (done; 4 missing lines + one minus-sign difference, category (a), note written). First item joins page 6 (`space`) and precedes Table VI. **Table VI** -> `table-6` (10x4, header "deg/m)" kept). New item `p0007-b011a` (KITTI "**Comparison:** ...") split from "All of the experimental results are presented in Table VI."; it is joined across columns (`p0007-b017`, space). **Figure 7** -> `figure-7` [311,51,564,144]; **Table VII** -> `table-7` (7x5; merged headers flattened to "Real-world (MAE): Joint (deg)" etc.; "±" without spaces as printed); footnote "Means ± standard errors." as a caption item after the table. Heading `### D. Robotic Manipulation`.
- **Page 8** (done, check OK 160/160). Headings `## V. CONCLUSIONS`, `## REFERENCES`. Conclusions: "real-world" restored. References: all 41 entries, one item per entry in printed style `[n] ...`, sequence 1-41 verified, no column interleaving. Four two-entry extractor items split (new ids `p0008-b013a` [10], `p0008-b031a` [29], `p0008-b037a` [36], `p0008-b038a` [38]). Repaired "Ścibior", en-dash page ranges split at line wraps (107–113, 6840–6851), emphasis spacing, "[36] α-mdf: An attention-based" (Unicode α so the reference page stays OK).

## Summary

### Final state
All 8 pages `reviewed: true`, notes start with `[v2]`. Pages 1 and 8: `OK`. Pages 2-7: `ATTENTION` only from LaTeX maths (missing lines that contain inline/display maths; U+2212 vs ASCII minus; glued exponents `102` = $10^2$). All category (a); adjudication notes written for pages 2, 3, 4, 5, 6, 7 (`DOC/adjudication-notes/page-000N.json`). No category (b) remains.

### Assets
| Page | Asset | Label | bbox |
|---|---|---|---|
| 1 | figure-1 | Figure 1 (diagram, embedded maths) | [313,150,563,272] |
| 3 | figure-2 | Figure 2 (full-width diagram, embedded maths) | [44,50,566,163] |
| 4 | figure-3 | Figure 3 (panels a-c) | [311,51,565,160] |
| 5 | table-1 | Table 1 (13x3) | rows |
| 5 | table-2 | Table 2 (2x6) | rows |
| 5 | figure-4 | Figure 4 (panels a-b) | [311,51,564,150] |
| 6 | table-3 / table-4 / table-5 | Tables 3-5 (12x4, 7x4, 3x6) | rows |
| 6 | figure-5 | Figure 5 (panels a-d) | [312,51,563,233] |
| 6 | figure-6 | Figure 6 (3 panels) | [310,273,565,333] |
| 7 | table-6 | Table 6 (10x4, header "deg/m)" as printed) | rows |
| 7 | figure-7 | Figure 7 | [311,51,564,144] |
| 7 | table-7 | Table 7 (7x5) | rows |

Equations: (1)-(7) on page 3, (8)-(10) on page 4, (11) on page 5. All are LaTeX display blocks with `\tag{n}`. (7) is one `aligned` block with a single `\tag{7}`. **No formulas kept as images.** No algorithms in this paper. Asset names are plain (`figure-N`, `table-N`) because one reviewer covers the whole paper, so they cannot clash.

### Table conventions
- Merged row-group labels (the multirow "Setting" column in Tables I and VI) are repeated on every row of their group.
- Table VII's two-level header is flattened to `Real-world (MAE): Joint (deg)`, `Real-world (MAE): EE (cm)`, `Simulation (MAE): Joint (deg)`, `Simulation (MAE): EE (cm)`.
- Table VII cells keep "±" without spaces, as printed. Tables I-VI print "a ± b" with spaces.
- Captions stay above the tables, as printed in IEEE style.
- The Table VII footnote "Means ± standard errors." is a `caption` item after the table.
- Bold best rows were dropped as typography.

### Joins
- Within my range: page 2 first item `none` ("elimi|nates"; hyphen removed from page 1); pages 4, 6, 7 first items `space`.
- Cross-column joins (each with the float moved after the completed paragraph): p0001-b015, p0003-b017, p0004-b014, p0005-b016, p0006-b014, p0007-b017.
- Range boundaries: page 1 starts the paper and page 8 ends it, so no joins are needed with other reviewers.

### New item ids
p0002-b002a, p0004-b020a, p0007-b011a, p0008-b013a, p0008-b031a, p0008-b037a, p0008-b038a. These were split off as separate paragraphs or reference entries.

### TeX vs PDF
- No disagreements found. The PDF matches the active TeX body (main.tex line 660 onward). Lines 1-658 are a commented-out older draft with different abstract numbers, and I ignored them.
- `\bm` was expanded to `\boldsymbol`. `\hl{}` is a no-op in the TeX (`\renewcommand{\hl}[1]{#1}`).

### Author typos and oddities kept as printed
- `x^{(i)}_{t.k}` (a period instead of a comma) in (7).
- Non-bold $\epsilon_\theta$ in (7) and (9), but bold in prose.
- $\theta_t$ has no $(i)$ in row 3 of (11).
- "Eq. 10", "Fig 4" (no period), "with $o_t$, We encode".
- "equally weighted particles samples" (Fig. 1 caption) and "green arrow represent" (Fig. 5 caption).
- "The internal state $x \in \mathbb{R}^{10}$ composed of" (missing verb).
- "an unidirectional LSTM".
- Table VI header "deg/m)".
- Ref [41] "A. Graves and A. Graves".

### Proposals for shared files
- No plan.json changes needed: there are no floats that need `reading_order`, since every float was placed between complete paragraphs within its page.
- Possible plan note: "Fig. 1 and Fig. 2 contain embedded equations (DDPM update, particle mean) that are also given in the text as (7) and (8)."

### Limitations and brief feedback
- Fig. 1/2 internal maths are only in the images. The same content appears as text equations (7)/(8), except the forward-noising expression $x_{t,k}=\sqrt{\alpha}x_{t,k-1}+\sqrt{1-\alpha}\epsilon$ in Fig. 2, which exists only in the image.
- Brief: the `check` tool does not distinguish table-caption placement. Re-running an edit script that reloads an already-edited page fails, so write scripts to be idempotent or patch in place. This was minor and is handled.
