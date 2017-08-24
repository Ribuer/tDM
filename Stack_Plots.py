from ROOT import *
import sys
import string
import math as mt
from array import array

color_list = [1, 633, 434, 402, 877, 419, 396, 628, 618, 882, 428, 612, 414, 596]

c1 = TCanvas("canvas1", "Test", 800, 600)
c2 = TCanvas("canvas2", "Test", 800, 600)
c3 = TCanvas("canvas3", "Test", 800, 600)
c4 = TCanvas("canvas4", "Test", 800, 600)

hist_list = [0, 0, 0, 0]
file_list = [0, 0, 0, 0]
final_list = [0, 0, 0, 0]
after_lept = [0, 0, 0, 0]
mindphi_lept = [0, 0, 0, 0]
scale_list = [19.76, 7.03e-2, 27.18e-1, 73.25e-2] #tt, single tops: s,t ,tw
name_list = ["ttDM", "s-Chan", "t-Chan", "tW-Chan"]
argv_list = [sys.argv[1], 0, 0, 0]
n_event = [2e5, 2e5, 128832, 2e5]

argv_list[1] = argv_list[0].replace("tt", "top").replace(".root", "_sChan_4F.root")
argv_list[2] = argv_list[1].replace("s", "t")
argv_list[3] = argv_list[1].replace("s", "tW").replace("4F", "5F")


for j in range(0, len(hist_list)):
	file_list[j] = TFile(argv_list[j])

	hist_list[j] = met_incl.Clone()
	del met_incl		

	final_list[j] = mindphi.Clone()	
	del mindphi

	after_lept[j] = leptons.Clone()
	del leptons

	mindphi_lept[j] = mindphi_val.Clone()
	del mindphi_val

title = argv_list[0][5:-5]

c1.cd()
hs = THStack("hs",title+" before selection; #slash{E}_{T} (GeV); Events / 40 GeV")
hs2 = THStack("hs2",title+" after selection; #slash{E}_{T} (GeV); Events / 40 GeV")
hs3 = THStack("hs3",title+" after Lepton selection; #slash{E}_{T} (GeV); Events / 40 GeV")
hs4 = THStack("hs3",title+" after Lepton selection; #Delta#Phi; Events / 0.2")

stack1_leg = TLegend(.60, .72, .73, .85)
stack1_leg.SetBorderSize(0)
stack1_leg.AddEntry(hist_list[0], name_list[0], "l")
stack2_leg = TLegend(.60, .72, .73, .85)
stack2_leg.SetBorderSize(0)
stack2_leg.AddEntry(final_list[0], name_list[0], "l")
stack3_leg = TLegend(.60, .72, .73, .85)
stack3_leg.SetBorderSize(0)
stack3_leg.AddEntry(after_lept[0], name_list[0], "l")
stack4_leg = TLegend(.60, .72, .73, .85)
stack4_leg.SetBorderSize(0)
stack4_leg.AddEntry(mindphi_lept[0], name_list[0], "l")

hist_list[0].SetLineColor(1)
final_list[0].SetLineColor(1)
after_lept[0].SetLineColor(1)
mindphi_lept[0].SetLineColor(1)

for i in range(1, len(hist_list)):
	hist_list[i].SetFillColor(color_list[i])
	hist_list[i].SetLineColor(color_list[i])
	hist_list[i].Scale(scale_list[i]/n_event[i]*2.2e3)
	stack1_leg.AddEntry(hist_list[i], name_list[i], "f")
	hs.Add(hist_list[i])

	final_list[i].SetFillColor(color_list[i])
	final_list[i].SetLineColor(color_list[i])
	final_list[i].Scale(scale_list[i]/n_event[i]*2.2e3)
	stack2_leg.AddEntry(final_list[i], name_list[i], "f")
	hs2.Add(final_list[i])

	after_lept[i].SetFillColor(color_list[i])
	after_lept[i].SetLineColor(color_list[i])
	after_lept[i].Scale(scale_list[i]/n_event[i]*2.2e3)
	stack3_leg.AddEntry(after_lept[i], name_list[i], "f")
	hs3.Add(after_lept[i])

	mindphi_lept[i].SetFillColor(color_list[i])
	mindphi_lept[i].SetLineColor(color_list[i])
	mindphi_lept[i].Scale(scale_list[i]/n_event[i]*2.2e3)
	stack4_leg.AddEntry(mindphi_lept[i], name_list[i], "f")
	hs4.Add(mindphi_lept[i])

hist_list[0].Scale(scale_list[0]/n_event[0]*2.2e3)
final_list[0].Scale(scale_list[0]/n_event[0]*2.2e3)
after_lept[0].Scale(scale_list[0]/n_event[0]*2.2e3)
mindphi_lept[0].Scale(scale_list[0]/n_event[0]*2.2e3)

hs.Draw("hist")
hs.GetXaxis().SetRangeUser(180, 820)
hist_list[0].Draw("histsame")
gPad.SetLogy()

stack1_leg.Draw("same")

c1.Print(argv_list[0][:-5]+"_Hadronic_Stack_Pre_Selection.pdf")

c2.cd()

hs2.Draw("hist")
hs2.GetXaxis().SetRangeUser(180, 820)
final_list[0].Draw("histsame")
gPad.SetLogy()

stack2_leg.Draw("same")

c2.Print(argv_list[0][:-5]+"_Hadronic_Stack_ Post_Selection.pdf")


c3.cd()

hs3.Draw("hist")
hs3.GetXaxis().SetRangeUser(180, 820)
after_lept[0].Draw("histsame")
gPad.SetLogy()

stack3_leg.Draw("same")

c3.Print(argv_list[0][:-5]+"_Hadronic_Stack_After_Lepton.pdf")

c4.cd()

hs4.Draw("hist")
hs4.GetXaxis().SetRangeUser(180, 820)
mindphi_lept[0].Draw("histsame")
gPad.SetLogy()

stack4_leg.Draw("same")

c4.Print(argv_list[0][:-5]+"_Hadronic_Stack_Phi_After_Lepton.pdf")
