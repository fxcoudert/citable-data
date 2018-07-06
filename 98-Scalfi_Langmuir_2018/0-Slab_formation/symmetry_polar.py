import numpy as np
import math

motif=20
n=10 # number of gibbsite units in Cradwick's data

# Load crystallographic data from Cradwick et al.
pol=np.loadtxt('polar10')
pol[:,1]*=math.pi/180 # convert degrees in radians
xyz=np.zeros((n*motif,3))

for unit in range(n):
	#operation a
	pol[:,1]+=math.pi/n
	pol[:,2]=4.2-pol[:,2]
	for atom in range(10):
		xyz[motif*unit+atom,0]=pol[atom,0]
		xyz[motif*unit+atom,1]=pol[atom,1]
		xyz[motif*unit+atom,2]=pol[atom,2]
	
	#hole cylinder
	for atom in range(10):
		xyz[motif*unit+10+atom,0]=xyz[motif*unit+atom,0]	
		xyz[motif*unit+10+atom,1]=xyz[motif*unit+atom,1]+math.pi	
		xyz[motif*unit+10+atom,2]=xyz[motif*unit+atom,2]	

np.savetxt('cell_polar', xyz, fmt='%06.4f')
