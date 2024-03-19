Supporting information for: [“Prediction of Diffusion Coefficient Through Machine Learning Based on Transition State Theory Descriptors”](https://doi.org/10.26434/chemrxiv-2024-h98mf), E. Ren and F.-X. Coudert, preprint on _ChemRxiv_, **2023**, DOI: [10.26434/chemrxiv-2024-h98mf](https://doi.org/10.26434/chemrxiv-2024-h98mf)


A first version of this paper was posted as a [preprint on chemRxiv](https://doi.org/10.26434/chemrxiv-2024-h98mf)


**Related repositories**

- The Grid Adsorption Energy Sampling code (GrAED) is available at https://github.com/coudertlab/GrAED
- Code and data related to the thermodynamic sampling of Xe/Kr selectivity, which serves as a basis for the present work, is available at https://github.com/eren125/xe_kr_selectivity_xgb


**Data and code**

- The scripts used to gather and clean the data, training models, test them, perform Shapley analysis, and produce the various visualizations are available in the top-level directory.
- The final trained model is made available as [`model/final_diffusion_model.sav`](model/final_diffusion_model.sav).
- The curated data is available in the [`data/`](data/) folder.
- Plots are available in the [`plot/`](plot/) and [`PDP/`](PDP/) folders.
