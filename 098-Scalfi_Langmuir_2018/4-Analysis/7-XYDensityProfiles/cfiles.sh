#!/bin/bash

box=(24.2 25.7 27.3 30.5)
dossier=(1-NT12 2-NT13 3-NT14 4-NT16)
subdossier=(1-Empty  2-Full)

len=${#dossier[@]}

link=/home/lscalfi/Work/8-Analysis/1-Links

#############################################################################################################################################################
# XY density profiles

path=/home/lscalfi/Work/8-Analysis/2-Analysis/7-XYDensityProfiles

rsync -avzh $link/* $path

range_si="(z <= 13.78975 and z > 11.66825)"
range_si="$range_si or (z <= 9.54675 and z > 7.42525)"
range_si="$range_si or (z <= 5.30375 and z > 3.18225)"
range_si="$range_si or (z <= 1.06075 and z > -1.06075)"
range_si="$range_si or (z > -5.30375 and z <= -3.18225)"
range_si="$range_si or (z > -9.54675 and z <= -7.42525)"
range_si="$range_si or (z > -13.78975 and z <= -11.66825)"

range_w="(z > 9.54675 and z <= 11.66825)"
range_w="$range_w or (z > 5.30375 and z <= 7.42525)"
range_w="$range_w or (z > 1.06075 and z <= 3.18225)"
range_w="$range_w or (z <= -1.06075 and z > -3.18225)"
range_w="$range_w or (z <= -5.30375 and z > -7.42525)"
range_w="$range_w or (z <= -9.54675 and z > -11.66825)"

for (( nt=0; nt<$len; nt++ ));
do
    echo ${dossier[$nt]}
    cd $path/${dossier[$nt]}
    pwd
    for sub in $subdossier
    do
        cd $sub
        pwd
        for element in Al Si Oint Oext Obr Hint Hext Ow Hw
        do
            cfiles density *.xyz -c ${box[$nt]}:${box[$nt]}:42.43:90:90:120 --topology=topology.pdb --selection="atoms: name $element and ($range_si)" --axis=X --axis=Y --max=30 --min=-30 -o densityXY_${element}.ringsi.dat  &
            cfiles density *.xyz -c ${box[$nt]}:${box[$nt]}:42.43:90:90:120 --topology=topology.pdb --selection="atoms: name $element and ($range_w)" --axis=X --axis=Y --max=30 --min=-30 -o densityXY_${element}.ringw.dat  &
        done
        cd ..
    done
    cd ..
done

