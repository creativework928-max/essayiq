from __future__ import annotations

from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT = Path(__file__).resolve().parents[1]

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    random_seed: int = 42
    min_essay_chars: int = 50
    max_essay_chars: int = 50000
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    model_name: str = "essayiq-hybrid"
    model_version: str = "1.0.0"
    log_level: str = "INFO"
    cors_origins: str = "http://localhost:5173,http://127.0.0.1:5173"
    train_file: Path = ROOT / "data/raw/train.csv"
    model_file: Path = ROOT / "models/hybrid/essayiq_hybrid.joblib"
    metadata_file: Path = ROOT / "models/metadata/model_metadata.json"
    reports_dir: Path = ROOT / "reports"
    min_score: float = 1.0
    max_score: float = 6.0
    max_tfidf_features: int = 120000

settings = Settings()

def ensure_directories() -> None:
    for p in [ROOT / "data/raw", ROOT / "data/interim", ROOT / "data/processed", ROOT / "data/external", ROOT / "models/baseline", ROOT / "models/tfidf", ROOT / "models/hybrid", ROOT / "models/metadata", ROOT / "reports/figures", ROOT / "reports/metrics", ROOT / "reports/data_quality"]:
        p.mkdir(parents=True, exist_ok=True)
