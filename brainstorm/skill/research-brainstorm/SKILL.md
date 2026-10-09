---
name: research-brainstorm
description: Runs a structured research brainstorm that combines methods from the user's paper-agent collections (NMPC, particle filtering, reachability, or any paper2agent skills) to improve or replace a research idea. Scouts extract mechanisms from the papers, generators combine them with explicit operators, critics search for prior work and check soundness against the project's failure evidence, and a developer turns the winner into a proposal with a kill test. Use when the user asks to brainstorm, improve a research idea, combine methods from their paper agents, find a better direction for a paper, or 头脑风暴.
---

# Research brainstorm

The orchestrator is the main session. It runs the stages below, spawning the subagents defined in
`~/AI_agents/brainstorm/agents/` (installed as `brainstorm-scout`, `brainstorm-generator`, `brainstorm-critic`,
`brainstorm-developer`). If those agent types are not available in the session (they register at session start),
spawn `general-purpose` agents and pass the full text of the agent file as the first part of the prompt.

Paths below are relative to `~/AI_agents/brainstorm/`.

## Stage 0: intake and brief

1. Read the project: the paper draft, research notes, and any experiment logs or result tables the user points
   to. Find the current idea and the evidence about it. Earlier session transcripts in
   `~/.claude/projects/<project>/` and project memory can hold context the files do not.
2. Create the session folder `sessions/<YYYY-MM-DD>_<slug>/` with subfolders `cards/`, `ideas/`, `critiques/`,
   `proposals/`, `pilots/`.
3. Write `brief.md` from `templates/brief.md`. The **failure ledger** is the most important part: numbered,
   sourced facts about what has been tried and what happened. A brainstorm without it repeats old mistakes.
   Quote the user's steer and how strictly to follow it.
4. Do not ask the user to approve the brief unless the project, the question or the venue is ambiguous.

## Stage 1: scout (parallel)

Pick lenses from `library/collections.md` (by default one per collection; split a collection of more than about
twelve papers into two lenses). Spawn one `brainstorm-scout` per lens, all in one message, with: the brief path,
the skill list, `library_out = library/cards/<lens>.md`, `session_out = sessions/<id>/cards/<lens>.md`, and any
focus questions from the brief. When a library card file exists and is recent, tell the scout to reuse it and add
only hooks.

While scouts run, the orchestrator may search the web for the gaps the brief already reveals (recent work that is
not in the collections). Record findings in `sessions/<id>/cards/web.md` with links.

## Stage 2: diverge (parallel)

Spawn three or four `brainstorm-generator` agents with different stances (`theorist`, `roboticist`,
`contrarian`, `analogist`, or custom), each writing `ideas/<stance>.md` with about six idea cards. Pass the user's
steer as one seed, and tell at least one generator explicitly to ignore the steer.

Then the orchestrator merges: deduplicate (same template = same idea), renumber I1..In in `ideas/all.md`, and add
its own ideas if the generators missed an obvious one. Aim for 12 to 20 distinct ideas.

## Stage 3: critique (parallel)

Split the ideas into disjoint groups of three to five and spawn one `brainstorm-critic` per group, writing
`critiques/<group>.md`. Critics search the web; they are the novelty check.

## Stage 4: converge and develop

1. Rank by verdict, then by Unity and Novelty, then by Regime. Merge ideas the critics said should merge.
2. Select the top one or two. Spawn a `brainstorm-developer` for each, with the critique's mutation and, if the
   kill test is cheap (CPU, under about 30 minutes) and the user has not said otherwise, `run_kill_test: yes`.
   Respect the brief's rules about where code may live.
3. Read the proposals yourself. Check the main proposition's proof sketch; if it is wrong, fix it or downgrade the
   claim.

## Stage 5: report

Write `sessions/<id>/report.md` from `templates/report.md`: the answer first, then ranked ideas, the recommended
direction, the kill-test outcome, next steps, provenance. If the user asked for the result in their project
(e.g. a research-notes entry), write it there in the project's style and notation, after the report exists, and
append only; never rewrite their earlier entries.

Tell the user, briefly: the recommended direction in two or three sentences, the evidence (kill test, nearest
work), what was parked and why, and where the files are.

## Rules

- Paper claims are cited to the skill (`dial-mpc-paper §III-C (eq. 6)`); proposals are marked as proposals.
- The failure ledger is binding on every stage.
- Do not commit to git or push. Do not edit project files other than the agreed notes entry.
- Keep the user's machine in mind: run heavy computations one at a time, and never several GPU jobs in parallel.
