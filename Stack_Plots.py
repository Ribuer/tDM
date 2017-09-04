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

hist_list = [0, 0, 0, 0]
file_list = [0, 0, 0, 0]
final_list = [0, 0, 0, 0]
after_lept = [0, 0, 0, 0]
mindphi_lept = [0, 0, 0, 0]
bjeteta_list = [0, 0, 0, 0]
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


for j in range(0, len(hist_list)):
	file_list[j] = TFile(argv_list[j])

	n_events.append(events.GetBinContent(1))
	del events

	hist_list[j] = met_incl.Clone()
	del met_incl		

	final_list[j] = mindphi.Clone()	
	del mindphi

	after_lept[j] = leptons.Clone()
	del leptons

	mindphi_lept[j] = mindphi_val.Clone()
	del mindphi_val

	bjeteta_list[j] = bjeteta.Clone()
	del bjeteta

hs = THStack("hs",level+title+" before selection; ; Events / 40 GeV")
hs2 = THStack("hs2",level+title+" after selection; ; Events / 40 GeV")
hs3 = THStack("hs3",level+title+" after Lepton veto;; Events / 40 GeV")
hs4 = THStack("hs4",level+title+" after Lepton veto;; Events / 0.2")
hs5 = THStack("hs5",level+title+" B Jet #Eta;; Events / 0.2")

stack1_leg = TLegend(.70, .65, .88, .85)
stack1_leg.SetBorderSize(0)
stack1_leg.AddEntry(hist_list[0], name_list[0], "l")
stack2_leg = TLegend(.70, .65, .88, .85)
stack2_leg.SetBorderSize(0)
stack2_leg.AddEntry(final_list[0], name_list[0], "l")
stack3_leg = TLegend(.70, .65, .88, .85)
stack3_leg.SetBorderSize(0)
stack3_leg.AddEntry(after_lept[0], name_list[0], "l")
stack4_leg = TLegend(.70, .65, .88, .85)
stack4_leg.SetBorderSize(0)
stack4_leg.AddEntry(mindphi_lept[0], name_list[0], "l")
stack5_leg = TLegend(.70, .65, .88, .85)
stack5_leg.SetBorderSize(0)
stack5_leg.AddEntry(bjeteta_list[0], name_list[0], "l")

hist_list[0].SetLineColor(1)
final_list[0].SetLineColor(1)
after_lept[0].SetLineColor(1)
mindphi_lept[0].SetLineColor(1)
bjeteta_list[0].SetLineColor(1)

hist_list[0].Scale(scale_dict[argv_list[0][:-14]]/n_events[0]*2.2e3)
final_list[0].Scale(scale_dict[argv_list[0][:-14]]/n_events[0]*2.2e3)
after_lept[0].Scale(scale_dict[argv_list[0][:-14]]/n_events[0]*2.2e3)
mindphi_lept[0].Scale(scale_dict[argv_list[0][:-14]]/n_events[0]*2.2e3)
bjeteta_list[0].Scale(scale_dict[argv_list[0][:-14]]/n_events[0]*2.2e3)

#Ratioplots ttDM
ratio1 = hist_list[0].Clone()
ratio2 = final_list[0].Clone()
ratio3 = after_lept[0].Clone()
ratio4 = mindphi_lept[0].Clone()
ratio5 = bjeteta_list[0].Clone()

