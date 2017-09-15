#!/bin/bash
for n in ttDM_Mchi1Mphi10_Hadronic.root
do
echo "
Cut_Flow"
python Cut_Flow.py $n
echo "
NJet_Plot"
python NJet_Plot.py $n
echo "
Met Flow"
python Met_Flow.py $n
done


