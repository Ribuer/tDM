from ROOT import *
import sys
import string
import math as mt
from array import array

color_list = [1, 633, 434, 402, 877, 419, 396, 628, 618, 882, 428, 612, 414, 596]

c1 = TCanvas("canvas1", "Test", 800, 600)

hist_list = [0, 0, 0, 0]
file_list = [0, 0, 0, 0]
scale_list = [19.76, 7.03e-2, 27.18e-1, 73.25e-2] #tt, single tops: s,t ,tw
name_list = ["ttDM", "s-Chan", "t-Chan", "tW-Chan"]
argv_list = [sys.argv[1], 0, 0, 0]
n_event = [2e5, 2e5, 128832, 2e5]

argv_list[1] = argv_list[0].replace("tt", "top").replace(".root", "_sChan_4F.root")
argv_list[2] = argv_list[1].replace("s", "t")
argv_list[3] = argv_list[1].replace("s", "tW").replace("4F", "5F")


for j in range(0, len(hist_list)):
	file_list[j] = TFile(argv_list[j])
	hist_list[j] = events.Clone()
	del events

title = argv_list[0][5:-5]

c1.cd()
hs = THStack("hs","Cut Flow "+title+"; Cuts applied; Events")

stack1_leg = TLegend(.60, .72, .73, .85)
stack1_leg.SetBorderSize(0)
stack1_leg.AddEntry(hist_list[0], name_list[0], "l")

hist_list[0].SetLineColor(1)
for i in range(1, len(hist_list)):
	hist_list[i].SetFillColor(color_list[i])
	hist_list[i].SetLineColor(color_list[i])
	hist_list[i].Scale(scale_list[i]/n_event[i]*2.2e3)
	stack1_leg.AddEntry(hist_list[i], name_list[i], "f")
	hs.Add(hist_list[i])

hist_list[0].Scale(scale_list[0]/n_event[0]*2.2e3)

hs.Draw("hist")
hs.SetMaximum(1e5)
hist_list[0].Draw("histsame")
gPad.SetLogy()

stack1_leg.Draw("same")

c1.Print("./images/"+title+"_Hadronic_Cut_Flow.pdf")
