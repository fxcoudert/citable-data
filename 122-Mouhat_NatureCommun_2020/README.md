Supporting information for: [“Structure and chemistry of graphene oxide in liquid water from first principles”](https://doi.org/10.1038/s41467-020-15381-y), F. Mouhat, F.-X. Coudert and M.-L. Bocquet, _Nature Commun._, **2020**, 11, 1566, DOI: [10.1038/s41467-020-15381-y](https://doi.org/10.1038/s41467-020-15381-y)


**Paper history**

This paper was first posted as a [preprint on arXiv](https://arxiv.org/abs/1911.04987).

**Movies**

- [`movie_1.mp4`](movie_1.mp4): Movie showing several proton exchanges between the surface hydroxyl groups and the surrounding H<sub>2</sub>O molecules present in the bulk.
- [`movie_2.mp4`](movie_2.mp4): Movie showing the dehydration reaction that is observed in the trajectory of the semi-ordered 4 graphene oxide model in liquid water.

**Structures**

- The models of graphene oxide created in this work are found in the [`models/GO`](models/GO) directory. As in the paper, they are classified in [random](models/GO/random) and [semi-ordered](models/GO/semi_ordered), and 5 models of each type were created. For each model, we provide coordinates in an `GO.xyz` file (in XYZ format) and cell parameters in a `cell_parameters.dat` file (in ångströms).
- The most stable models were then hydrated by adding H<sub>2</sub>O molecules, the resulting models are found in the [`models/GO_with_water`](models/GO_with_water) directory. The layout is the same as above.

**MD trajectories**

- The trajectories obtained for the hydrated graphene systems, labeled in the same way as the structures above, are available on [Zenodo, DOI: 10.5281/zenodo.3736713](https://doi.org/10.5281/zenodo.3736713) They trajectories report the atomic positions at each time step, in [XYZ format](https://en.wikipedia.org/wiki/XYZ_file_format), compressed with the [bzip2](https://www.sourceware.org/bzip2/) algorithm.

**Input files**

- [`input_SO1_water_MD.txt`](input_SO1_water_MD.txt): Representative input file for [CP2K](https://www.cp2k.org) ab initio molecular dynamics, for the semi-ordered model 1 with water.
