import pandas as pd
from src.data.validate import validate_training_data

def test_validation_report():
    df=pd.DataFrame({"essay_id":[1,1],"full_text":["hello",None],"score":[1,7]})
    r=validate_training_data(df)
    assert r["duplicates"]["essay_id"]==1
    assert r["nulls"]["full_text"]==1
    assert r["score_validation"]["above_max"]==1
