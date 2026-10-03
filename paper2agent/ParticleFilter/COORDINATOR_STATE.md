# ParticleFilter Paper2Agent conversion: coordinator state

## Goal
User request (2026-10-02/03): turn two particle-filter papers into agents with Paper2Agent
(skill at ~/.claude/skills/paper2agent), in a new subfolder of ~/AI_agents/paper2agent. Same conventions as the
sibling collections NMPC/ and Reachability/.

## Inputs
| id | paper | PDF | TeX | code |
| --- | --- | --- | --- | --- |
| diffpf-paper | DiffPF (Wan & Zhao, IEEE RA-L, accepted Jan 2026) | papers/diffpf.pdf = user's 12_DiffPF_2025.pdf (arXiv:2507.15716v2, 8 pp.) | tex-source/diffpf | ZiyuNUS/DiffPF @493081c |
| diffusion-resampling-paper | Diffusion differentiable resampling (Andersson & Zhao, ICML 2026) | papers/diffusion-resampling.pdf = user's 13_DiffusionDiffResampling_ICML2026.pdf (arXiv:2512.10401v3, 32 pp.) | tex-source/diffusion-resampling | zgbkdlm/diffres @767effe |

User's originals: C:\Users\jixia\OneDrive\Desktop\pf_papers\.

## Decisions
- Paper skills for both papers (paper2skill, maths as LaTeX from the authors' TeX, checked against the PDF).
- MCP (paper2mcp) for diffres only. Route python, CPU-only JAX through mcp-build/heavy.sh (lock shared with NMPC).
- DiffPF MCP excluded: the repository holds only raw training code for the global-localization experiment
  (README "Status"), no trained checkpoints, needs the external tu-rbo DPF dataset plus preprocessing, and the
  paper's setting trains 1000 epochs on a GPU; test scripts load checkpoints/particles that are not shipped.
  No runnable reference result is obtainable on this machine (7.5 GB RAM WSL, 8 GB laptop GPU, GPU JAX/torch jobs
  froze WSL twice on 2026-10-02 in the NMPC workspace). Source kept for inspection in mcp-build/DiffPF-source-inspection.

## Layout
papers/, tex-source/, paper-review/<id>/ (+ _tools briefs, _coord scripts, _scratch), staging/,
dist/particle-filter-agent/{skill,mcp}/, mcp-build/diffres/ (Paper2MCP project), logs/.

## Status log
- 2026-10-03T00:20Z reviewers launched: diffpf 1-8; diffres 1-7, 8-15, 16-23, 24-32 (brief paper-review/_tools/REVIEWER_BRIEF.md).
- 2026-10-03T00:33Z diffres MCP stage 1: environment manager + scanner launched concurrently.
- 2026-10-03T00:45Z all 40 pages reviewed. diffpf-paper: independent verifier 0 errors / 0 minors; DELIVERED to dist/particle-filter-agent/skill/diffpf-paper (strict verify exit 0, reviewed_with_limitations), symlinked into ~/.claude/skills.
- diffusion-resampling-paper: staging s1 strict OK (reading_order moves Tables 8-10 to end of I, Table 12 to end of J, Figs 8-11 to end of K); three verifiers running (pages 1-9, 10-20, 21-32).
- diffres MCP: setup gate passed (env py3.11, jax 0.7.2 CPU; test_filters 10/10, test_integrators 1/1; test_resampling excluded for memory: needs >= 3 GB). Selected 5 tools in 3 modules (resampling, feynman_kac, gaussian_filters). 2026-10-03T00:48Z eight executors launched (ids in mcp-build/diffres/reports/coordinator-executor-launch.json; brief EXECUTOR_BRIEF.md).
- 2026-10-03T01:00Z diffusion-resampling-paper DELIVERED to dist/particle-filter-agent/skill/ (strict verify exit 0, reviewed_with_limitations), symlinked into ~/.claude/skills. Verifier findings (pp 1-9: 1 error footnote-1 paragraph attached to footnote -> fixed via reading_order; pp 21-32: 1 error doubled backslashes in markdown tables -> LaTeX table cells rewritten as Unicode; minors: caption italics unified, index gained Acknowledgements/Impact statement, Luo ref italics, Table 4 unique CSV headers, conversion note on display continuations corrected). PDF-internal inconsistency kept: OT eps=1.6 loss error 2.75 (Table 2) vs 2.76 (Table 10).
- 2026-10-03T01:10Z diffres MCP: all 8 executors succeeded (bitwise replays); execution gate passed; reference_execution_done. Three implementers launched (resampling a527da757c84546c9, feynman_kac a02ba027b8a0a5273, gaussian_filters acf50d2e1c6204f2e; brief IMPLEMENTER_BRIEF.md). Known upstream property: PF nll offset -log(N) (documented, not corrected).
- 01:20Z extraction gate passed; three fresh verifiers launched (resampling af33ae7084e817472, feynman_kac a302589cd0a90678a, gaussian_filters a06135259c3f3f223; brief VERIFIER_BRIEF.md).
- 2026-10-03T01:47:49Z WSL stopped abruptly (journal ends; reboot 01:54Z) as the feynman_kac verifier started an MCP acceptance dry run under heavy.sh (1200 MB scope). Cause unknown. heavy.sh tightened (avail >= limit+2500, limit <= 1500), one heavy agent at a time. 01:58Z feynman_kac verifier resumed alone; resampling verifier (stopped, tests written, production file repaired to 29667bd6...) to resume after it.
- 02:04Z verification gate passed (resampling 99/99, feynman_kac 66/66, gaussian_filters 58/58 tests). Integration: src/diffres_mcp.py, 5 tools; project-env stdio acceptance 47/47 (peak 1214 MB); artifact contents match executor references (bitwise; notebook diffusion 1.8e-13). mcp_integration_done.
- 02:15Z runtime validation (clean env 47/47) and delivery (extracted ZIP in path with space, 47/47 + changed-input bitwise checks, independent delivery verifier) passed; workflow gate 'complete' passed; delivery_done. ZIP staged at dist/particle-filter-agent/mcp/ (files identical). ALL DONE.
