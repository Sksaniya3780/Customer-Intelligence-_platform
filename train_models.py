import pandas as pd
import joblib
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

os.makedirs("models", exist_ok=True)

df=pd.read_csv("data/customers.csv")

X=df[
[
'income',
'spending_score',
'tenure',
'monthly_visits',
'purchase_frequency'
]
]

y=df['churn']

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model=RandomForestClassifier()

model.fit(X_train,y_train)

joblib.dump(
    model,
    "models/churn_model.pkl"
)

print("Model Saved Successfully")