import sys
import numpy as np
import matplotlib.pyplot as plt
import pymatgen as pmg
from pymatgen.core.structure import Structure
import matplotlib as mpl
import itertools
import re

for count in range(1,8):
    structure = Structure.from_file("dut49_111k_dose"+str(count)+".cif")

    Kr_index = []
    for index, site in enumerate(structure):
        if site.species_string == "Hf":
            Kr_index.append(index)

    distances = []
    amount = []
    for i in Kr_index:
        neighbors = structure.get_neighbors(structure[i], 22, include_index=True)



        for element in neighbors:
            if element[0].species_string[:1] == "D":
                distances.append(element[1])
                occupancy = str(structure[element[2]]._species)
                occupancy = re.sub("[^0123456789\.]","",occupancy)
                amount.append(float(occupancy))

    rad = 20
    dist_hist, dist_bins = np.histogram(distances, bins=np.arange(0, rad + 0.5, 0.5), weights=amount, density=False)

    rdf = dist_hist
    plt.bar(dist_bins[:-1], rdf, width=np.diff(dist_bins), ec="k", align="edge")

    plot_data = [dist_bins[:-1], rdf]
    np.save('oct_D_'+str(count)+".npy", plot_data)

