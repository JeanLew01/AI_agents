#!/usr/bin/env bash
# Link the brainstorm skill and agents into ~/.claude so every Claude Code session can use them.
# Idempotent. Refuses to replace anything that is not already a symlink into this folder.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
mkdir -p "$HOME/.claude/skills" "$HOME/.claude/agents"

link() {
  local src="$1" dst="$2"
  if [ -L "$dst" ]; then
    ln -sfn "$src" "$dst"
  elif [ -e "$dst" ]; then
    echo "skip: $dst exists and is not a symlink" >&2
    return
  else
    ln -s "$src" "$dst"
  fi
  echo "linked: $dst -> $src"
}

link "$here/skill/research-brainstorm" "$HOME/.claude/skills/research-brainstorm"
for f in "$here"/agents/*.md; do
  link "$f" "$HOME/.claude/agents/$(basename "$f")"
done
echo "Restart Claude Code (or start a new session) to pick up the new agent types."
