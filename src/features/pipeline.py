from __future__ import annotations
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler
from scipy.sparse import csr_matrix, hstack
from src.features.linguistic import linguistic_features
from src.features.readability import readability_features
from src.features.vocabulary import vocabulary_features
from src.features.grammar import grammar_features
from src.features.structure import structure_features
from src.features.semantic import semantic_features
from src.features.tfidf import TfidfFeatureExtractor

class HybridFeaturePipeline(BaseEstimator,TransformerMixin):
    def __init__(self,max_tfidf_features=120000): self.max_tfidf_features=max_tfidf_features
    def fit(self,X,y=None):
        texts=pd.Series(X).fillna("").astype(str).tolist(); self.tfidf=TfidfFeatureExtractor(self.max_tfidf_features); self.tfidf.fit(texts); self.feature_names=self._numeric_names(); arr=np.array([[d[k] for k in self.feature_names] for d in [self._numeric(t) for t in texts]],dtype=float); self.scaler=StandardScaler(); self.scaler.fit(arr); return self
    def transform(self,X):
        texts=pd.Series(X).fillna("").astype(str).tolist(); sparse=self.tfidf.transform(texts); numeric=csr_matrix(self.scaler.transform(np.array([[d[k] for k in self.feature_names] for d in [self._numeric(t) for t in texts]],dtype=float))); return hstack([sparse,numeric],format="csr")
    def _numeric_names(self): return list(self._numeric("x").keys())
    def _numeric(self,text):
        d={};
        for fn in (linguistic_features,readability_features,vocabulary_features,grammar_features,structure_features,semantic_features): d.update(fn(text))
        return d
