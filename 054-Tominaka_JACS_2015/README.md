Supporting information for: [“Insulator-to-Proton-Conductor Transition in a Dense Metal–Organic Framework”](https://doi.org/10.1021/jacs.5b02777), S. Tominaka, F.-X. Coudert, T. D. Dao, T. Nagao, and A. K. Cheetham, _J. Am. Chem. Soc._, **2015**, 137, 6428–6431, DOI: [10.1021/jacs.5b02777](https://doi.org/10.1021/jacs.5b02777)

**Results / data files:**

- [`DFT_phase_I.cif`](DFT_phase_I.cif): Structure of phase I of dense MOF ((CH<sub>3</sub>)<sub>2</sub>NH<sub>2</sub>)<sub>2</sub>[Li<sub>2</sub>Zr(C<sub>2</sub>O<sub>4</sub>)<sub>4</sub>], fully relaxed by DFT calculation (space group _I_ 2/_a_)
- [`DFT_phase_II.cif`](DFT_phase_II.cif): Structure of hydrated phase II, with formula ((CH<sub>3</sub>)<sub>2</sub>NH<sub>2</sub>)<sub>2</sub>[Li<sub>2</sub>(H<sub>2</sub>O)<sub>0.5</sub>Zr(C<sub>2</sub>O<sub>4</sub>)<sub>4</sub>], fully relaxed by DFT calculation (space group _P_ 1)
- [`DFT_phase_II.cif`](DFT_phase_II.cif): Structure of dehydrated phase II, fully relaxed by DFT calculation (space group _P_ 1)


**Input files:**

Software used is [CRYSTAL14](http://www.crystal.unito.it/), version 1.0.2, parallel version on 64-bit GNU/Linux system.

- [`phaseI_geoopt.d12`](phaseI_geoopt.d12): input file for full geometry optimization (atomic coordinates and unit cell parameters) of phase I.
- [`phaseII_geoopt.d12`](phaseII_geoopt.d12): input file for full geometry optimization (atomic coordinates and unit cell parameters) of phase II.
- [`phaseIInowater_geoopt.d12`](phaseIInowater_geoopt.d12): input file for full geometry optimization (atomic coordinates and unit cell parameters) of dehydrated phase II; initial structure obtained from relaxed phase II by removing the water molecule.
