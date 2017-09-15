from ROOT import *
import sys
import string
import math as mt
from array import array

color_list = [1, 633, 434, 402, 877, 419, 396, 628, 618, 882, 428, 612, 414, 596]

c1 = TCanvas("canvas1", "Name", 800, 600)
pad_thresh = .2325
up_pad = TPad("upperPad", "Name", .005, pad_thresh, .995, .995)
low_pad = TPad("lowerPad", "Name", .005, .01, .995, pad_thresh+.075)

up_pad.Draw()
low_pad.Draw()
hist_list = [0, 0, 0, 0]
file_list = [0, 0, 0, 0]
scale_dict = {"ttDM_Mchi1Mphi10": 19.76, "topDM_Mchi1Mphi10_sChan_4F": 7.03e-2, "topDM_Mchi1Mphi10_tChan_4F": 27.18e-1, "topDM_Mchi1Mphi10_tWChan_5F": 73.25e-2}
name_list = ["ttDM", "s-Chan", "t-Chan", "tW-Chan"]
argv_list = [sys.argv[1], 0, 0, 0]

title = argv_list[0][5:-14]
type1 = argv_list[0][-13:-5]
level = "Reco "

argv_list[1] = argv_list[0].replace("tt", "top").replace(type1+".root", "sChan_4F_"+type1+".root")
argv_list[2] = argv_list[1].replace("s", "t")
argv_list[3] = argv_list[1].replace("s", "tW").replace("4F", "5F")


for j in range(0, len(hist_list)):
	file_list[j] = TFile(argv_list[j])
	hist_list[j] = events.Clone()
	del events


c1.cd()
hs = THStack("hs", level+type1+" Cut Flow "+title+";; Scaled Events")

stack1_leg = TLegend(.70, .65, .88, .85)
stack1_leg.SetBorderSize(0)
stack1_leg.AddEntry(hist_list[0], name_list[0], "l")

hist_list[0].SetLineColor(1)
for i in range(1, len(hist_list)):
	up_pad.cd()
	hist_list[i].SetFillColor(color_list[i])
	hist_list[i].SetLineColor(color_list[i])
	hist_list[i].Scale(scale_dict[argv_list[i][:-14]]/hist_list[i].GetBinContent(1)*2.2e3)
	stack1_leg.AddEntry(hist_list[i], name_list[i], "f")
	hs.Add(hist_list[i])

hs.Draw("hist")
gPad.Update()

hist_list[0].Scale(scale_dict[argv_list[0][:-14]]/hist_list[0].GetBinContent(1)*2.2e3)
hist_list[0].Draw("histsame")
hs.GetXaxis().SetLabelSize(0)

hs_max = hs.GetMaximum()
if hist_list[0].GetMaximum() > hs_max:
	hs_max = hist_list[0].GetMaximum()

hs.SetMaximum(hs_max*1.2)
hs.SetMinimum(1e-1)
gPad.SetLogy()

stack1_leg.Draw("same")

ratio_add = hist_list[1].Clone()
ratio_add.Add(hist_list[2])
ratio_add.Add(hist_list[3])

low_pad.cd()
hist_list[0].SetTitle(";;ttDM / topDM")
ratio = hist_list[0].Clone()

ratio.Divide(ratio_add)
ratio.Draw("hist")
gStyle.SetOptStat(0)

ratio.GetXaxis().SetLabelSize(.125)
ratio.GetYaxis().SetLabelSize(.1)
ratio.GetYaxis().SetTitleSize(ratio.GetYaxis().GetTitleSize()*2.25)
ratio.GetYaxis().SetTitleOffset(.425)
ratio.SetLineColor(kRed)
ratio.SetLineStyle(2)

ratio_line = TLine(0, int(ratio.GetBinContent(3)), int(ratio.GetSize())-2, int(ratio.GetBinContent(3)))
ratio_line.Draw("same")

c1.Print("./images/"+type1+"/Cut_Flow/"+title+"_"+type1+"_Cut_Flow.pdf")
