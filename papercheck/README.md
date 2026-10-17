# papergate

A read-only checker for LaTeX papers before submission. It is built mainly for camera-ready versions and
also has an anonymous-submission mode. It compiles a temporary copy of the paper, runs about 70 checks,
and writes a findings ledger (`findings.json`) with Markdown and HTML reports. Fixes are only proposed, as
unified diffs. You apply them yourself with `papergate apply`, which works on a new git branch.

## The read-only guarantee

- `papergate check` never writes to the paper directory. Before and after the run it hashes every path
  there (hidden files and `.git` included). If anything changed, appeared or disappeared, the run ends with
  verdict `ERROR` and exit code 3, and the report lists the changes.
- The build runs in a temporary copy (`latexmk -outdir` inside that copy). TeX may only write inside it
  (`openout_any=p`), and shell escape stays restricted unless the venue config allows it.
- `check` never runs `git` in the paper directory, because even `git status` can rewrite `.git/index`.
- The report directory must be outside the paper directory. By default it is
  `~/.cache/papergate/reports/<paper>/<timestamp>-<mode>`, with a `latest` symlink next to it.
- papergate never regenerates figures, never re-runs experiments, and never decides which of two
  conflicting numbers is right.

## Install

```bash
cd ~/AI_agents/papercheck && ./install.sh
```

`install.sh` does three things:
- creates `.venv` with Python 3.12 and installs the package with the `llm` and `dev` extras;
- links `papergate` into `~/.local/bin`;
- links the `paper-checker` subagent into `~/.claude/agents`.

**Needed on the system:** `latexmk` and pdfLaTeX/LuaLaTeX, BibTeX/Biber, and poppler (`pdffonts`). `git`
is needed only for `apply`. `chktex` is optional (`sudo apt install chktex`); without it, its check is
reported as skipped.

**Network use:** none during `check`, except the LLM stages (the Anthropic API) and `--online` (arXiv and
DBLP lookups for published versions of arXiv entries). `--no-llm` runs fully offline.

## Usage

```bash
papergate check <paper_dir> --venue venues/corl2026.yaml --mode camera-ready [--main paper.tex] \
    [--rebuttal rebuttal.md] [--no-llm] [--only build,pdf.fonts] [--out <report_dir>] \
    [--supp supplementary.zip] [--online] [--model claude-opus-5-5] [--keep-build]
papergate report <report_dir>                      # re-render report.md / report.html from findings.json
papergate diff <old_report_dir> <new_report_dir>   # resolved / new / persisting findings
papergate apply <paper_dir> <report_dir> --findings F3,F7 [--branch name] [--no-commit] [--no-recheck]
papergate list-checks [--markdown]
papergate measure-template <official_template_dir> --main root.tex   # template.layout for a venue config
```

**Exit codes:** 0 pass; 1 BLOCKERs found; 2 usage or config error; 3 read-only violation.

**`--only`** takes check ids or prefixes (`identity`, `pdf.fonts`, `math.rigor`).

**How `apply` works:**
- It refuses when the paper directory has uncommitted or untracked changes, when a named finding has no
  patch, or when a patch no longer applies to HEAD. Every patch is checked before anything is touched.
- It then creates `papergate/fix-<timestamp>` from HEAD, applies only the named patches, and commits them
  there. Your current branch is never modified.
- Finally it re-runs the check (with LLM stages off) into `<report_dir>-after-apply` and prints the diff.
- Review the change with `git diff <your-branch>..papergate/fix-…`.

**How `diff` matches findings:** by fingerprint, a hash of check id, file and normalised quote. Line
numbers are left out on purpose, so a finding keeps its identity when edits above it shift its line.

## Venue configs

Venue files live in `venues/`. No venue logic is hard-coded.

