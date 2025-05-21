
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

class ChurnPredictor:
    def __init__(self):
        self.model = LogisticRegression(max_iter=200)
        self.scaler = StandardScaler()

    def train(self, df, features, target):
        X = df[features]
        y = df[target]
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)

    def predict(self, df):
        X_scaled = self.scaler.transform(df)
        return self.model.predict_proba(X_scaled)[:, 1]
