# Script to fold the slab into a nanotube of the desired diameter
# The output needs post processing, it only contains the xyz coordinates
# as in atoms.dat file

import numpy as np
import math

motif=28
n=16 #number of gibbsite units in the circumference
a=4.90204967
b=8.48600143
c=20.0000000

slab=np.loadtxt('slab_'+str(n)+'_HB1')
xyz=np.zeros((motif*n,3))

Rnt=n*a/(2*math.pi)

#reference circle on aluminium atoms
for atom in range(n*motif):
	xyz[atom,0]=(Rnt+slab[atom,2])*math.cos(slab[atom,0]/Rnt)
	xyz[atom,1]=(Rnt+slab[atom,2])*math.sin(slab[atom,0]/Rnt)
	xyz[atom,2]=slab[atom,1]

np.savetxt('nanotube_'+str(n)+'_HB1', xyz, fmt='%06.4f')
