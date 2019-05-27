Supporting information for: [“Investigating the Pressure-Induced Amorphization of Zeolitic Imidazolate Framework ZIF-8: Mechanical Instability due to Shear Mode Softening”](https://doi.org/10.1021/jz400880p), A. U. Ortiz, A. Boutin, A. H. Fuchs and F.-X. Coudert, _J. Phys. Chem. Lett._, **2013**, 4 (11), 1861–1865, DOI: [10.1021/jz400880p](https://doi.org/10.1021/jz400880p)


**Simulation details:**

The [NAMD source code](http://www.ks.uiuc.edu/Research/namd/) for the barostat was patched in order to allow the unit cell to be fully flexible, with fluctuations of all components of the unit cell vectors (rather than the 3 vector lengths as implemented in NAMD version 2.9).

- [`NAMD-2.9-patch.txt`](NAMD-2.9-patch.txt): patch for NAMD version 2.9.
