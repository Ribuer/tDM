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
c5 = TCanvas("canvas5", "Test", 800, 600)
c6 = TCanvas("canvas6", "Test", 800, 600)

pad_thresh = .2325
up_pad1 = TPad("upperPad1", "Name", .005, pad_thresh, .995, .995)
low_pad1 = TPad("lowerPad1", "Name", .005, .005, .995, pad_thresh+.07)
up_pad2 = TPad("upperPad2", "Name", .005, pad_thresh, .995, .995)
low_pad2 = TPad("lowerPad2", "Name", .005, .005, .995, pad_thresh+.07)
up_pad3 = TPad("upperPad3", "Name", .005, pad_thresh, .995, .995)
low_pad3 = TPad("lowerPad3", "Name", .005, .005, .995, pad_thresh+.07)
up_pad4 = TPad("upperPad4", "Name", .005, pad_thresh, .995, .995)
low_pad4 = TPad("lowerPad4", "Name", .005, .005, .995, pad_thresh+.07)
up_pad5 = TPad("upperPad5", "Name", .005, pad_thresh, .995, .995)
low_pad5 = TPad("lowerPad5", "Name", .005, .005, .995, pad_thresh+.07)
up_pad6 = TPad("upperPad6", "Name", .005, pad_thresh, .995, .995)
low_pad6 = TPad("lowerPad6", "Name", .005, .005, .995, pad_thresh+.07)

cut1 = [0, 0, 0, 0]
cut2 = [0, 0, 0, 0]
cut3 = [0, 0, 0, 0]
cut4 = [0, 0, 0, 0]
cut5 = [0, 0, 0, 0]
cut6 = [0, 0, 0, 0]

file_list = [0, 0, 0, 0]
scale_dict = {"ttDM_Mchi1Mphi10": 19.76, "topDM_Mchi1Mphi10_sChan_4F": 7.03e-2, "topDM_Mchi1Mphi10_tChan_4F": 27.18e-1, "topDM_Mchi1Mphi10_tWChan_5F": 73.25e-2}
name_list = ["ttDM", "s-Chan", "t-Chan", "tW-Chan"]
argv_list = [sys.argv[1], 0, 0, 0]
n_events = []

title = argv_list[0][5:-14]
type1 = argv_list[0][-13:-5]
level = "Reco "

argv_list[1] = argv_list[0].replace("tt", "top").replace(type1+".root", "sChan_4F_"+type1+".root")
argv_list[2] = argv_list[1].replace("s", "t")
argv_list[3] = argv_list[1].replace("s", "tW").replace("4F", "5F")


for j in range(0, len(cut1)):
	file_list[j] = TFile(argv_list[j])

	n_events.append(events.GetBinContent(1))
	del events

	cut1[j] = met_incl.Clone()
	del met_incl	

	cut2[j] = leptons.Clone()
	del leptons

	cut3[j] = met_jet.Clone()
	del met_jet	

	cut4[j] = met_bjet.Clone()
	del met_bjet	

	cut5[j] = mindphi.Clone()	
	del mindphi

	cut6[j] = met_sel.Clone()	
	del met_sel

hs = THStack("hs",level+title+" No Cuts; ; Events / 40 GeV")
hs2 = THStack("hs2",level+title+" Lepton veto; ; Events / 40 GeV")
hs3 = THStack("hs3",level+title+" Njets >= 4; ; Events / 40 GeV")
hs4 = THStack("hs4",level+title+" Nbjets >= 2;; Events / 40 GeV")
hs5 = THStack("hs5",level+title+" min#Delta#Phi > 1;; Events / 40 GeV")
hs6 = THStack("hs6",level+title+" MET > 200 GeV;; Events / 40 GeV")

