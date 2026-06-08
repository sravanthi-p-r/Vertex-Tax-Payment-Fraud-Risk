import pandas as pd
import numpy as np


def engineer_features(df):

    df["customer_txn_count"] = (
        df.groupby("customer_id")
          ["transaction_id"]
          .transform("count")
    )

    df["customer_avg_amount"] = (
        df.groupby("customer_id")
          ["amount"]
          .transform("mean")
    )

    df["amount_vs_customer_avg"] = (
        df["amount"]
        /
        df["customer_avg_amount"]
    )

    amount_threshold = (
        df["amount"]
        .quantile(0.95)
    )

    df["high_amount_flag"] = np.where(
        df["amount"] > amount_threshold,
        1,
        0
    )

    df["merchant_txn_count"] = (
        df.groupby("merchant_id")
          ["transaction_id"]
          .transform("count")
    )

    df["merchant_fraud_rate"] = (
        df.groupby("merchant_id")
          ["fraud_flag"]
          .transform("mean")
    )

    df["country_fraud_rate"] = (
        df.groupby("country")
          ["fraud_flag"]
          .transform("mean")
    )

    df["device_fraud_rate"] = (
        df.groupby("device_type")
          ["fraud_flag"]
          .transform("mean")
    )

    return df


if __name__ == "__main__":

    df = pd.read_csv(
        "../data/synthetic_transactions.csv"
    )

    df = engineer_features(df)

    df.to_csv(
        "../data/processed/transactions_features.csv",
        index=False
    )

    print(df.shape)
