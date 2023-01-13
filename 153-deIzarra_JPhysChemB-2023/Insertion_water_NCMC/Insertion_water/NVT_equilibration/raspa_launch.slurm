#!/bin/bash
#SBATCH --job-name=LiCl
#SBATCH --export=MODULEHOME=''  # Compulsory
#SBATCH --partition=qAVX1       # qAVX0 | qAVX1 | qAVX2
#SBATCH --ntasks-per-node=1     # of MPI tasks/node
#SBATCH --cpus-per-task=1      # of OMP threads/task (default =  1)
#SBATCH --time=2000:00:00        # If possible to know
#SBATCH --nodes=1               # Number of nodes default to 1
#-SBATCH --exclude=nnode000
#SBATCH --mail-user=ambroise.deizarra@hotmail.com
#SBATCH --mail-type=END


export RASPA_DIR=${HOME}/RASPA/simulations/
export DYLD_LIBRARY_PATH=${RASPA_DIR}/lib
export LD_LIBRARY_PATH=${RASPA_DIR}/lib
$RASPA_DIR/bin/simulate $1
