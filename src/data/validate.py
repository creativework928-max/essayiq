from __future__ import annotations
import json
import pandas as pd
from src.config import ensure_directories, settings
from src.data.load import load_training_data

def validate_training_data(df: pd.DataFrame) -> dict:
    report={"rows":int(len(df)),"columns":list(df.columns),"required_columns":{c:c in df.columns for c in ["essay_id","full_text","score"]},"duplicates":{},"nulls":{},"score_validation":{},"essay_validation":{}}
    if "essay_id" in df: report["duplicates"]["essay_id"]=int(df["essay_id"].duplicated().sum())
    if "full_text" in df:
        report["nulls"]["full_text"]=int(df["full_text"].isna().sum())
        text=df["full_text"].fillna("").astype(str); lengths=text.str.len()
        report["essay_validation"]={"empty":int((lengths==0).sum()),"short_under_50_chars":int((lengths<settings.min_essay_chars).sum()),"long_over_limit":int((lengths>settings.max_essay_chars).sum()),"duplicate_text":int(text.duplicated().sum()),"min_chars":int(lengths.min()) if len(lengths) else 0,"max_chars":int(lengths.max()) if len(lengths) else 0,"median_chars":float(lengths.median()) if len(lengths) else 0.0}
    if "score" in df:
        scores=pd.to_numeric(df["score"],errors="coerce")
        report["nulls"]["score"]=int(df["score"].isna().sum())
        report["score_validation"]={"non_numeric":int(scores.isna().sum()),"below_min":int((scores<settings.min_score).sum()),"above_max":int((scores>settings.max_score).sum()),"unique_scores":sorted(scores.dropna().unique().tolist())}
    return report

def main()->None:
    ensure_directories(); df=load_training_data(); report=validate_training_data(df); out=settings.reports_dir/"data_quality/data_quality_report.json"; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(report,indent=2),encoding="utf8"); print(json.dumps(report,indent=2))
if __name__=="__main__": main()
