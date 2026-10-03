#!/usr/bin/env bash
# Coordinator check for one finished paper: re-run strict verification, then link the skill globally.
export PATH="$HOME/.local/bin:$PATH"
SK=$HOME/.claude/skills/paper2agent/paper2skill; R=$HOME/AI_agents/paper2agent/Reachability
for k in "$@"; do
  F=$R/skills/$k-paper; W=$R/paper-review/$k-paper
  [ -f $F/SKILL.md ] || { echo "$k: NO PACKAGE"; continue; }
  out=$(uv run $SK/scripts/paper_bundle.py verify --work $W --strict 2>&1); rc=$?
  st=$(python3 -c "import json;v=json.load(open('$W/verification.json'));print(v.get('status'))" 2>/dev/null)
  n=$(wc -l < $F/references/paper.md); a=$(find $F/assets -type f 2>/dev/null | wc -l)
  bad=$(grep -c -E "<sup>|�| ˆ|\*\* \*\*" $F/references/paper.md)
  dollars=$(python3 -c "print(open('$F/references/paper.md').read().count('\$')%2)")
  echo "$k: strict_exit=$rc status=$st paper.md=${n} lines assets=$a damage_hits=$bad odd_dollar=$dollars report=$([ -f $R/logs/reports/$k.md ] && echo yes || echo NO)"
  if [ $rc -eq 0 ]; then ln -sfn $F $HOME/.claude/skills/$k-paper; fi
done
