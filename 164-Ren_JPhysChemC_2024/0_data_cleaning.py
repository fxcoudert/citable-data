# %%
import pandas as pd
import numpy as np
from sklearn.model_selection import GroupShuffleSplit
import chemparse
import math

# %%
df_pore = pd.read_csv('raw_data/zeo/PoreSize_Uff298K_coremof2019.csv')

df_info = pd.read_csv('raw_data/zeo/Zeoinfo_descriptors_coremof2019.csv')
df_info.replace(np.inf,10, inplace=True)
df_chem =  pd.read_csv('raw_data/zeo/zeoinfo_coremof2019.csv')[['Structures','chem_comp']]

df_vol_12 = pd.read_csv('raw_data/zeo/VolumeOccupiable_Uff298K1.2_coremof2019.csv')
df_vol_18 = pd.read_csv('raw_data/zeo/VolumeOccupiable_Uff298K1.8_coremof2019.csv')
df_vol_20 = pd.read_csv('raw_data/zeo/VolumeOccupiable_Uff298K2.0_coremof2019.csv').rename(columns={"PO_VF":"PO_VF_2.0","POA_VF":"POA_VF_2.0","PONA_VF":"PONA_VF_2.0"})
df_vol = pd.merge(df_vol_12,df_vol_18, on="Structures",  how="left", suffixes=("_1.2", "_1.8"))
df_vol = pd.merge(df_vol,df_vol_20, on="Structures",  how="left")

df_sa_12 = pd.read_csv('raw_data/zeo/SurfaceArea_Uff298K1.2_coremof2019.csv')
df_sa_18 = pd.read_csv('raw_data/zeo/SurfaceArea_Uff298K1.8_coremof2019.csv')
df_sa_20 = pd.read_csv('raw_data/zeo/SurfaceArea_Uff298K2.0_coremof2019.csv').rename(columns={"ASA_m2/cm3":"ASA_m2/cm3_2.0","NASA_m2/cm3":"NASA_m2/cm3_2.0", "SA_m2/cm3":"SA_m2/cm3_2.0"})
df_sa = pd.merge(df_sa_12,df_sa_18, how="left", on="Structures", suffixes=("_1.2", "_1.8"))
df_sa = pd.merge(df_sa,df_sa_20, on="Structures",  how="left")

df_chan = pd.read_csv('raw_data/zeo/Channel_Uff298K1.8_coremof2019.csv')

# %%
df_diff = pd.read_csv('raw_data/raspa/Diffusion_xe_CoReMOF.csv')
df_diff['Diffusion_coefficient_log10'] = np.log10(df_diff['Diffusion_coefficient'])
df_diff.dropna(subset=['Diffusion_coefficient_log10'],inplace=True)

df_barrier = pd.read_csv('raw_data/barrier/output_barrier_0.1.csv')
df_barrier['Structures'] = df_barrier['Structures'].str.rsplit('_',1).str[0]

df_barrier['barrier_kjmol'] = df_barrier['Barrier_energy[kJ/mol]'] - df_barrier['Minimum_energy_channel[kJ/mol]']

df_barrier_std = df_barrier.groupby('Structures').std().fillna(0).reset_index()[["Structures","Barrier_energy[kJ/mol]"]].rename(columns={"Barrier_energy[kJ/mol]":"Barrier_energy_std"})

df_barrier_min = df_barrier.groupby('Structures').min().reset_index()

df_core = pd.read_csv('raw_data/raspa/Screening_CoReMOF_Dataset.csv')

df = pd.merge(df_diff, df_barrier_std, how="left", on="Structures")
df = pd.merge(df, df_barrier_min, how="left", on="Structures")
df = pd.merge(df,df_info, on='Structures', how='left')
df = pd.merge(df,df_chem, on='Structures', how='left')
df = pd.merge(df,df_pore, on='Structures', how='left')
df = pd.merge(df,df_chan, on='Structures', how='left')
df = pd.merge(df,df_sa, on='Structures', how='left')
df = pd.merge(df,df_vol, on='Structures', how='left')
df = pd.merge(df,df_core, on='Structures', how='left')

# %%
print(len(df))
df = df[df["DISORDER"]!="DISORDER"]
print(len(df))

# %%
# Data cleaning: remove structures with more than one channel
T = 298.0
R = 8.31446261815324e-3
df = df[(df["r2"]>=0.9)]
print(len(df))
df = df[(df["Barrier_energy_std"]<1)]
print(len(df))

