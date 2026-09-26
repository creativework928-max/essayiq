from __future__ import annotations
import re, numpy as np

def semantic_features(text:str,prompt:str|None=None)->dict[str,float]:
    sents=[s.strip() for s in re.split(r"(?<=[.!?])\s+",text) if s.strip()]
    # Optional lightweight lexical coherence proxy; embedding models can replace this module later.
    sims=[]
    for a,b in zip(sents,sents[1:]):
        A=set(re.findall(r"\b[a-zA-Z]{4,}\b",a.lower())); B=set(re.findall(r"\b[a-zA-Z]{4,}\b",b.lower()))
        sims.append(len(A&B)/len(A|B) if A|B else 0.0)
    prompt_sim=0.0
    if prompt:
        A=set(re.findall(r"\b[a-zA-Z]{4,}\b",prompt.lower())); B=set(re.findall(r"\b[a-zA-Z]{4,}\b",text.lower())); prompt_sim=len(A&B)/len(A|B) if A|B else 0.0
    return {"sentence_coherence_proxy":float(np.mean(sims)) if sims else 0.0,"paragraph_coherence_proxy":float(np.mean(sims)) if sims else 0.0,"prompt_similarity_proxy":float(prompt_sim)}
