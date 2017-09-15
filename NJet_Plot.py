from ROOT import *
import sys
import string
import math as mt
from array import array

color_list = [1, 633, 434, 402, 877, 419, 396, 628, 618, 882, 428, 612, 414, 596]

canvas1 = TCanvas("canvas1", "Test", 800, 600)
stack_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
stack_leg_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

select_list = [" after lepton veto", " after min#Delta#Phi selection", " after #slash{E}_{t} selection"]
select_print = ["Lept_vet", "MindPhi_sel", "MET_sel"]
axis_list = ["Number of jets", "Number of b-jets", "P_{t} (Leading Jet)", "P_{t} (Leading B-Jet)", "#Delta#Phi (MET, Leading b jet)"]
axis_print = ["Njets", "NBjets", "Jet1Pt", "BJet1Pt", "DPhi_MET_BJet"]

n_jet_lept = [0, 0, 0, 0]
n_jet_mindphi = [0, 0, 0, 0]
n_jet_met = [0, 0, 0, 0]
n_bjet_lept = [0, 0, 0, 0]
n_bjet_mindphi = [0, 0, 0, 0]
n_bjet_met = [0, 0, 0, 0]

jet_lept = [0, 0, 0, 0]
jet_mindphi = [0, 0, 0, 0]
jet_met = [0, 0, 0, 0]
bjet_lept = [0, 0, 0, 0]
bjet_mindphi = [0, 0, 0, 0]
bjet_met = [0, 0, 0, 0]

dphi_metbjet = [0, 0, 0, 0]

met_vs_jet_list = [0, 0, 0, 0]
met_vs_bjet_list = [0, 0, 0, 0]
top_list = [0, 0]


plot_list = [n_jet_lept, n_jet_mindphi, n_jet_met, n_bjet_lept, n_bjet_mindphi, n_bjet_met, jet_lept, jet_mindphi, jet_met, bjet_lept, bjet_mindphi, bjet_met, dphi_metbjet]

file_list = [0, 0, 0, 0]

scale_dict = {"ttDM_Mchi1Mphi10": 19.76, "topDM_Mchi1Mphi10_sChan_4F": 7.03e-2, "topDM_Mchi1Mphi10_tChan_4F": 27.18e-1, "topDM_Mchi1Mphi10_tWChan_5F": 73.25e-2}
name_list = ["ttDM", "s-Chan", "t-Chan", "tW-Chan"]
argv_list = [sys.argv[1], 0, 0, 0]
n_events = []

title = argv_list[0][5:-14]
type1 = argv_list[0][-13:-5]

argv_list[1] = argv_list[0].replace("tt", "top").replace(type1+".root", "sChan_4F_"+type1+".root")
argv_list[2] = argv_list[1].replace("s", "t")
argv_list[3] = argv_list[1].replace("s", "tW").replace("4F", "5F")

for i in range(0, len(stack_list)):
	selection = select_list[i % 3]
	axis = axis_list[int(i/3.)]
	if i == 12:
		selection = select_list[2]
	stack_list[i] = THStack("hs"+str(i),title+selection+";"+axis+" ; Events / 40 GeV")
	stack_leg_list[i] = TLegend(.70, .65, .88, .85)
	stack_leg_list[i].SetBorderSize(0)


for i in range(0, len(file_list)):
	file_list[i] = TFile(argv_list[i])

	n_events.append(events.GetBinContent(1))
	del events

	n_jet_lept[i] = njet_lept.Clone()		
	n_jet_mindphi[i] = njet_mindphi.Clone()
	n_jet_met[i] = njet_met.Clone()
	n_bjet_lept[i] = nbjet_lept.Clone()
	n_bjet_mindphi[i] = nbjet_mindphi.Clone()
	n_bjet_met[i] = nbjet_met.Clone()

	jet_lept[i] = jet1pt_lept.Clone()
	jet_mindphi[i] = jet1pt_mindphi.Clone()
	jet_met[i] = jet1pt_met.Clone()
	bjet_lept[i] = bjet1pt_lept.Clone()
	bjet_mindphi[i] = bjet1pt_mindphi.Clone()
	bjet_met[i] = bjet1pt_met.Clone()

	dphi_metbjet[i] = dphi_met_bjet.Clone()
	met_vs_jet_list[i] = met_jet1pt.Clone()
	met_vs_bjet_list[i] = met_bjet1pt.Clone()


	met_vs_jet_list[i].Scale(scale_dict[argv_list[i][:-14]]/n_events[i]*2.2e3)
	met_vs_bjet_list[i].Scale(scale_dict[argv_list[i][:-14]]/n_events[i]*2.2e3)

	del njet_lept, njet_mindphi, njet_met, nbjet_lept, nbjet_mindphi, nbjet_met, jet1pt_lept, jet1pt_mindphi, jet1pt_met, bjet1pt_lept, bjet1pt_mindphi, bjet1pt_met, dphi_met_bjet, met_jet1pt, met_bjet1pt

jet_range = [3, 7] #Adjust jet range for cut scenario testing
jetb_range = [0, 3]

stack_bin = [0]*jet_range[1]
tt_bin  = [0]*jet_range[1]
bin_comparison = [0]*jet_range[1]

