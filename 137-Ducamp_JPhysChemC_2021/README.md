Supporting information for: [“Systematic Study of the Thermal Properties of Zeolitic Frameworks”](https://doi.org/10.1021/acs.jpcc.1c03975), M. Ducamp and F.-X. Coudert, _J. Phys. Chem. C_, **2021**, 125 (28), 15647–15658, DOI: [10.1021/acs.jpcc.1c03975](https://doi.org/10.1021/acs.jpcc.1c03975)


A first version of this paper was posted as a [preprint on chemRxiv](https://doi.org/10.33774/chemrxiv-2021-g285c-v2).


**Structures:**

- A folder named [`starting_structures`](starting_structures/) containing the CIF files of the structures retrieved from the [IZA (International Zeolitic Association) database](http://www.iza-online.org).
- A folder named [`optimized_structures`](optimized_structures/) containing the CIF files of all optimized zeolite structures (with P1 symmetry).


**Data:**

The properties calculated for each zeolite are listed in two files:
- [`properties.tsv`](properties.tsv) in tab-separated format
- [`properties.csv`](properties.csv) in comma-separated format

The properties listed are, in order:
- Zeolite framework code
- Thermal expansion coefficient (K<sup>–1</sup>)
- Grüneisen parameter
- C<sub>p</sub> – C<sub>v</sub> (J/mol/K)
- Density (g/cm<sup>3</sup>)
- Entropy (J/mol), per SiO<sub>2</sub> unit
- Heat_Capacity (J/mol), per SiO<sub>2</sub> unit
- Energy (kJ/mol), per SiO<sub>2</sub> unit
- K<sub>0</sub> (GPa)
- K<sub>0</sub>’
- Volume (Å<sup>3</sup>), per SiO<sub>2</sub> unit
- Accessible volume AV (Å<sup>3</sup>), per SiO<sub>2</sub> unit
- Largest free sphere (Å)
- Largest included sphere (Å)
- Accessible surface area ASA (Å<sup>2</sup>), per SiO<sub>2</sub> unit
- Non-accessible surface area NASA (Å<sup>2</sup>), per SiO<sub>2</sub> unit
- ASA + NASA (Å<sup>2</sup>), per SiO<sub>2</sub> unit
- Non-accessible volume (Å<sup>3</sup>), per SiO<sub>2</sub> unit
- AV + NAV (Å<sup>3</sup>), per SiO<sub>2</sub> unit


**Input files for CRYSTAL17:**

- A directory called [`input_examples`](input_examples/) containing representative input files for optimization ([`input_examples/input_opt.d12`](input_examples/input_opt.d12)) and quasi-harmonic calculations ([`input_examples/input_QHA.d12`](input_examples/input_QHA.d12)).
