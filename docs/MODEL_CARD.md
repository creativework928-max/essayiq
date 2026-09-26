# Model Card

## Model overview
EssayIQ Hybrid combines word/character TF-IDF with measurable linguistic, readability, vocabulary, grammar-signal, structural and lightweight semantic features and a Ridge regression head.

## Intended use
Research prototypes, educational writing analytics, model experimentation and portfolio demonstration.

## Non-intended use
Automated high-stakes grading, disciplinary decisions, admissions decisions, or claims about a student's intelligence or ability.

## Training data
Learning Agency Lab AES 2.0 as obtained under its applicable terms.

## Limitations
The primary target is holistic scoring; analytical dimensions are derived indicators. The benchmark represents a particular assessment context. Grammar and semantic modules are signals, not perfect linguistic judgments.

## Fairness
No sensitive demographic attributes should be inferred from writing style. If legitimate labeled subgroup variables are available in a future study, evaluate QWK/MAE/RMSE separately. Otherwise subgroup fairness cannot be established.

## Human oversight
Every educational use should preserve human review and student agency.
