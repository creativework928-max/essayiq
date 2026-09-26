from __future__ import annotations
from fastapi import APIRouter,HTTPException
from src.api.schemas import EssayRequest
from src.config import settings
from src.services.model_service import ModelService
from src.services.scoring_service import ScoringService
router=APIRouter()
model_service=ModelService(); model_service.load(); scorer=ScoringService(model_service)

@router.get("/health")
def health(): return {"status":"healthy","model_loaded":model_service.loaded,"version":settings.model_version}

@router.get("/api/v1/model")
def model_info(): return {"model_name":settings.model_name,"version":settings.model_version,"dataset":"Learning Agency Lab AES 2.0","score_range":[1,6],"trained":model_service.loaded}

@router.post("/api/v1/score")
def score(request:EssayRequest):
    try:return scorer.score(request.essay)
    except Exception as exc: raise HTTPException(status_code=500,detail={"code":"SCORING_ERROR","message":str(exc)}) from exc