stack_bin_b = [0]*jet_range[1]
tt_bin_b  = [0]*jet_range[1]
bin_comparison_b = [0]*jet_range[1]

for i in range(0, len(n_jet_lept)):
	for j in range(0, len(plot_list)):
		plot_list[j][i].SetLineColor(color_list[i])
		plot_list[j][i].Scale(scale_dict[argv_list[i][:-14]]/n_events[i]*2.2e3)
		if i == 0:
			stack_leg_list[j].AddEntry(plot_list[j][i], name_list[i], "l")
		else:
			stack_leg_list[j].AddEntry(plot_list[j][i], name_list[i], "f")
			stack_list[j].Add(plot_list[j][i])
			plot_list[j][i].SetFillColor(color_list[i])
			if j == 2:	#Jet_Met after full selection
				for k in range(jet_range[0], jet_range[1]):		#Choose range for Jet Comparison
					stack_bin[k-1] += plot_list[j][i].GetBinContent(k)
					if i == 1:
						tt_bin[k-1] += plot_list[j][0].GetBinContent(k)

			elif j == 5:	#BJet_Met after full selection
				for k in range(jetb_range[0], jetb_range[1]):		#Choose range for B Jet Comparison
					stack_bin_b[k-1] += plot_list[j][i].GetBinContent(k)
					if i == 1:
						tt_bin_b[k-1] += plot_list[j][0].GetBinContent(k)

canvas1.cd()
gPad.SetLogy()
gStyle.SetOptStat(0)	#hide statbox

for i in range(0, len(plot_list)):
	axis = axis_print[int(i/3.)]
	select = select_print[i % 3]

	if i == 12:
		select = select_print[2]
		axis = axis_print[4]
		
	stack_list[i].Draw("hist")
	plot_list[i][0].Draw("histsame")
	stack_leg_list[i].Draw("same")

	hs_max = stack_list[i].GetMaximum()
	if plot_list[i][0].GetMaximum() > hs_max:
		hs_max = plot_list[i][0].GetMaximum()

	stack_list[i].SetMaximum(hs_max)
	stack_list[i].SetMinimum(1e-2)

	canvas1.Print("./images/Hadronic/Jet_Plots/"+axis+"/"+title+"_"+axis+"_"+select+".pdf")

	del hs_max

for i in range(0, len(bin_comparison)):
	if abs(stack_bin[i]+tt_bin[i]) > 0:
		#if abs((stack_bin[i]-tt_bin[i])/(stack_bin[i]+tt_bin[i])) < 1:
		bin_comparison[i] = abs((stack_bin[i]-tt_bin[i])/(stack_bin[i]+tt_bin[i]))
	if abs(stack_bin_b[i]+tt_bin_b[i]) > 0:
		if abs((stack_bin_b[i]-tt_bin_b[i])/(stack_bin_b[i]+tt_bin_b[i])) < 1:
			bin_comparison_b[i] = abs((stack_bin_b[i]-tt_bin_b[i])/(stack_bin_b[i]+tt_bin_b[i]))

indices = [i for i,x in enumerate(bin_comparison) if x == max(bin_comparison)]
print "\nMax difference between tt and top in range ["+str(jet_range[0])+","+str(jet_range[1]-1)+"] Jets: \n# of Jets: ", indices[0]+1, " Bin_Value: ", bin_comparison[indices[0]] 

indices_b = [i for i,x in enumerate(bin_comparison_b) if x == max(bin_comparison_b)]
print "\nMax difference between tt and top in range ["+str(jetb_range[0])+","+str(jetb_range[1]-1)+"] BJets: \n# of B Jets: ", indices_b[0]+1, " Bin_Value: ", bin_comparison_b[indices_b[0]], "\n"

k = plot_list[2][0].Integral()
print "Ratio of cut events to initial events: ", k/(scale_dict[argv_list[0][:-14]]/n_events[0]*2.2e3)/n_events[0], "\n"

def print_2D(histo, interaction_type, variable):
	histo.Draw("colz")
	histo.SetTitle(interaction_type+" "+title+"; P_{t} (Leading "+variable+");#slash{E}_{t} / 20 GeV")
	histo.GetXaxis().SetTitleOffset(1.2)
	histo.GetYaxis().SetTitleOffset(1.2)
	histo.GetZaxis().SetTickSize(.01)
	gPad.SetLogz()
	gPad.SetLogy(False)
	canvas1.Update()	
	palette = histo.GetListOfFunctions().FindObject("palette")
	palette.SetX2NDC(.93)
	canvas1.Print("./images/Hadronic/Jet_Plots/2D_Plots/"+interaction_type+"_"+title+"_MET_"+variable+"Pt.pdf")

for j in range(1, 4):
	if j == 1:
		top_list[0] = met_vs_jet_list[j]
		top_list[1] = met_vs_bjet_list[j]
	else:
		top_list[0].Add(met_vs_jet_list[j])
		top_list[1].Add(met_vs_bjet_list[j])

print_2D(met_vs_jet_list[0], "ttDM", "Jet")
print_2D(met_vs_bjet_list[0], "ttDM", "BJet")
print_2D(top_list[0], "topDM", "Jet")
print_2D(top_list[1], "topDM", "BJet")
