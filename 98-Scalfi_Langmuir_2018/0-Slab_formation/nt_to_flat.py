import numpy as np
import math

motif=200
n=10

pol=np.loadtxt('cell_polar')
xyz=np.zeros((motif,3))

Ral=pol[5,0]

#reference circle on aluminium atoms
for atom in range(motif):
	xyz[atom,0]=pol[atom,1]*Ral
	xyz[atom,1]=Ral-pol[atom,0]
	xyz[atom,2]=pol[atom,2]

np.savetxt('flat_cell', xyz, fmt='%06.4f')
