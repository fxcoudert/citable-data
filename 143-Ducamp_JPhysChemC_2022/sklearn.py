#!/opt/anaconda3/bin/python3

import numpy as np

import math

import rascal
from rascal.representations import SphericalInvariants

import ase
from ase import io

from sklearn.decomposition import PCA, KernelPCA
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.inspection import permutation_importance
from sklearn.model_selection import cross_val_score, KFold, cross_val_predict


def Variance(List, mean):
    tmp = 0
    for i in List:
        tmp = tmp + i**2
    return (tmp/len(List))-(mean**2)

def ecartType(Var):
    return math.sqrt(Var)



# Retrieve structures from StructureList.cif

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



# PropertiesList contains properties calculated with DFT and Volumetric descriptors calculated with zeo++ for each zeolite

with open("PropertiesList", "r") as t:
        lines = t.readlines()
        CODE = lines[0].split() # First line corresponds to code names of zeolites (ex: LTA, FAU, ...)
        alpha = [float(i) for i in lines[1].split()] # Following lines correspond to various properties (ex: alpha = thermal expansion coefficient)
        gruneisen = [float(i) for i in lines[2].split()] 
        CpCv = [float(i) for i in lines[3].split()] 
        density = [float(i) for i in lines[4].split()] 
        Entropy = [float(i) for i in lines[5].split()] 
        HeatCap = [float(i) for i in lines[6].split()] 
        Energy = [float(i) for i in lines[7].split()] 
        K0 = [float(i) for i in lines[8].split()] 
        K0prime = [float(i) for i in lines[9].split()]
        RUM = [float(i) for i in lines[10].split()]
        Volume = [float(i) for i in lines[11].split()]
        ZeoDensity = [float(i) for i in lines[12].split()]
        AV = [float(i) for i in lines[13].split()]
        FreeSphere = [float(i) for i in lines[14].split()]
        InclSphere = [float(i) for i in lines[15].split()]
        ASA = [float(i) for i in lines[16].split()]
        NASA = [float(i) for i in lines[17].split()]
        ASANASA = [float(i) for i in lines[18].split()]
        ASAchan = [float(i) for i in lines[19].split()]
        NAV = [float(i) for i in lines[20].split()]
        AVNAV = [float(i) for i in lines[21].split()]
        AVchan = [float(i) for i in lines[22].split()]


# "BondsAngles" contains the statistics on bonds and angles calculated with "getBondsAngles.py"

with open("BondsAngles", "r") as f:
        lines = f.readlines()
        SiOSi_mean, SiOSi_gmean, SiOSi_hmean, SiOSi_max, SiOSi_min, SiOSi_var, SiO_mean, SiO_gmean, SiO_hmean, SiO_max, SiO_min, SiO_var = [], [], [], [], [], [], [], [], [], [], [], []
        for line in lines:
                SiOSi_mean.append(float(line.split()[1]))
                SiOSi_gmean.append(float(line.split()[2]))
                SiOSi_hmean.append(float(line.split()[3]))
                SiOSi_max.append(float(line.split()[4]))
                SiOSi_min.append(float(line.split()[5]))
                SiOSi_var.append(float(line.split()[6]))
                SiO_mean.append(float(line.split()[7]))
                SiO_gmean.append(float(line.split()[8]))
                SiO_hmean.append(float(line.split()[9]))
                SiO_max.append(float(line.split()[10]))
                SiO_min.append(float(line.split()[11]))
                SiO_var.append(float(line.split()[12]))



# Retrieving coordination informations from "CODE_coord" files located in Coordination directory, CODE being code names of zeolites

coord = dict()
coordVar = dict()
coordMax = dict()
coordMin = dict()
coordET = dict()

for i in range(2,13):
	coord[i] = []
	coordVar[i] = []
        coordMax[i] = []
        coordMin[i] = []
        coordET[i] = []


for i in CODE:
        with open(i+"_coord", "r") as f:
                line = f.readlines()
                tmp = []
                coords = []
                coordsVar = []
                coordsMax = []
                coordsET = []
                coordsMin = []
                for i in range(len(line)):
                        tmp.append(line[i].split())

                tmp = np.array(tmp)
                tmp = tmp.transpose()

                for i in tmp:
                        x = [int(n) for n in i]
                        mean = sum(x)/len(x)
                        coords.append(mean)
                        variance = Variance(x, mean)
                        coordsVar.append(variance)
                        ET = ecartType(variance)
                        coordsET.append(ET)
                        coordsMax.append(max(x))
                        coordsMin.append(min(x))

                for i in range(2, 13):
			coord[i].append(float(coords[i-1]))
                        coordVar[i].append(float(coordsVar[i-1]))
                        coordMax[i].append(float(coordsMax[i-1]))
                        coordMin[i].append(float(coordsMin[i-1]))
                        coordET[i].append(float(coordsET[i-1]))




