# Evaluation

Primary metric: Quadratic Weighted Kappa (QWK). Secondary metrics: MAE, RMSE, Pearson correlation, Spearman correlation, exact agreement, and agreement within one score point.

Continuous predictions remain available for useful displays such as `4.72 / 6`. For QWK, predictions are rounded to the nearest integer and clipped to 1–6.

If a valid prompt/group field is available, grouped splitting is preferred. With the documented AES 2.0 schema lacking prompt metadata, the implemented fallback is a reproducible stratified split. This is a methodological limitation and not evidence of prompt-independent generalization.

Never hard-code evaluation metrics. `src/evaluation/evaluate.py` writes actual metrics after a trained model is evaluated on the locally generated test split.
