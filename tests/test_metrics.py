import numpy as np
from src.evaluation.metrics import quadratic_weighted_kappa,regression_metrics

def test_qwk_perfect():
    y=np.array([1,2,3,4,5,6]); assert quadratic_weighted_kappa(y,y)==1.0

def test_metrics_keys():
    m=regression_metrics(np.array([1,2,3]),np.array([1.,2.,3.]))
    assert set(m)=={"qwk","mae","rmse","pearson","spearman","exact_accuracy","within_one"}
    assert m["mae"]==0
