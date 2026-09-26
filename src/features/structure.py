from __future__ import annotations
import re, numpy as np
TRANSITIONS={"however","therefore","moreover","furthermore","firstly","secondly","finally","because","although","however","consequently","in addition","for example","on the other hand"}

def structure_features(text:str)->dict[str,float]:
    paras=[p.strip() for p in re.split(r"\n\s*\n",text) if p.strip()]
    lens=[len(re.findall(r"\b[\w'’-]+\b",p)) for p in paras]
    trans=sum(text.lower().count(t) for t in TRANSITIONS)
    return {"paragraph_count_signal":float(len(paras)),"avg_paragraph_length":float(np.mean(lens)) if lens else 0.0,"paragraph_length_std":float(np.std(lens)) if lens else 0.0,"first_paragraph_length":float(lens[0]) if lens else 0.0,"final_paragraph_length":float(lens[-1]) if lens else 0.0,"transition_word_frequency":float(trans)}
