Supporting information for: [“Neural Network-Based Interatomic Potential for the Study of Thermal and Mechanical Properties of Siliceous Zeolites”](https://doi.org/10.1021/acs.jpcc.4c07365), L. Brugnoli, M. Ducamp and F.-X. Coudert, _J. Phys. Chem. C_, **2024**, DOI: [10.1021/acs.jpcc.4c07365](https://doi.org/10.1021/acs.jpcc.4c07365)

A first version of this paper was posted as a [preprint on chemRxiv](https://doi.org/10.26434/chemrxiv-2024-np8wf-v2)


**Data, input files, code**

All data related to this paper is hosted on Zenodo at [DOI: 10.5281/zenodo.11519171](https://zenodo.org/doi/10.5281/zenodo.11519171). This contains:

- representative input files for AIMD simulations with CP2K (`example_CP2K_AIMD_input`)
- the full training set in ExtXYZ format (`full_training_set.extxyz`)
- the NequIP input for training the potential (`config.yaml`)
- the deployed model (`deployed_SiO_Zeolites_MLIP.pth`)
- representative input files for LAMMPS simulations (`MD_ramping_P` and `MD_ramping_T`)


**Starting structures for AIMD**

The [`CIF_FILES/`](CIF_FILES/) folder contains the crystallographic information files (CIF) representing the initial geometries of the frameworks at the start of the ab initio molecular dynamics (AIMD) simulations performed with CP2K. The structures are labeled according to the applied strain as follows:

- `0`: unstrained structure
- `1`: +1.5% strain
- `2`: +3.0% strain
- `3`: –1.5% strain

All unstrained structures (label 0) were obtained from the IZA Structure Database and subsequently relaxed using CP2K geometry optimization, while keeping the unit cell parameters fixed.

The unit cell settings of the original structures were preserved for all cases except for the CHA framework. For CHA, we adopted the rhombohedral setting instead of the hexagonal configuration, as it provides a more compact and efficient representation of the system.


**Starting structures for LAMMPS MD**

The [`LMP_FILES/`](LMP_FILES/) folder contains the initial structures used in the LAMMPS simulations for the 4 frameworks considered, in LAMMPS format.
