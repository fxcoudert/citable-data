# %%
import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
import xgboost as xgb
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import pickle

def rmse(a,b):
    return np.sqrt( np.mean ((a-b)**2) )
def mae(a,b):
    return np.mean( abs( a-b ) )

random_state = 123

# %%
# import training data
df_train = pd.read_csv('data/train.csv',index_col=0)
X_train, y_train, group_train = df_train.iloc[:,3:], df_train['Diffusion_coefficient_log10'], df_train["unique_chemcomp"]

df_test = pd.read_csv('data/test.csv',index_col=0)
X_test, y_test, group_test = df_test.iloc[:,3:], df_test['Diffusion_coefficient_log10'], df_test["unique_chemcomp"]

# %%
# parameters taken from data/hyperparameters.txt
params = {
    'objective':'reg:squarederror',
    'n_estimators':1500,
    'max_depth': 5,
    'colsample_bytree':0.9,
    'colsample_bylevel':0.75,
    'subsample':0.7,
    'alpha': 0.4,
    'lambda':0.5,
    'gamma' :0,
    'learning_rate': 0.04,
}

# %%
xgb_reg = xgb.XGBRegressor(**params,random_state=random_state)
xgb_reg.fit(X_train, y_train.to_numpy())

# %%
y_pred_train = xgb_reg.predict(X_train.to_numpy())
df_train = pd.DataFrame(data={'pred':y_pred_train, 'true':y_train.to_numpy()},index=y_train.index).dropna()

rmse_train = rmse(df_train['pred'],df_train['true'])
print("RMSE train:%s"%rmse_train)

mae_train = mae(df_train['pred'],df_train['true'])
print("MAE train:%s"%mae_train)

y_pred_test = xgb_reg.predict(X_test.to_numpy())
df_test = pd.DataFrame(data={'pred':y_pred_test, 'true':y_test.to_numpy()},index=y_test.index).dropna()

# data = df_test[df_test['true']<0]
rmse_test = rmse(df_test['pred'],df_test['true'])
print("RMSE test:%s"%rmse_test)

mae_test = mae(df_test['pred'],df_test['true'])
print("MAE test:%s"%mae_test)

r2_test = r2_score(df_test['pred'],df_test['true'])
print("R2 score on log test:%s"%r2_test)

# %%
RMSE = []
MAE = []
frac = [0.2,0.4,0.5,0.6,0.7,0.8,0.85,0.9,0.95]
for q in frac:
    xgb_reg_temp = xgb.XGBRegressor(**params,random_state=random_state)
    X_temp, _, y_temp, _ = train_test_split(X_train, y_train, test_size=1-q, random_state=random_state)
    xgb_reg_temp.fit(X_temp, y_temp.to_numpy())
    y_pred_test = xgb_reg_temp.predict(X_test.to_numpy())
    df_test = pd.DataFrame(data={'pred':y_pred_test, 'true':y_test.to_numpy()},index=y_test.index).dropna()
    RMSE.append(rmse(df_test['pred'],df_test['true']))
    MAE.append(mae(df_test['pred'],df_test['true']))

frac.append(1)
RMSE.append(rmse_test)
MAE.append(mae_test)

# %%
plt.plot(frac,RMSE)
plt.xlabel("Fraction of the initial training set")
plt.ylabel("RMSE on the same test size (kJ/mol)")
plt.savefig("plot/training_curve.pdf", dpi=440)
plt.show()

# %%
filename = 'model/final_diffusion_model.sav'
pickle.dump(xgb_reg, open(filename, 'wb'))

# %%
