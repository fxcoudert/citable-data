Supporting information for: [“Rapid Adsorption Enthalpy Surface Sampling (RAESS) to Characterize Nanoporous Materials”](https://doi.org/10.1039/D2SC05810C), E. Ren and F.-X. Coudert, _Chem. Sci._, **2023**, DOI: [10.1039/D2SC05810C](https://doi.org/10.1039/D2SC05810C)


A first version of this paper was posted as a [preprint on chemRxiv](https://doi.org/10.26434/chemrxiv-2022-mczh4-v2)


**Code repository**


The RAESS code can be found in the following GitHub repository: [RAESS](https://github.com/coudertlab/RAESS)


**Scripts**


- The Python code used to generate the data from the paper can be accessed [here](https://github.com/eren125/material-screening). We can use it to generate a glost list that can be used by the [Glost code](https://github.com/cea-hpc/glost) to screen over a large dataset of structures. A link to the database and the forcefield file are provided in the [Material Screening](https://github.com/eren125/material-screening) repository.

- An example of Glost list is given

- An example of shell script to launch a RAESS simulation is given


**Screening_Data**

Figure 7 can be obtained using the data in `Performance_coremof`.

Figure S12 can be reobtained using the data in `Screening_Data/ToBaCCo`.


**Tutorial**

Let's say you want to run a raess screening: 

1. Download [Raspa2](http://www.zeoplusplus.org/download.html and compile it according to the instructions. Remember the path as `$RASPA_DIR`

2. Download a database of cif files and put them in `$RASPA_DIR/share/raspa/structures/cif/`

3. Download and compile [RAESS](https://github.com/coudertlab/RAESS) according to the instructions. Remember the path as `$RAESS_DIR`. 
```
export PATH=$PATH:$RAESS_DIR
```

3. Download and compile [GLOST](https://github.com/cea-hpc/glost) according to the instructions. Remember the path as `$GLOST_DIR`

5. Final instructions for [material-screening](https://github.com/eren125/material-screening) usage.

We are in `$WORK_PATH`
```
git clone git@github.com:eren125/material-screening.git
vim material-screening/set_environment
```
Change the paths according to your file system

```
mkdir screening_test
```
copy the job_raess.sh file of the Scripts inside
The values after the flag -N -rj and -r can be changed according to the number of sphere sampling points, the parameter lambda and mu respectively (see article for more details). 
A `glost.list` file (containing the list of commands to execute) will be generated and a `run.sh` file 

```
cd screening_test
export MATSCREEN=$WORK_PATH/material-screening/
bash job_raess.sh
mpirun -np $nprocs $GLOST_DIR/glost_launch glost.list &>> glost.log
```
$nprocs is the number of processors you want to allocate to the tasks
