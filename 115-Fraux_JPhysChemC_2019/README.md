Supporting information for: [“Structure, Dynamics and Thermodynamics of Intruded Electrolytes in ZIF-8”](https://doi.org/10.1021/acs.jpcc.9b02718), G. Fraux, A. Boutin, A. H. Fuchs and F.-X. Coudert, _J. Phys. Chem. C_, **2019**, 123 (25), 15589–15598, DOI: [10.1021/acs.jpcc.9b02718](https://doi.org/10.1021/acs.jpcc.9b02718)


**Paper history**

This paper was first posted as a [preprint on chemRxiv](https://doi.org/10.26434/chemrxiv.8052716).


**LAMMPS input files:**

Organisation of the files:
- `bulk/<concentration>/`: bulk fluids
- `confined/<concentration>`: fluids confined in ZIF-8

Each `<concentration>` directory contains the initial equilibration simulation
(`equilibrate`) and simulations input for multiple pressures `XXX-GPa`. To run
the simulations, start by minimization of the initial configurations
(`<concentration>/equilibrate/min.in`) and then the equilibration run
(`<concentration>/equilibrate/run.in`). Then run the simulations at various
pressures (`<concentration>/XXX-GPa/run.in`).

Initial configurations are in LAMMPS Data formats, in `generate/XXX.lmp` files.
