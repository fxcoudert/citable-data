#!/bin/bash

source /usr/local/gromacs/bin/GMXRC

gmx grompp -f ../mdp/min.mdp -p ../prepare_system/topol.top -c ../prepare_system/conf.gro -o min.tpr -pp min.top -po min.mdp
gmx mdrun -s min.tpr -o min.trr -x min.xtc -c min.gro -e min.edr -g min.log

gmx grompp -f ../mdp/min2.mdp -p ../prepare_system/topol.top -o min2.tpr -pp min2.top -po min2.mdp -c min.gro
gmx mdrun -s min2.tpr -o min2.trr -x min2.xtc -c min2.gro -e min2.edr -g min2.log
