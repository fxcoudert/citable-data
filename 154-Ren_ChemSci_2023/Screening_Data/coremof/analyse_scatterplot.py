# %%
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 
import seaborn as sns 
def rmse(a, b):
    return np.sqrt( np.mean( (a-b)**2 ) )
def mae(a, b):
    return np.mean( abs(a-b) )
R = 8.31446261815324e-3
T = 298.0

df_coremof = pd.read_csv('2019-11-01-ASR-internal_14142.csv').rename(columns={'filename':'Structures'}).drop(columns=['Unnamed: 28', 'Unnamed: 29','Unnamed: 30', 'Unnamed: 31', 'Unnamed: 32', 'Unnamed: 33','Unnamed: 34', 'Unnamed: 35', 'Unnamed: 36', 'Unnamed: 37','Unnamed: 38', 'Unnamed: 39', 'Unnamed: 40', 'Unnamed: 41',])
df_ref = pd.read_csv('output_widom_100k.csv')

df_widom = pd.merge(df_ref, df_coremof, on='Structures', how='left')
df_surface_final = pd.read_csv('output_raess_2k_0.85_1.6.csv')
df_surface_spiral = pd.read_csv('output_surface_spiral_100k.csv')

df_voronoi = pd.read_csv('voronoi_output.csv')

df_voronoi['Structures'] = df_voronoi['Structure_name']

df_widom['H_Xe_widom'] = df_widom['H_Xe_0_widom']
df_widom['K_Xe_widom'] = df_widom['K_Xe_widom']

df_surface_final['Structures'] = df_surface_final['Structure_name'].str.rsplit('_',1).str[0]
df_surface_final['sym'] = df_surface_final['Structure_name'].str.rsplit('_',1).str[1].astype(int)
df_surface_final['H_Xe_surface_final'] = df_surface_final['Enthalpy_surface_kjmol']
df_surface_final['K_Xe_surface_final'] = df_surface_final['Henry_coeff_molkgPa']
df_surface_final['SA_final'] = df_surface_final['ASA_m2_cm3']
df_surface_final['time_final'] = df_surface_final['time']
df_surface_final.drop(columns=['Enthalpy_surface_kjmol','Henry_coeff_molkgPa'])

df_surface_spiral['Structures'] = df_surface_spiral['Structure_name'].str.rsplit('_',1).str[0]
df_surface_spiral['H_Xe_surface_spiral'] = df_surface_spiral['Enthalpy_surface_kjmol']
df_surface_spiral['K_Xe_surface_spiral'] = df_surface_spiral['Henry_coeff_molkgPa']
df_surface_spiral.drop(columns=['Enthalpy_surface_kjmol','Henry_coeff_molkgPa'])

df_merge = pd.merge(df_widom, df_surface_final, on='Structures', how='left')
df_merge = pd.merge(df_merge, df_surface_spiral, on='Structures', how='left')
df = pd.merge(df_merge, df_voronoi, on='Structures', how='left') 

# %%
df.replace([np.inf,-np.inf],np.nan,inplace=True)

P_0 = 101300          # Pa
mmol2mol = 1e-3

df_plot = df[~(df['DISORDER']=='DISORDER')]
df_plot['LCD'] = df_plot['LCD'].fillna(0)
df_plot = df_plot[~(df_plot['Structures'].isin(["ODONEB_clean","ODONIF_clean"]))]

# %%
def split_deviation(x):
    i=0
    if np.isnan(x):
        return np.nan
    elif x>10:
        return "]10;40["
    while i < 4:
        if 10-2*(i+1)<x<=10-2*i:
            return "]%.1f;%.1f]"%(10-2*(i+1),10-2*i)
        i += 1
    return "[0;%.1f["%(10-2*(i))


# %%
def pairplot(x, y, x_label, y_label,left=-70,right=160,bottom=-70,top=160, xscale='linear', yscale='linear', suff="overview"):
    plt.rcParams.update({'font.size':12})
    hue = 'LCD'
    df_plot[hue+"_cat"] = df_plot[hue].apply(split_deviation)
    plt.figure(figsize=(7,7))
    hue_order=[split_deviation(11-2*i) for i in range(6)]
    palette = sns.color_palette("tab10",n_colors=len(hue_order))

    sns.scatterplot(data=df_plot.dropna(subset=[x,y,hue]),x=x,y=y,hue=hue+"_cat",hue_order=hue_order,palette=palette,alpha=0.8,s=15)
    plt.xlim(left=left,right=right)
    plt.ylim(bottom=bottom,top=top)

    # plt.title("Selectivity at ambient pressure (20:80) vs Selectivity at low pressure")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xscale(xscale)
    plt.yscale(yscale)
    plt.legend(title=r"LCD ($\AA$)")
    plt.tight_layout()
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    ax.plot([0, 1], [0, 1], transform=ax.transAxes, linestyle="--", color = "gray")
    # plt.savefig("plot/%s_vs_%s_%s.jpeg"%(x,y,suff),dpi=280)
    plt.show()

