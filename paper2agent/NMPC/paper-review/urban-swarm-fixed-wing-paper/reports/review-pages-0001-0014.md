# Review report: "Agile Fixed-Wing UAVs for Urban Swarm Operations", PDF pages 1-14

Reviewer range: `pages/page-0001.json` ... `page-0014.json` (brief version 2, no TeX source available).
Document: `documents/s001-urban-swarm-fixed-wing`. Mathematics transcribed from 260-280 dpi crops of the page.
Scratch: `_scratch/swarm-1-14/` (files prefixed `v2` are from this run; the others are from the interrupted v1 run).

## Final state

All 14 pages are `reviewed: true` with `review_notes` starting with `[v2]`. Every page was re-examined from the
page image; the structural work of the interrupted run (figure boxes for Figures 1-4, headings, joins on pages 1-12)
was checked and reused, pages 13-14 were done from scratch. No formula is kept as an image: every symbol of
equations (1)-(26) was legible at 260-280 dpi. No tables and no algorithm boxes occur in pages 1-14.

| Page | Printed | check | Missing lines | Number diffs | Note file |
| --- | --- | --- | --- | --- | --- |
| 1 | 725 | OK | 0 | - | - |
| 2 | 726 | OK | 0 | - | - |
| 3 | 727 | ATTENTION | 1 (a) | - | yes |
| 4 | 728 | OK | 0 | - | - |
| 5 | 729 | OK | 0 | - | - |
| 6 | 730 | ATTENTION | 1 (a) | - | yes |
| 7 | 731 | ATTENTION | 2 (a) | - | yes |
| 8 | 732 | ATTENTION | 40 (a) | `−1`x2 vs `-1`x2 (a) | yes |
| 9 | 733 | ATTENTION | 12 (a) | `−1` vs `1` (a) | yes |
| 10 | 734 | ATTENTION | 8 (a) | `−1` vs `-1` (a) | yes |
| 11 | 735 | ATTENTION | 19 (a) | - | yes |
| 12 | 736 | ATTENTION | 15 (a) | `−1`x2 vs `-1`x2 (a) | yes |
| 13 | 737 | OK | 0 | - | - |
| 14 | 738 | ATTENTION | 1 (a) | `−4.9167` vs `-4.9167` (a) | yes |

Category (a) = LaTeX notation versus the PDF glyph stream (inline/display maths, degree signs, Unicode minus versus
ASCII minus, `-\frac{1}{2}` read by the parser as `−1`). Nothing of category (b) remains. The "second-parser"
number differences are identical to the first-parser ones on every page.

## Per-page log

### Page 1 (printed 725) - reviewed [v2]
- Kept as text: special-issue line, "Regular Article", title (`# Agile Fixed-Wing UAVs for Urban Swarm Operations`),
  authors, affiliation, abstract (two printed paragraphs), keywords, and the first-page footnote block split into
  received/revised/accepted/published dates, correspondence with email, open-access licence, copyright, DOI.
- Heading: `## 1. Introduction`.
- Order: the footnote block is placed before `## 1. Introduction` so the page ends with the introduction paragraph
  that continues on page 2.
- Omitted: header "Field Robotics, May, 2023 · 3:725–765 · 725" (b000) and the footer URL "http://fieldrobotics.net"
  (b014). Both extractor warnings resolved.
- Printed oddity kept: "revised: 21 November 2023; accepted: 7 March 2023" (revision dated after acceptance).
- Check: OK (39/39).

### Page 2 (printed 726) - reviewed [v2]
- Pure prose (seven paragraphs). First item `join_previous: space` (joins page 1). Last paragraph continues on page 3.
- Line wrap "Aero-/batic" rejoined. Omitted: header (b000), footer (b008).
- Check: OK (52/52).

### Page 3 (printed 727) - reviewed [v2]
- Headings: `## 2. Related Work`, `### 2.1. Quadcopter Planning and Control`, `### 2.2. Fixed-Wing Planning and Control`.
- First item `join_previous: space`. Last paragraph continues on page 4.
- Inline maths: `(attitudes $\leq 30^\circ$)`, `RRT$^*$`.
- Line wraps: "approx-/imations" rejoined, "cost-/function" kept as "cost-function".
- Authors' typos kept: "an urban swarm system system", "a dynamically a feasible motion plan".
- Omitted: header (b000), footer (b010).
- Check: 1 missing line, category (a) (`$\leq 30^\circ$`). Note written.

### Page 4 (printed 728) - reviewed [v2]
- Headings: `#### 2.2.1. Low angle-of-attack`, `#### 2.2.2. Post-stall regime`.
- First item `join_previous: space`. Last paragraph continues on page 5.
- Authors' typo kept: "is driven by a an outer control loop". Omitted: header (b000), footer (b009).
- Check: OK (50/50).