# %%
# Use chemical composition to group materials
df["chemcomp_dict"] = df['chem_comp'].apply(lambda x: chemparse.parse_formula(x))
df['atoms_count'] = df["chemcomp_dict"].apply(lambda x: sum(x.values()))

def unique_chemcomp(chemcomp_dict):
    atomic_symbols = [
    "H",  "He",
    "Li", "Be", "B",  "C",  "N",  "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P",  "S",  "Cl", "Ar",
    "K",  "Ca", "Sc", "Ti", "V",  "Cr", "Mn", "Fe", "Co",
    "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
    "Rb", "Sr", "Y",  "Zr", "Nb", "Mo", "Tc", "Ru", "Rh",
    "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
    "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu",
    "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu",
    "Hf", "Ta", "W",  "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn",
    "Fr", "Ra", "Ac", "Th", "Pa", "U",  "Np", "Pu", "Am",
    "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr",
    "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn",
    "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
    ]
    i, s = 0, 0
    chemcomp_values = chemcomp_dict.values()
    pgcd = int(list(chemcomp_values)[0])
    unique_comp = ""
    for val in chemcomp_values:
        pgcd = math.gcd(pgcd,int(val))
    while s<len(chemcomp_dict) or i<len(atomic_symbols):
        comp_value = chemcomp_dict.get(atomic_symbols[i],0)
        if comp_value != 0:
            unique_comp += atomic_symbols[i]
            unique_comp += "%d"%(int(comp_value)//pgcd)
            s += 1
        i += 1
    return unique_comp

df['unique_chemcomp'] = df["chemcomp_dict"].apply(lambda x: unique_chemcomp(x))

# %%
df['Adsorption_enthalpy'] = df['Adsorption_enthalpy[kJ/mol]']
df["delta_LCD_PLD"] = df["D_if_vdw_uff298"] - df["D_f_vdw_uff298"]

# %%
th = -30
df["pore_diff_restricted"] = df.apply(lambda x: 0 if x["Adsorption_enthalpy"]>th else x['delta_LCD_PLD'], axis=1)

df["1D_chan"] = df["chan_mean_dim"].apply(lambda x: 1 if (x>=1 and x<2) else 0)
df["2D_chan"] = df["chan_mean_dim"].apply(lambda x: 1 if (x>1 and x<=2) else 0)
df["3D_chan"] = df["chan_mean_dim"].apply(lambda x: 1 if x==3 else 0)

df.rename(columns={'Framework Mass [g/mol]':'Framework Mass (g/mol)','Framework Density [kg/m^3]':'Framework Density (kg/m^3)'}, inplace=True)

df.to_csv("data/all_columns.csv")

# %%
feats = [
    'Framework Mass (g/mol)', 
    'Framework Density (kg/m^3)', 
    'ASA_m2/cm3_1.2', 
    'PO_VF_2.0',
    'D_f_vdw_uff298', 
    'D_if_vdw_uff298', 
    'Adsorption_enthalpy', 
    'barrier_kjmol',
    "delta_LCD_PLD",
    "1D_chan",
    "2D_chan",
    "3D_chan"
    ]

y_column = ['Diffusion_coefficient_log10']

# %%
df.replace([np.inf,-np.inf],np.nan,inplace=True)

print(len(df))
df.dropna(subset=feats,inplace=True)
print(len(df))
df.dropna(subset=y_column,inplace=True)
print(len(df))

X = df[feats]
y = df[y_column]

# %%
df[["Structures","unique_chemcomp"]+y_column+feats].to_csv("data/all.csv",index=True)

# %%
random_state=123
test_size=0.2

gss = GroupShuffleSplit(n_splits=1, test_size=test_size,random_state=123)

# %%
train_idx, test_idx = next(gss.split(X=df[feats], y=df[y_column], groups=df["unique_chemcomp"]))

train_data = df.reset_index().iloc[train_idx]
test_data = df.reset_index().iloc[test_idx]

train_data[["Structures","unique_chemcomp"]+y_column+feats].to_csv("data/train.csv",index=True)
train_data.to_csv("data/train_all.csv",index=True)

test_data[["Structures","unique_chemcomp"]+y_column+feats].to_csv("data/test.csv",index=True)
test_data.to_csv("data/test_all.csv",index=True)

# %%