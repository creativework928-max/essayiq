from __future__ import annotations
import pandas as pd
from sklearn.model_selection import train_test_split
from src.config import settings

def split_dataframe(df: pd.DataFrame, test_size: float=.15, validation_size: float=.15, seed: int|None=None):
    seed=settings.random_seed if seed is None else seed
    if "prompt_id" in df.columns:
        from sklearn.model_selection import GroupShuffleSplit
        groups=df["prompt_id"]
        outer=GroupShuffleSplit(n_splits=1,test_size=test_size,random_state=seed)
        tr_idx,te_idx=next(outer.split(df,groups=groups))
        trainval=df.iloc[tr_idx].copy(); test=df.iloc[te_idx].copy()
        inner=GroupShuffleSplit(n_splits=1,test_size=validation_size/(1-test_size),random_state=seed)
        a,b=next(inner.split(trainval,groups=trainval["prompt_id"]))
        return trainval.iloc[a].copy(),trainval.iloc[b].copy(),test
    trainval,test=train_test_split(df,test_size=test_size,random_state=seed,stratify=df["score"])
    val_fraction=validation_size/(1-test_size)
    train,val=train_test_split(trainval,test_size=val_fraction,random_state=seed,stratify=trainval["score"])
    return train.copy(),val.copy(),test.copy()
