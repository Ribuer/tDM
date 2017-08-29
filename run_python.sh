#!/bin/bash
for n in ttDM_Mchi1Mphi10.root
do
python 2D_Plots.py $n
python Cut_Flow.py $n
python Stack_Plots.py $n
done


