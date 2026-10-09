# Brainstorm agent

A research-brainstorm agent for Claude Code that combines methods from the paper agents in
`~/AI_agents/paper2agent` (NMPC, particle filtering, reachability, and any collection added later) to improve or
replace a research idea.

It is built as one orchestrating skill and four subagents:

| Part | File | Job |
|---|---|---|
| `research-brainstorm` (skill) | `skill/research-brainstorm/SKILL.md` | Runs the stages, writes the brief and the report |
| `brainstorm-scout` | `agents/brainstorm-scout.md` | Reads one collection of papers through the brief; mechanism cards, hooks, identities |
| `brainstorm-generator` | `agents/brainstorm-generator.md` | Combines mechanisms into idea cards from a stance (theorist, roboticist, contrarian, analogist) |
| `brainstorm-critic` | `agents/brainstorm-critic.md` | Searches prior work, checks the math, tests ideas against the failure ledger, scores, mutates or drops |
| `brainstorm-developer` | `agents/brainstorm-developer.md` | Writes the proposal for a winning idea and runs its kill test |

The `library/` holds what makes the brainstorm more than free association:

- `operators.md`: named combination moves (ISO, TARGET, PSEUDO, SCHED, REUSE, INSIDE, INVERT, SETS, LIMITS,
  REGIME, BUDGET, CONDITION, DUAL, LOOP, FAIL), each with a test that separates a real combination from glue.
- `rubric.md`: three gates (evidence, falsifiable claim, nearest work) and six scored axes, with venue notes.
- `collections.md`: the paper skills by collection and lens.
- `cards/`: mechanism cards written by scouts, reused by later sessions.

## Stages

0. **Brief.** Project, current idea, the **failure ledger** (sourced facts about what has been tried and what
   happened), the user's steer, assets and constraints.
1. **Scout**, one agent per lens, in parallel.
2. **Diverge**, three or four generators with different stances, in parallel; merged and deduplicated.
3. **Critique**, critics on disjoint groups of ideas, with web search for novelty.
4. **Develop** the top one or two ideas into proposals; run the kill test when it is cheap.
5. **Report** in the session folder, and, when asked, an entry in the project's notes.

Each run lives in `sessions/<date>_<slug>/` with `brief.md`, `cards/`, `ideas/`, `critiques/`, `proposals/`,
`pilots/` and `report.md`.

## Install and use

```bash
~/AI_agents/brainstorm/install.sh     # links the skill and agents into ~/.claude (idempotent)
```

Start a new Claude Code session, then ask, for example:

```text
用 research-brainstorm：结合 NMPC、粒子滤波和可达性论文智能体，改进 ~/overleaf_project/Jixian_TRO_2027 的想法
Brainstorm with my paper agents how to put reachability verification inside the diffusion process of DIAL-MPC.
```

The skill also works before installation: the orchestrator falls back to `general-purpose` agents and passes them
the agent files as instructions.

## Sessions

| Session | Question | Outcome |
|---|---|---|
| `sessions/2026-10-06_tro2027-diffusion-control/` | Improve the diffusion-control + reachability idea of the TRO 2027 project | loop-law annealing; later judged useless by the user after review and audit; see `report.md` |
| `sessions/2026-10-07_tro2027-rerun/` | Rerun after the user rejected loop-law annealing; definitions-first cards | no idea survived; common cause = PREDICT generator fidelity / centre-based sets lose to a smooth density in 12-D; see `report.md` |
