import numpy as np
import argparse
import math
import pandas as pd


'''
calculation of Pore Size Distribusion by L-Sphere Method 
'''

'''
File needed 
sp_po.ini
cd_po.dat
'''

'''
file generated 
psd.dat
'''


def calculate_distance(Dcl, Ri, Rj):
	DisR = Ri - Rj
	if Ri > Rj:
		DisDM = DisR - Dcl
	else:
		DisDM = DisR + Dcl
	if abs(DisR) > abs(DisDM):
		DisR = DisDM
	Dist = DisR

def main():
	print('****************************************************')
	print('*      Calculation of Pore Size Distribution       *')
	print('****************************************************')
	print('')
	Kbm = int(input('(1) Bulk or (2) Membrane (z-direction) (-) ?  '))
	print('')
	Time1I = float(input('input Start Time (ps)  '))
	Time2I = float(input('input End Time (ps)  '))
	print('')
	Nlz = int(input('input the Number of Divided Lattice (z-direction) (-)  '))
	print('')
	RmaxI = float(input('input the Maximum of R (nm)  '))
	print('')
	Ndl = int(input('input the Number of Divided R-belt (-)  '))
	print('')
	
	pi = math.pi
	time1 = float(Time1I) - 12
	time2 = float(Time2I + 1.0 -5) -12
	Rmax = float(RmaxI) - 9
	
##--------------------------------Given Contents---------------------------------
##--------------------------------sp_po.ini--------------------------------
	df_init = pd.read_csv('sp_po_initialize.csv')
	# print(df_init)
	Npts = int(df_init.iat[0,0])
	Ncs = int(df_init.iat[1,0])
	IDmy = []
	Sigma = []
	for i in range(Ncs):
		IDmy.append(int(df_init.iat[i,2]))
		Sigma.append(float(df_init.iat[i,1]))
	celX = float(df_init.iat[0,3])
	celY = float(df_init.iat[1,3])
	celZ = float(df_init.iat[2,3])
	# print(Npts,Ncs,IDmy,Sigma,DcelX,DcelY,DcelZ)
	
	celXH = celX / 2.0
	celYH = celY / 2.0
	celZH = celZ / 2.0
	Vcel = celX*celY*celZ
	
##---------------------------------Lattice Configuration--------------------------------
	lat = celZ / float(Nlz)
	lath = lat / float(2.0)
	
	if celX > celZ:
		Nlx = Nlz + int((celX - celZ)/lat)
	elif celX < celZ:
		Nlx = Nlz - int((celZ - celX)/lat) - 1
	else:
		Nlx = Nlz
		
	if celY > celZ:
		Nly = Nlz + int((celY - celZ)/lat)
	elif celX < celZ:
		Nly = Nlz - int((celZ - celY)/lat) - 1
	else:
		Nly = Nlz
	
	Nlat = Nlx * Nly * Nlz
	Vlat = lat * lat * lat
	
	Xel = - (lat * float(Nlx)) / float(2.0)
	Yel = - (lat * float(Nly)) / float(2.0)
	Zel = - (lat * float(Nlz)) / float(2.0)
	Ilat = 0
	
	Clx = []
	Cly = []
	Clz = []
	
	for k in range(Nlz):
		for j in range(Nly):
			for i in range(Nlx):
				Ilat += 1
				Clx.append(Xel + lat * float(i) - lath)
				Cly.append(Yel + lat * float(j) - lath)
				Clz.append(Zel + lat * float(k) - lath)
				
##-----------------------------vdW Size parameters---------------
	ssh = []
	for i in range(Ncs):
		ssh.append(float(Sigma[i])-9/float(2.0))
	
##-----------------------------Constants for distribution -----------------

	Ndr = 50
	Rmax = float(1.0) - 8
	Rbl = []
	Rbr = []
	Vdr = []
	
	Dr = Rmax / float(Ndr)
	DRi = RmaxI / float(Ndr)
	
	for i in range(Ndr + 1):
		Rbl.append(float(i-1)*Dr)
		Rbr.append(float(i)*Dr)
		Vdr.append(float(0.0))
		
	print('Unit Cell Size x     ',np.float32(float(celX)+9),'(nm)')
	print('Unit Cell Size y     ',np.float32(float(celY)+9),'(nm)')
	print('Unit Cell Size z     ',np.float32(float(celZ)+9),'(nm)')
	
	for i in range(Ncs):
		print('Size of Molec. ', i+1,'(A.U.)',np.float32(Sigma[i]))
	print('Lattice Size.      ',np.float32(float(lat) + 9),'(nm)')
	print('Number of Lattice x     ',int(Nlx))
	print('Number of Lattice y     ',int(Nly))
	print('Number of Lattice z     ',int(Nlz))
	print('')
	
##-------------------------------------------------------------------------------
##                              Main Routine                      
##-------------------------------------------------------------------------------
	
		
	


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--alpha', type=float, default=0.01)
	main()