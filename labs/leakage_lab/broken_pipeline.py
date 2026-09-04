from __future__ import annotations

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def run(path: str = "dataset.csv") -> float:
    data = pd.read_csv(path)
    # Deliberate defect: future_outcome leaks the answer into the features.
    X = data[["age", "usage", "future_outcome"]]
    y = data["target"]
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.25, random_state=42)
    model = LogisticRegression(max_iter=1000).fit(X_train, y_train)
    return float(accuracy_score(y_valid, model.predict(X_valid)))


if __name__ == "__main__":
    print(run())
