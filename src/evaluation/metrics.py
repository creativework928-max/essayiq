from __future__ import annotations
import numpy as np
from scipy.stats import pearsonr,spearmanr
from sklearn.metrics import cohen_kappa_score,mean_absolute_error,mean_squared_error

def quadratic_weighted_kappa(y_true,y_pred,min_rating=1,max_rating=6):
    true=np.clip(np.rint(np.asarray(y_true,float)).astype(int),min_rating,max_rating); pred=np.clip(np.rint(np.asarray(y_pred,float)).astype(int),min_rating,max_rating)
    return float(cohen_kappa_score(true,pred,weights="quadratic"))

def regression_metrics(y_true,y_pred):
    true=np.asarray(y_true,float); pred=np.asarray(y_pred,float)
    if true.shape!=pred.shape: raise ValueError("Shapes must match")
    pear=float(pearsonr(true,pred).statistic) if len(true)>1 else 0.0; spear=float(spearmanr(true,pred).statistic) if len(true)>1 else 0.0
    return {"qwk":quadratic_weighted_kappa(true,pred),"mae":float(mean_absolute_error(true,pred)),"rmse":float(np.sqrt(mean_squared_error(true,pred))),"pearson":pear,"spearman":spear,"exact_accuracy":float(np.mean(np.rint(true)==np.rint(pred))),"within_one":float(np.mean(np.abs(np.rint(true)-np.rint(pred))<=1))}