### Page 5 (printed 729) - reviewed [v2]
- Headings: `### 2.3. UAV Navigation with Onboard Sensors`, `### 2.4. Control of Multiple Dynamic Aerial Vehicles`,
  `## 3. Approach`.
- Footnote 1: marker written `[^1]` in the running text; the footnote is a text item `Footnote 1: ...` placed before
  the page's last paragraph (that paragraph continues on page 6).
- First item `join_previous: space`. Line wraps "optimiza-/tion", "su-/permaneuverability" rejoined;
  "virtual-/target-following" kept as a compound.
- Authors' wording kept: "an outer-loop a virtual-target-following guidance method".
- Omitted: header (b000), footer (b011).
- Check: OK (45/45).

### Page 6 (printed 730) - reviewed [v2]
- Figure 1 -> `figure-1` (three picture regions merged: photo (a), plot (b), sub-labels), bbox
  [98, 75.5, 506.5, 221.5]; caption item follows.
- Order: continuing paragraph first (`join_previous: space`), then Figure 1 with caption, then three paragraphs; the
  last continues on page 7.
- Inline maths: `$90^\circ$ turn` (caption), `($> 6$)`.
- Omitted: header (b000), footer (b009).
- Check: 1 missing line, category (a) (`$90^\circ$` in the caption). Note written.

### Page 7 (printed 731) - reviewed [v2]
- Figure 2 -> `figure-2`, bbox [167.5, 77, 445.5, 234]; Figure 3 -> `figure-3`, bbox [170, 308.5, 394.5, 487];
  captions follow each figure.
- Heading: `### 3.1. Dynamics Model`.
- Order: continuing paragraph first (`join_previous: space`), Figure 2 + caption, heading 3.1, Figure 3 + caption
  (frames of the dynamics model), then the first lines of the Section 3.1 paragraph, which continues on page 8.
- Inline maths in the Figure 2 caption: `$10^\circ$ and $15^\circ$`, `($\alpha < 10^\circ$)`.
- Figure-internal oddity (not altered): the colour bar of Figure 2 is labelled "Angle-of-Attack (rad)" with ticks 10-80.
- Omitted: header (b000), footer (b008).
- Check: 2 missing lines, category (a) (degree signs in the caption). Note written.

### Page 8 (printed 732) - reviewed [v2]
- Display maths as `$$...$$` text items: (1) state vector; (2)-(7) equations of motion (six blocks in one item, one
  `\tag` each); (8) body-frame force; (9) surface force; (10) surface velocity.
- Former image items `equation-1`, `equation-2-7`, `equation-8`, `equation-9`, `equation-10` converted to text.
- All inline maths in LaTeX (bold vectors, frames `$O_{x_r y_r z_r}$`, rotation matrices, transposes as
  `${\mathbf{R}_b^r}^T$`).
- First item ("We define our state as") `join_previous: space` (same paragraph as the end of page 7). Last item
  continues on page 9.
- Omitted: header (b000), footer (b014).
- Check: 40 missing lines + `−1`/`-1` (x2), all category (a). Note written.

### Page 9 (printed 733) - reviewed [v2]
- Display maths: (11) backwash velocity; (12), (13) flat-plate coefficient and angle of attack; (14) moments;
  (15) profile-drag term. Former image items `equation-11` ... `equation-15` converted to text.
- Heading: `### 3.2. Control Strategy`.
- Figure 4 -> `figure-4` (block diagram), bbox [151, 535, 457, 678.5]; caption follows. The page ends with this float
  after a complete paragraph; page 10 starts with a heading.
- First item `join_previous: space`.
- Printed as is: `$\gamma$` without subscript after (11) (equation (10) uses `$\gamma_i$`); "(Equation 5)"; `$i^{th}$`.
- Omitted: header (b000), footer (b017).
- Check: 12 missing lines + `−1` vs `1` (minus and numerator of (15)), all category (a). Note written.

### Page 10 (printed 734) - reviewed [v2]
- Heading: `#### 3.2.1. RRT generation and spline-based smoothing`.
- Display maths: (16) control-point matrices (two lines, one number; exponent printed "3x4" with a letter x);
  (17) cubic Bezier curve (two lines, first ends with "..." as printed); (18) derivative row vectors.
  Former image items `equation-16`, `equation-17`, `equation-18` converted to text.
- Inline maths in LaTeX (`$\mathbf{x} = [x_0, x_1, \ldots, x_n]$`, `$[W_1, W_2, W_3]$`, `$\kappa_{\max}$`,
  `2 m$^{-1}$`, ...).
