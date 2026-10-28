# HeartRisk — Heart Disease Risk Predictor

Logistic regression (scikit-learn) trained on 900 synthetic patient records:
age, sex, resting blood pressure, cholesterol, max heart rate, fasting blood
sugar, exercise-induced angina, ST depression (oldpeak).

- 5-fold CV accuracy: 75.1%, AUC: 0.83 (majority-class baseline: 50.3%)
- `train.py` trains the model and exports `model.json`
- `index.html` is a single-page demo: the same coefficients run in JavaScript,
  so the browser demo reproduces the Python model exactly — no backend needed.

For learning only — not medical advice.

Live demo: https://heartrisk-ten.vercel.app

By Vikranth Reddy — B.Tech CSE (AI & ML), Woxsen University.
