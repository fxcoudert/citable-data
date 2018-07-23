This directory contains files aiming at describing the computational methods
used in the article (Chem. Mater., 2016, 28 (1), pp 368–375).
The two types of files are:

__ in the subdirectory optcifs/, structures in .cif format, optimized
with CRYSTAL14. They are also found in Supporting Information of the
paper; each file's name indicates its stoechiometry, with X standing for
Zn_2(ntb)_{4/3} , and e.g. bipy13 standing for (bipy)_{1/6}
(1/3 of the maximal content in bipy, which is 1/2). The exception is the
non-defective MUF-32 (file MUF32_opt.cif).

__in the subdirectory crystal14/, 3 representative input files used for
the calculations with the software CRYSTAL14 (version 1.0.2).  
_ MUF32_optim.d12 : input file for full geometry optimization of the
non-defective MUF-32.  
_ Xbipy_optim.d12 : same the X(bipy)_{1/2} structure.  
_ Xbipy_Cij.d12 : input file for the calculation of elastic constants
of the X(bipy)_{1/2} structure. To run it, an external file :
Xbipy_Cij.gui, produced earlier by running Xbipy_optim.d12, must be
present in the same directory.


