import pandas as pd

from sklearn.model_selection import (
    train_test_split
)

from sklearn.ensemble import (
    RandomForestClassifier
)

from sklearn.metrics import (
    roc_auc_score,
    classification_report
)


FEATURES = [

    "amount",

    "risk_score",

    "customer_txn_count",

    "amount_vs_customer_avg",

    "merchant_fraud_rate",

    "country_fraud_rate",

    "device_fraud_rate",

    "high_amount_flag"

]


def train_model(df):

    X = df[FEATURES]

    y = df["fraud_flag"]

    X_train, X_test, y_train, y_test = train_test_split(

        X,
        y,

        test_size=0.20,

        random_state=42,

        stratify=y
    )

    model = RandomForestClassifier(

        n_estimators=200,

        random_state=42,

        n_jobs=-1
    )

    model.fit(
        X_train,
        y_train
    )

    probabilities = model.predict_proba(
        X_test
    )[:, 1]

    predictions = model.predict(
        X_test
    )

    auc = roc_auc_score(
        y_test,
        probabilities
    )

    print(
        "ROC-AUC:",
        round(auc, 4)
    )

    print(
        classification_report(
            y_test,
            predictions
        )
    )

    results = X_test.copy()

    results["actual_fraud"] = y_test

    results["fraud_probability"] = probabilities

    return model, results


if __name__ == "__main__":

    df = pd.read_csv(
        "../data/processed/transactions_features.csv"
    )

    model, results = train_model(df)

    results.to_csv(
        "../outputs/model_results/model_predictions.csv",
        index=False
    )
