import numpy as np
import math

from chemfiles import Trajectory, UnitCell, Atom, Topology, Frame, Selection
name='nt12-24-full.trj_wrap'  #name of the trajectory wrapped around the nanotube axis
a=24 #the a box length

# Read the traj
trajectory = Trajectory(name+'.xyz')

# Set the topology
topo = Trajectory("topology.pdb").read()
trajectory.set_topology(topo.topology())

# Select all
selection = Selection("all")

Ral=6.5

with Trajectory(name+'_flat.xyz','w') as output:
    for frame in trajectory:
        nt = selection.evaluate(frame)
        positions = frame.positions()

        for atom in nt:
            x=positions[atom][0]
            y=positions[atom][1]

            r=math.sqrt(x*x+y*y)
            theta=math.atan2(y,x)

            positions[atom,0]=theta*Ral
	    positions[atom,1]=Ral-r
  
        output.write(frame)

trajectory.close()
