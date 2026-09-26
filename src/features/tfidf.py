from __future__ import annotations
from scipy.sparse import hstack
from sklearn.feature_extraction.text import TfidfVectorizer

class TfidfFeatureExtractor:
    def __init__(self,max_features=120000):
        self.word=TfidfVectorizer(ngram_range=(1,2),min_df=2,max_features=max_features//2,sublinear_tf=True)
        self.char=TfidfVectorizer(analyzer="char",ngram_range=(3,5),min_df=2,max_features=max_features//2,sublinear_tf=True)
    def fit(self,texts): self.word.fit(texts); self.char.fit(texts); return self
    def transform(self,texts): return hstack([self.word.transform(texts),self.char.transform(texts)],format="csr")
    def fit_transform(self,texts): self.fit(texts); return self.transform(texts)
