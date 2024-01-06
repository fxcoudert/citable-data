Supporting information for: [“Predictive Thermodynamic Model for Intrusion of Electrolyte Aqueous Solutions in Nanoporous Materials”](https://doi.org/10.1021/acs.chemmater.3c02230), A. De Izarra, F.-X. Coudert, A. H. Fuchs and A. Boutin, _Chem. Mater._, **2023**, 35 (24), 10606–10618, DOI: [10.1021/acs.chemmater.3c02230](https://doi.org/10.1021/acs.chemmater.3c02230)


A first version of this paper was posted as a [preprint on chemRxiv](https://doi.org/10.26434/chemrxiv-2023-k1q81-v2)


**RASPA2 common files:**

In the [`RASPA2/`](RASPA2/) directory:
- The content inside `forcefield/` must be copied in `simulations/share/raspa/forcefield`.
- The content inside `molecules/` must be copied in `simulations/share/raspa/molecules`.

Simulations were ran with the two modified versions of the RASPA2 code, previously published by our group, and available at https://github.com/fxcoudert/citable-data/tree/master/153-deIzarra_JPhysChemB-2023
For more details on the methodology, see [“Alchemical Osmostat for Monte Carlo Simulation: Sampling Aqueous Electrolyte Solution in Open Systems”](https://pubs.acs.org/doi/abs/10.1021/acs.jpcb.2c07902), A. De Izarra, F.-X. Coudert, A. H. Fuchs and A. Boutin, _J. Phys. Chem. B_, **2023**, 127 (3), 766–776, DOI: [https://doi.org/10.1021/acs.jpcb.2c07902](https://doi.org/10.1021/acs.jpcb.2c07902)

Finally, in `RASPA2/RASPA_insertion_water_NCMC/` we provide source files for a modified version of RASPA, where the NCMC move is adapted to insert a single water molecule in electrolyte solutions (instead of two water molecules as in our work linked above. In order to install this modified version, copy the files in the `src/` directory of RASPA2, which can be downloaded from https://github.com/iRASPA/RASPA2. These modifications are also available as a patch file: [`RASPA_insertion_water_NCMC.patch`](RASPA2/RASPA_insertion_water_NCMC.patch)


**Simulation input files:**

- In `Intrusion_electrolyte_zeosil/`, input files to perform MC simulations in the osmostic ensemble: we introduce a single electrolyte unit and output the alchemical work associated to this process.
- In `Water_intrusion_zeosil/`, input files to reproduce intrusion and extrusion of water in zeosils.
- In `Chemical_potential_ion_exchange_bulk_pressure/`, input files to construct the relationship between pressure and chemical potential of ion exchange, using density as an intermediate quantity:
  - In `NPT_pressure_density_gromacs`, we perform MD simulations of electrolyte solutions (600 particles) to retrieve the relationship between density and pressure.
  - After extracting the density, we deduce the size of the cubic box corresponding to 150 particles, stored in `density_vs_pressure.ods`.
  - The size of the cubic box is then used to perform MC simulations in osmotic ensemble in the `Osmotic_simulation_chemical_potential_RASPA` folder.
- In `Chemical_potential_water_bulk_pressure/`, we determine the relationship between pressure and chemical potential of water in electrolyte solutions, using density as an intermediate quantity:
  - In `NPT_pressure_density_gromacs`, we perform MD simulations of electrolyte solutions (600 particles) to retrieve the relationship between density and pressure.
  - After extracting the density, we deduce the size of the cubic box corresponding to 150 particles, stored in  `density_vs_pressure.ods`.
  - The size of the cubic box is then used to perform MC simulations in `Chemical_potential_water_RASPA`, where the chemical potenial of water is calculated.
