Supporting information for: [“Novel porous polymorphs of zinc cyanide with rich thermal and mechanical behavior”](https://doi.org/10.1021/acs.chemmater.5b01366), F. Trousselet, A. Boutin, and F.-X. Coudert, _Chem. Mater._, **2015**, 27, 4422–4430, DOI: [10.1021/acs.chemmater.5b01366](https://doi.org/10.1021/acs.chemmater.5b01366)



**In directory `ZnCN2_crystal14/`**

- `dia_opt.d12`: input file for a full geometry optimization (atomic coordinates and
unit cell parameters) of the _dia_ structure, performed with CRYSTAL14 (version 1.0.2)

- `DFT_opt_*.cif`: DFT-optimized structures for all of the Zn(CN)<sub>2</sub> polymorphs studied.


**In directory `ZnCN2_dlpoly/`**

- `CONTROL`, `CONFIG`, and `FIELD` are input files for Molecular Dynamic simulations performed with DL_POLY Classic 1.9. They contain respectively information on simulation parameters, the initial structure, and the force field. The system is a 3x3x2 supercell built from the _dia_ structure's unit cell.

- `cell.py` is a Python code processing a `STATIS` file produced by MD simulations, and extracting (i) average cell parameters and (ii) elastic constants (in Voigt notation).

- `mdangles.f90` is a Fortran code processing a `HISTORY` file produced by MD simulations (to be renamed as `fort.10`), and extracting inter alia:
 - `fort.11`, i.e. the distribution _g_(_θ_) of angles _θ_ between CN and Zn-Zn axes (unnormalized; _θ_ and _g_(_θ_) values are in the 1st and 2nd columns respectively)
 - `fort.13`, i.e. the distribution _g_(_d_) of distances between middle points of C-N and Zn-Zn segments (unnormalized).


- `meanangles.f90` is a Fortran code also processing a `HISTORY` file, but time-averaging the
structure before computing spatial distributions such as _g_(< _θ_ >) and _g_(< _d_ >) (`fort.11` and `fort.13` respectively).
