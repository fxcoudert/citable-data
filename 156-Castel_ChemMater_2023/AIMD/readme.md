# AIMD


## Finite strain difference

The MD runs should be launched sequentially: start 002 after 001 is over, etc.

Before launching 002, the `&CELL` parameters should be changed in the CP2K input file.
It can be done with the `change_cell.sh` script.

<!-- Add link to amof workflow when CP2K included -->