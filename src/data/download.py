from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from src.config import ensure_directories, settings

COMPETITION = "learning-agency-lab-automated-essay-scoring-2"

def main() -> None:
    ensure_directories()
    target = settings.train_file.parent
    target.mkdir(parents=True, exist_ok=True)
    kaggle = shutil.which("kaggle")
    if not kaggle:
        raise RuntimeError("Kaggle CLI not found. Install requirements and configure Kaggle credentials.")
    cmd = [kaggle, "competitions", "download", "-c", COMPETITION, "-p", str(target)]
    subprocess.run(cmd, check=True)
    archives = list(target.glob("*.zip"))
    if archives:
        import zipfile
        with zipfile.ZipFile(archives[0]) as zf:
            zf.extractall(target)
    expected = target / "train.csv"
    if not expected.exists():
        raise FileNotFoundError("Download completed but train.csv was not found in data/raw/. Check Kaggle access and archive contents.")
    print(f"Dataset available at {expected}")

if __name__ == "__main__":
    main()
