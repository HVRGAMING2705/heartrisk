import json, numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.metrics import accuracy_score, roc_auc_score

rng = np.random.default_rng(42)
n = 900
age = rng.uniform(29, 77, n)
sex = rng.integers(0, 2, n).astype(float)          # 0 female, 1 male
rest_bp = rng.uniform(94, 200, n)
chol = rng.uniform(126, 564, n)
max_hr = rng.uniform(71, 202, n)
fast_bs = rng.integers(0, 2, n).astype(float)     # fasting blood sugar > 120 mg/dl
ex_ang = rng.integers(0, 2, n).astype(float)      # exercise-induced angina
oldpeak = rng.uniform(0, 6.2, n)                  # ST depression
# Generative risk logit: older age, male, high BP, high cholesterol,
# low max heart rate, high fasting sugar, exercise angina and high
# ST depression all raise heart-disease risk.
logit = (-5.8 + 0.045*age + 0.7*sex + 0.012*rest_bp + 0.004*chol
         - 0.022*max_hr + 0.6*fast_bs + 0.9*ex_ang + 0.7*oldpeak)
p = 1/(1+np.exp(-logit))
y = (rng.random(n) < p).astype(int)
X = np.column_stack([age, sex, rest_bp, chol, max_hr, fast_bs, ex_ang, oldpeak])
names = ["age","sex","resting_bp","cholesterol","max_hr","fasting_bs","exercise_angina","oldpeak"]
mu, sd = X.mean(0), X.std(0)
Xs = (X - mu)/sd
model = LogisticRegression(max_iter=1000, C=1.0).fit(Xs, y)
kf = StratifiedKFold(5, shuffle=True, random_state=42)
pred_cv = cross_val_predict(LogisticRegression(max_iter=1000, C=1.0), Xs, y, cv=kf)
proba_cv = cross_val_predict(LogisticRegression(max_iter=1000, C=1.0), Xs, y, cv=kf, method="predict_proba")[:,1]
acc = float(accuracy_score(y, pred_cv)); auc = float(roc_auc_score(y, proba_cv))
base = float(max(y.mean(), 1-y.mean()))
print(f"CV accuracy={acc:.3f} AUC={auc:.3f} disease_rate={y.mean():.3f} baseline={base:.3f}")
print("coef", model.coef_, "intercept", model.intercept_)
mj = {"features": names, "means": mu.tolist(), "stds": sd.tolist(),
      "coef": model.coef_[0].tolist(), "intercept": float(model.intercept_[0]),
      "metrics": {"cv_accuracy": acc, "cv_auc": auc, "disease_rate": float(y.mean()), "baseline_accuracy": base, "n": n}}
with open("model.json","w") as f: json.dump(mj, f, indent=1)
def predict(v):
    z = (np.array(v)-mu)/sd
    return float(1/(1+np.exp(-(model.intercept_[0] + z @ model.coef_[0]))))
samples = [[55,1,140,260,150,0,0,1.0],[63,1,160,320,120,1,1,2.5],[38,0,110,180,175,0,0,0.0],[70,1,180,380,100,1,1,3.5],[45,0,120,200,165,0,0,0.5]]
for s in samples: print(s, round(predict(s),4))
