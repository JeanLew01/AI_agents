#!/usr/bin/env bash
# Set up papergate: virtualenv + package, `papergate` on PATH, and the paper-checker subagent in ~/.claude.
# Idempotent. Refuses to replace anything that is not already a symlink into this folder.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ ! -x "$here/.venv/bin/python" ]; then
  uv venv -q --python 3.12 "$here/.venv"
fi
uv pip install -q --python "$here/.venv/bin/python" -e "$here[llm,dev]"

link() {
  local src="$1" dst="$2"
  mkdir -p "$(dirname "$dst")"
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

link "$here/.venv/bin/papergate" "$HOME/.local/bin/papergate"
link "$here/.claude/agents/paper-checker.md" "$HOME/.claude/agents/paper-checker.md"
chmod +x "$here/.claude/hooks/papergate_only.py"
mkdir -p "$here/venues/local"
echo "Restart Claude Code (or start a new session) to pick up the paper-checker agent."
