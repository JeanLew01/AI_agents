#!/bin/bash
# usage: crop.sh PAGE NAME X0 Y0 X1 Y1 [DPI]   (PDF points, top-left origin) -> NAME.png in this folder
S=$(dirname "$0"); PDF=~/AI_agents/paper2agent/Reachability/paper-review/hashemi2025pca-paper/documents/s001-hashemi2025pca/source.pdf
P=$1; N=$2; DPI=${7:-300}
python3 - "$@" <<PY > /tmp/claude-1000/-home-jixia/8e7eed2b-fc6c-484a-99f6-9a94591f3a7a/scratchpad/crop_args.txt
import sys
p,n,x0,y0,x1,y1=sys.argv[1:7]; dpi=int(sys.argv[7]) if len(sys.argv)>7 else 300
s=dpi/72
print(int(float(x0)*s),int(float(y0)*s),int((float(x1)-float(x0))*s),int((float(y1)-float(y0))*s))
PY
read X Y W H < /tmp/claude-1000/-home-jixia/8e7eed2b-fc6c-484a-99f6-9a94591f3a7a/scratchpad/crop_args.txt
pdftoppm -r $DPI -f $P -l $P -x $X -y $Y -W $W -H $H -singlefile -png "$PDF" "$S/$N"
echo "$S/$N.png ${W}x${H}"
