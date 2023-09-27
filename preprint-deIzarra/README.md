Supporting information for: [“Predictive Thermodynamic Model for Intrusion of Electrolyte Aqueous Solutions in Nanoporous Materials”](LINK), A. De Izarra, F.-X. Coudert, A. H. Fuchs and A. Boutin, preprint DOI: [https://chemrxiv.org/engage/chemrxiv/article-details/64f0aede3fdae147fa33bec7]


**RASPA2 common files:**

In the [`RASPA2/`](RASPA2/) directory:
- The content inside `forcefield/` must be copied in `simulations/share/raspa/forcefield`.
- The content inside `molecules/` must be copied in `simulations/share/raspa/molecules`.


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
