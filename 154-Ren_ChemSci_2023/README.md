Supporting information for: [“Rapid adsorption enthalpy surface sampling (RAESS) to characterize nanoporous materials”](https://doi.org/10.1039/D2SC05810C), E. Ren and F.-X. Coudert, _Chem. Sci._, **2023**, DOI: [10.1039/D2SC05810C](https://doi.org/10.1039/D2SC05810C)


A first version of this paper was posted as a [preprint on chemRxiv](https://doi.org/10.26434/chemrxiv-2022-mczh4-v2)


**Code repository**

The RAESS code can be found in the following GitHub repository: [RAESS](https://github.com/coudertlab/RAESS). The version used in the paper corresponds to the [`v1.0.0-chemsci`](https://github.com/coudertlab/RAESS/releases/tag/v1.0.0-chemsci) tag.

You can either use it as is, or integrate it into a screening process. The way we use it, coupled with [our material-screening code](https://github.com/eren125/material-screening), is described in the final section.


**Scripts**

- The Python code used to generate the data from the paper can be accessed [here](https://github.com/eren125/material-screening). We can use it to generate a glost list that can be used by the [Glost code](https://github.com/cea-hpc/glost) or [Gnu-parallel](https://www.gnu.org/software/parallel) to screen over a large dataset of structures. A link to the database and some forcefield/structure files are provided in the [Material Screening](https://github.com/eren125/material-screening) repository.
- An example of `Glost` list is given in the `Scripts` directory
- An example of shell script to launch a RAESS calculation and a Widom simulation (`Raspa2`) is given in the `Scripts` directory


**Screening_Data**

- The data plotted in Figure 1 is available in [`voronoi_output.csv`](Screening_Data/coremof/voronoi_output.csv) and [`output_widom_100k.csv`](Screening_Data/coremof/output_widom_100k.csv) ([`2019-11-01-ASR-internal_14142.csv`](Screening_Data/coremof/2019-11-01-ASR-internal_14142.csv) for LCD labels). The python script [`analyse_scatterplot.py`](Screening_Data/coremof/analyse_scatterplot.py) does it.
- The data in Figure 3 are given in the ESI.
- Figure 4 can be obtained using [`lambda.py`](Screening_Data/coremof/lambda.py)
- Figure 6 can be obtained using [`mu.py`](Screening_Data/coremof/mu.py)
- Figure 7 can be obtained using the Python script [`analyse_final.py`](Screening_Data/coremof/analyse_final.py)

![Alt text](Screening_Data/coremof/Sum-up.png?raw=true "Comparison of the RMSE to the reference Widom insertion and the average computation time for diﬀerent types of enthalpy calculation methods. The surface sampling calculations were all performed with 2k sampling points on each sphere and the Widom simulations were performed using 12k cycles.")

- Figure S12 can be reobtained using the data in [`Screening_Data/ToBaCCo/`](Screening_Data/ToBaCCo/)
- Figure S1-3 and S5 can be obtained using [`analyse_scatterplot.py`](Screening_Data/coremof/analyse_scatterplot.py)


**Database**

- [`Database/coremof_sym.tar.gz`](Database/coremof_sym.tar.gz) contains the symmetry aware structures of CoREMOF 2019 (ASR). The raw/original data, can be found on zenodo [coremof2019](https://zenodo.org/record/3370144#.Y85ewafMJH4).
- [`Database/tobacco_sym_sample.tar.gz`](Database/tobacco_sym_sample.tar.gz) contains a sample of 1000 symmetry aware structures of the ToBaCCo database. The raw/original data can be found on the MOFXDB of the Northwestern University [tobacco](https://mof.tech.northwestern.edu/databases). The database was designed by Colon et al., see their paper [_Cryst. Growth Des._ *2017*, _17_, 5801–5810](https://pubs.acs.org/doi/10.1021/acs.cgd.7b00848).
- For the data of the amorphous database we considered please refer to the paper [“A Database of Porous Rigid Amorphous Materials”](https://pubs.acs.org/doi/10.1021/acs.chemmater.0c03057), where the CIF files are provided in the supplementary information. Symmetries cannot be determined for these structures and we did not manage to screen it on our lab computers using the `Raspa2` software probably due to memory issues (feel free to test it with a more efficient set-up if these materials interest you).


**Tutorial**

Let's say you want to run a RAESS screening, you can follow the steps below:

1. Download [Raspa2](https://github.com/iRASPA/RASPA2) and compile it according to the instructions. Remember the path as `$RASPA_DIR`

2. Download a database of cif files and put them in `$RASPA_DIR/share/raspa/structures/cif/`

A symmetry-specified version of CoREMOF 2019 (ASR) has been calculated using the `-t findsym` tag of [material-screening](https://github.com/eren125/material-screening) and can be used this way:

```
rm $RASPA_DIR/share/raspa/structures/cif/*
tar xvf coremof_sym.tar.gz
cp coremof_sym/* $RASPA_DIR/share/raspa/structures/cif/.
```

For this database, a list of the structure names and some key informations are already put in `material-screening/data/structures_sym.csv` and  `material-screening/data/info.csv`. For other databases, you will need to create other files and specify their name when using `material-screening`. See 4. for more details on `material-screening` or go on the [GitHub](https://github.com/eren125/material-screening) associated.

3. Download and compile [RAESS](https://github.com/coudertlab/RAESS) according to the instructions. Remember the path as `$RAESS_DIR`.
```
export PATH=$PATH:$RAESS_DIR
```

4. Download and compile [GLOST](https://github.com/cea-hpc/glost) according to the instructions. Remember the path as `$GLOST_DIR`

5. Final instructions for [material-screening](https://github.com/eren125/material-screening) usage.

In `$WORK_PATH`:
```
cd $WORK_PATH
git clone git@github.com:eren125/material-screening.git
vim material-screening/set_environment
```

```
cd $WORK_PATH
mkdir screening_test
```
Copy the `Scripts/job_raess.sh` (or the `Scripts/job_widom.sh`) file of this repository inside `$WORK_PATH/screening_test`

The values after the flags -N -rj and -r can be changed according to the number of sphere sampling points, the parameter lambda and mu respectively (see article for more details). A more comprehensive explanation of the flags are given in [Github repo](https://github.com/eren125/material-screening).

A `glost.list` file (containing the list of commands to execute) will be generated and a `run.sh` file

```
cd $WORK_PATH/screening_test
export MATSCREEN=$WORK_PATH/material-screening/
bash job_raess.sh
mpirun -np $nprocs $GLOST_DIR/glost_launch glost.list &>> glost.log
```
`$nprocs` is the number of processors you want to allocate to the tasks

- `Glost` works easily on several nodes in a HPC cluster of machines.

- But `Glost` uses one cpu for job distribution, which is not optimal if `$nprocs` is small. A better alternative is to simply use `Gnu-parallel` with the same `glost.list` we generated (works fine on a single node):
```
cd $WORK_PATH/screening_test
export MATSCREEN=$WORK_PATH/material-screening/
bash job_raess.sh
parallel -j $nprocs < glost.list
```

It is also possible to run it with `Gnu-parallel` on several nodes, see: https://www.msi.umn.edu/support/faq/how-can-i-use-gnu-parallel-run-lot-commands-parallel
