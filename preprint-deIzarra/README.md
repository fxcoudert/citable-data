Supporting information for: [“Predictive Thermodynamic Model for Intrusion of Electrolyte Aqueous Solutions in Nanoporous Materials”](LINK), A. De Izarra, F.-X. Coudert, A. H. Fuchs and A. Boutin, preprint DOI: [https://chemrxiv.org/engage/chemrxiv/article-details/64f0aede3fdae147fa33bec7]


**RASPA2 common files:**

In the [`RASPA2/`](RASPA2/) directory:
- The content inside `forcefield/` must be copied in `simulations/share/raspa/forcefield`.
- The content inside `molecules/` must be copied in `simulations/share/raspa/molecules`.


**Simulation input files:**

- In `Intrusion_electrolyte_zeosil/`, input files to perform MC simulations in the osmostic ensemble: we introduce a single electrolyte unit and output the alchemical work associated to this process.
- In `Water_intrusion_zeosil/`, input files to reproduce intrusion and extrusion of water in zeosils.
