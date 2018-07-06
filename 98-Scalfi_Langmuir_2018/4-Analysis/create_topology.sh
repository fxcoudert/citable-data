#!/bin/bash

box=(24.2 25.7 27.3 30.5)
dossier=(1-NT12 2-NT13 3-NT14 4-NT16)
subdossier=(1-Empty  2-Full)

len=${#dossier[@]}

link=/home/lscalfi/Work/8-Analysis/1-Links #tree of links to MD trajectories

#############################################################################################################################################################
# create topology

for (( nt=0; nt<$len; nt++ ));
do
    echo ${dossier[$nt]}
    cd $link/${dossier[$nt]}
    pwd
    for sub in $subdossier
    do
        cd $sub
        pwd
        cfiles convert *.xyz topology.pdb -c ${box[$nt]}:${box[$nt]}:42.43:90:90:120 --steps=0:0 --guess-bonds &
        cd ..
    done
    cd ..
done

