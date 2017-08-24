#!/bin/bash
for n in ttDM_Mchi1Mphi10 topDM_Mchi1Mphi10_tChan_4F topDM_Mchi1Mphi10_sChan_4F topDM_Mchi1Mphi10_tWChan_5F
do
echo $n
root -l <<EOF
.L Hadronic.C+
Hadronic t("$n");
t.Loop();
.q
EOF
done



