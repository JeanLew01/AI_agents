#!/bin/bash
# usage: crop.sh PAGE X0 Y0 X1 Y1 DPI OUTNAME   (coords in PDF points, top-left origin)
D=~/AI_agents/paper2agent/Reachability/paper-review/liebenwein2018sampling-paper/documents/s001-liebenwein2018sampling
S=~/AI_agents/paper2agent/Reachability/logs/work/liebenwein2018sampling
p=$1; x0=$2; y0=$3; x1=$4; y1=$5; dpi=$6; out=$7
X=$(python3 -c "print(int($x0*$dpi/72))"); Y=$(python3 -c "print(int($y0*$dpi/72))")
Wd=$(python3 -c "print(int(($x1-$x0)*$dpi/72))"); H=$(python3 -c "print(int(($y1-$y0)*$dpi/72))")
pdftoppm -r $dpi -f $p -l $p -x $X -y $Y -W $Wd -H $H -png -singlefile $D/source.pdf $S/$out
