#!/bin/bash
#MSUB -r water1
#MSUB -o water1.o
#MSUB -e water1.e
#MSUB -E --no-requeue
#MSUB -q skylake
##MSUB -x
#MSUB -A gen7069
#MSUB -m scratch,work,store
#MSUB -n 1 
#MSUB -T 86400


ccc_mprun run
