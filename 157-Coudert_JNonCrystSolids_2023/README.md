Supporting information for: [“Failure to Reproduce the Results of "A new transferable interatomic potential for molecular dynamics simulations of borosilicate glasses"”](https://doi.org/10.1016/j.jnoncrysol.2023.122423), F.-X. Coudert, _J. Non-Cryst. Solids_, **2023**, 615, 122423, DOI: [10.1016/j.jnoncrysol.2023.122423](https://doi.org/10.1016/j.jnoncrysol.2023.122423)


**Data**

This data is plotted in Figure 1, as density vs. composition:

- [`Wang_fig1a_experiments.txt`](Wang_fig1a_experiments.txt): experimental data from the original paper by Wang et al.
- [`Wang_fig1a_simulations.txt`](Wang_fig1a_simulations.txt): simulation data from the original paper by Wang et al.
- [`simulations_this_work.txt`](simulations_this_work.txt): simulation data from this work.

**Input files**

- In the [`input`](input/) folder, you can find LAMMPS input files for simulations according to the Wang force field (with correct atomic masses), where we tried to reproduce the original results. The glasses are labeled as in the original paper, so the input file for glass 75B is [`input/75B/md.inp`](input/75B/md.inp)
- The input files provided by Wang et al. as supplementary material, in PDF format, was converted to text as [`Wang-input.txt`](Wang-input.txt). It does not contain atomic masses (which would be in the data file `NCBS.dat`, not provided) and it contains a typo (`thermos` is an invalid LAMMPS keyword).
