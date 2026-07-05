"""
Project 3 — Customer Churn Analysis & Prediction
Author: Khattab Salim
Reads customer_churn.csv, explores churn drivers, and trains a logistic
regression model to predict churn (evaluated with ROC-AUC).
"""
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, classification_report

df = pd.read_csv("../data/customer_churn.csv")
print("Overall churn rate: {:.1f}%".format(df.churned.mean() * 100))

# --- Exploratory: churn by contract & tenure ---
print("\nChurn by contract:\n",
      df.groupby("contract").churned.mean().mul(100).round(1))
df["tenure_grp"] = pd.cut(df.tenure_months, [0, 12, 24, 48, 72],
                          labels=["0-12", "13-24", "25-48", "49-72"])
print("\nChurn by tenure group:\n",
      df.groupby("tenure_grp", observed=True).churned.mean().mul(100).round(1))

# --- Model ---
X = pd.get_dummies(
    df[["tenure_months", "monthly_charges", "contract",
        "support_calls", "payment_method"]], drop_first=True)
y = df.churned
Xtr, Xte, ytr, yte = train_test_split(
    X, y, test_size=0.25, random_state=1, stratify=y)

scaler = StandardScaler()
Xtr_s, Xte_s = scaler.fit_transform(Xtr), scaler.transform(Xte)

clf = LogisticRegression(max_iter=1000).fit(Xtr_s, ytr)
proba = clf.predict_proba(Xte_s)[:, 1]
print("\nROC-AUC: {:.3f}".format(roc_auc_score(yte, proba)))
print("\n", classification_report(yte, clf.predict(Xte_s)))

# --- Churn drivers (coefficients) ---
drivers = pd.Series(clf.coef_[0], index=X.columns).sort_values(ascending=False)
print("Churn drivers (positive = increases churn):\n", drivers.round(3))
