Supporting information for: [“Enhancing Gas Separation Selectivity Prediction through Geometrical and Chemical Descriptors”](https://doi.org/10.1021/acs.chemmater.3c01031), E. Ren and F.-X. Coudert, _Chem. Mater._, **2023**, 35 (17), 6771–6781, DOI: [10.1021/acs.chemmater.3c01031](https://doi.org/10.1021/acs.chemmater.3c01031)


A first version of this paper was posted as a [preprint on chemRxiv](https://doi.org/10.26434/chemrxiv-2023-q841f-v3)


**Code repository**

The GrAED code used to calculate the chemical descriptors can be found in the following GitHub repository: [GrAED](https://github.com/coudertlab/GrAED). The version used in the paper corresponds to the [` v1.0.0-chemmater `](https://github.com/coudertlab/GrAED/releases/tag/v1.0.0-chemmater) tag.

You can either use it as is, or integrate it into a screening process. We use it coupled with [our material-screening code](https://github.com/eren125/material-screening), which is described in a previous article: see the repository `../148-Ren_DigitalDiscovery_2022`.


**Scripts**

- The Python code used to generate the data from the paper can be accessed [here](https://github.com/eren125/material-screening). We can use it to generate a glost list that can be used by the [Glost code](https://github.com/cea-hpc/glost) or [Gnu-parallel](https://www.gnu.org/software/parallel) to screen over a large dataset of structures. A link to the database and some forcefield/structure files are provided in the [Material Screening](https://github.com/eren125/material-screening) repository.
- An example of `Glost` list is given in the `Scripts` directory
- An example of shell script to launch a RAESS calculation and a Widom simulation (`Raspa2`) is given in the `Scripts` directory


**ML model, Data Analysis and Data visualization**

The Python scripts to reproduce the plots from the article are available in the associated [Github repository](https://github.com/eren125/xe_kr_selectivity_xgb). The raw and cleaned data can be found in this repository also. Please refer to the data from a previous article for the reproduction of the adsorption and selectivity data: `../132-Ren_FaradayDiscuss_2021`.
