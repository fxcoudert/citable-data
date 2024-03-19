# %%
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

random_state = 123
T = 298.0
R = 8.31446261815324e-3

# %%
# import training data
df = pd.read_csv('data/all_columns.csv',index_col=0)
X_data, y_data, group = df.iloc[:,3:], df['Diffusion_coefficient_log10'], df["unique_chemcomp"]
df.rename(columns={"s_0_widom":"s_0"},inplace=True)

df_test = pd.read_csv('data/test.csv',index_col=0)
X_test, y_test, group_test = df_test.iloc[:,3:], df_test['Diffusion_coefficient_log10'], df_test["unique_chemcomp"]
feature_names = list(X_test.columns)

# %%
plt.figure(figsize=(18,18))
cor = df[["Diffusion_coefficient_log10"]+feature_names].corr()
sns.heatmap(cor, annot=True,fmt=".2f", cmap=plt.cm.seismic)
plt.savefig('plot/Feature_restrained_correlation.pdf', dpi=240,bbox_inches = 'tight')
plt.show()

# %%
data = df[["D_f_vdw_uff298","Diffusion_coefficient_log10","barrier_kjmol"]].sort_values(by="barrier_kjmol",ascending=True)
x = data["D_f_vdw_uff298"]
y = data["Diffusion_coefficient_log10"]
z = data['barrier_kjmol']

cmap = sns.color_palette("rocket_r", as_cmap=True)
f, ax = plt.subplots()
points = ax.scatter(x, y, c=z, s=2, alpha=0.8, cmap=cmap)
plt.xlim(left=2.5, right = 12)
plt.ylim(bottom=-11)
plt.ylabel(r"logarithm log$_{10}$(D) of the diffusion coefficeint in cm$^2$/s")
plt.xlabel(r"PLD defined using the UFF-based radii [$\AA$]")
clb = f.colorbar(points)
clb.ax.set_title(r"E_a [kj/mol]",fontsize=8)
plt.savefig('plot/difflog_Df-uff298K_barrier.pdf', dpi=240)

# %%
data = df[["D_f_vdw_uff298","Diffusion_coefficient_log10","barrier_kjmol"]].sort_values(by="barrier_kjmol",ascending=True)
x = data["D_f_vdw_uff298"]
y = data["Diffusion_coefficient_log10"]
z = data['barrier_kjmol']

cmap = sns.color_palette("rocket_r", as_cmap=True)
f, ax = plt.subplots()
points = ax.scatter(x, y, c=z, s=2, alpha=0.8, cmap=cmap)
plt.xlim(left=2.5, right = 12)
plt.ylim(bottom=-11)
plt.ylabel(r"log$_{10}$(D) [cm$^2$/s]")
plt.xlabel(r"Free sphere diameter (new definition) [$\AA$]")
clb = f.colorbar(points)
clb.ax.set_title(r"Barrier energy [kj/mol]",fontsize=8)
plt.savefig('plot/difflog_Df-uff298K_barrier_zoom.pdf', dpi=240)

# %%
data = df[["D_f_vdw_uff298","Diffusion_coefficient_log10","barrier_kjmol"]].sort_values(by="D_f_vdw_uff298",ascending=False)
# data = data[data["D_f_vdw_uff298"]<6]
z = data["D_f_vdw_uff298"]
y = data["Diffusion_coefficient_log10"]
x = data['barrier_kjmol']

cmap = sns.color_palette("tab20", as_cmap=True)
f, ax = plt.subplots()
points = ax.scatter(x, y, c=z, s=2, alpha=0.8, cmap=cmap)
# plt.xlim(left=2.5, right = 12)
# plt.ylim(bottom=-11)
plt.ylabel(r"log$_{10}$(D) [cm$^2$/s]")
plt.xlabel(r"Barrier energy [kj/mol]")
clb = f.colorbar(points)
clb.ax.set_title(r"PLD [$\AA$]",fontsize=8)
plt.savefig('plot/difflog_barrier_Df_uff.pdf', dpi=240)

# %%
data = df[["D_f_vdw_uff298","Diffusion_coefficient_log10","barrier_kjmol"]].sort_values(by="D_f_vdw_uff298",ascending=True)
data = data[data["D_f_vdw_uff298"]>6]
z = data["D_f_vdw_uff298"]
y = data["Diffusion_coefficient_log10"]
x = data['barrier_kjmol']

cmap = sns.color_palette("coolwarm", as_cmap=True)
f, ax = plt.subplots()
points = ax.scatter(x, y, c=z, s=2, alpha=0.8, cmap=cmap)
# plt.xlim(left=2.5, right = 12)
# plt.ylim(bottom=-11)
plt.ylabel(r"log$_{10}$(D) [cm$^2$/s]")
plt.xlabel(r"Barrier energy [kj/mol]")
clb = f.colorbar(points)
clb.ax.set_title(r"PLD [$\AA$]",fontsize=8)
plt.savefig('plot/difflog_barrier_Df_uff_2.pdf', dpi=240)