| Field | Meaning |
|---|---|
| `template` | `file` (official .sty/.cls), `sha256`, optional `official_path` (diffed against), `layout` (text block in pt; get it with `measure-template`) |
| `page_limit` | `submission`, `camera_ready`, `excluded_sections` (references, acknowledgments, appendix, limitations, …; `[]` means every page counts), optional `heading_patterns` |
| `review_mode_markers` / `final_mode_markers` | `package_option`, `class_option`, `source_regex`, `pdf_text`, `line_numbers` |
| `required_sections` / `forbidden_sections` | per mode: `{name, pattern, min_words}` |
| `fonts`, `max_file_size_mb`, `pdf_version`, `abstract_max_words` | PDF compliance |
| `title`, `authors` | canonical title and ordered author list (camera-ready: compared with page 1 and the PDF metadata) |
| `identity_terms` | names, institutions, labs, emails, GitHub users, domains, grant numbers (submission: must not appear) |
| `compliance_notes` | manual checklist items, per mode |
| `checks.<id>` | per-check options, e.g. `checks.build.overfull_threshold_pt`, `checks.figures.text_size.min_ratio` |
| `severity_overrides`, `disabled_checks` | by check id or prefix |
| `llm` | `model` (default `claude-opus-5-5`), `effort`, `max_tokens`, `max_severity` (LLM findings are capped at it), `max_context_chars` |
| `todo` | values not yet confirmed against the call for papers. They are shown in the report, so do not guess them |

**Paper-specific settings** (authors, identity terms) go in a small file that `extends:` a venue config.
Keep these files in `venues/local/`, which git ignores:

```yaml
extends: /home/jixia/AI_agents/papercheck/venues/corl2026.yaml
title: <exact paper title>
authors:
  - {name: Ada Lovelace, affiliations: [Analytical Engine Lab], email: ada@example.edu}
  - {name: Alan Turing, affiliations: [Computable Numbers Inst.], email: alan@example.org}
identity_terms: [Ada Lovelace, Alan Turing, Analytical Engine Lab, ada@example.edu, adalovelace, GRANT-12345]
```

**Shipped configs:**
- `corl2026.yaml`: from the official CoRL 2026 pages, with the measured `corl_2026.sty` layout and hash.
- `icra2027.yaml`: from the ICRA 2027 call. Final-version values are ICRA 2026's until the 2027 rules are
  published. The `ieeeconf.cls` hash and layout are TODO; fill them with `measure-template`.

## Pipeline and checks

Each check is a small class decorated with `@register`, declaring `id`, `stage`, `applies_to_modes`,
`requires` (`build`, `pdf`, `llm`, `rebuttal`, `online`) and `run(ctx) -> list[Finding]`. To add a check,
add a module to `src/papergate/checks/` (or expose it through the `papergate.checks` entry-point group);
the pipeline core does not change. A check that raises an exception becomes one INFO finding, not a failed
run. A check whose requirements are missing is listed as skipped, with the reason.

The stages are:
- **0, project:** config and includes.
- **1, build:** clean latexmk build, log, BibTeX/Biber, chktex.
- **2, PDF compliance:** page count, fonts, template integrity, margin ink, size, version, links.
- **3, identity:** final/review markers, authors, metadata, acknowledgments, anonymisation leftovers and
  editing artifacts; in submission mode, identity terms in the source, PDF, metadata, figures and
  supplementary archives.
- **4, consistency:** references, bibliography, acronyms, abstract and intro numbers against table cells,
  notation, theorem restatements.
- **5, math rigor:** proofs exist; LLM check per theorem.
- **6, claims and rebuttal:** strong words, limitations, LLM claim-evidence mapping, rebuttal commitments.
- **7, figures:** captions, text size relative to the body text, colour-blind and grayscale safety.

