Supporting information for: [“Machine learning interatomic potentials for amorphous zeolitic imidazolate frameworks”](https://doi.org/10.1039/D3DD00236E), N. Castel, D. André, C. Edwards, J. D. Evans and F.-X. Coudert, _Digital Discovery_, **2024**, 3, 355–368, DOI: [10.1039/D3DD00236E](https://doi.org/10.1039/D3DD00236E)

A first version of this paper was posted as a [preprint on ChemRxiv](https://doi.org/10.26434/chemrxiv-2023-8003d-v2)


**Ab initio data:**

The trajectories from several ab initio molecular dynamics simulations of ZIF-4, which are produced by CP2K and used as input for training by the machine-learned potentials are large data sets, made publicly available on Zenodo with DOI [10.5281/zenodo.10015593](https://doi.org/10.5281/zenodo.10015593). They consist of NVT simulations of 60 to 80 ps in duration, performed at various temperatures and volumes.


**Trained models:**

We provide here our two “production” machine-learned potentials, i.e., the trained models and their 

- The NequIP model is named `l2r6stress0`: [deployed model](nequip_l2r6stress0.pth) and [associated config file](nequip_l2r6stress0.yaml)
- The Allegro model is named `l2r6stress0a2`: [deployed model](allegro_l2r6stress0a2.pth) and [associated config file](allegro_l2r6stress0a2.yaml)

We also provide input files to run LAMMPS MD simulations on a 2x2x2 super cell of ZIF-4, with the NequIP model. This requires a version of LAMMPS with the [`pair_nequip`](https://github.com/mir-group/pair_nequip) extension compiled in.

- The LAMMPS input file: [`lmp_input.in`](lmp_input.in)
- The starting geometry: [`crystal.lmp`](crystal.lmp)
