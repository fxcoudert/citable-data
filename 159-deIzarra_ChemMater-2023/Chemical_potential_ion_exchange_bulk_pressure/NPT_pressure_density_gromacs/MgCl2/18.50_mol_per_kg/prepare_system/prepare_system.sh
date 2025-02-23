#!/bin/bash

source /usr/local/gromacs/bin/GMXRC
gmx solvate -cs tip4p -o conf.gro -box 2.61 2.61 2.61 -p topol.top
gmx grompp -f ../mdp/min.mdp -c conf.gro -p topol.top -o ions.tpr
gmx genion -s ions.tpr -o conf.gro -p topol.top -pname MG -np 96 -nname CL -nn 192 -rmin 0.2
