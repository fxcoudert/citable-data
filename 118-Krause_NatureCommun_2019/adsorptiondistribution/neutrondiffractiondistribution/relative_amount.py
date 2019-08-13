import sys
import numpy as np
import matplotlib.pyplot as plt
import pymatgen as pmg
from pymatgen.core.structure import Structure
import matplotlib as mpl
import itertools
import re


total_vacuum = 0

data0 = np.load("oct_D_"+str(1)+".npy")

rads = data0[0]
radelement = np.where(rads == 17.5)[0]

relative_amount_oct=[]
for count in range(1,8):
    data1 = np.load("oct_D_"+str(count)+".npy")
    rel = sum(data1[1][:radelement[0]])-total_vacuum
    relative_amount_oct.append(rel)
print relative_amount_oct







data0 = np.load("tet_D_"+str(1)+".npy")

rads = data0[0]
radelement = np.where(rads == 14.5)[0]

relative_amount_tet=[]
for count in range(1,8):
    data1 = np.load("tet_D_"+str(count)+".npy")
    rel = sum(data1[1][:radelement[0]])-total_vacuum
    relative_amount_tet.append(rel)
print relative_amount_tet


data0 = np.load("oct_D_"+str(1)+".npy")

rads = data0[0]
radelement = np.where(rads == 10.5)[0]

relative_amount_cub=[]
for count in range(1,8):
    data1 = np.load("cub_D_"+str(count)+".npy")
    rel = sum(data1[1][:radelement[0]])-total_vacuum
    relative_amount_cub.append(rel)
print relative_amount_cub

relative_amounts_oct=[]
relative_amounts_tet=[]
relative_amounts_cub=[]
for i in range(0,7):
    total_amount = relative_amount_oct[i] + relative_amount_tet[i] + relative_amount_cub[i]
    relative_amounts_oct.append((relative_amount_oct[i]))
    relative_amounts_tet.append((relative_amount_tet[i]))
    relative_amounts_cub.append((relative_amount_cub[i]))

f, axarr = plt.subplots(ncols=7, sharey=True)
for count in range(0,7):
    N=1

    cuba = relative_amounts_cub[count]
    teta = relative_amounts_tet[count]
    octa = relative_amounts_oct[count]
    ind = np.arange(N)
    width = 0.3


    axarr[count].bar(ind, cuba, width)
    axarr[count].bar(ind + width, teta, width)
    axarr[count].bar(ind + width+width, octa, width)

    axarr[count].set_xticks(ind + width+width / 2)
    axarr[count].set_xticklabels((str(count)))

axarr[0].set_ylabel("deuterium frequency")

plt.savefig("relative_loading.pdf", format='pdf', bbox_inches="tight", dpi=600)

