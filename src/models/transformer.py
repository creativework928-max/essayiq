"""Optional transformer training helpers. Kept separate from the CPU production path."""
from __future__ import annotations

def transformer_dependencies_available()->bool:
    try:
        import torch, transformers, datasets
        return True
    except ImportError:
        return False

def build_transformer_config(model_name="distilbert-base-uncased"):
    return {"model_name":model_name,"task":"regression","long_document_strategy":"chunk_and_aggregate","status":"optional"}
