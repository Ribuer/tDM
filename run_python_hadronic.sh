#!/bin/bash
for n in ttDM_Mchi1Mphi10_Hadronic.root
do
echo "
2D_Plots"
python 2D_Plots.py $n
echo "
Cut_Flow"
python Cut_Flow.py $n
echo "
Stack_Plots"
python Stack_Plots.py $n
echo "
Met Flow"
python Met_Flow.py $n
done


