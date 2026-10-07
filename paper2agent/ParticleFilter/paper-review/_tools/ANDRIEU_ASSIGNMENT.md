# Shared assignment notes: Andrieu, Doucet, Holenstein (2010), "Particle Markov chain Monte Carlo methods"

- Journal-typeset PDF, J. R. Statist. Soc. B 72(3), pp. 269-342, 74 PDF pages, single column: the read paper
  (sections 1-6, appendices, references), then "Discussion on the paper by Andrieu, Doucet and Holenstein"
  (many contributions) and "The authors replied later, in writing, as follows", then references in the discussion.
- DOC = /home/jixia/AI_agents/paper2agent/ParticleFilter/paper-review/andrieu-pmcmc-2010-paper/documents/s001-andrieu-pmcmc-2010
- TEX: none. Transcribe mathematics from high-resolution crops. Typical notation to get exactly right:
  x_{1:T}, X_{1:n}^k, ancestor indices A_n^k and B_n^k, weights W_n^k and w_n(\cdot), \hat p_\theta(y_{1:T}),
  \gamma_n, Z_n, \tilde\pi^N, bold vectors (\mathbf{X}_n, \mathbf{A}_n), sub/superscripts such as
  x_{1:n-1}^{a_{n-1}^k}, script letters, and the difference between \theta, \vartheta, \theta^*.
- Eight reviewers own PDF pages 1-9, 10-18, 19-27, 28-36, 37-46, 47-56, 57-65, 66-74. Adjacent pages are read-only.
- Conventions (all reviewers):
  - Headings: `## 1. Introduction` for numbered sections, `### 2.1. ...` subsections, `#### 2.2.1. ...` below;
    `## Acknowledgements`, `## Appendix A: ...`, `## References`, `## Discussion on the paper by Andrieu, Doucet and Holenstein`,
    `## References in the discussion`. In the discussion each contribution starts with a heading
    `### <Name as printed> (<affiliation as printed>)`; the authors' reply is `### The authors replied later, in writing, as follows`.
    Bold run-in step labels and italic run-in titles stay text.
  - The printed algorithm descriptions (e.g. "Step 1: ...", "(a) ...", SMC algorithm, PIMH, PMMH, particle Gibbs,
    conditional SMC) are text in this paper: keep them as text items, one item per step, with the printed
    step labels, verbatim; no image needed unless the layout cannot be expressed as text.
  - Theorem-like blocks: bold printed labels (`**Theorem 1.**`, `**Assumption 1.**`, `**Proposition 1.**`,
    `**Lemma 1.**`, `**Proof.**`, `**Remark 1.**`, `**Definition 1.**`).
  - Printed equation numbers as \tag, one $$ block per printed number; displays are separate blocks, no join
    onto a display; write := for \coloneqq; inside mathematics write "]{}(" instead of "](".
  - Asset names: figure-N with the printed number for the main paper ("Fig. 3" -> figure-3). Figures inside the
    discussion restart or continue numbering: use the printed number with a `d-` discriminator and the page,
    e.g. figure-d9-p0052, so names never clash. Tables likewise (table-1; table-d1-p0060).
    Table cells plain text/Unicode, no LaTeX backslashes.
  - Running headers/footers and page numbers: omit. The first-page footer (address for correspondence, copyright
    line, journal line) is kept as text.
  - Each page must end with the paragraph that continues onto the next page; if your first page starts
    mid-paragraph set join_previous on its first item (look at the previous page's last line).
  - No footnotes between a paragraph and an item joined to it.
