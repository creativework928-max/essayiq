from __future__ import annotations
import re, unicodedata
import pandas as pd
CONTROL = re.compile(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]")

def normalize_text(text: str) -> str:
    if not isinstance(text, str): return ""
    text = unicodedata.normalize("NFKC", text)
    text = CONTROL.sub("", text).replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def clean_training_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    out = dataframe.copy()
    out["raw_text"] = out["full_text"].astype("string")
    out["clean_text"] = out["full_text"].map(normalize_text)
    return out
