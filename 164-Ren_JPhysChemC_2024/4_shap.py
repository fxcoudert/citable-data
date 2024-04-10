# %%
import pandas as pd 
import numpy as np 
import xgboost as xgb
import matplotlib.pyplot as plt
import shap
import pickle

random_state = 123
T = 298.0
R = 8.31446261815324e-3

# %%
# import training data
df_data = pd.read_csv('data/all_columns.csv',index_col=0)
X_data, y_data, group = df_data.iloc[:,3:], df_data['Diffusion_coefficient_log10'], df_data["unique_chemcomp"]

df_train = pd.read_csv('data/train.csv',index_col=0)
X_train, y_train, group_train = df_train.iloc[:,3:], df_train['Diffusion_coefficient_log10'], df_train["unique_chemcomp"]

df_test = pd.read_csv('data/test.csv',index_col=0)
X_test, y_test, group_test = df_test.iloc[:,3:], df_test['Diffusion_coefficient_log10'], df_test["unique_chemcomp"]

feature_names = X_train.columns

# Load ML model
filename = 'model/final_diffusion_model.sav'
xgb_reg = pickle.load(open(filename, 'rb'))

y_pred_train = xgb_reg.predict(X_train.to_numpy())
df_train = pd.DataFrame(data={'pred':y_pred_train, 'true':y_train.to_numpy()},index=y_train.index).dropna()

y_pred_test = xgb_reg.predict(X_test.to_numpy())
df_test = pd.DataFrame(data={'pred':y_pred_test, 'true':y_test.to_numpy()},index=y_test.index).dropna()

# %%
fig, ax = plt.subplots(figsize=(12,14))
xgb.plot_importance(xgb_reg,ax=ax)
plt.show()


# %%
explainerModel = shap.TreeExplainer(xgb_reg)
X_shap = X_test
shap_values = explainerModel.shap_values(X_shap.to_numpy())
feature_names = X_shap.columns
resultX = pd.DataFrame(shap_values, columns = feature_names)
vals = np.abs(resultX.values).mean(0)

shap_importance = pd.DataFrame(list(zip(feature_names, vals)),columns=['features name','feature_importance_vals']).sort_values(by=['feature_importance_vals'],ascending=True)

fig, ax = plt.subplots()
shap_importance.plot.barh(x="features name", y="feature_importance_vals", ax=ax)
ax.set(xlabel="mean(|SHAP value|) (average impact on model output magnitude)", ylabel="Features")
ax.get_legend().remove()
fig.savefig('plot/Diff_Feature_importance_shapbased.pdf', dpi=240,bbox_inches = 'tight')

# %%
X_shap = df_data[feature_names]
shap_values = explainerModel.shap_values(X_shap.to_numpy())
top_inds = np.argsort(-np.sum(np.abs(shap_values), 0))
# make SHAP plots of the three most important features
for i in range(len(top_inds)):
    shap.dependence_plot(top_inds[i], shap_values, X_shap.to_numpy(),feature_names=feature_names,show=False)
    plt.savefig('PDP/%s.pdf'%feature_names[top_inds[i]].replace('/','_').replace('%','_percent'), dpi=240, bbox_inches='tight')
    plt.show()

# %%
i = df_data[df_data['Structures']=="EWEWUZ_charged"].index[0]
X_out = X_shap.loc[i:i+1,:]
X_out['barrier_kjmol'] = 11.4
shap.plots.waterfall(explainerModel(X_out)[0], max_display=10)

# %%
X_out = X_shap[X_shap['barrier_kjmol']>30]
shap.plots.waterfall(explainerModel(X_out)[0], max_display=10)

# %%
X_out = X_shap[X_shap['D_f_vdw_uff298']>10]
shap.plots.waterfall(explainerModel(X_out)[0], max_display=10)

# %%
X_out = X_shap[(X_shap['D_f_vdw_uff298']>10) & (X_shap['barrier_kjmol']>15)]
shap.plots.waterfall(explainerModel(X_out)[0], max_display=10)
# %%
X_out = X_shap[(X_shap['D_f_vdw_uff298']<4) & (X_shap['barrier_kjmol']<15)]
shap.plots.waterfall(explainerModel(X_out)[0], max_display=10)
# %%
