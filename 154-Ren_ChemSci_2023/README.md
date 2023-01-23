Supporting information for: [“Rapid Adsorption Enthalpy Surface Sampling (RAESS) to Characterize Nanoporous Materials”](https://doi.org/10.1039/D2SC05810C), E. Ren and F.-X. Coudert, _Chem. Sci._, **2023**, DOI: [10.1039/D2SC05810C](https://doi.org/10.1039/D2SC05810C)


A first version of this paper was posted as a [preprint on chemRxiv](https://doi.org/10.26434/chemrxiv-2022-mczh4-v2)


**Code repository**


The RAESS code can be found in the following GitHub repository: [RAESS](https://github.com/coudertlab/RAESS)

You can either use it as is or integrate it into a screening process (the way we use it is described in the final section)


**Scripts**


- The Python code used to generate the data from the paper can be accessed [here](https://github.com/eren125/material-screening). We can use it to generate a glost list that can be used by the [Glost code](https://github.com/cea-hpc/glost) to screen over a large dataset of structures. A link to the database and the forcefield file are provided in the [Material Screening](https://github.com/eren125/material-screening) repository.

- An example of Glost list is given

- An example of shell script to launch a RAESS simulation is given


**Screening_Data**

- Figure 1 can be obtained using `voronoi_output.csv` and `output_widom_100k.csv` (`2019-11-01-ASR-internal_14142.csv` for LCD labels). The python script `analyse_scatterplot.py` does it.

- Figure 3's data are given in the ESI

- Figure 4 can be obtained using `lambda.py` in `coremof`

- Figure 6 can be obtained using `mu.py` in `coremof`

- Figure 7 can be obtained using the Python script `analyse_final.py` in `coremof`

![Alt text](Screening_data/coremof/Sum-up.png?raw=true "Comparison of the RMSE to the reference Widom insertion and the average computation time for diﬀerent types of enthalpy calculation methods. The surface sampling calculations were all performed with 2k sampling points on each sphere and the Widom simulations were performed using 12k cycles.")

- Figure S12 can be reobtained using the data in `Screening_Data/ToBaCCo`

- Figure S1-3 and S5 can be obtained using `analyse_scatterplot.py`

**Database**

Contains the symmetry aware structures of CoREMOF 2019 (ASR). For the brute data go on zenodo [coremof2019](https://zenodo.org/record/3370144#.Y85ewafMJH4). 

**Tutorial**

Let's say you want to run a RAESS screening: 

1. Download [Raspa2](http://www.zeoplusplus.org/download.html and compile it according to the instructions. Remember the path as `$RASPA_DIR`

2. Download a database of cif files and put them in `$RASPA_DIR/share/raspa/structures/cif/`

A symmetry-specified version of CoREMOF 2019 (ASR) has been calculated using the `-t findsym` tag of [material-screening](https://github.com/eren125/material-screening) and can be used this way: 

```
rm $RASPA_DIR/share/raspa/structures/cif/*
tar xvf coremof_sym.tar.gz
cp coremof_sym/* $RASPA_DIR/share/raspa/structures/cif/.
```

3. Download and compile [RAESS](https://github.com/coudertlab/RAESS) according to the instructions. Remember the path as `$RAESS_DIR`. 
```
export PATH=$PATH:$RAESS_DIR
```

4. Download and compile [GLOST](https://github.com/cea-hpc/glost) according to the instructions. Remember the path as `$GLOST_DIR`

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
`$nprocs` is the number of processors you want to allocate to the tasks
