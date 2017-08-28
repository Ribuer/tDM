from ROOT import *
import sys
import string
import math as mt
from array import array

c1 = TCanvas("canvas2", "Test2", 800, 600)

hist_list = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
top_rec_hist = [0, 0, 0, 0, 0]
ratio_hist = [0, 0, 0, 0, 0]
file_list = [0, 0, 0, 0]
scale_list = [19.76, 7.03e-2, 27.18e-1, 73.25e-2] #tt, single tops: s,t ,tw
argv_list = [sys.argv[1], 0, 0, 0, 0]
n_event = [2e5, 2e5, 128832, 2e5]

axis_labelling = ["; #Delta#Phi between #slash{E}_{t} and Top quark / .2; #slash{E}_{t} (GeV) / 20 (GeV)", "; P_{t} (Leading jet) (GeV) / 20 (GeV); #slash{E}_{t} (GeV) / 20 (GeV)", "; P_{t} (Leading b-jet) (GeV) / 20 (GeV); #slash{E}_{t} (GeV) / 20 (GeV)", "; Top quark P_{t} (GeV) / 20 (GeV); P_{t} (Leading b-jet) (GeV) / 20 (GeV)", "; Top quark #Phi / .2; Highest P_{T} B-Jet, #Phi / .2"]
title_labelling = "Ratio Hadronic "+argv_list[0][5:-5]
output_name = ["TopdPhiMet_MET", "Jet1Pt_MET", "BJet1Pt_MET", "TopPt_BJet1Pt", "TopPhi_BJet1Phi"]

argv_list[1] = argv_list[0].replace("tt", "top").replace(".root", "_sChan_4F.root")
argv_list[2] = argv_list[1].replace("s", "t")
argv_list[3] = argv_list[1].replace("s", "tW").replace("4F", "5F")
argv_list[4] = argv_list[0].replace("tt", "top")

def print_tt(file_name, hist1, hist2, hist3, hist4, hist5):
	hist1.Draw("colz")
	gStyle.SetOptStat(0)
	hist1.SetTitle(file_name[0:4]+" "+file_name[5:-5]+" Hadronic "+axis_labelling[0])
	hist1.GetXaxis().SetTitleOffset(1.2)
	hist1.GetYaxis().SetTitleOffset(1.2)
	hist1.GetZaxis().SetTickSize(.01)
	c1.Update()	
	palette = hist1.GetListOfFunctions().FindObject("palette")
	palette.SetX2NDC(.93)
	c1.Print("./images/"+file_name[:-5]+"_Hadronic_"+output_name[0]+".pdf")

	hist2.Draw("colz")
	hist2.SetTitle(file_name[0:4]+" "+file_name[5:-5]+" Hadronic "+axis_labelling[1])
	hist2.GetXaxis().SetTitleOffset(1.2)
	hist2.GetYaxis().SetTitleOffset(1.2)
	hist2.GetZaxis().SetTickSize(.01)
	c1.Update()	
	palette = hist2.GetListOfFunctions().FindObject("palette")
	palette.SetX2NDC(.93)
	c1.Print("./images/"+file_name[:-5]+"_Hadronic_"+output_name[1]+".pdf")

	hist3.Draw("colz")
	hist3.SetTitle(file_name[0:4]+" "+file_name[5:-5]+" Hadronic "+axis_labelling[2])
	hist3.GetXaxis().SetTitleOffset(1.2)
	hist3.GetYaxis().SetTitleOffset(1.2)
	hist3.GetZaxis().SetTickSize(.01)
	c1.Update()	
	palette = hist3.GetListOfFunctions().FindObject("palette")
	palette.SetX2NDC(.93)
	c1.Print("./images/"+file_name[:-5]+"_Hadronic_"+output_name[2]+".pdf")

	hist4.Draw("colz")
	hist4.SetTitle(file_name[0:4]+" "+file_name[5:-5]+" Hadronic "+axis_labelling[3])
	hist4.GetXaxis().SetTitleOffset(1.2)
	hist4.GetYaxis().SetTitleOffset(1.2)
	hist4.GetZaxis().SetTickSize(.01)
	c1.Update()	
	palette = hist4.GetListOfFunctions().FindObject("palette")
	palette.SetX2NDC(.93)
	c1.Print("./images/"+file_name[:-5]+"_Hadronic_"+output_name[3]+".pdf")

	hist5.Draw("colz")
	hist5.SetTitle(file_name[0:4]+" "+file_name[5:-5]+" Hadronic "+axis_labelling[4])
	hist5.GetXaxis().SetTitleOffset(1.2)
	hist5.GetYaxis().SetTitleOffset(1.2)
	hist4.GetZaxis().SetTickSize(.01)
	c1.Update()	
	palette = hist4.GetListOfFunctions().FindObject("palette")
	palette.SetX2NDC(.93)
	c1.Print("./images/"+file_name[:-5]+"_Hadronic_"+output_name[4]+".pdf")

for j in range(0, len(hist_list)):
	file_list[j] = TFile(argv_list[j])
	
	hist_list[j][0] = met_topdphi.Clone()
	hist_list[j][1] = met_jet1pt.Clone()
	hist_list[j][2] = met_bjet1pt.Clone()
	hist_list[j][3] = toppt_bjet1pt.Clone()
	hist_list[j][4] = topphi_bjet1phi.Clone()

	for i in range(0, len(hist_list[0])):
		hist_list[j][i].Scale(scale_list[j]/n_event[j]*2.2e3)

	if j == 0:
		print_tt(argv_list[j], hist_list[j][0], hist_list[j][1], hist_list[j][2], hist_list[j][3], hist_list[j][4])
	elif j == 1:
		for k in range(0, len(top_rec_hist)):
			top_rec_hist[k] = hist_list[j][k]
	else:
		for k in range(0, len(top_rec_hist)):
			top_rec_hist[k].Add(hist_list[j][k])

	del met_topdphi, met_jet1pt, met_bjet1pt, toppt_bjet1pt, topphi_bjet1phi

print_tt(argv_list[4], top_rec_hist[0], top_rec_hist[1], top_rec_hist[2], top_rec_hist[3], top_rec_hist[4])

for m in range(0, len(top_rec_hist)):
	hist_list[0][m].Draw("colz")
	hist_list[0][m].Divide(top_rec_hist[m])
	hist_list[0][m].SetTitle(title_labelling+axis_labelling[m])
	c1.Print("./images/Ratio_Hadronic_"+output_name[m]+".pdf")