# %%
x = 'H_Xe_widom'
x_label = r"Reference Xe adsorption enthalpy $\Delta_{ads}H_0^{Xe}$ (Widom insertion)"
y = 'Boltzmann_average_energy'
y_label = r"Voronoi Xe adsorption enthalpy at infinite dilution (Voronoi sampling)"
pairplot(x, y, x_label, y_label,left=-70,right=160,bottom=-70,top=160)

# %%
print(rmse(df_plot[x],df_plot[y]))
print(mae(df_plot[x],df_plot[y]))

print(rmse(df_plot[df_plot['LCD']>3.7][x],df_plot[df_plot['LCD']>3.7][y]))
print(mae(df_plot[df_plot['LCD']>3.7][x],df_plot[df_plot['LCD']>3.7][y]))
# %%
x = 'H_Xe_widom'
x_label = r"Reference Xe adsorption enthalpy $\Delta_{ads}H_0^{Xe}$ (Widom insertion)"
y = 'H_Xe_surface_spiral'
y_label = r"Surface Xe adsorption enthalpy (RAESS)"
pairplot(x, y, x_label, y_label,left=-70,right=160,bottom=-70,top=160)

# %%
print(rmse(df_plot[x],df_plot[y]))
print(mae(df_plot[x],df_plot[y]))

print(rmse(df_plot[df_plot['LCD']>3.7][x],df_plot[df_plot['LCD']>3.7][y]))
print(mae(df_plot[df_plot['LCD']>3.7][x],df_plot[df_plot['LCD']>3.7][y]))

# %%
rmse(df_plot[df_plot['LCD']>3.7][x],df_plot[df_plot['LCD']>3.7][y])
# %%
df_plot[df_plot['LCD']>3.7][[x, y]].corr(method="pearson")

# %%
rmse(df_plot[x],df_plot[y])
# %%
df_plot[[x, y]].corr(method="pearson")

# %%
x = 'K_Xe_widom'
x_label = r"Reference Henry coefficient $K_H^{Xe}$ calculated by Widom insertion"
y = 'K_Xe_surface_spiral'
y_label = r"Surface Henry coefficient $K_H^{Xe}$ calculated by our initial algorithm"
pairplot(x, y, x_label, y_label,left=1e-54,right=1e1,bottom=1e-54,top=1e1, xscale='log', yscale='log')

# %%
x = 'K_Xe_widom'
x_label = r"Reference Henry coefficient $K_H^{Xe}$ calculated by Widom insertion"
y = 'K_Xe_surface_spiral'
y_label = r"Surface Henry coefficient $K_H^{Xe}$ calculated by our initial algorithm"
pairplot(x, y, x_label, y_label,left=1e-12,right=1e2,bottom=1e-12,top=1e2, xscale='log', yscale='log')

# %%
df_plot = df_plot[df_plot['LCD']>3.7]

# %%
x = 'H_Xe_widom'
x_label = r"Reference adsorption enthalpy $\Delta_{ads}H_0^{Xe}$ calculated by Widom insertion"
y = 'H_Xe_surface_spiral'
y_label = r"Surface adsorption enthalpy $\Delta_{ads}H_0^{Xe}$""\ncalculated by our initial algorithm"
pairplot(x, y, x_label, y_label,left=-60,right=10,bottom=-60,top=10,suff="zoom")

# %%
x = 'H_Xe_widom'
x_label = r"Reference adsorption enthalpy $\Delta_{ads}H_0^{Xe}$ calculated by Widom insertion"
y = 'H_Xe_surface_final'
y_label = r"Surface adsorption enthalpy $\Delta_{ads}H_0^{Xe}$""\ncalculated by our final algorithm"
pairplot(x, y, x_label, y_label,left=-60,right=10,bottom=-60,top=10,suff="zoom")

# %%
print(rmse(df_plot[x],df_plot[y]))
print(mae(df_plot[x],df_plot[y]))

# %%
x = 'K_Xe_widom'
x_label = r"Reference Henry coefficient $K_H^{Xe}$ calculated by Widom insertion"
y = 'K_Xe_surface_final'
y_label = r"Surface Henry coefficient $K_H^{Xe}$ calculated by our algorithm"
pairplot(x, y, x_label, y_label,left=1e-11,right=1e1,bottom=1e-11,top=1e1, xscale='log', yscale='log',suff="zoom")

# %%
rmse(df_plot[x],df_plot[y])

df_plot[[x, y]].corr(method="pearson")
