from __future__ import annotations
import json,joblib,pandas as pd
from src.config import settings
from src.data.load import load_training_data
from src.data.clean import clean_training_data
from src.data.split import split_dataframe
from src.evaluation.metrics import regression_metrics

def main():
    if not settings.model_file.exists(): raise FileNotFoundError("Train a model first with python -m src.models.train")
    df=clean_training_data(load_training_data()); _,_,test=split_dataframe(df); model=joblib.load(settings.model_file); pred=model.predict(test["clean_text"]); metrics=regression_metrics(test["score"].to_numpy(),pred)
    out=settings.reports_dir/"metrics/model_evaluation.json"; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(metrics,indent=2),encoding="utf8"); print(json.dumps(metrics,indent=2))
if __name__=="__main__": main()
