from __future__ import annotations
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from src.features.pipeline import HybridFeaturePipeline

def build_hybrid(alpha:float=10.0,max_tfidf_features:int=120000):
    return Pipeline([("features",HybridFeaturePipeline(max_tfidf_features=max_tfidf_features)),("regressor",Ridge(alpha=alpha))])
