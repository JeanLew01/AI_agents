#!/bin/bash
# usage: crop.sh page left top right bottom outname [dpi]   (PDF points, top-left origin)
R=~/AI_agents/paper2agent/Reachability; D=$R/paper-review/selim2022safe-paper/documents/s001-selim2022safe; S=$R/logs/work/selim2022safe
dpi=${7:-200}
x=$(python3 -c "print(round($2*$dpi/72))"); y=$(python3 -c "print(round($3*$dpi/72))")
w=$(python3 -c "print(round(($4-$2)*$dpi/72))"); h=$(python3 -c "print(round(($5-$3)*$dpi/72))")
pdftoppm -r $dpi -f $1 -l $1 -x $x -y $y -W $w -H $h -singlefile -png $D/source.pdf $S/$6
