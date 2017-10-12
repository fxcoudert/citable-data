import sys
import json
import yaml
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from pprint import pprint
from sklearn.preprocessing import RobustScaler
import pymatgen as pmg
from pymatgen.analysis.elasticity.elastic import ElasticTensor
from pymatgen.core.structure import Structure
from matminer.descriptors.composition_features  import get_holder_mean
import scipy.stats as stats
from pymatgen.util.coord_utils import pbc_shortest_vectors, get_angle
from pymatgen.io.zeopp import ZeoCssr, ZeoVoronoiXYZ, get_voronoi_nodes, \
    get_high_accuracy_voronoi_nodes, get_void_volume_surfarea, \
    get_free_sphere_params
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import matplotlib as mpl

data = pd.read_pickle('FX_dft_hero.pkl')

print data.columns

y = data['g_vrh']

X = data.drop(['k_vrh', 'g_vrh', 'uni_anis', 'energy'], axis=1)


print np.shape(X)

#y = np.log10(y)

from sklearn.model_selection import cross_val_predict, cross_val_score
from sklearn import linear_model
lr = linear_model.LinearRegression()
import seaborn as sns
from sklearn.model_selection import train_test_split, KFold

gbr = GradientBoostingRegressor(n_estimators=1000, learning_rate=0.01, min_samples_split=2, min_samples_leaf=3, max_depth=3, max_features='sqrt', loss='ls', subsample=0.4)
# gbr = GradientBoostingRegressor(n_estimators=1000, learning_rate=0.01)
#
# gbr = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4),
#                         n_estimators=300, random_state=0)

mpl.rcParams['pdf.fonttype'] = 42
sns.set(style="white", palette="muted")
sns.set_style("ticks")
sns.set_context("notebook", font_scale=1.8, rc={"figure.figsize": (8, 6)})
sns.set_palette("muted")
b, gr, r, p, v = sns.color_palette("muted", 5)

scores = []
iterations = 100
for i in range(0,iterations):
    cv = KFold(n_splits=3, random_state=i)
    predict = cross_val_predict(gbr,X, y, cv=cv, n_jobs=-1)
    score = cross_val_score(gbr,X, y, cv=cv, scoring='neg_mean_squared_error', n_jobs=-1)
    score = (score*-1)**0.5
    scores.append(score)
    if i == (iterations-1):
        plt.plot([0,60],[0,60], '--', color='black')
        plt.plot(y, predict, 'o', color=b,  markersize=10)

scores = np.array(scores)
#print scores
print np.mean(scores.flatten())
print np.std(scores.flatten())

plt.ylabel('G$\mathregular{_{GBR}}$ / GPa')
plt.xlabel('G$\mathregular{_{DFT}}$ / GPa')



plt.savefig("crossval_G_nolog.pdf", format='pdf', bbox_inches="tight", dpi=600)
