# Script to form a slab of the wright dimension to be folded

import numpy as np

n=16 #number of gibbsite units in the circumference
a=4.90204967
b=8.48600143
c=20.0000000
shift=1.029151 #in angstroms

coord=np.loadtxt('slab_crys_HB1')

coord[:,2]+=shift/c

coordC=np.zeros(coord.shape)
coordC[:,0]=coord[:,0]+0.5
coordC[:,1]=coord[:,1]+0.5
coordC[:,2]=coord[:,2]

coord[:,0]*=a
coord[:,1]*=b
coord[:,2]*=c

coordC[:,0]*=a
coordC[:,1]*=b
coordC[:,2]*=c

centered=np.concatenate((coord, coordC), axis=0)

fin=np.zeros((centered.shape))
fin[:,:]=centered[:,:]

for unit in range(n-1):
	centered[:,0]+=a
	fin=np.concatenate((fin,centered),axis=0)

np.savetxt('slab_'+str(n)+'_HB1',fin, fmt='%10.8f')