# Choice of set of descriptors (uncomment one)
 
xtrain = np.c_[SiOSi_mean, SiOSi_gmean, SiOSi_hmean, SiOSi_max, SiOSi_min, SiOSi_var, SiO_mean, SiO_gmean, SiO_hmean, SiO_max, SiO_min, SiO_var]
#xtrain = np.c_[[coord[i] for i in range[2,13)], coordVar[2]]
#xtrain = np.array(reduced)
#xtrain = np.c_[Volume, ZeoDensity, AV, FreeSphere, InclSphere, ASA, NASA, ASANASA, ASAchan, NAV, AVNAV, AVchan]
#xtrain = np.c_[reduced, coord2, coord3, coord4, SiOSi_hmean, SiO_min, SiOSi_var, Volume, ZeoDensity, ASANASA]


# Attributing names for feature importance plot (uncomment one)

#names = ["Volume", "ZeoDensity", "AccVol", "FreeSphere", "InclSphere", "ASA", "NASA", "ASAsum", "ASAchan", "NAV", "AVsum", "AVchan"]
#names = ["coord2", "coord3", "coord4", "coord5", "coord6", "coord7", "coord8", "coord9", "coord10", "coord11", "coord12", "coord2V"]#"coord8", "coord9", "coord10", "coord11", "coord12"]
#names = ["PCA1", "PCA2", "PCA3", "PCA4", "PCA5", "PCA6", "PCA7", "PCA8", "PCA9", "PCA10", "PCA11", "PCA12"]
names = ["SiOSi_mean", "SiOSi_gmean", "SiOSi_hmean", "SiOSi_max", "SiOSi_min", "SiOSi_var", "SiO_mean", "SiO_gmean", "SiO_hmean", "SiO_max", "SiO_min", "SiO_var"]
#names = ["PCA1", "PCA2", "PCA3", "coord2", "coord3", "coord4", "SiOSi_hmean", "SiO_min", "SiOSi_var", "Volume", "ZeoDensity", "ASANASA"]



# Choice of target property

ytrain = np.array(K0)



# Definition of GBR and training
 
trainingSet = { "data" : xtrain, "target" : ytrain, "feature_names" : names,}
 
gbr = GradientBoostingRegressor(n_estimators=500, learning_rate=0.01, min_samples_split=2, min_samples_leaf=2, max_depth=2, max_features='sqrt', loss='ls', subsample=0.4)
fittest = gbr.fit(xtrain, ytrain)
ytest = gbr.predict(xtrain)
 
with open("train_vs_test", "w") as f:
        f.write("train\tprediction\n")
        for x, y in zip(ytrain, ytest):
                f.write(str(x)+"\t"+str(y)+"\n")
        
score = gbr.score(xtrain, ytrain)
print("The score on test set is {}".format(score))
mse = (mean_squared_error(ytrain, ytest))**0.5
print("The mean squared error on test set is {}".format(mse))
        
        
# Permutation feature importance
        
r = permutation_importance(gbr, trainingSet["data"], trainingSet["target"], n_repeats=30, random_state=0)
with open("feature_importance", "w") as FI:
        for i in r.importances_mean.argsort()[::-1]:
                if r.importances_mean[i] - 2 * r.importances_std[i] > 0:
                        FI.write(f"{trainingSet['feature_names'][i]:<8}"
                              f"{r.importances_mean[i]:.3f}"
                              f" +/- {r.importances_std[i]:.3f}\n")

feature_importance = gbr.feature_importances_
        
        
        
# Cross-validation

print('cross-validation')
scores = []
iterations = 50
for i in range(0, iterations):
        cv = KFold(n_splits=3, shuffle=True, random_state=i)
        predict = cross_val_predict(gbr, xtrain, ytrain, cv=cv, n_jobs=-1)
        CVscore = cross_val_score(gbr, xtrain, ytrain, cv=cv, scoring='neg_mean_squared_error', n_jobs=-1)
        CVscore = (CVscore*-1)**0.5
        scores.append(CVscore)
        

scores = np.array(scores)
CVscore = np.mean(scores.flatten())
print(CVscore)
        
with open("cross_validation", "w") as f:
                f.write("train\tprediction\n")
                for x, y in zip(ytrain, predict):
                        f.write(str(x)+"\t"+str(y)+"\n")
