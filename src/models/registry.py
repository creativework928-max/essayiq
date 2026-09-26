from __future__ import annotations
import json
from datetime import datetime,timezone
from pathlib import Path

def write_metadata(path:Path,**kwargs):
    path.parent.mkdir(parents=True,exist_ok=True); data={"created_at":datetime.now(timezone.utc).isoformat(),**kwargs}; path.write_text(json.dumps(data,indent=2),encoding="utf8"); return data

def read_metadata(path:Path):
    if not path.exists(): return None
    return json.loads(path.read_text(encoding="utf8"))
