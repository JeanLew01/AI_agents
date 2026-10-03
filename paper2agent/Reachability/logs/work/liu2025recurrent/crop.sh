#!/bin/bash
# usage: crop.sh name page x0 y0 x1 y1 [dpi]   (PDF points, top-left origin)
R=~/AI_agents/paper2agent/Reachability; S=$R/logs/work/liu2025recurrent; D=$R/paper-review/liu2025recurrent-paper/documents/s001-liu2025recurrent
dpi=${7:-240}
read x y w h < <(python3 -c "
import sys
n,p,x0,y0,x1,y1,dpi=sys.argv[1:]
s=float(dpi)/72
print(int(float(x0)*s),int(float(y0)*s),int((float(x1)-float(x0))*s),int((float(y1)-float(y0))*s))
" "$1" "$2" "$3" "$4" "$5" "$6" "$dpi")
pdftoppm -r $dpi -f $2 -l $2 -x $x -y $y -W $w -H $h -singlefile -png $D/source.pdf $S/$1
