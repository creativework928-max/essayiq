from __future__ import annotations
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

def build_tfidf_ridge():
    features=Pipeline([("word",TfidfVectorizer(ngram_range=(1,2),min_df=2,sublinear_tf=True,max_features=60000))])
    return Pipeline([("tfidf",features),("model",Ridge(alpha=8.0))])