# %%
df["s_0_log"] = np.log10(df['s_0'])
data = df[["D_f","Diffusion_coefficient_log10","s_0_log"]].sort_values(by="s_0_log",ascending=True)
data = data[data["D_f"]>3]
x = data["D_f"]
y = data["Diffusion_coefficient_log10"]
z = data['s_0_log']

cmap = sns.color_palette("rocket_r", as_cmap=True)
f, ax = plt.subplots()
points = ax.scatter(x, y, c=z, s=2, alpha=0.8, cmap=cmap)
plt.xlim(left=2.5, right = 12)
plt.ylim(bottom=-11)
plt.ylabel(r"log$_{10}$(D) [cm$^2$/s]")
plt.xlabel(r"Free sphere diameter (PLD$_{{CCDC}}$) [$\AA$]")
clb = f.colorbar(points)
clb.ax.set_title(r"$\log_{10}(s_0)$",fontsize=8)
plt.savefig('plot/D_log-diameter_ccdc_colored_s_+.pdf', dpi=240)

# %%
df["s_0_log"] = np.log10(df['s_0'])
data = df[["D_f_vdw_uff298","Diffusion_coefficient_log10","s_0_log"]].sort_values(by="s_0_log",ascending=True)
data = data[data["D_f_vdw_uff298"]>3]
x = data["D_f_vdw_uff298"]
y = data["Diffusion_coefficient_log10"]
z = data['s_0_log']

cmap = sns.color_palette("rocket_r", as_cmap=True)
f, ax = plt.subplots()
points = ax.scatter(x, y, c=z, s=2, alpha=0.8, cmap=cmap)
lim = 4.6
ax.plot([(lim-2.5)/(12-2.5), (lim-2.5)/(12-2.5)], [0, 1], transform=ax.transAxes, linestyle="--", alpha=0.8, color = "gray")

plt.xlim(left=2.5, right = 12)
plt.ylim(bottom=-11)
plt.ylabel(r"log$_{10}$(D) [cm$^2$/s]")
plt.xlabel(r"Free sphere diameter (PLD$_{{UFF}}$) [$\AA$]")
clb = f.colorbar(points)
clb.ax.set_title(r"$\log_{10}(s_0)$",fontsize=8)
plt.savefig('plot/D_log-diameter_colored_s_+.pdf', dpi=240)

# %%
df["s_0_log"] = np.log10(df['s_0'])
data = df[["PO_VF_2.0","Diffusion_coefficient_log10","s_0_log"]].sort_values(by="s_0_log",ascending=True)
# data = data[data["PO_VF_2.0"]>3]
x = data["PO_VF_2.0"]
y = data["Diffusion_coefficient_log10"]
z = data['s_0_log']

cmap = sns.color_palette("rocket_r", as_cmap=True)
f, ax = plt.subplots()
points = ax.scatter(x, y, c=z, s=2, alpha=0.8, cmap=cmap)
# plt.xlim(left=2.5, right = 12)
# plt.ylim(bottom=-11)
plt.ylabel(r"log$_{10}$(D) [cm$^2$/s]")
plt.xlabel(r"Void Fraction for a $2$ $\AA$-radius probe")
clb = f.colorbar(points)
clb.ax.set_title(r"$\log_{10}(s_0)$",fontsize=8)
plt.savefig('plot/D_log-vf_2_s_+.pdf', dpi=240)

# %%
df["s_0_log"] = np.log10(df['s_0'])
data = df[["ASA_m2/cm3_1.2","Diffusion_coefficient_log10","s_0_log"]].sort_values(by="s_0_log",ascending=True)
x = data["ASA_m2/cm3_1.2"]
y = data["Diffusion_coefficient_log10"]
z = data['s_0_log']

cmap = sns.color_palette("rocket_r", as_cmap=True)
f, ax = plt.subplots()
points = ax.scatter(x, y, c=z, s=2, alpha=0.8, cmap=cmap)
# plt.xlim(left=2.5, right = 12)
# plt.ylim(bottom=-11)
plt.ylabel(r"log$_{10}$(D) [cm$^2$/s]")
plt.xlabel(r"Accessible surface area for a $1.2$ $\AA$-radius probe")
clb = f.colorbar(points)
clb.ax.set_title(r"$\log_{10}(s_0)$",fontsize=8)
plt.savefig('plot/D_log-sa_12_s_+.pdf', dpi=240)

