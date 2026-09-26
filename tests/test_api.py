from fastapi.testclient import TestClient
from src.api.main import app
client=TestClient(app)

def test_health():
    r=client.get("/health"); assert r.status_code==200; assert r.json()["status"]=="healthy"

def test_model_info():
    r=client.get("/api/v1/model"); assert r.status_code==200; assert r.json()["score_range"]==[1,6]

def test_short_essay_rejected():
    r=client.post("/api/v1/score",json={"essay":"too short"}); assert r.status_code==422
