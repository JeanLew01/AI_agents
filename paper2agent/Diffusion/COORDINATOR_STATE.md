# Diffusion Paper2Agent conversion: coordinator state

## Goal
User request (2026-10-14): build a Paper2Agent for "Large Language Diffusion Models" (LLaDA, Nie et al.,
arXiv:2502.09992v3, NeurIPS 2025) in ~/AI_agents/paper2agent/Diffusion. Same conventions as the sibling
collections Reachability/, NMPC/, ParticleFilter/ (briefs and coordinator scripts copied from ParticleFilter).

## Inputs
| id | paper | PDF | TeX | code |
| --- | --- | --- | --- | --- |
| llada-paper | LLaDA (NeurIPS 2025) | papers/llada.pdf = user's C:\Users\jixia\Downloads\2502.09992v3.pdf (33 pp., sha256 18942f14...) | tex-source/llada (arXiv src v3) | github.com/ML-GSAI/LLaDA |

## Layout
papers/, tex-source/, paper-review/llada-paper (+ _tools briefs incl. LLADA_ASSIGNMENT.md, _coord scripts, _scratch),
staging/, dist/diffusion-agent/{skill,mcp}/, mcp-build/, logs/.

## Status log
- 2026-10-14T13:33Z prepared + extracted (33 pages, 36 queue items). Reviewers: r1 pp.1-9, r2 pp.10-22, r3 pp.23-33.

## MCP assessment (2026-10-14)
Repository cloned for inspection: mcp-build/LLaDA-source-inspection @ 9182493 (2026-07-15). Callable implementations:
generate.py `generate()` (low-confidence / random remasking, semi-AR blocks, CFG, Gumbel temperature),
get_log_likelihood.py `get_log_likelihood()` (Monte Carlo conditional likelihood, Eq. (6)/Algorithm 3),
chat.py, app.py, eval_*.py (lm-eval / OpenCompass harnesses). Every tool needs the HF checkpoint
GSAI-ML/LLaDA-8B-{Base,Instruct} (MIT licence per README; ~16 GB bf16). This machine: RTX 4070 Laptop 8 GB VRAM
(about 2.4 GB held by the Windows display), WSL 11 GB RAM. bf16 does not fit; CPU/disk offload is impractical.
Only a 4-bit (bitsandbytes NF4, ~5 GB VRAM) load could run, after a 16 GB download, with numerics that differ
from the paper's bf16. NMPC/mcp-build/HEAVY_JOBS_DISABLED is still present. Decision: MCP not started; the user
decides (quantized local run, a bigger GPU, or skill only).
- 2026-10-14T13:45Z r1 (1-9) and r2 (10-22) finished; r3 running.
- 2026-10-14T13:49Z all 33 pages [v2]; reading-order moves + meta applied (_coord/spec/llada-paper.json); staging build verify --strict exit 0 (reviewed_with_limitations, 47 adjudications). Fresh verifiers v1 (pp.1-18), v2 (pp.19-33) launched.
- 2026-10-14 verifiers: v1 (pp.1-18) 0 errors / 5 minors (all notes/index); v2 (pp.19-33) 1 error (Table 16: two "Daily life" cases read as one) / 6 minors. Repairs: case labels numbered in Tables 15-16, printed line breaks in Table 15 movie answer, iGSM solution + B.9 lines as paragraphs, algorithm comments plain text, Tables 3/13/14 made image-only tables (assets/table/), notes corrected (algorithm/Table 13 print positions, external URLs marked, |EOS| forms, bold in all tables), Related Work index row. Adjudication notes added for pp. 31-32 (case numbers). Rechecked by coordinator.
- 2026-10-14 converter's observation added to notes: Algorithm 5 literal remask count n_un vs intended L - n_un.
- 2026-10-14 FINAL: dist/diffusion-agent/skill/llada-paper, verify --strict exit 0 (reviewed_with_limitations, 49 adjudications), symlinked ~/.claude/skills/llada-paper. MCP not started (see assessment); README.md written.
- 2026-10-14 user decision: stop with the paper skill only; no MCP server. Collection complete.
