from __future__ import annotations
import re, math
from collections import Counter
WORD_RE=re.compile(r"\b[\w'’-]+\b",re.UNICODE)

def vocabulary_features(text:str)->dict[str,float]:
    ws=WORD_RE.findall(text); low=[w.lower() for w in ws]; counts=Counter(low); n=len(low); u=len(counts)
    return {"vocabulary_size":float(u),"lexical_diversity":float(u/n) if n else 0.0,"average_word_length":float(sum(map(len,low))/n) if n else 0.0,"long_word_ratio":float(sum(len(w)>=7 for w in low)/n) if n else 0.0,"rare_word_signal":float(sum(v==1 for v in counts.values())/u) if u else 0.0,"hapax_count":float(sum(v==1 for v in counts.values()))}
