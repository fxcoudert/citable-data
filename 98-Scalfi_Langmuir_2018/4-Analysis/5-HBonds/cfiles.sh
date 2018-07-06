#!/bin/bash

box=(24.2 25.7 27.3 30.5)
dossier=(1-NT12 2-NT13 3-NT14 4-NT16)
subdossier=(1-Empty  2-Full)

len=${#dossier[@]}

link=/home/lscalfi/Work/8-Analysis/1-Links

#############################################################################################################################################################
# detect hbonds

path=/home/lscalfi/Work/8-Analysis/2-Analysis/5-HBonds

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
        #SiOh-SiOh HB
        cfiles hbonds *.xyz --topology=topology.pdb --distance=3.5 -c  ${box[$nt]}:${box[$nt]}:42.43:90:90:120 -o hbonds_si-si.dat --acceptors="atoms: name Oint" --donors="bonds: name(#1) Oint and name(#2) Hint" &
        #AlOh-AlOh HB
        cfiles hbonds *.xyz --topology=topology.pdb --distance=3.5 -c  ${box[$nt]}:${box[$nt]}:42.43:90:90:120 -o hbonds_al-al.dat --acceptors="atoms: name Oext" --donors="bonds: name(#1) Oext and name(#2) Hext" &
       #water_in-water_in HB
       cfiles hbonds *.xyz --topology=topology.pdb --distance=3.5 -c ${box[$nt]}:${box[$nt]}:42.43:90:90:120 -o hbonds_wi-wi.dat --acceptors="atoms: name Ow" --donors="bonds: name(#1) Ow and name(#2) Hw" &

       #water_out-water_out HB
       cfiles hbonds *.xyz --topology=topology.pdb --distance=3.5 -c ${box[$nt]}:${box[$nt]}:42.43:90:90:120 -o hbonds_wo-wo.dat --acceptors="atoms: name Owo" --donors="bonds: name(#1) Owo and name(#2) Hwo" &

       #SiOh-water HB
       cfiles hbonds *.xyz --topology=topology.pdb --distance=3.5 -c ${box[$nt]}:${box[$nt]}:42.43:90:90:120 -o hbonds_si-w.dat --acceptors="atoms: name Oint" --donors="bonds: name(#1) Ow and name(#2) Hw" &

       #water-SiOh HB
       cfiles hbonds *.xyz --topology=topology.pdb --distance=3.5 -c ${box[$nt]}:${box[$nt]}:42.43:90:90:120 -o hbonds_w-si.dat --acceptors="atoms: name Ow" --donors="bonds: name(#1) Oint and name(#2) Hint" &

       #AlOh-water HB
       cfiles hbonds *.xyz --topology=topology.pdb --distance=3.5 -c ${box[$nt]}:${box[$nt]}:42.43:90:90:120 -o hbonds_al-w.dat --acceptors="atoms: name Oext" --donors="bonds: name(#1) Owo and name(#2) Hwo" &

       #water-AlOh HB
       cfiles hbonds *.xyz --topology=topology.pdb --distance=3.5 -c ${box[$nt]}:${box[$nt]}:42.43:90:90:120 -o hbonds_w-al.dat --acceptors="atoms: name Owo" --donors="bonds: name(#1) Oext and name(#2) Hext" &
        cd ..
    done
    cd ..
done

