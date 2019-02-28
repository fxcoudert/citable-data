Supporting information for: [“Impacts of the Imidazolate Linker Substitution (CH3, Cl or Br) on the Structural and Adsorptive Properties of ZIF-8”](https://doi.org/10.1021/acs.jpcc.8b08706), G. Chaplais, G. Fraux, J.-L. Paillaud, C. Marichal, H. Nouali, A. H. Fuchs, F.-X. Coudert, and J. Patarin, _J. Phys. Chem. C_, **2018**, 122, 26945–26955, DOI: [10.1021/acs.jpcc.8b08706](https://doi.org/10.1021/acs.jpcc.8b08706)

# Error in the published version

There is a small error in the published article − page 26951; page 26952; and in the legend of figure 4 − the swing angle is described as the Zn−Zn−C−X dihedral angle. It should read as the Zn−Zn−Zn−X dihedral angle.

# Supporting information

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
- Simulation output for each system in a `*.tar.xz` file, containing four files:
    - `*.pos.xyz`: trajectory in XYZ format
    - `*.vel.xyz`: velocities at each step in XYZ format
    - `*.frc.xyz`: forces at each step in XYZ format
    - `*.stress`: stress matrix at each step
