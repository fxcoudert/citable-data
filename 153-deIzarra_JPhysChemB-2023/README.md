Supporting information for: [“Alchemical Osmostat for Monte Carlo Simulation: Sampling Aqueous Electrolyte Solution in Open Systems”](https://pubs.acs.org/doi/abs/10.1021/acs.jpcb.2c07902), A. De Izarra, F.-X. Coudert, A. H. Fuchs and A. Boutin, _J. Phys. Chem. B_, **2023**, 127 (3), 766–776, DOI: [https://doi.org/10.1021/acs.jpcb.2c07902](https://doi.org/10.1021/acs.jpcb.2c07902)



**Folder [`Osmostat_electrolytes_NCMC`](Osmostat_electrolytes_NCMC/)**

- In [`Osmostat_electrolytes_NCMC/RASPA`](Osmostat_electrolytes_NCMC/RASPA/) we provide our modified version of RASPA2, where the NCMC move is implemented for performing MC simulations in the osmotic ensemble. This is based on the [`v2.0.47`](https://github.com/iRASPA/RASPA2/releases/tag/v2.0.47) tag of RASPA2, dated 30 November 2021, corresponding to commit [`673ad2d`](https://github.com/iRASPA/RASPA2/commit/673ad2d52a9c11e5ee7db9e5e7339663bfabecf9). You can install this modified version by copying the files in the `src/` directory into the RASPA2 directory of the same name. Alternatively, you can also directly apply the patch file at [`Osmostat_electrolytes_NCMC/RASPA.patch`](Osmostat_electrolytes_NCMC/RASPA.patch).
- In [`Osmostat_electrolytes_NCMC/MC_computation_chemical_potential_ion_exchange_CsCl`](Osmostat_electrolytes_NCMC/MC_computation_chemical_potential_ion_exchange_CsCl/) we provide input files to perform calculations of the alchemical work and chemical potential in the CsCl electrolyte, using the modified RASPA code.
- In [`Osmostat_electrolytes_NCMC/MC_osmotic_ensemble_from_bulk_water_to_electrolytes_CsCl`](Osmostat_electrolytes_NCMC/MC_osmotic_ensemble_from_bulk_water_to_electrolytes_CsCl/) we provide input filesto perform MC simulations in the osmostic ensemble where CsCl electrolytes are inserted in a system initially constituted of pure TIP4P water, using the modified RASPA code.


**Folder [`Insertion_water_NCMC`](Insertion_water_NCMC/)**

- In [`Insertion_water_NCMC/RASPA`](Insertion_water_NCMC/RASPA/) we provide our modified version of RASPA2, where the the NCMC move is adapted to insert 2 water molecules in bulk water (which we use for the calculation of free energy of water solvation). This is based on the [`v2.0.47`](https://github.com/iRASPA/RASPA2/releases/tag/v2.0.47) tag of RASPA2, dated 30 November 2021, corresponding to commit [`673ad2d`](https://github.com/iRASPA/RASPA2/commit/673ad2d52a9c11e5ee7db9e5e7339663bfabecf9). You can install this modified version by copying the files in the `src/` directory into the RASPA2 directory of the same name. Alternatively, you can also directly apply the patch file at [`Insertion_water_NCMC/RASPA.patch`](Insertion_water_NCMC/RASPA.patch).
- In [`Insertion_water_NCMC/Simulations`](Insertion_water_NCMC/Simulations/) you can find input files used to perform calculations of free energy of water solvation in bulk water, using above patched version of RASPA.
