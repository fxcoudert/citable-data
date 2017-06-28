Supporting information for: [“Origins of Negative Gas Adsorption”](https://doi.org/10.1016/j.chempr.2016.11.004), J. D. Evans, L. Bocquet, and F.-X. Coudert, _Chem_, **2016**, 1, 873–886, DOI: [10.1016/j.chempr.2016.11.004](https://doi.org/10.1016/j.chempr.2016.11.004)


**Input files:**

Software used for DFT calculations is [CRYSTAL14](http://www.crystal.unito.it/), version 1.0.2, parallel version on 64-bit GNU/Linux system.

- [DUT-49_ligand.d12](CRYSTAL/DUT-49_ligand.d12): Input file for geometry optimization of DUT-49 ligand.
- [DUT-49_ligand_scan.d12](CRYSTAL/DUT-49_ligand_scan.d12): Input file for the N–N fixed length scans of the DUT-49 ligand.


Classical molecular dynamics simulations were performed with [pydlpoly](http://cmc.aci.ruhr-uni-bochum.de/cmc/default/index), courtesy of Rochus Schmid.

- [dut49.xyz](pydlpoly/dut49.xyz): [Tinker](http://chembytes.wikidot.com/tnk-tut00#toc2) xyz file of DUT-49-op.
- [dut49.key](pydlpoly/dut49.key): key forcefield file for DUT-49 system using the MOF-FF force field with missing parameters taken from the MM3 force field.
- [md.py](pydlpoly/md.py): example of an NPT molecular dynamics simulation of 5~ns.

**Data:**

- [DUT-49cp-DFT.cif](DUT-49cp-DFT.cif): DFT-optimized structure of DUT-49-cp, from the supporting information by [Krause et al.](https://doi.org/10.1038/nature17430).
- [DUT-49op-DFT.cif](DUT-49op-DFT.cif): DFT-optimized structure of DUT-49-op, from the supporting information by [Krause et al.](https://doi.org/10.1038/nature17430).

- [ligandscan_energy.dat](ligandscan_energy.dat): Relative energy (kJ.mol<sup>-1</sup>) with respect to N-N distance (Å) for the DUT-49 ligand.
- [freeenergy_DUT-49.dat](freeenergy_DUT-49.dat): Free energy (kJ.mol<sup>-1</sup>) with respect to unit cell volume (Å<sup>3</sup>) for the DUT-49 framework.
- [pressure_DUT-49.dat](pressure_DUT-49.dat): Internal pressure (MPa) with respect to unit cell volume (Å<sup>3</sup>) for the DUT-49 framework.
