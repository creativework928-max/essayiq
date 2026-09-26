from __future__ import annotations
from pydantic import BaseModel,Field
class EssayRequest(BaseModel):
    essay:str=Field(...,min_length=50,max_length=50000)
class ScoreResponse(BaseModel):
    score:dict; uncertainty:dict; dimensions:dict; statistics:dict; readability:dict; strengths:list[str]; improvements:list[str]; model:dict; latency_ms:float
