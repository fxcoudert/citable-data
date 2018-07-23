This directory contains files aiming at describing the computational methods
used in the article ( Dalton Trans., 2016,45, 4352-4359 ).
The two types of files are:

__ in directory optcifs/: structures (in .cif format) optimized with
the CRYSTAL14 software (version 1.0.2).  
File names indicate the type and number of defects per cluster, for
ex. "formate_z10" corresponds to 10 bdc linkers, and 2 formate-capping
ligands around each Zr6O4(OH)4 octahedron. In the "z12" case, there is
no capping ligand, thus the shorter name. The "formate_reo" case
corresponds to the structure with z=8 bdc around each linker, but
(instead of the structure labeled "formate_z8") with a "reo"-type
framework topology.  TFA, OHH2O and ClH2O stand respectively for
trifluoroacetate, [(OH,H2O)] and [(Cl,H2O)] capping ligands.


__ in directory crystal14/: input files of calculations done with
CRYSTAL14: The name of each file indicates the structure it
corresponds to, in the same way as for the .cif files in optcifs/

The last part of the name (before the .d12 extension) indicates the
type of calculation : "optim" for a (full) geometry optimization and
"Cij" for an elastic constant calculation.  For instance: 
_ UiO66_ClH2O_z8_Cij.d12 : Input file for the computation of elastic
constants for the structure labeled "UiO66_ClH2O_z8".  
_ UiO66_formate_z10_Cij.d12 : Input file of elastic constant
calculations for the structure labeled "UiO66_formate_z10". To run it,
the directory where it runs must also contain: 
_ UiO66_formate_z10_Cij.gui : Additional file containing the geometry
information for the calculation above.

Note that convergence criteria, such as the integer following keyword
TOLDEE (in the SCF block) may differ from one input file to another. A
value of 5 (convergence threshold 10^{-5} on energies in SCF
calculations) was used for certain low-symmetry, very computationally
demanding structures (such as "UiO66_ClH2O_z8") while the standard
values (7 for a geometry optimization and 8 for an elastic constant
calculation) were used otherwise.

