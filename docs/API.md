# API

## GET /health
Returns service health, whether a trained model is loaded, and application version.

## GET /api/v1/model
Returns model name, version, dataset, score range and training status.

## POST /api/v1/score
Request:
```json
{"essay":"At least 50 characters of essay text..."}
```

Response contains score, estimated range, analytical dimensions, writing statistics, readability metrics, strengths, improvements, model information and measured request latency.

The service rejects empty/too-short/oversized essays through Pydantic validation.