for i in range(1, len(hist_list)):
	hist_list[i].SetFillColor(color_list[i])
	hist_list[i].SetLineColor(color_list[i])
	hist_list[i].Scale(scale_dict[argv_list[i][:-14]]/n_events[i]*2.2e3)
	stack1_leg.AddEntry(hist_list[i], name_list[i], "f")
	hs.Add(hist_list[i])

	final_list[i].SetFillColor(color_list[i])
	final_list[i].SetLineColor(color_list[i])
	final_list[i].Scale(scale_dict[argv_list[i][:-14]]/n_events[i]*2.2e3)
	stack2_leg.AddEntry(final_list[i], name_list[i], "f")
	hs2.Add(final_list[i])

	after_lept[i].SetFillColor(color_list[i])
	after_lept[i].SetLineColor(color_list[i])
	after_lept[i].Scale(scale_dict[argv_list[i][:-14]]/n_events[i]*2.2e3)
	stack3_leg.AddEntry(after_lept[i], name_list[i], "f")
	hs3.Add(after_lept[i])

	mindphi_lept[i].SetFillColor(color_list[i])
	mindphi_lept[i].SetLineColor(color_list[i])
	mindphi_lept[i].Scale(scale_dict[argv_list[i][:-14]]/n_events[i]*2.2e3)
	stack4_leg.AddEntry(mindphi_lept[i], name_list[i], "f")
	hs4.Add(mindphi_lept[i])

	bjeteta_list[i].SetFillColor(color_list[i])
	bjeteta_list[i].SetLineColor(color_list[i])
	bjeteta_list[i].Scale(scale_dict[argv_list[i][:-14]]/n_events[i]*2.2e3)
	stack4_leg.AddEntry(bjeteta_list[i], name_list[i], "f")
	hs4.Add(bjeteta_list[i])

	if i == 1:
		#Ratioplots topDM, summing up below
		ratio_hist1 = hist_list[1].Clone()
		ratio_hist2 = final_list[1].Clone()
		ratio_hist3 = after_lept[1].Clone()
		ratio_hist4 = mindphi_lept[1].Clone()
		ratio_hist5 = bjeteta_list[1].Clone()

	else:
		ratio_hist1.Add(hist_list[i])
		ratio_hist2.Add(final_list[i])
		ratio_hist3.Add(after_lept[i])
		ratio_hist4.Add(mindphi_lept[i])
		ratio_hist5.Add(bjeteta_list[i])


c1.cd()
up_pad1.Draw()
low_pad1.Draw()

up_pad1.cd()
hs.Draw("hist")
hist_list[0].Draw("histsame")
gPad.SetLogy()

hs_max = hs.GetMaximum()
if hist_list[0].GetMaximum() > hs_max:
	hs_max = hist_list[0].GetMaximum()

hs.SetMaximum(hs_max*1.1)

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

c1.Print("./images/"+type1+"/Stack_Plots/"+argv_list[0][5:-5]+"_Stack_Pre_Selection.pdf")


c2.cd()
up_pad2.Draw()
low_pad2.Draw()

up_pad2.cd()
hs2.Draw("hist")
final_list[0].Draw("histsame")
gPad.SetLogy()

hs2_max = hs2.GetMaximum()
if final_list[0].GetMaximum() > hs2_max:
	hs2_max = final_list[0].GetMaximum()

hs2.GetXaxis().SetRangeUser(0, 640)
hs2.SetMaximum(hs2_max*1.1)
hs2.SetMinimum(1e-2)

stack2_leg.Draw("same")

low_pad2.cd()
ratio2.Divide(ratio_hist2)
ratio2.Draw("hist")
ratio2.GetXaxis().SetRangeUser(0, 640)
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

c2.Print("./images/"+type1+"/Stack_Plots/"+argv_list[0][5:-5]+"_Stack_ Post_Selection.pdf")


c3.cd()
up_pad3.Draw()
low_pad3.Draw()

up_pad3.cd()
hs3.Draw("hist")
after_lept[0].Draw("histsame")
gPad.SetLogy()

hs3_max = hs3.GetMaximum()
if after_lept[0].GetMaximum() > hs3_max:
	hs3_max = after_lept[0].GetMaximum()

hs3.GetXaxis().SetRangeUser(0, 500)
hs3.SetMaximum(hs3_max*1.1)
hs3.SetMinimum(1e-1)

stack3_leg.Draw("same")

low_pad3.cd()
ratio3.Divide(ratio_hist3)
ratio3.Draw("hist")
ratio3.GetXaxis().SetRangeUser(0, 500)
gStyle.SetOptStat(0)

