#!-*-coding:utf-8-*-

from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pylab
from scipy.optimize import curve_fit

fig_width=7.32 # inches, adapté pour taille de police LaTex = 12 
fig_fonts = {
        "text.usetex"        : True,
        "font.family"        : "serif",
        "axes.labelsize"     : 12,
        "font.size"          : 12,
        "legend.fontsize"    : 10,
        "xtick.labelsize"    : 12,
        "ytick.labelsize"    : 12,
        }
mpl.rcParams.update(fig_fonts)

# ---------- Input file ----------  
inputFile = "adsorption_pressure_MC_cycle.csv"
# --------------------------------  

# ---------- Plot paramters ----------
golden_ratio = (np.sqrt(5.)-1.)/2
fig_heigth   = fig_width*golden_ratio
f, (ax1)     = plt.subplots(1, figsize=(fig_width, fig_heigth))

ax1.set_title("Molécules d'eau adsorbées")
ax1.set_xlabel("cycles MC")
ax1.set_ylabel("Molécules d'eau adsorbées dans MFI_SI à 0.005 MPa et 300 K")
#ax1.set_xscale('log')

plt.grid(which='both')
# ------------------------------------

data = np.genfromtxt(inputFile,delimiter=",")

MC_cycle    		= data[1:,0]
absolute_ad   		= data[1:,1]   # absolute adsorbate species IN MOF.


ax1.plot(MC_cycle, absolute_ad, label="TIP4P")
ax1.set_ylim(absolute_ad.min(), absolute_ad.max()+10)
plt.axvline(x=400000, linewidth=2, color='k')
#x1.legend(ncol=1, loc=0)
plt.show()


