Supporting information for: [“CoRE MOF DB: A curated experimental metal-organic framework database with machine-learned properties for integrated material-process screening”](https://doi.org/10.1016/j.matt.2025.102140), G. Zhao, L. M. Brabson, S. Chheda, J. Huang, H. Kim, K. Liu, K. Mochida, T. D. Pham, Prerna, G. G. Terrones, S. Yoon, L. Zoubritzky, F.-X. Coudert, M. Haranczyk, H. J. Kulik, S. M. Moosavi, D. S. Sholl, J. I. Siepmann, R. Q. Snurr and Y. G. Chung, _Matter_, **2025**, 8 (6), 102140, DOI: [10.1016/j.matt.2025.102140](https://doi.org/10.1016/j.matt.2025.102140)


A first version of this paper was posted as a [preprint on chemRxiv](https://doi.org/10.26434/chemrxiv-2024-nvmnr-v2)

**Data**

Some of the data associated with this study is available freely, and some of the data comes from the [Cambridge Structural Database (CSD)](https://www.ccdc.cam.ac.uk/solutions/software/csd/) and requires adhering to the CSD license agreement and its addendum.

- Structures in CIF format include:
  - 8,300 structures from CoRE MOF SI. Derived from the supporting information of published literature, these are freely available on the Zenodo web server at https://zenodo.org/records/15055758
  - 20,276 structures from CoRE MOF CSD Modified. Adapted from the CSD database, these can be accessed freely via the CSD website with a valid email registration: https://www.ccdc.cam.ac.uk/support-and-resources/downloads/.
  - 12,261 structures from CoRE MOF CSD Unmodified. Available through the CCDC GitHub repository using a Python API script (https://github.com/ccdc-opensource/csd-python-api-scripts/tree/main/notebooks/CoRE-MOF), provided the user has a valid CSD license (CSD-Core or better). These structures require additional processing (e.g., conversion to primitive cells and imposing P1 symmetry) and assignment of PACMAN DDEC6 partial atomic charges. The workflow for these operations is detailed in the same repository.
- Tabular data in Excel spreadsheets, split into two parts:
  - Part 1 is available on Zenodo: https://zenodo.org/records/15055758
  - Part 2 is available on the CSD website: https://www.ccdc.cam.ac.uk/support-and-resources/downloads/


**Code**

All scripts used in this work are publicly available in the GitHub repository at https://github.com/mtap-research/CoRE-MOF-Tools