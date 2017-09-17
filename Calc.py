import math as mt
from decimal import Decimal

scale_dict = {"ttDM_Mchi1Mphi10": 19.76, "topDM_Mchi1Mphi10_sChan_4F": 7.03e-2, "topDM_Mchi1Mphi10_tChan_4F": 27.18e-1, "topDM_Mchi1Mphi10_tWChan_5F": 73.25e-2}
scale_list = [19.76, 7.03e-2, 27.18e-1, 73.25e-2]

tot_events = 51217.76
lumi = 2.2e3
n_events = [200000.0, 200000.0, 128832.0, 200000.0]

n_jets = [3, 4, 5, 6]
n_bjets = [1, 2]

values = [[140, 171, 29, 31, 393, 542, 134, 149, 124, 168, 44, 44, 253, 371, 105, 118, 72, 107, 29, 35, 129, 203, 61, 74, 42, 60, 13, 18, 57, 96, 32, 39],[134, 180, 43, 46, 239, 351, 97, 112, 74, 114, 34, 40, 105, 171, 54, 66, 25, 42, 15, 17, 31, 57, 20, 26, 5, 10, 4, 5, 6, 15, 5, 9],[201, 242, 41, 41, 461, 594, 126, 133, 165, 213, 44, 48, 260, 352, 85, 92, 62, 87, 24, 25, 95, 139, 41, 44, 17, 30, 11, 13, 33, 52, 17, 19],[343, 371, 26, 28, 990, 1181, 170, 191, 346, 408, 60, 62, 647, 810, 144, 163, 195, 255, 50, 60, 301, 402, 84, 101, 72, 98, 21, 26, 106, 147, 34, 41]]



for l in range(0, 2):
	if l == 0:
		print "\nttDM: \n"
	else: 
		print "\ntopDM: \n"
	for k in range(0, len(n_jets)):
		for i in range(0, len(n_bjets)*4):
			if l == 0:
				print '%.3E' % Decimal(values[l][k*(len(n_bjets)*4)+i]*scale_list[l]/n_events[l]*lumi/tot_events)
			else:
				stack = values[l][k*(len(n_bjets)*4)+i]*scale_list[l]/n_events[l]*lumi/tot_events+values[l+1][k*(len(n_bjets)*4)+i]*scale_list[l+1]/n_events[l+1]*lumi/tot_events+values[l+2][k*(len(n_bjets)*4)+i]*scale_list[l+2]/n_events[l+2]*lumi/tot_events
				print '%.3E' % Decimal(stack)



#print 29*19.76/2e5*lumi/tot_events
