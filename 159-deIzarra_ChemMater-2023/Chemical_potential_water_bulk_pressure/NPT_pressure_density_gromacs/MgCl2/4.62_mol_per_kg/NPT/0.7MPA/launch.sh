#!/bin/bash
#SBATCH --nodes=1               # 1 node is used
#SBATCH --ntasks-per-node=4     # 4 MPI tasks
#SBATCH --cpus-per-task=8      # Number of OpenMP threads per MPI task
#SBATCH --hint=nomultithread    # Disable hyperthreading
#SBATCH --job-name=10Mg7      # Jobname
#SBATCH --output=GMX_GenMD.o%j  # Standard output file (%j is the job number)
#SBATCH --error=GMX_GenMD.o%j   # Standard error file
#SBATCH --time=02:00:00         # Expected runtime HH:MM:SS (max 100h)
#SBATCH -A drd@cpu
##
## Please, refer to comments below for
## more information about these 4 last options.
##SBATCH --account=<account>@cpu       # To specify cpu accounting: <account> = echo $IDRPROJ
##SBATCH --partition=<partition>       # To specify partition (see IDRIS web site for more info)
##SBATCH --qos=qos_cpu-dev      # Uncomment for job requiring less than 2 hours
##SBATCH --qos=qos_cpu-t4      # Uncomment for job requiring more than 20h (only one node) 
# Cleans out the modules loaded in interactive and inherited by default

module purge

# Load needed modules
module load gcc/8.4.1
module load cuda/11.2
module load openmpi/4.1.1-cuda
module load gromacs/2022.2-mpi-cuda

# Run : 4 MPI tasks (--ntasks-per-node=4) and 10 threads/task (--cpus-per-task=10)
# Be aware that Gromacs recommands 2 <= ntomp <= 6.

gmx_mpi grompp -f eql2.mdp -c ../../NVT/eql.gro -p ../../prepare_system/topol.top -o eql2.tpr -pp eql2.top -po eql2.mdp 
srun gmx_mpi mdrun -s eql2.tpr -o eql2.trr -x eql2.xtc -c eql2.gro -e eql2.edr -g eql2.log -ntomp ${SLURM_CPUS_PER_TASK}

gmx_mpi grompp -f prd.mdp -c eql2.gro -p ../../prepare_system/topol.top -o prd.tpr -pp prd.top -po prd.mdp
srun gmx_mpi mdrun -s prd.tpr -o prd.trr -x prd.xtc -c prd.gro -e prd.edr -g prd.log -ntomp ${SLURM_CPUS_PER_TASK}

