# LAMMPS Input Files

In this directory the [LAMMPS](https://lammps.sandia.gov/) input files to simulate ZIF8-H, ZIF8-CH3, ZIF8-Br and ZIF8-Cl with the developed force fields are provided. Note, that LAMMPS has to be build with additional packages in order to be able to use MOF-FF force fields. Therefore cd to the lammps directory and install via

```
cd src

make yes-CLASS2
make yes-KSPACE
make yes-MANYBODY
make yes-USER-MOFFF
make yes-USER-MISC
make yes-MOLECULE
```
Afterwards, LAMMPS has to be recompiled.
