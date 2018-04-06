Supporting information for: [“Structure and Dynamics of Solvated Polymers Near a Silica Surface: on the Different Roles Played by Solvent”](https://doi.org/10.1021/acs.jpcb.7b11753), R. Gaillac, P. Pullumbi, and F.-X. Coudert, _J. Phys. Chem. C_, **2018**, DOI: [10.1021/acs.jpcb.7b11753](https://doi.org/acs.jpcb.7b11753)



**Coarse-grained molecular dynamics input files for [LAMMPS](http://lammps.sandia.gov/)** (version 10 Aug 2015):

- Input files for explicit solvent model in the [`input_PAAm_explicit`](input_PAAm_explicit/) directory:
  - [`run.in.nvt`](input_PAAm_explicit/run.in.nvt): main LAMMPS input file for molecular dynamics
  - [`system.init`](input_PAAm_explicit/system.init): general declarations
  - [`in.data`](input_PAAm_explicit/in.data): system configuration and topology, from a previous LAMMPS run
  - [`system.settings`](input_PAAm_explicit/system.settings): force field parameters
- Input files for implicit solvent model in the [`input_PAAm_implicit`](input_PAAm_implicit/) directory, with the same layout.
