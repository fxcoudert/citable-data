Supporting information for: [“Encoding complexity within supramolecular analogues of frustrated magnets”](http://dx.doi.org/10.1038/nchem.2462), D. Corradini,	A. B. Cairns, M. J. Cliffe, J. A. M. Paddison, D. Daisenberger, M. G. Tucker, F.-X. Coudert, and A. L. Goodwin, _Nature Chem._, **2016**, DOI: [10.1038/nchem.2462](http://dx.doi.org/10.1038/nchem.2462)

Software used is [CRYSTAL14](http://www.crystal.unito.it/), version 1.0.2, parallel version on 64-bit GNU/Linux system.

**Bulk calculations:**

- [`bulk_AgCN.cif`](bulk_AgCN.cif): DFT-optimized structure of bulk AgCN.
- [`bulk_AgCN.d12`](bulk_AgCN.d12): CRYSTAL14 input file for bulk AgCN.
- [`bulk_AuCN.cif`](bulk_AuCN.cif): DFT-optimized structure of bulk AuCN.
- [`bulk_AuCN.d12`](bulk_AuCN.d12): CRYSTAL14 input file for bulk AuCN.

**Chains calculations:**

We performed single-point quantum chemical calculations to measure the variations in energy in pairs of metal–cyanide chains as a function of phase shift Δ_θ_. Single-point calculations were performed and the impact of Grimme D2 corrections was tested, with parameters for Au taken from [Sławińska et al., _Phys. Rev. B_, 83, 245429 (2011)](http://dx.doi.org/10.1103/PhysRevB.83.245429). Below are input files used for Δ_θ_ = 0:

- [`scan_Ag.d12`](scan_Ag.d12): input file for AgCN chains
- [`scan_Au.d12`](scan_Au.d12): input file for AuCN chains
- [`scan_AgAu.d12`](scan_AgAu.d12): input file for bimetallic Ag<sub>1/2</sub>Au<sub>1/2</sub>CN chains
