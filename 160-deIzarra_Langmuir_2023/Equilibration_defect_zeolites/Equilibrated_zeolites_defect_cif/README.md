
**In "Equilibrated_zeolites_defect_cif":**

- Here, one extracts the final pdb structure of the zeolite at the end of a MC simulation performed in 'Equilibration_zeolites_defect' (e.g. /Movies/System_0/Framework_final.pdb) and convert it in cif file.

IMPORTANT : We used chemfiles to convert pdb to cif format. If the user use chemfiles, he must remove manually the cartesian coordinates and only keep the fractional coordinates since RASPA read those by default.
