# Dataset

## Primary source
Learning Agency Lab — Automated Essay Scoring 2.0, Kaggle. The project specification identifies the documented fields as `essay_id`, `full_text`, and `score`, with a holistic 1–6 score.

Official source: https://www.kaggle.com/competitions/learning-agency-lab-automated-essay-scoring-2

## License
The supplied specification identifies the competition dataset as CC BY-NC 4.0. Follow the competition's current terms before downloading or using it. Do not commit or redistribute raw competition data in this repository.

## Download
Configure Kaggle CLI credentials, then run `python -m src.data.download`. Expected files include `train.csv`, `test.csv`, and `sample_submission.csv`.

## Schema
- `essay_id`: unique identifier
- `full_text`: student-written essay
- `score`: holistic score, 1–6

## Prompt metadata
The primary documented schema does not assume a prompt column. The split module uses `prompt_id` only if it is genuinely present; otherwise it uses a reproducible stratified split and documents the limitation.

## Privacy and intended use
Use the data for research, experimentation, NLP engineering, and educational analytics prototyping. Do not expose raw student essays in public reports or logs. Do not use the prototype as the sole basis for high-stakes educational decisions.
