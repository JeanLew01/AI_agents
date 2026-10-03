#!/usr/bin/env bash
# final.sh PAPER [OUTDIR]
#   1. apply metadata; 2. clear adjudications and make a throw-away build to obtain the current diagnostics;
#   3. bind reviewers' adjudication notes to the current fingerprints; 4. build the package for real;
#   5. verify --strict.  Default OUTDIR: dist/nmpc-agent/skill/PAPER
set -u
export PATH="$HOME/.local/bin:$PATH"
SK=/home/jixia/.claude/skills/paper2agent/paper2skill; N=/home/jixia/AI_agents/paper2agent/NMPC; P="$1"
OUT="${2:-$N/dist/nmpc-agent/skill/$P}"
cd $N/paper-review || exit 1
python3 _coord/coord.py meta $P _coord/meta/$P.json || exit 1
DOC=$(ls -d $N/paper-review/$P/documents/*/)
echo '{"schema_version": 1, "entries": []}' > "$DOC/adjudications.json"
TMP=$N/staging/.diag-$P; rm -rf "$TMP"
uv run $SK/scripts/paper_bundle.py build --work $N/paper-review/$P --output "$TMP" --require-reviewed 2>&1 | grep -E 'rror' 
uv run $SK/scripts/paper_bundle.py review-aid --work $N/paper-review/$P 2>&1 | grep queue_items
python3 _coord/coord.py bind $P || { echo "pages with diagnostics but no reviewer note: stop"; exit 3; }
rm -rf "$TMP" "$OUT"; mkdir -p "$(dirname "$OUT")"
uv run $SK/scripts/paper_bundle.py build --work $N/paper-review/$P --output "$OUT" --require-reviewed --dpi 300 2>&1 | grep -E '"status"|"files"|rror'
mkdir -p $N/paper-review/$P/reports
uv run $SK/scripts/paper_bundle.py verify --work $N/paper-review/$P --strict > $N/paper-review/$P/reports/verify-strict-$(basename "$OUT").json 2>&1; rc=$?
status=$(python3 -c "import json;print(json.load(open('$N/paper-review/$P/verification.json'))['status'])")
echo "verify --strict exit=$rc status=$status draft_lines_in_SKILL.md=$(grep -c 'Draft' $OUT/SKILL.md) output=$OUT"
exit $rc
