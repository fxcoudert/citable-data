#!/bin/bash

continue="yes"
global_name=" water"

oldline="ContinueAfterCrash"
newline="ContinueAfterCrash $continue"

oldline1="#MSUB -r"
oldline2="#MSUB -o"
oldline3="#MSUB -e"

for i in {1..30}
do
    sed -i "s/$oldline.*/$newline/" $i/simulation.input

    newline1=$oldline1$global_name$i
    sed -i "s/$oldline1.*/$newline1/" $i/RASPA_sub.sh

    newline2=$oldline2$global_name$i".o"
    sed -i "s/$oldline2.*/$newline2/" $i/RASPA_sub.sh

    newline3=$oldline3$global_name$i".e"
    sed -i "s/$oldline3.*/$newline3/" $i/RASPA_sub.sh

    sleep 0.1
    cd $i
    ccc_msub RASPA_sub.sh
    cd ..
done
