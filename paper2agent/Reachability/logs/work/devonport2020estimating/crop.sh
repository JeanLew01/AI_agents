#!/bin/bash
# usage: crop.sh name page x0 y0 x1 y1 dpi   (coordinates in PDF points, top-left origin)
R=~/AI_agents/paper2agent/Reachability; S=$R/logs/work/devonport2020estimating; D=$R/paper-review/devonport2020estimating-paper/documents/s001-devonport2020estimating
read x y w h < <(python3 -c "
import sys
n,p,x0,y0,x1,y1,dpi=sys.argv[1:]
s=float(dpi)/72
print(int(float(x0)*s),int(float(y0)*s),int((float(x1)-float(x0))*s),int((float(y1)-float(y0))*s))
" "$@")
pdftoppm -r $7 -f $2 -l $2 -x $x -y $y -W $w -H $h -png $D/source.pdf $S/$1
