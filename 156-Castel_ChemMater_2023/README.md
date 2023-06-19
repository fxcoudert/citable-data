Supporting information for: [“Computation of Finite Temperature Mechanical Properties of Zeolitic Imidazolate Framework Glasses by Molecular Dynamics”](https://doi.org/10.1021/acs.chemmater.3c00392), N. Castel and F.-X. Coudert, _Chem. Mater._, **2023**, 35, 10, 4038–4047, DOI: [10.1021/acs.chemmater.3c00392](https://doi.org/10.1021/acs.chemmater.3c00392)

A first version of this paper was posted as a [preprint on chemRxiv](https://doi.org/10.26434/chemrxiv-2023-d2wxz-v3).

**Code repository**

The code repository of the python library `amof` associated with the article is there: https://github.com/coudertlab/amof

The version used for this work is [`v1.0.0`](https://github.com/coudertlab/amof/releases/tag/jphyschem).



**Molecular dynamics input files**

For each method and MD scheme used in the article, the input files are provided for the crystal.

The file structure is `MD-scheme/method` where `MD-scheme` can be `AIMD`, `ReaxFF` and `MOF-FF` and `method` can be `finite strain difference`, `finite stress difference` or `strain-fluctuation`.

**Glass structures**

TODO

---
Below: not updated yet

**ReaxFF molecular dynamics input files ([Implemented in LAMMPS](https://docs.lammps.org/pair_reaxff.html)):**

- LAMMPS input files of the 4 steps of the melt-quenching simulation outlined in the paper:
  - [`prepare.in`](prepare.in).
  - [`melt.in`](melt.in).
  - [`quench.in`](quench.in). 
  - [`equilibrate.in`](equilibrate.in). 
- A single cell of the ZIF-4 crystal formatted in the  [`charge` atom_style](https://docs.lammps.org/atom_style.html): [`ZIF-4_crystal_singlecell.data`](ZIF-4_crystal_singlecell.data).
- The ReaxFF potential file [`ffield_ZnN_2016`](`ffield_ZnN_2016`) and control file [`lmp_control`](`ffield_ZnN_2016`), made available on this repository courtesy of [Prof. Adri van Duin](https://www.engr.psu.edu/adri/Home.aspx). Associated training set files can be obtained upon request through the Penn State Materials Computation Center website using [this contact form](https://www.mri.psu.edu/materials-computation-center/connect-mcc). 

The original paper of this force field: [“Enabling Computational Design of ZIFs Using ReaxFF”](https://doi.org/10.1021/acs.jpcb.8b08094 ), Yongjian Yang, Yun Kyung Shin, Shichun Li, Thomas D. Bennett, Adri C. T. van Duin, and John C. Mauro, _J. Phys. Chem. C_, **2018**, 122 (41), 9616-9624, DOI: [10.1021/acs.jpcb.8b08094 ](https://doi.org/10.1021/acs.jpcb.8b08094 )
