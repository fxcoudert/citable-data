

List and description of files:
In directory ZnCN2_crystal14/

_ dia_opt.d12: input file for a full geometry optimization (atomic coordinates and 
unit cell parameters) of the "dia" structure, performed with CRYSTAL14 (version 1.0.2) 

_ DFT_opt_*.cif: DFT-optimized structures for all of the Zn(CN)2 polymorphs studied.

  
- In directory ZnCN2_dlpoly/: 
_ CONTROL, CONFIG, and FIELD are input files for Molecular Dynamic simulations 
performed with DL_POLY Classic 1.9. They contain respectively information on simulation parameters, the initial structure, and the force field. 
The system is a 3x3x2 supercell built from the "dia" structure's unit cell. 

_ cell.py is a Python code processing a STATIS file produced by MD simulations, and 
extracting (i) average cell parameters and (ii) elastic constants (in Voigt notation).

_ mdangles.f90 is a Fortran code processing a HISTORY file produced by MD simulations (to be renamed as fort.10), and extracting inter alia:
_ fort.11, i.e. the distribution g(\theta) of angles \theta between CN and Zn-Zn axes
(unnormalized; \theta and g(theta) values are in the 1st and 2nd columns respectively).
_ fort.13, i.e. the distribution g(d) of distances between middle points 
of C-N and Zn-Zn segments (unnormalized).

_ meanangles.f90 is a Fortran code also processing a HISTORY file, but time-averaging the
structure before computing spatial distributions such as g(<theta>) and g(<d>) (fort.11 and fort.13 respectively).

 


