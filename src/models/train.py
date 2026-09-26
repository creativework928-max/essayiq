from __future__ import annotations
import json
from pathlib import Path
import joblib
import pandas as pd
from src.config import ensure_directories,settings
from src.data.load import load_training_data
from src.data.clean import clean_training_data
from src.data.split import split_dataframe
from src.models.hybrid_model import build_hybrid
from src.evaluation.metrics import regression_metrics
from src.models.registry import write_metadata

def train_and_save():
    ensure_directories(); df=clean_training_data(load_training_data()); train,val,test=split_dataframe(df)
    model=build_hybrid(max_tfidf_features=settings.max_tfidf_features); model.fit(train["clean_text"],train["score"].astype(float))
    val_pred=model.predict(val["clean_text"]); metrics=regression_metrics(val["score"].to_numpy(),val_pred)
    joblib.dump(model,settings.model_file); write_metadata(settings.metadata_file,model_name=settings.model_name,version=settings.model_version,dataset="Learning Agency Lab AES 2.0",score_range=[1,6],features=["TF-IDF word/character n-grams","linguistic","readability","vocabulary","grammar signals","structure","semantic proxies"],metrics=metrics,split_sizes={"train":len(train),"validation":len(val),"test":len(test)},status="trained")
    print(json.dumps(metrics,indent=2)); print(f"Saved model to {settings.model_file}")

if __name__=="__main__": train_and_save()