- Authors' typo kept: "select an goal point".
- The page ends with equation (18); its sentence continues on page 11 (no join because of the `$$` block).
- Omitted: header (b000), footer (b011).
- Check: 8 missing lines + `−1`/`-1`, all category (a). Note written.

### Page 11 (printed 735) - reviewed [v2]
- Display maths: (19) curvature; (20) curvature-to-velocity map (printed with `*`); (21) time reparameterisation;
  (22) the direct-NMPC feasibility problem (one `aligned` block, single number); (23) Hermite-Simpson collocation
  definitions (one `aligned` block, single number). Former image items `equation-19` ... `equation-23` converted.
- Heading: `#### 3.2.2. Direct trajectory optimization`.
- Authors' typo kept: "and are are often more robust".
- First item follows equation (18) of page 10: no join. The page ends with equation (23).
- Omitted: header (b000), footer (b015).
- Check: 19 missing lines, all category (a); no number differences. Note written.

### Page 12 (printed 736) - reviewed [v2]
- Display maths: (24) TVLQR control law; (25) Riccati differential equation (two lines, one number, first line ends
  with "..." as printed); (26) gain matrix. Former image items `equation-24`, `equation-25`, `equation-26` converted.
- Headings: `#### 3.2.3. Local linear feedback control`, `## 4. Real-time Trajectory Optimization Performance`,
  `## 5. Motion Capture Experiments`.
- Inline maths in LaTeX, including `$h_{\min} = 0.001s$`, `$h_{\max} = 0.2s$`, `$90^\circ$` (x2), `$\approx 20$`,
  `($\approx$0.1s ...)`.
- Printed as is (possible authors' slips, not corrected): `$\mathbf{A}(t)$` is defined with `$\mathbf{x}_0$` without
  "(t)"; the Euler constraint reads `$\mathbf{x}_{k+1} - \mathbf{x}_k - h(\mathbf{x}_{\mathbf{k}}, \mathbf{u}_{\mathbf{k}}) = \mathbf{0}$`
  (no `$\mathbf{f}$`); "by a factor of almost 2-1".
- No join on the item after equation (25). Last paragraph continues on page 13.
- Omitted: header (b000), footer (b015).
- Check: 15 missing lines + `−1`/`-1` (x2), all category (a). Note written.

### Page 13 (printed 737) - reviewed [v2]
- Figure 5 -> `figure-5` (two picture regions merged: "NLP Execution Time" and "Trajectory Following Performance"),
  bbox [154.3, 74.6, 453.5, 294.9]; Figure 6 -> `figure-6` (photo), bbox [195.4, 370.2, 412.4, 534]. Captions follow.
- Heading corrected from `# ` to `### 5.1. Experimental Setup`.
- Order: continuing paragraph first (`join_previous: space`, joins page 12), Figures 5 and 6 with captions, heading,
  first paragraph of 5.1 (continues on page 14).
- Printed inconsistency kept: the Figure 5 caption says "Hermite-Simpson (blue) and Euler (green)" for the lower
  plot, whose legend shows Hermite-Simpson in green and Euler in dashed blue.
- Omitted: header (b000) and footer (b009), both previously extracted as text.
- Check: OK (17/17).

### Page 14 (printed 738) - reviewed [v2]
- Figure 7 -> `figure-7` (three panels merged), bbox [102, 416.9, 512.1, 523.9]; Figure 8 -> `figure-8` (three panels
  merged), bbox [102, 562.5, 512.1, 669.1]. Captions follow each figure.
- Heading corrected from `# ` to `### 5.2. System Identification`.
- Inline maths repaired (split decimals, emphasis markers): `$\gamma_{ar} = \gamma_{al} = \gamma_r = 0.1$`,
  `$\gamma_e = 0.3$`, `$C_{b_d} = 0.0$`, `$a_t = -4.9167$`, `$b_t = 9.6466$`.
- First item `join_previous: space` (joins page 13). The page ends with Figures 7 and 8; page 15 starts with the
  heading "5.3. Control Experiments", so no join is needed at the range boundary.
- Omitted: header (b000, was text) and footer (b014, was a caption).
- Check: 1 missing line + `−4.9167`/`-4.9167`, category (a). Note written.

## Assets in pages 1-14

| Asset | Page | Notes |
| --- | --- | --- |
| `figure-1` | 6 | photo (a) + turn-radius plot (b); 3 extractor regions merged |
| `figure-2` | 7 | turn radius vs wing loading |
| `figure-3` | 7 | coordinate frames, contains in-figure formulas for ω, v, r |
| `figure-4` | 9 | block diagram of the receding-horizon control approach |
| `figure-5` | 13 | two stacked plots; 2 regions merged; lower plot has very small tick labels in the source |
| `figure-6` | 13 | photo of the Edge 540 EPP model |
| `figure-7` | 14 | linear accelerations, 3 panels merged |
| `figure-8` | 14 | angular accelerations, 3 panels merged |

No formula images, tables or algorithm crops. Asset names follow printed numbering; no clash with the other ranges
(checked across all 41 page files: no duplicate asset names or item ids).

## Equations (all as LaTeX text with printed tags)

Page 8: (1)-(10). Page 9: (11)-(15). Page 10: (16)-(18). Page 11: (19)-(23). Page 12: (24)-(26).
Formulas kept as images: none. TeX-versus-PDF disagreements: not applicable (no TeX source).

## Joins

- `join_previous: space` set on the first content item of pages 2, 3, 4, 5, 6, 7, 8, 9, 13, 14.
- No join on pages 10 (starts with a heading), 11 (follows the `$$` block of equation (18)), 12 (new sentence after
  equation (23)).
- Range boundary 14 -> 15: none needed (page 14 ends with Figure 8 and its caption after a complete paragraph;
  page 15 starts with a heading).
- No item that follows a `$$` block carries `join_previous`.

## Text repairs of substance

- Pages 13-14: headings wrongly emitted as `# ` set to `###`; running headers/footers that had been extracted as
  text/caption are omitted; six picture regions merged into Figures 7 and 8, two into Figure 5.
- Page 14: split decimals and emphasis markers in the system-identification constants repaired.
- Pages 8-12: glyph-soup and HTML `<sub>/<sup>` inline maths replaced by LaTeX; v1 formula images replaced by LaTeX.
- Page 5: footnote converted to `Footnote 1: ...` with marker `[^1]`.
- Line-wrap hyphens resolved on pages 2, 3, 5, 7, 9, 12, 14 (listed per page above).

## Proposals for shared files (coordinator)

- `plan.json` `title`: currently `urban-swarm-fixed-wing`; propose
  "Agile Fixed-Wing UAVs for Urban Swarm Operations".
- `plan.json` `notes` (suggested strings):
  1. "Basescu, Polevoy, Yeh, Scheuer, Sutton and Moore, Field Robotics, May 2023, vol. 3, pp. 725-765,
     DOI 10.55417/fr.2023023. The journal citation line appears only in the running headers/footers, which are omitted."
  2. "No TeX source was available; all mathematics was transcribed from high-resolution renders of the PDF and
     checked symbol by symbol. Equations (1)-(26) are LaTeX text."
  3. "Authors' typos and inconsistencies are kept as printed, e.g. the first-page dates ('revised: 21 November 2023;
     accepted: 7 March 2023'), the Figure 5 caption colours for the lower plot (legend shows Hermite-Simpson green,
     Euler blue), the 'rad' label on the Figure 2 colour bar whose ticks run 10-80, and the Euler constraint on PDF
     page 12 printed without f."
