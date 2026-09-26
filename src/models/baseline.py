from __future__ import annotations
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor, HistGradientBoostingRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def mean_baseline(y): return float(np.mean(y))

def numerical_ridge(X,y,alpha=1.0): return Pipeline([("scale",StandardScaler()),("model",Ridge(alpha=alpha))]).fit(X,y)

def tree_models():
    return {"random_forest":RandomForestRegressor(n_estimators=300,min_samples_leaf=2,n_jobs=-1,random_state=42),"hist_gradient_boosting":HistGradientBoostingRegressor(max_iter=300,learning_rate=.05,max_leaf_nodes=31,random_state=42)}
