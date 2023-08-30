Supporting information for: [“Computation of Finite Temperature Mechanical Properties of Zeolitic Imidazolate Framework Glasses by Molecular Dynamics”](https://doi.org/10.1021/acs.chemmater.3c00392), N. Castel and F.-X. Coudert, _Chem. Mater._, **2023**, 35, 10, 4038–4047, DOI: [10.1021/acs.chemmater.3c00392](https://doi.org/10.1021/acs.chemmater.3c00392)

A first version of this paper was posted as a [preprint on chemRxiv](https://doi.org/10.26434/chemrxiv-2023-d2wxz-v3).

**Code repository**

The code repository of the python library `amof` associated with the article is there: https://github.com/coudertlab/amof

The version used for this work is [`v1.0.0`](https://github.com/coudertlab/amof/releases/tag/jphyschem).



**Molecular dynamics input files**

For each method and MD scheme used in the article, the input files are provided for the crystal.

The file structure is `MD-scheme/method` where `MD-scheme` can be `AIMD`, `ReaxFF` and `MOF-FF` and `method` can be `finite strain difference`, `finite stress difference` or `strain-fluctuation`.

**Structures**

A number of structural files of both crystals and glasses are present in the [`Structures`](Structures) folder.
They are provided in several formats and can be used to adapt the MD input files provided.

This folder contains:
- Ab initio glasses from [“Structure of Metal–Organic Framework Glasses by Ab Initio Molecular Dynamics”](https://doi.org/10.1021/acs.chemmater.0c02950), R. Gaillac, P. Pullumbi, and F.-X. Coudert, _Chem. Mater._, **2020**, 32, 8004–8011, already available as `cif` files [here](129-Gaillac_ChemMater_2020/)
- An RMC glass from [“Liquid metal-organic frameworks”](https://doi.org/10.1038/nmat4998), R. Gaillac, P. Pullumbi, K. A. Beyer, K. W. Chapman, D. A. Keen, T. D. Bennett, and F.-X. Coudert, _Nature Mater._, **2017**, 16, 1149–1154
- Different supercells of the crystal prepared for MOF-FF
- A ReaxFF glass generated in [“Challenges in Molecular Dynamics of Amorphous ZIFs Using Reactive Force Fields”](https://doi.org/10.1021/acs.jpcc.2c06305), N. Castel and F.-X. Coudert, _J. Phys. Chem. C_, **2022**, 126 (45), 19532–19541
