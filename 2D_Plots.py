from ROOT import *
import sys
import string
import math as mt
from array import array

c1 = TCanvas("canvas2", "Test2", 800, 600)

hist_list = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]]
top_rec_hist = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
file_list = [0, 0, 0, 0]
scale_dict = {"ttDM_Mchi1Mphi10": 19.76, "topDM_Mchi1Mphi10_sChan_4F": 7.03e-2, "topDM_Mchi1Mphi10_tChan_4F": 27.18e-1, "topDM_Mchi1Mphi10_tWChan_5F": 73.25e-2}
argv_list = [sys.argv[1], 0, 0, 0, 0]
name_list = [0, 0, 0, 0, 0]

level = "Gen "
type1 = argv_list[0][-13:-5]

argv_list[1] = argv_list[0].replace("tt", "top").replace(type1+".root", "sChan_4F_"+type1+".root")
argv_list[2] = argv_list[1].replace("s", "t")
argv_list[3] = argv_list[1].replace("s", "tW").replace("4F", "5F")
argv_list[4] = argv_list[0].replace("tt", "top")

axis_labelling = ["; #Delta#Phi between #slash{E}_{t} and Top quark / .2; #slash{E}_{t} (GeV) / 20 (GeV)", "; P_{t} (Leading jet) (GeV) / 20 (GeV); #slash{E}_{t} (GeV) / 20 (GeV)", "; P_{t} (Leading b-jet) (GeV) / 20 (GeV); #slash{E}_{t} (GeV) / 20 (GeV)", "; Top quark P_{t} (GeV) / 20 (GeV); P_{t} (Leading b-jet) (GeV) / 20 (GeV)", "; Top quark #Phi / .2; Highest P_{T} B-Jet, #Phi / .2"]
output_name = ["TopdPhiMet_MET", "Jet1Pt_MET", "BJet1Pt_MET", "TopPt_BJet1Pt", "TopPhi_BJet1Phi"]