- Navigation headings in this range (all real printed headings): `## 1. Introduction`; `## 2. Related Work`
  (`### 2.1.`, `### 2.2.` with `#### 2.2.1.`, `#### 2.2.2.`, `### 2.3.`, `### 2.4.`); `## 3. Approach`
  (`### 3.1. Dynamics Model`, `### 3.2. Control Strategy` with `#### 3.2.1.`, `#### 3.2.2.`, `#### 3.2.3.`);
  `## 4. Real-time Trajectory Optimization Performance`; `## 5. Motion Capture Experiments`
  (`### 5.1. Experimental Setup`, `### 5.2. System Identification`; 5.3 onward belongs to pages 15+).
  The abstract and keywords are run-in bold paragraphs on page 1, not headings.
- Adjudication notes exist for pages 3, 6, 7, 8, 9, 10, 11, 12, 14 (only the keys that `check` reports).

## Limitations

- The lower plot of Figure 5 has very small tick labels in the source PDF; they are legible at 220 dpi but may be
  hard to read in a compact JPEG.
- Section 3.2.x headings are printed as bold-italic lines directly above their text; they are emitted as `####`
  headings with printed numbering.
- Figure 3's in-figure formulas (ω, v, r in frame components) are only in the image, not transcribed as text.

## Notes on the brief

- The brief's footnote rule ("own text item at the end of that page's items") conflicts with "the page ends with the
  prose that continues onto the next page" when the footnote's paragraph crosses the page break (page 5). The
  coordinator's later convention (footnote before the last continuing paragraph, marker `[^n]`) resolves it and was
  applied.
- Writing every degree sign as `$90^\circ$` turns otherwise clean prose/caption lines into category (a) diagnostics
  (pages 3, 6, 7); cheap to adjudicate but worth knowing.
- The ink-extent helper (`tight.py`, threshold-based) under-reports photographs with light backgrounds; for
  pages 13-14 the embedded image rectangles from PyMuPDF were used instead.
