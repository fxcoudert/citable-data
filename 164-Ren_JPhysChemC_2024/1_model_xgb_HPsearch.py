# %%
import sys
import pandas as pd 
import numpy as np 
from sklearn.model_selection import GroupShuffleSplit
from sklearn.model_selection import RandomizedSearchCV
import xgboost as xgb

# import training data
df_train = pd.read_csv('data/train.csv',index_col=0)
X_train, y_train, group = df_train.iloc[:,3:], df_train['Diffusion_coefficient_log10'], df_train["unique_chemcomp"]

# %%
xgbr = xgb.XGBRegressor()

params_search = { 
           'n_estimators': [1500], 
           'max_depth': [2,3,4],
           'learning_rate': [0.02,0.04,0.06,0.08],
           'colsample_bytree': np.arange(0.7, 1.0, 0.1),
           'colsample_bylevel': np.arange(0.7, 1.0, 0.05),
           'alpha': np.arange(0, 4, 0.2),
           'lambda': [1,1.5,2],
           'subsample': np.arange(0.7, 0.95, 0.05),
         }

s = 1
for key in params_search.keys():
    s *= len(params_search[key])
print(s)

# %%
group_kfold = GroupShuffleSplit(n_splits=5, test_size=0.2, random_state=123)

clf = RandomizedSearchCV(estimator=xgbr,
                         param_distributions=params_search,
                         scoring='neg_mean_squared_error',
                         n_iter=30000,
                         verbose=1,
                         cv=group_kfold.split(X_train, y_train.values, groups=group), 
                         n_jobs=-1,
                         )

clf.fit(X_train, y_train.values)

print("Best parameters:", clf.best_params_)
print("Lowest RMSE: ", np.sqrt(-clf.best_score_))

original_stdout = sys.stdout # Save a reference to the original standard output

with open('data/hyperparameters.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print("Best parameters:", clf.best_params_)
    print("Lowest RMSE: ", np.sqrt(-clf.best_score_))
    sys.stdout = original_stdout # Reset the standard output to its original value

# %%