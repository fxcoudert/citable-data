#!/bin/bash

box=(24.2 25.7 27.3 30.5)
dossier=(1-NT12 2-NT13 3-NT14 4-NT16)
subdossier=(1-Empty  2-Full)

len=${#dossier[@]}

link=/home/lscalfi/Work/8-Analysis/1-Links #tree of links to MD trajectories

#############################################################################################################################################################
#angle distribution

path=/home/lscalfi/Work/8-Analysis/2-Analysis/1-AngleDistribution

rsync -avzh $link/* $path

for (( nt=0; nt<$len; nt++ ));
do
    echo ${dossier[$nt]}
    cd $path/${dossier[$nt]}
    pwd
    for sub in $subdossier
    do
        cd $sub
        pwd
        cfiles angles *.xyz --topology=topology.pdb -c ${box[$nt]}:${box[$nt]}:42.43:90:90:120 -o sioh.dat --selection="angles: name(#1) == Si and name(#2) == Oint and name(#3) == Hint" &
        cfiles angles *.xyz --topology=topology.pdb -c ${box[$nt]}:${box[$nt]}:42.43:90:90:120 -o aloh.dat --selection="angles: name(#1) == Al and name(#2) == Oext and name(#3) == Hext" &
        cfiles angles *.xyz --topology=topology.pdb -c ${box[$nt]}:${box[$nt]}:42.43:90:90:120 -o dihedral.dat --selection="dihedrals: name(#1) == Obr and name(#2) == Si and name(#3) == Oint and name(#4) == Hint" &
        cd ..
    done
    cd ..
done