def print_tt(file_name, hist1, hist2, hist3, hist4, hist5):
	file_print = file_name.split("_")[0]
	hist1.Draw("colz")
	gStyle.SetOptStat(0)
	hist1.SetTitle(level+type1+" "+file_print+" "+file_name[6:-14]+axis_labelling[0])
	hist1.GetXaxis().SetTitleOffset(1.2)
	hist1.GetYaxis().SetTitleOffset(1.2)
	hist1.GetZaxis().SetTickSize(.01)
	gPad.SetLogz()
	c1.Update()	
	palette = hist1.GetListOfFunctions().FindObject("palette")
	palette.SetX2NDC(.93)
	c1.Print("./images/"+type1+"/2D_Plots/"+file_name[:-5]+"_"+output_name[0]+".pdf")

	hist1_x = hist1.ProjectionX()
	hist1_x.SetTitle(level+type1+" "+file_print+" "+file_name[6:-14]+";#Delta#Phi between #slash{E}_{t} and Top quark; Events / 0.2")
	hist1_x.Draw("hist")
	c1.Print("./images/"+type1+"/1D_Plots/"+file_name[:-5]+"_"+output_name[0]+"_xaxis.pdf")

	hist1_y = hist1.ProjectionY()
	hist1_y.SetTitle(level+type1+" "+file_print+" "+file_name[6:-14]+"; #slash{E}_{t} (GeV) ; Events / 20 (GeV)")
	hist1_y.Draw("hist")
	c1.Print("./images/"+type1+"/1D_Plots/"+file_name[:-5]+"_"+output_name[0]+"_yaxis.pdf")

	hist2.Draw("colz")
	hist2.SetTitle(level+type1+" "+file_print+" "+file_name[6:-14]+axis_labelling[1])
	hist2.GetXaxis().SetTitleOffset(1.2)
	hist2.GetYaxis().SetTitleOffset(1.2)
	hist2.GetZaxis().SetTickSize(.01)
	gPad.SetLogz()
	c1.Update()	
	palette = hist2.GetListOfFunctions().FindObject("palette")
	palette.SetX2NDC(.93)
	c1.Print("./images/"+type1+"/2D_Plots/"+file_name[:-5]+"_"+output_name[1]+".pdf")

	hist2_x = hist2.ProjectionX()
	hist2_x.SetTitle(level+type1+" "+file_print+" "+file_name[6:-14]+";P_{t} (Leading jet) (GeV); Events / 20 (GeV)")
	hist2_x.Draw("hist")
	c1.Print("./images/"+type1+"/1D_Plots/"+file_name[:-5]+"_"+output_name[1]+"_xaxis.pdf")

	hist2_y = hist2.ProjectionY()
	hist2_y.SetTitle(level+type1+" "+file_print+" "+file_name[6:-14]+"; #slash{E}_{t} (GeV) ; Events / 20 (GeV)")
	hist2_y.Draw("hist")
	c1.Print("./images/"+type1+"/1D_Plots/"+file_name[:-5]+"_"+output_name[1]+"_yaxis.pdf")

	hist3.Draw("colz")
	hist3.SetTitle(level+type1+" "+file_print+" "+file_name[5:-5]+axis_labelling[2])
	hist3.GetXaxis().SetTitleOffset(1.2)
	hist3.GetYaxis().SetTitleOffset(1.2)
	hist3.GetZaxis().SetTickSize(.01)
	c1.Update()	
	palette = hist3.GetListOfFunctions().FindObject("palette")
	palette.SetX2NDC(.93)
	c1.Print("./images/"+type1+"/2D_Plots/"+file_name[:-5]+"_"+output_name[2]+".pdf")

	hist3_x = hist3.ProjectionX()
	hist3_x.SetTitle(level+type1+" "+file_print+" "+file_name[6:-14]+";P_{t} (Leading b-jet) (GeV); Events / 20 (GeV)")
	hist3_x.Draw("hist")
	c1.Print("./images/"+type1+"/1D_Plots/"+file_name[:-5]+"_"+output_name[2]+"_xaxis.pdf")

	hist3_y = hist3.ProjectionY()
	hist3_y.SetTitle(level+type1+" "+file_print+" "+file_name[6:-14]+"; #slash{E}_{t} (GeV) ; Events / 20 (GeV)")
	hist3_y.Draw("hist")
	c1.Print("./images/"+type1+"/1D_Plots/"+file_name[:-5]+"_"+output_name[2]+"_yaxis.pdf")


	hist4.Draw("colz")
	hist4.SetTitle(level+type1+" "+file_print+" "+file_name[6:-14]+axis_labelling[3])
	hist4.GetXaxis().SetTitleOffset(1.2)
	hist4.GetYaxis().SetTitleOffset(1.2)
	hist4.GetZaxis().SetTickSize(.01)
	gPad.SetLogz()
	c1.Update()	
	palette = hist4.GetListOfFunctions().FindObject("palette")
	palette.SetX2NDC(.93)
	c1.Print("./images/"+type1+"/2D_Plots/"+file_name[:-5]+"_"+output_name[3]+".pdf")

	hist4_x = hist4.ProjectionX()
	hist4_x.SetTitle(level+type1+" "+file_print+" "+file_name[6:-14]+"; Top quark P_{t} (GeV) ; 20 (GeV);")
	hist4_x.Draw("hist")
	c1.Print("./images/"+type1+"/1D_Plots/"+file_name[:-5]+"_"+output_name[3]+"_xaxis.pdf")

	hist4_y = hist4.ProjectionY()
	hist4_y.SetTitle(level+type1+" "+file_print+" "+file_name[6:-14]+"; P_{t} (Leading b-jet) (GeV) ; Events / 20 (GeV)")
	hist4_y.Draw("hist")
	c1.Print("./images/"+type1+"/1D_Plots/"+file_name[:-5]+"_"+output_name[3]+"_yaxis.pdf")

	hist5.Draw("colz")
	hist5.SetTitle(level+type1+" "+file_print+" "+file_name[6:-14]+axis_labelling[4])
	hist5.GetXaxis().SetTitleOffset(1.2)
	hist5.GetYaxis().SetTitleOffset(1.2)
	hist5.GetZaxis().SetTickSize(.01)
	gPad.SetLogz()
	c1.Update()	
	palette = hist5.GetListOfFunctions().FindObject("palette")
	palette.SetX2NDC(.93)
	c1.Print("./images/"+type1+"/2D_Plots/"+file_name[:-5]+"_"+output_name[4]+".pdf")

	hist5_x = hist5.ProjectionX()
	hist5_x.SetTitle(level+type1+" "+file_print+" "+file_name[6:-14]+";  Top quark #Phi; Events / .2")
	hist5_x.Draw("hist")
	c1.Print("./images/"+type1+"/1D_Plots/"+file_name[:-5]+"_"+output_name[4]+"_xaxis.pdf")

	hist5_y = hist5.ProjectionY()
	hist5_y.SetTitle(level+type1+" "+file_print+" "+file_name[6:-14]+";  Highest P_{T} B-Jet #Phi ; Events / .2)")
	hist5_y.Draw("hist")
	c1.Print("./images/"+type1+"/1D_Plots/"+file_name[:-5]+"_"+output_name[4]+"_yaxis.pdf")

