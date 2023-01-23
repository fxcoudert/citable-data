import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 
import seaborn as sns 

def rmse(a, b):
    return np.sqrt( np.mean( (a-b)**2 ) )
R = 8.31446261815324e-3
T = 298.0

df_coremof = pd.read_csv('2019-11-01-ASR-internal_14142.csv').rename(columns={'filename':'Structures'}).drop(columns=['Unnamed: 28', 'Unnamed: 29','Unnamed: 30', 'Unnamed: 31', 'Unnamed: 32', 'Unnamed: 33','Unnamed: 34', 'Unnamed: 35', 'Unnamed: 36', 'Unnamed: 37','Unnamed: 38', 'Unnamed: 39', 'Unnamed: 40', 'Unnamed: 41',])
df_ref = pd.read_csv('output_widom_100k.csv')
df_widom = pd.merge(df_ref, df_coremof, on='Structures', how='left')
df_widom['H_Xe_widom'] = df_widom['H_Xe_0_widom']

df_surface_spiral_2k = pd.read_csv('output_surface_initial_2k.csv')
df_surface_final_2k = pd.read_csv('output_raess_2k_0.85_1.6.csv')
df_surface_radius_2k = pd.read_csv('output_radius_2k.csv')
df_surface_rejection_2k = pd.read_csv('output_rejection_2k.csv')

df_surface_spiral_2k['Structures'] = df_surface_spiral_2k['Structure_name'].str.rsplit('_',1).str[0]
df_surface_spiral_2k['H_Xe_surface_standard_2k'] = df_surface_spiral_2k['Enthalpy_surface_kjmol']
df_surface_spiral_2k['time_Xe_surface_standard_2k'] = df_surface_spiral_2k['time']

df_surface_final_2k['Structures'] = df_surface_final_2k['Structure_name'].str.rsplit('_',1).str[0]
df_surface_final_2k['H_Xe_surface_final_2k'] = df_surface_final_2k['Enthalpy_surface_kjmol']
df_surface_final_2k['time_Xe_surface_final_2k'] = df_surface_final_2k['time']

df_surface_radius_2k['Structures'] = df_surface_radius_2k['Structure_name'].str.rsplit('_',1).str[0]
df_surface_radius_2k['H_Xe_surface_radius_2k'] = df_surface_radius_2k['Enthalpy_surface_kjmol']
df_surface_radius_2k['time_Xe_surface_radius_2k'] = df_surface_radius_2k['time']

df_surface_rejection_2k['Structures'] = df_surface_rejection_2k['Structure_name'].str.rsplit('_',1).str[0]
df_surface_rejection_2k['H_Xe_surface_rejection_2k'] = df_surface_rejection_2k['Enthalpy_surface_kjmol']
df_surface_rejection_2k['time_Xe_surface_rejection_2k'] = df_surface_rejection_2k['time']

df_voro = pd.read_csv('voronoi_output.csv')
df_voro['Structures'] = df_voro['Structure_name']
df_voro['H_Xe_voronoi'] = df_voro['Boltzmann_average_energy']
df_voro['time_Xe_voronoi'] = 0.43

df_widom_12k = pd.read_csv('output_widom_12k.csv')
df_widom_12k['H_Xe_widom_12k'] = df_widom_12k['H_Xe_0_widom']
df_widom_12k['time_Xe_widom_12k'] = pd.read_csv('time_widom_12k.csv')['CPU_time (s)']

df_merge = pd.merge(df_widom, df_surface_spiral_2k, on='Structures', how='left')
df_merge = pd.merge(df_merge, df_surface_radius_2k, on='Structures', how='left')
df_merge = pd.merge(df_merge, df_surface_rejection_2k, on='Structures', how='left')
df_merge = pd.merge(df_merge, df_surface_final_2k, on='Structures', how='left')
df_merge = pd.merge(df_merge, df_voro, on='Structures', how='left')
df = pd.merge(df_merge, df_widom_12k, on='Structures', how='left')

list_label = ['surface_standard_2k','surface_radius_2k','surface_rejection_2k','surface_final_2k','voronoi','widom_12k']

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

method = []
rmse_list = []
time_list = []

for label in list_label:
    method.append(label)
    rmse_list.append(rmse(df_out['H_Xe_%s'%label],df_out['H_Xe_widom']))
    time_list.append(df_out['time_Xe_%s'%label].mean())

df_map = pd.DataFrame(data={'Method':method, 'RMSE (kj/mol)':rmse_list, 'Time (s)':time_list})
plt.rcParams.update({'font.size':16})
plt.figure(figsize=(10,6))

palette = sns.color_palette(n_colors=len(df_map))[::-1]
sns.scatterplot(data=df_map, x="Time (s)", y="RMSE (kj/mol)", hue="Method",palette=palette,s=240)
plt.ylabel('RMSE to Widom as a reference (kj/mol)')
plt.xlabel('Mean CPU time spent per simulation (s)')
# plt.title('Average time spent vs. RMSE labeled by the accessibility coeff. used\n in a 100k-step simulation on structures with PLD>3.7')
legend = plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title=r"Method")
legend.remove()
plt.tight_layout()
plt.xscale('log')
plt.xlim(left=0.09)
plt.savefig("Sum-up.png",dpi=280)

plt.show()