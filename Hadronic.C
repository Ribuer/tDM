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
   
  //prints number or tree entries
  cout << "Entries " << nentries << endl;

  //Example of declaration of an histrogram. This particular histogram is used in particular to have the cut-flow of the selection
  //The selection here and later is just an example and not the full one used in the analysis
  TH1F *h_events = new TH1F("events",";;Events;log",6,0,6); h_events->Sumw2();
  h_events->GetXaxis()->SetBinLabel(1, "All");
  h_events->GetXaxis()->SetBinLabel(2, "leptons = 0");
  h_events->GetXaxis()->SetBinLabel(3, "jets #geq 4");
  h_events->GetXaxis()->SetBinLabel(4, "b jets #geq 2");
  h_events->GetXaxis()->SetBinLabel(5, "minDPhi > 1");
  h_events->GetXaxis()->SetBinLabel(6, "#slash{E_{T}} > 200 GeV");
  
  //Example: declaration of histrograms used to save for each event the value of a specific variable before any selection 
  //("_incl" stands for inclusive selection, i.e. no selection at all applied)
  TH1F *h_met_incl = new TH1F("met_incl",";#slash{E}_{t} (GeV);Events / (40 GeV);log",20,0,800); h_met_incl->Sumw2();
  TH1F *h_njet_incl = new TH1F("n_jet_incl",";Number of jets;Events",12,-0.5,11.5); h_njet_incl->Sumw2();

  //Example: declaration of histrograms used to save for each event the value of a specific variable at generator level
  TH1F *h_toppt = new TH1F("toppt",";top p_{t} (GeV);Events / (40 GeV);log",40,0,800); h_toppt->Sumw2();
  TH1F *h_antitoppt = new TH1F("antitoppt",";Antitop p_{t} (GeV);Events / (40 GeV);log",20,0,800); h_antitoppt->Sumw2();
  TH1F *h_medpt = new TH1F("medpt",";Mediator p_{t} (GeV);Events / (40 GeV);log",20,0,800); h_medpt->Sumw2();


  TH1F *h_met = new TH1F("met",";#slash{E}_{t} (GeV);Events / (40 GeV);log",25,0,1000); h_met->Sumw2();
  TH1F *h_jet1pt = new TH1F("jet1pt",";Leading jet p_{t} (GeV);Events / (40 GeV);log",30,0,1200); h_jet1pt->Sumw2();

  TH1F *h_met_sel = new TH1F("met_sel",";#slash{E}_{t} (GeV);Events / (40 GeV)",25,200,1200); h_met_sel->Sumw2();

  TH1F *h_bjet1pt = new TH1F("bjet1pt",";Leading bjet p_{t} (GeV);Events / (40 GeV);log",30,0,1200); h_jet1pt->Sumw2();
  TH1F *h_leptons = new TH1F("leptons",";#slash{E}_{t} (GeV);Events / (40 GeV);log",30,0,1200); h_leptons->Sumw2();
  TH1F *h_mindphi = new TH1F("mindphi",";MinDPhi;Events / (40 GeV);log",30,0,1200); h_mindphi->Sumw2();
  TH1F *h_mindphi_val = new TH1F("mindphi_val",";MinDPhi;Events / 0.2;log",20,0,4); h_mindphi_val->Sumw2();

  TH2F *h_met_topdphi = new TH2F("met_topdphi","", 17, 0, 3.4, 25, 0, 500); h_met_topdphi->Sumw2();
  TH2F *h_met_jet1pt = new TH2F("met_jet1pt", "", 35, 0, 700, 25, 0, 500); h_met_jet1pt->Sumw2();
  TH2F *h_met_bjet1pt = new TH2F("met_bjet1pt", "", 35, 0, 700, 25, 0, 500); h_met_bjet1pt->Sumw2();
  TH2F *h_toppt_bjet1pt = new TH2F("toppt_bjet1pt ", "", 35, 0, 700, 25, 0, 500); h_toppt_bjet1pt->Sumw2();
  TH2F *h_topphi_bjet1phi = new TH2F("topphi_bjet1phi  ", "", 17, 0, 3.4, 17, 0, 3.4); h_topphi_bjet1phi->Sumw2();


  for (Long64_t jentry=0; jentry<nentries;jentry++) {

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

    Float_t dphi = 0;
    Float_t dphi_jet = 0;
    
    float eventweight(1.);
    
    Float_t top_phi = 0;
    Float_t antitop_phi = 0;
    Float_t top_pt = 0;    
    Float_t antitop_pt = 0;

    Float_t dphi_tMET = 0;    
    Float_t min_dphi = 1000;
    Float_t min_dphi1 = 0;
    
    met =  MissingET_MET[0];
    
    //Loop over particles at generator level
    for (Int_t j=0; j < Particle_size; j++){
      
      //Check on PDGid and status of the particles at generator level
      //Particle_PID[j]==6 && Particle_Status[j]==3 is to select a top quark
      if(Particle_PID[j]==6 && Particle_Status[j]==3 ) {
	h_toppt->Fill(std::min(float(Particle_PT[j]), float(h_toppt->GetXaxis()->GetXmax()-0.1)), eventweight);
	top_phi = Particle_Phi[j];
	top_pt = Particle_PT[j];
      }

      //Check on PDGid and status of the particles at generator level
      //Particle_PID[j]==6 && Particle_Status[j]==3 is to select a anti top quark
      if(Particle_PID[j]==-6 && Particle_Status[j]==3 ) {
	h_antitoppt->Fill(std::min(float(Particle_PT[j]), float(h_antitoppt->GetXaxis()->GetXmax()-0.1)), eventweight);
	antitop_phi = Particle_Phi[j];
	antitop_pt = Particle_PT[j];
      }
      
      if(abs(Particle_PID[j])==1000000 && Particle_Status[j]==3) {
	h_medpt->Fill(std::min(float(Particle_PT[j]), float(h_medpt->GetXaxis()->GetXmax()-0.1)), eventweight);
	met_test = float(Particle_PT[j]); 
      }
    }

    //Loop over reconstructed electrons
    if( (sample.substr(0,3) == "ttD") ) {
	for (Int_t k=0; k < Electron_size; k++){
		if( (Electron_PT[k]>10. && std::abs(Electron_Eta[k])<2.5) ) n_lept += 1;
	}
    }
    else {
	for (Int_t k=0; k < Electron_size; k++){
		if( (Electron_PT[k]>10. && std::abs(Electron_Eta[k])<2.4) ) n_lept += 1;	    
        }
    }

    //Loop over reconstructed muons
    for (Int_t m=0; m < Muon_size; m++){
	if(Muon_PT[m]>10. && std::abs(Muon_Eta[m])<2.4 ) {
	n_lept += 1;
	}
    }

    //Calculation of delta phi between the top quark and MET at gen level
    dphi_tMET = top_phi - GenMissingET_Phi[0];
    while (dphi_tMET > M_PI) dphi_tMET -= 2*M_PI;
    while (dphi_tMET <= -M_PI) dphi_tMET += 2*M_PI;  
    dphi_tMET = std::abs(dphi_tMET); 
        
    //Example of selection applied to the jets
    //Loop over reconstructed jets 
    for (Int_t i=0; i < Jet_size; i++){

      //Apply analysis selection to jets. Only jets in the events satisfying the following conditions are considered as jets for the analysis
      if(std::abs(Jet_Eta[i])<4. && Jet_PT[i]>30) {
	//Increment number of jets found in the events that satisfy the quality selection 
	n_jet += 1;
	
	//Keep track of the index of the first jet that satisfy the requirement for later
	//Note that jets the jet array in the tree are ordered as a function of pt, 
	//i.e. the first element of the array is the jet in the event with the highest pt
	if(index_j1==-1) index_j1=i;

	if( std::abs(Jet_Eta[i])<2.4 && std::abs(Jet_BTag[i]==1) ) {
      	//Increment number of jets found in the events that satisfy the quality selection 
      	n_bjet += 1;
	
      	//Keep track of the index of the first bjet that satisfy the requirement for later
      	if(index_bj1==-1) index_bj1=i;
        }
	
      }
      
    }
    for (Int_t i=0; i < 6; i++){
	//if( (std::abs(Jet_Phi[i]-MissingET_Phi[0]) < min_dphi) ) min_dphi = std::abs(Jet_Phi[i]-MissingET_Phi[0]);
	
	min_dphi1 = Jet_Phi[i] - MissingET_Phi[0];
	while (min_dphi1 > M_PI) min_dphi1 -= 2*M_PI;
	while (min_dphi1 <= -M_PI) min_dphi1 += 2*M_PI;  
	min_dphi1 = std::abs(min_dphi1); 
	if( (min_dphi1 < min_dphi) ) min_dphi = min_dphi1;
    }

    //printf("%f\n", min_dphi1);
    //printf("%f\n", min_dphi);

    //Fill histograms - no selection
    h_events->Fill(0., eventweight);
    h_njet_incl->Fill(std::min(float(n_jet), float(h_njet_incl->GetXaxis()->GetXmax()-0.1)), eventweight);
    h_met_incl->Fill(std::min(float(met), float(h_met_incl->GetXaxis()->GetXmax()-0.1)), eventweight);

    h_met_topdphi->Fill(dphi_tMET, GenMissingET_MET[0]);
    h_met_jet1pt->Fill(GenJet_PT[index_j1], GenMissingET_MET[0]);
    h_met_bjet1pt->Fill(GenJet_PT[index_bj1], GenMissingET_MET[0]);
    h_toppt_bjet1pt->Fill(top_pt, GenJet_PT[index_bj1]);
    h_topphi_bjet1phi->Fill(top_phi, GenJet_Phi[index_bj1]);
    
    //Fill histograms - 0 leptons
    if ( !(n_lept == 0) ) continue;

    h_events->Fill(1., eventweight);
    h_leptons->Fill(std::min(float(met), float(h_leptons->GetXaxis()->GetXmax()-0.1)), eventweight);
    h_mindphi_val->Fill(std::min(float(min_dphi), float(h_mindphi_val->GetXaxis()->GetXmax()-0.1)), eventweight);

    //Fill histograms - #jets selection
    if( !(n_jet > 3) ) continue;

    h_events->Fill(2., eventweight);
    h_jet1pt->Fill(std::min(float(Jet_PT[index_j1]), float(h_jet1pt->GetXaxis()->GetXmax()-0.1)), eventweight);
    h_met->Fill(std::min(float(met), float(h_met->GetXaxis()->GetXmax()-0.1)), eventweight);

    //Fill histograms - #b jets selection
    if( !(n_bjet > 1) ) continue;

    h_events->Fill(3., eventweight);
    h_bjet1pt->Fill(std::min(float(Jet_PT[index_j1]), float(h_bjet1pt->GetXaxis()->GetXmax()-0.1)), eventweight);
    h_met->Fill(std::min(float(met), float(h_met->GetXaxis()->GetXmax()-0.1)), eventweight);

    //Fill histograms - mindphi selection
    if( !(min_dphi > 1.) ) continue;

    h_events->Fill(4., eventweight);
    h_mindphi->Fill(std::min(float(met), float(h_mindphi->GetXaxis()->GetXmax()-0.1)), eventweight);

    //Fill histograms - met selection
    if( !(met > 200.) ) continue;

    h_events->Fill(5., eventweight);
    h_met_sel->Fill(std::min(float(met), float(h_met_sel->GetXaxis()->GetXmax()-0.1)), eventweight);

    n_event += 1;
  }
  
  Double_t err = 0.;
  Double_t integral = h_met_sel->IntegralAndError(0,100,err);
  
  //Write the histrograms into a root file
  TFile *f = new TFile(("./output_root/"+sample+".root").c_str(),"RECREATE");
  f->cd();
  
  h_events->Write();
  
  h_met_incl->Write();
  h_njet_incl->Write();
  
  h_toppt->Write();
  h_antitoppt->Write();
  h_medpt->Write();
    
  h_met->Write();
  h_jet1pt->Write();
  h_bjet1pt->Write(); 	
  h_leptons->Write();
  h_mindphi_val->Write();
  h_mindphi->Write();
  h_met_topdphi->Write();
  h_met_jet1pt->Write();
  h_met_bjet1pt->Write();
  h_toppt_bjet1pt->Write();
  h_topphi_bjet1phi->Write();
  
  h_met_sel->Write();

  f->Close();
}
