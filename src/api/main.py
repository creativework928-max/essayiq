from __future__ import annotations
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import router
from src.config import settings
from src.utils.logging import configure_logging
configure_logging()
app=FastAPI(title="EssayIQ API",version=settings.model_version,description="Automated essay scoring and writing analytics API.")
origins=[x.strip() for x in settings.cors_origins.split(",") if x.strip()]
app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=False,allow_methods=["GET","POST"],allow_headers=["*"])
app.include_router(router)
