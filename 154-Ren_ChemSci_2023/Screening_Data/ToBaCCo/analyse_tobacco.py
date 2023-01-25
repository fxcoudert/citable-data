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

df_widom = pd.read_csv('output_widom_tobacco_100k.csv')
df_widom['Structures'] = df_widom['Structures']
df_surface = pd.read_csv('output_surface_final_tobacco.csv')
df_surface['Structures'] = df_surface['Structure_name']
df_pore = pd.read_csv('tobacco_pores.csv')
df_pore['Structures'] = df_pore['Structures']

df_merge = pd.merge(df_surface,df_widom,how = 'left', on = 'Structures')
df_plot = pd.merge(df_merge,df_pore,how = 'left', on = 'Structures')

df_plot['LCD'] = df_plot['D_i']

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

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xscale(xscale)
    plt.yscale(yscale)
    plt.legend(title=r"LCD ($\AA$)")
    plt.tight_layout()
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    ax.plot([0, 1], [0, 1], transform=ax.transAxes, linestyle="--", color = "gray")
    # plt.savefig("%s_vs_%s_%s_tobacco.jpeg"%(x,y,suff),dpi=280)
    plt.show()

x = 'H_Xe_0_widom'
x_label = r"Reference Xe adsorption enthalpy $\Delta_{ads}H_0^{Xe}$ (Widom insertion)"+'\n'+"ToBaCCo"
y = 'Enthalpy_surface_kjmol'
y_label = r"Surface Xe adsorption enthalpy at infinite dilution (RAESS)"
pairplot(x, y, x_label, y_label,left=-55,right=5,bottom=-55,top=5)
plt.show()

print("RMSE: %.2f"%rmse(df_plot[x],df_plot[y]))
print("MAE: %.2f"%mae(df_plot[x],df_plot[y]))

print("Mean LCD: %.2f"%df_plot['LCD'].mean())
print("#structures with LCD above 10A: %.2f"%len(df_plot[df_plot['LCD']>10]))

