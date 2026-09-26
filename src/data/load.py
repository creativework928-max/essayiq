from __future__ import annotations
from pathlib import Path
import pandas as pd
from src.config import settings
REQUIRED_TRAIN_COLUMNS = {"essay_id", "full_text", "score"}

def load_training_data(path: Path | None = None) -> pd.DataFrame:
    csv_path = path or settings.train_file
    if not csv_path.exists():
        raise FileNotFoundError(f"Training dataset not found: {csv_path}. Run `python -m src.data.download` first.")
    df = pd.read_csv(csv_path)
    missing = REQUIRED_TRAIN_COLUMNS.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    return df
