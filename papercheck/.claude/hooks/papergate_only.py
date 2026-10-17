#!/usr/bin/env python3
"""PreToolUse hook for the paper-checker subagent: Bash may only run read-only papergate commands.
Reads the hook JSON on stdin; exits 2 (blocking, reason on stderr) for anything else."""

import json
import re
import shlex
import sys

ALLOWED = {"check", "report", "diff", "list-checks", "version", "--help"}
FORBIDDEN_CHARS = set(";&|`$()<>\n\r\\")


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        print("paper-checker hook: could not parse hook input", file=sys.stderr)
        return 2
    if data.get("tool_name") != "Bash":
        return 0
    cmd = (data.get("tool_input") or {}).get("command", "").strip()
    bad = sorted(c for c in FORBIDDEN_CHARS if c in cmd)
    if bad:
        print(f"paper-checker may not use shell metacharacters ({' '.join(map(repr, bad))}); "
              "run one papergate command with absolute paths.", file=sys.stderr)
        return 2
    try:
        argv = shlex.split(cmd)
    except ValueError as e:
        print(f"paper-checker hook: cannot parse command: {e}", file=sys.stderr)
        return 2
    if len(argv) < 2 or not re.fullmatch(r"(?:.*/)?papergate", argv[0]) or argv[1] not in ALLOWED:
        print("paper-checker may only run `papergate check|report|diff|list-checks|version`. "
              "`papergate apply` and every other command are reserved for the user.", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
