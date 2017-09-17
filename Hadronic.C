#define Hadronic_cxx
#include "Hadronic.h"
#include <TH2.h>
#include <TH1.h>
#include <TStyle.h>
#include <TCanvas.h>
#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream> 
#include "TROOT.h"
#include "TRint.h"

void Hadronic::Loop()
{
	gROOT->SetBatch();

	if (fChain == 0) return;

	Long64_t nentries = fChain->GetEntriesFast();
	Long64_t nbytes = 0, nb = 0;

	Float_t met = 0;
	Float_t met_phi = 0;
	Float_t met_test = 0;
	UInt_t csv = 0;
	Int_t n_event = 0;

/*
	Int_t jeq3_beq1 = 0;
	Int_t jeq3_beq2 = 0;
	Int_t jeq3_bgeq1 = 0;
	Int_t jeq3_bgeq2 = 0;

	Int_t jgeq3_beq1 = 0;
	Int_t jgeq3_beq2 = 0;
	Int_t jgeq3_bgeq1 = 0;
	Int_t jgeq3_bgeq2 = 0;


	Int_t jeq4_beq1 = 0;
	Int_t jeq4_beq2 = 0;
	Int_t jeq4_bgeq1 = 0;
	Int_t jeq4_bgeq2 = 0;

	Int_t jgeq4_beq1 = 0;
	Int_t jgeq4_beq2 = 0;
	Int_t jgeq4_bgeq1 = 0;
	Int_t jgeq4_bgeq2 = 0;

	Int_t jeq5_beq1 = 0;
	Int_t jeq5_beq2 = 0;
	Int_t jeq5_bgeq1 = 0;
	Int_t jeq5_bgeq2 = 0;

	Int_t jgeq5_beq1 = 0;
	Int_t jgeq5_beq2 = 0;
	Int_t jgeq5_bgeq1 = 0;
	Int_t jgeq5_bgeq2 = 0;

	Int_t jeq6_beq1 = 0;
	Int_t jeq6_beq2 = 0;
	Int_t jeq6_bgeq1 = 0;
	Int_t jeq6_bgeq2 = 0;

	Int_t jgeq6_beq1 = 0;
	Int_t jgeq6_beq2 = 0;
	Int_t jgeq6_bgeq1 = 0;
	Int_t jgeq6_bgeq2 = 0;
*/
	   
	//prints number or tree entries
	cout << "Entries " << nentries << endl;

	//Example of declaration of an histrogram. This particular histogram is used in particular to have the cut-flow of the selection
	//The selection here and later is just an example and not the full one used in the analysis
	TH1F *h_events = new TH1F("events",";;Events;log",4,0,4); h_events->Sumw2();
	h_events->GetXaxis()->SetBinLabel(1, "All");
	h_events->GetXaxis()->SetBinLabel(2, "leptons = 0");
	h_events->GetXaxis()->SetBinLabel(3, "minDPhi > 1");
	h_events->GetXaxis()->SetBinLabel(4, "#slash{E_{T}} > 200 GeV");
	  
	//Example: declaration of histrograms used to save for each event the value of a specific variable before any selection 
	//("_incl" stands for inclusive selection, i.e. no selection at all applied)
	TH1F *h_met_incl = new TH1F("met_incl",";#slash{E}_{t} (GeV);Events / (40 GeV);log",30,0,1200); h_met_incl->Sumw2();
	TH1F *h_met_lept = new TH1F("met_lept",";#slash{E}_{t} (GeV);Events / (40 GeV);log",30,0,1200); h_met_lept->Sumw2();
	TH1F *h_mindphi_sel = new TH1F("mindphi_sel",";MinDPhi;Events / (40 GeV);log",30,0,1200); h_mindphi_sel->Sumw2();
	TH1F *h_met_sel = new TH1F("met_sel",";#slash{E}_{t} (GeV);Events / (40 GeV)",30,0,1200); h_met_sel->Sumw2();

	TH1F *h_njet_lept = new TH1F("njet_lept",";Number of jets;Events",12,0,12); h_njet_lept->Sumw2();
	TH1F *h_njet_mindphi = new TH1F("njet_mindphi",";Number of jets;Events",12,0,12); h_njet_mindphi->Sumw2();
	TH1F *h_njet_met = new TH1F("njet_met",";Number of jets;Events",12,0,12); h_njet_met->Sumw2();
	TH1F *h_nbjet_lept = new TH1F("nbjet_lept",";Number of jets;Events",8,0,8); h_nbjet_lept->Sumw2();
	TH1F *h_nbjet_mindphi = new TH1F("nbjet_mindphi",";Number of jets;Events",8,0,8); h_nbjet_mindphi->Sumw2();
	TH1F *h_nbjet_met = new TH1F("nbjet_met",";Number of jets;Events",8,0,8); h_nbjet_met->Sumw2();

	//Example: declaration of histrograms used to save for each event the value of a specific variable at generator level
	TH1F *h_jet1pt_lept = new TH1F("jet1pt_lept",";Leading jet p_{t} (GeV);Events / (40 GeV);log",30,0,1200); h_jet1pt_lept->Sumw2();
	TH1F *h_jet1pt_mindphi = new TH1F("jet1pt_mindphi",";Leading jet p_{t} (GeV);Events / (40 GeV);log",30,0,1200); h_jet1pt_mindphi->Sumw2();
	TH1F *h_jet1pt_met = new TH1F("jet1pt_met",";Leading jet p_{t} (GeV);Events / (40 GeV);log",30,0,1200); h_jet1pt_met->Sumw2();

	TH1F *h_bjet1pt_lept = new TH1F("bjet1pt_lept",";Leading b-jet p_{t} (GeV);Events / (40 GeV);log",30,0,1200); h_bjet1pt_lept->Sumw2();
	TH1F *h_bjet1pt_mindphi = new TH1F("bjet1pt_mindphi",";Leading b-jet p_{t} (GeV);Events / (40 GeV);log",30,0,1200); h_bjet1pt_mindphi->Sumw2();
	TH1F *h_bjet1pt_met = new TH1F("bjet1pt_met",";Leading b-jet p_{t} (GeV);Events / (40 GeV);log",30,0,1200); h_bjet1pt_met->Sumw2();

	TH1F *h_mindphi = new TH1F("mindphi",";min#Delta#Phi (Jets, MET);Events / 0.2;log",20,0,4); h_mindphi->Sumw2();
	TH1F *h_dphi_met_bjet = new TH1F("dphi_met_bjet",";#Delta#Phi (MET, leading B Jet); Events / 0.2; log",20, 0, 4); h_dphi_met_bjet->Sumw2();

	TH1F *h_jet1pt_eta = new TH1F("jet1pt_eta","; p_{t} (leading jet); Events / 0.2; log",50, -5, 5); h_jet1pt_eta->Sumw2();
	TH1F *h_bjet1pt_eta = new TH1F("bjet1pt_eta","; p_{t} (leading b jet); Events / 0.2; log",50, -5, 5); h_bjet1pt_eta->Sumw2();

	TH2F *h_met_jet1pt = new TH2F("met_jet1pt","", 35, 30, 730, 25, 0, 500); h_met_jet1pt->Sumw2();
	TH2F *h_met_bjet1pt = new TH2F("met_bjet1pt", "", 35, 30, 730, 25, 0, 500); h_met_bjet1pt->Sumw2();

	for (Long64_t jentry=0; jentry<nentries;jentry++) 
	{
		Long64_t ientry = LoadTree(jentry);
		if (ientry < 0) break;
		nb = fChain->GetEntry(jentry);   
		nbytes += nb;
		   
		if(jentry % 1000 == 0) std::cout << "Events processed: " << jentry << std::endl;
		     	
		fChain->GetEntry(jentry);
		    
		Int_t n_jet = 0;
		Int_t n_bjet = 0;
		Int_t n_lept = 0;
		    
		Int_t index_j1 = -1;
		Int_t index_bj1 = -1;
		    
		float eventweight(1.);

		Float_t min_dphi = 1000;
		Float_t min_dphi1 = 0;
		Float_t dphi_met_bjet = -1;
		    
		met =  MissingET_MET[0];
		    
		//Loop over reconstructed electrons
		for (Int_t k=0; k < Electron_size; k++)
		{
			if( (Electron_PT[k]>10. && std::abs(Electron_Eta[k])<2.5) ) n_lept += 1;
		}

		//Loop over reconstructed muons
		for (Int_t m=0; m < Muon_size; m++)
		{
			if(Muon_PT[m]>10. && std::abs(Muon_Eta[m])<2.5 ) n_lept += 1;
		}

		//Example of selection applied to the jets
		//Loop over reconstructed jets 
		for (Int_t i=0; i < Jet_size; i++)
		{
			//Apply analysis selection to jets. Only jets in the events satisfying the following conditions are considered as jets for the analysis
			if(std::abs(Jet_Eta[i])<4. && Jet_PT[i]>30) 	//4
			{
				//Increment number of jets found in the events that satisfy the quality selection 
				n_jet += 1;

				if( (n_jet <= 6) ) 
				{
					min_dphi1 = Jet_Phi[i] - MissingET_Phi[0];
					while (min_dphi1 > M_PI) min_dphi1 -= 2*M_PI;
					while (min_dphi1 <= -M_PI) min_dphi1 += 2*M_PI;  
					min_dphi1 = std::abs(min_dphi1); 
					if( (min_dphi1 < min_dphi) ) min_dphi = min_dphi1;
				}
	
				//Keep track of the index of the first jet that satisfy the requirement for later
				//Note that jets the jet array in the tree are ordered as a function of pt, 
				//i.e. the first element of the array is the jet in the event with the highest pt
				if(index_j1==-1) index_j1=i;

				if( std::abs(Jet_Eta[i])<2.4 && std::abs(Jet_BTag[i]==1) )  //2.4
				{
					//Increment number of jets found in the events that satisfy the quality selection 
					n_bjet += 1;
	
					//Keep track of the index of the first bjet that satisfy the requirement for later
					if(index_bj1==-1) index_bj1=i;

					dphi_met_bjet = Jet_Phi[i] - MissingET_Phi[0];
					while (dphi_met_bjet > M_PI) dphi_met_bjet -= 2*M_PI;
					while (dphi_met_bjet <= -M_PI) dphi_met_bjet += 2*M_PI;  
					dphi_met_bjet = std::abs(dphi_met_bjet); 
				}
		    	}
		}

		//Fill histograms - no selection
		h_events->Fill(0., eventweight);
		h_met_incl->Fill(std::min(float(met), float(h_met_incl->GetXaxis()->GetXmax()-0.1)), eventweight);

		if( n_jet > 0 ) 
		{
			h_met_jet1pt->Fill(float(Jet_PT[index_j1]), float(met));
			if( n_bjet > 0)	h_met_bjet1pt->Fill(float(Jet_PT[index_bj1]), float(met));
		}
		   
		//Fill histograms - 0 leptons
		if ( !(n_lept == 0) ) continue;

		h_events->Fill(1., eventweight);
		h_met_lept->Fill(std::min(float(met), float(h_met_lept->GetXaxis()->GetXmax()-0.1)), eventweight);
		h_mindphi->Fill(std::min(float(min_dphi), float(h_mindphi->GetXaxis()->GetXmax()-0.1)), eventweight);

		h_njet_lept->Fill(std::min(float(n_jet), float(h_njet_lept->GetXaxis()->GetXmax()-0.1)), eventweight);	
		h_nbjet_lept->Fill(std::min(float(n_bjet), float(h_nbjet_lept->GetXaxis()->GetXmax()-0.1)), eventweight);	
		h_jet1pt_lept->Fill(std::min(float(Jet_PT[index_j1]), float(h_jet1pt_lept->GetXaxis()->GetXmax()-0.1)), eventweight);
		h_bjet1pt_lept->Fill(std::min(float(Jet_PT[index_j1]), float(h_bjet1pt_lept->GetXaxis()->GetXmax()-0.1)), eventweight);
		
		if( n_jet > 0) h_jet1pt_eta->Fill(std::min(float(Jet_Eta[index_j1]), float(h_jet1pt_eta->GetXaxis()->GetXmax()-0.1)), eventweight);
		if( n_bjet > 0) h_bjet1pt_eta->Fill(std::min(float(Jet_Eta[index_bj1]), float(h_bjet1pt_eta->GetXaxis()->GetXmax()-0.1)), eventweight);
		

		//Fill histograms - #jets selection
		//if( !(n_jet == 3) ) continue;

		//Fill histograms - #jets selection
		//if( !(n_bjet > 1) ) continue;


		//Fill histograms - mindphi selection
		if( !(min_dphi > 1.) ) continue;

		h_events->Fill(2., eventweight);
		h_mindphi_sel->Fill(std::min(float(met), float(h_mindphi_sel->GetXaxis()->GetXmax()-0.1)), eventweight);

		h_njet_mindphi->Fill(std::min(float(n_jet), float(h_njet_mindphi->GetXaxis()->GetXmax()-0.1)), eventweight);	
		h_nbjet_mindphi->Fill(std::min(float(n_bjet), float(h_nbjet_mindphi->GetXaxis()->GetXmax()-0.1)), eventweight);	
		h_jet1pt_mindphi->Fill(std::min(float(Jet_PT[index_j1]), float(h_jet1pt_mindphi->GetXaxis()->GetXmax()-0.1)), eventweight);
		h_bjet1pt_mindphi->Fill(std::min(float(Jet_PT[index_j1]), float(h_bjet1pt_mindphi->GetXaxis()->GetXmax()-0.1)), eventweight);


		//Fill histograms - met selection
		if( !(met > 200.) ) continue;

		h_events->Fill(3., eventweight);
		h_met_sel->Fill(std::min(float(met), float(h_met_sel->GetXaxis()->GetXmax()-0.1)), eventweight);

		h_njet_met->Fill(std::min(float(n_jet), float(h_njet_met->GetXaxis()->GetXmax()-0.1)), eventweight);	
		h_nbjet_met->Fill(std::min(float(n_bjet), float(h_nbjet_met->GetXaxis()->GetXmax()-0.1)), eventweight);	
		h_jet1pt_met->Fill(std::min(float(Jet_PT[index_j1]), float(h_jet1pt_met->GetXaxis()->GetXmax()-0.1)), eventweight);
		h_bjet1pt_met->Fill(std::min(float(Jet_PT[index_j1]), float(h_bjet1pt_met->GetXaxis()->GetXmax()-0.1)), eventweight);

		if( dphi_met_bjet > -1 ) h_dphi_met_bjet->Fill(std::min(float(dphi_met_bjet), float(h_dphi_met_bjet->GetXaxis()->GetXmax()-0.1)), eventweight);

		n_event += 1;

/*
		if( n_jet == 3) 
		{
			if( n_bjet == 1) jeq3_beq1 += 1;
			else if( n_bjet == 2) jeq3_beq2 += 1;
			if( n_bjet > 0 ) jeq3_bgeq1 += 1;
			if( n_bjet > 1) jeq3_bgeq2 += 1;
		}
		if( n_jet > 2) 
		{
			if( n_bjet == 1) jgeq3_beq1 += 1;
			else if( n_bjet == 2) jgeq3_beq2 += 1;
			if( n_bjet > 0 ) jgeq3_bgeq1 += 1;
			if( n_bjet > 1) jgeq3_bgeq2 += 1;
		}

		if( n_jet == 4) 
		{
			if( n_bjet == 1) jeq4_beq1 += 1;
			else if( n_bjet == 2) jeq4_beq2 += 1;
			if( n_bjet > 0 ) jeq4_bgeq1 += 1;
			if( n_bjet > 1) jeq4_bgeq2 += 1;
		}
		if( n_jet > 3) 
		{
			if( n_bjet == 1) jgeq4_beq1 += 1;
			else if( n_bjet == 2) jgeq4_beq2 += 1;
			if( n_bjet > 0 ) jgeq4_bgeq1 += 1;
			if( n_bjet > 1) jgeq4_bgeq2 += 1;
		}
		if( n_jet == 5) 
		{
			if( n_bjet == 1) jeq5_beq1 += 1;
			else if( n_bjet == 2) jeq5_beq2 += 1;
			if( n_bjet > 0 ) jeq5_bgeq1 += 1;
			if( n_bjet > 1) jeq5_bgeq2 += 1;
		}
		if( n_jet > 4) 
		{
			if( n_bjet == 1) jgeq5_beq1 += 1;
			else if( n_bjet == 2) jgeq5_beq2 += 1;
			if( n_bjet > 0 ) jgeq5_bgeq1 += 1;
			if( n_bjet > 1) jgeq5_bgeq2 += 1;
		}
		if( n_jet == 6) 
		{
			if( n_bjet == 1) jeq6_beq1 += 1;
			else if( n_bjet == 2) jeq6_beq2 += 1;
			if( n_bjet > 0 ) jeq6_bgeq1 += 1;
			if( n_bjet > 1) jeq6_bgeq2 += 1;
		}
		if( n_jet > 5) 
		{
			if( n_bjet == 1) jgeq6_beq1 += 1;
			else if( n_bjet == 2) jgeq6_beq2 += 1;
			if( n_bjet > 0 ) jgeq6_bgeq1 += 1;
			if( n_bjet > 1) jgeq6_bgeq2 += 1;
		}
*/

	}

/*	cout << "J = 3, BJ = 1 " << jeq3_beq1 << endl;
	cout << "J = 3, BJ >= 1 " << jeq3_bgeq1 << endl;
	cout << "J = 3, BJ = 2 " << jeq3_beq2 << endl;
	cout << "J = 3, BJ >= 2 " << jeq3_bgeq2 << endl;
	cout << "J >= 3, BJ = 1 " << jgeq3_beq1 << endl;
	cout << "J >= 3, BJ >= 1 " << jgeq3_bgeq1 << endl;
	cout << "J >= 3, BJ = 2 " << jgeq3_beq2 << endl;
	cout << "J >= 3, BJ >= 2 " << jgeq3_bgeq2 << endl;

	cout << "J = 4, BJ = 1 " << jeq4_beq1 << endl;
	cout << "J = 4, BJ >= 1 " << jeq4_bgeq1 << endl;
	cout << "J = 4, BJ = 2 " << jeq4_beq2 << endl;
	cout << "J = 4, BJ >= 2 " << jeq4_bgeq2 << endl;
	cout << "J >= 4, BJ = 1 " << jgeq4_beq1 << endl;
	cout << "J >= 4, BJ >= 1 " << jgeq4_bgeq1 << endl;
	cout << "J >= 4, BJ = 2 " << jgeq4_beq2 << endl;
	cout << "J >= 4, BJ >= 2 " << jgeq4_bgeq2 << endl;

	cout << "J = 5, BJ = 1 " << jeq5_beq1 << endl;
	cout << "J = 5, BJ >= 1 " << jeq5_bgeq1 << endl;
	cout << "J = 5, BJ = 2 " << jeq5_beq2 << endl;
	cout << "J = 5, BJ >= 2 " << jeq5_bgeq2 << endl;
	cout << "J >= 5, BJ = 1 " << jgeq5_beq1 << endl;
	cout << "J >= 5, BJ >= 1 " << jgeq5_bgeq1 << endl;
	cout << "J >= 5, BJ = 2 " << jgeq5_beq2 << endl;
	cout << "J >= 5, BJ >= 2 " << jgeq5_bgeq2 << endl;

	cout << "J = 6, BJ = 1 " << jeq6_beq1 << endl;
	cout << "J = 6, BJ >= 1 " << jeq6_bgeq1 << endl;
	cout << "J = 6, BJ = 2 " << jeq6_beq2 << endl;
	cout << "J = 6, BJ >= 2 " << jeq6_bgeq2 << endl;
	cout << "J >= 6, BJ = 1 " << jgeq6_beq1 << endl;
	cout << "J >= 6, BJ >= 1 " << jgeq6_bgeq1 << endl;
	cout << "J >= 6, BJ = 2 " << jgeq6_beq2 << endl;
	cout << "J >= 6, BJ >= 2 " << jgeq6_bgeq2 << endl;
*/
	Double_t err = 0.;
	Double_t integral = h_met_sel->IntegralAndError(0,100,err);
		  
	//Write the histrograms into a root file
	TFile *f = new TFile(("./output_root/"+sample+"_Hadronic.root").c_str(),"RECREATE");
	f->cd();

	h_events->Write();

	//Miscellaneous		
	h_mindphi->Write(); 			
	h_njet_lept->Write();		
	h_njet_mindphi->Write();			
	h_njet_met->Write();
	h_nbjet_lept->Write();		
	h_nbjet_mindphi->Write();			
	h_nbjet_met->Write();	
	h_dphi_met_bjet->Write();				

	//Leading jets
	h_jet1pt_lept->Write();	
	h_jet1pt_mindphi->Write();	
	h_jet1pt_met->Write();							
	h_bjet1pt_lept->Write();	
	h_bjet1pt_mindphi->Write();	
	h_bjet1pt_met->Write();		

	h_jet1pt_eta->Write();
	h_bjet1pt_eta->Write();	
		
	//Met after cuts  
	h_met_incl->Write();			
	h_met_lept->Write();			
	h_mindphi_sel->Write();			
	h_met_sel->Write();			

	//2D plots before cuts		 
	h_met_jet1pt->Write();				
	h_met_bjet1pt->Write();			


	f->Close();
}
