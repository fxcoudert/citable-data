Supporting information for: [“Microscopic structure of mechanically amorphized ZIF glasses: insight from molecular simulations”](https://doi.org/10.26434/chemrxiv.15010773/v1), L. Triestram and F.-X. Coudert, preprint on _ChemRxiv_, **2026**, DOI: [10.26434/chemrxiv.15010773/v1](https://doi.org/10.26434/chemrxiv.15010773/v1)


**Example of LAMMPS input files for the generation of mechanical glasses:**

- [`LAMMPS_input/shear_xy_120_0.01.in`](LAMMPS_input/shear_xy_120_0.01.in): Input file for the formation of a shear glass, tilt factor xy, deformation 120%, rate 1%/ps
- [`LAMMPS_input/elongate_x_80_0.01.in`](LAMMPS_input/elongate_x_80_0.01.in): Input file for the formation of an elongate glass, axis x, deformation 80%, rate 1%/ps
- [`LAMMPS_input/800K.restart`](LAMMPS_input/800K.restart): Equilibrated ZIF-4 crystal structure at 800 K

**Glass structures:**

- [`Glass_structures/mechanical_glasses`](Glass_structures/mechanical_glasses): Mechanical glasses named following the pattern `{type of deformation}_{axis or tilt factor of the deformation}_{max percentage of deformation}_{deformation rate}`
- [`Glass_structures/mechanical_glasses/4x4x4_cell`](Glass_structures/mechanical_glasses/4x4x4_cell): Mechanical glass models from a 4x4x4 supercell
- [`Glass_structures/thermal_glasses`](Glass_structures/thermal_glasses): thermal glasses

**ML-IAP force field**

The MLIP force field used in this work was made available in prior work, see:
https://github.com/fxcoudert/citable-data/tree/master/176-Triestram_ChemSci_2026