| Check | Stage | Default severity | Modes | Needs | Source |
|---|---|---|---|---|---|
| `config.unconfirmed` | 0 | INFO | both | - | deterministic |
| `project.includes` | 0 | BLOCKER | both | - | deterministic |
| `build.bibtex` | 1 | WARN | both | build | deterministic |
| `build.chktex` | 1 | INFO | both | build | deterministic |
| `build.errors` | 1 | BLOCKER | both | build | deterministic |
| `build.labels_changed` | 1 | WARN | both | build | deterministic |
| `build.multiply_defined_label` | 1 | WARN | both | build | deterministic |
| `build.overfull_hbox` | 1 | WARN | both | build | deterministic |
| `build.undefined_citation` | 1 | BLOCKER | both | build | deterministic |
| `build.undefined_ref` | 1 | BLOCKER | both | build | deterministic |
| `pdf.file_size` | 2 | BLOCKER | both | pdf | deterministic |
| `pdf.fonts.embedded` | 2 | BLOCKER | both | pdf | deterministic |
| `pdf.fonts.type3` | 2 | BLOCKER | both | pdf | deterministic |
| `pdf.links` | 2 | WARN | both | pdf | deterministic |
| `pdf.margins` | 2 | WARN | both | pdf | deterministic |
| `pdf.page_limit` | 2 | BLOCKER | both | pdf | deterministic |
| `pdf.version` | 2 | WARN | both | pdf | deterministic |
| `template.caption_format` | 2 | WARN | both | - | deterministic |
| `template.file` | 2 | BLOCKER | both | - | deterministic |
| `template.fontsize` | 2 | WARN | both | - | deterministic |
| `template.geometry` | 2 | BLOCKER | both | - | deterministic |
| `template.layout` | 2 | BLOCKER | both | build | deterministic |
| `template.layout_length` | 2 | BLOCKER | both | - | deterministic |
| `template.linespread` | 2 | BLOCKER | both | - | deterministic |
| `template.negative_vspace` | 2 | WARN | both | - | deterministic |
| `template.spacing` | 2 | WARN | both | - | deterministic |
| `artifacts.changes` | 3 | WARN | both | - | deterministic |
| `artifacts.color` | 3 | WARN | both | - | deterministic |
| `artifacts.commented_blocks` | 3 | WARN | both | - | deterministic |
| `artifacts.highlight` | 3 | WARN | both | - | deterministic |
| `artifacts.markers` | 3 | WARN | both | - | deterministic |
| `artifacts.packages` | 3 | INFO | camera-ready | - | deterministic |
| `artifacts.todo` | 3 | WARN | both | - | deterministic |
| `identity.acknowledgments` | 3 | WARN | both | - | deterministic |
| `identity.anonymized_links` | 3 | BLOCKER | camera-ready | - | deterministic |
| `identity.anonymous_selfcite` | 3 | BLOCKER | camera-ready | - | deterministic |
| `identity.author_list` | 3 | BLOCKER | camera-ready | pdf | deterministic |
| `identity.final_markers` | 3 | BLOCKER | both | pdf | deterministic |
| `identity.pdf_metadata` | 3 | WARN | camera-ready | pdf | deterministic |
| `identity.placeholder_authors` | 3 | BLOCKER | camera-ready | - | deterministic |
| `identity.review_markers` | 3 | BLOCKER | both | pdf | deterministic |
| `identity.self_citation_llm` | 3 | WARN | submission | llm | llm |
| `identity.self_citation_phrasing` | 3 | WARN | submission | - | deterministic |
| `identity.supplementary` | 3 | BLOCKER | submission | - | deterministic |
| `identity.terms_figures` | 3 | BLOCKER | submission | - | deterministic |
| `identity.terms_pdf` | 3 | BLOCKER | submission | pdf | deterministic |
| `identity.terms_source` | 3 | WARN | submission | - | deterministic |
| `structure.abstract_length` | 3 | WARN | both | - | deterministic |
| `structure.forbidden_sections` | 3 | BLOCKER | both | pdf | deterministic |
| `structure.required_sections` | 3 | BLOCKER | both | - | deterministic |
| `bib.arxiv_published` | 4 | INFO | both | - | deterministic |
| `bib.duplicates` | 4 | WARN | both | - | deterministic |
| `bib.unused_entries` | 4 | INFO | both | - | deterministic |
| `bib.venue_format` | 4 | WARN | both | - | deterministic |
| `consistency.numbers` | 4 | WARN | both | - | deterministic |
| `consistency.unreferenced_floats` | 4 | WARN | both | - | deterministic |
| `consistency.unreferenced_labels` | 4 | INFO | both | - | deterministic |
| `math.notation` | 4 | WARN | both | - | deterministic |
| `math.restatements` | 4 | WARN | both | - | deterministic |
| `text.acronyms` | 4 | WARN | both | - | deterministic |
| `math.assumptions_unreferenced` | 5 | WARN | both | - | deterministic |
| `math.proof_presence` | 5 | WARN | both | - | deterministic |
| `math.rigor` | 5 | WARN | both | llm | llm |
| `claims.limitations` | 6 | WARN | both | - | deterministic |
| `claims.strong_words` | 6 | INFO | both | - | deterministic |
| `claims.support` | 6 | WARN | both | llm | llm |
| `rebuttal.commitments` | 6 | WARN | both | rebuttal | deterministic |
| `rebuttal.commitments_llm` | 6 | WARN | both | llm, rebuttal | llm |
| `figures.captions` | 7 | WARN | both | - | deterministic |
| `figures.colors` | 7 | WARN | both | - | deterministic |
| `figures.text_size` | 7 | WARN | both | pdf | deterministic |