stack1_leg = TLegend(.70, .65, .88, .85)
stack1_leg.SetBorderSize(0)
stack1_leg.AddEntry(cut1[0], name_list[0], "l")
stack2_leg = TLegend(.70, .65, .88, .85)
stack2_leg.SetBorderSize(0)
stack2_leg.AddEntry(cut2[0], name_list[0], "l")
stack3_leg = TLegend(.70, .65, .88, .85)
stack3_leg.SetBorderSize(0)
stack3_leg.AddEntry(cut3[0], name_list[0], "l")
stack4_leg = TLegend(.70, .65, .88, .85)
stack4_leg.SetBorderSize(0)
stack4_leg.AddEntry(cut4[0], name_list[0], "l")
stack5_leg = TLegend(.70, .65, .88, .85)
stack5_leg.SetBorderSize(0)
stack5_leg.AddEntry(cut5[0], name_list[0], "l")
stack6_leg = TLegend(.70, .65, .88, .85)
stack6_leg.SetBorderSize(0)
stack6_leg.AddEntry(cut6[0], name_list[0], "l")

cut1[0].SetLineColor(1)
cut2[0].SetLineColor(1)
cut3[0].SetLineColor(1)
cut4[0].SetLineColor(1)
cut5[0].SetLineColor(1)
cut6[0].SetLineColor(1)

cut1[0].Scale(scale_dict[argv_list[0][:-14]]/n_events[0]*2.2e3)
cut2[0].Scale(scale_dict[argv_list[0][:-14]]/n_events[0]*2.2e3)
cut3[0].Scale(scale_dict[argv_list[0][:-14]]/n_events[0]*2.2e3)
cut4[0].Scale(scale_dict[argv_list[0][:-14]]/n_events[0]*2.2e3)
cut5[0].Scale(scale_dict[argv_list[0][:-14]]/n_events[0]*2.2e3)
cut6[0].Scale(scale_dict[argv_list[0][:-14]]/n_events[0]*2.2e3)

#Ratioplots ttDM
ratio1 = cut1[0].Clone()
ratio2 = cut2[0].Clone()
ratio3 = cut3[0].Clone()
ratio4 = cut4[0].Clone()
ratio5 = cut5[0].Clone()
ratio6 = cut6[0].Clone()

for i in range(1, len(cut1)):
	cut1[i].SetFillColor(color_list[i])
	cut1[i].SetLineColor(color_list[i])
	cut1[i].Scale(scale_dict[argv_list[i][:-14]]/n_events[i]*2.2e3)
	stack1_leg.AddEntry(cut1[i], name_list[i], "f")
	hs.Add(cut1[i])

	cut2[i].SetFillColor(color_list[i])
	cut2[i].SetLineColor(color_list[i])
	cut2[i].Scale(scale_dict[argv_list[i][:-14]]/n_events[i]*2.2e3)
	stack2_leg.AddEntry(cut2[i], name_list[i], "f")
	hs2.Add(cut2[i])

	cut3[i].SetFillColor(color_list[i])
	cut3[i].SetLineColor(color_list[i])
	cut3[i].Scale(scale_dict[argv_list[i][:-14]]/n_events[i]*2.2e3)
	stack3_leg.AddEntry(cut3[i], name_list[i], "f")
	hs3.Add(cut3[i])

	cut4[i].SetFillColor(color_list[i])
	cut4[i].SetLineColor(color_list[i])
	cut4[i].Scale(scale_dict[argv_list[i][:-14]]/n_events[i]*2.2e3)
	stack4_leg.AddEntry(cut4[i], name_list[i], "f")
	hs4.Add(cut4[i])

	cut5[i].SetFillColor(color_list[i])
	cut5[i].SetLineColor(color_list[i])
	cut5[i].Scale(scale_dict[argv_list[i][:-14]]/n_events[i]*2.2e3)
	stack5_leg.AddEntry(cut5[i], name_list[i], "f")
	hs5.Add(cut5[i])

	cut6[i].SetFillColor(color_list[i])
	cut6[i].SetLineColor(color_list[i])
	cut6[i].Scale(scale_dict[argv_list[i][:-14]]/n_events[i]*2.2e3)
	stack6_leg.AddEntry(cut6[i], name_list[i], "f")
	hs6.Add(cut6[i])


	if i == 1:
		#Ratioplots topDM, summing up below
		ratio_hist1 = cut1[1].Clone()
		ratio_hist2 = cut2[1].Clone()
		ratio_hist3 = cut3[1].Clone()
		ratio_hist4 = cut4[1].Clone()
		ratio_hist5 = cut5[1].Clone()
		ratio_hist6 = cut6[1].Clone()

	else:
		ratio_hist1.Add(cut1[i])
		ratio_hist2.Add(cut2[i])
		ratio_hist3.Add(cut3[i])
		ratio_hist4.Add(cut4[i])
		ratio_hist5.Add(cut5[i])
		ratio_hist6.Add(cut6[i])


