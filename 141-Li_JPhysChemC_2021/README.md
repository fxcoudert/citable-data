Supporting information for: [“Influence of Glass Composition on the Luminescence Mechanisms of CdSe Quantum-Dot-Doped Glasses”](https://doi.org/10.1021/acs.jpcc.1c04665), W. Li, X. Zhao, C. Liu and F.-X. Coudert, _J. Phys. Chem. C_, **2021**, 125 (34), 18916–18926, DOI: [10.1021/jacs.9b12073](https://doi.org/10.1021/acs.jpcc.1c04665)


**Paper history**

This paper was first posted as a [preprint on chemRxiv](https://doi.org/10.33774/chemrxiv-2021-w9g4h-v2).

**Input files**

- `DL_POLY` input files for classical molecular dynamics are found in the [`DL_POLY/`](DL_POLY/) folder: [`DL_POLY/CONTROL`](DL_POLY/CONTROL) contains the main simulation parameters, [`DL_POLY/CONFIG`](DL_POLY/CONFIG) is the initial configuration, [`DL_POLY/FIELD`](DL_POLY/FIELD) is the file describing parameters for interatomic potentials.
- [`cp2k-aimd.inp`](cp2k-aimd.inp): Input file for ab initio molecular dynamics (AIMD) simulations using the CP2K code.
- [`cp2k-electronic-structure.inp`](cp2k-electronic-structure.inp): Input file for electronic structure calculations using the CP2K code.

**Structures**

- [`structures/`](structures/): Structures extracted from the ab initio molecular dynamics runs, at intervals of 200 fs, and used for electronic structure calculations. For each system composition there is a specific folder, with 50 structures inside in XYZ format.
