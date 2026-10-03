#!/bin/bash
# usage: crop.sh page left top right bottom outname [dpi]   (PDF points, top-left origin)
R=~/AI_agents/paper2agent/Reachability; D=$R/paper-review/dietrich2024nonconvex-paper/documents/s001-dietrich2024nonconvex; S=$R/logs/work/dietrich2024nonconvex
dpi=${7:-240}
x=$(python3 -c "print(round($2*$dpi/72))"); y=$(python3 -c "print(round($3*$dpi/72))")
w=$(python3 -c "print(round(($4-$2)*$dpi/72))"); h=$(python3 -c "print(round(($5-$3)*$dpi/72))")
pdftoppm -r $dpi -f $1 -l $1 -x $x -y $y -W $w -H $h -png $D/source.pdf $S/$6
ls $S/$6*