c1.cd()
up_pad1.Draw()
low_pad1.Draw()

up_pad1.cd()
hs.Draw("hist")
cut1[0].Draw("histsame")
gPad.SetLogy()

hs_max = hs.GetMaximum()
if cut1[0].GetMaximum() > hs_max:
	hs_max = cut1[0].GetMaximum()

hs.SetMaximum(hs_max*1.1)
hs.SetMinimum(1e-1)

stack1_leg.Draw("same")

low_pad1.cd()
ratio1.Divide(ratio_hist1)
ratio1.Draw("hist")
gStyle.SetOptStat(0)

#Works for png
ratio1.SetTitle(";#slash{E}_{T} (GeV); ttDM / topDM")
ratio1.GetXaxis().SetLabelSize(.09)
ratio1.GetXaxis().SetTitleSize(ratio1.GetXaxis().GetTitleSize()*3)
ratio1.GetXaxis().SetTitleOffset(.8)
ratio1.GetYaxis().SetLabelSize(.09)
ratio1.GetYaxis().SetTitleSize(ratio1.GetYaxis().GetTitleSize()*2.25)
ratio1.GetYaxis().SetTitleOffset(.425)
gPad.SetBottomMargin(0.2)

c1.Print("./images/"+type1+"/Stack_Plots/Met_Flow/"+argv_list[0][5:-5]+"_Cut1.pdf")


c2.cd()
up_pad2.Draw()
low_pad2.Draw()

up_pad2.cd()
hs2.Draw("hist")
cut1[0].Draw("histsame")
gPad.SetLogy()

hs_max = hs2.GetMaximum()
if cut1[0].GetMaximum() > hs_max:
	hs_max = cut1[0].GetMaximum()

hs2.SetMaximum(hs_max*1.1)
hs2.SetMinimum(1e-1)

stack2_leg.Draw("same")

low_pad2.cd()
ratio2.Divide(ratio_hist2)
ratio2.Draw("hist")
gStyle.SetOptStat(0)

#Works for png
ratio2.SetTitle(";#slash{E}_{T} (GeV); ttDM / topDM")
ratio2.GetXaxis().SetLabelSize(.09)
ratio2.GetXaxis().SetTitleSize(ratio2.GetXaxis().GetTitleSize()*3)
ratio2.GetXaxis().SetTitleOffset(.8)
ratio2.GetYaxis().SetLabelSize(.09)
ratio2.GetYaxis().SetTitleSize(ratio2.GetYaxis().GetTitleSize()*2.25)
ratio2.GetYaxis().SetTitleOffset(.425)
gPad.SetBottomMargin(0.2)

c2.Print("./images/"+type1+"/Stack_Plots/Met_Flow/"+argv_list[0][5:-5]+"_Cut2.pdf")

c3.cd()
up_pad3.Draw()
low_pad3.Draw()

up_pad3.cd()
hs3.Draw("hist")
cut2[0].Draw("histsame")
gPad.SetLogy()

hs_max = hs3.GetMaximum()
if cut2[0].GetMaximum() > hs_max:
	hs_max = cut2[0].GetMaximum()

hs3.SetMaximum(hs_max*1.1)
hs3.SetMinimum(1e-1)

stack3_leg.Draw("same")

low_pad3.cd()
ratio3.Divide(ratio_hist3)
ratio3.Draw("hist")
gStyle.SetOptStat(0)

#Works for png
ratio3.SetTitle(";#slash{E}_{T} (GeV); ttDM / topDM")
ratio3.GetXaxis().SetLabelSize(.09)
ratio3.GetXaxis().SetTitleSize(ratio3.GetXaxis().GetTitleSize()*3)
ratio3.GetXaxis().SetTitleOffset(.8)
ratio3.GetYaxis().SetLabelSize(.09)
ratio3.GetYaxis().SetTitleSize(ratio3.GetYaxis().GetTitleSize()*2.25)
ratio3.GetYaxis().SetTitleOffset(.425)
gPad.SetBottomMargin(0.2)

