#!/bin/bash
# usage: crop.sh PAGE X0 Y0 X1 Y1 DPI NAME   (points, top-left origin)
PDF=~/AI_agents/paper2agent/Reachability/paper-review/lew2021sampling-paper/documents/s001-lew2021sampling/source.pdf
S=~/AI_agents/paper2agent/Reachability/logs/work/lew2021sampling
p=$1; x0=$2; y0=$3; x1=$4; y1=$5; dpi=$6; name=$7
px() { python3 -c "print(int(round($1*$dpi/72)))"; }
pdftoppm -r $dpi -f $p -l $p -x $(px $x0) -y $(px $y0) -W $(px "($x1-$x0)") -H $(px "($y1-$y0)") -png -singlefile $PDF $S/$name
