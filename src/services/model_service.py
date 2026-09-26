from __future__ import annotations
from pathlib import Path
import joblib
from src.config import settings
class ModelService:
    def __init__(self): self.model=None
    @property
    def loaded(self): return self.model is not None
    def load(self):
        if settings.model_file.exists(): self.model=joblib.load(settings.model_file); return True
        return False
    def predict(self,text:str):
        if not self.model: raise RuntimeError("No trained model is loaded")
        raw=float(self.model.predict([text])[0]); return max(settings.min_score,min(settings.max_score,raw))
