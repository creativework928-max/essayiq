PYTHON ?= python

setup:
	$(PYTHON) -m pip install -r requirements.txt

data:
	$(PYTHON) -m src.data.download
validate:
	$(PYTHON) -m src.data.validate
train:
	$(PYTHON) -m src.models.train
evaluate:
	$(PYTHON) -m src.evaluation.evaluate
test:
	pytest -q
api:
	uvicorn src.api.main:app --reload
frontend:
	cd frontend && npm install && npm run dev
