from ROOT import *
import sys
import string
import math as mt
from array import array

#Xsec upper limits

case1 = ["S", "Pseudos"]

mu_obs = [0.82, 1.5, 1.8, 2.2, 3.6, 6.4],[2.0, 2.2, 1.9, 2.0, 3.9, 4.9]	#[Scalar][Pseudo]
mu_exp = [.7, .8, 1.2, 2.3, 4.6, 8.7],[2.0, 2.2, 2.1, 2.6, 4.2, 6.3]

sigma1 = [[.45, .53, .85, 1.6, 3.2, 6.0],[1.1, 1.2, 1.9, 3.4, 6.9, 13]],[[1.4, 1.6, 1.5, 1.8, 2.9, 4.3],[3.0, 3.3, 3.1, 3.9, 6.3, 9.4]]		#[[-1sigma],[+1sigma]]
sigma2 = [[.32, .38, .62, 1.1, 2.4, 4.4],[1.8, 1.9, 2.8, 5.0, 9.8, 18]],[[1.0, 1.1, 1.1, 1.3, 2.1, 3.1],[4.4, 4.8, 4.5, 5.6, 9.3, 14]]

mass_points = array("d", [10-10e-10, 10, 20, 50, 100, 200, 300, 300+10e-10]) #Starting and end values for "fill"
mass_points_lower = array("d", [10-10e-9, 10, 20, 50, 100, 200, 300, 301])

for k in range(0, len(case1)):
	case = case1[k]

	g_obs = [mt.sqrt(mu_obs[k][0])]	#Starting values for "fill"
	g_exp = [mt.sqrt(mu_exp[k][0])]

	g_sig1 = [[0.5],[0.5]]
	g_sig2 = [[0.45],[0.5]]

	for i in range(0, len(mu_obs[k])):
		g_obs.append(mt.sqrt(mu_obs[k][i]))
		g_exp.append(mt.sqrt(mu_exp[k][i]))
		g_sig1[0].append(mt.sqrt(sigma1[k][0][i]))
		g_sig1[1].append(mt.sqrt(sigma1[k][1][i]))
		g_sig2[0].append(mt.sqrt(sigma2[k][0][i]))
		g_sig2[1].append(mt.sqrt(sigma2[k][1][i]))

	g_obs.append(g_obs[-1])		#Ending values for "fill"
	g_exp.append(g_exp[-1])
	g_sig1[0].append(0.5)
	g_sig1[1].append(0.5)
	g_sig2[0].append(0.45)
	g_sig2[1].append(0.5)

	g_obsarr = array("d", g_obs)
	g_exparr = array("d", g_exp)
	g_sig1_down= array("d", g_sig1[0])
	g_sig1_up = array("d", g_sig1[1])
	g_sig2_down = array("d", g_sig2[0])
	g_sig2_up = array("d", g_sig2[1])

	c1 = TCanvas("canvas", "TGraph", 800, 600)

	line1 = TGraph(len(mass_points), mass_points, g_sig2_up)
	line1.SetLineColor(kYellow)
	line1.SetFillColor(kYellow)

	line2 = TGraph(len(mass_points), mass_points, g_sig1_up)
	line2.SetLineColor(kGreen)
	line2.SetFillColor(kGreen)

	obs = TGraph(len(mass_points), mass_points, g_obsarr)
	obs.SetMarkerStyle(20)

	exp = TGraph(len(mass_points), mass_points, g_exparr)
	exp.SetLineColor(kRed)
	exp.SetLineStyle(3)

	line3 = TGraph(len(mass_points), mass_points, g_sig1_down)
	line3.SetLineColor(kYellow)
	line3.SetFillColor(kYellow)

	line4 = TGraph(len(mass_points), mass_points_lower, g_sig2_down)
	line4.SetLineColor(kWhite)
	line4.SetFillColor(kWhite)

	leg = TLegend(.15, .5, .5, .85)
	leg.SetBorderSize(0)
	leg.AddEntry(exp, "Median expected 95% CL", "l")
	leg.AddEntry(line2, "Expected #pm 1#sigma", "f")
	leg.AddEntry(line1, "Expected #pm 2#sigma", "f")
	leg.AddEntry(obs, "Observed", "lp")
	leg.SetHeader(case+"calar, Dirac, m_{#chi}=1 GeV")

	line1.SetTitle("2.2 fb -1 (13 TeV); M_{#Phi} (GeV); Upper limit on g assuming g_{ #chi} = g_{q}") #Change title name
	line1.GetYaxis().SetTitleOffset(1.2)
	line1.GetXaxis().SetRangeUser(0, 310)
	c1.SetLogx()
	c1.SetTicks(1,1)
	gStyle.SetTitleY(.95)
	gStyle.SetTitleX(.8)
	gStyle.SetTitleH(.04)
	gStyle.SetTitleW(.25)

	line1.Draw("AF")
	line2.Draw("F")
	obs.Draw("P")
	obs.Draw("same")
	exp.Draw("same")
	line3.Draw("F")
	line4.Draw("F")
	leg.Draw("same")

	c1.Print("Limit_Coupling_"+case+"calar.pdf")

	del c1, g_obsarr











