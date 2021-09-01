Supporting information for: [“Ab Initio Molecular Dynamics of CdSe Quantum-Dot-Doped Glasses”](https://doi.org/10.1021/jacs.9b12073), W. Li, X. Zhao, C. Liu and F.-X. Coudert, _J. Am. Chem. Soc._, **2020**, 142 (8), 3905–3912, DOI: [10.1021/jacs.9b12073](https://doi.org/10.1021/jacs.9b12073)


**Paper history**

This paper was first posted as a [preprint on chemRxiv](https://doi.org/10.26434/chemrxiv.10272041).

**Input files**

- `DL_POLY` input files for classical molecular dynamics: [`CONTROL`](CONTROL) contains the main simulation parameters, [`CONFIG`](CONFIG) is the initial configuration, [`FIELD`](FIELD) is the file describing parameters for interatomic potentials, and [`TABLE`](TABLE) describes the interatomic potentials from Pedone et al (ref. 16).
- [`cp2k_input.txt`](cp2k_input.txt): Input file for the AIMD simulation using the CP2K code

**Structures**

- CIF files for the four structures displayed in Figure 1: [`Figure 1a.cif`](Figure%201a.cif), [`Figure 1b.cif`](Figure%201b.cif), [`Figure 1c.cif`](Figure%201c.cif), [`Figure 1d.cif`](Figure%201d.cif)
- [`trajectory.xyz.gz`](trajectory.xyz.gz): The trajectory in XYZ format of 10 ps production run of ab initio molecular dynamics simulation