c3.Print("./images/"+type1+"/Stack_Plots/Met_Flow/"+argv_list[0][5:-5]+"_Cut3.pdf")

c4.cd()
up_pad4.Draw()
low_pad4.Draw()

up_pad4.cd()
hs4.Draw("hist")
cut3[0].Draw("histsame")
gPad.SetLogy()

hs_max = hs4.GetMaximum()
if cut3[0].GetMaximum() > hs_max:
	hs_max = cut3[0].GetMaximum()

hs4.SetMaximum(hs_max*1.1)
hs4.SetMinimum(1e-1)

stack4_leg.Draw("same")

low_pad4.cd()
ratio4.Divide(ratio_hist4)
ratio4.Draw("hist")
gStyle.SetOptStat(0)

#Works for png
ratio4.SetTitle(";#slash{E}_{T} (GeV); ttDM / topDM")
ratio4.GetXaxis().SetLabelSize(.09)
ratio4.GetXaxis().SetTitleSize(ratio4.GetXaxis().GetTitleSize()*3)
ratio4.GetXaxis().SetTitleOffset(.8)
ratio4.GetYaxis().SetLabelSize(.09)
ratio4.GetYaxis().SetTitleSize(ratio4.GetYaxis().GetTitleSize()*2.25)
ratio4.GetYaxis().SetTitleOffset(.425)
gPad.SetBottomMargin(0.2)

c4.Print("./images/"+type1+"/Stack_Plots/Met_Flow/"+argv_list[0][5:-5]+"_Cut4.pdf")

c5.cd()
up_pad5.Draw()
low_pad5.Draw()

up_pad5.cd()
hs5.Draw("hist")
cut4[0].Draw("histsame")
gPad.SetLogy()

hs_max = hs5.GetMaximum()
if cut4[0].GetMaximum() > hs_max:
	hs_max = cut4[0].GetMaximum()

hs5.SetMaximum(hs_max*1.1)
hs5.SetMinimum(1e-2)

stack5_leg.Draw("same")

low_pad5.cd()
ratio5.Divide(ratio_hist5)
ratio5.Draw("hist")
gStyle.SetOptStat(0)

#Works for png
ratio5.SetTitle(";#slash{E}_{T} (GeV); ttDM / topDM")
ratio5.GetXaxis().SetLabelSize(.09)
ratio5.GetXaxis().SetTitleSize(ratio5.GetXaxis().GetTitleSize()*3)
ratio5.GetXaxis().SetTitleOffset(.8)
ratio5.GetYaxis().SetLabelSize(.09)
ratio5.GetYaxis().SetTitleSize(ratio5.GetYaxis().GetTitleSize()*2.25)
ratio5.GetYaxis().SetTitleOffset(.425)
gPad.SetBottomMargin(0.2)

c5.Print("./images/"+type1+"/Stack_Plots/Met_Flow/"+argv_list[0][5:-5]+"_Cut5.pdf")

c6.cd()
up_pad6.Draw()
low_pad6.Draw()

up_pad6.cd()
hs6.Draw("hist")
cut6[0].Draw("histsame")
gPad.SetLogy()

hs_max = hs6.GetMaximum()
if cut6[0].GetMaximum() > hs_max:
	hs_max = cut6[0].GetMaximum()

hs6.SetMaximum(hs_max*1.1)
hs6.SetMinimum(1e-2)

stack6_leg.Draw("same")

low_pad6.cd()
ratio6.Divide(ratio_hist6)
ratio6.Draw("hist")
gStyle.SetOptStat(0)

#Works for png
ratio6.SetTitle(";#slash{E}_{T} (GeV); ttDM / topDM")
ratio6.GetXaxis().SetLabelSize(.09)
ratio6.GetXaxis().SetTitleSize(ratio6.GetXaxis().GetTitleSize()*3)
ratio6.GetXaxis().SetTitleOffset(.8)
ratio6.GetYaxis().SetLabelSize(.09)
ratio6.GetYaxis().SetTitleSize(ratio6.GetYaxis().GetTitleSize()*2.25)
ratio6.GetYaxis().SetTitleOffset(.425)
gPad.SetBottomMargin(0.2)

c6.Print("./images/"+type1+"/Stack_Plots/Met_Flow/"+argv_list[0][5:-5]+"_Cut6.pdf")

