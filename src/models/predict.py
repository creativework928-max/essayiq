from __future__ import annotations
import joblib
from src.config import settings

def load_model():
    if not settings.model_file.exists(): raise FileNotFoundError(f"Trained model not found: {settings.model_file}. Run python -m src.models.train")
    return joblib.load(settings.model_file)

def predict(text:str,model=None)->float:
    model=model or load_model(); return float(min(settings.max_score,max(settings.min_score,model.predict([text])[0])))