# %%
df["s_0_log"] = np.log10(df['s_0'])
data = df[["H_Xe_0_widom","Diffusion_coefficient_log10","s_0_log"]].sort_values(by="s_0_log",ascending=True)
x = data["H_Xe_0_widom"]
y = data["Diffusion_coefficient_log10"]
z = data['s_0_log']

cmap = sns.color_palette("rocket_r", as_cmap=True)
f, ax = plt.subplots()
points = ax.scatter(x, y, c=z, s=2, alpha=0.8, cmap=cmap)
# plt.xlim(left=2.5, right = 12)
# plt.ylim(bottom=-11)
plt.ylabel(r"log$_{10}$(D) [cm$^2$/s]")
plt.xlabel(r"Xenon adsorption enthalpy at infinite dilution (Widom insertion)")
clb = f.colorbar(points)
clb.ax.set_title(r"$\log_{10}(s_0)$",fontsize=8)
plt.savefig('plot/D_log-H_Xe_s_+.pdf', dpi=240)

# %%
df["s_0_log"] = np.log10(df['s_0'])
data = df[["D_if_vdw_uff298","Diffusion_coefficient_log10","s_0_log"]].sort_values(by="s_0_log",ascending=True)
x = data["D_if_vdw_uff298"]
y = data["Diffusion_coefficient_log10"]
z = data['s_0_log']

cmap = sns.color_palette("rocket_r", as_cmap=True)
f, ax = plt.subplots()
points = ax.scatter(x, y, c=z, s=2, alpha=0.8, cmap=cmap)
plt.xlim(left=2.5, right = 12)
plt.ylim(bottom=-11)
plt.ylabel(r"log$_{10}$(D) [cm$^2$/s]")
plt.xlabel(r"D$_{if}$ [$\AA$]")
clb = f.colorbar(points)
clb.ax.set_title(r"$\log_{10}(s_0)$",fontsize=8)
plt.savefig('plot/D_log-lcd_s_+.pdf', dpi=240)

# %%
df["s_0_log"] = np.log10(df['s_0'])
data = df[["Framework Density (kg/m^3)","Diffusion_coefficient_log10","s_0_log"]].sort_values(by="s_0_log",ascending=True)
x = data["Framework Density (kg/m^3)"]
y = data["Diffusion_coefficient_log10"]
z = data['s_0_log']

cmap = sns.color_palette("rocket_r", as_cmap=True)
f, ax = plt.subplots()
points = ax.scatter(x, y, c=z, s=2, alpha=0.8, cmap=cmap)
# plt.xlim(left=2.5, right = 12)
# plt.ylim(bottom=-11)
plt.ylabel(r"log$_{10}$(D) [cm$^2$/s]")
plt.xlabel(r"Framework Density [kg/m^3]")
clb = f.colorbar(points)
clb.ax.set_title(r"$\log_{10}(s_0)$",fontsize=8)
plt.savefig('plot/D_log-density_s_+.pdf', dpi=240)

# %%
df["s_0_log"] = np.log10(df['s_0'])
data = df[["Framework Mass (g/mol)","Diffusion_coefficient_log10","s_0_log"]].sort_values(by="s_0_log",ascending=True)
x = data["Framework Mass (g/mol)"]
y = data["Diffusion_coefficient_log10"]
z = data['s_0_log']

cmap = sns.color_palette("rocket_r", as_cmap=True)
f, ax = plt.subplots()
points = ax.scatter(x, y, c=z, s=2, alpha=0.8, cmap=cmap)
plt.xlim(left=0, right = 15000)
plt.ylim(bottom=-11)
plt.ylabel(r"log$_{10}$(D) [cm$^2$/s]")
plt.xlabel(r"Framework Mass (g/mol)")
clb = f.colorbar(points)
clb.ax.set_title(r"$\log_{10}(s_0)$",fontsize=8)
plt.savefig('plot/D_log-mass_s_+.pdf', dpi=240)

# %%
df["s_0_log"] = np.log10(df['s_0'])
data = df[["chan_mean_dim","Diffusion_coefficient_log10","s_0_log"]].sort_values(by="s_0_log",ascending=True)
x = data["chan_mean_dim"]
y = data["Diffusion_coefficient_log10"]
z = data['s_0_log']

cmap = sns.color_palette("rocket_r", as_cmap=True)
f, ax = plt.subplots()
points = ax.scatter(x, y, c=z, s=2, alpha=0.8, cmap=cmap)
# plt.xlim(left=0, right = 15000)
# plt.ylim(bottom=-11)
plt.ylabel(r"log$_{10}$(D) [cm$^2$/s]")
plt.xlabel(r"Mean channel dimension")
clb = f.colorbar(points)
clb.ax.set_title(r"$\log_{10}(s_0)$",fontsize=8)
plt.savefig('plot/D_log-channdim_s_+.pdf', dpi=240)

