Supporting information for: [“Systematic investigation of the mechanical properties of pure silica zeolites: stiffness, anisotropy, and negative linear compressibility”](http://dx.doi.org/10.1039/C3CP51817E), F.-X. Coudert, _Phys. Chem. Chem. Phys._, **2013**, 15, 16012–16018, DOI: [10.1039/C3CP51817E](http://dx.doi.org/10.1039/C3CP51817E)

**Results / data files:**

- [`elastic_properties.xlsx`](elastic_properties.xlsx): a summary of the calculated elastic properties of the pure-silica zeolites
- [`energies.xlsx`](energies.xlsx): calculated relative energies, as well as some other properties (space group, channel system dimensionality, density)
- [`optimized_structures.zip`](optimized_structures.zip): energy-minimized structures for 164 pure-silica zeolites. All structures were fully relaxed (atomic positions and unit cell parameters), with the B3LYP exchange–correlation functional and Grimme D2 dispersion corrections, as described in the text.
- [`elastic_tensors.zip`](elastic_tensors.zip): the elastic tensors calculated for 121 all-silica zeolites, in the form of 6×6 symmetric (positive definite) matrices in Voigt notation. One matrix per text file; only the upper half of each matrix is stored.
- [`elastic_tensors.json`](elastic_tensors.json): same as above, but as a single file in JSON format.

**Input files:**

Software used is [CRYSTAL09](http://www.crystal.unito.it/), version 2.0.1, parallel version on 64-bit GNU/Linux system.

- [`optgeom_FAU.d12`](optgeom_FAU.d12): input file for full geometry optimization (atomic coordinates and unit cell parameters) of all-silica zeolite FAU.
- [`elastic_FAU.d12`](elastic_FAU.d12): input file for calculation of elastic tensor of all-silica zeolite FAU.
