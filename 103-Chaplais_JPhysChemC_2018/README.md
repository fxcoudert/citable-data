Supporting information for: [“Impacts of the Imidazolate Linker Substitution (CH3, Cl or Br) on the Structural and Adsorptive Properties of ZIF-8”](https://doi.org/10.1021/acs.jpcc.8b08706), G. Chaplais, G. Fraux, J.-L. Paillaud, C. Marichal, H. Nouali, A. H. Fuchs, F.-X. Coudert, and J. Patarin, _J. Phys. Chem. C_, **2018**, DOI: [10.1021/acs.jpcc.8b08706](https://doi.org/10.1021/acs.jpcc.8b08706)

- Experimental structures and complete X-ray data, CCDC refs. [1860456](1860456.cif) and [1860457](1860457.cif)
- Initial conformation for ab initio simulations: [ZIF8-CH3](ZIF-CH3.pdb) with
  [10](ZIF-CH3-10.pdb), [25](ZIF-CH3-25.pdb), [40](ZIF-CH3-40.pdb), and
  [50](ZIF-CH3-50.pdb) N2 molecules inside; [ZIF8-Cl](ZIF-Cl.pdb) with
  [10](ZIF-Cl-10.pdb), [25](ZIF-Cl-25.pdb), [40](ZIF-Cl-40.pdb), and
  [50](ZIF-Cl-50.pdb) N2 molecules inside; and [ZIF8-Br](ZIF-Br.pdb) with
  [8](ZIF-Br-8.pdb), [20](ZIF-Br-20.pdb), [40](ZIF-Br-40.pdb), and
  [50](ZIF-Br-50.pdb) N2 molecules inside.
- CP2K 2.5.1 input file for [energy minimization](minimize.in) and [molecular
  dynamics](md.in). To reproduce our results, set the right values for `SYSNAME`
  and `CELL` at the beggining of both files, and run the energy minimization.
  Then remove the `GLOBAL` and `MOTION` sections from the `*.min.rst` file that
  was created, and run the molecular dynamics.
