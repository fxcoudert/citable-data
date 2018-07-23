Supporting information for: [“ELATE: An open-source online application for analysis and visualization of elastic tensors”](https://doi.org/10.1088/0953-8984/28/27/275201), R. Gaillac, P. Pullumbi, and F.-X. Coudert, _J. Phys. Condens. Matter_, **2016**, _28_, 275201, DOI: [10.1088/0953-8984/28/27/275201](https://doi.org/10.1088/0953-8984/28/27/275201)


**Source code:**

The repository with the ELATE source code is available [right here on GitHub](https://github.com/fxcoudert/elate). The version corresponding to the software as described in the paper is [commit  `8b9f0d6`](https://github.com/fxcoudert/elate/tree/8b9f0d6cf7e8bcf6a93c6968d964f1cc494ef7e7).


**Data:**

- The elastic tensor for Ag₃Co(CN)₆, used to plot Figure 2, comes from DFT calculations in [H. Fang, M. T. Dove, and K. Refson, _Phys. Rev. B_, **2014**, 90, 054302](https://doi.org/10.1103/PhysRevB.90.054302). It is (in units of GPa):
```
    34.3     13.1     47.1     -8.5        0        0  
    13.1     34.3     47.1      8.5        0        0  
    47.1     47.1    139.6        0        0        0  
    -8.5      8.5        0     32.7        0        0  
       0        0        0        0     32.7        0  
       0        0        0        0        0     10.6  
```

- The elastic tensor for α-quartz, used to plot Figure 3, is the following (in units of GPa):
```
    87.64   6.99   11.91  -17.19    0.00    0.00
     6.99  87.64   11.91   17.19    0.00    0.00
    11.91  11.91  107.20    0.00    0.00    0.00
   -17.19  17.19    0.00   57.94    0.00    0.00
     0.00   0.00    0.00    0.00   57.94  -17.19
     0.00   0.00    0.00    0.00  -17.19   39.88
```
