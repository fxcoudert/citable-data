#!/bin/bash

source /usr/local/gromacs/bin/GMXRC

gmx grompp -f ../mdp/eql.mdp -c ../minimization/min2.gro -p ../prepare_system/topol.top -o eql.tpr -pp eql.top -po eql.mdp 
gmx mdrun -s eql.tpr -o eql.trr -x eql.xtc -c eql.gro -e eql.edr -g eql.log
