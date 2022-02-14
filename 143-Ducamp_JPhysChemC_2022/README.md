Supporting information for: [“Prediction of Thermal Properties of Zeolites through Machine Learning”](https://doi.org/10.1021/acs.jpcc.1c09737), M. Ducamp and F.-X. Coudert, _J. Phys. Chem. C_, **2022**, 126 (3), 1651–1660, DOI: [10.1021/acs.jpcc.1c09737](https://doi.org/10.1021/acs.jpcc.1c09737)

A first version of this paper was posted as a [preprint on chemRxiv](https://doi.org/10.26434/chemrxiv-2021-m67lk-v3).


**Data:**

Here you will find the script used for machine learning, as well as the scripts used for the determination of Smooth Overlap of Atomic Positions (SOAP) features and for the determination of bonds and angles. Examples of files needed to run the machine learning script are also provided.

Structures and data files:
- [`StructureList.cif`](StructureList.cif): List of all the cif structures used.
- [`PropertiesList`](PropertiesList): List of properties calculated for each zeolite. See `sklearn.py` for more info.
- [`BondsAngles`](BondsAngles): List of bonds and angles statistics for each zeolite. See `sklearn.py` for more info.
- [`Coordination/`](Coordination/): Contains one file per zeolite, with the information on network coordination sequence, calculated by the [CrystalNets.jl](https://github.com/coudertlab/CrystalNets.jl) code.

Scripts:
- [`getBondsAngles.py`](getBondsAngles.py): script used to create `BondsAngles` file.
- [`getSOAP.py`](getSOAP.py): script used to get SOAP features.
- [`sklearn.py`](sklearn.py): Script used for machine learning. Contains the recovery of data, the creation of the data set and the machine learning training.
