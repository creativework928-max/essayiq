from __future__ import annotations
import re, statistics
from collections import Counter
import numpy as np

WORD_RE=re.compile(r"\b[\w'’-]+\b",re.UNICODE)
SENT_RE=re.compile(r"(?<=[.!?])(?:[\"'”’)]*)\s+")

def words(text): return WORD_RE.findall(text)
def sentences(text):
    parts=re.split(r"(?<=[.!?])\s+",text.strip()) if text.strip() else []
    return [p for p in parts if p.strip()]

def linguistic_features(text: str)->dict[str,float]:
    ws=words(text); ss=sentences(text); paras=[p for p in re.split(r"\n\s*\n",text) if p.strip()]
    lens=[len(re.findall(r"\b[\w'’-]+\b",s)) for s in ss]
    wlen=[len(re.sub(r"[^A-Za-z]","",w)) for w in ws]; wlen=[x for x in wlen if x>0]
    uniq=set(w.lower() for w in ws); counts=Counter(w.lower() for w in ws)
    n=len(ws); u=len(uniq)
    return {"char_count":float(len(text)),"alpha_char_count":float(sum(c.isalpha() for c in text)),"word_count":float(n),"sentence_count":float(len(ss)),"paragraph_count":float(len(paras)),"avg_sentence_length":float(np.mean(lens)) if lens else 0.0,"median_sentence_length":float(np.median(lens)) if lens else 0.0,"std_sentence_length":float(np.std(lens)) if lens else 0.0,"min_sentence_length":float(min(lens)) if lens else 0.0,"max_sentence_length":float(max(lens)) if lens else 0.0,"avg_word_length":float(np.mean(wlen)) if wlen else 0.0,"median_word_length":float(np.median(wlen)) if wlen else 0.0,"long_word_pct":float(np.mean(np.array(wlen)>=7)*100) if wlen else 0.0,"short_word_pct":float(np.mean(np.array(wlen)<=3)*100) if wlen else 0.0,"unique_words":float(u),"type_token_ratio":float(u/n) if n else 0.0,"corrected_ttr":float(u/np.sqrt(2*n)) if n else 0.0,"hapax_ratio":float(sum(v==1 for v in counts.values())/u) if u else 0.0,"comma_count":float(text.count(",")),"period_count":float(text.count(".")),"semicolon_count":float(text.count(";")),"colon_count":float(text.count(":")),"question_count":float(text.count("?")),"exclamation_count":float(text.count("!")),"quote_count":float(text.count('"'))}
