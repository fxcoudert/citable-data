Supporting information for: [“Microscopic Mechanism of Chiral Induction in a Metal–Organic Framework”](https://doi.org/10.1021/jacs.6b02781), J. D. Evans, and F.-X. Coudert, _J. Am. Chem. Soc._, **2016**, 138, 6131–6134, DOI: [10.1021/jacs.6b02781](https://doi.org/10.1021/jacs.6b02781)


**Input files:**

Software used for DFT calculations is [CRYSTAL14](http://www.crystal.unito.it/), version 1.0.2, parallel version on 64-bit GNU/Linux system.

- [MOF5.d12](CRYSTAL/MOF5.d12): Input file for full geometry optimization of MOF-5.
- [CMOF5.d12](CRYSTAL/CMOF5.d12): Input file for full geometry optimization of CMOF-5.
- [CMOF5_NMP12mol.d12](CRYSTAL/CMOF5_NMP12mol.d12): Input file for full geometry optimization of CMOF-5 with 12 NMP molecules per unit cell.
- [CMOF5_NMP24mol.d12](CRYSTAL/CMOF5_NMP24mol.d12): Input file for full geometry optimization of CMOF-5 with 24 NMP molecules per unit cell.
- [CMOF5_DMF12mol.d12](CRYSTAL/CMOF5_DMF12mol.d12): Input file for full geometry optimization of CMOF-5 with 12 DMF molecules per unit cell.
- [CMOF5_DMF24mol.d12](CRYSTAL/CMOF5_DMF24mol.d12): Input file for full geometry optimization of CMOF-5 with 24 DMF molecules per unit cell.

Monte Carlo simulations were performed with the [RASPA](https://github.com/numat/RASPA2/), version 2.0.

- [MOF5_pbesol0.cif](RASPA/MOF5_pbesol0.cif): Energy-minimized structure of MOF-5.
- [MOF5_nmp24.input](RASPA/MOF5_nmp24.input): RASPA input for MOF-5 with 24 NMP molecules per unit cell.
- [MOF5_dmf24.input](RASPA/MOF5_dmf24.input): RASPA input for MOF-5 with 24 DMF molecules per unit cell.
- [CS](RASPA/CS): RASPA forcefield parameters for DMF.
- [GAFF](RASPA/GAFF): RASPA forcefield parameters for NMP.

**Data:**

- [ja5b11150_si_002_cleaned.cif](ja5b11150_si_002_cleaned.cif): Structure for Δ-CMOF-5, taken from the supporting information by [Zaworotko et al.](https://doi.org/10.1021/jacs.5b11150), with disorder removed.
- [ja5b11150_si_003_cleaned.cif](ja5b11150_si_003_cleaned.cif): Structure for Λ-CMOF-5, taken from the supporting information by [Zaworotko et al.](https://doi.org/10.1021/jacs.5b11150), with disorder removed.
- [CMOF5_NMP12mol.cif](CMOF5_NMP12mol.cif): Energy-minimized structure for CMOF-5 with 12 NMP molecules per unit cell.
- [CMOF5_NMP24mol.cif](CMOF5_NMP24mol.cif): Energy-minimized structure for CMOF-5 with 24 NMP molecules per unit cell.
- [CMOF5_DMF12mol.cif](CMOF5_DMF12mol.cif): Energy-minimized structure for CMOF-5 with 12 DMF molecules per unit cell.
- [CMOF5_DMF24mol.cif](CMOF5_DMF24mol.cif): Energy-minimized structure for CMOF-5 with 24 DMF molecules per unit cell.
- [MOF5_closedpore.cif](MOF5_closedpore.cif): Structure of the closed pore analogue of MOF-5.
