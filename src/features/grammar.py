from __future__ import annotations
import re

def grammar_features(text:str)->dict[str,float]:
    words=re.findall(r"\b[\w'’-]+\b",text)
    repeated=sum(1 for a,b in zip(words,words[1:]) if a.lower()==b.lower())
    repeated_punct=len(re.findall(r"([!?.,;:])\1+",text))
    spacing=len(re.findall(r"[ \t]{2,}",text))
    lowercase_starts=sum(1 for s in re.split(r"(?<=[.!?])\s+",text) if s and s[0].islower())
    fragments=sum(1 for s in re.split(r"(?<=[.!?])\s+",text) if 0<len(re.findall(r"\b[\w'’-]+\b",s))<3)
    return {"repeated_word_signals":float(repeated),"repeated_punctuation_signals":float(repeated_punct),"spacing_anomalies":float(spacing),"capitalization_anomalies":float(lowercase_starts),"fragment_signals":float(fragments)}