for i in range(0, len(hist_list)):
	if i == 1:
		for h in range(0, len(argv_list)):
			name_list[h] = argv_list[h][:-14]+"_Jet_Selection_"+argv_list[h][-13:]
	else:
		for h in range(0, len(argv_list)):
			name_list[h] = argv_list[h]

	for j in range(0, len(hist_list[0])):
		file_list[j] = TFile(argv_list[j])
	
		n_events = events.GetBinContent(1)
		if i == 0:
			hist_list[i][j][0] = met_topdphi.Clone()
			hist_list[i][j][1] = met_jet1pt.Clone()
			hist_list[i][j][2] = met_bjet1pt.Clone()
			hist_list[i][j][3] = toppt_bjet1pt.Clone()
			hist_list[i][j][4] = topphi_bjet1phi.Clone()
		else:
			hist_list[i][j][0] = met_topdphi2.Clone()
			hist_list[i][j][1] = met_jet1pt2.Clone()
			hist_list[i][j][2] = met_bjet1pt2.Clone()
			hist_list[i][j][3] = toppt_bjet1pt2.Clone()
			hist_list[i][j][4] = topphi_bjet1phi2.Clone()

		for k in range(0, len(hist_list[0][0])):
			hist_list[i][j][k].Scale(scale_dict[argv_list[j][:-14]]/n_events*2.2e3)

		if j == 0:
			print_tt(name_list[j], hist_list[i][j][0], hist_list[i][j][1], hist_list[i][j][2], hist_list[i][j][3], hist_list[i][j][4])
		elif j == 1:
			for k in range(0, len(top_rec_hist[0])):
				top_rec_hist[i][k] = hist_list[i][j][k]
		else:
			for k in range(0, len(top_rec_hist[0])):
				top_rec_hist[i][k].Add(hist_list[i][j][k])

		del met_topdphi, met_jet1pt, met_bjet1pt, toppt_bjet1pt, topphi_bjet1phi, events, n_events


	print_tt(name_list[4], top_rec_hist[i][0], top_rec_hist[i][1], top_rec_hist[i][2], top_rec_hist[i][3], top_rec_hist[i][4])

	for m in range(0, len(top_rec_hist[0])):
		hist_list[i][0][m].Draw("colz")
		hist_list[i][0][m].Divide(top_rec_hist[i][m])
		hist_list[i][0][m].Scale(1./hist_list[i][0][m].Integral())
		hist_list[i][0][m].Draw("colz")
		hist_list[i][0][m].SetMaximum(hist_list[i][0][m].GetMaximum()*1.1)
		hist_list[i][0][m].SetTitle("Ratio "+level+type1+" "+name_list[m][6:-14]+axis_labelling[m])
		c1.Print("./images/"+type1+"/2D_Plots/Ratio_"+name_list[0][5:-5]+"_"+output_name[m]+".pdf")


