from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_basic_eda(df:pd.DataFrame,out:Path):
    out.mkdir(parents=True,exist_ok=True); text=df["full_text"].fillna("").astype(str); words=text.str.split().str.len()
    plt.figure(); df["score"].value_counts().sort_index().plot(kind="bar"); plt.title("Score Distribution"); plt.tight_layout(); plt.savefig(out/"score_distribution.png",dpi=160); plt.close()
    plt.figure(); words.plot(kind="hist",bins=40); plt.title("Word Count Distribution"); plt.tight_layout(); plt.savefig(out/"word_count_distribution.png",dpi=160); plt.close()
    plt.figure(); plt.scatter(words,df["score"],s=8,alpha=.25); plt.xlabel("Word count"); plt.ylabel("Score"); plt.tight_layout(); plt.savefig(out/"score_vs_word_count.png",dpi=160); plt.close()
