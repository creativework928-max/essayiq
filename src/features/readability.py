from __future__ import annotations
import math, re
try:
    import textstat
except ImportError:
    textstat=None

def _basic(text):
    words=re.findall(r"\b[\w'’-]+\b",text); sentences=max(1,len(re.findall(r"[.!?]+",text))); syllables=0
    for w in words:
        parts=re.findall(r"[aeiouy]+",w.lower()); syllables += max(1,len(parts))
    n=max(1,len(words)); chars=sum(c.isalpha() for c in text)
    fre=206.835-1.015*(n/sentences)-84.6*(syllables/n)
    fk=0.39*(n/sentences)+11.8*(syllables/n)-15.59
    fog=0.4*((n/sentences)+100*sum(max(1,len(re.findall(r"[aeiouy]+",w.lower())))>=3 for w in words)/n)
    ari=4.71*(chars/n)+0.5*(n/sentences)-21.43
    return {"flesch_reading_ease":fre,"flesch_kincaid_grade":fk,"gunning_fog":fog,"smog":3.1291*math.sqrt(max(1,sum(max(1,len(re.findall(r"[aeiouy]+",w.lower())))>=3 for w in words)*30/sentences))-3.3171,"automated_readability_index":ari}

def readability_features(text:str)->dict[str,float]:
    if not text.strip(): return {k:0.0 for k in ["flesch_reading_ease","flesch_kincaid_grade","gunning_fog","smog","automated_readability_index"]}
    if textstat is None: return {k:float(v) for k,v in _basic(text).items()}
    def safe(fn):
        try:return float(fn(text))
        except Exception:return 0.0
    return {"flesch_reading_ease":safe(textstat.flesch_reading_ease),"flesch_kincaid_grade":safe(textstat.flesch_kincaid_grade),"gunning_fog":safe(textstat.gunning_fog),"smog":safe(textstat.smog_index),"automated_readability_index":safe(textstat.automated_readability_index)}