# %%
data = df[["chan_mean_dim","Diffusion_coefficient_log10","D_f_vdw_uff298"]]
data= data[data["chan_mean_dim"]==1]
z = data["chan_mean_dim"]
y = data["Diffusion_coefficient_log10"]
x = data['D_f_vdw_uff298']

f, ax = plt.subplots()
points = ax.scatter(x, y, c="tab:green", s=2, alpha=0.8, cmap=cmap)
plt.xlim(left=3, right = 12)
plt.ylim(top=-3.3,bottom=-11)
plt.ylabel(r"log$_{10}$(D) [cm$^2$/s]")
plt.xlabel(r"PLD$_{UFF}$")
plt.title("(a) 1D channel")
plt.savefig('plot/D_log-PLD_1D_chan.pdf', dpi=240)

# %%
data = df[["chan_mean_dim","Diffusion_coefficient_log10","D_f_vdw_uff298"]]
data= data[data["chan_mean_dim"]==2]
z = data["chan_mean_dim"]
y = data["Diffusion_coefficient_log10"]
x = data['D_f_vdw_uff298']

f, ax = plt.subplots()
points = ax.scatter(x, y, c="tab:purple", s=2, alpha=0.8, cmap=cmap)
plt.xlim(left=3, right = 12)
plt.ylim(top=-3.3,bottom=-11)
plt.ylabel(r"log$_{10}$(D) [cm$^2$/s]")
plt.xlabel(r"PLD$_{UFF}$")
plt.title("(b) 2D channel")
plt.savefig('plot/D_log-PLD_2D_chan.pdf', dpi=240)

# %%
data = df[["chan_mean_dim","Diffusion_coefficient_log10","D_f_vdw_uff298"]]
data= data[data["chan_mean_dim"]==3]
z = data["chan_mean_dim"]
y = data["Diffusion_coefficient_log10"]
x = data['D_f_vdw_uff298']

f, ax = plt.subplots()
points = ax.scatter(x, y, c="tab:brown", s=2, alpha=0.8, cmap=cmap)
plt.xlim(left=3, right = 12)
plt.ylim(top=-3.3,bottom=-11)
plt.ylabel(r"log$_{10}$(D) [cm$^2$/s]")
plt.xlabel(r"PLD$_{UFF}$")
plt.title("(c) 3D channel")
plt.savefig('plot/D_log-PLD_3D_chan.pdf', dpi=240)

# %%
plt.title("(a) 1D channels")
plt.xlim(left=-10, right=-2.5)
df[df["chan_mean_dim"]==1]["Diffusion_coefficient_log10"].hist(bins=np.arange(-9.5,-1.5,0.5), edgecolor='black', grid=False,  density=False, color="tab:green")

plt.xlabel(r"log$_{10}$(D) [cm$^2$/s]")
plt.ylabel("Count in the dataset")
plt.savefig("plot/histogram_chan1D.pdf",dpi=280)

# %%
plt.title("(b) 2D channels")
plt.xlim(left=-10, right=-2.5)
df[df["chan_mean_dim"]==2]["Diffusion_coefficient_log10"].hist(bins=np.arange(-9.5,-1.5,0.5), edgecolor='black', grid=False,  density=False, color="tab:purple")

plt.xlabel(r"log$_{10}$(D) [cm$^2$/s]")
plt.ylabel("Count in the dataset")
plt.savefig("plot/histogram_chan2D.pdf",dpi=280)

# %%
plt.title("(c) 3D channels")
plt.xlim(left=-10, right=-2.5)
df[df["chan_mean_dim"]==3]["Diffusion_coefficient_log10"].hist(bins=np.arange(-9.5,-1.5,0.5), edgecolor='black', grid=False,  density=False, color="tab:brown")

plt.xlabel(r"log$_{10}$(D) [cm$^2$/s]")
plt.ylabel("Count in the dataset")
plt.savefig("plot/histogram_chan3D.pdf",dpi=280)

# %%
data = df[["pore_diff_restricted","Diffusion_coefficient_log10","chan_mean_dim"]]
z = data["chan_mean_dim"]
y = data["Diffusion_coefficient_log10"]
x = data['pore_diff_restricted']

f, ax = plt.subplots()
points = ax.scatter(x, y, c="tab:purple", s=2, alpha=0.8, cmap=cmap)
# plt.xlim(left=3, right = 12)
plt.ylim(top=-3.3,bottom=-11)
plt.ylabel(r"log$_{10}$(D) [cm$^2$/s]")
plt.xlabel(r"PLD$_{UFF}$")
plt.title("(b) 2D channel")
# plt.savefig('plot/D_log-PLD_2D_chan.pdf', dpi=240)

# %%
