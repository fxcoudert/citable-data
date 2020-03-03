Supporting information for: [“Predicting the Mechanical Properties of Zeolite Frameworks by Machine Learning”](https://doi.org/10.1021/acs.chemmater.7b02532), J. D. Evans, and F.-X. Coudert, _Chem. Mater._, **2017**, 29, 7833–7839, DOI: [10.1021/acs.chemmater.7b02532](https://doi.org/10.1021/acs.chemmater.7b02532)

This paper was first posted as a [preprint on chemRxiv](https://doi.org/10.26434/chemrxiv.5349151.v1)

**Datasets:**

- [`datasets/dft_trainingset.csv`](datasets/dft_trainingset.csv): DFT training set used to learn the predictive model from [F.-X. Coudert, _Phys. Chem. Chem. Phys._, **2013**, 15, 16012–16018.](https://doi.org/10.1039/C3CP51817E) including values predicted from the machine learning model.
- [`datasets/classical_datasets.csv`](datasets/classical_datasets.csv): Bulk and shear moduli calculated using a number of model potentials from [M. Siddorn, F.-X. Coudert, K. Evans and A. Marmier, _Phys. Chem. Chem. Phys._, **2015**, 17, 17927–17933.](https://doi.org/10.1039/C5CP01168J)
- [`datasets/iza.csv`](datasets/iza.csv): Features and predicted bulk and shear moduli for IZA zeolite structures.
- [`datasets/pcod2.csv`](datasets/pcod2.csv): Features and predicted bulk and shear moduli for hypothetical PCOD2 zeolite structures.

For complete datasets of the PCOD2 zeolite structures please refer to the comprehensive dataset [repository](https://github.com/jackevansadl/10.1021_acs.chemmater.7b02532), hosted seperatly owing to the dataset size.

**Sci-kit learn example scripts:**

Example of python scripts for learning a GBR model.

- [`sklearn/gbr_learn_K.py`](sklearn/gbr_learn_K.py): script for learning a predictive model for bulk modulus and outputting a representative cross-validated sample plot.
- [`sklearn/gbr_learn_G.py`](sklearn/gbr_learn_G.py): script for learning a predictive model for shear modulus and outputting a representative cross-validated sample plot.
- [`sklearn/FX_dft_hero.pkl`](sklearn/FX_dft_hero.pkl): DFT dataset packaged in pandas format for use with sci-kit learn scripts.
