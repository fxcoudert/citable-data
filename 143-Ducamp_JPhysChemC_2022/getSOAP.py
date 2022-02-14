#!/opt/anaconda3/bin/python3

import numpy as np

import ase
from ase import io

import rascal
from rascal.representations import SphericalInvariants

from sklearn.decomposition import PCA, KernelPCA




#Read all the structures

frames = ase.io.read('StructureList.cif', ':')



# Computing SOAP

cutoff = 6

calculator = SphericalInvariants(
soap_type="PowerSpectrum",
interaction_cutoff=cutoff,
max_radial=8,
max_angular=10,
gaussian_sigma_constant=0.4,
gaussian_sigma_type="Constant",
cutoff_smooth_width=1,
normalize=True,
radial_basis="GTO",
compute_gradients=False,

global_species=[8, 14],
expansion_by_species_method="user defined",
)

feature_size = 2112
features = np.zeros((len(frames), feature_size))

for i, frame in enumerate(frames):
        representation = calculator.transform([frame])
        features[i, :] = np.mean(representation.get_features(calculator), axis=0)

print(features.shape)



# Dimensionnality reduction

pca = PCA(n_components=12)
reduced = pca.fit_transform(features)
print(pca.explained_variance_ratio_)
print(reduced.shape)
print(reduced)

