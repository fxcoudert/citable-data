# ReaxFF

[Implemented in LAMMPS](https://docs.lammps.org/pair_reaxff.html)

More details in the Supporting information for[“Challenges in Molecular Dynamics of Amorphous ZIFs Using Reactive Force Fields”](https://doi.org/10.1021/acs.jpcc.2c06305) at [this link](../../152-Castel_JPhysChemC_2022).

## Finite strain difference

The MD runs should be launched sequentially: start 002 after 001 is over, etc.
At each volume_change, deform should be launched before equilibrate.

<!-- Add link to amof workflow when ReaxFF included -->