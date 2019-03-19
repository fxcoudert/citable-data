Supporting information for: [ “Structure and Dynamics of Water Confined in Imogolite Nanotubes”](https://doi.org/10.1021/acs.langmuir.8b01115), L. Scalfi, G. Fraux, A. Boutin and F.-X. Coudert, _Langmuir_, **2018**, 34, 6748–6756, DOI: [10.1021/acs.langmuir.8b01115](https://doi.org/10.1021/acs.langmuir.8b01115)

This paper was published as a [preprint on chemRxiv](https://doi.org/10.26434/chemrxiv.6287810.v1)

Here are various input and analysis scripts for this paper. Most of the directories contains an `INSTRUCTION` file to follow to reproduce the simulations.

- [0-Slab_Formation](0-Slab_Formation): Initial formation of a flat slab from Cradwick's data.
- [1-NT-construction](1-NT-construction): Creation of Nanotubes from the optimized flat slab
- [2-Isotherms](2-Isotherms): GCMC simulations of water in the Nanotubes using GIBBS
- [3-MD](3-MD): Molecular dynamics of the full and empty isotherms using LAMMPS
- [4-Analysis](4-Analysis): Various analysis scripts, most of them are based on [cfiles](https://github.com/chemfiles/cfiles)
- [5-DFT](5-DFT): Geometry optimization input and output at DFT level using CRYSTAL14
