#!/bin/bash

export CURRENTDIR=$PWD
export MATSCREEN=$SCRIPTOFYOURCHOICE 
export NODES=$(srun hostname | sort | uniq)
echo "Running on nodes:"
echo "${NODES}"

python3 $MATSCREEN/screen.py -n $NUMBER_OF_CORES_AVAILABLE -ppn $CORES_PER_PROCS -s $MATSCREEN/data/structures.csv -m xenon krypton -c 20 80 -N 100000 -t coad
