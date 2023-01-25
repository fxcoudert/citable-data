import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 
import seaborn as sns 

def rmse(a, b):
    return np.sqrt( np.mean( (a-b)**2 ) )

df_coremof = pd.read_csv('2019-11-01-ASR-internal_14142.csv').rename(columns={'filename':'Structures'}).drop(columns=['Unnamed: 28', 'Unnamed: 29','Unnamed: 30', 'Unnamed: 31', 'Unnamed: 32', 'Unnamed: 33','Unnamed: 34', 'Unnamed: 35', 'Unnamed: 36', 'Unnamed: 37','Unnamed: 38', 'Unnamed: 39', 'Unnamed: 40', 'Unnamed: 41',])
df_widom = pd.read_csv('output_widom_100k.csv')

df_widom['H_Xe_widom'] = df_widom['H_Xe_0_widom']
df_widom['K_Xe_widom'] = df_widom['K_Xe_widom']

df_merge = pd.merge(df_widom, df_coremof, on='Structures', how='left')

acc_list = ['1.0','1.1','1.2','1.3','1.4','1.6','1.8','2.0','2.2','2.4','2.6']

for coeff in acc_list:
    df_surface_acc_coeff = pd.read_csv('Results_surface_radius/output_surface_radius_%s_100k.csv'%coeff)
    df_surface_acc_coeff['Structures'] = df_surface_acc_coeff['Structure_name'].str.rsplit('_',1).str[0]
    df_surface_acc_coeff['H_Xe_surface_acc_%s'%coeff] = df_surface_acc_coeff['Enthalpy_surface_kjmol']
    df_surface_acc_coeff['time_surface_acc_%s'%coeff] = df_surface_acc_coeff['time']
    df_surface_acc_coeff.drop(columns=['Enthalpy_surface_kjmol','time'])

    df_merge = pd.merge(df_merge, df_surface_acc_coeff, on='Structures', how='left', suffixes=('_random','_spiral'))

df_surface_spiral = pd.read_csv('output_surface_spiral_100k.csv')

df_surface_spiral['Structures'] = df_surface_spiral['Structure_name'].str.rsplit('_',1).str[0]
df_surface_spiral['H_Xe_surface_spiral'] = df_surface_spiral['Enthalpy_surface_kjmol']
df_surface_spiral['time_surface_spiral'] = df_surface_spiral['time']
df_surface_spiral.drop(columns=['Enthalpy_surface_kjmol','time'])

df = pd.merge(df_merge, df_surface_spiral, on='Structures', how='left', suffixes=('_random','_spiral'))

df.replace([np.inf,-np.inf],np.nan,inplace=True)

T = 298.0
R = 8.31446261815324
P_0 = 101300          # Pa
mmol2mol = 1e-3

df_plot = df[~(df['DISORDER']=='DISORDER')]
df_plot['LCD'] = df_plot['LCD'].fillna(0)
df_plot = df_plot[~(df_plot['Structures'].isin(["ODONEB_clean","ODONIF_clean"]))]

# Map the error and the time for each method for the structures not NAN for 0.90 
df_out = df_plot[df_plot['LCD']>3.7]
# df_out = df_plot

# method = ["Rmin"]
# rmse_list = [rmse(df_out['H_Xe_surface_spiral'],df_out['H_Xe_widom'])]
# time_list = [df_out['time_surface_spiral'].mean()]
method = []
rmse_list = []
time_list = []

for coeff in acc_list:
    method.append(coeff)
    rmse_list.append(rmse(df_out['H_Xe_surface_acc_%s'%coeff],df_out['H_Xe_widom']))
    time_list.append(df_out['time_surface_acc_%s'%coeff].mean())

df_map = pd.DataFrame(data={'Method':method, 'RMSE (kj/mol)':rmse_list, 'Time (s)':time_list})
plt.rcParams.update({'font.size':14})

plt.figure(figsize=(9.5,5))

palette = sns.color_palette("crest",n_colors=len(df_map))[::]
sns.scatterplot(data=df_map, x="Time (s)", y="RMSE (kj/mol)", hue="Method",palette=palette,s=60)
plt.xlabel('Mean CPU time spent per simulation (s)')
plt.ylabel('RMSE to Widom as a reference (kj/mol)')
# plt.title('Average time spent vs. RMSE labeled by the accessibility coeff. used\n in a 100k-step simulation on structures with PLD>3.7')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title=r"Sphere radius $R_{\lambda}$")
plt.tight_layout()
plt.show()
