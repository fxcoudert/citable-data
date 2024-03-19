# %%
import pandas as pd 
import numpy as np 
import xgboost as xgb
import matplotlib.pyplot as plt
import seaborn as sns
import shap
import pickle

random_state = 123
T = 298.0
R = 8.31446261815324e-3

# %%
# import training data
df_data = pd.read_csv('data/train.csv',index_col=0)
X_data, y_data, group = df_data.iloc[:,3:], df_data['Diffusion_coefficient_log10'], df_data["unique_chemcomp"]

df_train = pd.read_csv('data/train.csv',index_col=0)
X_train, y_train, group_train = df_train.iloc[:,3:], df_train['Diffusion_coefficient_log10'], df_train["unique_chemcomp"]

df_test = pd.read_csv('data/test.csv',index_col=0)
X_test, y_test, group_test = df_test.iloc[:,3:], df_test['Diffusion_coefficient_log10'], df_test["unique_chemcomp"]

# %%
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
fig = plt.figure()
ax = fig.add_subplot(111)
sns.scatterplot(x='true', y='pred', data=df_train, s=10, alpha=1, ax=ax,label="Training set (%d structures)"%len(df_train))
sns.scatterplot(x='true', y='pred', data=df_test, s=10, alpha=1, ax=ax, label="Test set (%d structures)"%len(df_test))
ax.set(xlabel=r"True log$_{10}$ of the Diffusion coefficient [cm$^2$/s] ", 
ylabel=r"ML Predicted log$_{10}$ of the Diffusion coefficient [cm$^2$/s]")
ax.set_aspect('equal', adjustable='box')
ax.plot([0, 1], [0, 1], transform=ax.transAxes, linestyle="--", color = "gray")
# plt.xlim(right=10)
# plt.ylim(top=10)
plt.savefig('plot/diffusion_prediction.pdf', dpi=240)

# %%
