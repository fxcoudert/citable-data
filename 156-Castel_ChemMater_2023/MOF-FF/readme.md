# MOF-FF

## Finite strain difference

The MD runs should be launched sequentially: start both 002 and 003 after 001 is over.


## Finite stress difference

Input file is provided for an isotropic cell (keyword `iso`).
For a flexible cell, replace `iso` with `tri` in the following lines:
```
fix    4  all  npt temp  300  300  100 iso * * 1000
```

## Strain-fluctuation

One very long run (5 ns), which may be split into a series of shorter ones sequentially restarted

<!-- Add link to amof workflow when MOF-FF included -->