### LLM-assisted checks

LLM checks go through `LLMBackend` (`src/papergate/llm/base.py`). Three backends exist:
- `NullBackend`: no model; the LLM stages are skipped.
- `AnthropicBackend`: model configurable, default `claude-opus-5-5` at effort `high`, with JSON-schema
  structured output. The API's server-side refusal fallback is on by default.
- `MockBackend`: canned answers, used by the tests.

**Credentials:** `ANTHROPIC_API_KEY` or an `ant auth login` profile. Without them the LLM stages are
skipped, and the report says so.

**Anti-hallucination rules:**
- Every LLM finding must quote the source exactly; whitespace differences are ignored. papergate looks the
  quote up in the paper (or the rebuttal) and moves the finding to the line where it actually occurs.
- If the quote is not found anywhere, the finding is dropped and counted under "Discarded unverifiable LLM
  findings" in the report.
- Answers are validated against a JSON schema. A malformed answer is retried once, then dropped and counted.
- LLM findings never carry patches; their fix is always manual. Their severity is capped at
  `llm.max_severity` (WARN by default).
- The math check sends one theorem at a time, with only its statement, its proof, and the
  definitions/assumptions/lemmas they reference.

## Tests

```bash
env -u PYTHONPATH .venv/bin/python -m pytest -q
```

`env -u PYTHONPATH` keeps ROS's pytest plugins from loading.

`tests/fixtures/` holds small synthetic papers on a bundled test template (`pgtest.sty`):
- one `clean` paper, which must produce no BLOCKERs and no stage 1–4 or 7 findings;
- one fixture per seeded defect: over page limit, Type 3 font figure, leftover "Anonymous", author order,
  undefined reference, abstract/table number mismatch, unused assumption, unfulfilled rebuttal promise,
  submission-mode identity leak, editing artifacts, consistency problems, template hacks, figures.

The fixtures are generated from `_base` by `tests/fixtures/_tools/make_fixtures.py`; the figures come from
`make_figures.py`.

**Tests also check that:**
- every fixture directory is byte-identical after a check;
- a check that writes into the paper makes the run fail;
- `apply` works on a temporary git repository;
- the LLM stages behave correctly with a mocked backend, including a hallucinated quote being discarded.

## Claude Code integration

`.claude/agents/paper-checker.md` is a read-only subagent:
- **Tools:** Read, Grep, Glob and Bash; Write, Edit and NotebookEdit are disallowed.
- **Bash restriction:** a PreToolUse hook (`.claude/hooks/papergate_only.py`) allows only
  `papergate check|report|diff|list-checks|version`, one command at a time, with no shell metacharacters.
- **What it does:** runs the checker, reports BLOCKERs first, and never edits files.

Applying fixes stays a manual `papergate apply` that you run yourself.

## Known gaps

- chktex is not installed on this machine (no sudo), so `build.chktex` is skipped.
- Margin and layout checks need `template.layout` in the venue config; ICRA's is still TODO.
- Number, acronym and notation checks are heuristics. They report at WARN/INFO, never BLOCKER.
- Figure text size is measured only for vector PDF figures whose `\includegraphics` width can be parsed.
  Raster figures are listed as not measured.
