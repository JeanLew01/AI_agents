# AI_agents

Claude Code agents and skills for research work. Each folder has its own README with details.

| Folder | What it is | Entry point |
|---|---|---|
| [`paper2agent/`](paper2agent/) | Paper skills built with the Paper2Agent workflow, one per paper: [`NMPC/`](paper2agent/NMPC/README.md) (7 sampling-based NMPC papers, plus MCP servers for code), [`ParticleFilter/`](paper2agent/ParticleFilter/README.md) (9 particle-filter papers), [`Reachability/`](paper2agent/Reachability/README.md) (20 sampling-based reachability papers) | Skills linked into `~/.claude/skills/` (e.g. `dial-mpc-paper`); ask Claude about a paper and the skill loads |
| [`brainstorm/`](brainstorm/README.md) | Research-brainstorm agent: scouts read the paper skills, generators combine mechanisms, critics check prior work and soundness, a developer writes the winning proposal | Skill `research-brainstorm` plus four `brainstorm-*` subagents; `brainstorm/install.sh` |
| [`papercheck/`](papercheck/README.md) | **papergate**, a read-only pre-submission checker for LaTeX papers (camera-ready and anonymous-submission modes): build, page limit, fonts, template, margins, author list, anonymity, consistency, math rigor, claims vs evidence, rebuttal promises, figures | `papergate check <paper_dir> --venue papercheck/venues/<venue>.yaml`; subagent `paper-checker`; `papercheck/install.sh` |

## Setup on a new machine

```bash
cd ~/AI_agents
brainstorm/install.sh      # links the brainstorm skill and subagents into ~/.claude
papercheck/install.sh      # creates papercheck/.venv, puts papergate on PATH, links the paper-checker subagent
```

The paper skills are linked into `~/.claude/skills/` as described in each `paper2agent/*/README.md`.
Restart Claude Code after installing so it picks up new agents and skills.

## Conventions

- Virtual environments (`.venv/`), caches and regenerable intermediates are git-ignored (see `.gitignore`).
- Agents that only read are restricted to read-only tools: `paper-checker` can run nothing but
  `papergate check|report|diff`, enforced by a hook. Changes to papers are applied only by the user
  (`papergate apply`, on a new git branch).
- Venue rules in `papercheck/venues/*.yaml` cite their sources. Values that could not be confirmed are
  listed under `todo:` rather than guessed.