#Works for png
ratio3.SetTitle("; #slash{E}_{T} (GeV); ttDM / topDM")
ratio3.GetXaxis().SetLabelSize(.09)
ratio3.GetXaxis().SetTitleSize(ratio3.GetXaxis().GetTitleSize()*3)
ratio3.GetXaxis().SetTitleOffset(.8)
ratio3.GetYaxis().SetLabelSize(.09)
ratio3.GetYaxis().SetTitleSize(ratio3.GetYaxis().GetTitleSize()*2.25)
ratio3.GetYaxis().SetTitleOffset(.425)
gPad.SetBottomMargin(0.2)

c3.Print("./images/"+type1+"/Stack_Plots/"+argv_list[0][5:-5]+"_Stack_After_Lepton.pdf")


c4.cd()
up_pad4.Draw()
low_pad4.Draw()

up_pad4.cd()
hs4.Draw("hist")
mindphi_lept[0].Draw("histsame")
gPad.SetLogy()

hs4_max = hs4.GetMaximum()
if mindphi_lept[0].GetMaximum() > hs4_max:
	hs4_max = mindphi_lept[0].GetMaximum()

hs4.GetXaxis().SetRangeUser(0, mt.pi)
hs4.SetMaximum(hs4_max*1.1)

stack4_leg.Draw("same")

low_pad4.cd()
ratio4.Divide(ratio_hist4)
ratio4.Draw("hist")
ratio4.GetXaxis().SetRangeUser(0, mt.pi)
gStyle.SetOptStat(0)

#Works for png
ratio4.SetTitle(";Min#Delta#Phi between #slash{E}_{T} and ; ttDM / topDM")
ratio4.GetXaxis().SetLabelSize(.09)
ratio4.GetXaxis().SetTitleSize(ratio4.GetXaxis().GetTitleSize()*3)
ratio4.GetXaxis().SetTitleOffset(.8)
ratio4.GetYaxis().SetLabelSize(.09)
ratio4.GetYaxis().SetTitleSize(ratio4.GetYaxis().GetTitleSize()*2.25)
ratio4.GetYaxis().SetTitleOffset(.425)
gPad.SetBottomMargin(0.2)

c4.Print("./images/"+type1+"/Stack_Plots/"+argv_list[0][5:-5]+"_Stack_Phi_After_Lepton.pdf")
c4.Print("./images/"+type1+"/Stack_Plots/"+argv_list[0][5:-5]+"_Stack_Phi_After_Lepton.png")

c5.cd()
up_pad5.Draw()
low_pad5.Draw()

up_pad5.cd()
hs5.Draw("hist")
bjeteta_list[0].Draw("histsame")
gPad.SetLogy()

hs_max = hs5.GetMaximum()
if bjeteta_list[0].GetMaximum() > hs_max:
	hs_max = bjeteta_list[0].GetMaximum()

hs5.SetMaximum(hs_max*1.1)

stack5_leg.Draw("same")

low_pad5.cd()
ratio5.Divide(ratio_hist5)
ratio5.Draw("hist")
gStyle.SetOptStat(0)

#Works for png
ratio5.SetTitle(";P_{t} Leading BJet #Eta; ttDM / topDM")
ratio5.GetXaxis().SetLabelSize(.09)
ratio5.GetXaxis().SetTitleSize(ratio5.GetXaxis().GetTitleSize()*3)
ratio5.GetXaxis().SetTitleOffset(.8)
ratio5.GetYaxis().SetLabelSize(.09)
ratio5.GetYaxis().SetTitleSize(ratio5.GetYaxis().GetTitleSize()*2.25)
ratio5.GetYaxis().SetTitleOffset(.425)
gPad.SetBottomMargin(0.2)

c5.Print("./images/"+type1+"/Stack_Plots/"+argv_list[0][5:-5]+"_Stack_BJet_Eta.pdf")

