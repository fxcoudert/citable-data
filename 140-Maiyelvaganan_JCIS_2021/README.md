Supporting information for: [“Identification of a Grotthuss Proton Hopping Mechanism at Protonated Polyhedral Oligomeric Silsesquioxane (POSS)–Water Interface”](https://doi.org/10.1016/j.jcis.2021.07.115), K. R. Maiyelvaganan, S. Kamalakannan, S. Shanmugan, M. Prakash, F.-X. Coudert and M. Hochlaf, _J. Colloid Interface Sci._, **2021**, 605, 701–709, DOI: [10.1016/j.jcis.2021.07.115](https://doi.org/10.1016/j.jcis.2021.07.115)



**Generating initial MD configurations:**

The [`packmol`](packmol/) folder contains input files to generate POSS–water systems as starting configurations for _ab initio_ molecular dynamics:

- [`packmol/packmol.inp`](packmol/packmol.inp): input file for [Packmol](http://leandro.iqm.unicamp.br/m3g/packmol/home.shtml)
- [`packmol/Poss-H.xyz`](packmol/Poss-H.xyz): POSS structure
- [`packmol/water.xyz`](packmol/water.xyz): water molecule structure


**CP2K input files:**

MD simulations were performed wiht [CP2K](https://www.cp2k.org) version 4.1 (source code revision number svn:17462), with `cp2kflags: libint fftw3 parallel mpi3 scalapack libint_max_am=5`. The MPI version was used on Intel Xeon CPU E5-2690 v4 @ 2.60GHz processors, with 56 message passing processes.

- [`CP2K/geoopt.inp`](CP2K/geoopt.inp): input file for geometry optimization, with CP2K
- [`CP2K/md.inp`](CP2K/md.inp): input file for MD at 300 K
