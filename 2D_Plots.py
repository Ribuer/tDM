from ROOT import *
import sys
import string
import math as mt
from array import array

file_name = sys.argv[1]

open_file = TFile(file_name) 

c2 = TCanvas("canvas2", "Test2", 800, 600)
c3 = TCanvas("canvas3", "Test3", 800, 600)
c4 = TCanvas("canvas4", "Test4", 800, 600)
c5 = TCanvas("canvas5", "Test5", 800, 600)
c6 = TCanvas("canvas6", "Test6", 800, 600)

c2.cd()
met_topdphi.Draw("colz")
gStyle.SetOptStat(0)
met_topdphi.SetTitle(file_name[0:4]+" "+file_name[5:-5]+"; #Delta#Phi between #slash{E}_{t} and Top quark / .2; #slash{E}_{t} (GeV) / 20 (GeV)")
met_topdphi.GetXaxis().SetTitleOffset(1.2)
met_topdphi.GetYaxis().SetTitleOffset(1.2)
c2.Print(file_name[:-5]+"_Hadronic_2D_TopdPhiMet_MET.pdf")

c3.cd()
met_jet1pt.Draw("colz")
met_jet1pt.SetTitle(file_name[0:4]+" "+file_name[5:-5]+"; P_{t) (Leading jet) (GeV) / 20 (GeV); #slash{E}_{t} (GeV) / 20 (GeV)")
met_jet1pt.GetXaxis().SetTitleOffset(1.2)
met_jet1pt.GetYaxis().SetTitleOffset(1.2)
c3.Print(file_name[:-5]+"_Hadronic_2D_Jet1Pt_MET.pdf")

c4.cd()
met_bjet1pt.Draw("colz")
met_bjet1pt.SetTitle(file_name[0:4]+" "+file_name[5:-5]+"; P_{t} (Leading b-jet) (GeV) / 20 (GeV); #slash{E}_{t} (GeV) / 20 (GeV)")
met_bjet1pt.GetXaxis().SetTitleOffset(1.2)
met_bjet1pt.GetYaxis().SetTitleOffset(1.2)
c4.Print(file_name[:-5]+"_Hadronic_2D_BJet1Pt_MET.pdf")

c5.cd()
toppt_bjet1pt.Draw("colz")
toppt_bjet1pt.SetTitle(file_name[0:4]+" "+file_name[5:-5]+"; Top quark P_{t} (GeV) / 20 (GeV); P_{t} (Leading b-jet) (GeV) / 20 (GeV)")
toppt_bjet1pt.GetXaxis().SetTitleOffset(1.2)
toppt_bjet1pt.GetYaxis().SetTitleOffset(1.2)
c5.Print(file_name[:-5]+"_Hadronic_2D_TopPt_BJet1Pt.pdf")

c6.cd()
topphi_bjet1phi.Draw("colz")
topphi_bjet1phi.SetTitle(file_name[0:4]+" "+file_name[5:-5]+"; Top quark #Phi / .2; Highest P_{T} B-Jet, #Phi / .2")
topphi_bjet1phi.GetXaxis().SetTitleOffset(1.2)
topphi_bjet1phi.GetYaxis().SetTitleOffset(1.2)
c6.Print(file_name[:-5]+"_Hadronic_2D_TopPhi_BJet1Phi.pdf")
