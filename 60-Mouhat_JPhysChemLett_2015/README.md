Supporting information for: [“Softening upon Adsorption in Microporous Materials: A Counterintuitive Mechanical Response”](http://dx.doi.org/10.1021/acs.jpclett.5b01965), F. Mouhat, D. Bousquet, A. Boutin, L. Bouëssel du Bourg, F.-X. Coudert, and A. H. Fuchs, _J. Phys. Chem. Lett._, **2015**, 6, 4265–4269, DOI: [10.1021/acs.jpclett.5b01965](http://dx.doi.org/10.1021/acs.jpclett.5b01965)

**Input files:**

- [`NAMD-2.9-patch.txt`](NAMD-2.9-patch.txt): Patch to the [NAMD 2.9](http://www.ks.uiuc.edu/Research/namd/) molecular dynamics program. This patch changes the barostat to allow the unit cell to be fully flexible, with random variations of all components of the unit cell vectors (rather than the 3 vector lengths as implemented in NAMD version 2.9).
- [`NAMD-input`](NAMD-input/): Complete set of input files for the [NAMD 2.9](http://www.ks.uiuc.edu/Research/namd/) software, corresponding to a molecular dynamics simulation of nine CH<sub>4</sub> molecules in a ZIF with *nog* topology.
